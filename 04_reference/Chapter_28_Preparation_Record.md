# Chapter 28 Preparation Record

**Chapter:** 28 — SUB Cases, Countercases, and Local Audit  
**Record version:** v0.2  
**Status:** preparation gate and WP1–WP4 execution complete; Chapter 28 and Part II — SUB provisionally locked  
**Local result:** `admissible_but_provisional`  
**Source-of-truth input:** ZIP 200, Chapter 28 WP3 complete and lock-ready  
**Next controlled step:** Chapter 29 Preparation Gate — Functional Projection without Origin-Type Replacement

## 1. Preparation Status and Scope

This record prepares the closing chapter of Part II — SUB. Chapters 18–27 already define the provisionally compressed source object, granularity change, the generic `DECOMPOSE` procedure, occurrence- and composite-specific reconstruction, Event/Non-Event and PATH-source decomposition, resolution outcomes, the SUB/RETYPE operation boundary, and the complete local SUB boundary procedure. Chapter 28 does not redefine those rules. It must demonstrate that they discriminate among positive cases, countercases, and confusion cases; produce the required case artifacts; execute the twenty-four-question SUB Local Audit; map local findings to the ten canonical Output Classes; and decide whether Chapter 28 and Part II may be provisionally locked.

The governing question is:

> Can SUB distinguish warranted relational opening from overfine analysis, unsupported microstructure, operator decomposition, fragmentation, resolution escape, false macrostructure, and operation confusion while preserving source reference, Loss, Stop, Non-Capture, and canonical output discipline?

The bounded Chapter-28 architecture is:

```text
rules and boundaries from Chapters 18–27
+
case architecture with explicit source, component, relation, function, Loss, and claim fields
+
six positive cases
+
six countercases
+
four confusion cases
+
standalone Markdown and schema-valid YAML artifacts
+
case-local audits and canonical output mapping
+
twenty-four-question SUB Local Audit
→
Chapter-28 lock decision
→
Part-II SUB provisional-lock decision
```

This Preparation Gate produces no canonical §28 prose, standalone Chapter-28 case file, YAML Transformation Record, case-index entry, Appendix-M expansion, Appendix-N audit form, new operation, new Rule, new Output Class, new audit stage, schema change, component ontology, automatic case classifier, person type, recommendation, sanction, or authority mechanism.

## 2. Authority and Dependency Lock

### 2.1 Governing order

```text
PMS.yaml
→ unchanged Δ–Ψ identities, order, and dependencies

00_source/PMS-STRATA_Structure.md
→ Chapter-28 section and case blueprint

05_minified/Chapter_Contracts.md
→ binding Chapter-28 artifact, case, audit, and lock contract

05_minified/Block_Contracts.md
→ binding Part-II SUB completion gate

01_blocks/03_part_ii_sub.md
→ later canonical Chapter-28 prose after WP execution

03_cases/*
→ later case artifacts below canonical prose and without theory-source authority

04_reference/Chapter_28_Preparation_Record.md
→ production control only

07_model/*
→ structural validation without substantive case judgment
```

The cases test the theory. They do not define or revise it. A case that appears to conflict with Chapters 18–27 creates a review obligation; it does not silently replace the canonical method.

### 2.2 Hard dependencies

Chapter 28 requires:

- Foundations Chapters 0–8 and their Lock;
- Part I — PATH Lock wherever a Path or Trajectory source is used;
- Chapter 18 source-entry and compression discipline;
- Chapter 19 granularity and comparability discipline;
- Chapter 20 generic `DECOMPOSE` procedure and complete Record view;
- Chapters 21–24 family-specific decomposition rules;
- Chapter 25 resolution classification, Stop, and anti-immunization;
- Chapter 26 SUB/RETYPE, recontextualization, and dual-operation boundaries;
- Chapter 27 lower/upper boundaries, Source Ceiling, counterfactual component test, function/type traceability, and complete local admissibility test;
- the Shared Transformation Record, canonical Loss, ten Output Classes, and twelve-stage audit.

### 2.3 Protected ownership

Chapter 28 owns:

- SUB case architecture;
- the specified positive, counter, and confusion case set;
- lock-critical Chapter-28 case artifacts;
- SUB Local Audit;
- SUB-local findings and their canonical output mapping;
- Chapter-28 lock and Part-II SUB provisional-lock decision.

It references rather than redefines:

- `DECOMPOSE` — Chapter 20;
- operator-typed occurrence and composite rules — Chapters 21–22;
- Event/Non-Event and PATH-source decomposition — Chapters 23–24;
- resolution taxonomy — Chapter 25;
- SUB/RETYPE boundary — Chapter 26;
- local SUB boundaries — Chapter 27;
- system-wide audit — Chapter 53;
- full Appendix-M and Appendix-N development — later appendix production;
- RETYPE target-function theory — Chapters 29–40;
- system-wide LIMITS consolidation — Chapters 41–53.

## 3. Contract Lock

Chapter 28 is locally complete only if:

1. all required positive, counter, and confusion classes are assigned;
2. the minimum three lock-critical cases are fully instantiated;
3. operator-decomposition error and fragmentation without source function are also fully instantiated;
4. every valid decomposition includes both components and relations;
5. source-function effects and resolution outcomes remain separate axes;
6. every final case result maps to exactly one canonical Output Class;
7. each case preserves complete Loss, alternatives, claim scope, Stop/Non-Capture, and governance boundaries;
8. `DECOMPOSE`, new PATH construction, `PROJECT_AS`, analogy, and modulation remain distinguishable;
9. the twenty-four-question SUB Local Audit passes;
10. Chapter 28 and Part II are locked only after artifact, schema, index, link, fingerprint, package, and roundtrip validation.

```text
one positive case
≠ DECOMPOSE generally validated

case plausibility
≠ source support

case completeness
≠ empirical truth

local audit pass
≠ system-wide Chapter-53 audit complete
```

## 4. Definition Ownership and Redundancy Guard

Chapter 28 may operationalize and test earlier definitions, but it must not re-derive them. Each case must cite the controlling chapter instead of creating a competing definition of component, relation, granularity, source function, resolution result, Source Ceiling, Stop, Non-Capture, or operation identity.

The following collapses are prohibited:

```text
operator type
→ decomposable source object

component list
→ relational reconstruction

finer detail
→ stronger truth

source function effect
→ canonical Output Class automatically

resolution result
→ source function effect automatically

confusion case
→ permission to mix operations

case artifact
→ theory source

formal validation
→ semantic validation
```

## 5. SUB Case Architecture

Every Chapter-28 case must expose a stable minimum view:

```yaml
sub_case:
  case_id:
  case_class:
  title:
  governing_claim:
  claim_scope:
  claim_ceiling:
  source_transformation_record:
  source_object:
  source_origin_type:
  source_frame:
  source_granularity:
  target_granularity:
  decomposition_question:
  expected_additional_praxis_difference:
  source_basis:
  components:
  component_relations:
  source_reference_status:
  coarser_function_status:
  type_integrity_status:
  resolution_result:
  operation_boundary_status:
  counterfactual_sensitivity:
  loss:
    preserved:
    compressed:
    excluded:
    uncertain:
    irrecoverable:
  alternatives:
  local_audit_result:
  canonical_output_mapping:
  stop_or_non_capture_status:
  governance_boundary:
```

This is a case wrapper and explanatory view, not a parallel transformation schema. Each YAML artifact must validate against `07_model/Transformation_Record.schema.json`; case-specific fields belong only in existing controlled extension carriers where necessary.

```text
case wrapper
≠ fourth schema
```

## 6. Case Classes

### 6.1 Positive case

A positive case demonstrates that a bounded finer reconstruction survives source, component, relation, reference, function, type, Loss, Band, operation-boundary, and governance pressure.

```text
positive case
≠ maximum-strength claim
```

A positive case may map to `admissible_with_bounded_claim` or `admissible_but_provisional` rather than `admissible`.

### 6.2 Countercase

A countercase begins from a plausible but inadmissible, unsupported, overfine, mis-typed, fragmented, or immunizing decomposition and identifies the exact gate that fails.

```text
countercase
≠ caricature
```

Its value lies in discriminating Claim Reduction, Failure, Mandatory Stop, and Non-Capture rather than merely displaying an obvious mistake.

### 6.3 Confusion case

A confusion case holds neighboring interpretations open long enough to determine whether the claim is `DECOMPOSE`, a new `COMPOSE`, a later `PROJECT_AS`, recontextualization, analogy, modulation, Failure, Stop, or Non-Capture.

```text
confusion case
≠ mixed-operation permission
```

## 7. Artifact Contract

Every fully instantiated Chapter-28 case requires four linked layers:

1. **Markdown reconstruction** — source and claim boundary, case narrative, components, relations, function/type effects, resolution result, Loss, alternatives, audit, output mapping, Stop/Non-Capture, and governance boundary;
2. **schema-valid YAML Transformation Record** — exact operation grammar, source/target declarations, admissibility, result, Loss, alternatives, and governance;
3. **case-local audit result** — the twelve-stage record audit plus case-specific SUB checks;
4. **canonical output mapping** — exactly one of the ten closed Output Classes with reasoned mapping.

Production must also update:

```text
03_cases/Case_Index.md
03_cases/Case_Index.yaml
```

The indexes record identity, class, operation, local result, canonical mapping, artifact status, hashes, audit status, lock-critical status, and ownership. They remain navigation and registry artifacts only.

No case is counted as instantiated until both files exist, YAML and schema validation pass, the local audit is recorded, cross-links resolve, hashes are registered, and the canonical mapping is valid.

## 8. Lock-Critical Artifact Set

At least these three cases must be complete before Chapter 28 or Part II may lock:

1. **Admissible Trajectory Decomposition** — a PATH-produced source object is opened into subpaths, transitions, turning points, competing continuations, and inherited Loss while the same source reference remains traceable;
2. **Overfine Analysis below the Relevance Floor** — many supported details produce no additional praxis difference and continuation reaches a bounded Mandatory Stop;
3. **SUB versus RETYPE Confusion** — internal reconstruction and a proposed contextual target function are separated into distinct claim segments and, where both are executed, distinct operation Records.

The operator-decomposition error and fragmentation-without-source-function countercases are also mandatory full artifacts even though the numeric lock-critical minimum is three.

The Preparation Gate assigns all sixteen Chapter-28 case classes as standalone artifact targets. It does not report any of them as produced.

## 9. Positive Case Set — WP1

WP1 owns §§28.1–28.7 and must instantiate:

### 9.1 Frame-Typed Occurrence

A stable macro-Frame is reconstructed through internal selection, exclusion, role differentiation, reproduction work, and variation without decomposing the Frame operator type or requiring internal homogeneity.

### 9.2 Attractor-Typed Occurrence

A recurrent occurrence is opened into internal Frames, Non-Events, friction changes, expectation stabilization, alternative costs, and maintenance conditions. The Attractor occurrence claim may be preserved, refined, reduced, or rejected; no higher-level Attractor-function is assigned.

### 9.3 Distributed Asymmetry

Multiple local `Ω`-typed relations, roles, resources, and temporal reinforcement are tested for whether they jointly carry one bounded macro-asymmetry. Local inequality does not automatically establish coordinated or sedimented macrostructure.

### 9.4 Structured Non-Event

An expected non-occurrence is reconstructed through delays, blocked transitions, role shifts, information bottlenecks, and positive sub-events while preserving or revising the `Λ` claim without Event Inflation.

### 9.5 Trajectory Decomposition

A PATH-produced source is opened into subpaths, transition clusters, turning points, branches, competing continuations, Frame changes, Path-Dependence load, and inherited/current Loss. Same-Path and rival-PATH pressure remain explicit.

### 9.6 Resolution Gain

A finer reconstruction changes a warranted claim through newly supported roles, relations, costs, binding, alternatives, or source-function effects. Gain must be demonstrated by changed reconstruction, not by added detail alone.

## 10. Countercase Set — WP2

WP2 owns §§28.8–28.13 and must instantiate:

### 10.1 Overfine Analysis

Supported detail accumulates without changing the tested claim. The Relevance Floor is crossed and continuation must stop without declaring the detail false.

### 10.2 Unsupported Internal Structure

Plausible components or relations exceed the source basis. Semantic precision is reduced to the strongest supported claim; invented completion is prohibited.

### 10.3 Operator Decomposition Error

A Δ–Ψ operator type is treated as a material aggregate or confused with one of its typed occurrences. The category error must fail and stop before downstream person, causal, or authority inference.

### 10.4 Fragmentation without Source Function

Parts are enumerated without supported relations or reconstructible return to the source object and coarser function. Weaker component findings may survive while the stronger decomposition fails.

### 10.5 Resolution Escape

A burdened coarse claim changes granularity repeatedly to evade the unresolved counterexample. The earlier disposition remains preserved and the escape route receives Mandatory-Stop pressure.

### 10.6 False Macro-Asymmetry

Local differences are projected upward without coordinated, relational, or sedimented macrostructure. The result may be a failed decomposition, a reduced local finding, or a separately testable future projection—not an automatic macroclaim.

## 11. Confusion Case Set — WP2 and WP3

### 11.1 SUB or RETYPE?

A Trajectory is internally opened while also being proposed as a Frame- or calibration-function in another context. The internal reconstruction belongs to `DECOMPOSE`; the contextual function requires a separate `PROJECT_AS` occurrence and cannot inherit success from SUB.

### 11.2 SUB or New PATH?

Finer structures may expose either the same PATH source under greater resolution or a rival PATH construction requiring a new `COMPOSE` Record. Shared source material does not decide object identity.

### 11.3 Decomposition or Analogy?

A foreign-domain model may illuminate structure without preserving source-bound component and relation warrant. Where only similarity survives, the result maps toward `analogy_only`, not successful SUB.

### 11.4 Modulator or New Operator?

A recurrent weighting profile may alter the behavior of existing operator-typed occurrences without becoming a new PMS operator. The case must preserve operator-type integrity and prevent type inflation.

## 12. Operation and Chain Discipline

Each Chapter-28 case has one primary operation Record. Confusion cases may expose more than one operation candidate, but no Record may contain a mixed operation.

Relevant chain pressure includes:

```text
COMPOSE source object
→ DECOMPOSE occurrence

DECOMPOSE finding
→ possible new COMPOSE claim

DECOMPOSE finding
→ possible later PROJECT_AS claim
```

Every executed link requires a distinct claim, Record, source/target declaration, Loss structure, admissibility result, Output Class, and Stop/Non-Capture route. Chapter 28 may classify a later RETYPE candidate without prematurely establishing its target function.

```text
success of prior COMPOSE
≠ success of DECOMPOSE

success of DECOMPOSE
≠ success of later COMPOSE or PROJECT_AS

shared source history
≠ shared Loss or result
```

## 13. Loss, Alternatives, Claim Boundary, and Governance

No Chapter-28 artifact may omit canonical Loss:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

Each case must also state materially relevant alternatives or explain why no distinct alternative can be supported. An empty alternatives field does not prove absence of alternatives; an empty Loss field does not establish a lossless reconstruction.

Each case must declare:

- the exact tested claim;
- its scope and Claim Ceiling;
- what stronger claims are excluded;
- what weaker findings survive reduction or failure;
- which uncertainty remains;
- the Stop or re-entry condition;
- the prohibition on person typing, legitimacy, recommendation, sanction, irreversible labeling, and authority inheritance.

## 14. Local Findings and Canonical Output Mapping

Chapter 28 may use explanatory SUB-local findings, but only the ten canonical Output Classes may serve as final mapped classes.

| SUB-local finding | Canonical mapping pressure |
| --- | --- |
| admissible decomposition | `admissible`, `admissible_with_bounded_claim`, or `admissible_but_provisional` |
| source function confirmed, refined, or internally differentiated | normally bounded/provisional admissibility according to support and Loss |
| source function partially preserved or reduced | `partially_admissible` or `claim_reduction_required` |
| source function rejected | `claim_reduction_required` or `failed_transformation`, depending on surviving findings |
| supported no-change | `resolution_neutral` |
| competing supported decompositions | `admissible_but_provisional`, `partially_admissible`, or `non_capture`, according to capture status |
| unsupported decomposition | `claim_reduction_required`, `failed_transformation`, or `mandatory_stop` |
| resolution drift or escape | usually `mandatory_stop`, with weaker findings preserved where warranted |
| analogy without source-bound reconstruction | `analogy_only` |
| adequate single capture unavailable | `non_capture` |

This table is not an automatic routing engine. Source-function effect, resolution result, prior claim disposition, and canonical Output Class remain separate axes.

```text
local result label
≠ eleventh Output Class
```

## 15. SUB Local Audit

Chapter 28 must execute the twenty-four questions assigned in the Structure:

1. source object is uniquely identified;
2. origin type is declared;
3. an occurrence or composite—not a base operator—is decomposed;
4. granularity change is declared;
5. Frame continuity or change is marked;
6. decomposition question is precise;
7. expected additional difference is stated;
8. sources carry the finer structure;
9. components and relations are separated and jointly reconstructed;
10. source function remains reconstructible or explicitly revised;
11. internal heterogeneity is shown without dissolving the object;
12. the reconstruction has praxeological purchase;
13. the Relevance Floor is respected;
14. Resolution Neutrality is named where applicable;
15. Resolution Drift is excluded or classified;
16. counterevidence is not displaced to finer granularity;
17. SUB remains separate from RETYPE;
18. SUB remains separate from rival PATH composition;
19. modulation is not promoted to a new operator;
20. the Counterfactual Component Test is applied where material;
21. source and calibration limits are visible;
22. a Stop condition is declared;
23. Non-Capture remains possible;
24. no additional authority is generated.

The integrated audit must also verify artifact completeness, Markdown/YAML cross-links, schema validity, index consistency, canonical Output-Class membership, case hashes, exact operation grammar, Loss completeness, alternatives, and absence of hidden authority inheritance.

This local audit does not replace Chapter 53. It tests SUB as a completed Part against its own contract.

## 16. Stop, Claim Reduction, Failure, and Non-Capture

`mandatory_stop` applies where continuation would require operator decomposition, source-gap completion, unsupported relation or causal inference, granularity escape, hidden RETYPE, hidden new PATH construction, person typing, legitimacy, recommendation, sanction, irreversible classification, or authority inheritance.

`claim_reduction_required` preserves the strongest source-supported weaker finding while withdrawing the stronger case claim.

`failed_transformation` applies where the attempted decomposition cannot preserve or explicitly revise source reference, relation structure, function traceability, type integrity, or operation identity.

`non_capture` remains available where multiple source-supported decompositions or object identities cannot be responsibly discriminated and no single map can be selected without false precision.

```text
failed_transformation
≠ mandatory_stop
≠ claim_reduction_required
≠ non_capture
```

## 17. Chapter-28 and Part-II Lock Boundary

Chapter 28 may be provisionally locked only if:

- all sixteen specified case classes are represented in canonical prose;
- all sixteen planned standalone Markdown/YAML artifact sets exist and are registered;
- at least the three lock-critical sets are complete;
- operator-decomposition error and fragmentation-without-source-function artifacts are complete;
- all valid cases contain components and relations;
- all YAML records validate;
- each case has a local audit and exactly one canonical mapping;
- the twenty-four-question SUB Local Audit passes;
- all twenty-four Chapter-28 Pressure Duties occur exactly once in canonical prose;
- References and Formal Model are synchronized;
- case indexes, links, hashes, fingerprints, ZIP CRC, and byte roundtrip pass.

Part II — SUB may be provisionally locked only after the integrated Chapters 18–28 audit confirms:

- operator types remain untouched;
- source reference and coarser-function traceability are retained or explicitly revised;
- finer resolution has no automatic privilege;
- Gain, Neutrality, Drift, and Escape remain discriminable;
- Source Ceiling, Stop, Claim Reduction, Failure, and Non-Capture remain available;
- SUB remains distinct from new PATH and `PROJECT_AS`;
- no failed claim is immunized by granularity change;
- no case or formal artifact creates authority.

```text
Chapter 28 complete
+ integrated SUB Local Audit pass
+ artifact and package integrity pass
→ Part II provisionally locked

Part II provisional lock
≠ final STRATA lock
≠ empirical validation
≠ RETYPE completed
≠ LIMITS consolidated
```

## 18. Downstream Handoffs

A successful Chapter-28 and SUB lock supplies RETYPE with tested finer source traces, explicit source-function effects, origin-type and operation-boundary findings, Loss, Failure, Stop, and Non-Capture records. It supplies LIMITS with concrete source, relevance, traceability, anti-immunization, and authority pressure. It supplies later integrated cases with registered DECOMPOSE artifacts.

No Chapter-28 result automatically authorizes a `PROJECT_AS` target function. No case mapping grants application authority. Appendix M and Appendix N remain later presentational and audit-form migrations, not theory sources.

## 19. Work-Package Plan

### WP1 — §§28.1–28.7: Case Architecture and Positive Case Set

- establish the canonical case architecture and artifact rule;
- instantiate six positive cases in chapter prose;
- produce six linked Markdown/YAML/audit/mapping artifact sets;
- complete the admissible Trajectory lock-critical artifact;
- initialize Chapter-28 case-index synchronization;
- preserve Components, Relations, Source Function, Loss, alternatives, and Claim Ceiling in every case.

### WP2 — §§28.8–28.15: Countercases and First Confusion Pair

- instantiate six countercases;
- instantiate SUB/RETYPE and SUB/new-PATH confusion cases;
- produce eight linked artifact sets;
- complete the overfine lock-critical case plus mandatory operator-error and fragmentation artifacts;
- classify unsupported structure, escape, false macro-asymmetry, and operation confusion without category collapse.

### WP3 — §§28.16–28.20: Remaining Confusion Cases, Local Audit, Outputs, and Closing

- instantiate Analogy and Modulator/New-Operator confusion cases;
- produce the final two linked artifact sets;
- complete the SUB/RETYPE lock-critical artifact and any separate-record burden;
- execute the twenty-four-question SUB Local Audit;
- integrate Loss, alternatives, Stop, Claim Reduction, Failure, Non-Capture, output mapping, Case Index, and Closing Statement;
- decide Chapter-28 and Part-II lock readiness without performing the final lock pass.

### WP4 — Integrated Chapter-28 and Part-II Lock Pass

Run chapter-contract, block-contract, case-class, artifact, schema, component/relation, source-function, resolution, operation-boundary, chain, Loss, alternatives, output-mapping, Stop/Non-Capture, Duty, local-audit, index, link, fingerprint, package, CRC, and roundtrip audits. Provisionally lock Chapter 28 and Part II only if every completion condition passes.

## 20. Pressure-Duty Architecture

### WP1 duties

- `C28-ARCH-01` — canonical SUB case architecture and non-parallel case wrapper;
- `C28-ARTIFACT-01` — four-layer artifact contract, indexing, validation, and hash burden;
- `C28-FRAME-01` — Frame-typed occurrence positive case;
- `C28-ATTR-01` — Attractor-typed occurrence positive case;
- `C28-ASYM-01` — distributed Asymmetry positive case;
- `C28-NONEVENT-01` — structured Non-Event positive case;
- `C28-TRAJECTORY-01` — Trajectory decomposition positive and lock-critical case;
- `C28-GAIN-01` — Resolution Gain positive case.

### WP2 duties

- `C28-OVERFINE-01` — overfine analysis and Relevance-Floor Stop countercase;
- `C28-UNSUPPORTED-01` — unsupported internal structure and Claim-Reduction countercase;
- `C28-OPTYPE-01` — operator-decomposition category-error countercase;
- `C28-FRAGMENT-01` — fragmentation without source-function reconstruction countercase;
- `C28-ESCAPE-01` — Resolution Escape and anti-immunization countercase;
- `C28-FALSEMACRO-01` — false macro-Asymmetry countercase;
- `C28-SUBRETYPE-01` — SUB/RETYPE confusion and lock-critical record-separation case;
- `C28-SUBPATH-01` — SUB/new-PATH confusion and operation-chain separation case.

### WP3 duties

- `C28-ANALOGY-01` — source-bound decomposition versus analogy confusion case;
- `C28-MODULATOR-01` — modulator versus new-operator confusion case;
- `C28-LOCALAUDIT-01` — twenty-four-question integrated SUB Local Audit;
- `C28-MAPPING-01` — local-finding to canonical Output-Class mapping without automation;
- `C28-LOSSALT-01` — complete Loss, alternatives, Claim Ceiling, and surviving-findings audit;
- `C28-STOPNC-01` — Stop, Claim Reduction, Failure, and Non-Capture separation;
- `C28-CHAIN-01` — separate claims, Records, Loss, and results for operation-chain pressure;
- `C28-LOCK-01` — Chapter-28 and Part-II lock-readiness decision and Chapter-29 handoff.

The twenty-four duties are preparation controls. They become canonical only when instantiated exactly once in Chapter-28 prose. Case artifacts may not be reported as complete before their files, records, audits, mappings, indexes, and hashes exist.

## 21. Formal-Model Architecture

No schema change is required at the Preparation Gate. Existing artifacts already provide:

- the three-operation registry;
- `DECOMPOSE` source, granularity, component, relation, source-function, Loss, Stop, and result fields;
- ten canonical Output Classes;
- twelve audit stages;
- Shared Transformation Record schema validation;
- case templates and Chapter-17 artifact precedent;
- case indexes;
- decision branches for description/DECOMPOSE, new PATH, RETYPE, analogy, Stop, and Non-Capture pressure.

The Formal Model may validate:

- artifact existence and path registration;
- YAML parseability and schema conformance;
- exact operation names;
- complete five-part Loss;
- canonical Output-Class membership;
- local-audit field presence;
- case-index counts and hashes;
- Pressure-Duty exact counts;
- closed operation, Rule, class, and audit-stage inventories;
- cross-links, fingerprints, and package integrity.

It may not decide:

- actual components or relations;
- empirical source sufficiency;
- causal load or component constitutiveness;
- correct source function or origin type;
- correct operation in a genuinely ambiguous semantic case;
- final canonical mapping without substantive reasoning;
- person responsibility, legitimacy, recommendation, sanction, or authority.

## 22. Preparation-Gate Audit Checklist

- [x] Chapter 28 remains the case, Local-Audit, output-mapping, and SUB-lock chapter.
- [x] Definitions from Chapters 18–27 are referenced rather than re-derived.
- [x] Six positive, six counter, and four confusion cases are assigned.
- [x] All sixteen case classes are assigned standalone artifact targets.
- [x] Three lock-critical artifacts are designated.
- [x] Operator-error and fragmentation artifacts are additionally mandatory.
- [x] Components and relations are required in every valid decomposition.
- [x] Markdown, YAML, local audit, and canonical mapping are all required.
- [x] Complete Loss, alternatives, Claim Ceiling, and governance boundaries are required.
- [x] Local findings remain separate from canonical Output Classes.
- [x] Each final Record receives exactly one canonical class.
- [x] Source-function effect, resolution result, claim disposition, and Output Class remain separate.
- [x] Confusion cases do not permit mixed-operation Records.
- [x] New PATH and RETYPE pressure require separate claims and Records where executed.
- [x] Operator types remain non-decomposable.
- [x] Resolution Escape preserves prior claim disposition.
- [x] Stop, Claim Reduction, Failure, and Non-Capture remain distinct.
- [x] The twenty-four-question SUB Local Audit is fixed.
- [x] Twenty-four preparation duties are assigned across WP1–WP3.
- [x] Chapter-53 integrated-audit ownership remains protected.
- [x] Appendix M/N production is not pre-empted.
- [x] No canonical §28 prose or Chapter-28 case artifact is prematurely produced.
- [x] No new Rule, operation, Output Class, audit stage, schema, score, or authority mechanism is created.
- [x] Reader, Graph, runtime, person, legitimacy, and authority boundaries remain intact.

## 23. Completion Test for the Preparation Gate

The Preparation Gate passes because:

1. Chapter and Block Contracts are explicit;
2. the case architecture and artifact contract are fixed;
3. all sixteen case classes are assigned;
4. the minimum lock-critical and additionally mandatory artifacts are designated;
5. local findings and canonical mappings remain separate;
6. operation and chain boundaries are explicit;
7. the twenty-four-question SUB Local Audit is fixed;
8. Stop, Claim Reduction, Failure, and Non-Capture remain available;
9. twenty-four duties are assigned exactly once;
10. existing Formal-Model and case infrastructure is sufficient;
11. Chapter 28 and Part II remain unlocked until actual execution and WP4 audit.

Preparation result:

```text
admissible_but_provisional
```

The provisionality preserves pressure from actual case production, artifact/schema/index validation, local audit, output mapping, Chapter-28 and Part-II lock, RETYPE, LIMITS, integrated cases, appendices, Reference Freeze, Corpus Audit, Model Finalization, derivatives, Reader, Graph, and runtime work.

## 24. Immediate Controlled Step

```text
Chapter 28 — WP1
→ §§28.1–28.7
→ Case Architecture
→ six positive cases
→ six Markdown/YAML/audit/mapping artifact sets
→ admissible Trajectory lock-critical artifact
→ Case Index synchronization
```

## 25. WP1 Execution Record

**Execution version:** v0.1.149  
**Source-of-truth input:** ZIP 197  
**Result:** `admissible_but_provisional`  
**Canonical prose:** §§28.1–28.7 produced  
**Positive artifact sets:** 6/6 produced, schema-validated, locally audited, mapped, indexed, and hashed  

Produced cases:
- `C28-FRAME-01` — `admissible_with_bounded_claim`; MD `C28-FRAME-01_Frame_Typed_Occurrence.md`; YAML `C28-FRAME-01_Frame_Typed_Occurrence.yaml`; MD SHA-256 `ec61d94ab8b5a9b3b9871dcc51775ae9ec1b747462f4d25326d3dec79632ae74`; YAML SHA-256 `5f09d409716fd92789a6abcec31952dac3bf84acd02d7ca42d81e7a16c81c861`.
- `C28-ATTR-01` — `admissible_with_bounded_claim`; MD `C28-ATTR-01_Attractor_Typed_Occurrence.md`; YAML `C28-ATTR-01_Attractor_Typed_Occurrence.yaml`; MD SHA-256 `ad1199560287a6a202cdc82f18f4a23c2b0b1f1ad3c8b52131d397e63274efca`; YAML SHA-256 `47c75874610b2e49c2b9d4dddc2b6750192ec30abd31611df4f9be276939a2ee`.
- `C28-ASYM-01` — `admissible_with_bounded_claim`; MD `C28-ASYM-01_Distributed_Asymmetry.md`; YAML `C28-ASYM-01_Distributed_Asymmetry.yaml`; MD SHA-256 `7e8af108d24fdbfd6857587f4f7060a9e6ccc2f06e436be89330ffb59b576977`; YAML SHA-256 `7cf052374cd0a709b45e82187b546d20339f3534b624d5d5cfaa9181484c2ee2`.
- `C28-NONEVENT-01` — `admissible_with_bounded_claim`; MD `C28-NONEVENT-01_Structured_Non_Event.md`; YAML `C28-NONEVENT-01_Structured_Non_Event.yaml`; MD SHA-256 `86967ae9399f6118be4c45b6d0f6d60c5f29c498df1a306a2ed95c90068d83de`; YAML SHA-256 `f3122db8caa57bb60dbf8ce8b9744bc18985705c570293d8274362a8cf32e5bf`.
- `C28-TRAJECTORY-01` — `admissible`; MD `C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.md`; YAML `C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.yaml`; MD SHA-256 `f2dd6103885af8dadb17c2ae7526d7f2f212822200f2d7378b6801f0bf6ac1f8`; YAML SHA-256 `35b06f5cf0a26d7f6acdd9c3b98d908bca2d9292e4fe6c13d52e6847c12d50fc`.
- `C28-GAIN-01` — `admissible_with_bounded_claim`; MD `C28-GAIN-01_Resolution_Gain.md`; YAML `C28-GAIN-01_Resolution_Gain.yaml`; MD SHA-256 `7082f6ab9734ef8ec33dcf1192c44ee3cbb5dd9711850da77b0eb12731fa78c3`; YAML SHA-256 `d999bbf21e124dd53adb5d1b3f97e4f250b98018becbee2f18d557595271c2b0`.

WP1 establishes the case wrapper, four-layer artifact contract, all six positive cases, and the lock-critical admissible Trajectory case. It does not produce or pre-classify the WP2/WP3 countercases and confusion cases, does not execute the integrated twenty-four-question Local Audit, and does not lock Chapter 28 or Part II.

Next controlled step: **Chapter 28 WP2 — §§28.8–28.15**.

## 26. WP2 Execution Record

**Execution version:** v0.1.150  
**Source-of-truth input:** ZIP 198  
**Result:** `admissible_but_provisional`  
**Canonical prose:** §§28.8–28.15 produced  
**Artifact sets:** 8/8 produced, schema-validated, locally audited, mapped, indexed, and hashed  

Produced cases:
- `C28-OVERFINE-01` — `mandatory_stop`; MD `C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.md`; YAML `C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.yaml`; MD SHA-256 `5e815279223af4f0d1dcef01f544467616002a5e1cf3951fb43263895c764da8`; YAML SHA-256 `534eebf5d2b65091e048427fe3153d66d6039e6f32ed10c1807c5ba637ab26c2`.
- `C28-UNSUPPORTED-01` — `claim_reduction_required`; MD `C28-UNSUPPORTED-01_Unsupported_Internal_Structure.md`; YAML `C28-UNSUPPORTED-01_Unsupported_Internal_Structure.yaml`; MD SHA-256 `a8fe9b9c3da05bd1aa29498ba101be1b79be9a0769bf7ef1ca35bf31170062fc`; YAML SHA-256 `5aa430ec7395e4134a15b289283efc46486cb98c4a8530b24d79616e2258a89e`.
- `C28-OPTYPE-01` — `failed_transformation`; MD `C28-OPTYPE-01_Operator_Decomposition_Error.md`; YAML `C28-OPTYPE-01_Operator_Decomposition_Error.yaml`; MD SHA-256 `42d04026172d2f3a2197f586614c3a250cdb447cb69769e83772b100d8b6082d`; YAML SHA-256 `637c048280a255bb31adee9f6973b5761808df928dc77cfeca68d8d77b52b133`.
- `C28-FRAGMENT-01` — `failed_transformation`; MD `C28-FRAGMENT-01_Fragmentation_without_Source_Function.md`; YAML `C28-FRAGMENT-01_Fragmentation_without_Source_Function.yaml`; MD SHA-256 `87c7bb815a99d21f2d47fe216cb11bfdee6652c1bf61172160e76fb9056fee6c`; YAML SHA-256 `8202c6cca5c9fa26282a12c9d90fdc10d051d7fb45dccabfa6324098668dda9a`.
- `C28-ESCAPE-01` — `mandatory_stop`; MD `C28-ESCAPE-01_Resolution_Escape.md`; YAML `C28-ESCAPE-01_Resolution_Escape.yaml`; MD SHA-256 `fcf84fedab86ea4d95d08e35f54d1f2795f728c202a1f31ae0a73de83c8198c5`; YAML SHA-256 `488d961693c2c7693ab6897673eca95d03d6103ae03f87db1d10b0cc2b9a07cf`.
- `C28-FALSEMACRO-01` — `claim_reduction_required`; MD `C28-FALSEMACRO-01_False_Macro_Asymmetry.md`; YAML `C28-FALSEMACRO-01_False_Macro_Asymmetry.yaml`; MD SHA-256 `224fdddc1ff307df472d9b1ddcec5c912bee0658098d1f44dcdd61566492b355`; YAML SHA-256 `4e157c74de9d94215bf2b699ba655bd943509d92c46cce2b9c833d19ebdbea41`.
- `C28-SUBRETYPE-01` — `partially_admissible`; MD `C28-SUBRETYPE-01_SUB_or_RETYPE.md`; YAML `C28-SUBRETYPE-01_SUB_or_RETYPE.yaml`; MD SHA-256 `e6ccfcca591aa09ce579f5a3cca9536eeb6355028ecd3400fdeebefb853c6b73`; YAML SHA-256 `3e41b78a905876b9c83fc92339a3058c3cb24cad1fa116507eaa706b4cbfedd4`.
- `C28-SUBPATH-01` — `partially_admissible`; MD `C28-SUBPATH-01_SUB_or_New_PATH.md`; YAML `C28-SUBPATH-01_SUB_or_New_PATH.yaml`; MD SHA-256 `e654884be0b6153235d0c7549f19f0d2db9e9325bda25a1290087e4e30679405`; YAML SHA-256 `c7499990e769246a7305f53cc240566b11643b03e55980c7803d16b4a1fd3036`.

WP2 completes all six countercases and the first confusion pair. Overfine, Operator-Error, and Fragmentation complete-artifact burdens are satisfied. SUB/RETYPE and SUB/new-PATH are segmented without mixed records. The SUB/RETYPE lock-critical artifact remains pending WP3 chain-separation and integrated Local-Audit closure.

Next controlled step: **Chapter 28 WP3 — §§28.16–28.20**.

## 27. WP3 Execution Record

**Execution version:** v0.1.151  
**Source-of-truth input:** ZIP 199  
**Result:** `admissible_but_provisional`  
**Canonical prose:** §§28.16–28.20 produced  
**New artifact sets:** 2/2 produced, schema-validated, locally audited, mapped, indexed, and hashed  
**Integrated SUB Local Audit:** 24/24 passed  
**Lock readiness:** ready for WP4; Chapter 28 and Part II not yet locked  

Produced cases:
- `C28-ANALOGY-01` — `analogy_only`; MD `C28-ANALOGY-01_Decomposition_or_Analogy.md`; YAML `C28-ANALOGY-01_Decomposition_or_Analogy.yaml`; MD SHA-256 `16d521df798f48de6e1ae57c86d8d240bbea03b6b3e37fb30cb6ed5e07be6f05`; YAML SHA-256 `33789ddddcf166443edd793b85a5250644ac1c22133b7684b0612459d1df0231`.
- `C28-MODULATOR-01` — `claim_reduction_required`; MD `C28-MODULATOR-01_Modulator_or_New_Operator.md`; YAML `C28-MODULATOR-01_Modulator_or_New_Operator.yaml`; MD SHA-256 `a10c5973cca06a09fd04a5d104cf9bf6c092dac6cfe8c197c5257879cdbfe36c`; YAML SHA-256 `571dda08065be44f56bf675bd39288d7c4e80c7141db9edbf960a3f0e8045e4c`.

The lock-critical `C28-SUBRETYPE-01` artifact now records completed chain separation and integrated Local-Audit closure without executing or validating PROJECT_AS. All sixteen target cases are represented in canonical prose and standalone artifacts.

Next controlled step: **Chapter 28 WP4 integrated Chapter-28 and Part-II lock pass**.

## 28. WP4 Integrated Chapter-28 and Part-II Provisional-Lock Record

**Execution version:** v0.1.152  
**Source-of-truth input:** ZIP 200  
**Chapter result:** `admissible_but_provisional`  
**Chapter-28 lock:** provisionally locked  
**Part-II — SUB lock:** provisionally locked  
**Next controlled step:** Chapter 29 Preparation Gate — Functional Projection without Origin-Type Replacement

### 28.1 Integrated scope

WP4 audits Chapter 28 and the complete Chapters-18–28 SUB chain as one bounded Part. The audit covers:

- the Chapter-28 and Part-II Contracts;
- all 135 numbered SUB sections and 256 chapter-local Pressure Duties across Chapters 18–28;
- all eleven chapter completion boundaries;
- six positive, six counter, and four confusion targets in Chapter 28;
- sixteen linked Markdown/YAML/audit/mapping Chapter-28 Artifact Sets;
- all twenty-nine indexed case Records, including the retained Part-I corpus;
- components and relations in every valid decomposition;
- Source Reference, Coarser-Function Traceability, Source Ceiling, Type Integrity, resolution classification, operation boundaries, Loss, alternatives, Stop, Non-Capture, and anti-immunization;
- the twenty-four-question integrated SUB Local Audit;
- canonical Output-Class membership without automatic semantic routing;
- Case Index identity, paths, hashes, links, and lock status;
- Reference Kernel and Formal Model synchronization;
- package, CRC, and byte-roundtrip integrity;
- Chapter-29/RETYPE, LIMITS, Chapter-53, Appendix-M/N, Reader, Graph, runtime, person, governance, and authority ownership boundaries.

### 28.2 Integrated repairs

The canonical method and all sixteen case Artifact Sets required no substantive repair. WP4 performs only integrations valid after the full audit:

1. the Chapter-28 opening now names the complete §§28.1–28.20 architecture;
2. §28.20 now records the actual Chapter-28 and Part-II provisional lock rather than lock readiness;
3. the WP3 completion boundary is replaced by the integrated Chapter-28 and Part-II completion boundary;
4. Case Index status and inventory now record the completed SUB lock;
5. README, Reference Kernel, Admissibility Rules, root manifest, and next-step pointers now hand off to Chapter 29 Preparation;
6. no case mapping, operation, source claim, Loss statement, or local audit answer is rewritten to obtain the lock.

### 28.3 Twenty-four-control integrated lock audit

- [x] Chapter 28 satisfies its Chapter Contract without re-deriving Chapters 18–27.
- [x] Part II satisfies the SUB Block Contract across Chapters 18–28.
- [x] All twenty Chapter-28 sections are present exactly once.
- [x] All twenty-four Chapter-28 Pressure Duties occur exactly once.
- [x] All sixteen specified Chapter-28 target cases are represented in canonical prose.
- [x] All sixteen Chapter-28 standalone Artifact Sets exist in Markdown and YAML.
- [x] All three lock-critical sets are complete.
- [x] Operator Error and Fragmentation complete-artifact burdens are complete.
- [x] All twenty-nine indexed Transformation Records validate against the retained schema.
- [x] Every valid decomposition reconstructs components and relations together.
- [x] Source-function effect, resolution result, prior disposition, and Output Class remain separate.
- [x] Operator types remain untouched and no new operator or fourth operation appears.
- [x] Fine resolution receives no automatic truth, causal, practical, or authority privilege.
- [x] Source Ceiling and calibration limits remain explicit and non-compensable.
- [x] SUB remains distinct from rival PATH construction and PROJECT_AS.
- [x] Every operation-chain pressure uses separate claims and Records where executed.
- [x] Stop, Claim Reduction, Failure, and Non-Capture remain non-equivalent.
- [x] Resolution Escape and re-entry preserve earlier Failure, Stop, disposition, and Loss.
- [x] Complete five-part Loss and alternatives remain present in all Chapter-28 Artifact Sets.
- [x] The twenty-four-question integrated SUB Local Audit passes 24/24.
- [x] Case Index identity, paths, mappings, statuses, and SHA-256 hashes match actual artifacts.
- [x] Reference, Formal-Model, closed-inventory, fingerprint, and relative-link checks pass.
- [x] ZIP CRC and byte-identical package roundtrip pass.
- [x] Chapter-29/RETYPE and later LIMITS/audit ownership remain protected; authority inheritance remains prohibited.

### 28.4 Integrated result

The integrated Chapter-28 and Part-II result is:

```text
admissible_but_provisional
```

Chapter 28 and Part II — SUB are provisionally locked. The lock confirms a complete, case-tested, locally audited decomposition discipline under the present Contracts and source authority. It does not turn the synthetic cases into empirical validation, make fine resolution privileged, close `non_capture`, execute `PROJECT_AS`, complete RETYPE or LIMITS, replace the Chapter-53 integrated audit, or increase application authority.

```text
Chapter 28 provisionally locked
+ Part II — SUB provisionally locked
≠ final STRATA lock
≠ every source object decomposable
≠ every ambiguity captured
≠ target function assigned
≠ authority inherited
```

### 28.5 Reopening and handoff

Reopening requires a concrete PMS/Contract conflict, source/claim/type/operation boundary defect, case artifact or schema defect, incorrect canonical mapping, incomplete Loss or alternatives, broken Local Audit result, Reference or Formal-Model inconsistency, fingerprint/link/hash/package defect, or a later RETYPE/LIMITS/integrated-audit dependency conflict. Preference for additional detail, cases, graph density, stronger claims, fewer visible losses, or automated routing is insufficient.

```text
Part II — SUB provisional lock
→ Chapter 29 Preparation Gate
→ Functional Projection without Origin-Type Replacement
```

