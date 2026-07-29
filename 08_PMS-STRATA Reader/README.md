# PMS-STRATA Reader

**Status:** experimental executable prototype; downstream presentation and navigation layer only  
**Version:** `0.5.5-derivative-routing`  
**Implementation:** single-file Python/Tkinter desktop application  
**Authority:** none beyond the artifacts it reads

The current prototype adapts the first executable PMS-EM Reader layer to the active PMS-STRATA repository. It can open either the repository folder or a Source-of-Truth ZIP and provides ordinary corpus reading together with an interactive graph layer.

Version `0.4.0-audit-support` supplied the bounded Reader Audit Support Patch required for reliable Corpus Audit work. Version `0.5.0-graph-lab` added the separately scoped **Graph Lab Package**. Version `0.5.1-reader-fixes` corrected file-browser scope, resize handles, startup pane minima, conditional horizontal table scrollbars, and the Search label. Version `0.5.2-graph-navigation` added explicit README naming under Start, middle/right-button graph panning, selected-node rotation pivots, blank-space deselection, and selected-node artifact rendering in the Graph Lab detail tabs. Version `0.5.3-rendered-details` completed rendered detail views and selected-node centering. Version `0.5.4-toolbar-cleanup` removes the redundant Browse Files, Open Folder, and Open ZIP controls; corpus selection occurs at launch, while Graph Lab navigation is node-selection based. Version `0.5.5-derivative-routing` labels and routes the three derivative publications explicitly and excludes internal derivative production controls from active Reader ingestion. These versions change only the Reader presentation layer and do not modify canonical theory or authority.

```text
Reader
≠ canonical corpus
≠ Formal Model
≠ evidence
≠ automatic classification
≠ application authority
```

The implementation deliberately displays declared repository relations. It does not generate new STRATA operations, claims, dependencies, Output Classes, historical alternatives, or authority relations.

## 1. Run

```bash
python pms_strata_reader.py
python pms_strata_reader.py "/path/to/16. PMS-STRATA"
python pms_strata_reader.py "/path/to/PMS-STRATA_Source_of_Truth.zip"
```

Linux distributions may package Tkinter separately:

```bash
sudo apt install python3-tk
```

A headless structural check remains available:

```bash
python pms_strata_reader.py --self-test "/path/to/PMS-STRATA_Source_of_Truth.zip"
```

The self-test belongs to the Reader’s existing corpus-ingestion layer. It is not required for the Graph Lab presentation package and does not establish substantive validity.

## 2. Active corpus ingestion

The Reader discovers active text artifacts dynamically rather than relying on a manually maintained fixed file list. It currently reads:

```text
README.md
00_source/*
01_blocks/*
02_appendices/*
03_cases/*
04_reference/*
05_minified/*
06_derivative_publications/*
07_model/*
08_PMS-STRATA Reader/*
```

Supported text formats:

```text
Markdown
YAML
JSON
CSV
plain text
Python source
```

The following internal layers are excluded by default and are not searchable, rendered, indexed, or graphed:

```text
_workfiles/**
06_derivative_publications/_production_controls/**
```

This is intentional. Workfiles and derivative production controls are production provenance, not active Reader input. The Derivative Publications section therefore routes only to the compact overview, publishable paper, and technical whitepaper.

## 3. Corpus Reader

The main window provides:

- a nested active-artifact navigator with **Start → README** as the root entry;
- a Derivative Publications branch with explicit labels for the compact overview, publishable paper, and technical whitepaper;
- canonical block labels in actual corpus order: Front Matter, Foundations, PATH, SUB, RETYPE, LIMITS, Conclusion;
- a heading navigator for Markdown and shallow YAML structure;
- automatic active-heading synchronization during document scrolling;
- Markdown-light rendering;
- functional Markdown links and document anchors;
- controlled external-browser handoff and visible unavailable-target reports;
- YAML syntax coloring for ordinary files;
- seamless progressive text rendering for very large Markdown, YAML, JSON, text, and source artifacts;
- loading state and block progress without direct worker-thread widget access;
- generation-safe cancellation of stale document loads;
- JSON pretty rendering;
- cell-based Markdown and CSV tables with fixed headers and horizontal scrolling only when content exceeds the visible width;
- sortable CSV columns;
- corpus-wide full-text search;
- jump-to-result behavior;
- search highlighting;
- reader fullscreen;
- font scaling;
- light and dark mode;
- visible resize handles in both modes, with startup minimum sizes that keep Corpus, Search Results, Headings, and the document area accessible;
- a toolbar **Search** button matching the search action.

The Graph Lab button is placed between **Reader Fullscreen** and the Light/Dark Mode control.

The Reader derives lightweight record summaries for navigation and graph display. This presentation layer does not replace schema validation or corpus audit.

```text
Reader presentation success
≠ schema validation
≠ substantive validation
```

Formal schema validation remains owned by `07_model/Transformation_Record.schema.json` and the repository audit workflow.

### 3.1 Large-file rendering boundary

Large files are not split or rewritten. Above the configured line or byte threshold, the Reader prepares blocks in a worker thread and inserts them into one continuous document surface in the Tk main thread.

```text
source artifact remains unchanged
→ worker prepares bounded blocks and shallow outline
→ one Reader surface displays the complete text seamlessly
```

Every document request receives an internal generation number. If another file is opened before loading completes, delayed blocks from the older generation are ignored.

For very large YAML files, the first audit view is intentionally plain monospace text rather than a fully recursive widget tree or full-document syntax pass. Navigation uses a shallow indentation-based outline. This is a presentation optimization only:

```text
shallow YAML outline
≠ schema validation
≠ semantic validation
```

### 3.2 Link and table boundary

Internal Markdown links open active text artifacts in the Reader. Document anchors jump within the current or linked document. External links require confirmation before opening in the default browser. Missing or inactive targets are reported visibly.

Markdown and CSV tables are rendered as downstream cell grids. Source files remain unchanged.

```text
table rendering
≠ source conversion
```

## 4. Graph Lab Package

Open **Graph Lab** from the main toolbar or press `Ctrl+G`.

The Graph Lab opens maximized rather than in OS-exclusive fullscreen mode. Window controls remain available, and a dedicated **Close** button is placed at the upper right.

Controls:

```text
left mouse-button drag
→ rotate the pseudo-3D graph around the selected node, or around the graph origin when nothing is selected

middle or right mouse-button drag
→ pan the graph without changing rotation

mouse wheel
→ zoom

hover
→ highlight a node and show brief status information

single click on a node
→ select it, make it the rotation pivot, and populate the detail tabs

single click on empty canvas
→ clear the selection and return rotation to the graph origin

double click
→ open the linked repository artifact in the main Reader
```

Selected nodes remain visibly marked and are named as the active rotation pivot on the canvas and in Summary. Clickable nodes and controls use a hand cursor and visible hover feedback.

### 4.1 Node-based navigation

Graph Lab navigation is intentionally node-selection based. Selecting a node centers it, makes it the rotation pivot, and renders its linked artifacts in the detail tabs. No separate file-browser control is shown in Graph Lab.

The main Reader loads its corpus at application launch, either from the default repository context or from a folder/ZIP path supplied on the command line. The toolbar therefore omits separate **Open Folder** and **Open ZIP** controls.

### 4.2 Detail tabs

The Graph Lab detail panel now provides five direct views:

```text
Summary
YAML
Markdown
Relations
Trace
```

For a selected Record, **Summary** displays:

- Record ID;
- operation;
- Output Class;
- case class and chapter owner;
- claim;
- Source and Target;
- Stop, Failure, and Non-Capture status as indicated by the selected Output Class;
- the five-channel Loss carrier names;
- paired YAML, Markdown, and Package artifacts.

For Record nodes, **YAML** and **Markdown** display the paired source artifacts directly inside Graph Lab. For other selected nodes, the matching linked YAML/JSON or Markdown artifact is displayed when one exists; otherwise the tab states that no artifact of that type is linked. **Summary** always identifies the selected node and its role as the active rotation pivot. All detail views are read-only. **Relations** displays previous/next occurrence, chain/package membership, paired artifacts, and related occurrences. **Trace** displays the bounded Source → Claim → Operation → Audit → Loss → Target → Output Class → Record sequence.

```text
raw artifact tab
≠ new parse result
≠ schema validation
≠ semantic finding
```

### 4.3 Dark mode and selection controls

Graph Lab now applies Light/Dark Mode consistently to:

- canvas and edge field;
- view, operation, and Output-Class select boxes;
- selected, hover, disabled, and drop-down states;
- detail notebook tabs;
- Summary, YAML, Markdown, Relations, and Trace surfaces;
- status surfaces.

The select-box text remains visible in both modes.

### 4.4 3D Case Tree labels

Case Tree labels now use a restrained background, border, and padding adapted to Light/Dark Mode. This improves legibility where graph edges overlap labels.

```text
label box
≠ node rank
≠ evidential weight
```

### 4.5 3D Case Tree

The tree is generated from declared Reader record summaries:

```text
PMS-STRATA Cases
→ operation
→ selected Output Class
→ individual Record
```

Available filters:

- operation: `COMPOSE`, `DECOMPOSE`, `PROJECT_AS`;
- selected Output Class;
- label visibility.

The layout is a visualization only:

```text
visual depth
≠ ontological depth

node size
≠ evidential strength

branch position
≠ class rank

visible relation
≠ new dependency
```

### 4.6 Authority Graph

The Authority Graph visualizes the declared repository order:

```text
PMS.yaml
→ 00_source
→ 01_blocks
→ 05_minified
→ 07_model
→ 02_appendices
→ 03_cases
→ 04_reference
→ 06_derivative_publications
→ 08 Reader
```

The graph preserves the controlling boundary:

```text
more structure
≠ more authority
```

### 4.7 Dependency Graph

The Dependency Graph links the current formal components:

- Root;
- Operation Registry;
- Admissibility Rules;
- Output Classes;
- Boundary Decision Tree;
- Shared Transformation Record Schema;
- Case Index;
- Reader views.

Double-clicking a component opens its repository artifact.

### 4.8 Transformation Flow

The Transformation Flow renders the audit path:

```text
Source + Claim
→ Operation Classification
→ 12-Stage Audit
→ Loss + Alternatives
→ Candidate Generation
→ Collision / Claim Split
→ one Output Class
→ Transformation Record
```

This is a route visualization, not Audit Stage 13.

### 4.9 Selected Record Trace

Open a case YAML record or its Markdown companion, then switch Graph Lab to **Selected Record Trace**.

The graph displays:

```text
Source
Claim
Operation
Audit
Target
Loss
Output Class
Record
```

Selecting any Record-associated node populates all five detail tabs for that Record.

### 4.10 Selected Chain

When the selected Record belongs to a shared Package Narrative or declared chain, **Selected Chain** renders all related operation occurrences and their local Output Classes.

Package membership is preferred over a single `chain_id`, because a package can preserve a sibling failure or countercase that is intentionally not absorbed into the successful chain.

```text
shared package
≠ merged operation
≠ averaged result
```

Each operation occurrence remains a separate node with a separate local class.

## 5. Current graph limitations

This remains an experimental prototype, not the final Reader described by the corpus.

Not yet implemented:

- direct field-level expansion of every Audit finding;
- complete five-channel Loss-value overlays per Record;
- historical branch-status validation in the rendering layer;
- source-supported alternative-history editing;
- Continuity Matrix switching;
- operator-profile overlays for all cases;
- action-corridor views;
- automatic graph export;
- persistent user layouts;
- high-density label collision avoidance;
- formal graph bundles generated during Model Finalization;
- a final maximum-detail 3D path tree for every case and test.

The present tree is therefore an inspection and navigation prototype rather than the final visualization architecture.

## 6. Planned Reader direction

Later Reader work can build on the current executable layer with views such as:

```text
Authority Graph
Dependency Graph
Transformation Flow
Claim-Splitting Graph
Class-Boundary Map
Chain Graph
Continuity Matrix
Interactive Record Trace
Path View
Trajectory View
Dependence View
Operator-Profile View
Action-Corridor View
Alternative-History View
Loss View
Competing-Construction View
```

A future maximum-detail 3D representation can use each test, Case, Markdown companion, YAML Record, Package Narrative, Loss profile, branch status, Stop, Failure, and Non-Capture carrier as declared graph input.

The governing constraint remains:

```text
Graphdarstellung
≠ neue Theorie
≠ neue Abhängigkeit
≠ neue Autorität
```

## 7. Prototype status boundary

The three derivative publications are present and explicitly routed in this Reader version. Their visibility does not change the repository authority order, create backflow into the canonical corpus, or turn Reader navigation into validation.

The Reader remains an experimental presentation layer. It may be used for inspection and design learning, but it must not be cited as substantive evidence, a completed semantic validator, or a source of analytical authority.
