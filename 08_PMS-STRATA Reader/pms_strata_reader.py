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

import csv
import json
import math
import queue
import re
import sys
import threading
import time
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

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
APP_VERSION = "0.3.0-prototype"

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
    "02_appendices": "Appendices A–N",
    "03_cases": "Cases and Records",
    "04_reference": "Reference Kernel",
    "05_minified": "Minified Controls",
    "06_derivative_publications": "Derivative Publications",
    "07_model": "Formal Model",
    "08_PMS-STRATA Reader": "Reader",
}

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

# Above this threshold the renderer avoids per-line source marks.
LARGE_DOC_LINE_THRESHOLD = 8000

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

    @property
    def line_count(self) -> int:
        return len(self.text.splitlines())

    @property
    def word_count(self) -> int:
        return len(WORD_RE.findall(self.text))


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
        self.status_var = tk.StringVar(value="Drag to rotate • wheel to zoom • double-click a record to open it")

        self.nodes: List[GraphNode] = []
        self.edges: List[Tuple[str, str]] = []
        self.node_by_id: Dict[str, GraphNode] = {}
        self.projected: Dict[str, Tuple[float, float, float, float]] = {}
        self.selected_node_id = ""
        self.angle_x = -0.22
        self.angle_y = 0.52
        self.zoom = 1.0
        self._drag_start: Optional[Tuple[int, int]] = None
        self._drag_moved = False

        self._build_ui()
        self.refresh()

    def _build_ui(self) -> None:
        toolbar = ttk.Frame(self, padding=(8, 8, 8, 5))
        toolbar.pack(fill=tk.X)

        ttk.Label(toolbar, text="View").pack(side=tk.LEFT)
        view_box = ttk.Combobox(
            toolbar,
            textvariable=self.view_var,
            state="readonly",
            width=25,
            values=[
                self.VIEW_CASE_TREE,
                self.VIEW_AUTHORITY,
                self.VIEW_DEPENDENCY,
                self.VIEW_FLOW,
                self.VIEW_RECORD,
                self.VIEW_CHAIN,
            ],
        )
        view_box.pack(side=tk.LEFT, padx=(5, 12))
        view_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())

        ttk.Label(toolbar, text="Operation").pack(side=tk.LEFT)
        op_box = ttk.Combobox(
            toolbar,
            textvariable=self.operation_var,
            state="readonly",
            width=13,
            values=["ALL", "COMPOSE", "DECOMPOSE", "PROJECT_AS"],
        )
        op_box.pack(side=tk.LEFT, padx=(5, 12))
        op_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())

        ttk.Label(toolbar, text="Output Class").pack(side=tk.LEFT)
        self.class_box = ttk.Combobox(toolbar, textvariable=self.class_var, state="readonly", width=30)
        self.class_box.pack(side=tk.LEFT, padx=(5, 12))
        self.class_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())

        ttk.Checkbutton(toolbar, text="Labels", variable=self.labels_var, command=self.redraw).pack(side=tk.LEFT)
        ttk.Button(toolbar, text="Reset View", command=self.reset_view).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(toolbar, text="Open Selected", command=self.open_selected).pack(side=tk.RIGHT)

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
        self.canvas.bind("<Double-1>", self._on_double_click)
        self.canvas.bind("<MouseWheel>", self._on_wheel)
        self.canvas.bind("<Button-4>", lambda event: self._zoom_by(1.12))
        self.canvas.bind("<Button-5>", lambda event: self._zoom_by(0.89))

        detail_frame = ttk.Frame(main, padding=(8, 4, 4, 4))
        main.add(detail_frame, weight=1)
        ttk.Label(detail_frame, text="Trace / Node Details", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W)
        self.details = tk.Text(detail_frame, wrap=tk.WORD, width=38, padx=10, pady=10, state=tk.DISABLED)
        self.details.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

        ttk.Label(self, textvariable=self.status_var, anchor=tk.W, padding=(8, 4)).pack(fill=tk.X)

    def _hide(self) -> None:
        self.withdraw()

    def set_current_path(self, rel_path: Optional[str]) -> None:
        if self.view_var.get() in {self.VIEW_RECORD, self.VIEW_CHAIN}:
            self.refresh()

    def reset_view(self) -> None:
        self.angle_x = -0.22
        self.angle_y = 0.52
        self.zoom = 1.0
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
        self._set_details(self._view_description(view))
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
                    details = self._record_details(record)
                    node_id = f"record:{record.record_id}"
                    nodes.append(GraphNode(node_id, record.case_id, "record", rx, ry, rz, record.yaml_path, details))
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
        nodes = [
            GraphNode("source", record.source_id or "Source", "source", -280, -90, -80, details=record.source_description),
            GraphNode("claim", "Claim", "claim", -120, -230, 0, details=record.claim),
            GraphNode("operation", record.operation, "operation", 0, 0, 0, details=record.operation),
            GraphNode("audit", "12-stage audit", "audit", 100, -220, 75, details="Audit findings remain qualitative and non-compensatory."),
            GraphNode("loss", "5-part Loss", "loss", 220, 180, 90, details="preserved / compressed / excluded / uncertain / irrecoverable"),
            GraphNode("target", record.target_id or "Target", "target", 280, -70, 110, details=record.target_description),
            GraphNode("class", record.output_class, "class", 100, 250, 190, details=record.output_class),
            GraphNode("record", record.case_id, "record", -120, 230, 240, record.yaml_path, self._record_details(record)),
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
            nodes.append(GraphNode(node_id, f"{member.case_id}\n{member.operation}", "record", x, y, z, member.yaml_path, self._record_details(member)))
            class_id = f"chainclass:{member.record_id}"
            nodes.append(GraphNode(class_id, member.output_class, "class", x + 150, y + 35, z + 35, details=member.output_class))
            edges.append((node_id, class_id))
            if index:
                edges.append((f"chain:{members[index - 1].record_id}", node_id))
        return nodes, edges

    @staticmethod
    def _view_description(view: str) -> str:
        descriptions = {
            GraphLab.VIEW_CASE_TREE: "Corpus tree: operation → output class → record. Rotate and zoom freely. Visual depth is not ontological depth.",
            GraphLab.VIEW_AUTHORITY: "Authority order from PMS Base to Reader. The graph visualizes declared precedence; it creates none.",
            GraphLab.VIEW_DEPENDENCY: "Formal-model dependency view. Schema and graph consistency do not establish substantive truth.",
            GraphLab.VIEW_FLOW: "Transformation flow from source and claim through audit, routing, and record preservation.",
            GraphLab.VIEW_RECORD: "Selected record trace. Open a YAML record or Markdown companion in the main reader first.",
            GraphLab.VIEW_CHAIN: "Selected chain view. Local results and Loss profiles remain separate at every handoff.",
        }
        return descriptions.get(view, "")

    @staticmethod
    def _record_details(record: RecordSummary) -> str:
        return (
            f"{record.case_id} — {record.title}\n\n"
            f"Operation: {record.operation}\n"
            f"Output class: {record.output_class}\n"
            f"Case class: {record.case_class or '—'}\n"
            f"Owner: {record.chapter_owner or '—'}\n"
            f"Record ID: {record.record_id}\n"
            f"Chain ID: {record.chain_id or '—'}\n\n"
            f"Claim\n{record.claim or '—'}\n\n"
            f"Source\n{record.source_id or '—'}\n{record.source_description or ''}\n\n"
            f"Target\n{record.target_id or '—'}\n{record.target_description or ''}\n\n"
            f"YAML: {record.yaml_path}\n"
            f"Markdown: {record.markdown_path or '—'}\n"
            f"Package: {record.package_path or '—'}"
        )

    def _set_details(self, text: str) -> None:
        self.details.configure(state=tk.NORMAL)
        self.details.delete("1.0", tk.END)
        self.details.insert("1.0", text)
        self.details.configure(state=tk.DISABLED)

    def redraw(self) -> None:
        if not hasattr(self, "canvas"):
            return
        self.canvas.delete("all")
        width = max(1, self.canvas.winfo_width())
        height = max(1, self.canvas.winfo_height())
        self.projected.clear()
        for node in self.nodes:
            self.projected[node.node_id] = self._project(node, width, height)

        edge_color = "#526173"
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
            width_line = 3 if node.node_id == self.selected_node_id else 1
            self.canvas.create_oval(sx - radius, sy - radius, sx + radius, sy + radius, fill=fill, outline=outline, width=width_line)
            if self.labels_var.get() and (node.kind != "record" or len(self.nodes) < 35 or node.node_id == self.selected_node_id):
                self.canvas.create_text(sx, sy + radius + 10, text=node.label, fill="#e8edf3", font=("Segoe UI", 8 if node.kind == "record" else 9, "bold"), justify=tk.CENTER, width=150)

        self.canvas.create_text(12, 12, anchor=tk.NW, text=self.view_var.get(), fill="#d7e0ea", font=("Segoe UI", 12, "bold"))
        self.canvas.create_text(12, 34, anchor=tk.NW, text=f"{len(self.nodes)} nodes • {len(self.edges)} edges", fill="#8fa3b8", font=("Segoe UI", 9))

    def _project(self, node: GraphNode, width: int, height: int) -> Tuple[float, float, float, float]:
        cosy, siny = math.cos(self.angle_y), math.sin(self.angle_y)
        cosx, sinx = math.cos(self.angle_x), math.sin(self.angle_x)
        x1 = cosy * node.x + siny * node.z
        z1 = -siny * node.x + cosy * node.z
        y1 = cosx * node.y - sinx * z1
        z2 = sinx * node.y + cosx * z1
        perspective = 760 / max(240, 760 + z2)
        scale = self.zoom * perspective
        return width / 2 + x1 * scale, height / 2 + y1 * scale, z2, scale

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
                self._set_details(node.details or node.label)
                self.redraw()
        self._drag_start = None

    def _on_double_click(self, event: tk.Event) -> None:
        node = self._nearest_node(event.x, event.y, threshold=30)
        if node and node.rel_path:
            self.app.open_document(node.rel_path)
            self.app.lift()

    def _on_wheel(self, event: tk.Event) -> str:
        self._zoom_by(1.12 if event.delta > 0 else 0.89)
        return "break"

    def _zoom_by(self, factor: float) -> None:
        self.zoom = max(0.35, min(3.0, self.zoom * factor))
        self.redraw()

    def open_selected(self) -> None:
        node = self.node_by_id.get(self.selected_node_id)
        if node and node.rel_path:
            self.app.open_document(node.rel_path)
            self.app.lift()


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
        self._search_entry: Optional[ttk.Entry] = None
        self.dark_mode = False
        self.graph_lab: Optional[GraphLab] = None

        self.reader_font_size = 10
        self.reader_fullscreen = False
        self._normal_geometry = ""

        # Guard against recursive Treeview callbacks:
        # programmatic selection_set() also emits <<TreeviewSelect>>.
        self._suppress_file_select_event = False

        # Queue for results coming back from the background loader thread.
        self._load_queue: queue.Queue = queue.Queue()

        self._configure_style()
        self._build_ui()
        self._bind_shortcuts()
        self.apply_theme()
        self._center_window()

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

        self.main_pane = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.main_pane.pack(fill=tk.BOTH, expand=True)

        self.left_pane = ttk.PanedWindow(self.main_pane, orient=tk.VERTICAL)
        self.main_pane.add(self.left_pane, weight=1)

        # File tree
        file_frame = ttk.Frame(self.left_pane, padding=(6, 6, 6, 3))
        self.left_pane.add(file_frame, weight=3)
        ttk.Label(file_frame, text="Corpus", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W)

        file_tree_wrap = ttk.Frame(file_frame)
        file_tree_wrap.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        self.file_tree = ttk.Treeview(file_tree_wrap, show="tree")
        self.file_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        file_scrollbar = ttk.Scrollbar(file_tree_wrap, orient=tk.VERTICAL, command=self.file_tree.yview)
        file_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_tree.configure(yscrollcommand=file_scrollbar.set)

        self.file_tree.bind("<<TreeviewSelect>>", self._on_file_selected)
        self._bind_mousewheel_scroll(self.file_tree)

        # Search results
        search_frame = ttk.Frame(self.left_pane, padding=(6, 3, 6, 6))
        self.left_pane.add(search_frame, weight=2)
        ttk.Label(search_frame, text="Search Results", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W)

        search_tree_wrap = ttk.Frame(search_frame)
        search_tree_wrap.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        self.search_tree = ttk.Treeview(
            search_tree_wrap,
            show="headings",
            columns=("file", "line", "text"),
            height=9,
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
        self.heading_frame = ttk.Frame(self.main_pane, padding=(6, 6, 6, 6))
        self.main_pane.add(self.heading_frame, weight=1)
        ttk.Label(self.heading_frame, text="Headings", font=("Segoe UI", 10, "bold")).pack(anchor=tk.W)

        heading_tree_wrap = ttk.Frame(self.heading_frame)
        heading_tree_wrap.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

        self.heading_tree = ttk.Treeview(heading_tree_wrap, show="tree")
        self.heading_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        heading_scrollbar = ttk.Scrollbar(heading_tree_wrap, orient=tk.VERTICAL, command=self.heading_tree.yview)
        heading_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.heading_tree.configure(yscrollcommand=heading_scrollbar.set)

        self.heading_tree.bind("<<TreeviewSelect>>", self._on_heading_selected)
        self._bind_mousewheel_scroll(self.heading_tree)

        # Document content
        self.content_frame = ttk.Frame(self.main_pane, padding=(6, 6, 6, 6))
        self.main_pane.add(self.content_frame, weight=4)

        self.document_label_var = tk.StringVar(value="No document loaded")
        self.document_label = ttk.Label(
            self.content_frame,
            textvariable=self.document_label_var,
            font=("Segoe UI", 11, "bold"),
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

        text_wrap = ttk.Frame(self.reader_border)
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

        yscroll = ttk.Scrollbar(text_wrap, orient=tk.VERTICAL, command=self.text.yview)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.configure(yscrollcommand=yscroll.set)

        self._configure_text_tags()

        self.status_var = tk.StringVar(value="Starting ...")
        self.status_label = ttk.Label(self, textvariable=self.status_var, anchor=tk.W, padding=(6, 3))
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
        ttk.Button(self.toolbar, text="Run", command=self.run_search).pack(side=tk.LEFT)
        ttk.Button(self.toolbar, text="Clear", command=self.clear_search).pack(side=tk.LEFT, padx=(4, 12))

        ttk.Button(self.toolbar, text="Reload", command=self.reload_source).pack(side=tk.LEFT)
        ttk.Button(self.toolbar, text="Home", command=self.open_home).pack(side=tk.LEFT, padx=(6, 6))
        ttk.Button(self.toolbar, text="Graph Lab", command=self.open_graph_lab).pack(side=tk.LEFT, padx=(0, 12))

        ttk.Button(self.toolbar, text="A−", command=self.decrease_reader_font).pack(side=tk.LEFT)
        ttk.Button(self.toolbar, text="A+", command=self.increase_reader_font).pack(side=tk.LEFT, padx=(4, 12))

        self.fullscreen_button = ttk.Button(
            self.toolbar,
            text="Reader Fullscreen",
            command=self.toggle_reader_fullscreen,
        )
        self.fullscreen_button.pack(side=tk.LEFT, padx=(0, 12))

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

    def toggle_dark_mode(self) -> None:
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self) -> None:
        if self.dark_mode:
            bg = "#1e1e1e"
            panel_bg = "#252526"
            fg = "#d4d4d4"
            muted_fg = "#a0a0a0"
            text_bg = "#1e1e1e"
            text_fg = "#d4d4d4"
            code_bg = "#2d2d2d"
            button_bg = "#333333"
            button_hover_bg = "#404040"
            selection_bg = "#3a3d41"
            current_line_bg = "#2a2d2e"
            search_bg = "#665c00"
            rule_fg = "#777777"
            yaml_key_fg = "#ce9178"
            yaml_value_fg = "#b5cea8"
            reader_border_fg = "#3a3d41"
            self.theme_button.configure(text="Light Mode")
        else:
            bg = "#f0f0f0"
            panel_bg = "#ffffff"
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
            self.theme_button.configure(text="Dark Mode")

        self.configure(background=bg)

        style = ttk.Style(self)
        style.configure(".", background=bg, foreground=fg)
        style.configure("TFrame", background=bg)
        style.configure("TLabel", background=bg, foreground=fg)
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
            "  Enter                   Run search from search field\n"
            "  Double-click result     Open search result\n\n"
            "Reader:\n"
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

        self.main_pane.add(self.left_pane, weight=1)
        self.main_pane.add(self.heading_frame, weight=1)
        self.main_pane.add(self.content_frame, weight=4)

        self.toolbar.pack(fill=tk.X, before=self.main_pane)
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)

        if self._normal_geometry:
            self.geometry(self._normal_geometry)

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
            self.graph_lab.refresh()

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
            item = self.file_tree.insert(parent, tk.END, text=doc.title, open=False)
            self._file_item_to_path[item] = rel_path

        dbg(f"populate_file_tree: inserted {len(self._file_item_to_path)} file items")

    def populate_heading_tree(self, doc: Document) -> None:
        self.heading_tree.delete(*self.heading_tree.get_children())
        self._heading_item_to_anchor.clear()

        parent_by_level: Dict[int, str] = {0: ""}
        for heading in doc.headings:
            parent_level = heading.level - 1
            while parent_level > 0 and parent_level not in parent_by_level:
                parent_level -= 1
            parent = parent_by_level.get(parent_level, "")
            label = f"{'  ' * max(0, heading.level - 1)}{heading.text}"
            item = self.heading_tree.insert(parent, tk.END, text=label, open=True)
            self._heading_item_to_anchor[item] = heading.anchor
            parent_by_level[heading.level] = item
            for deeper in list(parent_by_level):
                if deeper > heading.level:
                    del parent_by_level[deeper]

    # ------------------------------------------------------------------ #
    # Document rendering                                                 #
    # ------------------------------------------------------------------ #

    def open_document(self, rel_path: str, line_number: Optional[int] = None) -> None:
        if self.corpus is None or rel_path not in self.corpus.documents:
            return
        if self.current_path == rel_path and line_number is None:
            return

        dbg(f"open_document: {rel_path}")
        doc = self.corpus.documents[rel_path]
        self.current_path = rel_path
        self.document_label_var.set(f"{doc.title} — {rel_path}")
        self.populate_heading_tree(doc)
        self.render_document(doc)
        self.highlight_query()
        self._select_file_tree_item(rel_path)
        if line_number is not None:
            self.scroll_to_source_line(line_number)
        else:
            self.text.yview_moveto(0)

        record = self.corpus.record_for_path(rel_path)
        record_suffix = f" • {record.operation} → {record.output_class}" if record else ""
        self.status_var.set(
            f"{rel_path} — {doc.line_count:,} lines, {doc.word_count:,} words, "
            f"{len(doc.headings):,} headings{record_suffix}"
        )
        if self.graph_lab is not None and self.graph_lab.winfo_exists():
            self.graph_lab.set_current_path(rel_path)

    def render_document(self, doc: Document) -> None:
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

    def render_yaml(self, doc: Document) -> None:
        self.heading_indices.clear()
        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        for line_number, line in enumerate(doc.text.splitlines(), start=1):
            if doc.line_count <= LARGE_DOC_LINE_THRESHOLD:
                self.text.mark_set(f"source_line_{line_number}", self.text.index(tk.INSERT))
            self._insert_yaml_line(line)
        self.text.configure(state=tk.DISABLED)

    def render_json(self, doc: Document) -> None:
        try:
            rendered = json.dumps(json.loads(doc.text), indent=2, ensure_ascii=False)
        except Exception:
            rendered = doc.text
        self._render_plain_text(rendered, "code")

    def render_csv(self, doc: Document) -> None:
        try:
            rows = list(csv.reader(doc.text.splitlines()))
            if not rows:
                rendered = ""
            else:
                width_count = max(len(row) for row in rows)
                padded = [row + [""] * (width_count - len(row)) for row in rows]
                widths = [min(48, max(len(row[i]) for row in padded)) for i in range(width_count)]
                rendered_lines = []
                for row_index, row in enumerate(padded):
                    rendered_lines.append("  │  ".join(row[i][:widths[i]].ljust(widths[i]) for i in range(width_count)))
                    if row_index == 0:
                        rendered_lines.append("──┼──".join("─" * width for width in widths))
                rendered = "\n".join(rendered_lines)
        except Exception:
            rendered = doc.text
        self._render_plain_text(rendered, "table")

    def render_plain(self, doc: Document) -> None:
        self._render_plain_text(doc.text, "code" if doc.file_type == "py" else "body")

    def _render_plain_text(self, text: str, tag: str) -> None:
        self.heading_indices.clear()
        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", text, (tag,))
        self.text.configure(state=tk.DISABLED)

    def render_markdown(self, doc: Document) -> None:
        """Render *doc* into the text widget.

        This renderer keeps large files fast by avoiding per-line source marks
        in large documents, but still performs Markdown-light normalization:
        headings, fenced code blocks, YAML blocks, lists, and tables.
        """
        dbg(f"render_markdown: {doc.rel_path} ({doc.line_count} lines)")
        body = strip_frontmatter(doc.text)
        self.heading_indices.clear()

        self.text.configure(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)

        try:
            use_source_marks = doc.line_count <= LARGE_DOC_LINE_THRESHOLD
            self._render_markdown_blocks(doc, body, use_source_marks=use_source_marks)
        except Exception as exc:
            dbg(f"render_markdown: exception: {exc}")
            self.status_var.set(f"Render error: {exc}")
        finally:
            self.text.configure(state=tk.DISABLED)

    def _render_markdown_blocks(self, doc: Document, body: str, use_source_marks: bool) -> None:
        """Markdown-light block renderer.

        It is intentionally not a full Markdown engine. It renders the PMS-STRATA
        corpus well enough without external dependencies and without destroying
        performance on the large monolith.
        """
        lines = body.splitlines()
        i = 0
        heading_counter = 0

        while i < len(lines):
            raw_line = lines[i]
            source_line = i + 1
            line_start = self.text.index(tk.INSERT)

            if use_source_marks:
                self.text.mark_set(f"source_line_{source_line}", line_start)

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

                # Skip closing fence when present.
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
                prefix = "  " * level + "• "
                self.text.insert(tk.END, prefix, ("list",))
                self._insert_inline_markdown(content, ("list",))
                self.text.insert(tk.END, "\n", ("list",))
                i += 1
                continue

            ordered_match = ORDERED_LIST_RE.match(raw_line)
            if ordered_match:
                indent, number, content = ordered_match.groups()
                level = max(0, len(indent.replace("\t", "    ")) // 2)
                prefix = "  " * level + f"{number}. "
                self.text.insert(tk.END, prefix, ("list",))
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
                self.text.insert(tk.END, "\u2500" * 80 + "\n", ("rule",))
                i += 1
                continue

            self._insert_inline_markdown(raw_line, ("body",))
            self.text.insert(tk.END, "\n", ("body",))
            i += 1

        dbg(f"_render_markdown_blocks: done ({heading_counter} headings rendered)")

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
        """Insert one text fragment with lightweight inline Markdown styling.

        Supported:
        - `inline code`
        - ***bold italic***
        - **bold**
        - *italic*

        This intentionally avoids full Markdown parsing but handles the corpus'
        most common inline patterns.
        """
        token_re = re.compile(
            r"(`[^`]+`|\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*\n]+\*)"
        )

        pos = 0

        for match in token_re.finditer(text):
            if match.start() > pos:
                self.text.insert(tk.END, text[pos:match.start()], base_tags)

            token = match.group(0)

            if token.startswith("`") and token.endswith("`"):
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

    def _insert_table_block(self, table_lines: List[str]) -> None:
        """Render a Markdown table as an aligned monospace text table."""
        rows: List[List[str]] = []

        for line in table_lines:
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]

            # Skip Markdown separator rows like | --- | :---: |
            if cells and all(re.fullmatch(r":?-{3,}:?", cell or "---") for cell in cells):
                continue

            rows.append(cells)

        if not rows:
            return

        column_count = max(len(row) for row in rows)
        normalized_rows: List[List[str]] = [
            row + [""] * (column_count - len(row))
            for row in rows
        ]

        widths = [
            max(len(row[column]) for row in normalized_rows)
            for column in range(column_count)
        ]

        rendered_lines: List[str] = []
        for row_index, row in enumerate(normalized_rows):
            rendered = "  │  ".join(
                row[column].ljust(widths[column])
                for column in range(column_count)
            )
            rendered_lines.append(rendered)

            if row_index == 0 and len(normalized_rows) > 1:
                rendered_lines.append("──┼──".join("─" * width for width in widths))

        self.text.insert(tk.END, "\n", ("body",))
        self.text.insert(tk.END, "\n".join(rendered_lines) + "\n", ("table",))
        self.text.insert(tk.END, "\n", ("body",))

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
        query = self.search_var.get().strip()
        self.text.configure(state=tk.NORMAL)
        self.text.tag_remove("search", "1.0", tk.END)
        if query:
            start = "1.0"
            while True:
                pos = self.text.search(query, start, stopindex=tk.END, nocase=True)
                if not pos:
                    break
                end = f"{pos}+{len(query)}c"
                self.text.tag_add("search", pos, end)
                start = end
        self.text.configure(state=tk.DISABLED)

    def scroll_to_source_line(self, line_number: int) -> None:
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
        selection = self.heading_tree.selection()
        if not selection:
            return
        item = selection[0]
        anchor = self._heading_item_to_anchor.get(item)
        if anchor and anchor in self.heading_indices:
            index = self.heading_indices[anchor]
            self.text.see(index)
            self.text.configure(state=tk.NORMAL)
            self.text.tag_remove("current_line", "1.0", tk.END)
            self.text.tag_add("current_line", index, f"{index} lineend+1c")
            self.text.configure(state=tk.DISABLED)

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
