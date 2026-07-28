#!/usr/bin/env python3
"""
PMS-STRATA Reader — experimental executable presentation layer.

Δ ∇ □ Λ Α Ω Θ Φ Χ Σ Ψ

A single-file, dependency-free desktop reader for the PMS-STRATA repository.

Prototype features:
- Loads the active PMS-STRATA corpus from a folder or a .zip file.
- Excludes ``_workfiles/**`` from normal ingestion.
- Navigates Markdown, YAML, JSON, CSV, and reader source files.
- Provides corpus-wide full-text search and heading navigation.
- Parses the 59 transformation records into lightweight record summaries.
- Includes an interactive Graph Lab with:
  * a rotatable/zoomable 3D case tree,
  * Authority Graph,
  * Dependency Graph,
  * Transformation Flow,
  * selected Record Trace,
  * selected Chain Graph.

The graph layer only visualizes declared repository relations. It does not
create theory, evidence, classifications, dependencies, or authority.

Run:
    python pms_strata_reader.py
    python pms_strata_reader.py /path/to/16. PMS-STRATA
    python pms_strata_reader.py /path/to/PMS-STRATA.zip
    python pms_strata_reader.py --self-test /path/to/PMS-STRATA.zip

Tkinter is part of Python's standard library, but some Linux distributions
package it separately as ``python3-tk``.
"""

from __future__ import annotations

import bisect
import csv
import json
import math
import posixpath
import queue
import re
import sys
import threading
import time
import webbrowser
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import unquote, urlparse

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    import tkinter.font as tkfont
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Tkinter is not available. Install the Tk bindings for your Python "
        "distribution, for example: sudo apt install python3-tk"
    ) from exc

APP_TITLE = "PMS-STRATA Reader"
APP_VERSION = "0.5.3-rendered-details"

DEBUG = True  # set False to silence console output


def dbg(msg: str) -> None:
    if DEBUG:
        ts = time.strftime("%H:%M:%S")
        print(f"[{ts}] {msg}", flush=True)


SECTION_ORDER: List[str] = [
    "README.md",
    "00_source",
    "01_blocks",
    "02_appendices",
    "03_cases",
    "04_reference",
    "05_minified",
    "06_derivative_publications",
    "07_model",
    "08_PMS-STRATA Reader",
]

SECTION_LABELS: Dict[str, str] = {
    "README.md": "Start",
    "00_source": "Structure",
    "01_blocks": "Canonical Corpus",
    "02_appendices": "Appendices",
    "03_cases": "Cases and Records",
    "04_reference": "Reference Kernel",
    "05_minified": "Minified Controls",
    "06_derivative_publications": "Derivative Publications",
    "07_model": "Formal Model",
    "08_PMS-STRATA Reader": "Reader",
}

CANONICAL_BLOCK_LABELS: Dict[str, str] = {
    "README.md": "README",
    "01_blocks/00_front_matter.md": "Front Matter",
    "01_blocks/01_foundations.md": "Foundations",
    "01_blocks/02_part_i_path.md": "PATH",
    "01_blocks/03_part_ii_sub.md": "SUB",
    "01_blocks/04_part_iii_retype.md": "RETYPE",
    "01_blocks/05_part_iv_limits.md": "LIMITS",
    "01_blocks/06_conclusion.md": "Conclusion",
}

# Graph Lab's browser is deliberately narrower than the general Reader tree.
# It lists only audit- and graph-relevant artifacts that the Reader can render.
GRAPH_BROWSER_SECTIONS = {
    "01_blocks",
    "02_appendices",
    "03_cases",
    "04_reference",
    "05_minified",
    "07_model",
}
GRAPH_BROWSER_FILE_TYPES = {"md", "yaml", "yml", "json", "csv", "txt"}

ACTIVE_TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".json", ".csv", ".txt", ".py"}
EXCLUDED_TOP_LEVEL = {"_workfiles", ".git", "__pycache__"}

PREFERRED_HOME_FILES = [
    "README.md",
    "01_blocks/00_front_matter.md",
    "04_reference/Reader_Pathways.md",
    "05_minified/PMS_STRATA_Minified_Canonical.md",
]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)\s*([A-Za-z0-9_-]+)?(?:\s+.*)?\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+])\s+(.+?)\s*$")
ORDERED_LIST_RE = re.compile(r"^(\s*)(\d+)[.)]\s+(.+?)\s*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WORD_RE = re.compile(r"\b\w+\b", re.UNICODE)
YAML_KEY_RE = re.compile(r"^(\s*)([^#\s][^:]*?):(?:\s*(.*))?$")
YAML_OUTLINE_KEY_RE = re.compile(r"^(\s*)(-\s+)?([A-Za-z0-9_.-]+)\s*:\s*(.*?)\s*$")
HTML_ANCHOR_RE = re.compile(
    r'^\s*<a\s+(?:name|id)=["\']([^"\']+)["\']\s*></a>\s*$',
    re.IGNORECASE,
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

# Above this threshold the renderer avoids per-line source marks.
LARGE_DOC_LINE_THRESHOLD = 8000

# Audit-support rendering thresholds. Large source artifacts stay unchanged;
# only their presentation is prepared and inserted in seamless chunks.
CHUNKED_RENDER_LINE_THRESHOLD = 10_000
CHUNKED_RENDER_BYTE_THRESHOLD = 1_048_576
CHUNK_TARGET_BYTES = 192 * 1024
MAX_SEARCH_HIGHLIGHTS = 2_000

YAML_OUTLINE_LEVEL3_KEYS = {
    "claim",
    "statement",
    "claim_type",
    "source",
    "target",
    "reference_object",
    "operation",
    "kind",
    "admissibility",
    "audit_stages",
    "result",
    "routing",
    "loss",
    "governance",
    "selected_class",
    "failure_condition",
    "stop_condition",
    "non_capture_condition",
}

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    line_number: int
    anchor: str


@dataclass
class Document:
    rel_path: str
    title: str
    text: str
    file_type: str
    headings: List[Heading] = field(default_factory=list)
    frontmatter: Dict[str, str] = field(default_factory=dict)
    _line_count: int = field(init=False, repr=False)
    _word_count: int = field(init=False, repr=False)
    _byte_count: int = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._line_count = self.text.count("\n") + (
            1 if self.text and not self.text.endswith("\n") else 0
        )
        self._word_count = len(WORD_RE.findall(self.text))
        self._byte_count = len(self.text.encode("utf-8", errors="replace"))

    @property
    def line_count(self) -> int:
        return self._line_count

    @property
    def word_count(self) -> int:
        return self._word_count

    @property
    def byte_count(self) -> int:
        return self._byte_count


@dataclass(frozen=True)
class RenderChunk:
    text: str
    start_line: int


@dataclass
class RecordSummary:
    case_id: str
    title: str
    record_id: str
    yaml_path: str
    markdown_path: str = ""
    package_path: str = ""
    operation: str = "UNKNOWN"
    output_class: str = "unrouted"
    case_class: str = ""
    chapter_owner: str = ""
    claim: str = ""
    source_id: str = ""
    source_description: str = ""
    target_id: str = ""
    target_description: str = ""
    chain_id: str = ""
    previous_occurrence_id: str = ""
    next_occurrence_id: str = ""


@dataclass
class GraphNode:
    node_id: str
    label: str
    kind: str
    x: float
    y: float
    z: float
    rel_path: str = ""
    details: str = ""
    record_id: str = ""


class CorpusError(RuntimeError):
    """Raised when a PMS-STRATA corpus cannot be loaded."""


# ---------------------------------------------------------------------------
# Corpus source (folder or zip)
# ---------------------------------------------------------------------------

class CorpusSource:
    """Reads active PMS-STRATA text artifacts from a folder or a zip file."""

    def __init__(self, source_path: Path):
        self.source_path = source_path.expanduser().resolve()
        dbg(f"CorpusSource: resolving {self.source_path}")
        self.kind: str = "folder" if self.source_path.is_dir() else "zip"
        self._zip: Optional[zipfile.ZipFile] = None
        self._zip_prefix = ""
        self.root_dir: Optional[Path] = None

        if self.source_path.is_dir():
            self.root_dir = self._detect_folder_root(self.source_path)
            dbg(f"CorpusSource: folder root = {self.root_dir}")
        elif self.source_path.is_file() and self.source_path.suffix.lower() == ".zip":
            self._zip = zipfile.ZipFile(self.source_path)
            self._zip_prefix = self._detect_zip_prefix(self._zip)
            dbg(f"CorpusSource: zip prefix = '{self._zip_prefix}'")
        else:
            raise CorpusError(f"Unsupported source: {self.source_path}")

    def close(self) -> None:
        if self._zip is not None:
            self._zip.close()

    def describe(self) -> str:
        if self.kind == "folder" and self.root_dir is not None:
            return str(self.root_dir)
        return str(self.source_path)

    @staticmethod
    def _active_rel_path(rel_path: str) -> bool:
        rel_path = normalize_rel_path(rel_path)
        if not rel_path or rel_path.endswith("/"):
            return False
        first = rel_path.split("/", 1)[0]
        if first in EXCLUDED_TOP_LEVEL:
            return False
        return Path(rel_path).suffix.lower() in ACTIVE_TEXT_EXTENSIONS

    def exists(self, rel_path: str) -> bool:
        rel_path = normalize_rel_path(rel_path)
        if not self._active_rel_path(rel_path):
            return False
        if self.kind == "folder":
            assert self.root_dir is not None
            return (self.root_dir / rel_path).is_file()
        assert self._zip is not None
        return self._zip_name(rel_path) in self._zip.namelist()

    def read_text(self, rel_path: str) -> str:
        rel_path = normalize_rel_path(rel_path)
        if self.kind == "folder":
            assert self.root_dir is not None
            return (self.root_dir / rel_path).read_text(encoding="utf-8", errors="replace")
        assert self._zip is not None
        with self._zip.open(self._zip_name(rel_path), "r") as handle:
            raw = handle.read()
        return raw.decode("utf-8", errors="replace")

    def available_files(self) -> List[str]:
        if self.kind == "folder":
            assert self.root_dir is not None
            paths = [
                path.relative_to(self.root_dir).as_posix()
                for path in self.root_dir.rglob("*")
                if path.is_file()
            ]
        else:
            assert self._zip is not None
            paths = []
            for name in self._zip.namelist():
                if self._zip_prefix and not name.startswith(self._zip_prefix):
                    continue
                rel = name[len(self._zip_prefix):] if self._zip_prefix else name
                paths.append(rel)

        active = [normalize_rel_path(p) for p in paths if self._active_rel_path(p)]
        result = sorted(set(active), key=corpus_sort_key)
        dbg(f"CorpusSource.available_files: {len(result)} active text artifacts found")
        return result

    def _zip_name(self, rel_path: str) -> str:
        rel_path = normalize_rel_path(rel_path)
        return f"{self._zip_prefix}{rel_path}" if self._zip_prefix else rel_path

    @staticmethod
    def _looks_like_root(candidate: Path) -> bool:
        return (
            (candidate / "README.md").is_file()
            and (candidate / "00_source").is_dir()
            and (candidate / "01_blocks").is_dir()
            and (candidate / "07_model").is_dir()
        )

    @classmethod
    def _detect_folder_root(cls, path: Path) -> Path:
        candidates = [
            path,
            path / "16. PMS-STRATA",
            path / "PMS-STRATA",
        ]
        try:
            candidates.extend(child for child in path.iterdir() if child.is_dir())
        except OSError:
            pass

        seen = set()
        for candidate in candidates:
            try:
                resolved = candidate.resolve()
            except OSError:
                continue
            if resolved in seen:
                continue
            seen.add(resolved)
            valid = cls._looks_like_root(resolved)
            dbg(f"  _detect_folder_root: {resolved} valid={valid}")
            if valid:
                return resolved
        raise CorpusError(
            "Could not find a PMS-STRATA project root. Select the folder that "
            "contains README.md, 00_source/, 01_blocks/, and 07_model/."
        )

    @staticmethod
    def _detect_zip_prefix(zf: zipfile.ZipFile) -> str:
        names = zf.namelist()
        name_set = set(names)
        readmes = [name for name in names if name.endswith("README.md")]
        for readme in sorted(readmes, key=lambda value: value.count("/")):
            prefix = readme[:-len("README.md")]
            has_blocks = any(name.startswith(prefix + "01_blocks/") for name in names)
            has_model = any(name.startswith(prefix + "07_model/") for name in names)
            has_source = any(name.startswith(prefix + "00_source/") for name in names)
            if has_blocks and has_model and has_source:
                return prefix
        raise CorpusError(
            "Could not find a PMS-STRATA project root inside the zip file. "
            "Expected README.md, 00_source/, 01_blocks/, and 07_model/."
        )


# ---------------------------------------------------------------------------
# Corpus (collection of loaded documents)
# ---------------------------------------------------------------------------

class Corpus:
    """Loaded active PMS-STRATA artifacts plus record and graph helpers."""

    def __init__(self, source: CorpusSource):
        self.source = source
        self.documents: Dict[str, Document] = {}
        self.ordered_paths: List[str] = []
        self.records: List[RecordSummary] = []
        self.record_by_yaml: Dict[str, RecordSummary] = {}
        self.record_by_markdown: Dict[str, RecordSummary] = {}
        self.record_by_id: Dict[str, RecordSummary] = {}
        self.load()

    def load(self) -> None:
        self.documents.clear()
        self.records.clear()
        self.record_by_yaml.clear()
        self.record_by_markdown.clear()
        self.record_by_id.clear()
        self.ordered_paths = self.source.available_files()
        dbg(f"Corpus.load: loading {len(self.ordered_paths)} artifacts ...")

        for rel_path in self.ordered_paths:
            text = self.source.read_text(rel_path)
            suffix = Path(rel_path).suffix.lower().lstrip(".") or "text"
            if suffix == "md":
                frontmatter, body = parse_frontmatter(text)
                headings = parse_headings(body)
                title = frontmatter.get("title") or first_heading_title(headings) or prettify_file_name(rel_path)
            elif suffix in {"yaml", "yml"}:
                frontmatter = {}
                headings = parse_yaml_outline(text)
                title = prettify_file_name(rel_path)
            else:
                frontmatter = {}
                headings = []
                title = prettify_file_name(rel_path)
            self.documents[rel_path] = Document(
                rel_path=rel_path,
                title=title,
                text=text,
                file_type=suffix,
                headings=headings,
                frontmatter=frontmatter,
            )

        self._load_record_summaries()
        dbg(
            f"Corpus.load: done — {len(self.documents)} artifacts, "
            f"{len(self.records)} transformation records"
        )

    def _load_record_summaries(self) -> None:
        index_entries: Dict[str, Dict[str, str]] = {}
        index_path = "03_cases/Case_Index.yaml"
        if index_path in self.documents:
            index_entries = parse_case_index(self.documents[index_path].text)

        for rel_path in self.ordered_paths:
            if not (rel_path.startswith("03_cases/yaml/") and rel_path.endswith(".yaml")):
                continue
            flat = flatten_yaml_scalars(self.documents[rel_path].text)
            stem = Path(rel_path).stem
            case_id = stem.split("_", 1)[0]
            meta = index_entries.get(case_id, {})

            operation = scalar_from_flat(flat, [
                ("operation", "kind"),
                ("operation", "operation_type"),
            ], "UNKNOWN")
            selected = scalar_by_leaf(flat, "selected_class") or meta.get("canonical_output_mapping", "unrouted")
            claim = scalar_from_flat(flat, [("claim", "statement")], "")
            source_id = scalar_from_flat(flat, [("source", "reference_object", "object_id")], "")
            source_desc = scalar_from_flat(flat, [("source", "reference_object", "description")], "")
            target_id = scalar_from_flat(flat, [("target", "reference_object", "object_id")], "")
            target_desc = scalar_from_flat(flat, [("target", "reference_object", "description")], "")
            record_id = flat.get(("record_id",), stem)
            chain_id = scalar_from_flat(flat, [("relations", "chain_id")], "")
            previous = scalar_from_flat(flat, [("relations", "previous_occurrence_id")], "")
            next_occurrence = scalar_from_flat(flat, [("relations", "next_occurrence_id")], "")

            markdown_path = meta.get("markdown_artifact") or f"03_cases/markdown/{stem}.md"
            if markdown_path not in self.documents:
                markdown_path = ""
            package_path = meta.get("package_markdown_artifact", "")
            if package_path and package_path not in self.documents:
                package_path = ""

            record = RecordSummary(
                case_id=case_id,
                title=meta.get("title") or prettify_file_name(stem),
                record_id=record_id,
                yaml_path=rel_path,
                markdown_path=markdown_path,
                package_path=package_path,
                operation=operation,
                output_class=selected,
                case_class=meta.get("case_class", ""),
                chapter_owner=meta.get("chapter_owner", ""),
                claim=claim,
                source_id=source_id,
                source_description=source_desc,
                target_id=target_id,
                target_description=target_desc,
                chain_id=chain_id,
                previous_occurrence_id=previous,
                next_occurrence_id=next_occurrence,
            )
            self.records.append(record)
            self.record_by_yaml[rel_path] = record
            if markdown_path:
                self.record_by_markdown[markdown_path] = record
            self.record_by_id[record_id] = record

        self.records.sort(key=lambda record: natural_sort_key(record.case_id))

    def get(self, rel_path: str) -> Document:
        return self.documents[rel_path]

    def search(self, query: str, limit: int = 500) -> List[Tuple[str, int, str]]:
        query_norm = query.strip().lower()
        if not query_norm:
            return []
        results: List[Tuple[str, int, str]] = []
        for rel_path in self.ordered_paths:
            doc = self.documents[rel_path]
            for line_no, line in enumerate(strip_frontmatter(doc.text).splitlines(), start=1):
                if query_norm in line.lower():
                    snippet = line.strip() or "<blank line>"
                    results.append((rel_path, line_no, snippet[:300]))
                    if len(results) >= limit:
                        return results
        return results

    def record_for_path(self, rel_path: Optional[str]) -> Optional[RecordSummary]:
        if not rel_path:
            return None
        return self.record_by_yaml.get(rel_path) or self.record_by_markdown.get(rel_path)

    def records_for_chain(self, record: RecordSummary) -> List[RecordSummary]:
        # Prefer the shared package narrative: it can preserve explicit failure or
        # countercase records that sit beside, rather than inside, one chain_id.
        if record.package_path:
            members = [item for item in self.records if item.package_path == record.package_path]
            if members:
                return self._order_chain_members(members)
        if record.chain_id:
            members = [item for item in self.records if item.chain_id == record.chain_id]
            if members:
                return self._order_chain_members(members)
        prefix = re.sub(r"[A-Z]$", "", record.case_id)
        members = [item for item in self.records if item.case_id.startswith(prefix)]
        return self._order_chain_members(members or [record])

    @staticmethod
    def _order_chain_members(records: List[RecordSummary]) -> List[RecordSummary]:
        by_occurrence = {record.record_id: record for record in records}
        starters = [record for record in records if not record.previous_occurrence_id]
        ordered: List[RecordSummary] = []
        current = starters[0] if starters else None
        seen = set()
        while current and current.record_id not in seen:
            ordered.append(current)
            seen.add(current.record_id)
            next_record = None
            if current.next_occurrence_id:
                next_record = by_occurrence.get(current.next_occurrence_id)
                if next_record is None:
                    for candidate in records:
                        if current.next_occurrence_id in {candidate.record_id, candidate.case_id}:
                            next_record = candidate
                            break
            current = next_record
        ordered.extend(sorted((r for r in records if r.record_id not in seen), key=lambda r: natural_sort_key(r.case_id)))
        return ordered

    @property
    def document_count(self) -> int:
        return len(self.documents)

    @property
    def total_word_count(self) -> int:
        return sum(doc.word_count for doc in self.documents.values())

    @property
    def total_line_count(self) -> int:
        return sum(doc.line_count for doc in self.documents.values())


class AutoHideScrollbar(ttk.Scrollbar):
    """A grid-managed scrollbar that disappears when the full range is visible."""

    def __init__(self, master: tk.Misc, **kwargs):
        super().__init__(master, **kwargs)
        self.visibility_callback = None
        self._is_visible: Optional[bool] = None

    def set(self, first: str, last: str) -> None:
        try:
            fully_visible = float(first) <= 0.0 and float(last) >= 0.999999
        except (TypeError, ValueError):
            fully_visible = False
        visible = not fully_visible
        if visible:
            self.grid()
        else:
            self.grid_remove()
        super().set(first, last)
        if visible != self._is_visible:
            self._is_visible = visible
            callback = self.visibility_callback
            if callback is not None:
                self.after_idle(lambda: callback(visible))


class BrowseFilesDialog(tk.Toplevel):
    """Searchable, category-aware browser for active Reader artifacts."""

    def __init__(self, graph_lab: "GraphLab"):
        super().__init__(graph_lab)
        self.graph_lab = graph_lab
        self.app = graph_lab.app
        self.title(f"{APP_TITLE} — Browse Files")
        self.geometry("980x680")
        self.minsize(720, 480)
        self.transient(graph_lab)
        self.protocol("WM_DELETE_WINDOW", self.withdraw)

        self.query_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self._category_items: Dict[str, str] = {}
        self._row_to_path: Dict[str, str] = {}
        self._selected_section = "ALL"

        self._build_ui()
        self.apply_theme()
        self._populate_categories()
        self.refresh_files()
        self.after_idle(self._center_over_parent)

    def _build_ui(self) -> None:
        top = ttk.Frame(self, padding=(10, 10, 10, 6))
        top.pack(fill=tk.X)
        ttk.Label(top, text="Search active files").pack(side=tk.LEFT)
        self.search_entry = ttk.Entry(top, textvariable=self.query_var, width=44)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(8, 8))
        self.search_entry.bind("<KeyRelease>", lambda event: self.refresh_files())
        ttk.Button(top, text="Clear", command=self._clear_search).pack(side=tk.LEFT)
        ttk.Button(top, text="Close", command=self.withdraw).pack(side=tk.RIGHT, padx=(8, 0))

        pane = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        pane.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 6))

        categories_frame = ttk.Frame(pane, padding=(0, 0, 8, 0))
        files_frame = ttk.Frame(pane)
        pane.add(categories_frame, weight=1)
        pane.add(files_frame, weight=4)

        ttk.Label(categories_frame, text="Categories", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        self.categories = ttk.Treeview(categories_frame, show="tree", selectmode="browse", style="Browser.Treeview")
        cat_scroll = ttk.Scrollbar(categories_frame, orient=tk.VERTICAL, command=self.categories.yview)
        self.categories.configure(yscrollcommand=cat_scroll.set)
        self.categories.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        cat_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.categories.bind("<<TreeviewSelect>>", self._on_category_selected)

        ttk.Label(files_frame, text="Graph-relevant files", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        table_wrap = ttk.Frame(files_frame)
        table_wrap.pack(fill=tk.BOTH, expand=True)
        self.files = ttk.Treeview(
            table_wrap,
            columns=("title", "path", "type"),
            show="headings",
            selectmode="browse",
            style="Browser.Treeview",
        )
        self.files.heading("title", text="Title")
        self.files.heading("path", text="Repository path")
        self.files.heading("type", text="Type")
        self.files.column("title", width=250, minwidth=140, stretch=True)
        self.files.column("path", width=470, minwidth=220, stretch=True)
        self.files.column("type", width=70, minwidth=55, stretch=False, anchor=tk.CENTER)
        yscroll = ttk.Scrollbar(table_wrap, orient=tk.VERTICAL, command=self.files.yview)
        xscroll = AutoHideScrollbar(table_wrap, orient=tk.HORIZONTAL, command=self.files.xview)
        self.files.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        self.files.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll.grid(row=1, column=0, sticky="ew")
        table_wrap.rowconfigure(0, weight=1)
        table_wrap.columnconfigure(0, weight=1)
        self.files.bind("<Double-1>", lambda event: self.open_selected())
        self.files.bind("<Return>", lambda event: self.open_selected())

        bottom = ttk.Frame(self, padding=(10, 4, 10, 10))
        bottom.pack(fill=tk.X)
        ttk.Label(bottom, textvariable=self.status_var, style="Status.TLabel").pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(bottom, text="Open", command=self.open_selected).pack(side=tk.RIGHT)

        for widget in (self.categories, self.files):
            widget.configure(cursor="hand2")
        self.search_entry.configure(cursor="xterm")

    def _populate_categories(self) -> None:
        self.categories.delete(*self.categories.get_children())
        self._category_items.clear()
        self._selected_section = "ALL"
        all_item = self.categories.insert("", tk.END, text="All Files", open=True)
        self._category_items[all_item] = "ALL"
        corpus = self.app.corpus
        if corpus is not None:
            sections = []
            seen = set()
            for rel_path in corpus.ordered_paths:
                section = rel_path.split("/", 1)[0] if "/" in rel_path else rel_path
                doc = corpus.documents.get(rel_path)
                if (
                    section not in GRAPH_BROWSER_SECTIONS
                    or doc is None
                    or doc.file_type not in GRAPH_BROWSER_FILE_TYPES
                ):
                    continue
                if section not in seen:
                    seen.add(section)
                    sections.append(section)
            for section in sections:
                label = SECTION_LABELS.get(section, section)
                item = self.categories.insert("", tk.END, text=label)
                self._category_items[item] = section
        self.categories.selection_set(all_item)
        self.categories.focus(all_item)

    def _on_category_selected(self, event: tk.Event) -> None:
        selection = self.categories.selection()
        if not selection:
            return
        self._selected_section = self._category_items.get(selection[0], "ALL")
        self.refresh_files()

    def _clear_search(self) -> None:
        self.query_var.set("")
        self.refresh_files()
        self.search_entry.focus_set()

    def refresh_files(self) -> None:
        self.files.delete(*self.files.get_children())
        self._row_to_path.clear()
        corpus = self.app.corpus
        if corpus is None:
            self.status_var.set("No corpus loaded")
            return
        query = self.query_var.get().strip().casefold()
        visible = 0
        for rel_path in corpus.ordered_paths:
            section = rel_path.split("/", 1)[0] if "/" in rel_path else rel_path
            doc = corpus.documents[rel_path]
            if section not in GRAPH_BROWSER_SECTIONS or doc.file_type not in GRAPH_BROWSER_FILE_TYPES:
                continue
            if self._selected_section != "ALL" and section != self._selected_section:
                continue
            haystack = f"{doc.title} {rel_path}".casefold()
            if query and query not in haystack:
                continue
            row = self.files.insert("", tk.END, values=(doc.title, rel_path, doc.file_type.upper()))
            self._row_to_path[row] = rel_path
            visible += 1
        self.status_var.set(f"{visible:,} graph-relevant file{'s' if visible != 1 else ''}")

    def open_selected(self) -> None:
        selection = self.files.selection()
        if not selection:
            return
        rel_path = self._row_to_path.get(selection[0])
        if not rel_path:
            return
        self.app.open_document(rel_path)
        self.app.deiconify()
        self.app.lift()

    def apply_theme(self) -> None:
        palette = self.graph_lab.theme_palette()
        self.configure(background=palette["window_bg"])
        style = ttk.Style(self)
        style.configure(
            "Browser.Treeview",
            background=palette["panel_bg"],
            fieldbackground=palette["panel_bg"],
            foreground=palette["fg"],
            rowheight=26,
        )
        style.map(
            "Browser.Treeview",
            background=[("selected", palette["selection_bg"])],
            foreground=[("selected", palette["fg"])],
        )
        style.configure(
            "Browser.Treeview.Heading",
            background=palette["button_bg"],
            foreground=palette["fg"],
        )
        style.map("Browser.Treeview.Heading", background=[("active", palette["button_hover_bg"])])

    def _center_over_parent(self) -> None:
        try:
            self.update_idletasks()
            width = max(self.winfo_width(), 720)
            height = max(self.winfo_height(), 480)
            parent_x = self.graph_lab.winfo_rootx()
            parent_y = self.graph_lab.winfo_rooty()
            parent_w = self.graph_lab.winfo_width()
            parent_h = self.graph_lab.winfo_height()
            x = max(0, parent_x + (parent_w - width) // 2)
            y = max(0, parent_y + (parent_h - height) // 2)
            self.geometry(f"{width}x{height}+{x}+{y}")
        except tk.TclError:
            pass


class GraphLab(tk.Toplevel):
    """Interactive graph and pseudo-3D exploration layer."""

    VIEW_CASE_TREE = "3D Case Tree"
    VIEW_AUTHORITY = "Authority Graph"
    VIEW_DEPENDENCY = "Dependency Graph"
    VIEW_FLOW = "Transformation Flow"
    VIEW_RECORD = "Selected Record Trace"
    VIEW_CHAIN = "Selected Chain"

    def __init__(self, app: "PmsStrataReaderApp"):
        super().__init__(app)
        self.app = app
        self.title(f"{APP_TITLE} — Graph Lab")
        self.geometry("1260x820")
        self.minsize(880, 580)
        self.protocol("WM_DELETE_WINDOW", self._hide)

        self.view_var = tk.StringVar(value=self.VIEW_CASE_TREE)
        self.operation_var = tk.StringVar(value="ALL")
        self.class_var = tk.StringVar(value="ALL")
        self.labels_var = tk.BooleanVar(value=True)
        self.status_var = tk.StringVar(value="Left-drag to rotate • middle/right-drag to pan • wheel to zoom • click a node for details")

        self.nodes: List[GraphNode] = []
        self.edges: List[Tuple[str, str]] = []
        self.node_by_id: Dict[str, GraphNode] = {}
        self.projected: Dict[str, Tuple[float, float, float, float]] = {}
        self.selected_node_id = ""
        self.hovered_node_id = ""
        self.angle_x = -0.22
        self.angle_y = 0.52
        self.zoom = 1.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        self._drag_start: Optional[Tuple[int, int]] = None
        self._drag_moved = False
        self._pan_start: Optional[Tuple[int, int]] = None
        self.browser_dialog: Optional[BrowseFilesDialog] = None
        self._detail_texts: Dict[str, tk.Text] = {}

        self._build_ui()
        self.apply_theme()
        self.refresh()
        self.after_idle(self._maximize)

    def _build_ui(self) -> None:
        toolbar = ttk.Frame(self, padding=(8, 8, 8, 5))
        toolbar.pack(fill=tk.X)

        ttk.Button(toolbar, text="Browse Files", command=self.browse_files).pack(side=tk.LEFT, padx=(0, 14))

        ttk.Label(toolbar, text="View").pack(side=tk.LEFT)
        self.view_box = ttk.Combobox(
            toolbar,
            textvariable=self.view_var,
            state="readonly",
            width=25,
            style="Graph.TCombobox",
            values=[
                self.VIEW_CASE_TREE,
                self.VIEW_AUTHORITY,
                self.VIEW_DEPENDENCY,
                self.VIEW_FLOW,
                self.VIEW_RECORD,
                self.VIEW_CHAIN,
            ],
        )
        self.view_box.pack(side=tk.LEFT, padx=(5, 12))
        self.view_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())

        ttk.Label(toolbar, text="Operation").pack(side=tk.LEFT)
        self.op_box = ttk.Combobox(
            toolbar,
            textvariable=self.operation_var,
            state="readonly",
            width=13,
            style="Graph.TCombobox",
            values=["ALL", "COMPOSE", "DECOMPOSE", "PROJECT_AS"],
        )
        self.op_box.pack(side=tk.LEFT, padx=(5, 12))
        self.op_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())

        ttk.Label(toolbar, text="Output Class").pack(side=tk.LEFT)
        self.class_box = ttk.Combobox(
            toolbar,
            textvariable=self.class_var,
            state="readonly",
            width=30,
            style="Graph.TCombobox",
        )
        self.class_box.pack(side=tk.LEFT, padx=(5, 12))
        self.class_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())

        ttk.Checkbutton(toolbar, text="Labels", variable=self.labels_var, command=self.redraw).pack(side=tk.LEFT)
        ttk.Button(toolbar, text="Reset View", command=self.reset_view).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(toolbar, text="Close", command=self._hide).pack(side=tk.RIGHT)

        for box in (self.view_box, self.op_box, self.class_box):
            box.configure(cursor="hand2")

        main = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        main.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 5))

        canvas_frame = ttk.Frame(main)
        main.add(canvas_frame, weight=4)
        self.canvas = tk.Canvas(canvas_frame, highlightthickness=0, background="#10151c")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", lambda event: self.redraw())
        self.canvas.bind("<ButtonPress-1>", self._on_press)
        self.canvas.bind("<B1-Motion>", self._on_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_release)
        self.canvas.bind("<ButtonPress-2>", self._on_pan_press)
        self.canvas.bind("<B2-Motion>", self._on_pan_drag)
        self.canvas.bind("<ButtonRelease-2>", self._on_pan_release)
        self.canvas.bind("<ButtonPress-3>", self._on_pan_press)
        self.canvas.bind("<B3-Motion>", self._on_pan_drag)
        self.canvas.bind("<ButtonRelease-3>", self._on_pan_release)
        self.canvas.bind("<Double-1>", self._on_double_click)
        self.canvas.bind("<Motion>", self._on_motion)
        self.canvas.bind("<Leave>", self._on_leave)
        self.canvas.bind("<MouseWheel>", self._on_wheel)
        self.canvas.bind("<Button-4>", lambda event: self._zoom_by(1.12))
        self.canvas.bind("<Button-5>", lambda event: self._zoom_by(0.89))

        detail_frame = ttk.Frame(main, padding=(8, 4, 4, 4))
        main.add(detail_frame, weight=2)
        ttk.Label(detail_frame, text="Case / Node Details", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W)
        self.detail_notebook = ttk.Notebook(detail_frame, style="Graph.TNotebook")
        self.detail_notebook.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self._create_detail_tab("Summary", wrap=tk.WORD)
        self._create_detail_tab("YAML", wrap=tk.NONE)
        self._create_detail_tab("Markdown", wrap=tk.WORD)
        self._create_detail_tab("Relations", wrap=tk.WORD)
        self._create_detail_tab("Trace", wrap=tk.WORD)

        ttk.Label(self, textvariable=self.status_var, anchor=tk.W, padding=(8, 4), style="Status.TLabel").pack(fill=tk.X)

    def _create_detail_tab(self, label: str, wrap: str) -> None:
        frame = ttk.Frame(self.detail_notebook, padding=0)
        text = tk.Text(frame, wrap=wrap, padx=12, pady=12, state=tk.DISABLED, undo=False)
        yscroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
        text.configure(yscrollcommand=yscroll.set)
        text.grid(row=0, column=0, sticky="nsew")
        yscroll.grid(row=0, column=1, sticky="ns")
        if wrap == tk.NONE:
            xscroll = AutoHideScrollbar(frame, orient=tk.HORIZONTAL, command=text.xview)
            text.configure(xscrollcommand=xscroll.set)
            xscroll.grid(row=1, column=0, sticky="ew")
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        self.detail_notebook.add(frame, text=label)
        self._detail_texts[label] = text
        self._configure_detail_tags(text)

    def _maximize(self) -> None:
        try:
            self.state("zoomed")
            return
        except tk.TclError:
            pass
        try:
            self.attributes("-zoomed", True)
            return
        except tk.TclError:
            pass
        try:
            width = self.winfo_screenwidth()
            height = self.winfo_screenheight()
            self.geometry(f"{width}x{height}+0+0")
        except tk.TclError:
            pass

    def _hide(self) -> None:
        if self.browser_dialog is not None and self.browser_dialog.winfo_exists():
            self.browser_dialog.withdraw()
        self.withdraw()

    def browse_files(self) -> None:
        if self.browser_dialog is None or not self.browser_dialog.winfo_exists():
            self.browser_dialog = BrowseFilesDialog(self)
        else:
            self.browser_dialog.deiconify()
            self.browser_dialog.lift()
            self.browser_dialog._populate_categories()
            self.browser_dialog.refresh_files()
            self.browser_dialog.apply_theme()
            self.browser_dialog.after_idle(self.browser_dialog._center_over_parent)

    def set_current_path(self, rel_path: Optional[str]) -> None:
        if self.view_var.get() in {self.VIEW_RECORD, self.VIEW_CHAIN}:
            self.refresh()

    def reset_view(self) -> None:
        self.angle_x = -0.22
        self.angle_y = 0.52
        self.zoom = 1.0
        self.pan_x = 0.0
        self.pan_y = 0.0
        self.redraw()

    def refresh(self) -> None:
        corpus = self.app.corpus
        if corpus is None:
            return
        classes = sorted({record.output_class for record in corpus.records})
        self.class_box.configure(values=["ALL"] + classes)
        if self.class_var.get() not in (["ALL"] + classes):
            self.class_var.set("ALL")

        view = self.view_var.get()
        if view == self.VIEW_CASE_TREE:
            self.nodes, self.edges = self._build_case_tree()
        elif view == self.VIEW_AUTHORITY:
            self.nodes, self.edges = self._build_authority_graph()
        elif view == self.VIEW_DEPENDENCY:
            self.nodes, self.edges = self._build_dependency_graph()
        elif view == self.VIEW_FLOW:
            self.nodes, self.edges = self._build_transformation_flow()
        elif view == self.VIEW_RECORD:
            self.nodes, self.edges = self._build_record_trace()
        else:
            self.nodes, self.edges = self._build_chain_graph()

        self.node_by_id = {node.node_id: node for node in self.nodes}
        self.selected_node_id = ""
        self.hovered_node_id = ""
        self.pan_x = 0.0
        self.pan_y = 0.0
        self._show_general_details(self._view_description(view))
        self.redraw()

    def _filtered_records(self) -> List[RecordSummary]:
        assert self.app.corpus is not None
        op_filter = self.operation_var.get()
        class_filter = self.class_var.get()
        return [
            record for record in self.app.corpus.records
            if (op_filter == "ALL" or record.operation == op_filter)
            and (class_filter == "ALL" or record.output_class == class_filter)
        ]

    def _build_case_tree(self) -> Tuple[List[GraphNode], List[Tuple[str, str]]]:
        records = self._filtered_records()
        nodes = [GraphNode("root", "PMS-STRATA\nCases", "root", 0, 0, -260, details=f"{len(records)} visible records")]
        edges: List[Tuple[str, str]] = []
        operations = [op for op in ["COMPOSE", "DECOMPOSE", "PROJECT_AS"] if any(r.operation == op for r in records)]
        for oi, operation in enumerate(operations):
            angle = 2 * math.pi * oi / max(1, len(operations)) - math.pi / 2
            ox, oy = 250 * math.cos(angle), 250 * math.sin(angle)
            op_id = f"op:{operation}"
            op_records = [record for record in records if record.operation == operation]
            nodes.append(GraphNode(op_id, operation, "operation", ox, oy, -70, details=f"{len(op_records)} records"))
            edges.append(("root", op_id))
            classes = sorted({record.output_class for record in op_records})
            for ci, output_class in enumerate(classes):
                spread = (ci - (len(classes) - 1) / 2) * 0.55
                class_angle = angle + spread
                cx = ox + 190 * math.cos(class_angle)
                cy = oy + 190 * math.sin(class_angle)
                class_id = f"class:{operation}:{output_class}"
                class_records = [record for record in op_records if record.output_class == output_class]
                nodes.append(GraphNode(class_id, output_class, "class", cx, cy, 90, details=f"{len(class_records)} records"))
                edges.append((op_id, class_id))
                for ri, record in enumerate(class_records):
                    local_angle = class_angle + (ri - (len(class_records) - 1) / 2) * 0.20
                    radius = 85 + 18 * (ri % 4)
                    rx = cx + radius * math.cos(local_angle)
                    ry = cy + radius * math.sin(local_angle)
                    rz = 245 + 18 * (ri % 5)
                    node_id = f"record:{record.record_id}"
                    nodes.append(GraphNode(
                        node_id, record.case_id, "record", rx, ry, rz,
                        record.yaml_path, self._record_summary(record), record.record_id,
                    ))
                    edges.append((class_id, node_id))
        return nodes, edges

    def _build_authority_graph(self) -> Tuple[List[GraphNode], List[Tuple[str, str]]]:
        layers = [
            ("PMS.yaml", "external governing grammar", ""),
            ("00_source", "architecture and chapter blueprint", "00_source/PMS-STRATA_Structure.md"),
            ("01_blocks", "canonical corpus prose", "01_blocks/00_front_matter.md"),
            ("05_minified", "binding compact controls", "05_minified/PMS_STRATA_Minified_Canonical.md"),
            ("07_model", "formal operationalization", "07_model/PMS-STRATA.yaml"),
            ("02_appendices", "schemas, templates, supplements", "02_appendices/Appendix_A_Core_Definitions.md"),
            ("03_cases", "cases and transformation records", "03_cases/Case_Index.md"),
            ("04_reference", "terminology and cross-reference support", "04_reference/Reader_Pathways.md"),
            ("06_derivative_publications", "derivatives without backflow; currently pending", ""),
            ("08 Reader", "presentation and navigation only", "08_PMS-STRATA Reader/README.md"),
        ]
        nodes: List[GraphNode] = []
        edges: List[Tuple[str, str]] = []
        for index, (label, detail, rel_path) in enumerate(layers):
            node_id = f"authority:{index}"
            x = 90 * math.sin(index * 0.75)
            y = (index - (len(layers) - 1) / 2) * 105
            z = (index - 4.5) * 30
            nodes.append(GraphNode(node_id, label, "authority", x, y, z, rel_path, detail + "\n\nmore structure ≠ more authority"))
            if index:
                edges.append((f"authority:{index - 1}", node_id))
        return nodes, edges

    def _build_dependency_graph(self) -> Tuple[List[GraphNode], List[Tuple[str, str]]]:
        specs = [
            ("root", "PMS-STRATA.yaml", "root", 0, 0, -170, "07_model/PMS-STRATA.yaml", "formal root / manifest"),
            ("ops", "Operation Registry", "model", -250, -170, 0, "07_model/Operation_Registry.yaml", "exactly three operation types"),
            ("rules", "Admissibility Rules", "model", 0, -220, 30, "07_model/Admissibility_Rules.yaml", "sixteen rule carriers"),
            ("classes", "Output Classes", "model", 250, -170, 0, "07_model/Output_Classes.yaml", "ten non-ranked classes"),
            ("tree", "Boundary Decision Tree", "model", 270, 85, 75, "07_model/Boundary_Decision_Tree.yaml", "post-audit route selection"),
            ("schema", "Record Schema", "model", 0, 230, 95, "07_model/Transformation_Record.schema.json", "one occurrence per record"),
            ("registry", "Case Index", "case", -270, 85, 75, "03_cases/Case_Index.yaml", "59 records / 10 packages"),
            ("reader", "Reader Views", "reader", 0, 0, 280, "08_PMS-STRATA Reader/README.md", "visualization without authority"),
        ]
        nodes = [GraphNode(*spec) for spec in specs]
        edges = [
            ("root", "ops"), ("root", "rules"), ("root", "classes"),
            ("ops", "schema"), ("rules", "tree"), ("classes", "tree"),
            ("tree", "schema"), ("schema", "registry"), ("registry", "reader"),
            ("root", "reader"),
        ]
        return nodes, edges

    def _build_transformation_flow(self) -> Tuple[List[GraphNode], List[Tuple[str, str]]]:
        labels = [
            ("entry", "Source + Claim", "flow"),
            ("classification", "Operation Classification", "operation"),
            ("audit", "12-Stage Audit", "audit"),
            ("loss", "Loss + Alternatives", "loss"),
            ("candidates", "Candidate Generation", "flow"),
            ("collision", "Collision / Claim Split", "flow"),
            ("class", "One Output Class", "class"),
            ("record", "Transformation Record", "record"),
        ]
        nodes: List[GraphNode] = []
        edges: List[Tuple[str, str]] = []
        for index, (node_id, label, kind) in enumerate(labels):
            angle = index * 0.78 - 2.6
            radius = 250
            nodes.append(GraphNode(node_id, label, kind, radius * math.cos(angle), radius * math.sin(angle), index * 55 - 170, details=label))
            if index:
                edges.append((labels[index - 1][0], node_id))
        edges.extend([("audit", "loss"), ("loss", "candidates")])
        return nodes, edges

    def _current_record(self) -> Optional[RecordSummary]:
        if self.app.corpus is None:
            return None
        return self.app.corpus.record_for_path(self.app.current_path)

    def _build_record_trace(self) -> Tuple[List[GraphNode], List[Tuple[str, str]]]:
        record = self._current_record()
        if record is None:
            return [GraphNode("none", "Select a case YAML or Markdown companion", "warning", 0, 0, 0)], []
        rid = record.record_id
        nodes = [
            GraphNode("source", record.source_id or "Source", "source", -280, -90, -80, details=record.source_description, record_id=rid),
            GraphNode("claim", "Claim", "claim", -120, -230, 0, details=record.claim, record_id=rid),
            GraphNode("operation", record.operation, "operation", 0, 0, 0, details=record.operation, record_id=rid),
            GraphNode("audit", "12-stage audit", "audit", 100, -220, 75, details="Audit findings remain qualitative and non-compensatory.", record_id=rid),
            GraphNode("loss", "5-part Loss", "loss", 220, 180, 90, details="preserved / compressed / excluded / uncertain / irrecoverable", record_id=rid),
            GraphNode("target", record.target_id or "Target", "target", 280, -70, 110, details=record.target_description, record_id=rid),
            GraphNode("class", record.output_class, "class", 100, 250, 190, details=record.output_class, record_id=rid),
            GraphNode("record", record.case_id, "record", -120, 230, 240, record.yaml_path, self._record_summary(record), rid),
        ]
        edges = [
            ("source", "operation"), ("claim", "operation"), ("operation", "audit"),
            ("operation", "target"), ("operation", "loss"), ("audit", "class"),
            ("loss", "class"), ("target", "class"), ("class", "record"),
        ]
        return nodes, edges

    def _build_chain_graph(self) -> Tuple[List[GraphNode], List[Tuple[str, str]]]:
        record = self._current_record()
        if record is None or self.app.corpus is None:
            return [GraphNode("none", "Select a chain record or package member", "warning", 0, 0, 0)], []
        members = self.app.corpus.records_for_chain(record)
        nodes: List[GraphNode] = []
        edges: List[Tuple[str, str]] = []
        for index, member in enumerate(members):
            angle = index * 0.88 - (len(members) - 1) * 0.44
            x = 270 * math.sin(angle)
            y = (index - (len(members) - 1) / 2) * 115
            z = index * 80 - 120
            node_id = f"chain:{member.record_id}"
            nodes.append(GraphNode(
                node_id, f"{member.case_id}\n{member.operation}", "record", x, y, z,
                member.yaml_path, self._record_summary(member), member.record_id,
            ))
            class_id = f"chainclass:{member.record_id}"
            nodes.append(GraphNode(
                class_id, member.output_class, "class", x + 150, y + 35, z + 35,
                details=member.output_class, record_id=member.record_id,
            ))
            edges.append((node_id, class_id))
            if index:
                edges.append((f"chain:{members[index - 1].record_id}", node_id))
        return nodes, edges

    @staticmethod
    def _view_description(view: str) -> str:
        descriptions = {
            GraphLab.VIEW_CASE_TREE: "Corpus tree: operation → output class → record. Left-drag rotates, middle/right-drag pans, and the selected node becomes the rotation pivot. Visual depth is not ontological depth.",
            GraphLab.VIEW_AUTHORITY: "Authority order from PMS Base to Reader. The graph visualizes declared precedence; it creates none.",
            GraphLab.VIEW_DEPENDENCY: "Formal-model dependency view. Schema and graph consistency do not establish substantive truth.",
            GraphLab.VIEW_FLOW: "Transformation flow from source and claim through audit, routing, and record preservation.",
            GraphLab.VIEW_RECORD: "Selected record trace. Open a YAML record or Markdown companion in the main reader first.",
            GraphLab.VIEW_CHAIN: "Selected chain view. Local results and Loss profiles remain separate at every handoff.",
        }
        return descriptions.get(view, "")

    @staticmethod
    def _record_summary(record: RecordSummary) -> str:
        stop_status, failure_status, non_capture_status = GraphLab._status_flags(record)
        return (
            f"{record.case_id} — {record.title}\n\n"
            f"Record ID: {record.record_id}\n"
            f"Operation: {record.operation}\n"
            f"Output Class: {record.output_class}\n"
            f"Case Class: {record.case_class or '—'}\n"
            f"Chapter Owner: {record.chapter_owner or '—'}\n\n"
            f"Claim\n{record.claim or '—'}\n\n"
            f"Source\n{record.source_id or '—'}\n{record.source_description or '—'}\n\n"
            f"Target\n{record.target_id or '—'}\n{record.target_description or '—'}\n\n"
            f"Status\nStop: {stop_status}\nFailure: {failure_status}\nNon-Capture: {non_capture_status}\n\n"
            f"Loss\nFive-channel profile: preserved / compressed / excluded / uncertain / irrecoverable. "
            f"See the YAML tab for the declared values.\n\n"
            f"Paired Artifacts\nYAML: {record.yaml_path}\n"
            f"Markdown: {record.markdown_path or '—'}\n"
            f"Package: {record.package_path or '—'}"
        )

    @staticmethod
    def _status_flags(record: RecordSummary) -> Tuple[str, str, str]:
        output = record.output_class.casefold()
        stop = "present" if "stop" in output else "not selected by Output Class"
        failure = "present" if output == "failed_transformation" or "failed" in output else "not selected by Output Class"
        non_capture = "present" if "non_capture" in output or "non-capture" in output else "not selected by Output Class"
        return stop, failure, non_capture

    def _record_for_node(self, node: GraphNode) -> Optional[RecordSummary]:
        corpus = self.app.corpus
        if corpus is None or not node.record_id:
            return None
        return corpus.record_by_id.get(node.record_id)

    def _show_general_details(self, summary: str) -> None:
        self._set_detail_text("Summary", summary + "\n\nNo node is selected. Rotation uses the graph origin.")
        self._set_detail_text("YAML", "No YAML artifact is selected.")
        self._set_detail_text("Markdown", "No Markdown artifact is selected.")
        for label in ("Relations", "Trace"):
            self._set_detail_text(label, "Select a Record node to inspect this view.")
        self.detail_notebook.select(0)

    def _show_node_details(self, node: GraphNode) -> None:
        record = self._record_for_node(node)
        corpus = self.app.corpus
        pivot_note = f"Graph rotation pivot: {node.label}"

        if record is None:
            summary = (
                f"{node.label}\n\n"
                f"Node kind: {node.kind}\n"
                f"{pivot_note}\n\n"
                f"{node.details or 'No additional node summary is declared.'}"
            )
            yaml_text = "No YAML artifact is linked to the selected node."
            markdown_text = "No Markdown artifact is linked to the selected node."
            if node.rel_path:
                summary += f"\n\nRepository artifact\n{node.rel_path}\n\nDouble-click the node to open it in the Reader."
                if corpus is not None:
                    doc = corpus.documents.get(node.rel_path)
                    if doc is not None:
                        if doc.file_type in {"yaml", "yml", "json"}:
                            yaml_text = doc.text
                        elif doc.file_type == "md":
                            markdown_text = doc.text
                        else:
                            summary += f"\n\nArtifact type: {doc.file_type.upper()}"
            self._set_detail_text("Summary", summary)
            self._set_detail_text("YAML", yaml_text, node.rel_path if node.rel_path and node.rel_path.lower().endswith((".yaml", ".yml", ".json")) else None)
            self._set_detail_text("Markdown", markdown_text, node.rel_path if node.rel_path and node.rel_path.lower().endswith(".md") else None)
            self._set_detail_text("Relations", "No Record relation set is attached to this node.")
            self._set_detail_text("Trace", "No Record trace is attached to this node.")
            self.detail_notebook.select(0)
            return

        self._set_detail_text("Summary", self._record_summary(record) + f"\n\n{pivot_note}")
        yaml_text = "Artifact unavailable in active corpus."
        markdown_text = "No Markdown companion is declared."
        if corpus is not None:
            yaml_doc = corpus.documents.get(record.yaml_path)
            if yaml_doc is not None:
                yaml_text = yaml_doc.text
            if record.markdown_path:
                markdown_doc = corpus.documents.get(record.markdown_path)
                if markdown_doc is not None:
                    markdown_text = markdown_doc.text
        self._set_detail_text("YAML", yaml_text, record.yaml_path)
        self._set_detail_text("Markdown", markdown_text, record.markdown_path)
        self._set_detail_text("Relations", self._relations_text(record))
        self._set_detail_text("Trace", self._trace_text(record))

    def _relations_text(self, record: RecordSummary) -> str:
        corpus = self.app.corpus
        chain_members: List[RecordSummary] = []
        if corpus is not None:
            chain_members = corpus.records_for_chain(record)
        member_lines = "\n".join(
            f"- {member.case_id} — {member.operation} → {member.output_class}"
            for member in chain_members
        ) or "—"
        return (
            f"Record ID: {record.record_id}\n"
            f"Chain ID: {record.chain_id or '—'}\n"
            f"Previous occurrence: {record.previous_occurrence_id or '—'}\n"
            f"Next occurrence: {record.next_occurrence_id or '—'}\n"
            f"Package narrative: {record.package_path or '—'}\n\n"
            f"Paired artifacts\n"
            f"- YAML: {record.yaml_path}\n"
            f"- Markdown: {record.markdown_path or '—'}\n\n"
            f"Chain / package members\n{member_lines}\n\n"
            "Each occurrence preserves its own operation, Loss profile, and local Output Class."
        )

    @staticmethod
    def _trace_text(record: RecordSummary) -> str:
        stop_status, failure_status, non_capture_status = GraphLab._status_flags(record)
        return (
            f"1. Source\n   {record.source_id or '—'} — {record.source_description or '—'}\n\n"
            f"2. Claim\n   {record.claim or '—'}\n\n"
            f"3. Operation\n   {record.operation}\n\n"
            "4. Admissibility Audit\n   Qualitative, non-compensatory, and bounded by Stop / Non-Capture.\n\n"
            "5. Loss\n   preserved / compressed / excluded / uncertain / irrecoverable\n\n"
            f"6. Target\n   {record.target_id or '—'} — {record.target_description or '—'}\n\n"
            f"7. Output Class\n   {record.output_class}\n\n"
            f"8. Status\n   Stop: {stop_status}\n   Failure: {failure_status}\n   Non-Capture: {non_capture_status}\n\n"
            f"9. Record Preservation\n   {record.record_id}\n"
        )

    def _configure_detail_tags(self, widget: tk.Text) -> None:
        palette = self.theme_palette()
        widget.tag_configure("detail_body", font=("Segoe UI", 10), foreground=palette["text_fg"], spacing1=1, spacing3=1)
        widget.tag_configure("detail_title", font=("Segoe UI", 14, "bold"), foreground=palette["title_fg"], spacing1=2, spacing3=10)
        widget.tag_configure("detail_h2", font=("Segoe UI", 11, "bold"), foreground=palette["title_fg"], spacing1=9, spacing3=4)
        widget.tag_configure("detail_h3", font=("Segoe UI", 10, "bold"), foreground=palette["title_fg"], spacing1=6, spacing3=2)
        widget.tag_configure("detail_bold", font=("Segoe UI", 10, "bold"), foreground=palette["text_fg"])
        widget.tag_configure("detail_italic", font=("Segoe UI", 10, "italic"), foreground=palette["text_fg"])
        widget.tag_configure("detail_code", font=("Consolas", 9), foreground=palette["text_fg"], background=palette["label_bg"], lmargin1=8, lmargin2=8, spacing1=2, spacing3=2)
        widget.tag_configure("detail_inline_code", font=("Consolas", 9), foreground=palette["selected_ring"], background=palette["label_bg"])
        widget.tag_configure("detail_quote", font=("Segoe UI", 10, "italic"), foreground=palette["muted_fg"], lmargin1=16, lmargin2=16)
        widget.tag_configure("detail_list", font=("Segoe UI", 10), foreground=palette["text_fg"], lmargin1=18, lmargin2=34)
        widget.tag_configure("detail_rule", foreground=palette["edge"], spacing1=5, spacing3=5)
        widget.tag_configure("detail_table", font=("Consolas", 9), foreground=palette["text_fg"], background=palette["label_bg"])
        widget.tag_configure("detail_link", font=("Segoe UI", 10, "underline"), foreground=palette["hover_ring"])
        widget.tag_configure("yaml_key", font=("Consolas", 9, "bold"), foreground=palette["hover_ring"])
        widget.tag_configure("yaml_value", font=("Consolas", 9), foreground=palette["text_fg"])
        widget.tag_configure("yaml_string", font=("Consolas", 9), foreground="#2d8a55" if not self.app.dark_mode else "#89d185")
        widget.tag_configure("yaml_scalar", font=("Consolas", 9, "bold"), foreground="#8a4fb8" if not self.app.dark_mode else "#c586c0")
        widget.tag_configure("yaml_comment", font=("Consolas", 9, "italic"), foreground=palette["muted_fg"])
        widget.tag_configure("yaml_code", font=("Consolas", 9), foreground=palette["text_fg"])

    def _set_detail_text(self, label: str, text: str, rel_path: Optional[str] = None) -> None:
        widget = self._detail_texts[label]
        widget.configure(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        self._configure_detail_tags(widget)
        if label == "Summary":
            self._render_detail_summary(widget, text)
        elif label == "YAML":
            self._render_detail_yaml(widget, text)
        elif label == "Markdown":
            self._render_detail_markdown(widget, text, rel_path)
        else:
            widget.insert("1.0", text, ("detail_body",))
        widget.configure(state=tk.DISABLED)
        widget.yview_moveto(0.0)
        widget.xview_moveto(0.0)

    def _render_detail_summary(self, widget: tk.Text, text: str) -> None:
        section_names = {
            "Claim", "Source", "Target", "Status", "Loss", "Paired Artifacts",
            "Repository artifact", "Graph rotation pivot", "Relations", "Trace",
        }
        first_content = True
        for raw_line in text.splitlines():
            line = raw_line.rstrip()
            if not line:
                widget.insert(tk.END, "\n", ("detail_body",))
                continue
            if first_content:
                widget.insert(tk.END, line + "\n", ("detail_title",))
                first_content = False
                continue
            if line in section_names:
                widget.insert(tk.END, line + "\n", ("detail_h2",))
                continue
            key_match = re.match(r"^([A-Za-z][A-Za-z /_-]{0,34}):\s*(.*)$", line)
            if key_match:
                key, value = key_match.groups()
                widget.insert(tk.END, key + ": ", ("detail_bold",))
                widget.insert(tk.END, value + "\n", ("detail_body",))
                continue
            if re.match(r"^(?:README\.md|0[0-8]_[^/]+/|[^\s]+\.(?:md|ya?ml|json|csv|py))(?:/|$)", line):
                widget.insert(tk.END, line + "\n", ("detail_code",))
                continue
            widget.insert(tk.END, line + "\n", ("detail_body",))

    def _render_detail_yaml(self, widget: tk.Text, text: str) -> None:
        if text.startswith("No YAML artifact") or text.startswith("Artifact unavailable"):
            widget.insert(tk.END, text, ("detail_body",))
            return
        for raw_line in text.splitlines():
            stripped = raw_line.lstrip()
            if not stripped:
                widget.insert(tk.END, "\n", ("yaml_code",))
                continue
            if stripped.startswith("#"):
                widget.insert(tk.END, raw_line + "\n", ("yaml_comment",))
                continue
            match = re.match(r"^(\s*)(-\s+)?([A-Za-z0-9_.-]+)(\s*:\s*)(.*)$", raw_line)
            if match:
                indent, bullet, key, separator, value = match.groups()
                widget.insert(tk.END, indent + (bullet or ""), ("yaml_code",))
                widget.insert(tk.END, key, ("yaml_key",))
                widget.insert(tk.END, separator, ("yaml_code",))
                self._insert_detail_yaml_value(widget, value)
                widget.insert(tk.END, "\n", ("yaml_code",))
                continue
            list_match = re.match(r"^(\s*-\s+)(.*)$", raw_line)
            if list_match:
                widget.insert(tk.END, list_match.group(1), ("yaml_key",))
                self._insert_detail_yaml_value(widget, list_match.group(2))
                widget.insert(tk.END, "\n", ("yaml_code",))
                continue
            widget.insert(tk.END, raw_line + "\n", ("yaml_code",))

    def _insert_detail_yaml_value(self, widget: tk.Text, value: str) -> None:
        comment_at = -1
        quote = None
        for index, char in enumerate(value):
            if char in {'"', "'"}:
                if quote is None:
                    quote = char
                elif quote == char:
                    quote = None
            elif char == "#" and quote is None and (index == 0 or value[index - 1].isspace()):
                comment_at = index
                break
        main = value if comment_at < 0 else value[:comment_at].rstrip()
        comment = "" if comment_at < 0 else value[comment_at:]
        scalar = main.strip()
        if scalar.startswith(("'", '"')) and scalar.endswith(("'", '"')) and len(scalar) >= 2:
            tag = "yaml_string"
        elif scalar.casefold() in {"true", "false", "null", "none", "yes", "no", "on", "off", "~"} or re.fullmatch(r"[-+]?\d+(?:\.\d+)?", scalar or ""):
            tag = "yaml_scalar"
        else:
            tag = "yaml_value"
        widget.insert(tk.END, main, (tag,))
        if comment:
            if main:
                widget.insert(tk.END, " ", ("yaml_code",))
            widget.insert(tk.END, comment, ("yaml_comment",))

    def _render_detail_markdown(self, widget: tk.Text, text: str, rel_path: Optional[str]) -> None:
        if text.startswith("No Markdown"):
            widget.insert(tk.END, text, ("detail_body",))
            return
        body = strip_frontmatter(text)
        lines = body.splitlines()
        i = 0
        while i < len(lines):
            raw_line = lines[i]
            fence = FENCE_RE.match(raw_line)
            if fence:
                language = (fence.group(2) or "").casefold()
                block = []
                i += 1
                while i < len(lines) and not FENCE_RE.match(lines[i]):
                    block.append(lines[i])
                    i += 1
                if i < len(lines):
                    i += 1
                if language in {"yaml", "yml"}:
                    self._render_detail_yaml(widget, "\n".join(block))
                else:
                    widget.insert(tk.END, "\n".join(block) + "\n", ("detail_code",))
                continue
            heading = HEADING_RE.match(raw_line)
            if heading:
                level = len(heading.group(1))
                tag = "detail_title" if level == 1 else "detail_h2" if level <= 3 else "detail_h3"
                self._insert_detail_inline_markdown(widget, clean_heading_text(heading.group(2)), (tag,), rel_path)
                widget.insert(tk.END, "\n", (tag,))
                i += 1
                continue
            if looks_like_table_line(raw_line):
                table_lines = []
                while i < len(lines) and looks_like_table_line(lines[i]):
                    table_lines.append(lines[i])
                    i += 1
                for table_line in table_lines:
                    if re.match(r"^\s*\|?\s*:?-{3,}", table_line):
                        continue
                    cells = [cell.strip() for cell in table_line.strip().strip("|").split("|")]
                    widget.insert(tk.END, "  │  ".join(cells) + "\n", ("detail_table",))
                widget.insert(tk.END, "\n", ("detail_body",))
                continue
            list_match = LIST_RE.match(raw_line)
            if list_match:
                indent, _bullet, content = list_match.groups()
                level = max(0, len(indent.replace("\t", "    ")) // 2)
                widget.insert(tk.END, "  " * level + "• ", ("detail_list",))
                self._insert_detail_inline_markdown(widget, content, ("detail_list",), rel_path)
                widget.insert(tk.END, "\n", ("detail_list",))
                i += 1
                continue
            ordered = ORDERED_LIST_RE.match(raw_line)
            if ordered:
                indent, number, content = ordered.groups()
                level = max(0, len(indent.replace("\t", "    ")) // 2)
                widget.insert(tk.END, "  " * level + number + ". ", ("detail_list",))
                self._insert_detail_inline_markdown(widget, content, ("detail_list",), rel_path)
                widget.insert(tk.END, "\n", ("detail_list",))
                i += 1
                continue
            if raw_line.strip().startswith(">"):
                quote = re.sub(r"^\s*>\s?", "", raw_line)
                self._insert_detail_inline_markdown(widget, quote, ("detail_quote",), rel_path)
                widget.insert(tk.END, "\n", ("detail_quote",))
                i += 1
                continue
            if raw_line.strip() in {"---", "***", "___"}:
                widget.insert(tk.END, "─" * 72 + "\n", ("detail_rule",))
                i += 1
                continue
            self._insert_detail_inline_markdown(widget, raw_line, ("detail_body",), rel_path)
            widget.insert(tk.END, "\n", ("detail_body",))
            i += 1

    def _insert_detail_inline_markdown(
        self,
        widget: tk.Text,
        text: str,
        base_tags: Tuple[str, ...],
        rel_path: Optional[str],
    ) -> None:
        token_re = re.compile(r"(\[[^\]]+\]\([^)]+\)|`[^`]+`|\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*\n]+\*)")
        position = 0
        for match in token_re.finditer(text):
            if match.start() > position:
                widget.insert(tk.END, text[position:match.start()], base_tags)
            token = match.group(0)
            link_match = MARKDOWN_LINK_RE.fullmatch(token)
            if link_match:
                label, target = link_match.groups()
                tag = f"detail_link_{id(widget)}_{widget.index(tk.END).replace('.', '_')}"
                widget.insert(tk.END, label, base_tags + ("detail_link", tag))
                widget.tag_bind(tag, "<Button-1>", lambda _event, t=target, p=rel_path: self._open_detail_link(t, p))
                widget.tag_bind(tag, "<Enter>", lambda _event, w=widget: w.configure(cursor="hand2"))
                widget.tag_bind(tag, "<Leave>", lambda _event, w=widget: w.configure(cursor="xterm"))
            elif token.startswith("`"):
                widget.insert(tk.END, token[1:-1], base_tags + ("detail_inline_code",))
            elif token.startswith("***"):
                widget.insert(tk.END, token[3:-3], base_tags + ("detail_bold", "detail_italic"))
            elif token.startswith("**"):
                widget.insert(tk.END, token[2:-2], base_tags + ("detail_bold",))
            elif token.startswith("*"):
                widget.insert(tk.END, token[1:-1], base_tags + ("detail_italic",))
            position = match.end()
        if position < len(text):
            widget.insert(tk.END, text[position:], base_tags)

    def _open_detail_link(self, raw_target: str, source_path: Optional[str]) -> None:
        target = raw_target.strip()
        parsed = urlparse(target)
        if parsed.scheme in {"http", "https", "mailto"}:
            webbrowser.open(target)
            return
        path_part, _, anchor = target.partition("#")
        if path_part:
            base_dir = posixpath.dirname(source_path or "")
            resolved = posixpath.normpath(posixpath.join(base_dir, unquote(path_part)))
        else:
            resolved = source_path or ""
        if resolved and self.app.corpus is not None and resolved in self.app.corpus.documents:
            self.app.open_document(resolved, anchor_name=unquote(anchor) if anchor else None)
            self.app.deiconify()
            self.app.lift()

    def redraw(self) -> None:
        if not hasattr(self, "canvas"):
            return
        self.canvas.delete("all")
        width = max(1, self.canvas.winfo_width())
        height = max(1, self.canvas.winfo_height())
        self.projected.clear()
        for node in self.nodes:
            self.projected[node.node_id] = self._project(node, width, height)

        palette = self.theme_palette()
        edge_color = palette["edge"]
        for source_id, target_id in self.edges:
            if source_id not in self.projected or target_id not in self.projected:
                continue
            sx, sy, _sd, _ss = self.projected[source_id]
            tx, ty, _td, _ts = self.projected[target_id]
            self.canvas.create_line(sx, sy, tx, ty, fill=edge_color, width=1.4, arrow=tk.LAST, arrowshape=(7, 9, 3))

        draw_nodes = sorted(self.nodes, key=lambda node: self.projected[node.node_id][2], reverse=True)
        for node in draw_nodes:
            sx, sy, _depth, scale = self.projected[node.node_id]
            radius = self._node_radius(node.kind) * max(0.55, min(1.5, scale))
            fill, outline = self._node_colors(node)
            if node.node_id == self.selected_node_id:
                self.canvas.create_oval(
                    sx - radius - 5, sy - radius - 5, sx + radius + 5, sy + radius + 5,
                    outline=palette["selected_ring"], width=3,
                )
            elif node.node_id == self.hovered_node_id:
                self.canvas.create_oval(
                    sx - radius - 4, sy - radius - 4, sx + radius + 4, sy + radius + 4,
                    outline=palette["hover_ring"], width=2,
                )
            width_line = 3 if node.node_id == self.selected_node_id else 2 if node.node_id == self.hovered_node_id else 1
            self.canvas.create_oval(
                sx - radius, sy - radius, sx + radius, sy + radius,
                fill=fill, outline=outline, width=width_line,
            )
            show_label = self.labels_var.get() and (
                self.view_var.get() == self.VIEW_CASE_TREE
                or node.kind != "record"
                or len(self.nodes) < 35
                or node.node_id in {self.selected_node_id, self.hovered_node_id}
            )
            if show_label:
                self._draw_node_label(node, sx, sy + radius + 11)

        self.canvas.create_text(12, 12, anchor=tk.NW, text=self.view_var.get(), fill=palette["title_fg"], font=("Segoe UI", 12, "bold"))
        self.canvas.create_text(12, 34, anchor=tk.NW, text=f"{len(self.nodes)} nodes • {len(self.edges)} edges", fill=palette["muted_fg"], font=("Segoe UI", 9))
        if self.selected_node_id in self.node_by_id:
            pivot_label = self.node_by_id[self.selected_node_id].label.replace("\n", " / ")
            self.canvas.create_text(12, 54, anchor=tk.NW, text=f"Rotation pivot: {pivot_label}", fill=palette["selected_ring"], font=("Segoe UI", 9, "bold"))

    def _draw_node_label(self, node: GraphNode, x: float, y: float) -> None:
        palette = self.theme_palette()
        font_size = 8 if node.kind == "record" else 9
        text_id = self.canvas.create_text(
            x, y,
            text=node.label,
            fill=palette["label_fg"],
            font=("Segoe UI", font_size, "bold"),
            justify=tk.CENTER,
            width=160,
        )
        bbox = self.canvas.bbox(text_id)
        if bbox is None:
            return
        left, top, right, bottom = bbox
        pad_x, pad_y = 5, 3
        rect_id = self.canvas.create_rectangle(
            left - pad_x, top - pad_y, right + pad_x, bottom + pad_y,
            fill=palette["label_bg"], outline=palette["label_border"], width=1,
        )
        self.canvas.tag_lower(rect_id, text_id)

    def _project(self, node: GraphNode, width: int, height: int) -> Tuple[float, float, float, float]:
        pivot = self.node_by_id.get(self.selected_node_id)
        pivot_x = pivot.x if pivot is not None else 0.0
        pivot_y = pivot.y if pivot is not None else 0.0
        pivot_z = pivot.z if pivot is not None else 0.0

        rel_x = node.x - pivot_x
        rel_y = node.y - pivot_y
        rel_z = node.z - pivot_z

        cosy, siny = math.cos(self.angle_y), math.sin(self.angle_y)
        cosx, sinx = math.cos(self.angle_x), math.sin(self.angle_x)
        x1 = cosy * rel_x + siny * rel_z
        z1 = -siny * rel_x + cosy * rel_z
        y1 = cosx * rel_y - sinx * z1
        z2 = sinx * rel_y + cosx * z1
        perspective = 760 / max(240, 760 + z2)
        scale = self.zoom * perspective
        return (
            width / 2 + self.pan_x + x1 * scale,
            height / 2 + self.pan_y + y1 * scale,
            z2,
            scale,
        )

    @staticmethod
    def _node_radius(kind: str) -> float:
        return {
            "root": 28, "operation": 23, "class": 17, "record": 8,
            "authority": 20, "model": 18, "reader": 18, "flow": 18,
            "audit": 18, "loss": 16, "source": 18, "target": 18,
            "claim": 16, "warning": 24, "case": 18,
        }.get(kind, 14)

    def _node_colors(self, node: GraphNode) -> Tuple[str, str]:
        palette = {
            "root": ("#8f63ff", "#d8c9ff"),
            "operation": ("#2376c9", "#9dcfff"),
            "class": ("#b67816", "#ffd38a"),
            "record": ("#2b9b70", "#9ce7c8"),
            "authority": ("#7357b5", "#c9b6f7"),
            "model": ("#2f6d9b", "#99d0f4"),
            "reader": ("#4f8e3f", "#b8e4aa"),
            "flow": ("#4c7f9f", "#b8dcf2"),
            "audit": ("#8d4a9c", "#e1b5eb"),
            "loss": ("#a45c3c", "#f2b699"),
            "source": ("#3a75a8", "#a7d4f6"),
            "target": ("#2d936d", "#a8e8cd"),
            "claim": ("#8f5e3b", "#f2c6a3"),
            "warning": ("#b64646", "#ffb0b0"),
            "case": ("#2b9b70", "#9ce7c8"),
        }
        if node.kind == "operation":
            if "COMPOSE" in node.label:
                return "#286db5", "#a8d6ff"
            if "DECOMPOSE" in node.label:
                return "#b46f20", "#ffd19b"
            if "PROJECT_AS" in node.label:
                return "#27845e", "#a9e8cc"
        return palette.get(node.kind, ("#68798b", "#c7d2de"))

    def _nearest_node(self, x: int, y: int, threshold: float = 24) -> Optional[GraphNode]:
        nearest = None
        best = threshold * threshold
        for node_id, (sx, sy, _depth, _scale) in self.projected.items():
            distance = (sx - x) ** 2 + (sy - y) ** 2
            if distance < best:
                best = distance
                nearest = self.node_by_id.get(node_id)
        return nearest

    def _on_press(self, event: tk.Event) -> None:
        self._drag_start = (event.x, event.y)
        self._drag_moved = False

    def _on_drag(self, event: tk.Event) -> None:
        if self._drag_start is None:
            return
        dx = event.x - self._drag_start[0]
        dy = event.y - self._drag_start[1]
        if abs(dx) + abs(dy) > 2:
            self._drag_moved = True
        self.angle_y += dx * 0.008
        self.angle_x += dy * 0.008
        self.angle_x = max(-1.45, min(1.45, self.angle_x))
        self._drag_start = (event.x, event.y)
        self.redraw()

    def _on_release(self, event: tk.Event) -> None:
        if not self._drag_moved:
            node = self._nearest_node(event.x, event.y)
            if node:
                self.selected_node_id = node.node_id
                self.pan_x = 0.0
                self.pan_y = 0.0
                self._show_node_details(node)
                self.status_var.set(
                    f"Selected pivot: {node.label} • left-drag rotates around it • middle/right-drag pans"
                )
            else:
                self.selected_node_id = ""
                self._show_general_details(self._view_description(self.view_var.get()))
                self.status_var.set(
                    "Selection cleared • left-drag to rotate • middle/right-drag to pan • wheel to zoom"
                )
            self.redraw()
        self._drag_start = None

    def _on_pan_press(self, event: tk.Event) -> str:
        self._pan_start = (event.x, event.y)
        self.canvas.configure(cursor="fleur")
        return "break"

    def _on_pan_drag(self, event: tk.Event) -> str:
        if self._pan_start is None:
            return "break"
        dx = event.x - self._pan_start[0]
        dy = event.y - self._pan_start[1]
        self.pan_x += dx
        self.pan_y += dy
        self._pan_start = (event.x, event.y)
        self.redraw()
        return "break"

    def _on_pan_release(self, event: tk.Event) -> str:
        self._pan_start = None
        node = self._nearest_node(event.x, event.y, threshold=30)
        self.canvas.configure(cursor="hand2" if node else "arrow")
        return "break"

    def _on_motion(self, event: tk.Event) -> None:
        if (self._drag_start is not None and self._drag_moved) or self._pan_start is not None:
            return
        node = self._nearest_node(event.x, event.y, threshold=30)
        node_id = node.node_id if node else ""
        if node_id != self.hovered_node_id:
            self.hovered_node_id = node_id
            self.canvas.configure(cursor="hand2" if node else "arrow")
            if node:
                detail = (node.details or node.label).splitlines()[0]
                self.status_var.set(f"{node.label} • {detail} • click to select as pivot")
            else:
                self.status_var.set("Left-drag to rotate • middle/right-drag to pan • wheel to zoom • click a node for details")
            self.redraw()

    def _on_leave(self, event: tk.Event) -> None:
        if self.hovered_node_id:
            self.hovered_node_id = ""
            self.canvas.configure(cursor="arrow")
            self.status_var.set("Left-drag to rotate • middle/right-drag to pan • wheel to zoom • click a node for details")
            self.redraw()

    def _on_double_click(self, event: tk.Event) -> None:
        node = self._nearest_node(event.x, event.y, threshold=30)
        if node and node.rel_path:
            self.app.open_document(node.rel_path)
            self.app.deiconify()
            self.app.lift()

    def _on_wheel(self, event: tk.Event) -> str:
        self._zoom_by(1.12 if event.delta > 0 else 0.89)
        return "break"

    def _zoom_by(self, factor: float) -> None:
        self.zoom = max(0.35, min(3.0, self.zoom * factor))
        self.redraw()

    def theme_palette(self) -> Dict[str, str]:
        if self.app.dark_mode:
            return {
                "window_bg": "#151617",
                "panel_bg": "#191c1f",
                "fg": "#d4d4d4",
                "muted_fg": "#98a6b5",
                "canvas_bg": "#0d1117",
                "text_bg": "#101214",
                "text_fg": "#d4d4d4",
                "input_bg": "#202428",
                "button_bg": "#30343a",
                "button_hover_bg": "#3b4148",
                "selection_bg": "#3a5068",
                "edge": "#526173",
                "selected_ring": "#f4c95d",
                "hover_ring": "#7cc7ff",
                "label_bg": "#1b222b",
                "label_border": "#556273",
                "label_fg": "#eef3f8",
                "title_fg": "#d7e0ea",
            }
        return {
            "window_bg": "#f0f0f0",
            "panel_bg": "#ffffff",
            "fg": "#111111",
            "muted_fg": "#5a6875",
            "canvas_bg": "#f5f7fa",
            "text_bg": "#ffffff",
            "text_fg": "#111111",
            "input_bg": "#ffffff",
            "button_bg": "#eceff2",
            "button_hover_bg": "#dfe5ea",
            "selection_bg": "#cde8ff",
            "edge": "#8997a5",
            "selected_ring": "#a46a00",
            "hover_ring": "#1769aa",
            "label_bg": "#f7f9fb",
            "label_border": "#9aa8b6",
            "label_fg": "#15202b",
            "title_fg": "#15202b",
        }

    def apply_theme(self) -> None:
        palette = self.theme_palette()
        self.configure(background=palette["window_bg"])
        self.canvas.configure(background=palette["canvas_bg"])
        style = ttk.Style(self)
        style.configure(
            "Graph.TCombobox",
            fieldbackground=palette["input_bg"],
            background=palette["button_bg"],
            foreground=palette["fg"],
            arrowcolor=palette["fg"],
            selectbackground=palette["selection_bg"],
            selectforeground=palette["fg"],
        )
        style.map(
            "Graph.TCombobox",
            fieldbackground=[("readonly", palette["input_bg"]), ("disabled", palette["button_bg"])],
            foreground=[("readonly", palette["fg"]), ("disabled", palette["muted_fg"])],
            background=[("active", palette["button_hover_bg"]), ("readonly", palette["button_bg"])],
            selectbackground=[("readonly", palette["selection_bg"])],
            selectforeground=[("readonly", palette["fg"])],
        )
        style.configure("Graph.TNotebook", background=palette["window_bg"], borderwidth=0)
        style.configure(
            "Graph.TNotebook.Tab",
            background=palette["button_bg"],
            foreground=palette["fg"],
            padding=(10, 6),
        )
        style.map(
            "Graph.TNotebook.Tab",
            background=[("selected", palette["panel_bg"]), ("active", palette["button_hover_bg"])],
            foreground=[("selected", palette["fg"]), ("active", palette["fg"])],
        )
        self.option_add("*TCombobox*Listbox.background", palette["input_bg"])
        self.option_add("*TCombobox*Listbox.foreground", palette["fg"])
        self.option_add("*TCombobox*Listbox.selectBackground", palette["selection_bg"])
        self.option_add("*TCombobox*Listbox.selectForeground", palette["fg"])
        for widget in self._detail_texts.values():
            widget.configure(
                background=palette["text_bg"],
                foreground=palette["text_fg"],
                insertbackground=palette["text_fg"],
                selectbackground=palette["selection_bg"],
            )
            self._configure_detail_tags(widget)
        if self.browser_dialog is not None and self.browser_dialog.winfo_exists():
            self.browser_dialog.apply_theme()
        self.redraw()


# ---------------------------------------------------------------------------
# Main application
# ---------------------------------------------------------------------------

class PmsStrataReaderApp(tk.Tk):
    """Tkinter desktop app for browsing the PMS-STRATA corpus."""

    def __init__(self, initial_source: Optional[Path] = None):
        super().__init__()
        dbg("App: __init__ start")
        self.title(f"{APP_TITLE} {APP_VERSION}")
        self.geometry("1380x860")
        self.minsize(960, 600)

        # Ignore SIGINT so Ctrl+C in the console cannot interrupt Tk callbacks.
        import signal
        signal.signal(signal.SIGINT, signal.SIG_IGN)

        self.corpus: Optional[Corpus] = None
        self.current_path: Optional[str] = None
        self.heading_indices: Dict[str, str] = {}
        self.search_results: List[Tuple[str, int, str]] = []
        self._file_item_to_path: Dict[str, str] = {}
        self._heading_item_to_anchor: Dict[str, str] = {}
        self._heading_anchor_to_item: Dict[str, str] = {}
        self._document_anchor_indices: Dict[str, str] = {}
        self._heading_positions: List[Tuple[int, str, str]] = []
        self._search_entry: Optional[ttk.Entry] = None
        self.dark_mode = False
        self.graph_lab: Optional[GraphLab] = None

        self.reader_font_size = 10
        self.reader_fullscreen = False
        self._normal_geometry = ""

        # Guard against recursive Treeview callbacks:
        # programmatic selection_set() also emits <<TreeviewSelect>>.
        self._suppress_file_select_event = False
        self._suppress_heading_select_event = False
        self._heading_sync_after_id: Optional[str] = None
        self._manual_heading_until = 0.0

        self._link_tags: List[str] = []
        self._next_link_id = 0
        self._embedded_tables: List[tk.Widget] = []
        self._table_resize_after_id: Optional[str] = None

        # Queue for results coming back from the background loader thread.
        self._load_queue: queue.Queue = queue.Queue()

        # Separate queue and generation counter for document rendering. Opening
        # another file invalidates any delayed blocks from the previous file.
        self._render_queue: queue.Queue = queue.Queue()
        self._render_generation = 0
        self._render_poll_after_id: Optional[str] = None
        self._active_render_doc: Optional[Document] = None
        self._active_render_mode = ""
        self._active_render_total = 0
        self._active_render_inserted = 0
        self._chunk_heading_counter = 0
        self._pending_line_number: Optional[int] = None
        self._pending_anchor: Optional[str] = None

        self._configure_style()
        self._build_ui()
        self._bind_shortcuts()
        self.apply_theme()
        self._configure_clickable_cursors()
        self._center_window()
        self.after_idle(self._set_initial_pane_positions)

        dbg("App: UI built, scheduling background load")

        # Kick off corpus loading in a background thread after the window paints.
        if initial_source is not None:
            self.after(100, lambda: self._start_load_thread(initial_source))
        else:
            self.after(100, self._start_discover_thread)

        dbg("App: __init__ done")

    # ------------------------------------------------------------------ #
    # Background loading — worker thread, NO Tk calls allowed here       #
    # ------------------------------------------------------------------ #

    def _start_discover_thread(self) -> None:
        dbg("App: starting discover thread")
        self.status_var.set("Searching for PMS-STRATA corpus ...")
        t = threading.Thread(target=self._bg_discover, daemon=True)
        t.start()
        self.after(100, self._poll_load_queue)

    def _start_load_thread(self, source_path: Path) -> None:
        dbg(f"App: starting load thread for {source_path}")
        self.status_var.set(f"Loading corpus from {source_path} ...")
        t = threading.Thread(target=self._bg_load, args=(source_path,), daemon=True)
        t.start()
        self.after(100, self._poll_load_queue)

    def _bg_discover(self) -> None:
        """Runs in background thread: discover source path, then load."""
        try:
            dbg("bg_discover: searching ...")
            source_path = discover_default_source()
            if source_path is None:
                dbg("bg_discover: no source found")
                self._load_queue.put(("no_source", None))
                return
            dbg(f"bg_discover: found {source_path}, loading ...")
            self._bg_load(source_path)
        except Exception as exc:
            dbg(f"bg_discover: exception: {exc}")
            self._load_queue.put(("error", str(exc)))

    def _bg_load(self, source_path: Path) -> None:
        """Runs in background thread: create CorpusSource + Corpus."""
        try:
            dbg(f"bg_load: creating CorpusSource({source_path})")
            source = CorpusSource(source_path)
            dbg("bg_load: creating Corpus")
            corpus = Corpus(source)
            dbg("bg_load: done, posting result to queue")
            self._load_queue.put(("ok", corpus))
        except Exception as exc:
            dbg(f"bg_load: exception: {exc}")
            self._load_queue.put(("error", str(exc)))

    def _poll_load_queue(self) -> None:
        """Called periodically in the Tk thread to receive background results."""
        try:
            msg, payload = self._load_queue.get_nowait()
        except queue.Empty:
            # Nothing yet — reschedule.
            self.after(100, self._poll_load_queue)
            return

        dbg(f"poll_load_queue: received '{msg}'")

        if msg == "ok":
            corpus: Corpus = payload
            if self.corpus is not None:
                self.corpus.source.close()
            self.corpus = corpus
            self.current_path = None
            self.populate_file_tree()
            self.clear_search()
            self.status_var.set(
                f"Loaded {corpus.document_count} documents, "
                f"{corpus.total_line_count:,} lines, "
                f"{corpus.total_word_count:,} words — {corpus.source.describe()}"
            )
            self.open_home()

        elif msg == "no_source":
            self.status_var.set("Open a PMS-STRATA folder or zip file to begin.")

        elif msg == "error":
            error_msg: str = payload
            self.status_var.set(f"Error: {error_msg}")
            messagebox.showerror(APP_TITLE, error_msg)

        else:
            dbg(f"poll_load_queue: unknown message '{msg}'")

    # ------------------------------------------------------------------ #
    # Style / UI construction                                            #
    # ------------------------------------------------------------------ #

    def _configure_style(self) -> None:
        self.base_font = tkfont.Font(family="Segoe UI", size=10)
        self.bold_font = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.italic_font = tkfont.Font(family="Segoe UI", size=10, slant="italic")
        self.bold_italic_font = tkfont.Font(family="Segoe UI", size=10, weight="bold", slant="italic")
        self.mono_font = tkfont.Font(family="Consolas", size=10)
        self.heading_font_1 = tkfont.Font(family="Segoe UI", size=18, weight="bold")
        self.heading_font_2 = tkfont.Font(family="Segoe UI", size=15, weight="bold")
        self.heading_font_3 = tkfont.Font(family="Segoe UI", size=13, weight="bold")
        self.heading_font_4 = tkfont.Font(family="Segoe UI", size=11, weight="bold")

        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Treeview", rowheight=24)
        style.configure("TButton", padding=(8, 4))
        style.configure("TEntry", padding=(4, 4))

    def _build_ui(self) -> None:
        self._build_toolbar()
        self._build_fullscreen_toolbar()

        self.main_pane = tk.PanedWindow(
            self,
            orient=tk.HORIZONTAL,
            borderwidth=0,
            sashwidth=7,
            sashrelief=tk.RAISED,
            showhandle=True,
            handlesize=11,
            handlepad=2,
            opaqueresize=True,
        )
        self.main_pane.pack(fill=tk.BOTH, expand=True)

        self.left_pane = tk.PanedWindow(
            self.main_pane,
            orient=tk.VERTICAL,
            borderwidth=0,
            sashwidth=7,
            sashrelief=tk.RAISED,
            showhandle=True,
            handlesize=11,
            handlepad=2,
            opaqueresize=True,
        )
        self.main_pane.add(self.left_pane, minsize=230, stretch="always")

        # File tree
        self.file_frame = ttk.Frame(self.left_pane, padding=(6, 6, 6, 3), style="Navigation.TFrame")
        self.left_pane.add(self.file_frame, minsize=160, stretch="always")
        self.file_title_label = ttk.Label(
            self.file_frame,
            text="Corpus",
            font=("Segoe UI", 10, "bold"),
            style="NavigationTitle.TLabel",
        )
        self.file_title_label.pack(anchor=tk.W)

        file_tree_wrap = ttk.Frame(self.file_frame, style="Navigation.TFrame")
        file_tree_wrap.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        self.file_tree = ttk.Treeview(file_tree_wrap, show="tree", style="Corpus.Treeview")
        self.file_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        file_scrollbar = ttk.Scrollbar(file_tree_wrap, orient=tk.VERTICAL, command=self.file_tree.yview)
        file_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_tree.configure(yscrollcommand=file_scrollbar.set)

        self.file_tree.bind("<<TreeviewSelect>>", self._on_file_selected)
        self._bind_mousewheel_scroll(self.file_tree)

        # Search results
        self.search_frame = ttk.Frame(self.left_pane, padding=(6, 3, 6, 6), style="Navigation.TFrame")
        self.left_pane.add(self.search_frame, minsize=120, stretch="always")
        self.search_title_label = ttk.Label(
            self.search_frame,
            text="Search Results",
            font=("Segoe UI", 10, "bold"),
            style="NavigationTitle.TLabel",
        )
        self.search_title_label.pack(anchor=tk.W)

        search_tree_wrap = ttk.Frame(self.search_frame, style="Navigation.TFrame")
        search_tree_wrap.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        self.search_tree = ttk.Treeview(
            search_tree_wrap,
            show="headings",
            columns=("file", "line", "text"),
            height=9,
            style="Search.Treeview",
        )
        self.search_tree.heading("file", text="File")
        self.search_tree.heading("line", text="Line")
        self.search_tree.heading("text", text="Text")
        self.search_tree.column("file", width=130, stretch=False)
        self.search_tree.column("line", width=48, stretch=False, anchor=tk.E)
        self.search_tree.column("text", width=260, stretch=True)
        self.search_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        search_scrollbar = ttk.Scrollbar(search_tree_wrap, orient=tk.VERTICAL, command=self.search_tree.yview)
        search_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.search_tree.configure(yscrollcommand=search_scrollbar.set)

        self.search_tree.bind("<Double-1>", self._on_search_result_open)
        self.search_tree.bind("<Return>", self._on_search_result_open)
        self._bind_mousewheel_scroll(self.search_tree)

        # Heading tree
        self.heading_frame = ttk.Frame(
            self.main_pane,
            padding=(6, 6, 6, 6),
            style="HeadingPane.TFrame",
        )
        self.main_pane.add(self.heading_frame, minsize=200, stretch="always")
        self.heading_title_label = ttk.Label(
            self.heading_frame,
            text="Headings",
            font=("Segoe UI", 10, "bold"),
            style="HeadingTitle.TLabel",
        )
        self.heading_title_label.pack(anchor=tk.W)

        heading_tree_wrap = ttk.Frame(self.heading_frame, style="HeadingPane.TFrame")
        heading_tree_wrap.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        self.heading_tree = ttk.Treeview(heading_tree_wrap, show="tree", style="Heading.Treeview")
        self.heading_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        heading_scrollbar = ttk.Scrollbar(heading_tree_wrap, orient=tk.VERTICAL, command=self.heading_tree.yview)
        heading_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.heading_tree.configure(yscrollcommand=heading_scrollbar.set)

        self.heading_tree.bind("<<TreeviewSelect>>", self._on_heading_selected)
        self._bind_mousewheel_scroll(self.heading_tree)

        # Document content
        self.content_frame = ttk.Frame(
            self.main_pane,
            padding=(8, 6, 8, 6),
            style="DocumentPane.TFrame",
        )
        self.main_pane.add(self.content_frame, minsize=420, stretch="always")

        self.document_label_var = tk.StringVar(value="No document loaded")
        self.document_label = ttk.Label(
            self.content_frame,
            textvariable=self.document_label_var,
            font=("Segoe UI", 11, "bold"),
            style="DocumentTitle.TLabel",
        )
        self.document_label.pack(anchor=tk.W, padx=(2, 0), pady=(0, 4))

        # Reader border: same visual discipline as the side panes.
        self.reader_border = tk.Frame(
            self.content_frame,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#cfcfcf",
            highlightcolor="#cfcfcf",
        )
        self.reader_border.pack(fill=tk.BOTH, expand=True)

        text_wrap = tk.Frame(self.reader_border, borderwidth=0, highlightthickness=0)
        self.text_wrap = text_wrap
        text_wrap.pack(fill=tk.BOTH, expand=True)

        self.text = tk.Text(
            text_wrap,
            wrap=tk.WORD,
            undo=False,
            padx=18,
            pady=14,
            font=self.base_font,
            borderwidth=0,
            highlightthickness=0,
        )
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_yscroll = ttk.Scrollbar(text_wrap, orient=tk.VERTICAL, command=self.text.yview)
        self.text_yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.configure(yscrollcommand=self._on_text_yscroll)
        self.text.bind("<Configure>", self._on_text_configure)

        self._configure_text_tags()

        self.status_var = tk.StringVar(value="Starting ...")
        self.status_label = ttk.Label(
            self,
            textvariable=self.status_var,
            anchor=tk.W,
            padding=(6, 3),
            style="Status.TLabel",
        )
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)

    def _build_toolbar(self) -> None:
        self.toolbar = ttk.Frame(self, padding=(6, 6, 6, 3))
        self.toolbar.pack(fill=tk.X)

        ttk.Button(self.toolbar, text="Open Folder", command=self._open_folder).pack(side=tk.LEFT)
        ttk.Button(self.toolbar, text="Open ZIP", command=self._open_zip).pack(side=tk.LEFT, padx=(6, 10))

        ttk.Label(self.toolbar, text="Search").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self._search_entry = ttk.Entry(self.toolbar, textvariable=self.search_var, width=42)
        self._search_entry.pack(side=tk.LEFT, padx=(6, 4))
        self._search_entry.bind("<Return>", lambda event: self.run_search())
        ttk.Button(self.toolbar, text="Search", command=self.run_search).pack(side=tk.LEFT)
        ttk.Button(self.toolbar, text="Clear", command=self.clear_search).pack(side=tk.LEFT, padx=(4, 12))

        ttk.Button(self.toolbar, text="Reload", command=self.reload_source).pack(side=tk.LEFT)
        ttk.Button(self.toolbar, text="Home", command=self.open_home).pack(side=tk.LEFT, padx=(6, 12))

        ttk.Button(self.toolbar, text="A−", command=self.decrease_reader_font).pack(side=tk.LEFT)
        ttk.Button(self.toolbar, text="A+", command=self.increase_reader_font).pack(side=tk.LEFT, padx=(4, 12))

        self.fullscreen_button = ttk.Button(
            self.toolbar,
            text="Reader Fullscreen",
            command=self.toggle_reader_fullscreen,
        )
        self.fullscreen_button.pack(side=tk.LEFT, padx=(0, 8))

        ttk.Button(self.toolbar, text="Graph Lab", command=self.open_graph_lab).pack(side=tk.LEFT, padx=(0, 8))

        self.theme_button = ttk.Button(self.toolbar, text="Dark Mode", command=self.toggle_dark_mode)
        self.theme_button.pack(side=tk.LEFT)

        ttk.Button(self.toolbar, text="Exit", command=self.destroy).pack(side=tk.RIGHT)
        ttk.Button(self.toolbar, text="Help", command=self.show_help).pack(side=tk.RIGHT, padx=(0, 6))

    def _build_fullscreen_toolbar(self) -> None:
        self.fullscreen_toolbar = ttk.Frame(self, padding=(8, 6, 8, 4))

        ttk.Button(
            self.fullscreen_toolbar,
            text="A−",
            command=self.decrease_reader_font,
        ).pack(side=tk.LEFT)

        ttk.Button(
            self.fullscreen_toolbar,
            text="A+",
            command=self.increase_reader_font,
        ).pack(side=tk.LEFT, padx=(4, 12))

        ttk.Label(
            self.fullscreen_toolbar,
            text="Reader Fullscreen",
            font=("Segoe UI", 10, "bold"),
        ).pack(side=tk.LEFT)

        ttk.Button(
            self.fullscreen_toolbar,
            text="Exit Fullscreen",
            command=self.exit_reader_fullscreen,
        ).pack(side=tk.RIGHT)

        ttk.Button(
            self.fullscreen_toolbar,
            text="Help",
            command=self.show_help,
        ).pack(side=tk.RIGHT, padx=(0, 6))

    def _configure_text_tags(self) -> None:
        self.text.tag_configure("h1", font=self.heading_font_1, spacing1=22, spacing3=12, lmargin1=14, lmargin2=14)
        self.text.tag_configure("h2", font=self.heading_font_2, spacing1=20, spacing3=10, lmargin1=14, lmargin2=14)
        self.text.tag_configure("h3", font=self.heading_font_3, spacing1=16, spacing3=8, lmargin1=14, lmargin2=14)
        self.text.tag_configure("h4", font=self.heading_font_4, spacing1=14, spacing3=7, lmargin1=14, lmargin2=14)
        self.text.tag_configure("h5", font=self.heading_font_4, spacing1=12, spacing3=6, lmargin1=14, lmargin2=14)
        self.text.tag_configure("h6", font=self.heading_font_4, spacing1=12, spacing3=6, lmargin1=14, lmargin2=14)

        self.text.tag_configure("body", font=self.base_font, lmargin1=8, lmargin2=8)
        self.text.tag_configure("bold", font=self.bold_font)
        self.text.tag_configure("italic", font=self.italic_font)
        self.text.tag_configure("bold_italic", font=self.bold_italic_font)
        self.text.tag_configure("list", font=self.base_font, lmargin1=28, lmargin2=46, spacing1=1, spacing3=1)
        self.text.tag_configure("code", font=self.mono_font, background="#f4f4f4", lmargin1=28, lmargin2=28, spacing1=8, spacing3=8)
        self.text.tag_configure("inline_code", font=self.mono_font, background="#f4f4f4")
        self.text.tag_configure("yaml_key", font=self.mono_font, background="#f4f4f4", foreground="#7a3e9d", lmargin1=28, lmargin2=28)
        self.text.tag_configure("yaml_value", font=self.mono_font, background="#f4f4f4", foreground="#555555", lmargin1=28, lmargin2=28)
        self.text.tag_configure("quote", lmargin1=24, lmargin2=24, foreground="#555555")
        self.text.tag_configure("table", font=self.mono_font, lmargin1=24, lmargin2=24, spacing1=4, spacing3=4)
        self.text.tag_configure("rule", foreground="#777777")
        self.text.tag_configure("search", background="#fff2a8")
        self.text.tag_configure("current_line", background="#eef5ff")
        self.text.tag_configure("link", foreground="#0563c1", underline=True)
        self.text.tag_configure("link_hover", background="#dceeff")
        self.text.tag_configure(
            "loading",
            font=("Segoe UI", 14, "bold"),
            justify=tk.CENTER,
            spacing1=180,
            spacing3=20,
        )

    def toggle_dark_mode(self) -> None:
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self) -> None:
        if self.dark_mode:
            bg = "#151617"
            navigation_bg = "#1c1e20"
            heading_bg = "#202326"
            document_panel_bg = "#17191b"
            panel_bg = navigation_bg
            fg = "#d4d4d4"
            muted_fg = "#a0a0a0"
            text_bg = "#101214"
            text_fg = "#d4d4d4"
            code_bg = "#1b1e21"
            button_bg = "#333333"
            button_hover_bg = "#404040"
            selection_bg = "#3a3d41"
            current_line_bg = "#2a2d2e"
            search_bg = "#665c00"
            rule_fg = "#777777"
            yaml_key_fg = "#ce9178"
            yaml_value_fg = "#b5cea8"
            reader_border_fg = "#34383c"
            link_fg = "#6cb6ff"
            link_hover_bg = "#24384a"
            self.theme_button.configure(text="Light Mode")
        else:
            bg = "#f0f0f0"
            navigation_bg = "#f2f4f6"
            heading_bg = "#f7f8fa"
            document_panel_bg = "#ffffff"
            panel_bg = navigation_bg
            fg = "#000000"
            muted_fg = "#555555"
            text_bg = "#ffffff"
            text_fg = "#000000"
            code_bg = "#f4f4f4"
            button_bg = "#f0f0f0"
            button_hover_bg = "#e5e5e5"
            selection_bg = "#cde8ff"
            current_line_bg = "#eef5ff"
            search_bg = "#fff2a8"
            rule_fg = "#777777"
            yaml_key_fg = "#7a3e9d"
            yaml_value_fg = "#555555"
            reader_border_fg = "#cfcfcf"
            link_fg = "#0563c1"
            link_hover_bg = "#dceeff"
            self.theme_button.configure(text="Dark Mode")

        self.configure(background=bg)

        # Native paned windows keep resize handles visible in both themes.
        sash_bg = "#55595e" if self.dark_mode else "#9aa1a8"
        for pane in (getattr(self, "main_pane", None), getattr(self, "left_pane", None)):
            if pane is not None:
                pane.configure(
                    background=sash_bg,
                    sashrelief=tk.RAISED,
                    sashwidth=7,
                    showhandle=True,
                    handlesize=11,
                    handlepad=2,
                )

        style = ttk.Style(self)
        style.configure(".", background=bg, foreground=fg)
        style.configure("TFrame", background=bg)
        style.configure("TLabel", background=bg, foreground=fg)
        style.configure("Navigation.TFrame", background=navigation_bg)
        style.configure("HeadingPane.TFrame", background=heading_bg)
        style.configure("DocumentPane.TFrame", background=document_panel_bg)
        style.configure("NavigationTitle.TLabel", background=navigation_bg, foreground=fg)
        style.configure("HeadingTitle.TLabel", background=heading_bg, foreground=fg)
        style.configure("DocumentTitle.TLabel", background=document_panel_bg, foreground=fg)
        style.configure("Status.TLabel", background=bg, foreground=muted_fg)
        style.configure("Table.TFrame", background=text_bg)
        style.configure("TButton", background=button_bg, foreground=fg)
        style.map(
            "TButton",
            background=[
                ("active", button_hover_bg),
                ("pressed", selection_bg),
                ("!active", button_bg),
            ],
            foreground=[
                ("active", fg),
                ("pressed", fg),
                ("!active", fg),
            ],
        )
        style.configure("TEntry", fieldbackground=text_bg, foreground=fg)
        style.configure(
            "Treeview",
            background=panel_bg,
            fieldbackground=panel_bg,
            foreground=fg,
        )
        style.map(
            "Treeview",
            background=[("selected", selection_bg)],
            foreground=[("selected", fg)],
        )
        style.configure("Corpus.Treeview", background=navigation_bg, fieldbackground=navigation_bg, foreground=fg)
        style.configure("Search.Treeview", background=navigation_bg, fieldbackground=navigation_bg, foreground=fg)
        style.configure("Heading.Treeview", background=heading_bg, fieldbackground=heading_bg, foreground=fg)
        style.configure("Data.Treeview", background=text_bg, fieldbackground=text_bg, foreground=text_fg, rowheight=26)
        for tree_style in ("Corpus.Treeview", "Search.Treeview", "Heading.Treeview", "Data.Treeview"):
            style.map(
                tree_style,
                background=[("selected", selection_bg)],
                foreground=[("selected", fg)],
            )
        style.configure("Data.Treeview.Heading", background=button_bg, foreground=fg, relief="flat")
        style.map("Data.Treeview.Heading", background=[("active", button_hover_bg)])

        if hasattr(self, "reader_border"):
            self.reader_border.configure(
                background=reader_border_fg,
                highlightbackground=reader_border_fg,
                highlightcolor=reader_border_fg,
            )

        self.text.configure(
            background=text_bg,
            foreground=text_fg,
            insertbackground=text_fg,
        )
        if hasattr(self, "text_wrap"):
            self.text_wrap.configure(background=text_bg)

        for tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.text.tag_configure(tag, background=text_bg, foreground=text_fg)

        self.text.tag_configure("body", background=text_bg, foreground=text_fg)
        self.text.tag_configure("bold", background=text_bg, foreground=text_fg)
        self.text.tag_configure("italic", background=text_bg, foreground=text_fg)
        self.text.tag_configure("bold_italic", background=text_bg, foreground=text_fg)
        self.text.tag_configure("list", background=text_bg, foreground=text_fg)
        self.text.tag_configure("code", background=code_bg, foreground=text_fg)
        self.text.tag_configure("inline_code", background=code_bg, foreground=text_fg)
        self.text.tag_configure("yaml_key", background=code_bg, foreground=yaml_key_fg)
        self.text.tag_configure("yaml_value", background=code_bg, foreground=yaml_value_fg)
        self.text.tag_configure("quote", background=text_bg, foreground=muted_fg)
        self.text.tag_configure("table", background=text_bg, foreground=text_fg)
        self.text.tag_configure("rule", background=text_bg, foreground=rule_fg)
        self.text.tag_configure("search", background=search_bg, foreground=text_fg)
        self.text.tag_configure("current_line", background=current_line_bg)
        self.text.tag_configure("link", background=text_bg, foreground=link_fg)
        self.text.tag_configure("link_hover", background=link_hover_bg, foreground=link_fg)
        self.text.tag_configure("loading", background=text_bg, foreground=text_fg)

        if self.graph_lab is not None and self.graph_lab.winfo_exists():
            self.graph_lab.apply_theme()

    def _on_text_configure(self, _event: tk.Event) -> None:
        self._schedule_heading_sync()
        if self._table_resize_after_id is not None:
            try:
                self.after_cancel(self._table_resize_after_id)
            except tk.TclError:
                pass
        self._table_resize_after_id = self.after(40, self._resize_embedded_tables)

    def _resize_embedded_tables(self) -> None:
        self._table_resize_after_id = None
        available_width = max(320, self.text.winfo_width() - 44)
        live_frames: List[tk.Widget] = []
        for frame in self._embedded_tables:
            try:
                if not frame.winfo_exists():
                    continue
                live_frames.append(frame)
                tree = getattr(frame, "_table_tree", None)
                xscroll = getattr(frame, "_table_xscroll", None)
                if tree is None or xscroll is None:
                    continue
                frame.configure(width=available_width)
                tree.update_idletasks()
                scroll_height = xscroll.winfo_reqheight() if xscroll.winfo_manager() == "grid" else 0
                frame.configure(height=tree.winfo_reqheight() + scroll_height + 4)
            except tk.TclError:
                continue
        self._embedded_tables = live_frames

    def _configure_clickable_cursors(self) -> None:
        """Apply consistent interaction cursors without changing semantics."""
        for widget in walk_widgets(self):
            try:
                if isinstance(widget, ttk.Button):
                    widget.configure(cursor="hand2")
                elif isinstance(widget, ttk.Treeview):
                    widget.configure(cursor="hand2")
            except tk.TclError:
                pass
        try:
            self.text.configure(cursor="xterm")
        except tk.TclError:
            pass

    def _set_initial_pane_positions(self) -> None:
        """Keep Corpus, Search Results, Headings, and Reader visible at startup."""
        try:
            self.update_idletasks()
            width = max(self.main_pane.winfo_width(), 960)
            left_width = max(230, min(int(width * 0.19), width - 650))
            heading_width = max(200, min(int(width * 0.17), width - left_width - 440))
            self.main_pane.sash_place(0, left_width, 1)
            self.main_pane.sash_place(1, left_width + heading_width, 1)

            height = max(self.left_pane.winfo_height(), 500)
            corpus_height = max(180, min(int(height * 0.58), height - 140))
            self.left_pane.sash_place(0, 1, corpus_height)
        except (tk.TclError, IndexError):
            pass

    def _bind_mousewheel_scroll(self, widget: tk.Widget) -> None:
        """Make mouse-wheel scrolling work reliably for Treeview-like widgets.

        Tk/ttk scrolling behavior differs between Windows, macOS, and Linux.
        Binding directly to each navigation tree keeps Corpus, Search Results,
        and Headings scrollable even before they have keyboard focus.
        """
        widget.bind("<MouseWheel>", lambda event, w=widget: self._on_mousewheel_scroll(event, w))
        widget.bind("<Button-4>", lambda event, w=widget: self._on_linux_mousewheel_scroll(event, w, -1))
        widget.bind("<Button-5>", lambda event, w=widget: self._on_linux_mousewheel_scroll(event, w, 1))

    def _on_mousewheel_scroll(self, event: tk.Event, widget: tk.Widget) -> str:
        delta = getattr(event, "delta", 0)

        if delta == 0:
            return "break"

        # Windows usually sends +/-120. macOS can send smaller values.
        if abs(delta) >= 120:
            units = -int(delta / 120)
        else:
            units = -1 if delta > 0 else 1

        try:
            widget.yview_scroll(units, "units")
        except tk.TclError:
            pass

        return "break"

    def _on_linux_mousewheel_scroll(self, event: tk.Event, widget: tk.Widget, units: int) -> str:
        try:
            widget.yview_scroll(units, "units")
        except tk.TclError:
            pass

        return "break"

    def _on_text_yscroll(self, first: str, last: str) -> None:
        self.text_yscroll.set(first, last)
        self._schedule_heading_sync()

    def _schedule_heading_sync(self) -> None:
        if self._heading_sync_after_id is not None:
            try:
                self.after_cancel(self._heading_sync_after_id)
            except tk.TclError:
                pass
        self._heading_sync_after_id = self.after(120, self._sync_heading_from_scroll)

    def _refresh_heading_positions(self) -> None:
        positions: List[Tuple[int, str, str]] = []
        for anchor, index in self.heading_indices.items():
            item = self._heading_anchor_to_item.get(anchor)
            if not item:
                continue
            try:
                line_number = int(self.text.index(index).split(".", 1)[0])
            except (tk.TclError, ValueError):
                continue
            positions.append((line_number, item, anchor))
        self._heading_positions = sorted(positions, key=lambda entry: entry[0])

    def _sync_heading_from_scroll(self) -> None:
        self._heading_sync_after_id = None
        if (
            not self._heading_positions
            or self._active_render_doc is not None
            or time.monotonic() < self._manual_heading_until
        ):
            return
        try:
            top_line = int(self.text.index("@0,0").split(".", 1)[0]) + 2
        except (tk.TclError, ValueError):
            return
        lines = [entry[0] for entry in self._heading_positions]
        position = max(0, bisect.bisect_right(lines, top_line) - 1)
        _line, item, _anchor = self._heading_positions[position]
        if self.heading_tree.selection() == (item,):
            return
        self._suppress_heading_select_event = True
        try:
            self.heading_tree.selection_set(item)
            self.heading_tree.focus(item)
            self.heading_tree.see(item)
        finally:
            self.after_idle(self._enable_heading_select_events)

    def _center_window(self) -> None:
        """Center the main window on the current screen after widgets exist."""
        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()

        if width <= 1 or height <= 1:
            geometry = self.geometry().split("+", 1)[0]
            width_text, height_text = geometry.split("x", 1)
            width = int(width_text)
            height = int(height_text)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = max(0, (screen_width - width) // 2)
        y = max(0, (screen_height - height) // 2)

        self.geometry(f"{width}x{height}+{x}+{y}")

    def show_help(self) -> None:
        messagebox.showinfo(
            f"{APP_TITLE} Help",
            "PMS-STRATA Reader controls\n\n"
            "Navigation:\n"
            "  Open Folder / Open ZIP  Load a PMS-STRATA corpus\n"
            "  Home                    Open the preferred start document\n"
            "  Reload                  Reload the current corpus\n\n"
            "Search:\n"
            "  Ctrl+F                  Focus search field\n"
            "  Enter                   Search from search field\n"
            "  Double-click result     Open search result\n\n"
            "Reader:\n"
            "  Click link              Open internal links in Reader\n"
            "  External link           Confirm before browser opening\n"
            "  Scroll document         Synchronize active heading\n"
            "  A+ / Ctrl++             Increase reader font size\n"
            "  A− / Ctrl+-             Decrease reader font size\n"
            "  Ctrl+0                  Reset reader font size\n"
            "  F11                     Toggle reader fullscreen\n"
            "  Esc                     Exit reader fullscreen\n\n"
            "Graph Lab:\n"
            "  Graph Lab               Open the interactive graph window\n"
            "  Drag                     Rotate the pseudo-3D graph\n"
            "  Mouse wheel              Zoom\n"
            "  Double-click node        Open its repository artifact\n\n"
            "Theme:\n"
            "  Dark Mode               Toggle light / dark mode\n\n"
            "The graph layer visualizes declared relations only; it does not create theory, evidence, routes, or authority.",
        )

    def increase_reader_font(self) -> None:
        self.set_reader_font_size(self.reader_font_size + 1)

    def decrease_reader_font(self) -> None:
        self.set_reader_font_size(self.reader_font_size - 1)

    def reset_reader_font(self) -> None:
        self.set_reader_font_size(10)

    def set_reader_font_size(self, size: int) -> None:
        self.reader_font_size = max(8, min(24, size))
        self._apply_reader_font_sizes()
        self.status_var.set(f"Reader font size: {self.reader_font_size}")

    def _apply_reader_font_sizes(self) -> None:
        size = self.reader_font_size

        self.base_font.configure(size=size)
        self.bold_font.configure(size=size)
        self.italic_font.configure(size=size)
        self.bold_italic_font.configure(size=size)
        self.mono_font.configure(size=size)

        self.heading_font_1.configure(size=size + 8)
        self.heading_font_2.configure(size=size + 5)
        self.heading_font_3.configure(size=size + 3)
        self.heading_font_4.configure(size=size + 1)

        self.text.configure(font=self.base_font)

    def toggle_reader_fullscreen(self) -> None:
        if self.reader_fullscreen:
            self.exit_reader_fullscreen()
        else:
            self.enter_reader_fullscreen()

    def enter_reader_fullscreen(self) -> None:
        if self.reader_fullscreen:
            return

        self.reader_fullscreen = True
        self._normal_geometry = self.geometry()

        self.toolbar.pack_forget()
        self.status_label.pack_forget()
        self.fullscreen_toolbar.pack(fill=tk.X, before=self.main_pane)

        try:
            self.main_pane.forget(self.left_pane)
        except tk.TclError:
            pass

        try:
            self.main_pane.forget(self.heading_frame)
        except tk.TclError:
            pass

        self.attributes("-fullscreen", True)
        self.fullscreen_button.configure(text="Exit Fullscreen")
        self.text.focus_set()

    def exit_reader_fullscreen(self) -> None:
        if not self.reader_fullscreen:
            return

        self.reader_fullscreen = False
        self.attributes("-fullscreen", False)

        self.fullscreen_toolbar.pack_forget()

        try:
            self.main_pane.forget(self.content_frame)
        except tk.TclError:
            pass

        self.main_pane.add(self.left_pane, minsize=230, stretch="always")
        self.main_pane.add(self.heading_frame, minsize=200, stretch="always")
        self.main_pane.add(self.content_frame, minsize=420, stretch="always")

        self.toolbar.pack(fill=tk.X, before=self.main_pane)
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)

        if self._normal_geometry:
            self.geometry(self._normal_geometry)

        self.after_idle(self._set_initial_pane_positions)

        self.fullscreen_button.configure(text="Reader Fullscreen")
        self.text.focus_set()

    def _bind_shortcuts(self) -> None:
        self.bind("<Control-o>", lambda event: self._open_folder())
        self.bind("<Control-f>", self._focus_search)
        self.bind("<F5>", lambda event: self.reload_source())
        self.bind("<F1>", lambda event: self.show_help())
        self.bind("<Control-g>", lambda event: self.open_graph_lab())

        self.bind("<Control-plus>", lambda event: self.increase_reader_font())
        self.bind("<Control-equal>", lambda event: self.increase_reader_font())
        self.bind("<Control-KP_Add>", lambda event: self.increase_reader_font())

        self.bind("<Control-minus>", lambda event: self.decrease_reader_font())
        self.bind("<Control-KP_Subtract>", lambda event: self.decrease_reader_font())

        self.bind("<Control-0>", lambda event: self.reset_reader_font())
        self.bind("<F11>", lambda event: self.toggle_reader_fullscreen())
        self.bind("<Escape>", lambda event: self.exit_reader_fullscreen())

    def _focus_search(self, event: tk.Event) -> str:
        if self._search_entry is not None:
            self._search_entry.focus_set()
            self._search_entry.selection_range(0, tk.END)
        return "break"

    # ------------------------------------------------------------------ #
    # Source loading (UI-thread side)                                    #
    # ------------------------------------------------------------------ #

    def load_source(self, source_path: Path) -> None:
        """Called from the UI thread; kicks off a background load."""
        self._start_load_thread(source_path)

    def reload_source(self) -> None:
        if self.corpus is None:
            return
        source_path = self.corpus.source.source_path
        self.load_source(source_path)

    def open_home(self) -> None:
        if self.corpus is None:
            return
        for candidate in PREFERRED_HOME_FILES:
            if candidate in self.corpus.documents:
                self.open_document(candidate)
                return

    def open_graph_lab(self) -> None:
        if self.corpus is None:
            return
        if self.graph_lab is None or not self.graph_lab.winfo_exists():
            self.graph_lab = GraphLab(self)
        else:
            self.graph_lab.deiconify()
            self.graph_lab.lift()
            self.graph_lab.apply_theme()
            self.graph_lab.refresh()
            self.graph_lab.after_idle(self.graph_lab._maximize)

    # ------------------------------------------------------------------ #
    # Tree population                                                    #
    # ------------------------------------------------------------------ #

    def populate_file_tree(self) -> None:
        dbg("populate_file_tree: start")
        self.file_tree.delete(*self.file_tree.get_children())
        self._file_item_to_path.clear()
        if self.corpus is None:
            return

        section_items: Dict[str, str] = {}
        folder_items: Dict[Tuple[str, str], str] = {}

        for rel_path in self.corpus.ordered_paths:
            section_key = rel_path.split("/", 1)[0] if "/" in rel_path else rel_path
            section_label = SECTION_LABELS.get(section_key, section_key)
            if section_key not in section_items:
                section_items[section_key] = self.file_tree.insert("", tk.END, text=section_label, open=True)

            parent = section_items[section_key]
            parts = rel_path.split("/")
            for depth, folder in enumerate(parts[1:-1], start=1):
                key = (section_key, "/".join(parts[1:depth + 1]))
                if key not in folder_items:
                    folder_items[key] = self.file_tree.insert(parent, tk.END, text=folder, open=(depth < 2))
                parent = folder_items[key]

            doc = self.corpus.documents[rel_path]
            display_title = CANONICAL_BLOCK_LABELS.get(rel_path, doc.title)
            item = self.file_tree.insert(parent, tk.END, text=display_title, open=False)
            self._file_item_to_path[item] = rel_path

        dbg(f"populate_file_tree: inserted {len(self._file_item_to_path)} file items")

    def populate_heading_tree(self, doc: Document) -> None:
        self.heading_tree.delete(*self.heading_tree.get_children())
        self._heading_item_to_anchor.clear()
        self._heading_anchor_to_item.clear()

        parent_by_level: Dict[int, str] = {0: ""}
        for heading in doc.headings:
            parent_level = heading.level - 1
            while parent_level > 0 and parent_level not in parent_by_level:
                parent_level -= 1
            parent = parent_by_level.get(parent_level, "")
            label = f"{'  ' * max(0, heading.level - 1)}{heading.text}"
            item = self.heading_tree.insert(parent, tk.END, text=label, open=True)
            self._heading_item_to_anchor[item] = heading.anchor
            self._heading_anchor_to_item[heading.anchor] = item
            parent_by_level[heading.level] = item
            for deeper in list(parent_by_level):
                if deeper > heading.level:
                    del parent_by_level[deeper]

    # ------------------------------------------------------------------ #
    # Document rendering                                                 #
    # ------------------------------------------------------------------ #

    def open_document(
        self,
        rel_path: str,
        line_number: Optional[int] = None,
        anchor_name: Optional[str] = None,
    ) -> None:
        if self.corpus is None or rel_path not in self.corpus.documents:
            return

        if self.current_path == rel_path:
            if anchor_name:
                self.scroll_to_anchor(anchor_name)
            elif line_number is not None:
                self.scroll_to_source_line(line_number)
            return

        dbg(f"open_document: {rel_path}")
        self._cancel_active_render()
        doc = self.corpus.documents[rel_path]
        self.current_path = rel_path
        self.document_label_var.set(f"{doc.title} — {rel_path}")
        self.populate_heading_tree(doc)
        self._select_file_tree_item(rel_path)
        self._pending_line_number = line_number
        self._pending_anchor = anchor_name

        rendered_now = self.render_document(doc)
        if rendered_now:
            self._finish_document_render(doc)

        if self.graph_lab is not None and self.graph_lab.winfo_exists():
            self.graph_lab.set_current_path(rel_path)

    def _document_status(self, doc: Document) -> str:
        record = self.corpus.record_for_path(doc.rel_path) if self.corpus is not None else None
        record_suffix = f" • {record.operation} → {record.output_class}" if record else ""
        return (
            f"{doc.rel_path} — {doc.line_count:,} lines, {doc.word_count:,} words, "
            f"{len(doc.headings):,} headings{record_suffix}"
        )

    def _should_chunk_render(self, doc: Document) -> bool:
        return (
            doc.line_count > CHUNKED_RENDER_LINE_THRESHOLD
            or doc.byte_count > CHUNKED_RENDER_BYTE_THRESHOLD
        ) and doc.file_type in {"md", "yaml", "yml", "json", "txt", "py"}

    def render_document(self, doc: Document) -> bool:
        """Render a document and return True when rendering finished synchronously."""
        if self._should_chunk_render(doc):
            self._start_chunked_render(doc)
            return False
        if doc.file_type == "md":
            self.render_markdown(doc)
        elif doc.file_type in {"yaml", "yml"}:
            self.render_yaml(doc)
        elif doc.file_type == "json":
            self.render_json(doc)
        elif doc.file_type == "csv":
            self.render_csv(doc)
        else:
            self.render_plain(doc)
        return True

    def _reset_document_surface(self) -> None:
        for widget in self._embedded_tables:
            try:
                widget.destroy()
            except tk.TclError:
                pass
        self._embedded_tables.clear()

        for tag_name in self._link_tags:
            try:
                self.text.tag_delete(tag_name)
            except tk.TclError:
                pass
        self._link_tags.clear()
        self._next_link_id = 0

        self.heading_indices.clear()
        self._document_anchor_indices.clear()
        self._heading_positions.clear()
        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)

    def _cancel_active_render(self) -> None:
        self._render_generation += 1
        self._active_render_doc = None
        self._active_render_mode = ""
        self._active_render_total = 0
        self._active_render_inserted = 0
        self._pending_line_number = None
        self._pending_anchor = None
        if self._render_poll_after_id is not None:
            try:
                self.after_cancel(self._render_poll_after_id)
            except tk.TclError:
                pass
            self._render_poll_after_id = None

    def _show_loading(self, doc: Document) -> None:
        self._reset_document_surface()
        self.heading_tree.state(["disabled"])
        self.text.insert(
            "1.0",
            f"Loading {Path(doc.rel_path).name}…\n\nPreparing seamless audit view.",
            ("loading",),
        )
        self.text.configure(state=tk.DISABLED)
        self.status_var.set(f"Loading {doc.rel_path}…")

    def _start_chunked_render(self, doc: Document) -> None:
        generation = self._render_generation
        self._active_render_doc = doc
        self._active_render_mode = ""
        self._active_render_total = 0
        self._active_render_inserted = 0
        self._chunk_heading_counter = 0
        self._show_loading(doc)
        worker = threading.Thread(
            target=self._prepare_document_chunks,
            args=(generation, doc),
            daemon=True,
        )
        worker.start()
        self._schedule_render_poll()

    def _prepare_document_chunks(self, generation: int, doc: Document) -> None:
        """Prepare document chunks in a worker. Never touches Tk widgets."""
        try:
            if doc.file_type == "md":
                mode = "markdown"
                chunks = chunk_markdown_text(strip_frontmatter(doc.text), CHUNK_TARGET_BYTES)
            elif doc.file_type in {"yaml", "yml"}:
                mode = "yaml_plain"
                chunks = chunk_text_by_bytes(doc.text, CHUNK_TARGET_BYTES)
            else:
                mode = "code" if doc.file_type in {"json", "py"} else "body"
                chunks = chunk_text_by_bytes(doc.text, CHUNK_TARGET_BYTES)

            self._render_queue.put(("start", generation, doc.rel_path, mode, len(chunks)))
            for block_number, chunk in enumerate(chunks, start=1):
                self._render_queue.put(("chunk", generation, doc.rel_path, block_number, chunk))
            self._render_queue.put(("done", generation, doc.rel_path))
        except Exception as exc:
            self._render_queue.put(("error", generation, doc.rel_path, str(exc)))

    def _schedule_render_poll(self) -> None:
        if self._render_poll_after_id is None:
            self._render_poll_after_id = self.after(20, self._poll_render_queue)

    def _poll_render_queue(self) -> None:
        self._render_poll_after_id = None
        processed = 0
        while processed < 4:
            try:
                message = self._render_queue.get_nowait()
            except queue.Empty:
                break
            processed += 1
            kind = message[0]
            generation = message[1]
            rel_path = message[2]
            if generation != self._render_generation or rel_path != self.current_path:
                continue

            if kind == "start":
                _kind, _generation, _path, mode, total = message
                self._active_render_mode = mode
                self._active_render_total = total
                self._active_render_inserted = 0
                self._reset_document_surface()
                self.text.configure(state=tk.NORMAL)
            elif kind == "chunk":
                _kind, _generation, _path, block_number, chunk = message
                self._insert_prepared_chunk(chunk)
                self._active_render_inserted = block_number
                total = max(1, self._active_render_total)
                self.status_var.set(
                    f"Loading {rel_path}… {block_number:,} / {total:,} blocks"
                )
            elif kind == "done":
                self.text.configure(state=tk.DISABLED)
                doc = self._active_render_doc
                self._active_render_doc = None
                self.heading_tree.state(["!disabled"])
                if doc is not None:
                    if self._active_render_mode == "yaml_plain":
                        self._install_outline_indices(doc)
                    self._finish_document_render(doc)
                return
            elif kind == "error":
                _kind, _generation, _path, error_message = message
                self.text.configure(state=tk.DISABLED)
                self.heading_tree.state(["!disabled"])
                self._active_render_doc = None
                self.status_var.set(f"Render error: {error_message}")
                messagebox.showerror(APP_TITLE, f"Could not render {rel_path}:\n\n{error_message}")
                return

        if self._active_render_doc is not None:
            self._schedule_render_poll()

    def _insert_prepared_chunk(self, chunk: RenderChunk) -> None:
        mode = self._active_render_mode
        if mode == "markdown":
            self._chunk_heading_counter = self._render_markdown_blocks(
                self._active_render_doc,
                chunk.text,
                use_source_marks=False,
                source_line_offset=chunk.start_line - 1,
                heading_counter_start=self._chunk_heading_counter,
            )
        else:
            tag = "code" if mode in {"yaml_plain", "code"} else "body"
            self.text.insert(tk.END, chunk.text, (tag,))

    def _finish_document_render(self, doc: Document) -> None:
        self.text.configure(state=tk.DISABLED)
        if doc.file_type in {"yaml", "yml"} and not self.heading_indices:
            self._install_outline_indices(doc)
        self._refresh_heading_positions()
        self.highlight_query()

        if self._pending_anchor:
            pending = self._pending_anchor
            self._pending_anchor = None
            self.scroll_to_anchor(pending)
        elif self._pending_line_number is not None:
            pending_line = self._pending_line_number
            self._pending_line_number = None
            self.scroll_to_source_line(pending_line)
        else:
            self.text.yview_moveto(0)

        self.status_var.set(self._document_status(doc))
        self._schedule_heading_sync()

    def _install_outline_indices(self, doc: Document) -> None:
        for heading in doc.headings:
            index = f"{max(1, heading.line_number)}.0"
            self.heading_indices[heading.anchor] = index
            self._document_anchor_indices.setdefault(slugify(heading.text), index)
            self._document_anchor_indices[heading.anchor] = index

    def render_yaml(self, doc: Document) -> None:
        self._reset_document_surface()
        for line_number, line in enumerate(doc.text.splitlines(), start=1):
            if doc.line_count <= LARGE_DOC_LINE_THRESHOLD:
                self.text.mark_set(f"source_line_{line_number}", self.text.index(tk.INSERT))
            self._insert_yaml_line(line)
        self.text.configure(state=tk.DISABLED)
        self._install_outline_indices(doc)

    def render_json(self, doc: Document) -> None:
        try:
            rendered = json.dumps(json.loads(doc.text), indent=2, ensure_ascii=False)
        except Exception:
            rendered = doc.text
        self._render_plain_text(rendered, "code")

    def render_csv(self, doc: Document) -> None:
        self._reset_document_surface()
        try:
            rows = list(csv.reader(doc.text.splitlines()))
            self._insert_table_widget(rows, sortable=True)
        except Exception as exc:
            dbg(f"render_csv: table fallback ({exc})")
            self.text.insert("1.0", doc.text, ("table",))
        self.text.configure(state=tk.DISABLED)

    def render_plain(self, doc: Document) -> None:
        self._render_plain_text(doc.text, "code" if doc.file_type == "py" else "body")

    def _render_plain_text(self, text: str, tag: str) -> None:
        self._reset_document_surface()
        self.text.insert("1.0", text, (tag,))
        self.text.configure(state=tk.DISABLED)

    def render_markdown(self, doc: Document) -> None:
        """Render Markdown without changing the source artifact."""
        dbg(f"render_markdown: {doc.rel_path} ({doc.line_count} lines)")
        body = strip_frontmatter(doc.text)
        self._reset_document_surface()
        try:
            use_source_marks = doc.line_count <= LARGE_DOC_LINE_THRESHOLD
            self._render_markdown_blocks(
                doc,
                body,
                use_source_marks=use_source_marks,
                source_line_offset=0,
                heading_counter_start=0,
            )
        except Exception as exc:
            dbg(f"render_markdown: exception: {exc}")
            self.status_var.set(f"Render error: {exc}")
        finally:
            self.text.configure(state=tk.DISABLED)

    def _render_markdown_blocks(
        self,
        doc: Optional[Document],
        body: str,
        use_source_marks: bool,
        source_line_offset: int = 0,
        heading_counter_start: int = 0,
    ) -> int:
        """Markdown-light block renderer with links, anchors, and table widgets."""
        lines = body.splitlines()
        i = 0
        heading_counter = heading_counter_start

        while i < len(lines):
            raw_line = lines[i]
            source_line = source_line_offset + i + 1
            line_start = self.text.index(tk.INSERT)

            if use_source_marks:
                self.text.mark_set(f"source_line_{source_line}", line_start)

            anchor_match = HTML_ANCHOR_RE.match(raw_line)
            if anchor_match:
                anchor_id = unquote(anchor_match.group(1).strip())
                self._document_anchor_indices[anchor_id] = line_start
                self._document_anchor_indices[slugify(anchor_id)] = line_start
                i += 1
                continue

            fence_match = FENCE_RE.match(raw_line)
            if fence_match:
                language = (fence_match.group(2) or "").lower()
                block_lines: List[str] = []
                i += 1
                while i < len(lines):
                    close_match = FENCE_RE.match(lines[i])
                    if close_match:
                        break
                    block_lines.append(lines[i])
                    i += 1
                if i < len(lines) and FENCE_RE.match(lines[i]):
                    i += 1
                self._insert_code_block(block_lines, language)
                continue

            heading_match = HEADING_RE.match(raw_line)
            if heading_match:
                level = min(len(heading_match.group(1)), 6)
                heading_text = clean_heading_text(heading_match.group(2))
                anchor = f"h-{heading_counter}-{slugify(heading_text)}"
                heading_counter += 1
                self.heading_indices[anchor] = line_start
                self._document_anchor_indices.setdefault(slugify(heading_text), line_start)
                self._document_anchor_indices[anchor] = line_start
                self._insert_inline_markdown(heading_text, (f"h{level}",))
                self.text.insert(tk.END, "\n", (f"h{level}",))
                i += 1
                continue

            if looks_like_table_line(raw_line):
                table_lines: List[str] = []
                while i < len(lines) and looks_like_table_line(lines[i]):
                    table_lines.append(lines[i])
                    i += 1
                self._insert_table_block(table_lines)
                continue

            list_match = LIST_RE.match(raw_line)
            if list_match:
                indent, _bullet, content = list_match.groups()
                level = max(0, len(indent.replace("\t", "    ")) // 2)
                self.text.insert(tk.END, "  " * level + "• ", ("list",))
                self._insert_inline_markdown(content, ("list",))
                self.text.insert(tk.END, "\n", ("list",))
                i += 1
                continue

            ordered_match = ORDERED_LIST_RE.match(raw_line)
            if ordered_match:
                indent, number, content = ordered_match.groups()
                level = max(0, len(indent.replace("\t", "    ")) // 2)
                self.text.insert(tk.END, "  " * level + f"{number}. ", ("list",))
                self._insert_inline_markdown(content, ("list",))
                self.text.insert(tk.END, "\n", ("list",))
                i += 1
                continue

            if raw_line.strip().startswith(">"):
                quote_text = re.sub(r"^\s*>\s?", "", raw_line)
                self._insert_inline_markdown(quote_text, ("quote",))
                self.text.insert(tk.END, "\n", ("quote",))
                i += 1
                continue

            if raw_line.strip() in {"---", "***", "___"}:
                self.text.insert(tk.END, "─" * 80 + "\n", ("rule",))
                i += 1
                continue

            self._insert_inline_markdown(raw_line, ("body",))
            self.text.insert(tk.END, "\n", ("body",))
            i += 1

        dbg(f"_render_markdown_blocks: done ({heading_counter} headings rendered)")
        return heading_counter

    def _insert_code_block(self, block_lines: List[str], language: str) -> None:
        """Insert a fenced code block without showing the fence markers."""
        if not block_lines:
            self.text.insert(tk.END, "\n", ("code",))
            return

        # Top margin.
        self.text.insert(tk.END, "\n", ("body",))

        if language in {"yaml", "yml"}:
            for raw_line in block_lines:
                self._insert_yaml_line(raw_line)
        else:
            block = "\n".join(block_lines)
            self.text.insert(tk.END, block + "\n", ("code",))

        # Bottom margin.
        self.text.insert(tk.END, "\n", ("body",))

    def _insert_yaml_line(self, raw_line: str) -> None:
        """Insert one YAML line with lightweight syntax coloring."""
        match = re.match(r"^(\s*)([A-Za-z0-9_.-]+)(\s*:\s*)(.*)$", raw_line)

        if not match:
            self.text.insert(tk.END, raw_line + "\n", ("code",))
            return

        indent, key, separator, value = match.groups()

        self.text.insert(tk.END, indent, ("code",))
        self.text.insert(tk.END, key, ("yaml_key",))
        self.text.insert(tk.END, separator, ("code",))
        self.text.insert(tk.END, value + "\n", ("yaml_value",))

    def _insert_inline_markdown(self, text: str, base_tags: Tuple[str, ...]) -> None:
        """Insert inline Markdown, including navigable internal/external links."""
        token_re = re.compile(
            r"(\[[^\]]+\]\([^)]+\)|`[^`]+`|\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*\n]+\*)"
        )
        pos = 0
        for match in token_re.finditer(text):
            if match.start() > pos:
                self.text.insert(tk.END, text[pos:match.start()], base_tags)

            token = match.group(0)
            link_match = MARKDOWN_LINK_RE.fullmatch(token)
            if link_match:
                label, target = link_match.groups()
                self._insert_markdown_link(label, target, base_tags)
            elif token.startswith("`") and token.endswith("`"):
                self.text.insert(tk.END, token[1:-1], base_tags + ("inline_code",))
            elif token.startswith("***") and token.endswith("***"):
                self.text.insert(tk.END, token[3:-3], base_tags + ("bold_italic",))
            elif token.startswith("**") and token.endswith("**"):
                self.text.insert(tk.END, token[2:-2], base_tags + ("bold",))
            elif token.startswith("*") and token.endswith("*"):
                self.text.insert(tk.END, token[1:-1], base_tags + ("italic",))
            else:
                self.text.insert(tk.END, token, base_tags)
            pos = match.end()

        if pos < len(text):
            self.text.insert(tk.END, text[pos:], base_tags)

    def _insert_markdown_link(
        self,
        label: str,
        target: str,
        base_tags: Tuple[str, ...],
    ) -> None:
        tag_name = f"document_link_{self._next_link_id}"
        self._next_link_id += 1
        self._link_tags.append(tag_name)
        self.text.insert(tk.END, label, base_tags + ("link", tag_name))
        self.text.tag_bind(
            tag_name,
            "<Button-1>",
            lambda _event, link_target=target: self._open_markdown_link(link_target),
        )
        self.text.tag_bind(
            tag_name,
            "<Enter>",
            lambda _event, name=tag_name: self._set_link_hover(name, True),
        )
        self.text.tag_bind(
            tag_name,
            "<Leave>",
            lambda _event, name=tag_name: self._set_link_hover(name, False),
        )

    def _set_link_hover(self, tag_name: str, active: bool) -> None:
        ranges = self.text.tag_ranges(tag_name)
        if len(ranges) < 2:
            return
        if active:
            self.text.configure(cursor="hand2")
            self.text.tag_add("link_hover", ranges[0], ranges[1])
        else:
            self.text.configure(cursor="xterm")
            self.text.tag_remove("link_hover", ranges[0], ranges[1])

    def _open_markdown_link(self, raw_target: str) -> None:
        target = raw_target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()
        title_match = re.match(r'^(\S+?)(?:\s+["\'].*["\'])?$', target)
        if title_match:
            target = title_match.group(1)
        target = unquote(target)

        parsed = urlparse(target)
        if parsed.scheme.lower() in {"http", "https", "mailto"}:
            if messagebox.askyesno(
                "Open external link",
                f"Open this external destination in the default browser?\n\n{target}",
                parent=self,
            ):
                webbrowser.open_new_tab(target)
            return

        file_part, _separator, anchor = target.partition("#")
        if not file_part:
            self.scroll_to_anchor(anchor)
            return
        if self.corpus is None or self.current_path is None:
            return

        if file_part.startswith("/"):
            candidate = normalize_rel_path(posixpath.normpath(file_part))
        else:
            base_dir = posixpath.dirname(self.current_path)
            candidate = normalize_rel_path(posixpath.normpath(posixpath.join(base_dir, file_part)))

        if candidate.startswith("../") or candidate == "..":
            self._report_missing_link(target, "The target leaves the active repository root.")
            return
        if candidate not in self.corpus.documents:
            readme_candidate = normalize_rel_path(posixpath.join(candidate, "README.md"))
            if readme_candidate in self.corpus.documents:
                candidate = readme_candidate
            else:
                self._report_missing_link(target, f"No active Reader artifact exists at {candidate}.")
                return

        self.open_document(candidate, anchor_name=anchor or None)

    def _report_missing_link(self, target: str, reason: str) -> None:
        self.status_var.set(f"Link target unavailable: {target}")
        messagebox.showwarning(
            "Link target unavailable",
            f"The Reader could not open this link:\n\n{target}\n\n{reason}",
            parent=self,
        )

    def _insert_table_block(self, table_lines: List[str]) -> None:
        """Render a Markdown table as a real scrollable cell grid."""
        rows: List[List[str]] = []
        for line in table_lines:
            cells = split_markdown_table_row(line)
            if cells and all(re.fullmatch(r":?-{3,}:?", cell or "---") for cell in cells):
                continue
            rows.append(cells)
        self._insert_table_widget(rows, sortable=False)

    def _insert_table_widget(self, rows: List[List[str]], sortable: bool) -> None:
        if not rows:
            return
        column_count = max(len(row) for row in rows)
        normalized = [row + [""] * (column_count - len(row)) for row in rows]
        display_rows: List[List[str]] = []
        cell_links: Dict[Tuple[str, int], str] = {}
        for row_index, row in enumerate(normalized):
            display_row: List[str] = []
            for column_index, value in enumerate(row):
                label, link_target = markdown_link_cell(value)
                display_row.append(f"↗ {label}" if link_target else label)
                if row_index > 0 and link_target:
                    cell_links[(str(row_index - 1), column_index)] = link_target
            display_rows.append(display_row)

        headers = display_rows[0]
        data_rows = display_rows[1:]
        columns = tuple(f"c{index}" for index in range(column_count))

        frame = ttk.Frame(self.text, style="Table.TFrame", padding=(0, 2, 0, 2))
        tree_height = min(max(len(data_rows), 1), 16)
        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings",
            height=tree_height,
            style="Data.Treeview",
            selectmode="browse",
        )
        tree.grid(row=0, column=0, sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        xscroll = AutoHideScrollbar(frame, orient=tk.HORIZONTAL, command=tree.xview)
        xscroll.grid(row=1, column=0, sticky="ew")
        tree.configure(xscrollcommand=xscroll.set)

        if len(data_rows) > tree_height:
            yscroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
            yscroll.grid(row=0, column=1, sticky="ns")
            tree.configure(yscrollcommand=yscroll.set)

        sort_state: Dict[int, bool] = {}
        for index, column in enumerate(columns):
            header = headers[index].strip() or f"Column {index + 1}"
            values = [str(row[index]) for row in display_rows]
            max_chars = max((len(value) for value in values), default=8)
            width = max(90, min(420, max_chars * 8 + 24))
            command = None
            if sortable:
                command = lambda col=index: self._sort_table_column(tree, col, sort_state)
            if command is None:
                tree.heading(column, text=header)
            else:
                tree.heading(column, text=header, command=command)
            tree.column(column, width=width, minwidth=70, stretch=False, anchor=tk.W)

        for row_index, row in enumerate(data_rows):
            tree.insert("", tk.END, iid=str(row_index), values=row)

        def table_link_at(event: tk.Event) -> Optional[str]:
            item = tree.identify_row(event.y)
            column = tree.identify_column(event.x)
            if not item or not column.startswith("#"):
                return None
            try:
                column_index = int(column[1:]) - 1
            except ValueError:
                return None
            return cell_links.get((item, column_index))

        def on_table_motion(event: tk.Event) -> None:
            tree.configure(cursor="hand2" if table_link_at(event) else ("hand2" if sortable else "arrow"))

        def on_table_click(event: tk.Event) -> None:
            link_target = table_link_at(event)
            if link_target:
                self._open_markdown_link(link_target)

        tree.bind("<Motion>", on_table_motion)
        tree.bind("<ButtonRelease-1>", on_table_click)
        tree.configure(cursor="hand2" if sortable else "arrow")

        frame._table_tree = tree
        frame._table_xscroll = xscroll
        frame.grid_propagate(False)
        xscroll.visibility_callback = lambda _visible: self._resize_embedded_tables()
        self._embedded_tables.append(frame)
        self.text.insert(tk.END, "\n", ("body",))
        self.text.window_create(tk.END, window=frame, padx=8, pady=6, stretch=True)
        self.text.insert(tk.END, "\n\n", ("body",))
        self.after_idle(self._resize_embedded_tables)

    def _sort_table_column(
        self,
        tree: ttk.Treeview,
        column_index: int,
        sort_state: Dict[int, bool],
    ) -> None:
        descending = sort_state.get(column_index, False)
        rows = []
        for item in tree.get_children(""):
            values = tree.item(item, "values")
            value = values[column_index] if column_index < len(values) else ""
            rows.append((table_sort_value(str(value)), item))
        rows.sort(key=lambda pair: pair[0], reverse=descending)
        for position, (_value, item) in enumerate(rows):
            tree.move(item, "", position)
        sort_state[column_index] = not descending

    # ------------------------------------------------------------------ #
    # Search                                                             #
    # ------------------------------------------------------------------ #

    def run_search(self) -> None:
        if self.corpus is None:
            return
        query = self.search_var.get().strip()
        self.search_tree.delete(*self.search_tree.get_children())
        self.search_results = self.corpus.search(query)

        for index, (rel_path, line_no, snippet) in enumerate(self.search_results):
            title = self.corpus.documents[rel_path].title
            self.search_tree.insert("", tk.END, iid=str(index), values=(title, line_no, snippet))

        self.highlight_query()
        if query:
            self.status_var.set(f"Search '{query}': {len(self.search_results):,} result(s).")
        else:
            self.status_var.set("Search cleared.")

    def clear_search(self) -> None:
        self.search_var.set("")
        self.search_tree.delete(*self.search_tree.get_children())
        self.search_results = []
        self.text.configure(state=tk.NORMAL)
        self.text.tag_remove("search", "1.0", tk.END)
        self.text.configure(state=tk.DISABLED)

    def highlight_query(self) -> None:
        if self._active_render_doc is not None:
            return
        query = self.search_var.get().strip()
        self.text.configure(state=tk.NORMAL)
        self.text.tag_remove("search", "1.0", tk.END)
        if query:
            start = "1.0"
            count = 0
            while True:
                pos = self.text.search(query, start, stopindex=tk.END, nocase=True)
                if not pos:
                    break
                end = f"{pos}+{len(query)}c"
                self.text.tag_add("search", pos, end)
                start = end
                count += 1
                if count >= MAX_SEARCH_HIGHLIGHTS:
                    break
        self.text.configure(state=tk.DISABLED)

    def scroll_to_source_line(self, line_number: int) -> None:
        if self._active_render_doc is not None:
            self._pending_line_number = line_number
            return
        mark = f"source_line_{line_number}"

        try:
            index = self.text.index(mark)
        except tk.TclError:
            # Large documents do not create per-line marks.
            # Tk Text line indices are good enough for direct jumps.
            index = f"{max(1, line_number)}.0"

        self.text.configure(state=tk.NORMAL)
        self.text.tag_remove("current_line", "1.0", tk.END)
        self.text.tag_add("current_line", index, f"{index} lineend+1c")
        self.text.configure(state=tk.DISABLED)
        self.text.see(index)

    def scroll_to_anchor(self, anchor_name: str) -> None:
        anchor = unquote((anchor_name or "").lstrip("#").strip())
        if not anchor:
            return
        if self._active_render_doc is not None:
            self._pending_anchor = anchor
            return
        candidates = [anchor, anchor.lower(), slugify(anchor)]
        index = next(
            (self._document_anchor_indices[key] for key in candidates if key in self._document_anchor_indices),
            None,
        )
        if index is None:
            self._report_missing_link(f"#{anchor}", "No matching document anchor was found.")
            return
        self.text.see(index)
        self.text.configure(state=tk.NORMAL)
        self.text.tag_remove("current_line", "1.0", tk.END)
        self.text.tag_add("current_line", index, f"{index} lineend+1c")
        self.text.configure(state=tk.DISABLED)

    # ------------------------------------------------------------------ #
    # Toolbar / dialog actions                                           #
    # ------------------------------------------------------------------ #

    def _open_folder(self) -> None:
        path = filedialog.askdirectory(title="Open PMS-STRATA folder")
        if path:
            self.load_source(Path(path))

    def _open_zip(self) -> None:
        path = filedialog.askopenfilename(
            title="Open PMS-STRATA zip file",
            filetypes=[("Zip files", "*.zip"), ("All files", "*.*")],
        )
        if path:
            self.load_source(Path(path))

    # ------------------------------------------------------------------ #
    # Event handlers                                                     #
    # ------------------------------------------------------------------ #

    def _on_file_selected(self, event: tk.Event) -> None:
        if self._suppress_file_select_event:
            dbg("_on_file_selected: suppressed programmatic selection")
            return

        selection = self.file_tree.selection()
        if not selection:
            return

        item = selection[0]
        rel_path = self._file_item_to_path.get(item)
        if rel_path:
            self.open_document(rel_path)

    def _on_heading_selected(self, event: tk.Event) -> None:
        if self._suppress_heading_select_event:
            return
        selection = self.heading_tree.selection()
        if not selection:
            return
        item = selection[0]
        anchor = self._heading_item_to_anchor.get(item)
        if anchor and anchor in self.heading_indices:
            self._manual_heading_until = time.monotonic() + 0.65
            index = self.heading_indices[anchor]
            self.text.see(index)
            self.text.configure(state=tk.NORMAL)
            self.text.tag_remove("current_line", "1.0", tk.END)
            self.text.tag_add("current_line", index, f"{index} lineend+1c")
            self.text.configure(state=tk.DISABLED)

    def _enable_heading_select_events(self) -> None:
        self._suppress_heading_select_event = False

    def _on_search_result_open(self, event: tk.Event) -> None:
        selection = self.search_tree.selection()
        if not selection:
            return
        try:
            result_index = int(selection[0])
        except ValueError:
            return
        if result_index >= len(self.search_results):
            return
        rel_path, line_no, _snippet = self.search_results[result_index]
        self.open_document(rel_path, line_number=line_no)

    def _select_file_tree_item(self, rel_path: str) -> None:
        for item, item_path in self._file_item_to_path.items():
            if item_path == rel_path:
                self._suppress_file_select_event = True
                try:
                    self.file_tree.selection_set(item)
                    self.file_tree.see(item)
                finally:
                    self.after_idle(self._enable_file_select_events)
                break

    def _enable_file_select_events(self) -> None:
        self._suppress_file_select_event = False

    # ------------------------------------------------------------------ #
    # Cleanup                                                            #
    # ------------------------------------------------------------------ #

    def destroy(self) -> None:
        self._cancel_active_render()
        if self.graph_lab is not None and self.graph_lab.winfo_exists():
            try:
                self.graph_lab.destroy()
            except tk.TclError:
                pass
        if self.corpus is not None:
            self.corpus.source.close()
        super().destroy()


# ---------------------------------------------------------------------------
# Pure helper functions
# ---------------------------------------------------------------------------

def corpus_sort_key(rel_path: str) -> Tuple[int, Tuple[object, ...]]:
    first = rel_path.split("/", 1)[0] if "/" in rel_path else rel_path
    try:
        section_index = SECTION_ORDER.index(first)
    except ValueError:
        section_index = len(SECTION_ORDER)
    return section_index, natural_sort_key(rel_path)


def natural_sort_key(value: str) -> Tuple[Tuple[int, object], ...]:
    parts = re.split(r"(\d+)", value.lower())
    return tuple((0, int(part)) if part.isdigit() else (1, part) for part in parts)


def clean_yaml_scalar(value: str) -> str:
    value = value.strip()
    if value in {"null", "~"}:
        return ""
    if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
        value = value[1:-1]
    return value.strip()


def flatten_yaml_scalars(text: str) -> Dict[Tuple[str, ...], str]:
    """Best-effort scalar lens for the repository's controlled YAML files.

    It intentionally does not attempt to be a full YAML parser. The reader only
    needs a handful of declared identifiers and labels for navigation and graph
    views. Full validation remains owned by the repository schema tooling.
    """
    result: Dict[Tuple[str, ...], str] = {}
    stack: List[Tuple[int, str]] = []
    current_path: Optional[Tuple[str, ...]] = None
    current_indent = -1

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        match = YAML_KEY_RE.match(raw_line)
        if match:
            indent_text, key, value = match.groups()
            indent = len(indent_text.replace("\t", "    "))
            while stack and stack[-1][0] >= indent:
                stack.pop()
            path = tuple(item[1] for item in stack) + (key.strip(),)
            stack.append((indent, key.strip()))
            value = value or ""
            if value and value not in {"|", ">"} and not value.startswith("&"):
                result[path] = clean_yaml_scalar(value)
                current_path = path
                current_indent = indent
            else:
                current_path = None
                current_indent = indent
            continue

        if current_path is not None:
            indent = len(raw_line) - len(raw_line.lstrip(" "))
            stripped = raw_line.strip()
            if indent > current_indent and stripped and not stripped.startswith("- "):
                result[current_path] = (result[current_path] + " " + clean_yaml_scalar(stripped)).strip()

    return result


def scalar_from_flat(flat: Dict[Tuple[str, ...], str], paths: List[Tuple[str, ...]], default: str = "") -> str:
    for path in paths:
        value = flat.get(path)
        if value:
            return value
    return default


def scalar_by_leaf(flat: Dict[Tuple[str, ...], str], leaf: str) -> str:
    matches = [(path, value) for path, value in flat.items() if path and path[-1] == leaf and value]
    if not matches:
        return ""
    # Prefer the shortest path, which normally identifies result.routing.selected_class.
    matches.sort(key=lambda item: (len(item[0]), item[0]))
    return matches[0][1]


def parse_case_index(text: str) -> Dict[str, Dict[str, str]]:
    result: Dict[str, Dict[str, str]] = {}
    in_cases = False
    current: Optional[Dict[str, str]] = None
    for raw_line in text.splitlines():
        if raw_line.strip() == "cases:":
            in_cases = True
            continue
        if not in_cases:
            continue
        if raw_line and not raw_line.startswith(" ") and not raw_line.startswith("-"):
            break
        start_match = re.match(r"^-\s+case_id:\s*(.+?)\s*$", raw_line)
        if start_match:
            if current and current.get("case_id"):
                result[current["case_id"]] = current
            current = {"case_id": clean_yaml_scalar(start_match.group(1))}
            continue
        if current is None:
            continue
        field_match = re.match(r"^\s{2}([A-Za-z0-9_]+):\s*(.*?)\s*$", raw_line)
        if field_match:
            key, value = field_match.groups()
            if value and value not in {"|", ">"}:
                current[key] = clean_yaml_scalar(value)
    if current and current.get("case_id"):
        result[current["case_id"]] = current
    return result


def normalize_rel_path(path: str) -> str:
    return path.replace("\\", "/").lstrip("/")


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    raw = match.group(1)
    meta: Dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"\'')
        if key:
            meta[key] = value
    return meta, text[match.end():]


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def parse_yaml_outline(text: str) -> List[Heading]:
    """Return a shallow, indentation-based YAML outline.

    This is a navigation aid only. It is deliberately not a YAML parser and
    does not perform schema or semantic validation.
    """
    headings: List[Heading] = []
    stack: List[Tuple[int, str]] = []
    counter = 0
    identifier_keys = {"id", "rule_id", "stage_id", "class_id", "record_id", "name"}

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        match = YAML_OUTLINE_KEY_RE.match(raw_line)
        if not match:
            continue
        indent_text, list_marker, key, value = match.groups()
        indent = len(indent_text.replace("\t", "    ")) + (2 if list_marker else 0)
        while stack and stack[-1][0] >= indent:
            stack.pop()
        level = len(stack) + 1

        include = level <= 2 or (level == 3 and key in YAML_OUTLINE_LEVEL3_KEYS)
        if include:
            label = key
            scalar = clean_yaml_scalar(value)
            if key in identifier_keys and scalar and scalar not in {"|", ">"}:
                label = f"{key}: {scalar[:120]}"
            anchor = f"y-{counter}-{slugify(label)}"
            headings.append(Heading(level=min(level, 3), text=label, line_number=line_number, anchor=anchor))
            counter += 1
        stack.append((indent, key))

    return headings


def chunk_text_by_bytes(text: str, target_bytes: int) -> List[RenderChunk]:
    """Split text on line boundaries while preserving exact source content."""
    lines = text.splitlines(keepends=True)
    if not lines:
        return [RenderChunk("", 1)]
    chunks: List[RenderChunk] = []
    current: List[str] = []
    current_bytes = 0
    start_line = 1
    line_number = 1
    for line in lines:
        line_bytes = len(line.encode("utf-8", errors="replace"))
        if current and current_bytes + line_bytes > target_bytes:
            chunks.append(RenderChunk("".join(current), start_line))
            current = []
            current_bytes = 0
            start_line = line_number
        current.append(line)
        current_bytes += line_bytes
        line_number += 1
    if current:
        chunks.append(RenderChunk("".join(current), start_line))
    return chunks


def chunk_markdown_text(text: str, target_bytes: int) -> List[RenderChunk]:
    """Split Markdown at safe block boundaries, never inside fenced code."""
    lines = text.splitlines(keepends=True)
    if not lines:
        return [RenderChunk("", 1)]
    chunks: List[RenderChunk] = []
    current: List[str] = []
    current_bytes = 0
    start_line = 1
    in_fence = False
    line_number = 1

    for line in lines:
        current.append(line)
        current_bytes += len(line.encode("utf-8", errors="replace"))
        if FENCE_RE.match(line.rstrip("\r\n")):
            in_fence = not in_fence

        safe_boundary = not in_fence and not line.strip()
        forced_boundary = not in_fence and current_bytes >= target_bytes * 2
        if current_bytes >= target_bytes and (safe_boundary or forced_boundary):
            chunks.append(RenderChunk("".join(current), start_line))
            current = []
            current_bytes = 0
            start_line = line_number + 1
        line_number += 1

    if current:
        chunks.append(RenderChunk("".join(current), start_line))
    return chunks


def parse_headings(text: str) -> List[Heading]:
    headings: List[Heading] = []
    in_code = False
    heading_counter = 0

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        try:
            is_fence = bool(FENCE_RE.match(raw_line))
        except Exception:
            is_fence = False

        if is_fence:
            in_code = not in_code
            continue
        if in_code:
            continue

        try:
            match = HEADING_RE.match(raw_line)
        except Exception:
            continue

        if not match:
            continue

        text_value = clean_heading_text(match.group(2))
        anchor = f"h-{heading_counter}-{slugify(text_value)}"
        headings.append(
            Heading(
                level=len(match.group(1)),
                text=text_value,
                line_number=line_number,
                anchor=anchor,
            )
        )
        heading_counter += 1
    return headings


def first_heading_title(headings: List[Heading]) -> Optional[str]:
    return headings[0].text if headings else None


def clean_heading_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+#*$", "", text)
    text = text.replace("`", "")
    return text


def slugify(text: str) -> str:
    value = text.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "heading"


def looks_like_table_line(line: str) -> bool:
    stripped = line.strip()
    return (
        stripped.startswith("|")
        and stripped.endswith("|")
        and stripped.count("|") >= 2
    )


def split_markdown_table_row(line: str) -> List[str]:
    """Split a pipe table row while preserving escaped pipes."""
    stripped = line.strip().strip("|")
    cells: List[str] = []
    current: List[str] = []
    escaped = False
    for char in stripped:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return cells


def markdown_link_cell(value: str) -> Tuple[str, Optional[str]]:
    """Return display text and target for a cell containing one Markdown link."""
    match = MARKDOWN_LINK_RE.fullmatch(value.strip())
    if not match:
        return value, None
    label, target = match.groups()
    label = re.sub(r"[`*_]", "", label).strip()
    return label, target.strip()


def table_sort_value(value: str) -> Tuple[int, object]:
    cleaned = value.strip().replace(",", "")
    try:
        return 0, float(cleaned)
    except ValueError:
        return 1, value.casefold()


def prettify_file_name(rel_path: str) -> str:
    name = Path(rel_path).name
    if name.lower().endswith(".md"):
        name = name[:-3]
    name = name.replace("_", " ").replace("-", " - ")
    name = re.sub(r"\s+", " ", name).strip()
    return name


def walk_widgets(widget: tk.Widget) -> Iterable[tk.Widget]:
    yield widget
    for child in widget.winfo_children():
        yield from walk_widgets(child)


def discover_default_source() -> Optional[Path]:
    """Return the first valid PMS-STRATA source path found, or None."""
    candidates: List[Path] = []

    positional = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if positional:
        candidates.append(Path(positional[0]))

    cwd = Path.cwd()
    script_dir = Path(__file__).resolve().parent
    repo_root_from_tool_dir = script_dir.parent

    candidates.extend([
        cwd,
        cwd / "16. PMS-STRATA",
        cwd / "PMS-STRATA",
        cwd / "PMS-STRATA.zip",
        script_dir,
        script_dir / "16. PMS-STRATA",
        script_dir / "PMS-STRATA.zip",
        repo_root_from_tool_dir,
        repo_root_from_tool_dir / "16. PMS-STRATA",
    ])

    for candidate in candidates:
        dbg(f"discover: checking {candidate}")
        try:
            if candidate.is_dir():
                CorpusSource._detect_folder_root(candidate)
                return candidate
            if candidate.is_file() and candidate.suffix.lower() == ".zip":
                with zipfile.ZipFile(candidate) as zf:
                    CorpusSource._detect_zip_prefix(zf)
                return candidate
        except Exception as exc:
            dbg(f"discover: {candidate} rejected ({exc})")
    return None


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def run_self_test(source_path: Optional[Path]) -> int:
    source_path = source_path or discover_default_source()
    if source_path is None:
        print("No PMS-STRATA corpus found.", file=sys.stderr)
        return 2
    source = CorpusSource(source_path)
    try:
        corpus = Corpus(source)
        operations: Dict[str, int] = {}
        classes: Dict[str, int] = {}
        for record in corpus.records:
            operations[record.operation] = operations.get(record.operation, 0) + 1
            classes[record.output_class] = classes.get(record.output_class, 0) + 1
        summary = {
            "source": corpus.source.describe(),
            "active_artifacts": corpus.document_count,
            "records": len(corpus.records),
            "operations": operations,
            "output_classes": classes,
            "workfiles_ingested": any(path.startswith("_workfiles/") for path in corpus.ordered_paths),
            "record_yaml_markdown_pairs": sum(1 for record in corpus.records if record.markdown_path),
            "package_linked_records": sum(1 for record in corpus.records if record.package_path),
        }
        print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))
        return 0 if len(corpus.records) == 59 and not summary["workfiles_ingested"] else 1
    finally:
        source.close()


def main() -> None:
    if "--self-test" in sys.argv:
        globals()["DEBUG"] = False
    dbg(f"main: argv={sys.argv}")
    positional = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    initial_source = Path(positional[0]) if positional else None
    if "--self-test" in sys.argv:
        raise SystemExit(run_self_test(initial_source))
    app = PmsStrataReaderApp(initial_source=initial_source)
    app.mainloop()
    dbg("main: mainloop exited")


if __name__ == "__main__":
    main()
