# PMS-STRATA — Glossary

**Status:** active Reference Kernel artifact; corpus-audit synchronized 
**Repository role:** terminology core and canonical definition routing; not an independent theory or authority source 
**Authority basis:** `PMS.yaml` → `00_source/PMS-STRATA_Structure.md` → `01_blocks/*` → `05_minified/*`; formal, case, appendix, and Reader artifacts remain subordinate to their canonical owners 
**Reference Freeze duty:** open bounded duty; this artifact may be corrected for ownership, routing, duplication, and carrier consistency without broadening any claim 

---

## 1. Function and Status

This glossary fixes the canonical working vocabulary used across the seven canonical corpus Blocks. It supplies short definitions, designated primary definition sites, spelling conventions, and central non-equivalences. It does not replace canonical prose, the operator index, the operation index, the output-class index, or the appendices.

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
 - [Chapter 18](../01_blocks/03_part_ii_sub.md#chapter-18-the-provisionally-compressed-object)
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
 - [Chapter 18](../01_blocks/03_part_ii_sub.md#chapter-18-the-provisionally-compressed-object)
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
 - [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
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
 - [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
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
 - [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
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
 - [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
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
 - [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
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
 - [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
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
 - [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
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
- **Controlled local values:** `strongly_sensitive`, `partially_sensitive`, `weakly_sensitive`, `insensitive`, `underdetermined`, `untestable`
- **Legacy mapping:** `sensitive` → `strongly_sensitive`; `partially sensitive` → `partially_sensitive`; `not testable with available sources` → `untestable`
- **Central non-equivalences:**
 - Counterfactual Sensitivity ≠ causal proof
 - `untestable` ≠ automatically false
 - `insensitive` result ≠ source-dependent result

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
- **Status:** STRATA continuity view under canonical `TypeIntegrity`; not an independent Rule
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

The following compact entries were initially included to stabilize names and symbols within active canonical corpus maintenance and remain as a controlled cross-reference in the active corpus. Their detailed dependencies, provides-fields, examples, and PMS status belong in `Operator_Index.md`; `PMS.yaml` remains authoritative.

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
