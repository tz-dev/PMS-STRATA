# PMS-STRATA Reader

**Status:** experimental executable prototype; downstream presentation and navigation layer only  
**Version:** `0.3.0-prototype`  
**Implementation:** single-file Python/Tkinter desktop application  
**Authority:** none beyond the artifacts it reads

The current prototype adapts the first executable PMS-EM Reader layer to the active PMS-STRATA repository. It can open either the repository folder or a Source-of-Truth ZIP and provides ordinary corpus reading together with an initial interactive graph layer.

```text
Reader
≠ canonical corpus
≠ Formal Model
≠ evidence
≠ automatic classification
≠ application authority
```

The implementation deliberately reads declared repository relations. It does not generate new STRATA operations, claims, dependencies, Output Classes, historical alternatives, or authority relations.

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

A headless structural check is available:

```bash
python pms_strata_reader.py --self-test "/path/to/PMS-STRATA_Source_of_Truth.zip"
```

The self-test confirms, among other things:

- project-root detection;
- active-artifact ingestion;
- exclusion of `_workfiles/**`;
- transformation-record discovery;
- operation and Output-Class distributions;
- YAML/Markdown companion availability.

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

The following layer is excluded by default and is not searchable, rendered, indexed, or graphed:

```text
_workfiles/**
```

This is intentional. `_workfiles` is production provenance, not active Reader input.

## 3. Corpus Reader

The main window provides:

- a nested active-artifact navigator;
- a heading navigator for Markdown documents;
- Markdown-light rendering;
- YAML syntax coloring;
- JSON pretty rendering;
- aligned CSV display;
- corpus-wide full-text search;
- jump-to-result behavior;
- search highlighting;
- reader fullscreen;
- font scaling;
- light and dark mode.

The Reader parses the active Case Index and the 59 transformation-record YAML files into lightweight navigation summaries. This parsing is intentionally limited to declared identifiers and labels needed for presentation.

```text
Reader parse success
≠ schema validation
≠ substantive validation
```

Formal schema validation remains owned by `07_model/Transformation_Record.schema.json` and the repository audit workflow.

## 4. Graph Lab

Open **Graph Lab** from the toolbar or press `Ctrl+G`.

Controls:

```text
mouse drag
→ rotate the pseudo-3D graph

mouse wheel
→ zoom

single click
→ select node and show trace details

double click
→ open the linked repository artifact
```

### 4.1 3D Case Tree

The initial large tree is generated directly from the 59 YAML operation records:

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

### 4.2 Authority Graph

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

### 4.3 Dependency Graph

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

### 4.4 Transformation Flow

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

### 4.5 Selected Record Trace

Open a case YAML record or its same-basename Markdown companion, then switch Graph Lab to **Selected Record Trace**.

The view displays:

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

The right-hand trace panel shows the parsed case ID, title, operation, Output Class, case class, chapter owner, record ID, chain ID, claim, Source, Target, Markdown companion, and Package Narrative.

### 4.6 Selected Chain

When the selected Record belongs to a shared Package Narrative or declared chain, **Selected Chain** renders all related operation occurrences and their local Output Classes.

Package membership is preferred over a single `chain_id`, because a package can preserve a sibling failure or countercase that is intentionally not absorbed into the successful chain.

```text
shared package
≠ merged operation
≠ averaged result
```

Each operation occurrence remains a separate node with a separate local class.

## 5. Current graph limitations

This is an experimental prototype, not the final Reader described by the corpus.

Not yet implemented:

- direct field-level expansion of every Audit finding;
- complete five-channel Loss overlays per Record;
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

The present tree is therefore a useful executable proof of direction rather than the final visualization architecture.

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

The presence of this executable prototype does not change the controlled production sequence. Reference Freeze, Integrated Corpus Audit, Model Finalization, derivatives, final Reader work, and Release remain separate downstream stages.

The prototype may be used for inspection and design learning now. It must not be cited as a completed final Reader or as evidence that the later graph model is formally frozen.
