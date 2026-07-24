# PMS-STRATA — Glossary

**Status:** Reference Kernel v0.2.44 — Chapter-20-WP3-synchronized terminology core  
**Repository role:** `04_reference` navigation and terminology control; not an independent theory source  
**Authority basis:** `PMS.yaml`, `00_source/PMS-STRATA_Structure.md`, the Gate 1 minified kernel, `05_minified/Block_Contracts.md`, and `05_minified/Chapter_Contracts.md`

---

## 1. Function and Status

This glossary fixes the canonical working vocabulary used during production of the seven corpus Blocks. It supplies short definitions, designated primary definition sites, spelling conventions, and central non-equivalences. It does not replace canonical prose, the operator index, the operation index, the output-class index, or the appendices.

Until the relevant chapter is provisionally locked, each entry remains a controlled Reference definition. Chapter-0-owned entries route to the provisionally locked canonical prose in `01_blocks/01_foundations.md`. Chapter-1-owned entries route to the provisionally locked canonical object-model prose in the same Block; `04_reference/Chapter_1_Preparation_Record.md` records the completed WP1–WP4 production and audit history without becoming a theory source. Chapter-2-owned coordinate, scope, comparison, and Minimal Level Declaration entries now route to the provisionally locked canonical Sections 2.1–2.14; `04_reference/Chapter_2_Preparation_Record.md` records completed WP1–WP4 production and audit history without becoming a theory source. Chapter-3-owned configuration, state, event, non-event, transition, sequence, path, trajectory, path dependence, sedimentation, irreversibility, unrealized alternative, and Minimal Temporal Object Chain entries now route to canonical Sections 3.1–3.13; `04_reference/Chapter_3_Preparation_Record.md` records completed WP1–WP3 production and audit history without becoming a theory source. Chapter-4 through Chapter-7 entries now route to their provisionally locked canonical prose and synchronized execution records. Chapter-8-owned audit meaning, all thirteen foundational pairs, the integrated matrix, and catalogue-use guidance now route to provisionally locked canonical Sections 8.1–8.13. `04_reference/Chapter_8_Preparation_Record.md` records production history without theory authority. The field **Designated primary definition site** identifies where full canonical prose is or must be established. The field **Current control source** identifies the artifact that presently constrains the entry.

The governing terminology rule is:

```text
Each concept is defined once,
operationalized locally,
tested repeatedly,
and never re-derived without necessity.
```

## 2. Entry and Usage Rules

1. Canonical technical terms are written in English unless an operator symbol or fixed YAML identifier is used. German renderings are explanatory aliases, not competing canonical labels.
2. `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS` are always uppercase. They are the only core STRATA operations.
3. Canonical output classes use lowercase `snake_case`.
4. Δ–Ψ symbols and names follow `PMS.yaml`. STRATA does not rename, reorder, decompose, or extend them.
5. A designated primary chapter defines a term fully. Other chapters may apply, specify, test, or limit it without introducing a competing definition.
6. `frame`, `granularity`, `relative level`, and `transformation context` must never be used interchangeably.
7. `origin type` and `target function` must remain grammatically visible whenever PROJECT_AS is discussed.
8. Normal prose uses the canonical prose term; established formal predicates use `CamelCase`; canonical output classes use lowercase `snake_case`. A formal spelling is not a second concept.
9. Methodological concepts and output values remain distinct: for example, mandatory stop ≠ `mandatory_stop`, claim reduction ≠ `claim_reduction_required`, and Non-Capture ≠ `non_capture`.
10. Machine-field spellings not already fixed by the canonical kernel remain assigned to Formal Model v0 and are not invented in this glossary.

## 3. Scope of Glossary v0.2.15

Included are terms required by Foundations or repeatedly used across PATH, SUB, RETYPE, and LIMITS. Deferred to their dedicated reference artifacts are exhaustive operator dependencies, complete operation signatures, full output mappings, detailed claim types, record-field dictionaries, case identifiers, and final cross-references.

---

## A. Project, Claim, and Authority

### `PMS Base`

- **German working rendering:** PMS-Basis
- **Status:** PMS Base
- **Short definition:** The repository-reference PMS grammar defined by the Δ–Ψ operator inventory, its default dependency path, derived-structure rules, and application guardrails.
- **Designated primary definition site:** PMS.yaml
- **Current control sources:**
  - `PMS.yaml`
- **Central non-equivalences:**
  - PMS Base ≠ PMS-STRATA
  - PMS Base ≠ a claim of unique, final, or complete formalization

### `PMS-STRATA`

- **Status:** STRATA canonical
- **Short definition:** A bounded transformation discipline within PMS for composing, decomposing, and contextually projecting praxis structures across declared granularities and relative levels.
- **Designated primary definition site:** Chapter 0 — Position and Claim Boundary
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - PMS-STRATA ≠ a new PMS base
  - PMS-STRATA ≠ a superior or external meta-layer
  - PMS-STRATA ≠ an ontology of strata

### `bounded transformation discipline`

- **German working rendering:** begrenzte Transformationsdisziplin
- **Status:** STRATA canonical
- **Short definition:** A method whose operations are permitted only under declared source, context, continuity, loss, admissibility, stop, and claim constraints.
- **Designated primary definition site:** Chapter 0 — Position and Claim Boundary
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - bounded transformation discipline ≠ unrestricted analytical mobility
  - available transformation ≠ admissible transformation

### `governing claim`

- **German working rendering:** Leitclaim
- **Status:** STRATA canonical
- **Short definition:** The maximum positive claim that defines what STRATA specifies while preserving its dependency, authority, and failure boundaries.
- **Designated primary definition site:** Chapter 0
- **Secondary definition/application sites:**
  - final restatement in Chapter 57
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - governing claim ≠ empirical result
  - governing claim ≠ application authorization

### `claim boundary`

- **German working rendering:** Claim-Grenze
- **Status:** STRATA canonical
- **Short definition:** The explicit limit on what a reconstruction or transformation may assert, including what remains outside its scope and authority.
- **Designated primary definition site:** Chapter 0
- **Secondary definition/application sites:**
  - final closure in Chapter 57
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - claim boundary ≠ admissibility result
  - claim boundary ≠ source scope

### `claim type`

- **German working rendering:** Claim-Typ
- **Status:** STRATA canonical
- **Short definition:** The kind of structural, temporal, compositional, decompositional, functional, analogical, continuity, capture, or governance assertion made by a claim, distinct from its scope, support status, ceiling, record role, and output class.
- **Designated primary definition site:** Chapter 7 — Shared Transformation Record
- **Secondary definition/application sites:**
  - operation-specific application in Chapters 15, 20, and 30
  - integrated application in Chapter 53
- **Current control sources:**
  - `04_reference/Claim_Type_Table.md`
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - claim family ≠ claim type
  - claim type ≠ claim scope
  - claim type ≠ claim ceiling
  - claim type ≠ record status
  - claim type ≠ canonical output class
  - claim family ≠ universal rank

### `claim ceiling`

- **German working rendering:** Claim-Obergrenze
- **Status:** STRATA canonical
- **Short definition:** The maximum structurally and source-supported assertion—including its relation, reach, precision, generality, functional scope, and dependence strength—permitted by the available source, transformation, context, and governance constraints, subject to the independent authority ceiling.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - system-wide application in Chapters 49 and 53
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
  - `04_reference/Claim_Type_Table.md`
  - `04_reference/Admissibility_Band_Reference.md`
- **Central non-equivalences:**
  - claim ceiling ≠ Traceability Ceiling
  - claim ceiling ≠ Source Ceiling
  - claim ceiling ≠ authority ceiling
  - claim ceiling ≠ confidence score

### `No Meta-PMS`

- **Status:** STRATA canonical
- **Short definition:** The rule that STRATA neither stands above PMS Base nor gains authority to revise, adjudicate, or supersede it.
- **Designated primary definition site:** Chapter 0 — Position and Claim Boundary
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - method extension ≠ meta-theoretical superiority
  - integration ≠ authority inheritance

### `No Ontology of Strata`

- **Status:** STRATA canonical
- **Short definition:** The rule that frames, granularities, parts, composites, and declared level relations are analytical constructs or relations rather than claims about objectively discrete layers of reality.
- **Designated primary definition site:** Chapter 0
- **Secondary definition/application sites:**
  - system-wide elaboration in Chapter 42
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - relative level ≠ ontological layer
  - finer reconstruction ≠ deeper reality
  - composite ≠ ultimate whole
- **Control note:** Controlled alias: `No Ontology of Layers`.

### `No Universal STRATA Scale`

- **German working rendering:** keine universelle STRATA-Skala
- **Status:** STRATA canonical
- **Short definition:** The rule that STRATA has no universal smallest relevant element, largest legitimate composite, or fixed micro–meso–macro hierarchy; scale limits remain frame-, source-, object-, and claim-relative.
- **Designated primary definition site:** Chapter 6 — The STRATA Admissibility Band
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - no universal scale ≠ no local scale declaration
  - relational scale ≠ arbitrary scale

### `authority inheritance`

- **German working rendering:** Autoritätsvererbung
- **Status:** STRATA canonical
- **Short definition:** An impermissible transfer of evidential, normative, practical, or application authority from a source, formal layer, higher level, or successful transformation to a target claim.
- **Designated primary definition site:** Chapter 0
- **Secondary definition/application sites:**
  - governance field in Chapter 7
  - audit in Chapter 53
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - greater legibility ≠ greater authority
  - higher composition ≠ higher authority
  - formal validity ≠ application authority
- **Control note:** Canonical governance value: `authority_inheritance: prohibited`.

### `authority ceiling`

- **German working rendering:** Autoritätsobergrenze
- **Status:** STRATA canonical
- **Short definition:** The limit beyond which a structural transformation would illegitimately inherit or generate empirical, causal, normative, person-evaluative, legal, political, diagnostic, intervention, or application authority.
- **Designated primary definition site:** Chapter 0 — Governing Claim and Claim Boundary
- **Secondary definition/application sites:**
  - integrated Claim and Authority Ceiling audit in Chapter 53
  - prohibited-claim closure in Chapter 56
- **Current control sources:**
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
  - `04_reference/Admissibility_Band_Reference.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - claim ceiling ≠ authority ceiling
  - successful transformation ≠ application authority
  - formal validity ≠ semantic or empirical validity
- **Control note:** The authority ceiling prohibits authority inheritance; it is not a score, rank, or additional output class.

### `more structure ≠ more authority`

- **Status:** canonical governing principle
- **Short definition:** The governing non-equivalence that additional detail, composition, projection, formalization, or recursion does not by itself increase truth, legitimacy, or application authority.
- **Designated primary definition site:** Chapter 0
- **Secondary definition/application sites:**
  - canonical closure in Chapter 57
- **Current control sources:**
  - `README.md`
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - `01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary`
- **Central non-equivalences:**
  - more detail ≠ more truth
  - more operations ≠ stronger claim
  - machine-readable consistency ≠ semantic validity

## B. Object Model

### `operator sign`

- **German working rendering:** Operatorzeichen
- **Status:** PMS Base notation referenced by STRATA
- **Short definition:** The canonical symbol used in the current PMS repository reference to denote an operator type, such as `□`.
- **Designated primary definition site:** Chapter 1 for the STRATA distinction; `PMS.yaml` for the actual sign inventory
- **Current control sources:**
  - `PMS.yaml`
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `04_reference/Operator_Index.md`
- **Central non-equivalences:**
  - operator sign ≠ operator name
  - operator sign ≠ operator type

### `operator name`

- **German working rendering:** Operatorname
- **Status:** PMS Base nomenclature referenced by STRATA
- **Short definition:** The canonical English label associated in the current PMS repository reference with an operator sign and type, such as `Frame`.
- **Designated primary definition site:** Chapter 1 for the STRATA distinction; `PMS.yaml` for the actual name inventory
- **Current control sources:**
  - `PMS.yaml`
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `04_reference/Operator_Index.md`
- **Central non-equivalences:**
  - operator name ≠ operator sign
  - operator name ≠ operator type

### `operator type`

- **German working rendering:** Operator-Typ
- **Status:** STRATA canonical object-boundary term; semantic content governed by PMS Base
- **Short definition:** An abstract PMS Base function in the Δ–Ψ grammar to which a canonical sign and name refer; it is not a concrete occurrence or empirical object.
- **Designated primary definition site:** Chapter 1 — Object Model
- **Current control sources:**
  - `PMS.yaml`
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - operator type ≠ operator occurrence
  - operator type ≠ empirical object
  - operator type ≠ contextual target function
  - theoretical criticism of a type ≠ STRATA decomposition of that type

### `operator occurrence`

- **German working rendering:** Operator-Vorkommen
- **Status:** STRATA canonical
- **Short definition:** A concrete, reference-bound, context- or frame-bound, source-bound, and claim-bound structure reconstructed as expressing a PMS operator function within a specific analysis.
- **Designated primary definition site:** Chapter 1 — Object Model
- **Current control sources:**
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - operator occurrence ≠ operator type
  - operator occurrence ≠ composite structure
  - operator occurrence ≠ global person property
  - multiple occurrence typings ≠ composite formation

### `composite structure`

- **German working rendering:** Kompositstruktur
- **Status:** STRATA canonical
- **Short definition:** A selectively formed analytical object containing multiple identifiable constituents whose declared relations are constitutive of the object claimed.
- **Designated primary definition site:** Chapter 1 — Object Model
- **Current control sources:**
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - composite structure ≠ operator occurrence
  - composite structure ≠ list or co-presence
  - composite structure ≠ lossless sum
  - composite structure ≠ complete or ultimate whole
  - composite structure ≠ PMS operator composition
  - composite structure ≠ `Σ` Integration

### `configuration`

- **German working rendering:** Konfiguration
- **Status:** STRATA canonical
- **Short definition:** A temporally located, operator-structured, selectively incomplete praxis constellation formed relative to a declared analytical frame.
- **Designated primary definition site:** Chapter 1 as object category
- **Secondary definition/application sites:**
  - coordinate specification in Chapter 2
  - temporal specification in Chapter 3
- **Current control sources:**
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - [`Chapter 3 Sections 3.1–3.5`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - configuration ≠ complete world description
  - configuration ≠ event
  - configuration ≠ static ontology
  - one selected configuration ≠ exclusive world description

### `state`

- **German working rendering:** Zustand
- **Status:** STRATA canonical
- **Short definition:** A formal shorthand for a condition at an analytical time; less structurally rich than configuration where relations, non-events, and internal dynamics matter.
- **Designated primary definition site:** Chapter 3 — Temporal Object Chain
- **Current control sources:**
  - [`Chapter 3 Sections 3.1–3.5`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - state ≠ configuration in all contexts
  - state ≠ timeless essence

### `event-like object`

- **German working rendering:** ereignisartiges Objekt
- **Status:** STRATA canonical
- **Short definition:** A positively realized structural change treated as a bounded analytical unit, potentially extended, internally composite, and causally entangled; the category does not by itself supply the full temporal event grammar.
- **Designated primary definition site:** Chapter 1 — Object Model
- **Secondary definition/application sites:**
  - full temporal event definition in Chapter 3
- **Current control sources:**
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - event-like object ≠ necessarily punctual event
  - event-like object ≠ isolated cause
  - positive realization ≠ positive evaluation
  - event-like object ≠ transition

### `event`

- **German working rendering:** Ereignis
- **Status:** STRATA canonical
- **Short definition:** A temporally specified, frame-relevant occurrence or change that is positively realized within a reconstruction; it is the temporal category defined in Chapter 3, not merely the broader object-model category event-like object.
- **Designated primary definition site:** Chapter 3 — Temporal Object Chain
- **Current control sources:**
  - [`Chapter 3 Sections 3.1–3.5`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - event ≠ configuration
  - event ≠ transition
  - event ≠ non-event

### `non-event structure`

- **German working rendering:** Nicht-Ereignis-Struktur
- **Status:** STRATA canonical object-model category
- **Short definition:** A frame- and source-bound structured non-realization, delay, suspension, or blockage with an identifiable expected occurrence, warranted expectation relation, bounded realization condition, and praxeological load.
- **Designated primary definition site:** Chapter 1 — Object Model
- **Secondary definition/application sites:**
  - full temporal non-event definition in Chapter 3
  - PATH elaboration in Chapter 14
- **Current control sources:**
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `PMS.yaml`
  - `04_reference/Operator_Index.md`
- **Central non-equivalences:**
  - non-event structure ≠ mere absence
  - non-event structure ≠ missing information
  - non-event structure ≠ unknown event
  - positive sub-events ≠ elimination of the non-event structure

### `non-event`

- **German working rendering:** Nicht-Ereignis
- **Status:** STRATA canonical
- **Short definition:** A meaningful non-realization, delay, or absence of an expected occurrence within a supported expectation frame.
- **Designated primary definition site:** Chapter 3
- **Secondary definition/application sites:**
  - PATH elaboration in Chapter 14
- **Current control sources:**
  - [`Chapter 3 Sections 3.1–3.5`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `PMS.yaml`
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - non-event ≠ missing information
  - non-event ≠ every absence
  - non-event ≠ positive event

### `transition as object`

- **German working rendering:** Übergang als Analyseobjekt
- **Status:** STRATA canonical object-model category
- **Short definition:** A relation-bearing analytical object connecting identifiable configurations through supported order, intervening realized and non-realized structure, changed praxis conditions, and a declared transition boundary, without yet supplying the full temporal-chain definition.
- **Designated primary definition site:** Chapter 1 — Object Model
- **Secondary definition/application sites:**
  - full temporal transition definition in Chapter 3
  - PATH transition procedure in Chapter 9
- **Current control sources:**
  - [`01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
  - `05_minified/Chapter_Contracts.md`
- **Central non-equivalences:**
  - transition as object ≠ simple endpoint difference
  - transition as object ≠ event
  - transition as object ≠ path
  - object-category eligibility ≠ full temporal specification

### `transition`

- **German working rendering:** Übergang
- **Status:** STRATA canonical
- **Short definition:** A structured relation between configurations that preserves relevant temporal order, events, non-events, and changed praxis conditions.
- **Designated primary definition site:** Chapter 3
- **Secondary definition/application sites:**
  - validity procedure in Chapter 9
- **Current control sources:**
  - [`Chapter 3 Sections 3.1–3.5`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - transition ≠ difference between two isolated snapshots
  - transition ≠ event
  - transition ≠ path

### `derived analytical object`

- **German working rendering:** abgeleitetes Analyseobjekt
- **Status:** STRATA canonical
- **Short definition:** A source-dependent analytical object formed through a declared STRATA operation or chain, bounded formation rule, constitutive source trace, declared coordinates and loss, and explicit non-primitive status.
- **Designated primary definition site:** [Chapter 1 — Object Model](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
- **Secondary definition/application sites:**
  - operation-specific formation and validity in PATH, SUB, and RETYPE
- **Current control sources:**
  - canonical Chapter 1 Sections 1.9–1.11
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - `05_minified/Chapter_Contracts.md`
- **Central non-equivalences:**
  - derived analytical object ≠ new PMS primitive
  - derived analytical object ≠ operator type
  - derived analytical object ≠ analytical shorthand
  - derivation ≠ retroactive source-type replacement

### `object identity`

- **German working rendering:** Objektidentität
- **Status:** STRATA canonical
- **Short definition:** A bounded and defeasible claim that descriptions across declared change continue to concern the same historical or structural reference object, assessed through reference, supported typing, constitutive relations, function where relevant, temporal or historical continuity where relevant, and declared identity limits.
- **Designated primary definition site:** [Chapter 1 — Object Model](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) for minimum identification dimensions
- **Secondary definition/application sites:**
  - full transformation-continuity criteria in Chapter 5
  - record fields in Chapter 7
- **Current control sources:**
  - canonical Chapter 1 Sections 1.10–1.11
  - `05_minified/Chapter_Contracts.md`
  - `04_reference/Claim_Type_Table.md`
- **Central non-equivalences:**
  - object identity ≠ nominal sameness
  - object identity ≠ complete preservation
  - object identity ≠ immutable occurrence typing
  - historical reference continuity ≠ functional invariance
  - new analytical position ≠ repair of a prior identity failure

### `reference object`

- **German working rendering:** Referenzobjekt
- **Status:** STRATA canonical
- **Short definition:** The historical or structural object whose identity a transformation claims to preserve, open, compose, or project.
- **Designated primary definition site:** [Chapter 1 — Object Model](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure)
- **Secondary definition/application sites:**
  - continuity specification in Chapter 5
- **Current control sources:**
  - canonical Chapter 1 Sections 1.10–1.11
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - reference object ≠ label alone
  - same name ≠ same reference object

### `reference identity`

- **German working rendering:** Referenzidentität
- **Status:** STRATA canonical
- **Short definition:** The warranted claim that a transformation continues to concern the same identifiable historical or structural reference object despite declared changes in composition, granularity, or function.
- **Designated primary definition site:** Chapter 5 — Origin Type, Target Function, and Transformation Context
- **Secondary definition/application sites:**
  - minimal object-identification dimensions and nominal-sameness counterpressure in Chapter 1
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - canonical Chapter 1 Sections 1.10–1.11
  - `04_reference/Chapter_1_Preparation_Record.md`
- **Central non-equivalences:**
  - reference identity ≠ same label
  - reference identity ≠ complete preservation of detail

### `source object`

- **German working rendering:** Ausgangsobjekt
- **Status:** STRATA canonical
- **Short definition:** The declared object supplied to a STRATA operation, including its type, frame, granularity, level, temporal scope, and source basis.
- **Designated primary definition site:** Chapter 4
- **Secondary definition/application sites:**
  - record fields in Chapter 7
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - source object ≠ source material
  - source object ≠ target object

### `target object`

- **German working rendering:** Zielobjekt
- **Status:** STRATA canonical
- **Short definition:** The analytical object formed by COMPOSE or the finer reconstruction yielded by DECOMPOSE. In DECOMPOSE, the target is a new reconstruction of the same reference object, not automatically a new reference object. It remains distinct from a contextual target function in PROJECT_AS.
- **Designated primary definition site:** Chapter 4
- **Secondary definition/application sites:**
  - record fields in Chapter 7
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - target object ≠ target function
  - DECOMPOSE target ≠ automatically new reference object
  - target object ≠ necessarily new empirical object

### `provisional elementarity`

- **German working rendering:** vorläufige Elementarität
- **Status:** STRATA canonical
- **Short definition:** The analytical status of an object treated as undivided for a declared Frame, granularity, relative level, temporal scope, claim, source access, uncertainty, and present analytical use, without asserting absolute elementarity or ontological indivisibility.
- **Designated primary definition site:** [Chapter 18 §18.2](../01_blocks/03_part_ii_sub.md#18-2-provisional-elementarity)
- **Current control sources:**
  - [Chapter 18 WP1](../01_blocks/03_part_ii_sub.md#chapter-18-the-provisionally-compressed-object)
  - `04_reference/Chapter_18_Preparation_Record.md`
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - provisional elementarity ≠ final constituent
  - not currently decomposed ≠ undecomposable

### `compressed object`

- **German working rendering:** komprimiertes Objekt
- **Status:** STRATA canonical
- **Short definition:** An occurrence or composite treated as one analytical unit while the current representation leaves some internal distinctions, relations, or temporal structures unrepresented or unresolved.
- **Designated primary definition site:** [Chapter 18 §18.3](../01_blocks/03_part_ii_sub.md#18-3-the-compressed-object)
- **Current control sources:**
  - [Chapter 18 WP1](../01_blocks/03_part_ii_sub.md#chapter-18-the-provisionally-compressed-object)
  - `04_reference/Chapter_18_Preparation_Record.md`
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - compressed object ≠ simple object
  - compression ≠ falsification
  - compressed object ≠ operator type

## C. Analytical Coordinates and Scopes

### `frame`

- **German working rendering:** Frame / Bezugsrahmen
- **Status:** STRATA canonical
- **Short definition:** The declared contextual boundary that determines relevance, inside/outside, object focus, non-event relevance, and claim reach for a reconstruction.
- **Designated primary definition site:** Chapter 2 — Frame, Granularity, and Relative Level
- **Current control sources:**
  - [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
  - `PMS.yaml`
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - frame ≠ granularity
  - frame ≠ relative level
  - frame ≠ transformation context

### `granularity`

- **German working rendering:** Granularität / Auflösung
- **Status:** STRATA canonical
- **Short definition:** The resolution and distinction density used in a reconstruction.
- **Designated primary definition site:** Chapter 2 — Frame, Granularity, and Relative Level
- **Current control sources:**
  - [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - granularity ≠ frame
  - granularity ≠ relative level
  - finer granularity ≠ higher truth

### `relative level`

- **German working rendering:** relative Ebene
- **Status:** STRATA canonical
- **Short definition:** The position of an object within a declared compositional, part–whole, or functional relation to another object.
- **Designated primary definition site:** Chapter 2 — Frame, Granularity, and Relative Level
- **Current control sources:**
  - [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - relative level ≠ absolute rank
  - relative level ≠ ontological layer
  - relative level ≠ granularity

### `micro / meso / macro`

- **Status:** restricted shorthand
- **Short definition:** Optional shorthand for locally declared relative positions; never fixed universal classes or scales.
- **Designated primary definition site:** Chapter 2 — Frame, Granularity, and Relative Level
- **Current control sources:**
  - [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
  - `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`
- **Central non-equivalences:**
  - micro / meso / macro ≠ ontological strata
  - macro ≠ greater authority
  - micro ≠ deeper truth

### `temporal scope`

- **German working rendering:** zeitlicher Geltungs- oder Betrachtungsbereich
- **Status:** STRATA canonical
- **Short definition:** The declared temporal inclusion boundary of a reconstruction, including its primary interval, entry boundary, endpoint or open continuation, relevant prior conditions, later effects, and periodization uncertainty.
- **Designated primary definition site:** Chapter 2 — Frame, Granularity, and Relative Level
- **Current control sources:**
  - [`Chapter 2 WP2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - temporal scope ≠ temporal ordering
  - temporal scope ≠ temporal granularity
  - temporal scope ≠ sequence / path / trajectory / path dependence
  - temporal scope ≠ validity scope

### `source scope`

- **German working rendering:** Quellenumfang
- **Status:** STRATA canonical
- **Short definition:** The declared boundary of the material basis and source-supported distinctions available to a reconstruction, including direct support, inference, missing structure, uncertainty, and the speculative edge.
- **Designated primary definition site:** Chapter 2 — Frame, Granularity, and Relative Level
- **Current control sources:**
  - [`Chapter 2 WP2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - source basis ≠ source scope ≠ source ceiling
  - source scope ≠ claim scope
  - source scope ≠ source object
  - missing information ≠ positive source-supported structure

### `claim scope`

- **German working rendering:** Claim-Umfang
- **Status:** STRATA canonical
- **Short definition:** The declared range within which a tested statement applies, including its object, predicate, coordinates, temporal and contextual reach, generalization status, exclusions, and re-entry condition.
- **Designated primary definition site:** Chapter 2 — Frame, Granularity, and Relative Level
- **Current control sources:**
  - [`Chapter 2 WP2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - claim scope ≠ source scope
  - claim scope ≠ claim boundary
  - claim scope ≠ claim ceiling
  - claim scope ≠ validity scope
  - local claim ≠ global attribution

### `transformation context`

- **German working rendering:** Transformationskontext
- **Status:** STRATA canonical
- **Short definition:** The declared context in which an operation is expected to produce analytical performance and within which its target and validity are determined.
- **Designated primary definition site:** Chapter 5 — Origin Type, Target Function, and Transformation Context
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - transformation context ≠ source frame
  - transformation context ≠ target function
  - changed frame ≠ transformation context by itself

### `target context`

- **German working rendering:** Zielkontext
- **Status:** STRATA canonical
- **Short definition:** The declared analytical context within which an origin-typed source object is claimed to perform a bounded target function.
- **Designated primary definition site:** Chapter 5 — Origin Type, Target Function, and Transformation Context
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - target context ≠ source frame
  - target context ≠ transformation context as a whole
  - new frame ≠ PROJECT_AS without target function

### `validity scope`

- **German working rendering:** Geltungsbereich
- **Status:** STRATA canonical
- **Short definition:** The bounded context, period, level, roles, and praxis dimensions within which a transformation result may be used as claimed.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - PROJECT_AS specification in Chapter 30
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - validity scope ≠ universal transferability
  - validity scope ≠ source scope

## D. Temporal and Path Structures

### `sequence`

- **German working rendering:** Sequenz
- **Status:** STRATA canonical
- **Short definition:** A temporally ordered series that has not yet established the structural connectedness and selection burden required for a path.
- **Designated primary definition site:** Chapter 3 — Temporal Object Chain
- **Current control sources:**
  - [`Chapter 3 Sections 3.1–3.13`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `05_minified/Chapter_Contracts.md`
- **Central non-equivalences:**
  - sequence ≠ path
  - sequence ≠ trajectory
  - sequence ≠ path dependence

### `path`

- **German working rendering:** Pfad
- **Status:** STRATA canonical
- **Short definition:** The actually traversed, analytically reconstructed sequence of relevant configurations and transitions within a declared frame.
- **Designated primary definition site:** Chapter 3
- **Secondary definition/application sites:**
  - full PATH specification in Chapter 10
- **Current control sources:**
  - [`Chapter 3 Sections 3.1–3.13`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `05_minified/Chapter_Contracts.md`
- **Central non-equivalences:**
  - path ≠ chronology
  - path ≠ trajectory
  - path ≠ path dependence

### `trajectory`

- **German working rendering:** Trajektorie
- **Status:** STRATA canonical
- **Short definition:** A temporally ordered path whose sedimented structure historically conditions the current configuration and its continuation possibilities without implying teleology.
- **Designated primary definition site:** Chapter 3
- **Secondary definition/application sites:**
  - full PATH specification in Chapter 11
- **Current control sources:**
  - [`Chapter 3 Sections 3.1–3.13`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - [`Chapter 11 §11.1`](../01_blocks/02_part_i_path.md#11-1-definition-of-trajectory)
  - `05_minified/Chapter_Contracts.md`
- **Central non-equivalences:**
  - trajectory ≠ path
  - trajectory ≠ path dependence
  - trajectory ≠ predetermined development

### `path dependence`

- **German working rendering:** Pfadabhängigkeit
- **Status:** STRATA canonical
- **Short definition:** A property whereby present meaning, cost, or reachable continuation cannot be reconstructed adequately from the current state alone because prior order remains structurally load-bearing.
- **Designated primary definition site:** Chapter 3
- **Secondary definition/application sites:**
  - full test in Chapter 12
- **Current control sources:**
  - [`Chapter 3 §3.9`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - path dependence ≠ trajectory
  - path dependence ≠ duration
  - path dependence ≠ determinism

### `sedimentation`

- **German working rendering:** Sedimentation
- **Status:** STRATA canonical
- **Short definition:** The accumulation and persistence of historically produced attractors, asymmetries, bindings, residues, or changed action corridors.
- **Designated primary definition site:** Chapter 3
- **Secondary definition/application sites:**
  - PATH elaboration in Chapters 11–12
- **Current control sources:**
  - [`Chapter 3 §3.10`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - [`Chapter 11 §11.3`](../01_blocks/02_part_i_path.md#11-3-historical-sedimentation)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - sedimentation ≠ mere duration
  - sedimentation ≠ inevitable direction

### `irreversibility`

- **German working rendering:** Irreversibilität
- **Status:** STRATA canonical
- **Short definition:** A frame- and claim-bounded condition in which later change does not restore the original praxis structure, costs, alternatives, or historical position.
- **Designated primary definition site:** Chapter 3 — Temporal Object Chain
- **Current control sources:**
  - [`Chapter 3 §3.11`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - irreversibility ≠ metaphysical impossibility
  - exit ≠ reset
  - recontextualization ≠ erasure

### `unrealized alternative`

- **German working rendering:** nicht realisierte Alternative
- **Status:** STRATA canonical
- **Short definition:** A source-bounded continuation that was available, rejected, blocked, deferred, aborted, or later lost but not actually traversed.
- **Designated primary definition site:** Chapter 3
- **Secondary definition/application sites:**
  - classification in Chapter 13
- **Current control sources:**
  - [`Chapter 3 §3.12`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - unrealized alternative ≠ free counterfactual fiction
  - unrealized alternative ≠ missing information

### `historical load`

- **German working rendering:** historische Last
- **Status:** STRATA canonical
- **Short definition:** The continuing structural relevance of earlier transitions, non-events, costs, asymmetries, bindings, and closed alternatives for a later configuration.
- **Designated primary definition site:** Chapter 11 — Trajectory
- **Current control sources:**
  - [`Chapter 11 §§11.1–11.3`](../01_blocks/02_part_i_path.md#11-1-definition-of-trajectory)
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - historical load ≠ narrative background
  - historical load ≠ determinism

## E. Operations and Transformation Records

### `STRATA operation`

- **German working rendering:** STRATA-Operation
- **Status:** STRATA canonical
- **Short definition:** One of the exactly three core transformation types: COMPOSE, DECOMPOSE, or PROJECT_AS.
- **Designated primary definition site:** Chapter 4 — The Three STRATA Operations
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - operation type ≠ operation occurrence
  - LIMITS ≠ operation
  - recontextualization ≠ fourth STRATA operation

### `COMPOSE`

- **Status:** STRATA canonical
- **Short definition:** The operation that forms a new composite analytical object from multiple or sequential source structures under declared selection, ordering, formation, preservation, and loss rules.
- **Designated primary definition site:** Chapter 4
- **Secondary definition/application sites:**
  - full procedure in Chapter 15
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - COMPOSE ≠ chronology
  - COMPOSE ≠ lossless addition
  - COMPOSE ≠ automatic PROJECT_AS

### `DECOMPOSE`

- **Status:** STRATA canonical
- **Short definition:** The operation that reconstructs a provisionally compressed occurrence or composite under finer granularity while preserving or testing the same reference object and its coarser function.
- **Designated primary definition site:** Chapter 4
- **Secondary definition/application sites:**
  - full procedure in Chapter 20
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - DECOMPOSE ≠ decomposition of operator types
  - DECOMPOSE ≠ mere description
  - DECOMPOSE ≠ automatic truth gain

### `PROJECT_AS`

- **Status:** STRATA canonical
- **Short definition:** The operation that preserves an origin-typed source object while assigning it a bounded contextual target function.
- **Designated primary definition site:** Chapter 4
- **Secondary definition/application sites:**
  - full procedure in Chapter 30
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - PROJECT_AS ≠ origin-type replacement
  - PROJECT_AS ≠ analogy
  - PROJECT_AS ≠ label substitution

### `operation occurrence`

- **German working rendering:** Operationsvorkommen
- **Status:** STRATA canonical
- **Short definition:** A particular declared use of COMPOSE, DECOMPOSE, or PROJECT_AS on specified source and target structures in a transformation context.
- **Designated primary definition site:** Chapter 4 — The Three STRATA Operations
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - operation occurrence ≠ operation type
  - operation occurrence ≠ composite output

### `operation chain`

- **German working rendering:** Operationskette
- **Status:** STRATA canonical
- **Short definition:** A sequence of two or more separately declared STRATA operations, each with its own justification, continuity, loss, admissibility, and result.
- **Designated primary definition site:** Chapter 4
- **Secondary definition/application sites:**
  - integrated audit in Chapter 53
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - operation chain ≠ single compound operation
  - later operation ≠ retroactive validation of earlier operation

### `non-invertibility`

- **German working rendering:** Nicht-Invertierbarkeit
- **Status:** STRATA canonical
- **Short definition:** The rule that STRATA operations are not losslessly reversible and do not restore a neutral or original representation by applying an apparent inverse.
- **Designated primary definition site:** Chapter 4 — The Three STRATA Operations
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - DECOMPOSE(COMPOSE(X)) ≠ X
  - COMPOSE(DECOMPOSE(X)) ≠ X
  - PROJECT_AS(X) ≠ X as a new origin type

### `shared transformation record`

- **German working rendering:** gemeinsamer Transformationsrecord
- **Status:** STRATA canonical
- **Short definition:** The common record architecture used to declare source, operation, target, claim, admissibility, loss, alternatives, stop, non-capture, and governance.
- **Designated primary definition site:** Chapter 7 — Shared Transformation Record
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - record completeness ≠ empirical truth
  - record ≠ automatic decision
  - local extension ≠ bypass of common duties

### `record status`

- **German working rendering:** Record-Status
- **Status:** STRATA canonical
- **Short definition:** The record-level status declaration architecture that preserves separate support, resolution, claim-disposition, and capture information without replacing the canonical output class or collapsing those axes into one mixed enum.
- **Designated primary definition site:** Chapter 7 — Shared Transformation Record
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - `04_reference/Claim_Type_Table.md`
  - `04_reference/Output_Class_Index.md`
  - `04_reference/Evidence_Map.md`
- **Central non-equivalences:**
  - record status ≠ support status
  - record status ≠ output class
  - record status ≠ one flat mixed status enum
  - supported record ≠ true claim

### `operation-specific result`

- **German working rendering:** operationsspezifisches Ergebnis
- **Status:** STRATA canonical
- **Short definition:** A local description of what occurred within a particular COMPOSE, DECOMPOSE, or PROJECT_AS occurrence, retained alongside—but not replaced by—its canonical output class.
- **Designated primary definition site:** Chapter 6 — The STRATA Admissibility Band
- **Secondary definition/application sites:**
  - local result catalogues in Chapters 17, 28, and 40
  - integrated use in Chapter 53
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - `04_reference/Transformation_Operation_Index.md`
  - `04_reference/Output_Class_Index.md`
- **Central non-equivalences:**
  - operation-specific result ≠ canonical output class
  - local result label ≠ new system-wide class
  - operation result ≠ prior source-claim result

## F. Projection, Functions, and Profiles

### `origin type`

- **German working rendering:** Ursprungstyp
- **Status:** STRATA canonical
- **Short definition:** The analytical type of the source object in its source reconstruction, preserved through PROJECT_AS.
- **Designated primary definition site:** Chapter 5 — Origin Type, Target Function, and Transformation Context
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - origin type ≠ target function
  - origin type ≠ operator weighting
  - origin type ≠ person type

### `target function`

- **German working rendering:** Zielfunktion
- **Status:** STRATA canonical
- **Short definition:** The bounded role an origin-typed source object performs within a declared target context.
- **Designated primary definition site:** Chapter 5 — Origin Type, Target Function, and Transformation Context
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - target function ≠ origin type
  - target function ≠ new primitive
  - target function ≠ universal property

### `source function`

- **German working rendering:** Ausgangsfunktion
- **Status:** STRATA canonical
- **Short definition:** The coarser or current function attributed to a source object before DECOMPOSE, which the finer reconstruction may confirm, refine, differentiate, partially preserve, or reject.
- **Designated primary definition site:** Chapter 20 — DECOMPOSE
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - source function ≠ target function
  - source function ≠ immune source typing
  - finer components ≠ automatic rejection of source function

### `functional projection`

- **German working rendering:** funktionale Projektion
- **Status:** STRATA canonical
- **Short definition:** A typed claim that a source object, while retaining its origin type, performs a specified function in a declared target context.
- **Designated primary definition site:** Chapter 29 — Functional Projection
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - functional projection ≠ recontextualization alone
  - functional projection ≠ analogy
  - functional projection ≠ type identity

### `frame-function`

- **German working rendering:** Frame-Funktion
- **Status:** STRATA canonical
- **Short definition:** A bounded target function through which a source object structures relevance, expectation, interpretation, or available action within a target context.
- **Designated primary definition site:** Chapter 31 — Trajectory as Frame-Function
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - frame-function ≠ Frame operator type
  - trajectory as frame-function ≠ trajectory becomes □

### `macro-event`

- **German working rendering:** Makroereignis
- **Status:** STRATA canonical
- **Short definition:** A bounded target function in which a temporally extended trajectory operates as a transition-relevant event within a wider temporal frame.
- **Designated primary definition site:** Chapter 32 — Trajectory as Macro-Event
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - macro-event ≠ punctual event
  - macro-event ≠ trajectory stripped of internal duration
- **Control note:** Canonical RETYPE shorthand for `macro-event function`; it does not name a new event operator type.

### `attractor-function`

- **German working rendering:** Attraktor-Funktion
- **Status:** STRATA canonical
- **Short definition:** A bounded target function through which a recurrent structure stabilizes a configuration or transition form within a declared context.
- **Designated primary definition site:** Chapter 33 — Recurrent Trajectory Form as Attractor-Function
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - attractor-function ≠ Attractor operator type
  - recurrent similarity ≠ attractor-function

### `higher-level function`

- **German working rendering:** höherstufige Funktion
- **Status:** STRATA canonical
- **Short definition:** A source-traceable contextual function visible only at the level of a composite relation and not reducible to mere aggregation.
- **Designated primary definition site:** Chapter 34 — Composite Structures as Higher-Level Functions
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - higher-level function ≠ new primitive
  - higher-level function ≠ authority increase
  - aggregation ≠ functional formation

### `operator weighting`

- **German working rendering:** Operatorgewichtung
- **Status:** STRATA canonical
- **Short definition:** The relative analytical load, visibility, or temporal effectiveness of existing PMS operator occurrences within a configuration or composite.
- **Designated primary definition site:** Chapter 35 — Operator Weighting and Modulation
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - operator weighting ≠ operator replacement
  - weighting ≠ changed PMS dependency order
  - dominance ≠ new operator

### `modulator`

- **German working rendering:** Modulator
- **Status:** STRATA canonical
- **Short definition:** A non-operator condition that changes thresholds, accessibility, stabilization burdens, or path likelihoods without becoming a PMS primitive.
- **Designated primary definition site:** Chapter 35 — Operator Weighting and Modulation
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - modulator ≠ operator
  - modulator ≠ person type

### `modulating profile`

- **German working rendering:** modulierendes Profil
- **Status:** STRATA canonical
- **Short definition:** A configuration-bound pattern of operator weightings, thresholds, accessibility, and temporal effects.
- **Designated primary definition site:** Chapter 35 — Operator Weighting and Modulation
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - modulating profile ≠ operator type
  - modulating profile ≠ personality profile
  - profile ≠ universal class

### `structural analogy`

- **German working rendering:** strukturelle Analogie
- **Status:** STRATA canonical
- **Short definition:** A bounded comparison based on formal or relational similarity that does not by itself establish semantic preservation or PROJECT_AS validity.
- **Designated primary definition site:** Chapter 37 — Projection, Structural Analogy, and Label Substitution
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - structural analogy ≠ valid functional projection
  - structural analogy ≠ label substitution
  - formal correspondence ≠ semantic preservation
  - symbolic mapping ≠ praxeological function
- **Control note:** Methodological concept; corresponding canonical output value: `analogy_only` when no valid projection is established.

### `label substitution`

- **German working rendering:** Labelsubstitution
- **Status:** STRATA canonical
- **Short definition:** The application of a PMS or STRATA label to a target without additional discriminative performance, source trace, counterfactual sensitivity, or bounded function.
- **Designated primary definition site:** Chapter 37 — Projection, Structural Analogy, and Label Substitution
- **Current control sources:**
  - `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- **Central non-equivalences:**
  - label substitution ≠ PROJECT_AS
  - structural analogy ≠ label substitution
  - renaming ≠ transformation

### `invalid type jump`

- **German working rendering:** ungültiger Typensprung
- **Status:** STRATA canonical
- **Short definition:** An undeclared or unsupported replacement of one analytical type by another, especially when a target function is rewritten as an origin type.
- **Designated primary definition site:** Chapter 38 — Invalid Type Jumps and Level Mixing
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - functions as T ≠ is T as origin type
  - local function ≠ global property

### `level mixing`

- **German working rendering:** Ebenenvermischung
- **Status:** STRATA canonical
- **Short definition:** The unmarked collapse of claims, evidence, functions, or objects from different relative levels into a single assertion.
- **Designated primary definition site:** Chapter 38 — Invalid Type Jumps and Level Mixing
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - level mixing ≠ declared cross-level relation
  - micro support ≠ macro entailment

### `granularity mixing`

- **German working rendering:** Granularitätsvermischung
- **Status:** STRATA canonical
- **Short definition:** The unmarked comparison or evidential transfer between fine and coarse reconstructions without a declared granularity relation.
- **Designated primary definition site:** Chapter 38 — Invalid Type Jumps and Level Mixing
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - granularity mixing ≠ multi-granular analysis
  - fine detail ≠ automatic macro proof

## G. Admissibility, Continuity, Source, and Loss

### `STRATA Admissibility Band`

- **German working rendering:** STRATA-Zulässigkeitsband
- **Status:** STRATA canonical
- **Short definition:** The non-numeric operating range between the Praxeological Relevance Floor and the Praxeological Traceability Ceiling within which a transformation must also preserve type integrity and contextual boundedness.
- **Designated primary definition site:** Chapter 6 — STRATA Admissibility Band
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - Admissibility Band ≠ score
  - Admissibility Band ≠ universal scale
  - within band ≠ empirically true

### `admissible transformation`

- **German working rendering:** zulässige Transformation
- **Status:** STRATA canonical
- **Short definition:** A declared operation that produces warranted praxis-relevant difference while retaining traceable source load, type integrity, contextual boundedness, and applicable continuity and source constraints.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - integrated audit in Chapter 53
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - admissible ≠ true
  - admissible ≠ causally proven
  - admissible ≠ authorized for intervention

### `Praxeological Relevance Floor`

- **Status:** STRATA canonical
- **Short definition:** The lower boundary below which additional distinction or resolution no longer changes a warranted praxis-relevant reconstruction.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - full elaboration in Chapter 44
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - additional detail ≠ additional praxis finding
  - Relevance Floor ≠ source ceiling

### `PraxisPurchase`

- **Status:** STRATA canonical
- **Short definition:** The demonstrated difference a distinction or transformation makes to a warranted reconstruction of action corridors, costs, roles, asymmetries, expectations, temporality, bindings, or related praxis dimensions.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - Changed-Reconstruction Test in Chapter 44
- **Formal notation:** `PraxisPurchase(T, X, C)`
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - PraxisPurchase ≠ practical recommendation
  - PraxisPurchase ≠ mere detail

### `Changed-Reconstruction Test`

- **German working rendering:** Test der veränderten Rekonstruktion
- **Status:** STRATA canonical
- **Short definition:** The question of which warranted claim, distinction, cost structure, path, function, alternative, or stop decision must change because of an added distinction.
- **Designated primary definition site:** Chapter 44 — Praxeological Relevance Floor
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - changed wording ≠ changed reconstruction
  - more description ≠ changed reconstruction

### `resolution gain`

- **German working rendering:** Auflösungsgewinn
- **Status:** STRATA canonical
- **Short definition:** A finer reconstruction that reveals a relevant distinction, relation, cost, alternative, or source-function revision.
- **Designated primary definition site:** Chapter 25
- **Secondary definition/application sites:**
  - system-wide interpretation in Chapter 44
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - resolution gain ≠ more detail
  - resolution gain ≠ higher truth

### `resolution neutrality`

- **German working rendering:** Auflösungsneutralität
- **Status:** STRATA canonical
- **Short definition:** A result in which added detail may be accurate but does not alter the warranted source reconstruction or claim.
- **Designated primary definition site:** Chapter 25
- **Secondary definition/application sites:**
  - system-wide interpretation in Chapter 44
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - resolution neutrality ≠ failed transformation
  - resolution neutrality ≠ resolution gain
- **Control note:** Methodological concept; corresponding canonical output value: `resolution_neutral`.

### `resolution drift`

- **German working rendering:** Auflösungsdrift
- **Status:** STRATA canonical
- **Short definition:** A loss of reconstructive control in which detail, complexity, or uncertainty increases faster than discrimination, relation, source support, or calibration.
- **Designated primary definition site:** Chapter 25 — Resolution Gain, Neutrality, Drift, and Escape
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - resolution drift ≠ legitimate finer granularity
  - complexity ≠ gain

### `resolution escape`

- **German working rendering:** Auflösungsflucht
- **Status:** STRATA canonical
- **Short definition:** An anti-immunization failure in which a challenged claim is moved to increasingly fine granularity without directly answering or revising the original objection.
- **Designated primary definition site:** Chapter 25
- **Secondary definition/application sites:**
  - system-wide rule in Chapter 50
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - resolution escape ≠ warranted DECOMPOSE
  - new detail ≠ refutation of original objection

### `Praxeological Traceability Ceiling`

- **Status:** STRATA canonical
- **Short definition:** The upper boundary beyond which a composition, decomposition, or projection no longer carries reconstructible structural load from its source objects; in DECOMPOSE this includes fragmentation that loses the reference object or coarser functional load.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - full elaboration in Chapter 45
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - Traceability Ceiling ≠ claim ceiling
  - traceability ≠ exhaustiveness
  - citation ≠ traceable load

### `TraceableLoad`

- **Status:** STRATA canonical
- **Short definition:** The preserved constitutive source structure, relations, temporality, cost and asymmetry pattern, and source-result dependency carried by a transformation result and its tested claim.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - full elaboration in Chapter 45
- **Formal notation:** `TraceableLoad(T, X, C)`
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - TraceableLoad ≠ complete reproduction
  - TraceableLoad ≠ source citation alone

### `Constitutive Source Trace`

- **German working rendering:** konstitutive Quellspur
- **Status:** STRATA canonical
- **Short definition:** The explicit mapping from a target object or function to its load-bearing, modulating, compressed, excluded, and uncertain source features.
- **Designated primary definition site:** Chapter 45 — Praxeological Traceability Ceiling
- **Secondary definition/application sites:**
  - Chapter 30 — PROJECT_AS local specification
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - Constitutive Source Trace ≠ bibliography
  - source trace ≠ lossless copy

### `Counterfactual Sensitivity`

- **German working rendering:** kontrafaktische Sensitivität
- **Status:** STRATA canonical
- **Short definition:** The load test asking whether a relevant change in a declared constitutive source feature would alter the transformation result.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - system-wide definition in Chapter 46
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - Counterfactual Sensitivity ≠ causal proof
  - untestable ≠ automatically false
  - insensitive result ≠ source-dependent result

### `Type Integrity`

- **German working rendering:** Typintegrität
- **Status:** STRATA canonical
- **Short definition:** The requirement that source types, derived objects, components, and contextual functions remain correctly distinguished through transformation.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - admissibility gate in Chapter 6
- **Formal notation:** `TypeIntegrity(T, X, C)`
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - origin type ≠ target function
  - derived function ≠ new primitive
  - component type ≠ automatic whole type

### `reference continuity`

- **German working rendering:** Referenzkontinuität
- **Status:** STRATA canonical
- **Short definition:** The preservation of the same identifiable historical or structural reference object through a transformation, subject to declared limits.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - audit elaboration in Chapter 47
- **Formal notation:** `ReferenceContinuityPreserved`
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - same label ≠ reference continuity
  - reference continuity ≠ complete detail preservation

### `type continuity`

- **German working rendering:** Typkontinuität
- **Status:** STRATA canonical
- **Short definition:** The preservation of the source or origin type as visible and correctly bounded while outputs or functions are added, tested, or revised.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - audit elaboration in Chapter 47
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - type continuity ≠ type immunity
  - target function ≠ origin-type replacement

### `functional continuity`

- **German working rendering:** funktionale Kontinuität
- **Status:** STRATA canonical
- **Short definition:** The dependency of a claimed function on concrete source features within a bounded target context.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - audit elaboration in Chapter 47
- **Formal notation:** `FunctionalContinuityWarranted`
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - functional continuity ≠ semantic similarity
  - function independent of source ≠ functional continuity

### `temporal continuity`

- **German working rendering:** temporale Kontinuität
- **Status:** STRATA canonical
- **Short definition:** The preservation of relevant order, duration, transitions, sedimentation, and historical load across temporal compression or projection.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - audit elaboration in Chapter 47
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - temporal continuity ≠ complete chronology
  - macro-event ≠ punctualization

### `contextual boundedness`

- **German working rendering:** kontextuelle Begrenztheit
- **Status:** STRATA canonical
- **Short definition:** The requirement that a target function or transformation claim remain limited to a declared context, level, period, and affected praxis dimensions.
- **Designated primary definition site:** Chapter 5
- **Secondary definition/application sites:**
  - admissibility gate in Chapter 6
- **Formal notation:** `ContextualBoundedness(T, X, C)`
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - contextual boundedness ≠ universal transfer
  - local validity ≠ global property

### `loss`

- **German working rendering:** Verlust
- **Status:** STRATA canonical
- **Short definition:** The transformation-dependent change in visibility or recoverability that must be declared through the canonical loss classes.
- **Designated primary definition site:** Chapter 7
- **Secondary definition/application sites:**
  - system-wide elaboration in Chapter 48
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - selection ≠ loss
  - loss ≠ automatic failure
  - loss disclosure ≠ losslessness
  - uncertainty ≠ irrecoverability
- **Control note:** Canonical classes: `preserved`, `compressed`, `excluded`, `uncertain`, `irrecoverable`.

### `source basis`

- **German working rendering:** Quellenbasis
- **Status:** STRATA canonical
- **Short definition:** The declared set of documents, records, observations, reconstructed relations, existing PMS objects, or other materials on which a tested claim relies.
- **Designated primary definition site:** Chapter 49 — Source Limits and Calibration Limits
- **Secondary definition/application sites:**
  - shared record declaration in Chapter 7
  - operation applications in Chapters 15, 20, and 30
  - integrated audit in Chapter 53
- **Current control sources:**
  - `04_reference/Evidence_Map.md`
  - `04_reference/Claim_Type_Table.md`
- **Central non-equivalences:**
  - source basis ≠ Constitutive Source Trace
  - source basis ≠ Source Ceiling
  - source basis ≠ source scope
  - evidence item ≠ source basis
  - source quantity ≠ support sufficiency

### `support mode`

- **German working rendering:** Unterstützungsmodus
- **Status:** STRATA canonical
- **Short definition:** The declared way in which source material bears on a tested claim—directly, indirectly, through reconstruction, or through a mixed component-level relation—without deciding the claim's support status.
- **Designated primary definition site:** Chapter 7 — Shared Transformation Record
- **Secondary definition/application sites:**
  - source and calibration limits in Chapter 49
  - operation records in Chapters 15, 20, and 30
- **Current control sources:**
  - `04_reference/Evidence_Map.md`
  - `04_reference/Claim_Type_Table.md`
- **Central non-equivalences:**
  - support mode ≠ support status
  - direct support ≠ stronger claim automatically
  - indirect support ≠ weak support automatically

### `support status`

- **German working rendering:** Unterstützungsstatus
- **Status:** STRATA canonical
- **Short definition:** The declared current condition of support for a tested claim—supported, provisional, contested, underdetermined, or unsupported—distinct from support mode, evidence availability, claim disposition, record status, operation-specific result, and canonical output class.
- **Designated primary definition site:** Chapter 7 — Shared Transformation Record
- **Secondary definition/application sites:**
  - source and calibration limits in Chapter 49
  - integrated audit in Chapter 53
- **Current control sources:**
  - `04_reference/Evidence_Map.md`
  - `04_reference/Claim_Type_Table.md`
  - `04_reference/Output_Class_Index.md`
- **Central non-equivalences:**
  - support mode ≠ support status
  - evidence availability ≠ support status
  - claim disposition ≠ support status
  - record status ≠ support status
  - support status ≠ claim type
  - support status ≠ operation-specific result
  - support status ≠ canonical output class
  - support downgrade ≠ claim reduction

### `evidence availability`

- **German working rendering:** Evidenzverfügbarkeit
- **Status:** STRATA canonical
- **Short definition:** The declared access condition of claim-relevant material—available, partially available, missing, unavailable, or inaccessible—separate from how that material supports a claim and from whether external warrant is required.
- **Designated primary definition site:** Chapter 49 — Source Limits and Calibration Limits
- **Secondary definition/application sites:**
  - shared record declaration in Chapter 7
  - operation records in Chapters 15, 20, and 30
  - integrated audit in Chapter 53
- **Current control sources:**
  - `04_reference/Evidence_Map.md`
  - `04_reference/Claim_Type_Table.md`
- **Central non-equivalences:**
  - evidence availability ≠ support status
  - evidence availability ≠ support sufficiency
  - missing information ≠ non-event
  - external warrant required ≠ support status

### `Source Ceiling`

- **German working rendering:** Quellenobergrenze
- **Status:** STRATA canonical
- **Short definition:** The point beyond which available sources no longer support additional distinctions, internal processes, or precision.
- **Designated primary definition site:** Chapter 49 — Source Limits and Calibration Limits
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - Source Ceiling ≠ Traceability Ceiling
  - Source Ceiling ≠ Relevance Floor
  - model precision ≠ source precision

### `calibration`

- **German working rendering:** Kalibrierung
- **Status:** STRATA canonical
- **Short definition:** The determination of usable distinctions and thresholds such that comparable cases remain discriminable and counterexamples remain possible.
- **Designated primary definition site:** Chapter 49 — Source Limits and Calibration Limits
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - calibration ≠ universal numerical threshold
  - formal precision ≠ calibration

### `anti-immunization`

- **German working rendering:** Anti-Immunisierung
- **Status:** STRATA canonical
- **Short definition:** The rule that no change of frame, granularity, level, composition, or target function may erase a prior failed claim or shield a new claim from independent failure.
- **Designated primary definition site:** Chapter 50 — Anti-Immunization
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - new transformation ≠ answer to prior objection
  - translation success ≠ theory superiority

## H. Results, Stop, Non-Capture, and Audit

### `canonical output class`

- **German working rendering:** kanonische Output-Klasse
- **Status:** STRATA canonical
- **Short definition:** One of the fixed system-wide result classes to which every local operation-specific result must be mapped.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - system integration in Chapter 53
  - detailed index in Output_Class_Index.md
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - local result label ≠ new canonical class
  - output class ≠ empirical truth status
- **Control note:** The ten canonical classes are listed below under “Canonical output vocabulary”.

### `claim reduction`

- **German working rendering:** Claim-Reduktion
- **Status:** STRATA canonical
- **Short definition:** A required narrowing of the asserted relation, reach, generality, functional scope, component-role load, or dependence strength when the current claim is not admissible but a narrower claim remains supportable.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - sequence in Chapter 51
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - claim reduction ≠ concealment of failure
  - claim reduction ≠ support downgrade
  - claim reduction ≠ resolution-neutral result
  - narrower claim ≠ unchanged original claim
- **Control note:** Methodological concept; corresponding canonical output value: `claim_reduction_required`.

### `stop`

- **German working rendering:** Stop
- **Status:** STRATA canonical
- **Short definition:** A positive methodological result that ends an operation when further transformation is unnecessary, unsupported, untraceable, type-invalid, or anti-immunizing.
- **Designated primary definition site:** Chapter 51 — Stop Conditions
- **Secondary definition/application sites:**
  - canonical output architecture in Chapter 6
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - stop ≠ embarrassment
  - stop ≠ automatic refutation
  - stop ≠ non-capture

### `mandatory stop`

- **German working rendering:** verbindlicher Stop
- **Status:** STRATA canonical
- **Short definition:** A stop required because continuing the current operation would violate relevance, traceability, source, type, context, calibration, or anti-immunization constraints.
- **Designated primary definition site:** Chapter 51 — Stop Conditions
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - mandatory stop ≠ optional stop
  - mandatory stop ≠ failed transformation in every case
- **Control note:** Methodological concept; corresponding canonical output value: `mandatory_stop`.

### `optional stop`

- **German working rendering:** optionaler Stop
- **Status:** STRATA canonical
- **Short definition:** A stop chosen because the current claim is already sufficiently answered and further admissible transformation is not required.
- **Designated primary definition site:** Chapter 51 — Stop Conditions
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - optional stop ≠ prohibition on later work
  - optional stop ≠ mandatory stop

### `re-entry`

- **German working rendering:** Wiedereintritt
- **Status:** STRATA canonical
- **Short definition:** A newly recorded return to a stopped question after new sources, a new claim, a new counterstructure, or a justified recalibration.
- **Designated primary definition site:** Chapter 51 — Stop Conditions
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - re-entry ≠ unrecorded continuation
  - re-entry ≠ retroactive removal of stop

### `failed transformation`

- **German working rendering:** gescheiterte Transformation
- **Status:** STRATA canonical
- **Short definition:** A result in which the declared operation does not satisfy its defining, preservation, source, admissibility, or boundary conditions.
- **Designated primary definition site:** Chapter 6
- **Secondary definition/application sites:**
  - operation-specific failures in Chapters 15, 20, and 30
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - failed transformation ≠ non-capture
  - failed transformation ≠ mandatory stop in every case
- **Control note:** Methodological concept; corresponding canonical output value: `failed_transformation`.

### `Non-Capture`

- **German working rendering:** Nicht-Erfassung
- **Status:** STRATA canonical
- **Short definition:** The reasoned result that the current PMS-STRATA grammar, sources, granularity, composition, calibration, or projection cannot adequately capture all or part of the object.
- **Designated primary definition site:** Chapter 52 — Non-Capture
- **Secondary definition/application sites:**
  - canonical output architecture in Chapter 6
- **Current control sources:**
  - `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`
- **Central non-equivalences:**
  - Non-Capture ≠ failure avoidance
  - Non-Capture ≠ missing information alone
  - Non-Capture ≠ proof of rival superiority
- **Control note:** Methodological concept; corresponding canonical output value: `non_capture`.

### `non-equivalence`

- **German working rendering:** Nicht-Gleichsetzung
- **Status:** STRATA canonical audit concept
- **Short definition:** An explicit audit constraint that denies unmarked identity, category collapse, or authority transfer between distinct terms while permitting declared comparison, relation, analogy, or transformation.
- **Designated primary definition site:** Chapter 8 — Foundational Non-Equivalences
- **Secondary definition/application sites:**
  - consolidated reference in `Non_Equivalence_Index.md`
  - formal handoff to the later Boundary Decision Tree
- **Current control sources:**
  - `05_minified/Chapter_Contracts.md`
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
  - `04_reference/Chapter_8_Preparation_Record.md` as non-theory production control
- **Central non-equivalences:**
  - non-equivalence ≠ non-relation
  - non-equivalence ≠ prohibition of comparison or transformation
  - non-equivalence ≠ empirical counterclaim
  - non-equivalence ≠ semantic incomparability
- **Control note:** The identity denial is symmetric, but audit explanations may remain direction-sensitive because promotion, replacement, reduction, and authority transfer have different failure forms.

### `local audit`

- **German working rendering:** lokales Audit
- **Status:** STRATA canonical
- **Short definition:** A Part-specific check that applies common STRATA duties to PATH, SUB, or RETYPE without redefining the common operation or admissibility architecture.
- **Designated primary definition site:** Chapter 17 — PATH Cases, Countercases, and Local Audit
- **Secondary definition/application sites:**
  - Chapter 28 — SUB local application
  - Chapter 40 — RETYPE local application
- **Current control sources:**
  - `05_minified/Chapter_Contracts.md`
- **Central non-equivalences:**
  - local audit ≠ integrated audit
  - local application ≠ new definition layer

### `Integrated STRATA Admissibility Audit`

- **Status:** STRATA canonical
- **Short definition:** The staged system-wide audit of source entry, operation classification, relevance, traceability, continuity, counterfactual sensitivity, loss, alternatives, source limits, anti-immunization, stop, non-capture, and authority.
- **Designated primary definition site:** Chapter 53 — Integrated STRATA Admissibility Audit
- **Current control sources:**
  - `00_source/PMS-STRATA_Structure.md`
- **Central non-equivalences:**
  - integrated audit ≠ replacement of local audits
  - audit consistency ≠ empirical truth
  - audit ≠ application tribunal

### `formal model boundary`

- **German working rendering:** Grenze des formalen Modells
- **Status:** STRATA canonical
- **Short definition:** The limit that permits formal artifacts to validate structure, declarations, field completeness, type integrity, and allowed outputs but not empirical truth, causality, semantic adequacy, or normative validity.
- **Designated primary definition site:** Chapter 49
- **Secondary definition/application sites:**
  - corpus-level restatement in Chapter 56
- **Current control sources:**
  - `05_minified/PMS_STRATA_Minified_Canonical.md`
- **Central non-equivalences:**
  - machine-readable consistency ≠ truth
  - schema validity ≠ semantic validity
  - decision tree ≠ application authority

## I. Canonical Output Vocabulary

The glossary stabilizes the canonical values only. Exhaustive meanings and mappings remain assigned to `Output_Class_Index.md`.

### Canonical output values

| Machine-readable value | Compact working meaning | Central non-equivalence |
|---|---|---|
| `admissible` | The transformation satisfies the applicable common and operation-specific requirements without a required claim reduction. | admissible ≠ true |
| `admissible_with_bounded_claim` | The transformation is admissible only under an explicitly narrowed scope, context, level, time range, or function. | admissible with bounded claim ≠ admissible but provisional |
| `admissible_but_provisional` | The transformation is admissible under current support but remains source-, calibration-, or rivalry-sensitive. | admissible but provisional ≠ bounded claim |
| `resolution_neutral` | Additional resolution does not change the warranted reconstruction or claim. | resolution neutral ≠ resolution gain |
| `analogy_only` | A useful structural analogy is retained while a valid functional projection is not established. | analogy only ≠ label substitution |
| `partially_admissible` | Only specified parts, stages, or claims of a transformation are admissible. | partial admissibility ≠ whole-operation validation |
| `claim_reduction_required` | The current claim must be weakened before any admissible result can be retained. | claim reduction ≠ unchanged claim |
| `mandatory_stop` | Further continuation of the present operation would be inadmissible. | mandatory stop ≠ optional stop |
| `failed_transformation` | The declared transformation fails its defining or admissibility conditions. | failed transformation ≠ non-capture |
| `non_capture` | The present grammar, sources, or transformation cannot adequately capture the declared object or claim. | non-capture ≠ immunity from criticism |

Full definitions, local-to-canonical mappings, and operation-specific result tables belong in `Output_Class_Index.md`.

## J. PMS Base Operator Vocabulary — Compact Cross-Reference

The following compact entries were initially included to stabilize names and symbols before Block production and remain as a controlled cross-reference during production. Their detailed dependencies, provides-fields, examples, and PMS status belong in `Operator_Index.md`; `PMS.yaml` remains authoritative.

| Symbol and canonical name | Compact PMS Base definition | Default dependencies |
|---|---|---|
| `Δ — Difference` | Minimal structural distinction enabling differentiation. | none |
| `∇ — Impulse` | Directional tension or drive arising from difference. | Δ |
| `□ — Frame` | Contextual structure that constrains and shapes impulses. | Δ, ∇ |
| `Λ — Non-Event` | Structured absence: meaningful failure or delay of an expected occurrence within a frame. | □ |
| `Α — Attractor` | Recurrent pattern or stabilization emerging from repeated structural interaction. | Δ, ∇, □, Λ |
| `Ω — Asymmetry` | Structural imbalance establishing directionality of power, exposure, capacity, or obligation. | Α |
| `Θ — Temporality` | Temporal structuring that enables trajectories, commitments, development, and longer-form self-relation. | Ω, Α |
| `Φ — Recontextualization` | Transformation through placing an existing structure into a new frame. | Θ, Ω, □ |
| `Χ — Distance` | Reflective withdrawal that attenuates immediate impulses and patterns. | Φ, Θ, □ |
| `Σ — Integration` | Synthesis of disparate or conflicting elements into a more coherent whole. | Χ, Φ |
| `Ψ — Self-Binding` | Formation of self-relation through commitment to integrated structures across time. | Σ, Θ, Χ |

Operator control rules:

```text
operator type ≠ operator occurrence
operator occurrence ≠ composite structure
operator weighting ≠ operator replacement
contextual operator-like function ≠ new PMS primitive
```

---

## K. Historical Pre-Block Terminology Gate

The initial pre-Block terminology gate was passed before Foundations production. Its controls remain binding as a historical baseline, and Chapter-0-owned terms now route to the provisionally re-locked canonical prose only if all of the following remain true:

- every listed term has one designated primary definition site;
- no entry silently introduces a fourth STRATA operation;
- no entry decomposes or revises a Δ–Ψ operator type;
- `frame`, `granularity`, `relative level`, and `transformation context` remain distinct;
- `origin type` and `target function` remain distinct;
- sequence, path, trajectory, and path dependence remain distinct;
- projection, analogy, label substitution, and type jump remain distinct;
- missing information remains distinct from non-event;
- output vocabulary contains exactly the ten canonical classes;
- Stop, failure, claim reduction, and Non-Capture remain available;
- no definition creates person typing, diagnostic use, moral ranking, or authority inheritance;
- all later changes are synchronized through the chapter cycle and frozen only after Cases, Conclusion, Front Matter, and Appendices.

**Historical gate status:** `passed`  
**Current synchronization status:** `chapter_3_wp2_synchronized`

**Next reference artifact:** `04_reference/Operator_Index.md`

---

## Chapter 2 WP1–WP3 Handoff — Historical Pre-Lock Record

During Chapter 2 production, WP1–WP3 fixed the coordinate, scope, comparison, and minimal-declaration relations below before the integrated WP4 lock:

```text
Frame operator type
≠ analytical frame coordinate

granularity
≠ resolution-test result

relative level
≠ ontological layer

source scope
≠ source basis
≠ source ceiling

claim scope
≠ claim boundary
≠ claim ceiling
```

The conceptual coordinate slots `source_granularity`, `target_granularity`, `source_level`, and `target_level` map to the existing nested Shared Transformation Record paths under `/source/*` and `/target/*`. They are not new machine fields. Canonical Sections 2.1–2.14 are available at [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level); integrated synchronization and the Chapter 2 provisional lock are complete. This historical subsection records the pre-lock handoff only.

### Chapter 2 WP3 comparison terms

#### `coordinate change`

- **Short definition:** A declared material change in frame, granularity, relative relation, or scope that creates a new testable claim without by itself identifying a STRATA operation.
- **Primary definition site:** Chapter 2, Sections 2.9–2.14.
- **Non-equivalences:** coordinate change ≠ operation identity; new coordinate claim ≠ erasure of prior failure.

#### `granularity relation`

- **Short definition:** The declared basis on which two resolutions are compared, such as finer segmentation, coarser aggregation, temporal expansion, relational enrichment, or another bounded distinction rule.
- **Primary definition site:** Chapter 2, Sections 2.9 and 2.14.
- **Non-equivalences:** granularity relation ≠ truth rank; finer ≠ deeper reality.

#### `multiple-valid-granularity rule`

- **Short definition:** More than one source-supported granularity may be locally valid for the same reference object or claim family without automatic ranking, mutual reducibility, or total integration.
- **Primary definition site:** Chapter 2, Section 2.12.
- **Non-equivalences:** plurality ≠ equal usefulness for every claim; plurality ≠ contradiction neutralization.

#### `granularity conflict`

- **Short definition:** A comparison pressure in which reconstructions with different distinction sets appear to support incompatible claims and must be tested for genuine comparability and substantive contradiction.
- **Primary definition site:** Chapter 2, Section 2.13.
- **Non-equivalences:** mismatch ≠ contradiction automatically; mismatch ≠ contradiction dissolved automatically.

#### `Minimal Level Declaration`

- **Short definition:** A prose-bound conceptual declaration of source and target coordinates, scopes, declared changes, open operation identity, and loss or uncertainty before operation-specific testing.
- **Primary definition site:** Chapter 2, Section 2.14.
- **Non-equivalences:** Minimal Level Declaration ≠ Shared Transformation Record; declaration completeness ≠ support; conceptual slot ≠ new machine field.

---

## Chapter 2 Provisional-Lock Terminology Consolidation

The following Chapter 2 terms are now provisionally locked at [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level):

| Term | Locked short definition | Required non-equivalence |
| --- | --- | --- |
| analytical frame | declared boundary governing relevance and inside/outside for a bounded reconstruction | analytical frame ≠ `Frame` operator type ≠ transformation context |
| granularity | declared distinction set and resolution used to reconstruct and test a reference object | finer granularity ≠ deeper truth or greater authority |
| relative level | position of an object relative to a comparator under a declared relation and purpose | relative level ≠ ontological layer or intrinsic rank |
| temporal scope | declared time range and open temporal edges included in a claim | temporal scope ≠ sequence, path, trajectory, or later non-event |
| source scope | declared range of accessible source structures, inference, gaps, and uncertainty | source scope ≠ source basis or source ceiling |
| claim scope | object, predicate, reach, and exclusions of the current claim | claim scope ≠ claim boundary, claim ceiling, or validity scope |
| granularity conflict | comparison pressure arising when claims at different resolutions may be non-comparable, partially tense, or substantively contradictory | mismatch ≠ contradiction automatically; mismatch ≠ neutralization automatically |
| Minimal Level Declaration | smallest conceptual source/target coordinate declaration needed before operation classification | declaration ≠ Shared Transformation Record or operation proof |

These entries summarize the canonical chapter and may not independently expand it.

---

## Chapter 3 Provisionally Locked Terminology

Canonical Sections 3.1–3.13 now control the full Chapter 3 temporal object chain, historical-property burdens, supported alternatives, and the Minimal Temporal Object Chain. The Preparation Record supplies execution history only.

| Term | Canonical short definition | Required non-equivalence |
| --- | --- | --- |
| state | formal or compressed shorthand for a temporally located description | state ≠ complete praxeological configuration |
| configuration | bounded temporally located reconstruction of relevant operator relations and praxis conditions | configuration ≠ static ontology or total time-slice description |
| event | temporally specified realized relevant change within a declared chain | event ≠ transition or causal atom |
| non-event | source-supported structured non-realization under an expectation frame and bounded realization condition | missing information ≠ non-event |
| transition | bounded relation connecting configurations through supported realized/non-realized structure and changed praxis conditions | endpoint difference ≠ transition |
| sequence | selected ordered analytical series with a declared ordering basis | chronology ≠ sequence automatically; sequence ≠ path |
| path | selectively reconstructed actually traversed chain of relevant configurations and transitions | path ≠ chronology or trajectory |
| trajectory | path with source-supported sedimented historical load affecting later meaning, cost, or continuation possibility | trajectory ≠ teleology or path dependence |
| path dependence | bounded property claim that present structure materially depends on prior order/path | path dependence ≠ object class or Θ alone |
| sedimentation | accumulated historical load that remains structurally relevant | duration ≠ sedimentation |
| irreversibility | frame- and claim-bound failure of restoration, neutralization, or cost-equivalent return | irreversibility ≠ metaphysical absolute impossibility |
| unrealized alternative | source-supported available, delayed, blocked, rejected, or later unavailable continuation | imaginable option ≠ historically available alternative |

The canonical burden chain is:

```text
configuration
→ transition
→ sequence
→ path
→ trajectory

path dependence = separately tested property
```

Every arrow increases burden. No arrow is automatic.

## Chapter 3 WP2 Terminology Consolidation

Canonical return: [`Chapter 3 Sections 3.1–3.13`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Term | WP2 short definition | Required non-equivalence |
| --- | --- | --- |
| chronology | dated or before/after record that may remain analytically unselected | chronology ≠ sequence automatically |
| sequence | selected temporally ordered analytical series with declared units and ordering basis | sequence ≠ path, trajectory, or causal chain |
| path | selectively reconstructed actually traversed chain of relevant configurations and transitions under declared selection, trace, branch/omission, and loss | path ≠ complete chronology, causal history, trajectory, or completed `COMPOSE` procedure |
| trajectory | path whose source-supported historical carry-over changes later meaning, cost, accessibility, role, asymmetry, binding, residue, or continuation | trajectory ≠ duration, teleology, or path dependence automatically |
| actual traversal | source-supported realization of the selected chain rather than merely conceivable or retrospectively plausible routing | actual traversal ≠ narrative plausibility |
| directionality | bounded patterned continuation pressure visible in a trajectory | directionality ≠ purpose, destiny, or inevitability |

These Reference formulations summarize the canonical chapter. They do not independently define PATH procedures or historical-property tests.

## Chapter 3 WP3 Terminology Consolidation

Canonical return: [`Chapter 3 Sections 3.9–3.13`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Term | WP3 short definition | Required non-equivalence |
| --- | --- | --- |
| path dependence | bounded property claim requiring current-conditions insufficiency, prior-order or branch relevance, supported counterfactual sensitivity, and traceable carry-over | path dependence ≠ trajectory, determinism, teleology, or `Θ` |
| sedimentation | accumulated or persistent source-supported historical load that changes a declared later praxis relation | sedimentation ≠ duration, archival survival, remembrance, or operator formula |
| bounded irreversibility | failure of restoration, neutralization, or cost-equivalent return under a declared frame, claim, relation, and restoration criterion | bounded irreversibility ≠ metaphysical impossibility |
| unrealized alternative | source-supported historically available or conditionally available continuation not traversed | unrealized alternative ≠ analyst-imagined counterfactual |
| Minimal Temporal Object Chain | burden progression from configuration through trajectory, with path dependence separately tested and downward reduction preserved | chain ≠ automatic derivation, causal history, `COMPOSE`, or Shared Transformation Record |

These entries summarize canonical prose and may not independently expand it.

---

## Chapter 3 Provisional-Lock Synchronization

The temporal-object entries now route to the provisionally locked canonical [`Chapter 3`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory). The controlling chain is `configuration → transition → sequence → path → trajectory`; path dependence remains a separately tested property. Reference entries may summarize and route these burdens but may not redefine them, infer them from timestamps, or convert them into closed machine categories.

---

## Chapter 4 Preparation Terminology Handoff

The following entries are production-controlled pending canonical Chapter 4 prose. Existing minified signatures remain binding.

### Operation identity

**Short definition:** The classified source–target transformation relation of one declared occurrence: `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

**Not equivalent to:** coordinate direction, temporal-object label, procedure step, audit act, output class, or chain.

### Operation occurrence

**Short definition:** One bounded, uniquely identified application claim carrying exactly one operation type, source/target relation, justification, preservation duty, loss account, and local result.

**Not equivalent to:** abstract operation type, chain, composite, or transformation record as a mere completed form.

### Operation chain

**Short definition:** An ordered sequence of separately declared operation occurrences.

**Not equivalent to:** a fourth operation, one collapsed multi-operation occurrence, or inherited validity.

### Source object

**Short definition:** The typed reference object or source-object family on which one operation occurrence acts.

**Not equivalent to:** target object, target function, source basis, or source scope.

### Target object

**Short definition:** The analytical object formed or reconstructed as the object-side result of `COMPOSE` or `DECOMPOSE`.

**Not equivalent to:** contextual target function.

### Target function

**Short definition:** A bounded contextual function assigned through `PROJECT_AS` while source reference and origin type remain preserved.

**Not equivalent to:** target object, new origin type, new primitive, analogy, or label.

### Non-invertibility

**Short definition:** The operation-specific fact that selection, compression, reconstruction, context, and type preservation prevent a reverse expression from recovering an identical untouched source relation.

**Not equivalent to:** total loss, metaphysical irreversibility, or exemption from continuity duties.

### Minimal Operation Declaration

**Short definition:** A compact conceptual declaration of operation occurrence, source, target, context, justification, preservation, loss, alternatives, uncertainty, and result boundary mapped to existing Shared Record paths.

**Not equivalent to:** a second schema, a completed Shared Transformation Record, or proof of admissibility.

Primary future definition site: Chapter 4. Production-control route: `04_reference/Chapter_4_Preparation_Record.md`.

---

## Chapter 4 WP1 Canonical Terminology Synchronization

The following terms now return to canonical Sections 4.1–4.4:

- `STRATA operation` — exactly one of `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`;
- `operation occurrence` — one declared use of exactly one operation kind;
- `COMPOSE` — formation of a new composite analytical object;
- `DECOMPOSE` — finer relational reconstruction of the same compressed reference object;
- `PROJECT_AS` — bounded contextual function with source reference and origin type preserved.

Canonical return: [`Chapter 4 WP1`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

`operation chain`, `non-invertibility`, and the complete `Minimal Operation Declaration` remain controlled by the Preparation Record and minified signatures until Sections 4.5–4.10 are drafted.

---

## Chapter 4 WP2 Canonical Terminology Synchronization

- `transformation direction` — the declared source–target relation of one operation occurrence; not ontological, temporal, claim, or authority direction;
- `operation / level relation` — the separately declared relation between an operation occurrence and its frame, granularity, relative level, and scopes;
- `operation chain` — an ordered sequence of separately identified exclusive operation occurrences;
- `chain handoff` — a declared claim that a prior target, reconstruction, function, or occurrence is available as the next link’s source;
- `link-local result` — the retained canonical Output Class of one chain occurrence.

Canonical return: [`Chapter 4 WP2`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

```text
operation chain
≠ compound operation
≠ inherited admissibility
```

---

## Chapter 4 WP3 Terminology Synchronization

### Non-invertibility

A bounded property of STRATA operations according to which a reverse-looking later occurrence does not restore an untouched source relation and must be declared and tested as a new occurrence.

```text
non-invertibility
≠ total loss
≠ metaphysical irreversibility
≠ permission to ignore preservation
```

### Operation confusion

A category error in which chronology, aggregation, description, a competing formation, coordinate change, recontextualization, analogy, renaming, or a collapsed chain is presented as a canonical operation without its source–target signature.

### Minimal Operation Declaration

The smallest prose-bound declaration that makes one exclusive operation occurrence testable through source, target, context, justification, preservation, loss, alternatives, uncertainty, and local-result boundaries. It maps to the Shared Transformation Record and is not a second schema.

Canonical return: [`Chapter 4 §4.8–4.10`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

---

## Chapter 4 Provisional-Lock Synchronization

The operation entries now return to the provisionally locked canonical [`Chapter 4`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as). `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS` remain the exact and closed core inventory; operation type, occurrence, result, and chain remain distinct; the Minimal Operation Declaration is prose-bound and maps to existing Shared Record paths.

---

## Chapter 5 Preparation Terminology Cards

These cards are production-control previews. Canonical definitions remain pending Chapter 5 drafting.

### Origin Type

The declared analytical type under which a source object is identified in its source reconstruction before a later target function is assigned or tested.

```text
origin type
≠ operator type automatically
≠ target function
≠ permanent essence
```

### Target Function

A bounded, relational role performed by an origin-typed source object within a declared target context, validity scope, and analytical purpose.

```text
target function
≠ target object type
≠ new primitive
≠ permanent identity
```

### Target Context

The target-side scene, relation, configuration, or analytical use within which a target function is proposed.

### Transformation Context

The declared relational envelope governing an operation’s source–target relation, purpose, relevant sources and coordinates, target context, temporal reach, validity scope, Claim Ceiling, uncertainty, and revision conditions.

```text
frame
≠ target context
≠ transformation context
```

### Reference Continuity

The degree to which the relevant source or historical object remains identifiable through the tested transformation relation, with constitutive relations and reference boundaries preserved or explicitly revised.

```text
same name
≠ reference continuity
```

### Type Integrity

The requirement that source typing, target-object typing, and target function remain visible and non-substitutable, and that any revision be explicit rather than retrospective replacement.

### Functional Continuity

The source-sensitive relation by which a proposed target function is carried by specific load-bearing source features and changes when those features materially change.

### Temporal Continuity

Preservation of the historically relevant order, duration, heterogeneity, and carried load required by the target claim, without an exhaustive-detail requirement.

### Contextual Boundedness

The restriction of a target function to its declared target context, temporal reach, relative level, analytical purpose, validity scope, exclusions, and re-entry conditions.

These terms remain separate even where one local case satisfies all of them.

---

## Chapter 5 WP1 Canonical Terminology Synchronization

The following entries now return to canonical Sections 5.1–5.3:

### Origin Type

The declared source-side analytical typing under which an identified source object enters a transformation.

```text
origin type
≠ operator type automatically
≠ target function
≠ permanent essence
```

### Target Function

A bounded, source-carried, defeasible role performed by an origin-typed source object in a declared target context for a specified purpose and validity scope.

```text
target function
≠ target object type
≠ new primitive
≠ permanent identity
```

### Target Context

The target-side scene, relation, configuration, or analytical use within which a target function is proposed.

### Transformation Context

The wider relational envelope governing the source–operation–target claim, including purpose, reference relation, coordinates, relevant sources, target context, temporal reach, validity scope, Claim Ceiling, uncertainty, and revision conditions.

```text
frame
≠ target context
≠ transformation context
```

Canonical return: [`Chapter 5 WP1`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP2 Canonical Continuity Synchronization

### Reference Identity

The claim that identifies which bounded historical or analytical object is under examination.

### Reference Continuity

The operation-appropriate preservation of an identifiable source or historical object, its constitutive bridge, and its reference boundary through a tested transformation relation.

```text
same name
≠ same reference object
```

### Type Integrity

The requirement that source typing, target-object typing, and target function remain visible, separately declared, and free from hidden substitution.

### Type Continuity

Warranted preservation or explicit source-supported revision of analytical typing across a transformation relation.

```text
explicit warranted type revision
≠ retrospective type replacement
```

### Functional Continuity

The source-sensitive relation by which a precise target function is carried by specific load-bearing source features and changes when those features materially change.

```text
functional continuity
≠ contextual usefulness
≠ metaphorical association
```

Canonical return: [`Chapter 5 §§5.4–5.6`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP3 Temporal and Contextual Synchronization

### Temporal Continuity

Preservation of the historically relevant order, carry-over, and transformation history required for a later object or function claim to remain traceable to its source, without requiring exhaustive chronology.

### Contextual Boundedness

Restriction of a target function and validity claim to the declared target context, purpose, temporal reach, scope, exclusions, and revision conditions.

### Minimal Projection Form

The smallest prose-bound declaration that makes a `PROJECT_AS` candidate inspectable for origin-type preservation, bounded target function, four continuity findings, context, loss, alternatives, governance, and local result.

```text
Minimal Projection Form
≠ second record schema
≠ semantic continuity proof
≠ authority
```

Canonical return: [`Chapter 5 §§5.7–5.9`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

---

## Chapter 5 Continuity Terminology Synchronization

The canonical definitions of `origin type`, `target function`, `target context`, `transformation context`, `reference continuity`, `Type Integrity`, `type continuity`, `functional continuity`, `temporal continuity`, `contextual boundedness`, and `Minimal Projection Form` now reside in [`Chapter 5`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

Reference use must preserve:

```text
origin type ≠ target function
frame ≠ target context ≠ transformation context
reference continuity ≠ type integrity ≠ functional continuity ≠ temporal continuity
local function ≠ inherited validity or authority
```

## Chapter 6 Preparation Terminology Handoff

### Praxeological Relevance Floor

The lower relational boundary below which an added distinction or transformation creates no changed warranted reconstruction of praxis-relevant structure.

### PraxisPurchase

The claim-specific difference made by a distinction or transformation to warranted reconstruction, including action corridors, costs, exposure, roles, expectations, temporal structure, alternatives, scope, failure, or Stop conditions. Purchase does not require immediate actionability.

### Praxeological Traceability Ceiling

The upper relational boundary above which a transformation result no longer carries reconstructible structural load from its declared source objects.

### TraceableLoad

The preserved and inspectable dependency of a result on identifiable source objects, load-bearing features, relevant relations and temporality, declared selection and loss, source-change sensitivity, and bounded claim reach.

### Counterfactual Sensitivity

A bounded source-dependency test asking whether a relevant change in declared load-bearing source structure would alter the transformation result. It is not causal proof.

### STRATA Admissibility Band

The relational, non-numeric, non-compensatory operating range above distinction without praxeological purchase and below abstraction without traceable load.

### No Universal STRATA Scale

The rule that STRATA has no universal smallest relevant element, finest admissible granularity, largest legitimate composite, or fixed threshold for temporal or functional categories.

Production control: [`Chapter 6 Preparation Record`](Chapter_6_Preparation_Record.md).

---

## Chapter 6 WP1 Canonical Terminology Synchronization

### Operating Range

The relational interval in which a delimited transformation claim must both add a warranted praxis-relevant difference and remain reconstructibly source-carried. WP1 canonically defines its lower-bound side.

### Praxeological Relevance Floor

The lower relational boundary below which an added distinction or transformation creates no changed warranted reconstruction for the tested claim.

### PraxisPurchase

The claim-specific change made by a distinction or transformation to warranted reconstruction of praxis-relevant structure. Purchase may consist in revision, narrowing, countercase visibility, loss disclosure, or Stop; it does not require actionability.

### Changed-Reconstruction Test

The lower-bound test asking which warranted reconstruction must be stated differently because of an added distinction, and requiring the prior claim, revised claim, affected praxis dimension, and source-supported difference to be explicit.

### Praxis-Relevant Dimension

A claim-relevant aspect of reconstructed praxis—such as action corridors, costs, exposure, roles, asymmetries, commitments, expectations, temporal order, path structure, target function, scope, loss, or Stop conditions—whose warranted change may supply PraxisPurchase.

### Distinction without Praxeological Purchase

Additional resolution or description that changes no warranted reconstruction for the tested claim.

### Resolution Gain

A supported lower-bound finding in which an added distinction changes at least one warranted reconstruction.

### Valid Resolution Neutrality

A supported comparison showing that a finer distinction is not load-bearing and that the coarser reconstruction remains sufficient. Its canonical candidate may be `resolution_neutral` only after full applicable checks.

Canonical return: [`Chapter 6 WP1`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP2 Canonical Terminology Synchronization

### Praxeological Traceability Ceiling

The upper relational boundary above which a transformation result no longer carries reconstructible structural load from its declared source objects.

### TraceableLoad

The preserved and inspectable dependency of a result on identifiable source objects, constitutive features, relevant relations and temporality, disclosed selection and loss, source-change sensitivity, and bounded claim reach.

### Structural Mapping

The explicit correspondence between source structures and target elements or functions. Mapping is necessary for TraceableLoad but does not alone establish source-result dependency.

### Source-Result Dependency

The bounded relation under which a material change in a declared load-bearing source structure requires a material change in the tested result.

### Abstraction without Traceable Load

A composition, fragmentation, or projection whose target remains rhetorically or semantically stable while its declared source load can materially change without consequence.

### Counterfactual Sensitivity Finding

One of the local dependency findings `sensitive`, `partially sensitive`, `insensitive`, `underdetermined`, or `not testable with available sources`. These are not canonical Output Classes and do not prove causality.

Canonical return: [`Chapter 6 WP2`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP3 Canonical Terminology Synchronization

### Transformation Admissibility Test

The conjunctive, claim-relative assessment requiring PraxisPurchase, TraceableLoad, Type Integrity, and Contextual Boundedness, together with all other applicable continuity, loss, alternative, ceiling, Stop, Non-Capture, and authority duties.

### Non-Compensation

The rule that a successful or strong condition cannot cancel failure of another load-bearing condition. STRATA admissibility is not a weighted score.

### Admissibility Band

The relational operating range bounded below by praxeological purchase and above by reconstructible source load. It assesses a declared transformation occurrence, context, claim, and source basis rather than ranking objects or levels.

### Within-Band Transformation

A discriminating and reconstructively anchored transformation that changes a warranted reconstruction, carries traceable source load, preserves required type commitments, and remains contextually bounded.

### No Universal STRATA Scale

The rule that STRATA supplies no universal smallest relevant element, finest admissible granularity, largest legitimate composite, fixed projection threshold, or compensatory numeric score. Bounded local comparisons remain possible.

Canonical return: [`Chapter 6 WP3`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 Provisional-Lock Terminology Status

The Chapter 6 definitions of **Praxeological Relevance Floor**, **PraxisPurchase**, **Praxeological Traceability Ceiling**, **TraceableLoad**, **Counterfactual Sensitivity**, **Admissibility Band**, and **No Universal STRATA Scale** are provisionally locked at [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

This glossary remains a navigation layer. It does not convert the compact gate into a score, define a universal scale, select Output Classes, prove causality, or replace the canonical prose.

---

## Chapter 7 Preparation Terminology Synchronization

The Chapter 7 Preparation Gate controls the following record terms before canonical Sections 7.1–7.10 are drafted:

| Term | Preparation definition | Primary future site | Central non-equivalence |
| --- | --- | --- | --- |
| Shared Transformation Record | common declaration and audit envelope used by all three STRATA operations and their chains | Chapter 7 | record ≠ transformation |
| declaration completeness | presence and explicit treatment of every applicable shared duty, including known gaps and routing state | Chapter 7 | declaration completeness ≠ epistemic completeness |
| epistemic completeness | degree to which available sources support all distinctions required for the tested claim | Chapter 7 boundary; Evidence Map | epistemic incompleteness ≠ analyst omission |
| serialization companion | metadata, claim, chain, relation, extension, result, or formal-diagnostic structure needed to serialize the shared duties | Chapter 7; Appendix C | serialization companion ≠ new primitive |
| support status | separate axis describing how the tested claim is currently supported | Chapter 7 | support status ≠ Output Class |
| resolution-test result | separate axis for resolution gain, neutrality, drift, escape, or non-applicability | Chapter 7 | resolution result ≠ claim disposition |
| claim disposition | maintained, withdrawn, failed, or superseded-without-erasure state of a delimited claim | Chapter 7 | failed disposition ≠ failed_transformation |
| capture statement | claim-relative statement of what is captured and whether a capture limit is present | Chapter 7 | capture limit ≠ automatic non_capture |
| routing state | `routed` or `formal_diagnostic` process state | Chapter 7 | formal diagnostic ≠ canonical Output Class |
| local extension | namespaced, sourced, bounded additional declaration that leaves all shared duties intact | Chapter 7 | extension ≠ bypass |
| chain declaration | ordered relation among separately recorded operation occurrences and a distinct chain-level claim | Chapter 7 | chain ≠ multi-kind occurrence |
| non-translation | explicit alternative finding that the tested movement is not responsibly representable as a STRATA operation | Chapter 7; later RETYPE boundary | non-translation ≠ rival transformation |

These are controlled preparation definitions only. The existing JSON schema remains an implementation candidate and does not become the canonical definition source.

---

## Chapter 7 WP1 Terminology Synchronization

| Term | Canonical WP1 meaning | Primary site | Central non-equivalence |
| --- | --- | --- | --- |
| Shared Transformation Record | inspectable declaration of one delimited transformation claim and its common duty families | [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record) | record ≠ transformation |
| declaration completeness | explicit treatment of every applicable record duty, including gaps and empty categories | Chapter 7 §7.1 | declaration completeness ≠ epistemic completeness |
| epistemic completeness | degree to which available sources support all distinctions required by the claim | Chapter 7 §7.1 | epistemic incompleteness ≠ analyst omission |
| serialization companion | identity, metadata, claim, relation, chain, extension, result, or diagnostic carrier needed for implementation | Chapter 7 §7.1 | companion ≠ primitive |
| Source Declaration | source-side reference, typing, coordinates, scopes, basis, constitutive trace, gaps, and ceiling | Chapter 7 §7.2 | Source Basis ≠ Constitutive Source Trace |
| Operation Declaration | one occurrence identity, exactly one kind, and the testable rationale for its source–target signature | Chapter 7 §7.3 | justification ≠ warrant |
| Target Declaration | target reference, typing, contextual function, coordinates, scope, and function-origin relation | Chapter 7 §7.4 | target object ≠ target function |

WP1 does not yet canonically define Admissibility, Loss, Alternatives, Governance, status/result axes, chains, or extensions; those remain assigned to Sections 7.5–7.10.

---

## Chapter 7 WP2 Terminology Synchronization

| Term | Canonical WP2 meaning | Primary site | Central non-equivalence |
| --- | --- | --- | --- |
| Admissibility Declaration | inspectable record of upstream audit findings and their routing basis | [Chapter 7 §7.5](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record) | recorded finding ≠ automated adjudication |
| Loss Declaration | closed five-category account of preserved, compressed, excluded, uncertain, and irrecoverable structure | Chapter 7 §7.6 | empty category ≠ omitted category |
| Alternative Transformations | rival operations, no transformation, non-translation, and unresolved candidates kept separately testable | Chapter 7 §7.7 | rival transformation ≠ non-translation |
| Governance Declaration | claim, authority, Stop, Non-Capture, prohibited-inference, and external-warrant limits | Chapter 7 §7.8 | governance record ≠ authority grant |
| explicit empty loss category | no item currently asserted in that category within scope | Chapter 7 §7.6 | empty ≠ universal absence |
| sibling record | separate occurrence record for a materially distinct rival claim | Chapter 7 §7.7 | sibling records ≠ collapsed multi-kind record |
| external-warrant pointer | reference to authority or validity supplied outside STRATA | Chapter 7 §7.8 | pointer ≠ inherited authority |

---

## Chapter 7 WP3 Terminology Synchronization

| Term | Canonical WP3 meaning | Primary site | Central non-equivalence |
| --- | --- | --- | --- |
| support status | present source-support relation of a delimited tested claim | [Chapter 7 §7.9](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record) | support status ≠ Output Class |
| resolution-test result | effect of a tested resolution change on the claim | Chapter 7 §7.9 | test result ≠ canonical route |
| claim disposition | maintained, withdrawn, failed, or superseded-without-erasure claim history | Chapter 7 §7.9 | failed disposition ≠ failed transformation automatically |
| capture statement | claim-relative account of captured and uncaptured structure | Chapter 7 §7.9 | capture limit ≠ automatic non-capture |
| formal diagnostic | non-routed record state preserving unresolved formal prerequisites | Chapter 7 §7.9 | formal diagnostic ≠ Output Class |
| chain declaration | ordered cross-record relation preserving occurrence-level results and losses | Chapter 7 §7.10 | chain ≠ operation |
| local extension | namespaced bounded addition that cannot replace shared duties | Chapter 7 §7.10 | extension ≠ override |

---

## Chapter 7 WP4 Provisional-Lock Synchronization

Chapter 7 is provisionally locked after integrated ownership, redundancy, status, case-duty, prose-to-schema, link, schema, fingerprint, package, and roundtrip audit. The Shared Transformation Record records transformation claims without becoming the transformation, a truth proof, or an authority source. The existing record schema supplies lower-authority structural carriers; its Chapter-7 handoff annotation does not redefine canonical prose. The sixteen Chapter-7 case identifiers remain later production duties rather than completed evidence. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 8 Preparation Terminology Synchronization

The Chapter 8 Preparation Gate confirms that `non-equivalence` is the audit concept owned by Chapter 8 and that the terms on either side of every pair retain their primary definition sites in Chapters 0–7 or PMS Base.

```text
Chapter 8 collection site
≠ second definition layer
```

The controlled minimum contains thirteen foundational pairs. Local wording variants remain variants under the applicable pair and do not become new canonical terms. Production control: [`Chapter 8 Preparation Record`](Chapter_8_Preparation_Record.md).

---

## Chapter 8 WP1 Terminology Synchronization

Canonical Chapter-8 audit terms now route as follows:

- `non-equivalence` → [Chapter 8 introduction](../01_blocks/01_foundations.md#chapter-8-foundational-non-equivalences);
- `finer granularity ≠ higher truth` → [Section 8.1](../01_blocks/01_foundations.md#81-finer-granularity-is-not-higher-truth);
- `relative level ≠ ontological layer` → [Section 8.2](../01_blocks/01_foundations.md#82-relative-level-is-not-ontological-layer);
- `composition ≠ lossless addition` → [Section 8.3](../01_blocks/01_foundations.md#83-composition-is-not-lossless-addition);
- `decomposition ≠ discovery of final constituents` → [Section 8.4](../01_blocks/01_foundations.md#84-decomposition-is-not-discovery-of-final-constituents).

The terms on each side retain their definition owners in Chapters 0–7 or PMS Base.

---

## Chapter 8 WP2 Terminology Synchronization

Canonical WP2 audit terms now route as follows:

- `path ≠ sequence` → [Section 8.5](../01_blocks/01_foundations.md#85-path-is-not-sequence);
- `path ≠ trajectory` → [Section 8.6](../01_blocks/01_foundations.md#86-path-is-not-trajectory);
- `trajectory ≠ path dependence` → [Section 8.7](../01_blocks/01_foundations.md#87-trajectory-is-not-path-dependence);
- `origin type ≠ target function` → [Section 8.8](../01_blocks/01_foundations.md#88-origin-type-is-not-target-function);
- `projection ≠ operator identity` → [Section 8.9](../01_blocks/01_foundations.md#89-projection-is-not-operator-identity);
- `operator weighting ≠ operator replacement` → [Section 8.10](../01_blocks/01_foundations.md#810-operator-weighting-is-not-operator-replacement).

The terms on each side retain their definition owners in Chapters 0–7, PMS Base, or the later designated procedure chapter.

---

## Chapter 8 WP3 Terminology Synchronization

Canonical WP3 audit terms now route as follows:

- `structural analogy ≠ valid projection` → [Section 8.11](../01_blocks/01_foundations.md#811-structural-analogy-is-not-valid-projection);
- `recursion ≠ completeness` → [Section 8.12](../01_blocks/01_foundations.md#812-recursion-is-not-completeness);
- `legibility ≠ authority` → [Section 8.13](../01_blocks/01_foundations.md#813-legibility-is-not-authority);
- `integrated thirteen-pair comparison matrix` → [Section 8.13](../01_blocks/01_foundations.md#integrated-thirteen-pair-comparison-matrix);
- `integrated catalogue use` → [Section 8.13](../01_blocks/01_foundations.md#integrated-catalogue-use).

Analogy remains a declared comparison relation, recursion remains repeated testable transformation availability, and legibility remains inspectability. None becomes a new operation, completeness criterion, truth status, or authority source.

---

## Chapter 8 WP4 Terminology Lock

The foundational non-equivalence catalogue is provisionally locked at thirteen pairs. Chapter 8 owns their audit wording; Chapters 0–7 and PMS Base retain ownership of the paired terms.

```text
Foundations completion
≠ final freeze
≠ exhaustive capture
≠ higher authority
```

`Foundations provisional lock` denotes a production status: the foundational object, coordinate, temporal, operation, continuity, admissibility, record, and non-equivalence architecture is sufficient for PATH entry while remaining reopenable under documented conditions.

---

## Chapter 9 Preparation Terminology Handoff

The entries below are controlled drafting summaries. Chapter 3 retains primary ownership of the underlying temporal object categories. Chapter 9 is the designated PATH operational site for the listed transition burdens.

| Term | Controlled short definition | Designated primary site | Central non-equivalence |
| --- | --- | --- | --- |
| temporal position | claim-relative placement as instant, interval, relative order, disputed date, open edge, or declared retrospective periodization | Chapter 9 §9.3 | temporal position ≠ timestamp |
| order dependence | bounded property that materially changing the declared order would change the warranted praxis reconstruction | Chapter 9 §9.4 | order dependence ≠ succession or path dependence |
| praxeologically relevant duration | interval length or persistence whose difference changes a declared praxis relation | Chapter 9 §9.5 | duration ≠ metric time alone |
| delay as transition structure | deferred temporal relation between configurations that changes costs, expectations, bindings, or alternatives | Chapter 9 §9.6 | delay structure ≠ framed non-event automatically |
| persistence | continued structural relevance across an interval despite changing events or configurations | Chapter 9 §9.7 | persistence ≠ stasis, duration, or sedimentation |
| bounded irreversibility | supported failure of restoration, neutralization, or cost-equivalent return under declared criteria | Chapter 9 §9.8, returning to Chapter 3 | irreversibility ≠ metaphysical impossibility |
| temporal recontextualization | later event- or frame-relative change in the legibility of prior structure while its occurrence and sequence remain preserved | Chapter 9 §9.9 | recontextualization ≠ retroactive erasure, `Φ` identity, or `PROJECT_AS` automatically |
| transition preconditions | conjunctive declaration burdens required before a transition claim can be tested | Chapter 9 §9.10 | declared preconditions ≠ transition truth |
| transition structure | source-supported relation between configurations including order, events/non-events, changed praxis conditions, and residue | Chapter 9 §9.11, returning to Chapter 3 | transition ≠ snapshot difference or STRATA operation |
| transition failure | bounded refusal or reduction of a transition claim while weaker configurations, chronology, uncertainty, and re-entry remain visible | Chapter 9 §9.12 | failed transition ≠ absence of temporal information |

Production control: [`Chapter 9 Preparation Record`](Chapter_9_Preparation_Record.md). Canonical Sections 9.1–9.12 remain pending.

---

## Chapter 9 WP1 Canonical Terminology Handoff

| Term | Canonical WP1 control | Primary location | Non-equivalence |
| --- | --- | --- | --- |
| PATH purpose | reconstruction of temporally ordered praxis structures without automatic operation or target function | [§9.1](../01_blocks/02_part_i_path.md#9-1-purpose-of-path) | PATH ≠ `COMPOSE` ≠ RETYPE |
| `Θ`-supported temporal declaration | object- and claim-specific use of PMS temporal structuring | [§9.2](../01_blocks/02_part_i_path.md#9-2-theta-as-temporal-structuring) | temporal articulation ≠ historical sufficiency |
| temporal position | claim-relative placement as instant, interval, relative/partial order, disputed date, or declared periodization | [§9.3](../01_blocks/02_part_i_path.md#9-3-temporal-position) | temporal position ≠ timestamp |
| partial temporal order | supported set of ordering relations with one or more unresolved internal relations | [§9.3](../01_blocks/02_part_i_path.md#9-3-temporal-position) | partial order ≠ failed chronology |
| order dependence | bounded property that material reorder changes the warranted reconstruction of the tested claim | [§9.4](../01_blocks/02_part_i_path.md#9-4-order-dependence) | order dependence ≠ succession or path dependence |
| narrative order | order used in report, interview, or explanation | [§9.4](../01_blocks/02_part_i_path.md#9-4-order-dependence) | narrative order ≠ historical order |

The earlier Preparation Handoff remains production history. Sections 9.5–9.12 remain pending.

---

## Chapter 9 WP2 Canonical Terminology Handoff

| Term | Canonical control | Primary location | Non-equivalence |
| --- | --- | --- | --- |
| praxeologically relevant duration | interval whose length or continuation changes warranted praxis reconstruction | [§9.5](../01_blocks/02_part_i_path.md#9-5-duration) | duration ≠ metric time alone |
| delay as transition structure | deferred relation changing costs, expectations, bindings, alternatives, or asymmetry | [§9.6](../01_blocks/02_part_i_path.md#9-6-delay) | delay structure ≠ framed non-event |
| delay as framed non-event | warranted expected occurrence unrealized within bounded condition with load | [§9.6](../01_blocks/02_part_i_path.md#9-6-delay) | silence ≠ non-event |
| persistence | continued structural relevance across changing events/configurations | [§9.7](../01_blocks/02_part_i_path.md#9-7-persistence) | persistence ≠ stasis or sedimentation |
| restoration criterion | declared condition for restoration, neutralization, or cost-equivalent return | [§9.8](../01_blocks/02_part_i_path.md#9-8-irreversibility) | formal reversal ≠ full restoration |
| temporal recontextualization | later event/frame changes earlier legibility while historical trace remains | [§9.9](../01_blocks/02_part_i_path.md#9-9-temporal-recontextualization) | relation ≠ `Φ` type ≠ `PROJECT_AS` |

---

## Chapter 9 WP3 Canonical Terminology Handoff

| Term | Canonical control | Primary location | Non-equivalence |
| --- | --- | --- | --- |
| transition preconditions | conjunctive burdens required before a transition claim can be warranted | [§9.10](../01_blocks/02_part_i_path.md#9-10-transition-preconditions) | precondition completeness ≠ transition truth |
| comparison basis | declared dimension under which configurations are comparable | [§9.10](../01_blocks/02_part_i_path.md#9-10-transition-preconditions) | same label ≠ same basis |
| transition candidate | delimited but not yet fully resolved transition claim | [§9.10](../01_blocks/02_part_i_path.md#9-10-transition-preconditions) | candidate ≠ warranted transition |
| warranted transition | bounded transition claim passing applicable local tests | [§9.10](../01_blocks/02_part_i_path.md#9-10-transition-preconditions) | transition ≠ operation or path |
| frame handoff | explicit cross-frame comparability relation with loss and scope | [§9.11](../01_blocks/02_part_i_path.md#9-11-transition-structure) | frame difference ≠ direct transition |
| transition failure | failure of a delimited source-to-target relation with weaker findings preserved | [§9.12](../01_blocks/02_part_i_path.md#9-12-transition-failure) | failure ≠ absence of temporal information |
| warranted transition set | collection of individually delimited transition records available to Chapter 10 | [§9.12](../01_blocks/02_part_i_path.md#9-12-transition-failure) | set ≠ path automatically |


## Chapter 9 Provisional-Lock Terminology Handoff

**warranted transition**  
A frame-bound and source-supported relation between reconstructed configurations whose temporal order, constitutive events and non-events, changed and retained praxis conditions, loss, and unresolved residue support the delimited transition claim. It is not a path, causal mechanism, or operation occurrence automatically.

**transition gate**  
The conjunctive and non-compensatory Chapter 9 burden covering configurations, comparison basis, temporal relation, constitutive change, events/non-events, frame, source trace, intermediate structures, changed and retained fields, praxis difference, and claim ceilings. Field completion alone does not establish passage.

**Chapter 10 transition handoff**  
A set of individually delimited transition records supplied for later Path testing. It does not establish actual traversal, Path identity, branch handling, selection, or `COMPOSE` passage.

Primary definition and operational site: [`Chapter 9`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

---

## Chapter 10 Preparation Terminology Handoff

Chapter 3 retains primary ownership of the core temporal object definition. Chapter 10 is the designated operational PATH site for the burdens below.

| Term | Controlled short definition | Designated primary site | Central non-equivalence |
| --- | --- | --- | --- |
| path threshold | additional burden beyond chronology/sequence requiring actual traversal, bounded reference, selection, connectedness, trace, branch/omission/loss disclosure | Chapter 10 §§10.1–10.2, returning to Chapter 3 | sequence or transition set ≠ path |
| actual traversal | source- and claim-supported realization of the selected chain rather than mere possibility or retrospective plausibility | Chapter 10 §§10.1, 10.6–10.7 | plausible route ≠ traversed route |
| path components | source configuration, transitions, intermediates, event/non-event structures, branch points, selected continuation, alternatives, endpoint/open continuation | Chapter 10 §10.3 | component list ≠ path automatically |
| path selection | declared relevance rule governing inclusion, compression, exclusion, uncertainty, alternatives, and residue | Chapter 10 §10.4 | selection ≠ archival completeness or storytelling |
| path frame | bounded reference, periodization, roles, institutions, environments, scopes, granularity, and comparison basis | Chapter 10 §10.5 | path boundary ≠ objective universal boundary |
| path evidence | declared support for components, traversal, connectedness, selection, branches, endpoint, gaps, and rivals | Chapter 10 §10.6 | evidence quantity ≠ path admissibility |
| realized path | actually traversed selected chain to the declared endpoint or open continuation | Chapter 10 §10.7 | realized ≠ necessary, rational, or closed |
| blocked continuation | source-supported available/prepared continuation prevented by an identifiable condition | Chapter 10 §10.8 | blocked ≠ imagined alternative |
| aborted path | initiated, authorized, or partly traversed route that ceased and may leave residue | Chapter 10 §10.9 | aborted ≠ never begun |
| deferred continuation | still-available continuation postponed under a temporally load-bearing condition | Chapter 10 §10.10 | deferred ≠ uninterrupted or permanently unrealized |
| path comparison | bounded comparison of paths under compatible frame, scope, selection, alternatives, and evidence | Chapter 10 §10.11 | path comparison ≠ endpoint comparison alone |
| path without strong dependence | valid path whose historical order adds limited constraint or explanatory load to the present | Chapter 10 §10.13 | path ≠ strong path dependence |
| minimal path record | compact path-specific declaration embedded in the Chapter-7 Shared Record | Chapter 10 §10.14 | record completeness ≠ path admissibility |

Production control: [`Chapter 10 Preparation Record`](Chapter_10_Preparation_Record.md). Canonical Sections 10.1–10.14 remain pending.

---

## Chapter 10 WP1 Canonical Terminology Handoff

| Term | Canonical WP1 control | Primary location | Non-equivalence |
| --- | --- | --- | --- |
| path | actually traversed, selectively reconstructed chain of relevant configurations and transitions in a declared frame | [§10.1](../01_blocks/02_part_i_path.md#10-1-definition-of-path) | path ≠ chronology, trajectory, dependence, or operation |
| path candidate | delimited path claim before full conjunctive passage | [§10.1](../01_blocks/02_part_i_path.md#10-1-definition-of-path) | candidate ≠ warranted path |
| actual traversal | source-supported passage of the bounded reference object through the selected chain | [§10.1](../01_blocks/02_part_i_path.md#10-1-definition-of-path) | plausible route ≠ traversed route |
| path component | claim-relevant configuration, transition, cluster, non-event structure, branch, continuation, alternative, or endpoint role | [§10.3](../01_blocks/02_part_i_path.md#10-3-path-components) | component inclusion ≠ constitutive role automatically |
| path selection | explicit rule for inclusion, compression, exclusion, alternatives, uncertainty, and lineage | [§10.4](../01_blocks/02_part_i_path.md#10-4-path-selection) | selection ≠ retrospective inevitability |
| path frame | bounded reference, periodization, environment, scope, granularity, relative level, and claim reach | [§10.5](../01_blocks/02_part_i_path.md#10-5-path-frame) | frame boundary ≠ universal boundary |
| path evidence | six-relation support architecture for component, traversal, constitutive, selection, branch, and praxis claims | [§10.6](../01_blocks/02_part_i_path.md#10-6-path-evidence) | evidence quantity ≠ admissibility |

Sections 10.7–10.14 remain pending.

---

## Chapter 10 WP2 — Qualified Path-Status Terms

### Realized Path

A warranted path whose declared chain was actually traversed by the bounded reference object through the stated analytical cut.

```text
realized
≠ necessary
≠ successful
≠ closed
```

Primary operational site: [`Chapter 10 §10.7`](../01_blocks/02_part_i_path.md#10-7-realized-path).

### Blocked Continuation

A source-supported continuation that was genuinely available or structurally prepared and whose further realization was prevented by an identifiable blocking condition. The preferred form preserves a realized prefix and an untraversed blocked continuation separately.

```text
imagined possibility
≠ blocked continuation
```

Primary operational site: [`Chapter 10 §10.8`](../01_blocks/02_part_i_path.md#10-8-blocked-path).

### Aborted Path

A path segment or continuation that was initiated, authorized, committed, or partially traversed and then ceased before its bounded continuation criterion was met.

```text
aborted
≠ never begun
```

Primary operational site: [`Chapter 10 §10.9`](../01_blocks/02_part_i_path.md#10-9-aborted-path).

### Deferred Continuation

A source-supported continuation whose realization is postponed while some bounded form of availability, authorization, preparation, or commitment remains operative at the relevant cut.

```text
deferred continuation
≠ uninterrupted continuation
```

Primary operational site: [`Chapter 10 §10.10`](../01_blocks/02_part_i_path.md#10-10-deferred-path).

### Qualified Path Status

A segment-, continuation-, claim-, and temporal-cut-relative declaration of realized, blocked, aborted, deferred, or unresolved historical relation. It is not a global essence, PMS operator, STRATA operation, or canonical Output Class.

---

## Chapter 10 WP3 — Comparison and Record Terminology

### Path Comparison

A bounded comparison between path claims whose reference, frame, temporal scope, granularity, selection, source basis, dimensions, uncertainty, and claim scope are explicitly aligned or translated.

```text
path comparison
≠ endpoint comparison alone
≠ universal ranking
```

Primary definition site: [`Chapter 10 §10.11`](../01_blocks/02_part_i_path.md#10-11-path-comparison).

### Incomparability

A positive bounded result where the declared path comparison cannot be responsibly carried under the available reference, frame, source, selection, or translation relation. It preserves valid local path findings.

### Endpoint Similarity

Similarity between path endpoints in one or more declared dimensions. It does not establish path identity, equivalent historical load, or equivalent continuation.

```text
same endpoint
≠ same path
```

Primary operational site: [`Chapter 10 §10.12`](../01_blocks/02_part_i_path.md#10-12-similar-end-states-different-paths).

### Path without Strong Dependence

A warranted reconstructible path whose earlier order carries weak, absent, or unresolved additional constraint on the current configuration beyond present conditions. It preserves history while withholding a stronger Chapter-12 dependence claim.

Primary operational site: [`Chapter 10 §10.13`](../01_blocks/02_part_i_path.md#10-13-path-without-strong-dependence).

### Minimal Path Record

A compact conceptual view of path-specific fields carried within the Shared Transformation Record. It is not a second schema and does not establish admissibility by completeness.

Primary operational site: [`Chapter 10 §10.14`](../01_blocks/02_part_i_path.md#10-14-minimal-path-record).


## Chapter 10 Provisional-Lock Terminology Handoff

**warranted path**  
An actually traversed, selectively reconstructed and constitutively connected chain of relevant configurations and individually tested transitions within a declared frame, with explicit selection, loss, alternatives, evidence, residue, and claim ceiling. It is not a Trajectory, Path-Dependence claim, operation occurrence, causal mechanism, or authority grant automatically.

**qualified path status**  
A segment-, continuation-, reference-, claim-, temporal-cut-, evidence-, and ceiling-relative declaration such as realized, blocked, aborted, deferred, open, or unresolved. It is not a global essence, PMS operator, STRATA operation, Output Class, or formal enum.

**Chapter 11 path handoff**  
A warranted Path record supplied for later Trajectory testing. It transfers actual traversal, selection, status lineage, endpoint, alternatives, evidence, loss, and residue but does not establish cumulative change, sedimentation, historical load, directed continuation, or Trajectory identity.

Primary definition and operational site: [`Chapter 10`](../01_blocks/02_part_i_path.md#chapter-10-path).

---

## Chapter 11 Preparation and WP1 Terminology Handoff

Sections 11.1–11.9 are now canonical. The first nine entries route to WP1–WP2; the remaining entries continue as bounded drafting controls for WP3.

| Term | Preparation definition | Primary canonical destination |
| --- | --- | --- |
| Trajectory threshold | additional load by which a warranted Path carries sedimented historical structure into present configuration and continuation possibilities | Chapter 11 §11.1–11.2 |
| Historical Sedimentation | traceable retention and cumulative transformation of earlier Path structure with present praxis effect | Chapter 11 §11.3 |
| historical co-determination | bounded present load from earlier Path structure without exclusive causal determination | Chapter 11 §11.2–11.3 |
| non-teleological directionality | dimension-specific oriented change preserving contingency, alternatives, reversal, and no destiny claim | Chapter 11 §11.4 |
| Attractor Sedimentation | bounded `Α + Θ` occurrence relation with stabilized continuation accessibility | Chapter 11 §11.5 |
| Asymmetry Accumulation | bounded `Ω + Θ` occurrence relation with repeated differential load and present effect | Chapter 11 §11.6 |
| Binding Accumulation | bounded `Ψ + Θ` occurrence relation with persistent commitment or breach/reopening cost | Chapter 11 §11.7 |
| Residual Accumulation | bounded `Λ + Θ` occurrence relation with persistent expectation-bound residue | Chapter 11 §11.8 |
| Trajectory Boundary | claim-relative start, endpoint/open cut, prehistory, periodization, and scope of the Trajectory reconstruction | Chapter 11 §11.10 |
| Trajectory Compression | declared reduction preserving load-bearing transitions, Non-Events, profiles, residue, alternatives, and loss | Chapter 11 §11.11 |
| Competing Trajectory Construction | materially different bounded reconstruction from shared or overlapping Path material | Chapter 11 §11.12 |
| False Trajectory | chronology, duration, repetition, or macro-coherence insufficient for a Trajectory claim | Chapter 11 §11.13 |
| Minimal Trajectory Record | compact Trajectory view inside the Shared Transformation Record | Chapter 11 §11.14 |

Production control: [`Chapter 11 Preparation Record`](Chapter_11_Preparation_Record.md).

## Chapter 11 WP1 Canonical Terminology Synchronization

| Term | Canonical WP1 meaning | Primary route |
| --- | --- | --- |
| Trajectory candidate | warranted Path plus a declared historical carrier, cumulative or sedimented relation, present praxis effect, Source–Result Dependency, counterpressure, and bounded claim ceiling | [§§11.1–11.2](../01_blocks/02_part_i_path.md#11-1-definition-of-trajectory) |
| warranted Trajectory | Trajectory candidate that additionally passes applicable continuity, admissibility, loss, governance, Stop, and Non-Capture tests | [§11.1](../01_blocks/02_part_i_path.md#11-1-definition-of-trajectory) |
| historical carrier | source-supported relation through which earlier Path structure persists or is translated into the present analytical cut | [§11.3](../01_blocks/02_part_i_path.md#11-3-historical-sedimentation) |
| historical co-determination | bounded contribution of earlier Path structure to present praxis conditions without exclusive causation or automatic Path Dependence | [§§11.1–11.2](../01_blocks/02_part_i_path.md#11-1-definition-of-trajectory) |
| present praxis effect | source-supported difference in meaning, cost, role, expectation, access, Asymmetry, Binding, residue, action corridor, or continuation attributable in part to the historical carrier | [§11.3](../01_blocks/02_part_i_path.md#11-3-historical-sedimentation) |
| non-teleological directionality | dimension-specific historical orientation that preserves alternatives, reversals, repairs, contingencies, and the distinction between accessibility and necessity | [§11.4](../01_blocks/02_part_i_path.md#11-4-directionality-without-teleology) |

These entries do not create new PMS primitives, operation kinds, Output Classes, scores, or machine truth conditions.

## Chapter 11 WP2 Canonical Profile Terminology Synchronization

| Term | Canonical WP2 meaning | Primary route |
| --- | --- | --- |
| Attractor Sedimentation | occurrence-level `Α + Θ` relation in which a source-supported historical carrier changes local friction, expectation, visibility, or default continuation accessibility | [§11.5](../01_blocks/02_part_i_path.md#11-5-attractor-sedimentation) |
| local friction | effort, delay, uncertainty, authorization burden, coordination work, or material cost required to enact a bounded continuation | [§11.5](../01_blocks/02_part_i_path.md#11-5-attractor-sedimentation) |
| Asymmetry Accumulation | occurrence-level `Ω + Θ` relation in which differential cost, access, exposure, information, capacity, burden, or exit condition is retained, intensified, redistributed, or hardened | [§11.6](../01_blocks/02_part_i_path.md#11-6-asymmetry-accumulation) |
| role hardening | repeated allocation through which a role becomes harder to leave, contest, reinterpret, or perform differently without person typing | [§11.6](../01_blocks/02_part_i_path.md#11-6-asymmetry-accumulation) |
| Binding Accumulation | occurrence-level `Ψ + Θ` relation in which commitments, reliance, coordination investment, breach cost, or reopening conditions remain present-bearing | [§11.7](../01_blocks/02_part_i_path.md#11-7-binding-accumulation) |
| Residual Accumulation | occurrence-level `Λ + Θ` relation in which expectation- and frame-bound Non-Events leave active, repaired, translated, dormant, or historically delimited residue | [§11.8](../01_blocks/02_part_i_path.md#11-8-residual-accumulation) |
| Changed Action Corridor | source-supported difference in practical accessibility, visibility, authorization, affordability, coordination feasibility, temporal availability, reversibility, expectedness, evidentiary burden, or exposure at the present analytical cut | [§11.9](../01_blocks/02_part_i_path.md#11-9-changed-action-corridors) |
| current-condition allocation | explicit separation of historical contribution, current-condition contribution, their interaction, and underdetermined allocation | [§11.9](../01_blocks/02_part_i_path.md#11-9-changed-action-corridors) |

These terms remain derived, occurrence-level, frame-bound, source-sensitive, and non-authorizing. Changed Action Corridors are an integrative present-effect declaration, not a fifth profile, operation, operator, score, prediction, or recommendation.

## Chapter 11 WP3 Canonical Boundary and Record Terminology Synchronization

| Term | Canonical WP3 meaning | Primary route |
| --- | --- | --- |
| Trajectory Boundary | claim-sensitive declaration of reference object, temporal beginning, entry rationale, relevant prehistory, included segments, analytical cut, terminal status, open continuation, disputed periodization, and claim scope | [§11.10](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary) |
| relevant prehistory | earlier source-supported structure that conditions the selected entry but is not included as a full constitutive Trajectory segment | [§11.10](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary) |
| present analytical cut | declared endpoint of the current reconstruction, which may remain distinct from the end of the Trajectory object | [§11.10](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary) |
| segment lineage | explicit relation among formation, reinforcement, redistribution, interruption, repair, dormancy, re-entry, reversal, Frame translation, or closure segments of a reference-preserving Trajectory claim | [§11.10](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary) |
| Trajectory Compression | selective representation of a historically extended object at coarser resolution while retaining constitutive trace and canonical Loss disclosure | [§11.11](../01_blocks/02_part_i_path.md#11-11-trajectory-compression) |
| macro-label substitution | replacement of traceable Path, transitions, Non-Events, profiles, alternatives, and loss by a large historical label that remains insensitive to source variation | [§11.11](../01_blocks/02_part_i_path.md#11-11-trajectory-compression) |
| Competing Trajectory Construction | source-responsible reconstruction of overlapping historical material that differs in boundary, periodization, constitutive selection, profile weighting, directionality, or claim scope | [§11.12](../01_blocks/02_part_i_path.md#11-12-competing-trajectory-constructions) |
| False Trajectory | diagnostic phrase for a failed or overclaimed Trajectory construction; not a new object class or Output Class | [§11.13](../01_blocks/02_part_i_path.md#11-13-false-trajectory) |
| Minimal Trajectory Record | compact Trajectory-specific view inside the Shared Transformation Record; not an independent schema or substantive warrant | [§11.14](../01_blocks/02_part_i_path.md#11-14-minimal-trajectory-record) |

These terms remain analytical, source-bound, claim-sensitive, revisable, and non-authorizing. Boundary, Compression, competition, and Record completion cannot create sedimentation, Path Dependence, a target function, or application authority.

## Chapter 11 Provisional-Lock Terminology Handoff

| Term | Locked Chapter 11 use | Non-equivalence |
| --- | --- | --- |
| Trajectory | warranted Path with source-traceable sedimented historical load co-determining present praxis and continuation possibilities | Trajectory ≠ Path Dependence |
| Historical Sedimentation | cumulative carried relation with present praxis effect and Source–Result Dependency | sedimentation ≠ duration, repetition, permanence |
| directionality | dimension-specific historical tendency under preserved contingency | directionality ≠ teleology |
| accumulation profile | bounded occurrence-level `Α/Ω/Ψ/Λ + Θ` relation | profile ≠ fused operator or score |
| Changed Action Corridor | historically altered field of practical accessibility across declared dimensions | narrowed corridor ≠ eliminated agency |
| Trajectory Boundary | claim-sensitive temporal and referential cut with prehistory, segment lineage, and open-continuation status | Boundary ≠ natural seam |
| Trajectory Compression | bounded representation preserving constitutive trace and canonical Loss | Compression ≠ macro-label substitution |
| False Trajectory | diagnostic name for a failed or overclaimed construction | False Trajectory ≠ no history or new Output Class |

Primary completion site: [`Chapter 11 completion boundary`](../01_blocks/02_part_i_path.md#chapter-11-completion-boundary).


---

## Chapter 12 Preparation Terminology Handoff

| Term | Preparation meaning | Primary canonical destination |
| --- | --- | --- |
| Path Dependence | graded property by which prior Path history may be indispensable to an adequate present reconstruction; not an object, operator, or operation | Chapter 12 §12.1 |
| weak order dependence | bounded local effect of sequence while the present remains largely reconstructible from current conditions | Chapter 12 §12.2 |
| strong Path Dependence | source-bounded historical indispensability for present meaning, cost, role, credibility, accessibility, reachability, or continuation | Chapter 12 §12.3 |
| historical indispensability | material inadequacy of the present reconstruction when the relevant prior Path is omitted or responsibly varied | Chapter 12 §§12.1–12.3, 12.11 |
| current-state baseline | strongest source-supported reconstruction from present rules, resources, roles, frames, constraints, and alternatives without detailed Path history | Chapter 12 §§12.3, 12.11 |
| historical-omission test | test of what becomes materially wrong, incomplete, or misleading when the relevant prior Path is removed from the reconstruction | Chapter 12 §12.11 |
| source-bounded alternative-history test | actual comparator, competing reconstruction, or bounded counterfactual variation used to test Source–Result Dependency without prediction | Chapter 12 §12.11 |
| dependence-bearing carrier | source-traceable `Α/Ω/Ψ/Λ + Θ` occurrence relation that remains present-bearing in a declared dependence dimension | Chapter 12 §§12.4–12.7 |
| modifier occurrence | later `Φ`, `Χ`, `Σ`, or `Ψ` occurrence that may attenuate, redistribute, redirect, or terminate a carrier without automatic erasure | Chapter 12 §§12.8–12.9 |
| reset claim | new testable claim that the earlier historical carrier no longer changes the present reconstruction; not inferred from a new label, frame, policy, exit, or repair | Chapter 12 §§12.8–12.9 |

These are bounded preparation definitions only. Canonical definition ownership remains with Chapter 12 after drafting. None creates a new PMS primitive, operation, Output Class, score, probability, causal proof, target function, or authority.

Production control: [`Chapter 12 Preparation Record`](Chapter_12_Preparation_Record.md).

## Chapter 12 WP1 Canonical Terminology Synchronization

| Term | Canonical WP1 meaning | Primary route |
| --- | --- | --- |
| Path Dependence | graded property by which a present configuration or bounded continuation field is materially dependent on a prior Path in a declared dimension | [§12.1](../01_blocks/02_part_i_path.md#12-1-path-dependence-as-a-property) |
| weak order dependence | bounded order-sensitive difference under substantial current-state reconstructibility | [§12.2](../01_blocks/02_part_i_path.md#12-2-weak-order-dependence) |
| strong Path Dependence | historical-indispensability claim under which the tested present dimension is materially misdescribed or underdescribed without the relevant prior Path | [§12.3](../01_blocks/02_part_i_path.md#12-3-strong-path-dependence) |
| dependence dimension | bounded current feature—such as meaning, credibility, cost, role, access, reversibility, evidentiary burden, or reachability—for which dependence is tested | [§12.1](../01_blocks/02_part_i_path.md#12-1-path-dependence-as-a-property) |
| present analytical cut | declared temporal cut at which current conditions and historical carriers are compared without later-outcome leakage | [§12.1](../01_blocks/02_part_i_path.md#12-1-path-dependence-as-a-property) |
| current-state baseline | explicit reconstruction of current rules, resources, roles, constraints, records, and alternatives used to test whether history is materially indispensable | [§12.3](../01_blocks/02_part_i_path.md#12-3-strong-path-dependence) |
| historical indispensability | condition under which omission or material alteration of the relevant Path makes the bounded present reconstruction materially inadequate | [§12.3](../01_blocks/02_part_i_path.md#12-3-strong-path-dependence) |
| approximately held-present comparison | source-bounded comparison that holds declared present features approximately similar while preserving remaining differences and without claiming object identity or causal isolation | [§12.3](../01_blocks/02_part_i_path.md#12-3-strong-path-dependence) |

These terms create no new PMS primitive, STRATA operation, Output Class, score, probability, target function, or authority layer.

## Chapter 12 WP2 Canonical Profile Terminology Synchronization

| Term | Canonical WP2 meaning | Primary route |
| --- | --- | --- |
| Attractor Dependence | bounded `Α + Θ` property claim where the prior recurrence lineage is materially indispensable to current friction, expectation, visibility, default, or continuation accessibility | [§12.4](../01_blocks/02_part_i_path.md#12-4-a-theta-attractor-dependence) |
| Asymmetry Dependence | bounded `Ω + Θ` property claim where prior distribution is materially indispensable to current cost, access, exposure, capacity, information, burden, role, or exit condition | [§12.5](../01_blocks/02_part_i_path.md#12-5-o-theta-asymmetry-dependence) |
| Binding Dependence | bounded `Ψ + Θ` property claim where prior commitment, reliance, coordination investment, or reopening structure is materially indispensable to the present | [§12.6](../01_blocks/02_part_i_path.md#12-6-ps-theta-binding-dependence) |
| Residual Dependence | bounded `Λ + Θ` property claim where a warranted expectation-bound Non-Event leaves historically indispensable present residue | [§12.7](../01_blocks/02_part_i_path.md#12-7-lambda-theta-residual-dependence) |
| dependence-bearing profile | occurrence-level historical carrier relation that passes a profile-specific present-effect and current-state-sufficiency burden; not a fused operator or score | [§§12.4–12.7](../01_blocks/02_part_i_path.md#12-4-a-theta-attractor-dependence) |
| profile non-compensation | rule that profile richness cannot repair invalid substrate, absent present effect, failed current-state pressure, missing Source–Result Dependency, or source/claim ceiling breach | [§12.7](../01_blocks/02_part_i_path.md#12-7-lambda-theta-residual-dependence) |

These terms remain occurrence-level, source-bound, dimension-specific, revisable, non-deterministic, and non-authorizing. They create no new PMS primitive, STRATA operation, Output Class, target function, score, probability, or authority layer.

## Chapter 12 WP3 Canonical Test and Modifier Terminology Synchronization

| Term | Canonical WP3 meaning | Primary route |
| --- | --- | --- |
| recontextualization under dependence | `Φ` occurrence that changes the frame and may preserve, translate, attenuate, redistribute, replace, release, or render irrelevant a historical carrier; not an automatic reset | [§12.8](../01_blocks/02_part_i_path.md#12-8-phi-under-path-dependence) |
| later modifier | temporally later `Χ`, `Σ`, or `Ψ` occurrence that changes a carrier's present force without automatically erasing the earlier Path | [§12.9](../01_blocks/02_part_i_path.md#12-9-chi-sigma-and-psi-as-later-trajectory-modifiers) |
| Historical-Omission test | test of what warranted present reconstruction becomes wrong, incomplete, or misleading when the relevant prior Path is omitted | [§12.11](../01_blocks/02_part_i_path.md#12-11-path-dependence-test) |
| source-bounded Alternative-History test | bounded variation of a source-supported earlier Path used to test Source–Result Dependency; not prediction or causal isolation | [§12.11](../01_blocks/02_part_i_path.md#12-11-path-dependence-test) |
| Current-State Baseline | strongest source-supported explanation of the tested present feature using current conditions only | [§12.11](../01_blocks/02_part_i_path.md#12-11-path-dependence-test) |
| Minimal Path-Dependence Claim View | compact view inside the Shared Transformation Record; not a second schema and not proof | [§12.11](../01_blocks/02_part_i_path.md#12-11-path-dependence-test) |

These terms are source-bound, dimension-specific, non-deterministic, revisable, and non-authorizing.

## Chapter 12 Provisional-Lock Terminology Handoff

- **Path Dependence:** graded property of a warranted Path, Trajectory, or bounded segment at a declared present cut and dependence dimension; not an object, primitive, operation, level, target function, score, or authority layer.
- **Weak Order Dependence:** bounded historical effect under substantial current-state reconstructibility.
- **Strong Path Dependence:** historical indispensability of a relevant prior Path to adequate reconstruction of a tested present dimension.
- **Current-State Sufficiency Challenge:** explicit counterpressure asking whether current conditions alone adequately explain the tested present feature.
- **Historical Omission:** source-bounded test of what becomes materially false, incomplete, or misleading when the relevant prior Path is removed from the reconstruction.
- **Alternative History:** bounded variation supported by historically available or structurally comparable sources; not free counterfactual storytelling or prediction.
- **Modifier:** later `Χ`, `Σ`, or `Ψ` occurrence that may alter dependence without automatically erasing it.
- **Dependence-bearing profile:** occurrence-level `Α + Θ`, `Ω + Θ`, `Ψ + Θ`, or `Λ + Θ` relation carrying a bounded present dependence dimension under independent support.

Canonical return: [`Chapter 12 completion boundary`](../01_blocks/02_part_i_path.md#chapter-12-completion-boundary).

---

## Chapter 13 Preparation Terminology Handoff

| Term | Preparation meaning | Canonical destination |
| --- | --- | --- |
| alternative space | source-bounded field of historically reachable, conditionally reachable, prepared, contested, or later-lost continuations material to a Path claim | Chapter 13 §13.1 |
| branch point | historical configuration and window in which more than one continuation was practically source-supported | Chapter 13 §13.2 |
| realized branch | actually traversed continuation without rationality, legitimacy, optimality, or necessity inference | Chapter 13 §13.3 |
| rejected branch | materially available continuation that was source-supported as refused or not selected | Chapter 13 §13.4 |
| blocked branch | materially available or prepared continuation prevented by an identifiable blocking structure | Chapter 13 §13.5 |
| aborted branch | initiated continuation later interrupted, with possible sunk cost, expectation, infrastructure, or residue | Chapter 13 §13.6 |
| deferred branch | continuation shifted beyond its initial window and therefore subject to changed conditions | Chapter 13 §13.7 |
| lost alternative | earlier source-supported continuation that later became unavailable or materially unreachable | Chapter 13 §13.8 |
| source-bounded counterfactual Path | hypothetical continuation beginning from a documented alternative and stopping at the source ceiling | Chapter 13 §13.9 |
| non-selection | source-supported absence of selection inside an active decision context and temporal window | Chapter 13 §13.10 |
| alternative-space compression | reduced visibility of historically relevant alternatives in a Path or Trajectory representation | Chapter 13 §13.11 |
| Alternative Status Record | Shared-Record view declaring branch point, availability, status, window, support, later reachability, effect, and uncertainty | Chapter 13 §13.12 |

These are preparation definitions only. They create no PMS primitive, operation, Output Class, forecast, counterfactual truth, completed `COMPOSE`, target function, or authority. Production control: [`Chapter 13 Preparation Record`](Chapter_13_Preparation_Record.md).

## Chapter 13 WP1 Terminology Synchronization

### Alternative Space
Source-bounded field of continuations materially or conditionally reachable at a declared historical cut. It is not the set of all imaginable possibilities.

### Branch Point
Declared historical configuration and temporal window at which at least two distinct continuations were source-supported as materially available, conditionally available, prepared, or actively contested.

### Realized Branch
Continuation actually entered and traversed from a warranted alternative field. Realization does not imply rationality, legitimacy, optimality, intention, or inevitability.

### Rejected Branch
Materially or conditionally available continuation documented as declined or not selected while the relevant availability window remained open.

Primary definition site: [Chapter 13 WP1](../01_blocks/02_part_i_path.md#13-branches-aborts-delays-and-unavailable-alternatives).

## Chapter 13 WP2 Terminology Synchronization

### Blocked Branch
Earlier materially or conditionally available, prepared, or attempted continuation prevented inside a declared historical window by an identifiable blocking structure. Blocked is not impossible, rejected, or merely unrealized.

### Aborted Branch
Continuation actually initiated and partially traversed, then interrupted before the claimed transition or continuation was completed. Initiation trace is mandatory; planning or announcement alone is insufficient.

### Deferred Branch
Continuation shifted beyond its initially relevant window while later candidacy or reachability remains. Delay is part of the Path and may change the continuation's frame, cost, roles, permissions, bindings, and identity.

### Lost Alternative
Earlier source-supported continuation that later became unavailable or materially unreachable under a declared frame and claim scope. Lost is not merely unattractive, more expensive, temporarily blocked, or retrospectively imagined.

Primary definition site: [Chapter 13 WP2](../01_blocks/02_part_i_path.md#13-5-blocked-branch).

## Chapter 13 WP3 Terminology Synchronization

### Counterfactual Path

A source-bounded hypothetical continuation beginning from a historically available branch at a declared cut, using an explicit variation rule and stopping at the counterfactual horizon where source support no longer carries the continuation.

### Non-Selection

The source-supported absence of selection inside an active decision context and bounded temporal window where that absence changes later reachability, cost, role, binding, residue, or Path formation. Missing decision information alone is insufficient.

### Alternative-Space Compression

The disclosed reduction of the visible historical alternative field in a Path, Trajectory, record, diagram, or later composition. It is governed by the canonical five-part Loss structure and must not produce retrospective linearization or branch inflation.

### Counterfactual Horizon

The last point at which a Counterfactual Path remains reconstructively anchored. Beyond it, only open possibility, uncertainty, Stop, or Non-Capture may be declared.

### Alternative Status Record Extension

An owner-bound Shared-Record `extensions` entry for one historical continuation, declaring window, availability, source support, selection status, later reachability, residual effect, uncertainty, claim scope, and Output-Class mapping without replacing required fields.

Primary definition site: [Chapter 13 WP3](../01_blocks/02_part_i_path.md#13-9-counterfactual-path).

## Chapter 13 Provisional-Lock Terminology Boundary

Chapter 13 is provisionally locked. `Historical Alternative`, `Branch Point`, `Realized Branch`, `Rejected Branch`, `Blocked Branch`, `Aborted Branch`, `Deferred Branch`, `Lost Alternative`, `Counterfactual Path`, `Non-Selection`, `Alternative-Space Compression`, `counterfactual horizon`, and `Alternative Status Record` retain their source-, window-, and claim-bounded definitions from Sections 13.1–13.12.

None is a PMS primitive, STRATA operation, Output Class, prediction category, causal finding, target function, or authority layer. A later same-labelled continuation does not automatically inherit identity or continuity. A complete Record or graph does not establish availability or status.

Canonical return: [`Chapter 13 completion boundary`](../01_blocks/02_part_i_path.md#chapter-13-completion-boundary).

## Chapter 14 Preparation Terminology Handoff

This handoff prepares PATH-specific Non-Event terminology without replacing the foundational definition in Chapter 3.

| Term | Preparation meaning | Primary owner after drafting | Required non-equivalence |
| --- | --- | --- | --- |
| PATH-specific Non-Event | source-supported non-realization of an identifiable expected occurrence inside a warranted frame and bounded window, carrying praxeological and temporal-chain load | Chapter 14, consuming Chapter 3 | ordinary absence; missing source |
| expectation relation | source-supported commitment, rule, schedule, role, recurrent procedure, adopted plan, trigger, or comparable relation that makes an occurrence due or conditionally due | Chapter 14 | analyst preference; moral intuition |
| expectation frame | declared institutional, procedural, relational, contractual, or other context in which the expectation relation operates | Chapter 14 | granularity; relative level |
| expected window | bounded interval, deadline, recurrence window, trigger condition, or sequence position in which realization is due | Chapter 14 | open-ended possibility |
| source-supported non-realization | evidence capable of establishing that the expected occurrence did not realize inside the declared bound | Chapter 14 with Chapter 49 limits | no record found |
| Delay as Non-Event | missed warranted realization window whose non-realization changes praxis conditions | Chapter 14 | observed postponement-event chain |
| repeated Non-Decision | renewed decision contexts in which an expected decision repeatedly fails to realize | Chapter 14 | refusal; repeated missing records |
| Blocked Responsibility | expected action or decision remains unrealized under a traceable distributed or blocking responsibility structure | Chapter 14 | person blame; diagnosis |
| Missing Repair | warranted repair, integration, correction, review, or remediation fails within its supported frame and window | Chapter 14 | undefined duty |
| Missing Exit | warranted or triggered exit/release occurrence fails within its supported condition or window | Chapter 14 | hidden motive; formal exit availability alone |
| Non-Event Sedimentation | one or more warranted `Λ` occurrences remain active in later meaning, cost, roles, alternatives, bindings, residue, or corridors | Chapter 14 | repetition or duration alone |
| False Non-Event | local failed claim where expectation, window, source-supported non-realization, load, or relevance is missing | Chapter 14 | proof that a positive event occurred |
| Minimal Non-Event Record | bounded Shared-Record view prepared for Chapter 14; carrier decision deferred to WP3 | Chapter 14 / Chapter 7 record owner | semantic proof; parallel record schema |

Canonical preparation control: [`Chapter_14_Preparation_Record.md`](Chapter_14_Preparation_Record.md).

## Chapter 14 WP1 Terminology Synchronization

### PATH-Specific Non-Event
A Chapter-3-eligible Non-Event whose source-supported non-realization materially changes a declared Path relation such as transition completion, configuration persistence, alternatives, costs, roles, bindings, residue, or later meaning.

### Expectation Relation
Source-supported commitment, rule, procedure, schedule, role relation, recurrent practice, adopted plan, or triggered condition that makes a specified occurrence due or conditionally due.

### Expectation Frame
Declared contextual structure within which an occurrence becomes expected and its non-realization becomes analytically relevant.

### Expected Window
Bounded date, interval, recurring window, triggered condition, sequence position, or phase-completion condition within which realization is due.

### Delay as Non-Event
Source-supported failure of an expected transition within its warranted window where the missed window carries material Path load. Positive postponement events may coexist with the governing non-realization.

Primary definition site: [Chapter 14 WP1](../01_blocks/02_part_i_path.md#14-non-events-within-paths-and-trajectories).

## Chapter 14 WP2 Terminology Synchronization

### Repeated Non-Decision
A sequence of renewed or recurring decision contexts in which a source-supported expected decision repeatedly remains unrealized. It is not a long silent interval, repeated missing documentation, or repeated refusal.

### Blocked Responsibility
A configuration-level Non-Event pattern in which distributed, cyclic, conditional, jurisdictional, or authorization-dependent responsibility relations prevent an expected occurrence from resolving. It does not assign person blame, legal duty, diagnosis, or sanction.

### Missing Repair
A warranted repair, integration, correction, reconciliation, restoration, or closure occurrence that fails within its expected frame and window and leaves material residue or changes later praxis.

### Missing Exit
A warranted or triggered exit or release occurrence that fails within a bounded realization condition and materially changes the Path. Formal exit availability and observed continuation are insufficient.

### Non-Event Sedimentation
Traceable carryover of one or more warranted `Λ` occurrences into later meaning, costs, roles, alternatives, bindings, residue, or action corridors.

Primary definition site: [Chapter 14 WP2](../01_blocks/02_part_i_path.md#14-4-repeated-non-decision).

## Chapter 14 WP3 Terminology Synchronization

### False Non-Event
A claimed `Λ` occurrence that fails one or more constitutive burdens: identifiable expected occurrence, warranted expectation relation, declared frame, bounded window or condition, source-supported non-realization, praxeological load, or temporal-chain relevance. It is a local failure description, not an Output Class and not proof of positive occurrence.

### Minimal Non-Event Record
An optional owner-bound `extensions` view inside the Shared Transformation Record that preserves one bounded PATH-specific `Λ` claim without replacing required top-level fields.

### Non-Event Preservation Burden
The requirement that later composition preserve or place under canonical Loss the expectation, frame, window, non-realization, positive sub-events, persistence/repetition, affected roles and alternatives, residue, later carrier, uncertainty, and missing-information distinction.

Primary definition site: [Chapter 14 WP3](../01_blocks/02_part_i_path.md#14-9-preserving-%CE%BB-in-composition).

## Chapter 14 Provisional-Lock Terminology Boundary

Chapter 14 is provisionally locked. `PATH-specific Non-Event`, `Expectation Relation`, `Expectation Frame`, `Expected Window`, `Delay as Non-Event`, `Repeated Non-Decision`, `Blocked Responsibility`, `Missing Repair`, `Missing Exit`, `Non-Event Sedimentation`, `False Non-Event`, and `Minimal Non-Event Record` retain their bounded meanings from Sections 14.1–14.11.

None is a new PMS primitive, STRATA operation, Output Class, person diagnosis, blame category, duty finding, target function, or authority layer. Missing information, an empty interval, a graph gap, later residue, or a complete record does not establish `Λ`.

Canonical return: [`Chapter 14 completion boundary`](../01_blocks/02_part_i_path.md#chapter-14-completion-boundary).

## Chapter 15 Preparation Terminology Handoff

| Term | Preparation meaning | Primary owner | Required non-equivalence |
| --- | --- | --- | --- |
| COMPOSE occurrence | one bounded execution of the canonical operation over typed, related sources | Chapter 15 consuming Chapter 4 | operation type; target composite |
| source set | declared typed objects eligible for one composition claim | Chapter 15 | composite object |
| selection rule | source- and claim-bound justification for inclusion, omission, load-bearing status, and contestability | Chapter 15 | passive discovery; endpoint convenience |
| ordering rule | warranted temporal or structural relation among sources | Chapter 15 | storytelling order |
| formation rule | account of how constitutive relations produce a new composite with added praxis discrimination | Chapter 15 | aggregation; macro-label |
| constitutive relation | relation whose removal or material change alters target identity or licensed claim | Chapter 15 | illustrative association |
| preservation duty | requirement that target claims remain reconstructibly dependent on constitutive source load | Chapter 15 | total retention; losslessness |
| overelastic composition | target label or claim remains unchanged under too many material source alterations | Chapter 15 | robustness automatically |
| composition claim | bounded claim licensed by one COMPOSE occurrence about a declared target class | Chapter 15 | Path-Dependence or function claim automatically |
| no-composition option | explicit possibility that the warranted result remains a collection, chronology, or unresolved source field | Chapter 15 | failure to analyze |

Canonical preparation control: [`Chapter_15_Preparation_Record.md`](Chapter_15_Preparation_Record.md).

## Chapter 15 WP1 Terminology Synchronization

### COMPOSE Entry Gate
Conjunctive and non-compensatory threshold requiring typed sources, scope, relation, selection, ordering where claimed, formation hypothesis, source support, expected praxeological difference, possible five-part Loss, bounded target claim, and rival/no-composition pressure.

### Source-Set Boundary
Claim-bound declaration of the source domain searched, time range, eligible source families, inaccessible or contested material, and use of later sources.

### Source Role
Local declaration that a source is load-bearing, supporting, illustrative, redundant, contested, omitted, or excluded. Source roles are not new canonical Output Classes.

### Partial Order
Warranted ordering in which only some source relations are fixed while other cross-order relations remain unresolved or simultaneous.

### Composition Frame
Declared contextual boundary connecting the reference object, source frame, target-object frame, temporal scope, roles/contexts, granularity, relative level, Claim Boundary, and Claim Ceiling for one COMPOSE candidate.

Primary definition site: [Chapter 15 WP1](../01_blocks/02_part_i_path.md#15-compose-selection-formation-and-compression).

## Chapter 15 WP2 Terminology Synchronization

### Formation Hypothesis
Provisional claim that selected, ordered, and framed sources may form a declared composite through specified constitutive relations. It is not a completed formation finding or `COMPOSE` occurrence.

### Formation Finding
Bounded finding that a target object is more than a collection or chronology because a declared Formation Rule, constitutive relations, source trace, target threshold, and Loss duties are supported.

### Preserved Structure
Claim-relevant source load that remains reconstructibly connected to the target through representation, explicit relation, stable lineage, or another declared carrier. Preservation is not total copying or losslessness.

### Compression Rule
Declared method for reducing resolution while specifying what remains represented, what is lost at target level, what remains externally recoverable, and how uncertainty and claim scope change.

### Excluded Structure
Material explicitly and reasonedly kept outside one target composition. Exclusion is frame-bound and is not disproof, source absence, accidental omission, compression, or uncertainty.

### Source-Inherited Irrecoverability
Information already unavailable before the composition occurrence and not reconstructible from the available source lineage.

### Composition-Induced Irrecoverability
Information rendered non-reconstructible by the composition's selection, boundary, relation, or compression procedure.

Primary definition site: [Chapter 15 WP2](../01_blocks/02_part_i_path.md#15-7-formation-rule).

## Chapter 15 WP3 Terminology Synchronization

### Composition Claim
Bounded claim licensed about a formed composite object. It is distinct from the object, its constitutive-relation finding, and stronger target-level claims.

### Counterfactual Composition Test
Source-bounded variation of removal, substitution, reorder, recompression, reframing, rival composition, or no-composition used to test whether declared elements and relations are constitutive. It is not free alternative history or causal proof.

### Overelastic Composition
Composition whose target label and claim remain unchanged under changes that should be material if the declared Formation Rule and constitutive set were genuine.

### Constitutive Load
Source or relation whose bounded removal or exchange materially changes the target identity, boundary, type, or licensed claim. Constitutive status is claim-relative.

Primary definition site: [Chapter 15 WP3](../01_blocks/02_part_i_path.md#15-12-composition-claim).

## Chapter 15 Provisional-Lock Terminology

### COMPOSE Occurrence
A particular execution of the canonical `COMPOSE` operation over typed and selected source structures under a declared ordering, frame, Formation Rule, constitutive relation set, target typing, Loss declaration, sensitivity test, Claim Ceiling, and canonical output route.

### Composite Analytical Object
A new derived object formed by a warranted `COMPOSE` occurrence. It preserves source origin types and does not become a PMS primitive, contextual target function, or authority source.

### Overelastic Composition
A composition whose target identity and claim remain unchanged under source-bounded variations that should be material if the declared constitutive set and Formation Rule were genuine.

### No-Composition
Positive analytical result where source relations, praxis purchase, type integrity, traceability, target boundary, or Loss requirements do not support formation of one composite.

Primary definition site: [`Chapter 15 completion boundary`](../01_blocks/02_part_i_path.md#chapter-15-completion-boundary).

## Chapter 16 Preparation Terminology Handoff

| Term | Preparation meaning | Primary owner | Required non-equivalence |
| --- | --- | --- | --- |
| Lower PATH Boundary | point below which added temporal differentiation creates no material praxis gain for the tested claim | Chapter 16 consuming Chapter 6 | Upper PATH Boundary |
| Upper PATH Boundary | point above which a temporal result no longer carries reconstructible load from declared source structures | Chapter 16 consuming Chapter 6 | lower-bound failure |
| chronology without gain | correct or detailed order that does not alter the licensed praxis reconstruction | Chapter 16 | false chronology; Trajectory |
| Trajectory without Path trace | historical macro-claim lacking reconstructible configurations, transitions, alternatives, `Λ`, `Ω`, and Loss | Chapter 16 | bounded abstraction |
| temporal punctualization | collapse of an extended internally differentiated process into a point or homogeneous phase | Chapter 16 | warranted compression |
| artificial directionality | retrospective order presented as intrinsic historical vector while contingency and reversals are suppressed | Chapter 16 | directionality as bounded finding |
| hidden teleology | endpoint-conditioned selection or periodization that renders the later outcome necessary or purposive | Chapter 16 | non-teleological directionality |
| PATH anti-rescue rule | a failed PATH claim remains failed across frame, level, granularity, graph, SUB, RETYPE, or label changes unless retested as a new claim | Chapter 16 | prohibition on new analysis |

Canonical preparation control: [`Chapter_16_Preparation_Record.md`](Chapter_16_Preparation_Record.md).

## Chapter 16 WP1 Terminology Synchronization

### Lower PATH Boundary
PATH-local application of the Praxeological Relevance Floor. Temporal differentiation passes only where it materially changes a warranted reconstruction of praxis for the tested claim.

### Chronology without Trajectory Gain
Accurate or useful ordering that does not establish sedimentation, historical load, changed continuation structure, or a stronger temporal claim.

### Upper PATH Boundary
PATH-local application of the Praxeological Traceability Ceiling. A target remains within the Ceiling only while its identity and claim are reconstructibly dependent on the temporal and structural source load declared as constitutive.

### Trajectory without Path Trace
A claimed historical direction or sedimentation whose configurations, transitions, turning points, Non-Events, asymmetries, alternatives, repairs, present-bearing load, selection, compression, or Loss cannot be reconstructed sufficiently for the claim.

### Punctualization
Excessive temporal compression that treats an internally differentiated extended process as one point, event, or homogeneous phase and thereby removes claim-relevant internal temporality.

### Same-Material Band Contrast
Use of one broad source field to compare an admissible PATH representation, a below-Floor chronology, and an above-Ceiling macro-label without treating them as stylistic equivalents.

Primary definition site: [Chapter 16 WP1](../01_blocks/02_part_i_path.md#16-path-boundary-conditions).

## Chapter 16 WP2 Terminology Synchronization

### Artificial Directionality
A directionality claim produced by retrospective linearization that suppresses source-supported contingency, reversals, parallel subpaths, alternatives, or periodization dependence and presents one invariant developmental vector.

### Hidden Teleology
Endpoint-conditioned selection, periodization, or interpretation through which a realized later state is treated as earlier purpose, necessary destination, progress, decline, maturation, convergence, or predictive completion.

### Constitutive Omission
Removal or translation of a source structure whose restoration materially changes the target boundary or claim. Chapter 16 WP2 applies this to warranted `Λ` and source-supported `Ω` load.

### PATH/RETYPE Rescue
Prohibited attempt to repair a failed temporal-object claim by assigning the object a contextual target function. A lawful later `PROJECT_AS` is a new claim and preserves the failed origin analysis.

### PATH/SUB Rescue
Prohibited attempt to repair a failed PATH claim through finer detail or interface expansion. A lawful `DECOMPOSE` requires an identified compressed occurrence or composite, same reference object, explicit reconstruction rule, and separate record.

Primary definition site: [Chapter 16 WP2](../01_blocks/02_part_i_path.md#16-6-artificial-directionality).

## Chapter 16 WP3 Terminology Synchronization

### PATH Praxeological Purchase Test
Claim-relative test of whether temporal differentiation materially changes a warranted reconstruction of roles, costs, alternatives, bindings, residuals, reachability, Action Corridors, target class, or Claim Ceiling.

### Traceable Path Test
Test of whether a PATH target and claim remain reconstructibly dependent on typed source structures, warranted order, constitutive load, selection, formation, complete Loss, and bounded sensitivity.

### PATH Claim Reduction
Controlled withdrawal or narrowing of an unsupported stronger temporal claim while preserving warranted sources, relations, uncertainty, Loss, and weaker target objects.

### PATH Non-Capture
Canonical `non_capture` result where one adequate temporal object remains unavailable after bounded tests because forced closure would erase decisive heterogeneity, incompatible traces, or unresolved periodization.

Primary definition site: [Chapter 16 WP3](../01_blocks/02_part_i_path.md#16-12-praxeological-purchase-test).

## Chapter 16 Provisional-Lock Terminology

| Term | Locked local meaning | Non-equivalence |
| --- | --- | --- |
| PATH Relevance Floor | lower local boundary at which temporal differentiation must materially change the warrantable praxis reconstruction | more dates, duration, or detail |
| PATH Traceability Ceiling | upper local boundary at which the target and claim must remain reconstructibly dependent on their declared path load | citation density, graph cohesion, or macro-label stability |
| Purchase Test | claim-relative test of whether temporal differentiation changes roles, costs, alternatives, binding, residues, reachability, or Action Corridors | additive score or whole-object gain |
| Traceable Path Test | test of typed, lineaged, ordered, relational, loss-declared, and sensitivity-bearing source-to-result dependency | total certainty or forced total order |
| punctualization | destructive collapse of internally differentiated temporal structure into a point, event, or homogeneous period | bounded compression |
| artificial directionality | unsupported conversion of retrospective order, visual direction, or endpoint-conditioned selection into historical direction | bounded dimension-specific directionality |
| PATH anti-rescue rule | prior PATH failure survives frame, level, granularity, graph, SUB, RETYPE, or label changes unless separately retested | prohibition on new analysis |

Primary return: [`Chapter 16 completion boundary`](../01_blocks/02_part_i_path.md#chapter-16-completion-boundary).

## Chapter 17 Preparation Terminology Handoff

**PATH case** — a bounded reconstruction that tests a PATH claim under explicit sources, coordinates, operation decision, Loss, alternatives, Band findings, and canonical output mapping.

**PATH countercase** — a plausible but inadmissible or overextended temporal construction used to discriminate a specific rule, boundary, reduction, Stop, or failure route.

**PATH confusion case** — a case that holds adjacent interpretations or operations apart until the correct object, frame, resolution, or operation boundary is tested.

**lock-critical case artifact** — the required linked set of Markdown reconstruction, schema-valid YAML record, local audit result, and canonical Output-Class mapping.

**PATH local audit** — the Chapter-17 audit that tests case artifacts and Part-I rules without replacing Chapter 53's system-wide audit.

Canonical preparation control: [`Chapter_17_Preparation_Record.md`](Chapter_17_Preparation_Record.md).

## Chapter 17 WP1 Terminology Synchronization

### Standalone PATH Case Artifact
A linked Markdown reconstruction and schema-valid YAML Shared Transformation Record carrying complete Loss, alternatives, a local audit, canonical output mapping, Stop/Non-Capture status, and governance boundary.

### Local PATH Case Result
Operation-specific description such as bounded Path, branching Path, or source-sensitive Trajectory. It is not a canonical Output Class and must be mapped explicitly.

### Lock-Critical Case Artifact
A standalone case set required for provisional Part-I lock. Completion of one such artifact does not satisfy the three-artifact minimum or validate PATH globally.

Primary definition site: [Chapter 17 §17.1](../01_blocks/02_part_i_path.md#17-1-case-architecture).

## Chapter 17 WP2-A Terminology Synchronization

### Dependence Dimension
A declared present feature—such as burden, reversibility, residual repair, meaning, access, or continuation—for which historical indispensability is tested separately. Dependence in one dimension does not establish total historical determination.

### Current-State Sufficiency
A bounded finding that present configuration and immediate carrier conditions adequately support the tested present claim without full historical reconstruction. It does not make history irrelevant.

### Weak Path Dependence
A bounded historical contribution in which order or earlier stabilization changes some local reconstruction while the tested current state remains substantially reconstructible from present conditions.

Primary sites: Chapter 17 §§17.5–17.6.

## Chapter 17 WP2-B Terminology Synchronization

**Chronology Presented as Path** — an accurate ordered source field whose stronger Path label lacks a supported continuation-sensitive Formation Rule.

**Source-indifferent macro target** — a proposed composite whose identity remains unchanged under removal, inversion, or replacement of source structures declared constitutive.

**Teleological composition** — a `COMPOSE` occurrence in which the realized endpoint controls earlier source selection or interpretation, producing retrospective purpose or necessity rather than source-sensitive historical formation.

Primary sites: Chapter 17 §§17.7–17.9.


## Chapter 17 WP2-C Terminology Synchronization

**Composition through omitted asymmetry** — A failed `COMPOSE` occurrence in which event order is retained but materially constitutive occurrence-level `Ω` load is removed from target identity.

**False central Non-Event** — An unsupported `Λ` construction formed from missing information without a source-supported expectation frame, expected window, and praxeological non-occurrence effect.


## Chapter 17 WP3-A Terminology Synchronization

**Projection claim separation** — Preservation of an origin-typed PATH object while a contextual function claim is withheld for a separate `PROJECT_AS` record.

**Resolution-neutral temporal elaboration** — A valid source-supported temporal refinement that leaves the warranted praxis reconstruction materially unchanged and forms neither a new PATH object nor `DECOMPOSE` automatically.

**Trajectory/Attractor boundary** — Repetition within one historical Trajectory does not establish Attractor identity or a contextual Attractor-function.


## Chapter 17 WP3-B Terminology Synchronization

**PATH Local Audit** — chapter-level integration test over the case corpus; distinct from the twelve-stage audit of one Transformation Record.

**Part-I lock readiness** — positive finding that Chapter-17 and PATH Gate prerequisites are complete; not the provisional lock act itself.

**PATH Output census** — descriptive count of selected canonical classes in the current case corpus; never a quota, score, rank, or routing rule.

## Part I — PATH Provisional-Lock Terminology

**Part-I provisional lock** — positive integrated closure of the current Chapters 9–17 PATH corpus under its Contracts, cases, audits, references, model mirrors, and package checks; not final STRATA lock, empirical validation, or authority.

**PATH reopening ground** — concrete Contract, type, operation, source/claim, artifact, schema, mapping, reference, fingerprint, package, or later integrated-audit conflict capable of changing the locked PATH state; not preference for more detail or stronger narrative closure.

**PATH-to-SUB handoff** — transfer of a provisionally locked temporal composite as a possible Chapter-18 source object without inherited truth priority, decomposition requirement, or authority.

## Chapter 18 Preparation Terminology Lock

Chapter 18 remains the primary definition site for `provisional elementarity` and `compressed object`. The Preparation Gate fixes their use without replacing the canonical prose still to be drafted:

- provisional elementarity is relative to Frame, granularity, claim, source access, and present analytical use;
- compressed object denotes an occurrence or composite treated as a unit while internal structure remains unrepresented;
- operator types are never compressed empirical aggregates;
- source function is the current/coarser function tested by later decomposition and remains distinct from target function;
- no-decomposition is a legitimate bounded decision, not proof of simplicity.

```text
provisional elementarity ≠ final constituent
compressed object ≠ simple object
source preservation ≠ source-function immunity
```

## Chapter 18 WP1 Canonical Terminology Synchronization

**SUB source-candidate architecture** — the bounded declaration of an identifiable occurrence or composite before target granularity, component identity, relation reconstruction, or a `DECOMPOSE` result is claimed.

**Absolute-elementarity prohibition** — STRATA authorizes no claim that a source object is finally indivisible or ultimately constituted. Provisional elementarity records only where the current reconstruction stops for a declared coordinate set, source access, and claim.

**Known / unresolved / unsupported internal content** — three-way control separating directly supported source-side distinctions, bounded open questions, and content that may not be populated from the coarse label alone.

**Source-side typing** — the occurrence typing relevant to the present transformation question; it does not establish one exclusive true type of the reference object.

```text
source candidate ≠ target granularity ≠ discovered components ≠ DECOMPOSE result
unresolved internal structure ≠ hidden microstructure asserted as fact
object category ≠ source-side typing ≠ current/coarser function
```



## Chapter 18 WP2 Canonical Terminology Synchronization

**Necessary compression** — the bounded treatment of an occurrence or composite as one analytical unit where that representation preserves the reference, constitutive relation, uncertainty, comparison, temporal orientation, source precision, or claim ceiling required by the current inquiry. Necessary compression is not automatically `COMPOSE` and is not an analytical defect.

**Compression insufficiency** — the condition in which a source-supported internal distinction may materially alter a warranted reconstruction of the same reference object, its current/coarser function, burden allocation, temporal relation, alternatives, or claim scope. Available detail alone does not establish insufficiency.

**Reason to decompose** — a pre-operation proposal stating the coarse claim under pressure, expected internal distinction, source route, praxeological gain condition, neutrality condition, and stop condition. It does not establish components, target granularity, or a `DECOMPOSE` result.

**No-decomposition decision** — the bounded finding that finer reconstruction is not presently warranted for the declared reference, Frame, granularity, sources, claim, and expected difference. It is neither `resolution_neutral` nor proof of permanent undecomposability.

Canonical sites: [§18.5](../01_blocks/03_part_ii_sub.md#18-5-why-compression-is-necessary), [§18.6](../01_blocks/03_part_ii_sub.md#18-6-why-compression-can-become-insufficient), [§18.7](../01_blocks/03_part_ii_sub.md#18-7-reasons-to-decompose), and [§18.8](../01_blocks/03_part_ii_sub.md#18-8-reasons-not-to-decompose).


## Chapter 18 WP3 Terminology Synchronization

### Source Preservation
Retention of the same source reference, source-side typing, current/coarser function as test target, lineage, uncertainty, and inherited Loss across a proposed finer reconstruction. Preservation retains testability, not a favorable result.

### Source Immunization
Prohibited treatment of the coarse source function as true by definition, such that contrary finer findings are excluded, renamed, reframed, or absorbed rather than allowed to revise or defeat the claim.

### Minimal Source Declaration
Chapter-18 entry declaration containing `compressed_object`, `reference`, `origin_type`, `source_frame`, `source_granularity`, `source_level`, `current_function`, `known_internal_structure`, `unresolved_internal_structure`, and `decomposition_reason`. It is not a completed `DECOMPOSE` record.

### Source-Function Effect
Later Chapter-20 result concerning whether the current/coarser function is confirmed, refined, internally differentiated, partially preserved, rejected, or underdetermined. These local effects are not additional canonical Output Classes.

### Source-Entry Stop
Optional or Mandatory Stop applied before operation execution where coarse sufficiency, lack of purchase, source ceiling, type failure, reference substitution, or another controlled boundary blocks or renders unnecessary a proposed `DECOMPOSE` continuation.

Primary definition site: [Chapter 18 WP3](../01_blocks/03_part_ii_sub.md#18-9-preservation-requirement).


## Chapter 18 Provisional-Lock Terminology

### Source-Entry Architecture
The complete Chapter-18 declaration discipline preceding a possible `DECOMPOSE` occurrence: source reference, source-side typing and coordinates, current/coarser function under test, known and unresolved structure, decomposition reason, uncertainty, inherited Loss, and Stop/Non-Capture availability.

### Source Readiness
A bounded finding that the source object is sufficiently declared for Chapter-19 granularity analysis. Source readiness does not establish target-granularity validity, decomposition warrant, operation success, or source-function survival.

### Chapter-18 Provisional Lock
The integrated result that Chapter 18 satisfies its Contract and local audit while remaining revisable under concrete upstream, ownership, integrity, or later dependency conflict. It does not lock SUB, execute `DECOMPOSE`, or increase authority.

Primary site: [Chapter 18 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-18-completion-boundary).

## Chapter 19 Preparation Terminology Handoff

The Chapter-19 Preparation Gate introduces no new PMS primitive and no final lexicon entries. It prepares the following controlled usages for canonical definition in Chapter 19:

- **granularity relation** — a declared relation between source and target distinction sets for the same bounded source reference;
- **relative downward movement** — analytical movement toward finer internal relations under an explicit comparator, never an ontological lower layer;
- **functional component** — a source-supported part or relation that carries, modifies, disturbs, constrains, or tests the coarser reconstruction;
- **fragment** — a detail that lacks sufficient source-reference, relation, or claim relevance to count as a component;
- **granularity comparability** — the bounded ability to align or translate reconstructions across reference, Frame, time, source standards, predicates, and distinction dimensions;
- **granularity mismatch** — an apparent disagreement generated or intensified by non-aligned distinction sets, without automatic contradiction or automatic neutralization;
- **Minimal Granularity Relation** — the eight-field conceptual Chapter-19 declaration mapped to existing Shared Record paths and controlled extensions.

Protected usage:

```text
finer ≠ truer
relative downward ≠ ontological lower
component ≠ fragment
incomparability ≠ both claims true
mismatch ≠ contradiction dissolved
```

Primary canonical owner remains Chapter 19 after drafting and provisional lock. [`Chapter_19_Preparation_Record.md`](Chapter_19_Preparation_Record.md) is production control only.

## Chapter 19 WP1 Canonical Terminology Return

Chapter 19 WP1 now canonically fixes the following usages:

### Granularity Change
A declared change in the distinction set and resolution used to reconstruct and test a bounded source reference. More text, data, timestamps, quotations, or named details do not establish granularity change unless the operative distinctions change.

Primary site: [§19.1](../01_blocks/03_part_ii_sub.md#19-1-granularity-change).

### Granularity Relation
The declared analytical relation between a source resolution and a proposed target resolution of a bounded reference object, including the comparison dimension, Frame and reference status, and expected praxeological difference. Declaration does not prove target support, admissibility, or operation success.

Primary site: [Chapter 19 opening and §19.1](../01_blocks/03_part_ii_sub.md#chapter-19-granularity-change-and-the-logic-of-decomposition).

### Relative Downward Movement
Comparator-bound analytical movement from an occurrence or composite treated at one resolution toward proposed finer internal, reproductive, temporal, relational, or distributed structures. It is not ontological descent, lower operator rank, causal priority, or final constituent discovery.

Primary site: [§19.2](../01_blocks/03_part_ii_sub.md#19-2-relative-downward-movement).

### Stable Frame, Finer Granularity
A granularity relation in which the source reference, relevance rule, bounded predicate, and relevant scope remain sufficiently stable while the distinction set becomes finer along a declared dimension.

Primary site: [§19.3](../01_blocks/03_part_ii_sub.md#19-3-stable-frame-finer-granularity).

### Changed Frame during Decomposition
A separately declared change in relevance rule that may accompany finer analysis but creates a new Frame-bound claim and does not by itself identify `DECOMPOSE`.

Primary site: [§19.4](../01_blocks/03_part_ii_sub.md#19-4-changed-frame-during-decomposition).

The Preparation-Gate terms for functional component, fragment, comparability, mismatch, and Minimal Granularity Relation remain pending canonical return in WP2–WP3.

## Chapter 19 WP2 Canonical Terminology Return

### Distinction Set
The units, relations, temporal orderings, thresholds, role differences, access/cost/exposure relations, expectation windows, and exclusions through which a bounded source reference is reconstructed. More source material does not change the distinction set unless the operative partition or relation changes.

Primary site: [§19.5](../01_blocks/03_part_ii_sub.md#19-5-change-of-distinction-set).

### Locally Concentrated Component Candidate
A source-visible structure identifiable within a bounded segment or site that has a plausible relation to the source claim. Local concentration does not establish necessity, sufficiency, causal primacy, or final component status.

Primary site: [§19.6](../01_blocks/03_part_ii_sub.md#19-6-local-versus-distributed-structure).

### Distributed Component Candidate
A proposed source-relevant structure carried across times, roles, institutional sites, documents, relations, or non-contiguous occurrences while remaining traceably related to the bounded source object. Distribution does not automatically imply macro-level status.

Primary site: [§19.6](../01_blocks/03_part_ii_sub.md#19-6-local-versus-distributed-structure).

### Functional Component Candidate
A proposed part or relation satisfying the conjunctive burdens of reference relation, source route, function/claim relation, praxeological relevance, and relational placement. Candidate status does not establish actual component status or causal role.

### Carrying Component
A component that contributes to reproduction, maintenance, or constitution of a coarser source function without automatic necessity or sufficiency.

### Disturbing Component
A component whose source-supported relation may weaken, interrupt, contradict, qualify, or reject the coarser function or claim.

### Replaceable Component
A participating component for which alternative carriers may preserve the coarser function. Replaceability does not imply irrelevance.

### Fragment
A source-authentic or descriptive detail that fails the current conjunctive component burden. Fragment status is local to the declared Frame and claim, not a universal declaration of meaninglessness.

Primary site for component/fragment terms: [§19.7](../01_blocks/03_part_ii_sub.md#19-7-functional-parts-versus-mere-fragments).

Comparability, mismatch, the Lower Granularity Question, and the Minimal Granularity Relation remain pending canonical return in WP3.

## Chapter 19 WP3 Canonical Terminology Return

### Granularity Comparability
A bounded relation between reconstruction claims whose reference, predicate, Frame, temporal scope, source standard, granularity dimension, translation basis, and Loss support responsible comparison. Comparability is local and does not imply identity, mutual substitutability, or truth rank.

### Comparable with Declared Translation
A local comparison description for different but traceably translatable distinction sets. The translation rule, unmatched structures, uncertainty, and Loss remain explicit.

### Partial Comparability
A local comparison relation in which only specified predicates, segments, roles, or dimensions align. It may not be generalized to the whole source object.

### Incomparability
A positive bounded finding that current reference, Frame, predicate, time, source, dimension, or translation conditions do not support responsible comparison. Incomparability does not establish plural truth or preserve weak claims.

Primary site for comparability terms: [§19.8](../01_blocks/03_part_ii_sub.md#19-8-granularity-comparability).

### Granularity Mismatch
An apparent disagreement produced when non-aligned distinction sets are treated as though they directly affirm or deny the same bounded predicate. Mismatch can explain apparent conflict but cannot dissolve a substantive contradiction automatically.

Primary site: [§19.9](../01_blocks/03_part_ii_sub.md#19-9-granularity-mismatch).

### Lower Granularity Question
The claim-sensitive pre-operation test: “Does the additional distinction change a warranted reconstruction of the praxis-relevant structure?” It prepares relevance, Stop, or Non-Capture pressure without selecting a Chapter-25 resolution outcome.

Primary site: [§19.10](../01_blocks/03_part_ii_sub.md#19-10-the-lower-granularity-question).

### Minimal Granularity Relation
The exact eight-field conceptual declaration of source-to-target granularity change, source and target granularities, added distinction, Frame and reference preservation, expected praxeological difference, and local comparability status. It maps to the Shared Transformation Record and controlled extensions; it is not a parallel schema or operation result.

Primary site: [§19.11](../01_blocks/03_part_ii_sub.md#19-11-minimal-granularity-relation).


## Chapter 19 Provisional-Lock Terminology

### Granularity-Relation Architecture
The complete Chapter-19 declaration discipline linking a bounded source granularity to a proposed target granularity through an explicit distinction-set change, Frame and reference status, expected praxeological difference, comparability basis, and Loss.

### Coordinate Readiness
A bounded finding that the source-to-target granularity relation is sufficiently declared for Chapter-20 procedural testing. Coordinate readiness does not establish material source support, actual components, operation admissibility, or operation success.

### Chapter-19 Provisional Lock
The integrated result that Chapter 19 satisfies its Contract and local audit while remaining revisable under concrete upstream, ownership, integrity, or later dependency conflict. It does not lock SUB, execute `DECOMPOSE`, or increase authority.

Primary site: [Chapter-19 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-19-completion-boundary).

## Chapter 20 Preparation Terms

### Decomposition question

A bounded operation-leading question that identifies the source object, proposed finer distinction, current/coarser claim under test, source route, no-gain condition, and Stop condition. It is not a thematic request for more detail.

### Local operation result

An operation-specific descriptive result such as supported decomposition, heterogeneous source object, competing internal models, insufficient source support, or failed decomposition. It is not a canonical Output Class.

### Source-function effect

The post-decomposition status of the current/coarser source function, for example confirmed, refined, internally differentiated, partially preserved, rejected, or underdetermined. It is recorded separately from operation admissibility and Output Class.

### Component relation

A source-supported relation among proposed components—such as dependency, sequence, feedback, threshold, substitution, inhibition, asymmetric load, or reproduction condition—that makes the finer reconstruction relational rather than a parts list.

Primary preparation control: [`Chapter_20_Preparation_Record.md`](Chapter_20_Preparation_Record.md).

## Chapter 20 WP1 Canonical Terminology Return

### DECOMPOSE Occurrence
A controlled transformation occurrence that reconstructs an independently identifiable provisionally compressed source object as a relational organization of finer source-supported structures under declared granularity while retaining the same bounded source reference as reconstruction and test target.

Primary site: [§20.1](../01_blocks/03_part_ii_sub.md#20-1-definition).

### Decomposition Preconditions
The conjunctive and non-compensatory entry conditions for attempting `DECOMPOSE`: identifiable source, bounded insufficiency question, expected PraxisPurchase, source route, declared granularity change, Frame/reference status, source-function test target, and Loss/Stop readiness. Satisfaction does not prove operation success.

Primary site: [§20.2](../01_blocks/03_part_ii_sub.md#20-2-preconditions).

### Decomposition Question
One precise leading question that identifies the source object, finer distinction family, affected current claim/function, source route, no-gain condition, and Stop condition without containing a preferred result.

Primary site: [§20.4](../01_blocks/03_part_ii_sub.md#20-4-decomposition-question).

## Chapter 20 WP2 Canonical Terminology Return

### Expected Additional Difference
A pre-operation declaration of which warranted praxis reconstruction could change if the proposed finer distinctions and relations are source-supported, paired with an explicit no-gain condition. It is not promised discovery or an Output Class.

Primary site: [§20.5](../01_blocks/03_part_ii_sub.md#20-5-expected-additional-difference).

### Source-Support Role
A claim-specific description of how material bears on a finer component or relation, including direct support, indirect reconstruction, uncertain attribution, missing intermediate structure, rival internal model, inaccessible area, or unsupported inference. These roles are open descriptions, not a closed enum or truth score.

Primary site: [§20.6](../01_blocks/03_part_ii_sub.md#20-6-source-support).

### Established Component
A source-supported finer structure that satisfies reference, source-route, function/claim, praxeological-relevance, and relational-placement burdens within one bounded reconstruction. Establishment is local and does not imply final constituency, necessity, sufficiency, or causality.

Primary site: [§20.7](../01_blocks/03_part_ii_sub.md#20-7-component-identification).

### Internal Temporality
The source-supported sequence, duration, delay, persistence, overlap, phase, branch, or expectation-window structure required when the finer claim depends on time. It may remain partial, uncertain, or inaccessible.

Primary site: [§20.8](../01_blocks/03_part_ii_sub.md#20-8-relation-identification).

## Chapter 20 WP3 Canonical Terminology Return

### Source-Function Effect
The effect of a completed finer reconstruction on the coarser function under test. Controlled values include confirmed, refined, internally differentiated, partially preserved, rejected, and underdetermined. The effect is not an Output Class, operation result, or authority increase.

Primary site: [§20.9](../01_blocks/03_part_ii_sub.md#20-9-preservation-of-source-function).

### Local Operation Result
A bounded description of what the operation achieved, such as supported relational decomposition, heterogeneous source object, valid no-gain decomposition, failed decomposition, or competing internal models. It is not the canonical governance class.

Primary site: [§20.10](../01_blocks/03_part_ii_sub.md#20-10-decomposition-output).

### DECOMPOSE Non-Invertibility
The requirement that decomposition after composition does not restore the pre-compression information state, and recomposition after decomposition does not reproduce the source representation identically.

Primary site: [§20.11](../01_blocks/03_part_ii_sub.md#20-11-non-invertibility).

## Chapter 20 WP4 Provisional-Lock Terminology Return

Chapter 20 is provisionally locked as the primary generic procedure site for `DECOMPOSE`. The lock preserves `component`, `component relation`, `source support`, `source-function effect`, `local operation result`, `prior source-claim disposition`, and `canonical Output Class` as distinct terms. It introduces no new primitive, class, enum, or authority.

Primary site: [Chapter-20 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-20-completion-boundary).

## Chapter 21 Preparation Terminology

### Operator-Typed Occurrence Decomposition
The source-supported reconstruction of production, maintenance, variation, and failure conditions of one concrete occurrence currently typed through a PMS operator. The operator type remains unchanged and the occurrence typing remains revisable.

Preparation control: [Chapter 21 Preparation Record](Chapter_21_Preparation_Record.md).

### Production Condition
A source-supported practice, relation, temporality, Non-Event, role, rule, cost, threshold, commitment, or other finer structure that helps produce or maintain one bounded occurrence. It is not a constituent of the operator type.

### Stable Function with Internal Variation
A condition in which one coarse occurrence function remains warranted despite heterogeneous, conflicting, unequally distributed, or substitutable internal structures. Stability does not prove homogeneity or essential components.

## Chapter 21 WP1 Canonical Terminology Return

### Operator-Typed Occurrence Decomposition
Occurrence-level application of `DECOMPOSE` to a bounded source object currently typed through a PMS operator. The operation reconstructs source-supported production and maintenance conditions without treating the operator type as an empirical aggregate.

Primary site: [§21.1](../01_blocks/03_part_ii_sub.md#21-1-general-rule).

### Frame Formation Conditions
The source-supported selection, admission, exclusion, role, authority, temporal, Non-Event, routing, commitment, and interpretive structures through which one concrete Frame-typed occurrence is produced or maintained. They are not universal constituents of `□`.

Primary site: [§21.3](../01_blocks/03_part_ii_sub.md#21-3-frame-formation).

### Stable Frame Function with Internal Variation
A bounded Frame function that remains reconstructable despite heterogeneous components, conflict, changing role occupancy, exceptions, unequal maintenance work, or component substitution. Stability does not imply homogeneity.

Primary site: [§21.4](../01_blocks/03_part_ii_sub.md#21-4-frame-stability-and-internal-variation).

## Chapter 21 WP2 Canonical Terminology Return

### Attractor Reproduction Conditions
The source-supported repetition, local-friction, expectation, role, cost, Non-Event, threshold, alternative-access, and exit relations through which one concrete Attractor-typed occurrence is renewed. Repetition alone is insufficient.

Primary site: [§21.6](../01_blocks/03_part_ii_sub.md#21-6-attractor-reproduction).

### Dynamic Attractor Occurrence
A bounded Attractor-typed occurrence whose recurrent object is a transition form rather than a static state. It remains distinct from a newly composed Path/Trajectory and from a projected Attractor-function.

Primary site: [§21.7](../01_blocks/03_part_ii_sub.md#21-7-dynamic-attractor-occurrence).

### Distributed Asymmetry
One bounded Asymmetry occurrence carried across multiple source-supported local gradients whose alignment, reinforcement, substitution, offset, temporal compatibility, and shared practical relation are explicitly tested. Distribution alone does not establish one macro-Asymmetry.

Primary site: [§21.9](../01_blocks/03_part_ii_sub.md#21-9-distributed-asymmetry).

## Chapter 21 WP3 Canonical Terminology Return

### Impulse Occurrence Formation
The source-supported activating difference, directing Frame, amplifying Non-Event, temporal threshold, attenuation condition, and continuation-corridor structure through which one concrete Impulse-typed occurrence becomes operative. It is not a decomposition of `∇` or an inference of inner motive.

Primary site: [§21.10](../01_blocks/03_part_ii_sub.md#21-10-impulse-typed-occurrence).

### Binding Load Distribution
The source-supported distribution of formal commitment, continuity expectation, implementation work, revision capacity, dependency, breach exposure, and exit cost within one concrete Binding-typed occurrence. Unequal load does not erase Binding automatically and does not imply person rank.

Primary site: [§21.11](../01_blocks/03_part_ii_sub.md#21-11-binding-typed-occurrence).

### Failed Operator-Occurrence Decomposition
A failed `DECOMPOSE` occurrence in which the analyst materializes an operator type, forces finer evidence into the coarse typing, exceeds source precision, loses the reference, drifts into another operation, infers person properties, or immunizes the source typing.

Primary site: [§21.12](../01_blocks/03_part_ii_sub.md#21-12-failed-operator-occurrence-decomposition).

## Chapter 21 WP4 Provisional-Lock Return

### Operator-Occurrence Decomposition
A source-bound `DECOMPOSE` occurrence that reconstructs the production, maintenance, disturbance, and failure conditions of one concrete operator-typed occurrence while leaving the PMS operator type unchanged and the source typing revisable.

Primary site: [Chapter-21 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-21-completion-boundary).

### Representative Occurrence Family
One non-exhaustive family used to test the same generic operation under a distinct occurrence-specific evidence burden. Frame, Attractor, Asymmetry, Impulse, and Binding are representative applications, not a new enum, hierarchy, primitive set, or automatic typing catalogue.

## Chapter 22 Preparation Terminology

**Composite source entry** — bounded admission of an already-composite source object with identifiable constituents, declared boundary, constitutive relations, function under test, internal traceability, and known selection/compression/Loss limits. A source bundle, multiple typing, shared label, or co-presence does not satisfy this threshold.

**Internal composition map** — source-supported representation of components together with their relations, temporal or institutional distribution, role assignments, uncertainty, and bearing on the same composite function. It is not a parts list or causal proof.

**Component hierarchy** — claim-bound distinction among constitutive, modulating, replaceable, compensatory, and incidental elements. The hierarchy is local to the composite, Frame, function, time, and granularity; it is not an ontology.

**Dominant operator weighting** — bounded description of relative load among existing operator-typed occurrences or relations inside a composite under a declared dimension and time. It does not change Δ–Ψ dependencies or establish a numerical strength scale.

**Modulating profile** — source-side description of differences in access, threshold, temporal efficacy, persistence, cost, exposure, repair, or stabilization load inside one composite. It is neither an operator nor a person type nor a contextual target function.

**Distributed function** — a composite function carried by spatially, institutionally, or temporally separated elements under a supported coordination or dependency relation. Distribution is not aggregation.

**Composite fragmentation** — failed finer representation in which parts or details remain visible but their relation to the same source composite and tested function is lost.

Preparation control: [Chapter 22 Preparation Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP1 Canonical Terminology Return

### Composite Source Entry
Entry of an independently warranted composite into `DECOMPOSE`, requiring identifiable constituents, a declared boundary, at least one constitutive relation, a bounded function or identity claim, internal traceability, known selection/compression/Loss limits, and a Same-Reference route to finer reconstruction.

Primary site: [§22.1](../01_blocks/03_part_ii_sub.md#22-1-composite-structure-as-sub-object).

### Internal Composition Map
A source-supported relational reconstruction showing which components belong to the same composite, how they are related, and how those relations bear on the bounded composite function. It is not a parts inventory.

Primary site: [§22.2](../01_blocks/03_part_ii_sub.md#22-2-internal-composition-map).

### Claim-Bound Component Role
A local role assigned to a source-supported element relative to one composite, claim, Frame, time, and granularity. Chapter 22 WP1 distinguishes constitutive, modulating, replaceable, compensatory, and incidental roles without treating them as ontological kinds.

Primary site: [§22.3](../01_blocks/03_part_ii_sub.md#22-3-component-hierarchy).

### Dominant Operator Weighting
A qualitative, source-bound description of relative load among existing operator-typed occurrences or relations within one composite, declared by function, dimension, and temporal scope. It is not an operator score, dependency revision, person profile, or target function.

Primary site: [§22.4](../01_blocks/03_part_ii_sub.md#22-4-dominant-operator-weighting).

## Chapter 22 WP2 Canonical Terminology Return

### Modulating Profile
A bounded source-side description of how supported relations inside one composite differ along a declared dimension such as access, threshold, temporal efficacy, persistence, coordination cost, exposure, repair burden, or stabilization load. It is not an operator, composite type, person type, synthetic score, or contextual target function.

Primary site: [§22.5](../01_blocks/03_part_ii_sub.md#22-5-modulating-profiles).

### Distributed Function
A bounded composite function carried by spatially, institutionally, or temporally separated elements under a supported same-composite relation and coordination or dependency mechanism. Distribution is not aggregation or co-presence.

Primary site: [§22.6](../01_blocks/03_part_ii_sub.md#22-6-distributed-function).

### Bounded Removal Pressure
A local analytic pressure asking what function, load, relation, or identity claim changes if one supported component is removed, disabled, delayed, or made unavailable while the remaining relation map is held fixed as far as responsibly possible. It does not establish universal causality or replace Chapter 27's complete Counterfactual Component Test.

### Substitution Claim
A claim that one supported carrier can assume a bounded function from another under declared transition conditions, changed costs, burdens, access, timing, uncertainty, and Loss. Functional substitution does not imply structural identity or lossless replacement.

Primary site: [§22.7](../01_blocks/03_part_ii_sub.md#22-7-redundant-and-substitutable-components).

### Qualitative Change Threshold
A source-, function-, Frame-, and claim-bound point at which supported relation changes materially alter the bounded composite function or identity. It is not a universal percentage, score, resilience index, or operator cutoff.

### Internal Conflict Outcome
A bounded description of how source-supported internal incompatibility bears on the composite: destabilization, functional integration, suppression through asymmetry, residual persistence, or competing subpaths. These are open local descriptions, not Output Classes or a closed enum.

Primary site: [§22.8](../01_blocks/03_part_ii_sub.md#22-8-internal-conflict).

## Chapter 22 WP3 Canonical Terminology Return

### Composite Stability
A bounded claim that a declared composite reference, function, constitutive relation, role structure, access pattern, burden distribution, output, or label persists across a stated interval through source-supported mechanisms. Stability of one object does not imply stability of the others.

Primary site: [§22.9](../01_blocks/03_part_ii_sub.md#22-9-composite-stability).

### Non-Fragmenting Composite Decomposition
A finer reconstruction that keeps the source composite, boundary, constitutive relations, component roles, composition trace, inherited/new Loss, and macrofunction test target reconstructible. Detail size does not decide fragment status.

Primary site: [§22.10](../01_blocks/03_part_ii_sub.md#22-10-decomposition-of-a-composite-without-fragmentation).

## Chapter 22 WP4 Provisional-Lock Return

### Relational Composite Decomposition
A source-bound `DECOMPOSE` occurrence that opens one independently warranted composite into a finer map of constituents, constitutive relations, roles, distributed function, redundancy, conflict, stability, inherited Loss, and new Loss while preserving the same bounded composite reference as the object under test.

Primary site: [Chapter-22 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-22-completion-boundary).

### Composite Reconstructibility
The requirement that the source composite, its boundary, constitutive relations, bounded function, lineage, and Loss remain traceable through the finer map. Reconstructibility does not imply inversion of `COMPOSE`, restoration of excluded information, or immunity of the coarse composite claim.

## Chapter 23 Preparation Terminology

**Temporal source entry** — bounded admission of an independently identifiable Event-like or Non-Event source object with declared category, Frame, temporal scope, boundary, current function or expected structure, source basis, known internal structure, and decomposition reason.

**Event boundary** — claim- and Frame-bound declaration of an Event's beginning, completion, contextual margins, internal phases, and rival boundary constructions. It is not fixed by the smallest timestamp.

**Extended Event** — one bounded event-like object whose identity depends on source-supported internal phases and completion relations across a non-trivial interval. Duration alone does not establish an Extended Event.

**Event Cluster** — several local Events related under one bounded event-complex claim. A cluster is not a single Event automatically and may require a separate `COMPOSE` occurrence if formed from previously independent sources.

**Event Inflation** — multiplication of Event units through timestamp, observation, utterance, document, or micro-change density without additional praxeological purchase.

**Categorical preservation** — explicit test of whether finer reconstruction preserves, refines, splits, clusters, partially preserves, rejects, or leaves underdetermined the Event or Non-Event category of the same source reference.

**Temporal granularity drift** — finer temporal differentiation that adds timestamps or micro-changes without changing a warranted reconstruction of transition, phase, threshold, expectation, completion, source function, or Loss.

Preparation control: [Chapter 23 Preparation Record](Chapter_23_Preparation_Record.md).

## Chapter 23 WP1 Canonical Terminology Return

### Event Decomposition Entry
Entry of an independently warranted Event-like source object into `DECOMPOSE`, with declared category, Frame, coarse boundary, praxis-relevant change, source basis, existing compression, and finer-resolution question. A timestamp or record does not establish entry by itself.

Primary site: [§23.1](../01_blocks/03_part_ii_sub.md#23-1-event-decomposition).

### Event Boundary
The claim-bound temporal boundary of an Event, including beginning, completion, contextual predecessors and aftermath, interruptions or resumptions, and supported rival boundaries. It is not the smallest timestamp or the widest relevant context.

Primary site: [§23.1](../01_blocks/03_part_ii_sub.md#23-1-event-decomposition).

### Extended Event
One bounded Event whose identity depends on multiple phases and a common completion relation. Duration, sequence, or a shared topic is insufficient by itself.

Primary site: [§23.2](../01_blocks/03_part_ii_sub.md#23-2-extended-event).

### Event Cluster
A bounded temporal object containing locally distinguishable Events related through a common decision object, coordinated formation, dependency, threshold, transition, or completion environment. Opening an already warranted coarse Event into a cluster may be `DECOMPOSE`; newly selecting independent Events into a cluster requires `COMPOSE`.

Primary site: [§23.3](../01_blocks/03_part_ii_sub.md#23-3-event-cluster).

### Event Inflation
Multiplication of Event claims from timestamps, micro-changes, duplicated records, or observational units without changed praxis reconstruction.

Primary site: [§23.4](../01_blocks/03_part_ii_sub.md#23-4-event-inflation).

### Event Unit
A temporal unit justified relative to the current claim, Frame, sources, transition relevance, and source reference. No universal minimum Event unit is introduced.

Primary site: [§23.4](../01_blocks/03_part_ii_sub.md#23-4-event-inflation).

## Chapter 23 WP2 Canonical Terminology Return

### Non-Event Decomposition Entry
Entry of a bounded `Λ` source claim into `DECOMPOSE` only after expected structure, Expectation Frame, expected window or completion condition, supported non-realization, praxis difference, and Source Ceiling are declared. Missing records or mere absence do not establish entry.

Primary site: [§23.5](../01_blocks/03_part_ii_sub.md#23-5-non-event-decomposition).

### Non-Event Categorical Preservation
Preservation of the same higher-level non-realization where positive sub-events produce, stabilize, defer, fragment, or fail to overcome the warranted expected structure within its bounded window. Positive internal activity does not automatically dissolve `Λ`.

Primary site: [§23.6](../01_blocks/03_part_ii_sub.md#23-6-preserving-the-non-event-character).

### Delay Structure
A source-supported temporal relation in which an expected or prepared continuation occurs later, remains unrealized, or changes completion condition through declared mechanisms, roles, thresholds, and dependencies. Elapsed time alone and motive inference are insufficient.

Primary site: [§23.7](../01_blocks/03_part_ii_sub.md#23-7-delay-structure).

### Repeated Non-Decision
A candidate temporal form in which related decision opportunities or closure attempts repeatedly fail to produce the expected binding occurrence. It may resolve as one continuing Non-Event, several Non-Events, an Event Cluster plus higher-level Non-Event, or a broader PATH object.

Primary site: [§23.8](../01_blocks/03_part_ii_sub.md#23-8-repeated-non-decision).



## Chapter 23 WP3 Addendum — Internal Temporal Order and Temporal Non-Capture

**Internal temporal order** — A source-supported relation among phases, sub-events, delays, thresholds, interruptions, reopenings, and completion conditions inside the same bounded temporal object; it is not a timestamp list. Primary site: [§23.9](../01_blocks/03_part_ii_sub.md#23-9-internal-temporal-order).

**Multiple-clock relation** — A bounded relation among distinct temporal measures such as formal, interaction, information, authority, or consequence time. Evidence for one clock does not automatically establish another. Primary site: [§23.9](../01_blocks/03_part_ii_sub.md#23-9-internal-temporal-order).

**Temporal granularity drift** — Finer temporal distinction without changed Event boundary, phase relation, expectation, completion, praxis effect, Source-Function Effect, or Loss. Primary site: [§23.10](../01_blocks/03_part_ii_sub.md#23-10-temporal-granularity-drift).

**Temporal Non-Capture** — A bounded result where a legitimate temporal question cannot responsibly select one finer Event/Non-Event map under available sources, without rescuing the coarse claim or converting missingness into `Λ`. Primary site: [§23.11](../01_blocks/03_part_ii_sub.md#23-11-event--non-event-confusion-results-and-completion).


## Chapter 23 Provisional-Lock Note

Chapter 23 provisionally locks **temporal decomposition** as source-bound `DECOMPOSE` of Event-like and Non-Event objects through explicit category, boundary, expectation, phases, internal order, delay, multiple clocks, drift, and result-axis controls. Event, Extended Event, Event Cluster, Non-Event, Delay Structure, and Repeated Non-Decision remain revisable local source categories, not new primitives or Output Classes. Primary site: [Chapter 23](../01_blocks/03_part_ii_sub.md#23-decomposing-events-non-events-and-internal-temporal-structures).

## Chapter 24 Preparation Terminology

**PATH-source entry** — bounded admission of an independently warranted Path, Trajectory, phase, turning-point claim, branch cluster, or Path-Dependence claim with explicit reference, boundary, source category, original selection/formation rule, coarser function, inherited Loss, and decomposition reason.

**Subpath** — source-related internal Path segment with its own bounded transitions and a reconstructible relation to the same coarser Path. A temporally isolated fragment is not a subpath automatically.

**Transition cluster** — source-supported intermediate configuration and transition structure opening one coarse transition without automatically forming a new Path.

**Turning-point claim** — claim that a transition or transition cluster materially changed later alternatives, costs, bindings, Frames, or action corridors. Retrospective salience alone is insufficient.

**Rival PATH construction** — materially different source selection, periodization, boundary, Frame, or formation rule producing another Path object through `COMPOSE`, not a finer map of the same source through `DECOMPOSE`.

**Compression debt** — declared unresolved traceability burden created by inherited PATH compression. It is not a score, Output Class, or new PMS primitive.

Preparation control: [Chapter 24 Preparation Record](Chapter_24_Preparation_Record.md).

## Chapter 24 WP1 Canonical Terminology Return

### PATH-Produced Source Object
An independently warranted Path-side analytical object admitted to `DECOMPOSE` with explicit historical reference, boundary, source category, coarse function, original selection/formation rule, inherited Loss, and finer-resolution question. Raw chronology is insufficient.

Primary site: [§24.1](../01_blocks/03_part_ii_sub.md#24-1-path-objects-as-sub-objects).

### Formation Lineage
The declared relation between the original PATH selection/formation commitments and the current finer map, separating inherited selections, recovered detail, newly sourced detail, new analytical selections, and continuing exclusion, uncertainty, and irrecoverability.

Primary site: [§24.1](../01_blocks/03_part_ii_sub.md#24-1-path-objects-as-sub-objects).

### Subpath
A bounded internal course with its own configurations and transitions and a reconstructible relation to the same coarse Path or Trajectory. A temporal segment, thematic subset, or shared carrier is not a subpath automatically.

Primary site: [§24.3](../01_blocks/03_part_ii_sub.md#24-3-subpaths).

### Transition Cluster
A source-supported set of intermediate configurations and relations that opens one coarse transition while retaining its source and target configuration relation. An expanded Event list is insufficient.

Primary site: [§24.4](../01_blocks/03_part_ii_sub.md#24-4-transition-clusters).

## Chapter 24 WP2 Canonical Terminology Return

### Turning Point
A bounded transition or transition cluster whose historically traceable effects materially alter later alternatives, costs, asymmetries, bindings, action corridors, or continuation conditions. Retrospective salience alone is insufficient.

Primary site: [§24.5](../01_blocks/03_part_ii_sub.md#24-5-turning-points).

### Branch Reconstruction
Source- and window-bounded reconstruction of a historically available continuation and its realized, rejected, blocked, aborted, deferred, or lost relation to the source Path. Imaginability alone is insufficient.

Primary site: [§24.6](../01_blocks/03_part_ii_sub.md#24-6-branch-reconstruction).

### Internal Frame Change
A change of contextual relevance, access, role, expectation, or closure inside the same candidate Path or Trajectory, tested through reference and functional continuity. It is neither source replacement nor `PROJECT_AS` automatically.

Primary site: [§24.7](../01_blocks/03_part_ii_sub.md#24-7-internal-frame-changes).

### Competing Continuations
Two or more source-supported continuations from the current Path configuration with declared entry conditions, unequal accessibility, costs, exposure, binding load, horizon, and uncertainty. They are not predictions or recommendations.

Primary site: [§24.8](../01_blocks/03_part_ii_sub.md#24-8-competing-continuations).

## Chapter 24 WP3 Canonical Terminology Return

### Irrecoverable PATH Compression
Historical structure excluded, collapsed, unrecorded, destroyed, or otherwise unavailable after the source PATH `COMPOSE` occurrence and not recoverable merely through finer analysis.

Primary site: [§24.9](../01_blocks/03_part_ii_sub.md#24-9-irrecoverable-compression).

### Compression Debt
The unresolved traceability burden carried by a coarse Path or Trajectory claim where constitutive distinctions remain compressed, uncertain, or irrecoverable. Compression debt is neither a score, Output Class, primitive, nor automatic failure.

Primary site: [§24.9](../01_blocks/03_part_ii_sub.md#24-9-irrecoverable-compression).

### Path-Dependence Load
A claim-bound occurrence-level set of historical carriers through which a present structure may depend on its Path, such as `Α + Θ`, `Ω + Θ`, `Ψ + Θ`, or `Λ + Θ` profiles. It is not substance, operator fusion, determinism, or a universal score.

Primary site: [§24.10](../01_blocks/03_part_ii_sub.md#24-10-decomposition-of-path-dependence).

### Rival PATH Construction
A separately testable `COMPOSE` occurrence produced by materially different source selection, periodization, boundary, formation rule, macro-object, historical referent, or PATH question. It does not inherit the current `DECOMPOSE` result.

Primary site: [§24.11](../01_blocks/03_part_ii_sub.md#24-11-decomposition-versus-alternative-path-construction).

## Chapter 24 Provisional-Lock Terminology Return

**Path/Trajectory decomposition** — source-bound finer reconstruction of an already formed PATH object that preserves historical reference, original selection and formation lineage, coarse function, and inherited Loss while opening subpaths, transitions, branches, Frame changes, and dependence load.

**Same-Path continuity** — warranted continuity of historical referent, source boundary, original selection/formation, constitutive transition relations, coarse function, and inherited Loss across finer reconstruction. Shared dates, archives, endpoints, institutions, or labels are insufficient.

**Irrecoverable PATH compression** — source history excluded, collapsed, unrecorded, destroyed, or otherwise unavailable after PATH formation and not restored by later detail volume, graphing, schema completeness, or `DECOMPOSE`.

**Chapter-24 lock** — provisional closure of the Path/Trajectory `DECOMPOSE` method, not confirmation of any particular Path, periodization, turning point, branch, continuation, Path-Dependence claim, prediction, person property, or authority.

Primary site: [Chapter 24](../01_blocks/03_part_ii_sub.md#chapter-24-decomposing-paths-and-trajectories). Lock record: [Chapter 24 WP4](Chapter_24_Preparation_Record.md#26-wp4-execution-and-provisional-lock-record).

## Chapter 25 Preparation Terminology

**Resolution Gain** — supported finding that finer resolution changes at least one warranted praxis reconstruction for the tested claim. Gain may strengthen, narrow, correct, reduce, reject, or expose Loss in the prior claim.

**Resolution Neutrality** — valid source-supported comparison in which correct finer detail changes no warranted reconstruction for the tested claim. It is not failure, unsupported refinement, Claim Reduction, Non-Capture, or automatic Mandatory Stop.

**Resolution Drift** — growth of complexity, fragmentation, uncertainty, or inferential burden faster than relational or discriminative performance.

**Resolution Escape** — anti-immunization failure in which a burdened claim is moved to finer granularity without answering the burden, while local detail is treated as retroactive confirmation.

**Source Overreach** — finer semantic or structural precision exceeding what the declared sources support.

**Calibration Loss** — loss of stable comparison and revision conditions such that rival decompositions, thresholds, or counterevidence can no longer constrain the preferred reconstruction.

**Decomposition Fatigue** — methodological Stop marker where further opening remains possible in principle but carries no additional structural load for the current claim. It is not analyst psychology.

Preparation control: [Chapter 25 Preparation Record](Chapter_25_Preparation_Record.md).

## Chapter 25 WP1 Canonical Terminology Return

### Resolution Gain
A local SUB comparison result in which finer resolution changes at least one warranted statement about the reconstructed praxis. The change may confirm, refine, differentiate, reduce, or reject the coarse claim.

Primary site: [§25.1](../01_blocks/03_part_ii_sub.md#25-1-resolution-gain).

### Resolution Neutrality
A valid, source-supported coarse/finer comparison in which the tested warranted reconstruction remains unchanged. Neutrality is not failure, unsupported refinement, Missing Information, or Non-Capture.

Primary site: [§25.2](../01_blocks/03_part_ii_sub.md#25-2-resolution-neutrality).

### Resolution Drift
A local SUB condition in which complexity, fragmentation, or inferential load grows faster than discriminative performance, relation support, or reconstructive coherence.

Primary site: [§25.3](../01_blocks/03_part_ii_sub.md#25-3-resolution-drift).

### Resolution Escape
An anti-immunization failure in which a burdened claim is moved to another granularity or analytical coordinate and the new local detail is presented as confirmation without answering the prior burden.

Primary site: [§25.4](../01_blocks/03_part_ii_sub.md#25-4-resolution-escape).

### Warranted Revision
A controlled response to counterpressure that preserves the prior claim disposition, formulates a separate finer claim, declares its new basis, and prohibits inherited authority.

Primary site: [§25.4](../01_blocks/03_part_ii_sub.md#25-4-resolution-escape).

## Chapter 25 WP2 Canonical Terminology Return

### Detail without Purchase
A supported finer distinction that does not change the warranted reconstruction, claim disposition, source-function status, relevant Loss, uncertainty, or Stop condition for the tested claim. Lack of purchase is claim-relative rather than universal.

Primary site: [§25.5](../01_blocks/03_part_ii_sub.md#25-5-detail-without-purchase).

### Components without Coarser Function
A finer component inventory whose relation to the coarser source object or tested source function has not been reconstructed. Supported parts do not by themselves complete `DECOMPOSE`.

Primary site: [§25.6](../01_blocks/03_part_ii_sub.md#25-6-components-without-coarser-function).

### Relation Support
The source-bound warrant for a claimed relation among components, occurrences, phases, or structures. Component support, relation support, and claim support remain separate burdens.

Primary site: [§25.6](../01_blocks/03_part_ii_sub.md#25-6-components-without-coarser-function).

### Source Overreach
A condition in which the semantic, structural, temporal, causal, or categorical precision of a reconstruction exceeds the combined precision warranted by its sources.

Primary site: [§25.7](../01_blocks/03_part_ii_sub.md#25-7-source-overreach).

### Calibration Loss
Loss of stable comparison, threshold, or revision conditions such that a preferred claim can absorb counterpressure without a traceable disposition change.

Primary site: [§25.8](../01_blocks/03_part_ii_sub.md#25-8-calibration-loss).

### Open Threshold
A provisional comparison or decision threshold whose basis, uncertainty, revision conditions, rival thresholds, and Stop condition remain explicit. An open threshold is not Calibration Loss by itself.

Primary site: [§25.8](../01_blocks/03_part_ii_sub.md#25-8-calibration-loss).

## Chapter 25 WP3 Terminology Return

**Decomposition Fatigue** — claim-bound methodological marker indicating that further opening remains possible in principle but no longer carries additional warranted structural load for the present source, question, and comparison. It is not analyst psychology, permanent undecomposability, or an Output Class.

**Resolution family** — one of the six local Chapter-25 comparison results `gain`, `neutral`, `drift`, `escape`, `unsupported`, or `non_capture`. These are not a second canonical Output-Class inventory.

**Re-entry** — a new testable transformation claim after Stop, authorized only by a materially new source, claim, Frame, comparison basis, relation map, counterexample, threshold, bounded question, or relevant runtime invariant. Re-entry preserves the earlier Stop and prior claim disposition.

## Chapter 25 Provisional-Lock Terminology Return

**Resolution assessment** — claim-bound comparison of a warranted coarse reconstruction with a warranted finer reconstruction to determine Gain, Neutrality, Drift, Escape, unsupported refinement, or Non-Capture and the bounded continuation consequence.

**Bounded continuation decision** — source-, claim-, relation-, calibration-, and invariant-bound judgment that a concrete transformation may continue, should optionally stop, must stop, or may re-enter on a materially new basis; not a universal halting decision.

**Anti-immunizing re-entry** — a new testable claim or record based on materially new sources, relations, Frame, comparison basis, counterexample, threshold, source object, or relevant invariant while preserving the earlier Stop and claim disposition.

**Chapter-25 lock** — provisional closure of the resolution-assessment and bounded-continuation method, not automatic classification of any decomposition or process, proof of universal halting, runtime implementation, person judgment, or authority.

Primary site: [Chapter 25](../01_blocks/03_part_ii_sub.md#chapter-25-resolution-gain-neutrality-drift-and-escape). Lock record: [Chapter 25 WP4](Chapter_25_Preparation_Record.md#26-wp4-execution-and-provisional-lock-record).

## Chapter 26 Preparation Terminology

### Internal Constitution
The source-supported components, relations, phases, subpaths, transitions, and carrying or destabilizing structures opened while the same source object remains the explanation target. Internal constitution is tested by `DECOMPOSE`; it is not a contextual target function.

### Contextual Target Function
A bounded function asserted for an origin-typed source object within a declared target context. It requires a separate `PROJECT_AS` occurrence and never replaces the origin type.

### Recontextualization
A changed Frame, source perspective, comparison setting, question, or presentation context that alters legibility without necessarily executing `DECOMPOSE` or `PROJECT_AS`. Recontextualization becomes an operation only when a transformation claim is separately declared.

### Dual Operation
A chain in which one inquiry requires both `DECOMPOSE` and `PROJECT_AS`. Each operation occurrence retains a separate claim, Record, Loss account, result, and failure possibility.

### Invalid Collapse
The prohibited merger of internal-constitution and contextual-target-function claims, including silent mixed records, origin-type replacement, or using support for one operation as automatic support for the other.

Preparation control: [Chapter 26 Preparation Record](Chapter_26_Preparation_Record.md).

## Chapter 26 WP1 Canonical Terminology Return

### Internal-Constitution Claim
A `DECOMPOSE`-directed claim asking which finer structures and relations constitute, reproduce, maintain, interrupt, destabilize, or revise the same bounded source object. The source object remains the explanatory target.

Primary site: [§26.2](../01_blocks/03_part_ii_sub.md#26-2-sub-question).

### Target-Function Candidate
A proposed `PROJECT_AS` claim in which an origin-typed source object is retained and asserted to perform a bounded function in a declared target context. The function remains contextual and separately testable.

Primary site: [§26.3](../01_blocks/03_part_ii_sub.md#26-3-retype-question).

### Operation-Boundary Entry
The bounded declaration of source object, origin type, source function, Frame, granularity, analysis question, proposed context, proposed function, uncertainty, and Loss required before classifying an analysis as DECOMPOSE, PROJECT_AS, recontextualization, or dual-operation pressure.

Primary site: [§26.1](../01_blocks/03_part_ii_sub.md#26-1-why-the-boundary-is-difficult).

### Source Function
The bounded function or role of the source object that remains the explanation target in SUB and may be confirmed, differentiated, reduced, rejected, or left underdetermined.

Primary site: [§26.2](../01_blocks/03_part_ii_sub.md#26-2-sub-question).

## Chapter 26 WP2 Canonical Terminology Return

### Trajectory Operation Comparison
A paired operation-boundary comparison in which the same origin-typed Trajectory is first treated as an internal reconstruction source and separately as a retained source object for a bounded contextual target-function candidate. Shared evidence does not merge the claims or occurrences.

Primary site: [§26.5](../01_blocks/03_part_ii_sub.md#26-5-trajectory-decomposition-and-projection).

### Attractor-Occurrence / Attractor-Function Separation
The distinction among an Attractor-typed occurrence, its internally reconstructed recurrence structure, and a contextual Attractor-function assigned to a retained source object. Repetition of the term does not establish type or operation identity.

Primary site: [§26.6](../01_blocks/03_part_ii_sub.md#26-6-attractor-occurrence).

### Subtle Misclassification
An operation-boundary error in which decompositional vocabulary or component detail conceals a substantive contextual target-function claim.

Primary site: [§26.7](../01_blocks/03_part_ii_sub.md#26-7-subtle-misclassification).

### Reverse Misclassification
An operation-boundary error in which functional-sounding language or a new label is routed to RETYPE even though it only summarizes internal source structure and asserts no target function.

Primary site: [§26.8](../01_blocks/03_part_ii_sub.md#26-8-reverse-misclassification).

### Recontextualization
A change of Frame, perspective, question, audience, or presentation context that changes legibility without yet opening finer internal structure or asserting a bounded contextual target function.

Primary site: [§26.9](../01_blocks/03_part_ii_sub.md#26-9-sub-versus-recontextualization).

## Chapter 26 WP3 Canonical Terminology Return

**Operation-boundary decision test** — claim-segment-specific sequence distinguishing internal source reconstruction, bounded contextual function, recontextualization, dual-operation pressure, underdetermination, and invalid collapse through source, granularity, context, function, and Record conditions.

**Dual-operation chain** — ordered sequence containing distinct `DECOMPOSE` and `PROJECT_AS` occurrences with separate claims, Records, Loss, results, and failure possibilities; never a mixed fourth operation.

**Operation-boundary underdetermination** — bounded finding that available sources do not responsibly discriminate among DECOMPOSE, PROJECT_AS, recontextualization, or a separable dual-operation chain. It may lead to `non_capture` and does not authorize a compromise operation.

Primary sites: [§26.10](../01_blocks/03_part_ii_sub.md#26-10-sub-retype-decision-test), [§26.11](../01_blocks/03_part_ii_sub.md#26-11-dual-operation), and [§26.12](../01_blocks/03_part_ii_sub.md#26-12-invalid-collapse).

## Chapter 26 Provisional-Lock Terminology Return

**Operation-boundary assessment** — claim-segment-specific determination of whether an analysis opens the internal constitution of the same source object, assigns that preserved origin-typed object a bounded contextual function, merely recontextualizes it, requires a chain of both operations, or remains underdetermined.

**Recontextualization-only result** — changed Frame, question, perspective, comparison setting, or presentation that alters legibility without itself executing `DECOMPOSE` or `PROJECT_AS`.

**Dual-operation chain** — explicitly ordered sequence of separate `DECOMPOSE` and `PROJECT_AS` occurrences, each with its own claim, Record, support, Loss, result, and failure possibility; never a mixed or fourth operation.

**Chapter-26 lock** — provisional closure of the SUB/RETYPE operation-boundary method, not automatic semantic classification, completed RETYPE, target-function warrant, origin-type replacement, Graph or Reader implementation, person judgment, or authority.

Primary site: [Chapter 26](../01_blocks/03_part_ii_sub.md#chapter-26-the-boundary-between-sub-and-retype). Lock record: [Chapter 26 WP4](Chapter_26_Preparation_Record.md#chapter-26-wp4-execution-and-provisional-lock-record).

## Chapter 27 Preparation Terminology

### `Lower SUB Boundary`

**Short definition:** The local boundary below which additional distinctions, though possibly correct, do not change a warranted praxis reconstruction for the tested `DECOMPOSE` claim.

**Non-equivalences:**

- lower SUB boundary ≠ false detail;
- lower SUB boundary ≠ unsupported refinement;
- lower SUB boundary ≠ universal minimum granularity;
- lower SUB boundary ≠ automatic `failed_transformation`.

**Primary operational site:** Chapter 27 — SUB Boundary Conditions.

### `Upper SUB Boundary`

**Short definition:** The local boundary above which finer reconstruction loses reconstructible anchoring to the source object, component relations, source function, or source-supported precision.

**Non-equivalences:**

- upper SUB boundary ≠ system-wide Traceability Ceiling in full;
- upper SUB boundary ≠ high detail alone;
- upper SUB boundary ≠ source type rejection automatically;
- upper SUB boundary ≠ `non_capture` automatically.

### `Fragmentation without Reconstruction`

**Short definition:** A decomposition failure pressure in which parts or local descriptions proliferate while their relations, source reference, and coarser-function load are not reconstructibly preserved or explicitly revised.

### `Component Sensitivity Finding`

**Short definition:** A bounded result of testing whether changing, removing, delaying, disabling, or replacing a supported component would alter the reconstructed source function under a responsibly held relation map.

Prepared local findings are `constitutive`, `strongly_modulating`, `weakly_modulating`, `replaceable`, `incidental`, and `underdetermined`. They are not PMS primitives, operator types, universal causal classes, person properties, or canonical Output Classes.

### `Coarser-Function Traceability`

**Short definition:** The reconstructible relation by which finer components and relations confirm, refine, differentiate, partially preserve, reject, or leave underdetermined the bounded function attributed to the source object.

```text
source type preserved
≠ coarser function confirmed
```

Preparation control: [Chapter 27 Preparation Record](Chapter_27_Preparation_Record.md).

## Chapter 27 WP1 Canonical Terminology Return

### Lower SUB Boundary

The claim-relative point below which an additional distinction, though possibly valid and supported, changes no warranted praxis reconstruction for the tested claim.

Primary site: [§27.1](../01_blocks/03_part_ii_sub.md#27-1-lower-sub-boundary).

### Resolution without Purchase

A supported finer reconstruction that is validly comparable to the coarse reconstruction but changes no warranted praxis claim. It is a Resolution Neutrality candidate, not unsupported refinement.

Primary site: [§27.2](../01_blocks/03_part_ii_sub.md#27-2-resolution-without-purchase).

### Upper SUB Boundary

The point at which finer components, relations, precision, or object splitting cease to remain reconstructibly anchored to the source object and the coarser function under test.

Primary site: [§27.3](../01_blocks/03_part_ii_sub.md#27-3-upper-sub-boundary).

### Fragmentation without Reconstruction

A failed or underdetermined SUB condition in which components are identified but their source-related relational structure and return to the coarser object cannot be responsibly reconstructed.

Primary site: [§27.4](../01_blocks/03_part_ii_sub.md#27-4-fragmentation-without-reconstruction).

## Chapter 27 WP2 Canonical Terminology Return

### Source Ceiling — local SUB use

The finest component, relation, temporal, and functional precision that the available source basis can responsibly carry for a bounded `DECOMPOSE` claim.

Primary site: [§27.5](../01_blocks/03_part_ii_sub.md#27-5-source-ceiling).

### Counterfactual Component Test

A bounded test of whether removal, delay, deactivation, replacement, or material alteration of a supported component changes the reconstructed source function under a declared relation map.

Primary site: [§27.6](../01_blocks/03_part_ii_sub.md#27-6-counterfactual-component-test).

### Component Sensitivity

A local description of a component's constitutive, modulating, replaceable, incidental, or underdetermined load for one tested source function. It is not a primitive, score, person type, or universal causal class.

Primary site: [§27.6](../01_blocks/03_part_ii_sub.md#27-6-counterfactual-component-test).

### Coarser-Function Traceability

The ability to return every material finer finding to the source function under test and state whether that function is confirmed, refined, differentiated, partially preserved, reduced, rejected, or underdetermined.

Primary site: [§27.7](../01_blocks/03_part_ii_sub.md#27-7-coarser-function-traceability).

### Type Preservation — SUB

Maintenance of the distinction among operator type, operator occurrence, source-object type claim, and source-function claim while allowing explicit source-supported type revision.

Primary site: [§27.8](../01_blocks/03_part_ii_sub.md#27-8-type-preservation).

## Chapter 27 WP3 Canonical Terminology Return

### No Privilege of Fine Resolution

The rule that a finer reconstruction must be compared against the coarse reconstruction for the tested claim and may be better, co-equal, worse, or incomparable. Resolution depth creates no automatic truth or authority priority.

Primary site: [§27.9](../01_blocks/03_part_ii_sub.md#27-9-no-privilege-of-fine-resolution).

### SUB Stop

A bounded positive determination that further `DECOMPOSE` continuation is unnecessary (Optional Stop) or inadmissible (Mandatory Stop) for the current source object, claim, granularity relation, source basis, and relation map.

Primary site: [§27.10](../01_blocks/03_part_ii_sub.md#27-10-sub-stop-conditions).

### SUB Non-Capture

A result in which a legitimate decomposition question remains unresolved because no available granularity and relation map can responsibly carry a determinate reconstruction. It does not restore a failed coarse claim.

Primary site: [§27.11](../01_blocks/03_part_ii_sub.md#27-11-sub-non-capture).

### SUB Admissibility Test

The conjunctive local test requiring PraxisPurchase, Source Support, Source Reference, reconstructible relations, coarser-function traceability or revision, type integrity or revision, declared granularity, and a defined Stop condition.

Primary site: [§27.12](../01_blocks/03_part_ii_sub.md#27-12-sub-admissibility-test).

## Chapter 27 Provisional-Lock Terms

**Local SUB boundary procedure** — the bounded Chapter-27 application of the existing Admissibility Band to `DECOMPOSE`, combining lower-boundary PraxisPurchase, upper-boundary reconstructive traceability, Source Ceiling, Component/Relation Support, Source Reference, Coarser Function, Type Integrity, Stop, Claim Reduction, Failure, Non-Capture, and re-entry without creating new system-wide LIMITS.

**No Privilege of Fine Resolution** — the rule that finer reconstruction is compared for the tested claim rather than treated as automatically truer, more useful, or more authoritative.

Primary site: [Chapter 27 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-27-completion-boundary).

## Chapter 28 Preparation Terms

### `SUB Case Artifact Set`

**Short definition:** The linked Markdown reconstruction, schema-valid YAML Transformation Record, local audit result, and canonical Output-Class mapping required for an instantiated Chapter-28 case.

**Non-equivalences:**

- artifact set ≠ theory source;
- schema validity ≠ substantive admissibility;
- case completeness ≠ empirical truth;
- one positive case ≠ general validation of `DECOMPOSE`.

### `Lock-Critical SUB Case`

**Short definition:** A Chapter-28 case whose complete artifact set is required for the Chapter-28 and Part-II provisional-lock decision.

The minimum set covers admissible Trajectory decomposition, overfine analysis below the Relevance Floor, and SUB/RETYPE confusion. Operator-decomposition error and fragmentation without source function are additionally mandatory complete artifacts.

### `SUB Local Audit`

**Short definition:** The Chapter-28 twenty-four-question audit that tests source identity, type, granularity, components, relations, function, resolution, operation boundaries, counterfactuals, sources, Stop, Non-Capture, and authority for Part-II lock readiness.

```text
SUB Local Audit
≠ Chapter-53 integrated system audit
```

Preparation control: [Chapter 28 Preparation Record](Chapter_28_Preparation_Record.md).

## Chapter 28 WP1 Operational Use

**Positive SUB case** — one bounded occurrence- or composite-level `DECOMPOSE` test that survives source, relation, function, type, Loss, Band, operation-boundary, Stop, and governance pressure. It is a test artifact, not a new primitive, Rule, operation, or theory source.

**Case artifact set** — linked Markdown reconstruction, schema-valid YAML Transformation Record, case-local audit, canonical mapping, and Case Index registration with hashes.

## Chapter 28 WP2 Operational Use

**SUB countercase** — a bounded case that preserves source material while locating the failed, reduced, stopped, or separated transformation claim.

**Operation-confusion case** — one case packet that exposes multiple candidate claims while requiring separate operation occurrences and records; it is not a mixed operation.

## Chapter 28 WP3 Operational Use

**source-bound analogy** — bounded resemblance retained after source component or relation identity fails; final mapping pressure is `analogy_only`.

**modulator finding** — bounded occurrence-level weighting or load effect inside existing operator grammar; recurrence does not create a new operator.

**SUB lock readiness** — completion of chapter artifacts and local audits sufficient to enter the final lock pass; it is not the lock itself.

## Chapter 28 and Part II — SUB Provisional-Lock Terms

**Case-tested local SUB closure procedure** — the completed Chapters-18–28 decomposition discipline after sixteen Chapter-28 Artifact Sets, twenty-nine indexed case Records, the twenty-four-question SUB Local Audit, canonical mapping, and package controls pass.

**Part II — SUB provisional lock** — a reopenable methodological lock confirming the present `DECOMPOSE` corpus without granting fine-resolution privilege, empirical validation, target-function authority, or final STRATA completion.

```text
Part II — SUB provisional lock
≠ universal decomposability
≠ empirical truth
≠ PROJECT_AS authorization
≠ final STRATA lock
```

Primary site: [Chapter 28 and Part II completion boundary](../01_blocks/03_part_ii_sub.md#part-ii-sub-provisional-lock-boundary).
