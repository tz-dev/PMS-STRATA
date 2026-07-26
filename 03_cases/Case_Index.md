# PMS-STRATA Case Index

**Version:** 0.1.12  
**Status:** provisional Part-I- and Part-II-locked case-corpus index  
**Authority:** navigation and artifact registry only; no independent theory authority  
**Current production stage:** Foundations, PATH, and SUB are provisionally locked; RETYPE holds a bounded provisional method lock while its artifact-complete lock remains `mandatory_stop`; Pre-LIMITS Maintenance WP0–WP5 are complete and the maintenance gate has passed; Chapter 41 WP1 is next.  

```text
case index entry
≠ theory definition
≠ empirical proof
≠ automatic Output-Class decision
```

## Instantiated Cases

| Case ID | Title | Class | Operation | Local result | Canonical mapping | Lock-critical | Artifacts |
|---|---|---|---|---|---|---|---|
| `C17-ATTR-01` | Trajectory or Attractor? | `confusion_case` | `COMPOSE` | admissible single Trajectory with Attractor-function claim withheld | `admissible_with_bounded_claim` | no | [MD](markdown/C17-ATTR-01_Trajectory_or_Attractor.md) · [YAML](yaml/C17-ATTR-01_Trajectory_or_Attractor.yaml) |
| `C17-BRANCH-01` | Branching Path | `positive_case` | `COMPOSE` | admissible branching Path | `admissible` | no | [MD](markdown/C17-BRANCH-01_Branching_Path.md) · [YAML](yaml/C17-BRANCH-01_Branching_Path.yaml) |
| `C17-CHRON-01` | Chronology Presented as Path | `countercase` | `COMPOSE` | failed Path claim with retained chronology | `claim_reduction_required` | no | [MD](markdown/C17-CHRON-01_Chronology_Presented_as_Path.md) · [YAML](yaml/C17-CHRON-01_Chronology_Presented_as_Path.yaml) |
| `C17-FALSEL-01` | False Central Non-Event | `countercase` | `COMPOSE` | central Λ claim withdrawn with retained event field | `claim_reduction_required` | no | [MD](markdown/C17-FALSEL-01_False_Central_Non_Event.md) · [YAML](yaml/C17-FALSEL-01_False_Central_Non_Event.yaml) |
| `C17-HISTORY-01` | Similar End States, Different Histories | `positive_case` | `COMPOSE` | admissible dimension-specific Path-Dependence claim across similar endpoints | `admissible_with_bounded_claim` | no | [MD](markdown/C17-HISTORY-01_Similar_End_States_Different_Histories.md) · [YAML](yaml/C17-HISTORY-01_Similar_End_States_Different_Histories.yaml) |
| `C17-LAMBDA-01` | Trajectory with a Central Non-Event | `positive_case` | `COMPOSE` | admissible source-sensitive Trajectory with central Λ | `admissible` | yes | [MD](markdown/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.md) · [YAML](yaml/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.yaml) |
| `C17-LINEAR-01` | Simple Linear Path | `positive_case` | `COMPOSE` | admissible bounded Path | `admissible` | no | [MD](markdown/C17-LINEAR-01_Simple_Linear_Path.md) · [YAML](yaml/C17-LINEAR-01_Simple_Linear_Path.yaml) |
| `C17-MACRO-01` | Macro-Label without Traceable Path | `countercase` | `COMPOSE` | failed source-indifferent macro-Trajectory composition | `failed_transformation` | yes | [MD](markdown/C17-MACRO-01_Macro_Label_without_Traceable_Path.md) · [YAML](yaml/C17-MACRO-01_Macro_Label_without_Traceable_Path.yaml) |
| `C17-OMEGA-01` | Composition through Omitted Asymmetry | `countercase` | `COMPOSE` | failed Trajectory composition through omitted asymmetry | `failed_transformation` | no | [MD](markdown/C17-OMEGA-01_Composition_through_Omitted_Asymmetry.md) · [YAML](yaml/C17-OMEGA-01_Composition_through_Omitted_Asymmetry.yaml) |
| `C17-PROJ-01` | Path or Projection? | `confusion_case` | `COMPOSE` | admissible source-sensitive Trajectory with projection claim separated | `admissible_with_bounded_claim` | yes | [MD](markdown/C17-PROJ-01_Path_or_Projection.md) · [YAML](yaml/C17-PROJ-01_Path_or_Projection.yaml) |
| `C17-RES-01` | Path or Resolution Drift? | `confusion_case` | `DECOMPOSE` | resolution-neutral finer reconstruction; no new Path or stronger historical claim | `resolution_neutral` | no | [MD](markdown/C17-RES-01_Path_or_Resolution_Drift.md) · [YAML](yaml/C17-RES-01_Path_or_Resolution_Drift.yaml) |
| `C17-TEL-01` | Teleological Composition | `countercase` | `COMPOSE` | failed teleological Trajectory composition | `failed_transformation` | no | [MD](markdown/C17-TEL-01_Teleological_Composition.md) · [YAML](yaml/C17-TEL-01_Teleological_Composition.yaml) |
| `C17-WEAKPD-01` | Repeated Pattern with Weak Path Dependence | `positive_case` | `COMPOSE` | admissible repeated-pattern Path with weak order dependence | `admissible_with_bounded_claim` | no | [MD](markdown/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.md) · [YAML](yaml/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.yaml) |

| `C28-FRAME-01` | Frame-Typed Occurrence | `positive_case` | `DECOMPOSE` | admissible bounded decomposition of one Frame-typed occurrence into source-supported production and maintenance relations | `admissible_with_bounded_claim` | no | [MD](markdown/C28-FRAME-01_Frame_Typed_Occurrence.md) · [YAML](yaml/C28-FRAME-01_Frame_Typed_Occurrence.yaml) |
| `C28-ATTR-01` | Attractor-Typed Occurrence | `positive_case` | `DECOMPOSE` | admissible bounded decomposition of an Attractor-typed occurrence into recurrence-maintaining relations | `admissible_with_bounded_claim` | no | [MD](markdown/C28-ATTR-01_Attractor_Typed_Occurrence.md) · [YAML](yaml/C28-ATTR-01_Attractor_Typed_Occurrence.yaml) |
| `C28-ASYM-01` | Distributed Asymmetry | `positive_case` | `DECOMPOSE` | admissible bounded reconstruction of a distributed Asymmetry occurrence without single-center inflation | `admissible_with_bounded_claim` | no | [MD](markdown/C28-ASYM-01_Distributed_Asymmetry.md) · [YAML](yaml/C28-ASYM-01_Distributed_Asymmetry.yaml) |
| `C28-NONEVENT-01` | Structured Non-Event | `positive_case` | `DECOMPOSE` | admissible bounded decomposition of a structured Non-Event through expectation, blockage, positive sub-events, and later carryover | `admissible_with_bounded_claim` | no | [MD](markdown/C28-NONEVENT-01_Structured_Non_Event.md) · [YAML](yaml/C28-NONEVENT-01_Structured_Non_Event.yaml) |
| `C28-TRAJECTORY-01` | Admissible Trajectory Decomposition | `positive_case` | `DECOMPOSE` | admissible same-reference Trajectory decomposition with explicit subpaths, relations, residual binding, Loss, and no hidden RETYPE | `admissible` | yes | [MD](markdown/C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.md) · [YAML](yaml/C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.yaml) |
| `C28-GAIN-01` | Resolution Gain | `positive_case` | `DECOMPOSE` | Resolution Gain through source-supported differentiation of access, sequencing, binding, and repair with reduction of the broader authority-concentration claim | `admissible_with_bounded_claim` | no | [MD](markdown/C28-GAIN-01_Resolution_Gain.md) · [YAML](yaml/C28-GAIN-01_Resolution_Gain.yaml) |

| `C28-OVERFINE-01` | Overfine Analysis below the Relevance Floor | `countercase` | `DECOMPOSE` | supported microdetail adds no warranted Praxis difference; continuation below the Relevance Floor must stop while the prior adequate reconstruction remains preserved | `mandatory_stop` | yes | [MD](markdown/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.md) · [YAML](yaml/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.yaml) |
| `C28-UNSUPPORTED-01` | Unsupported Internal Structure | `countercase` | `DECOMPOSE` | the hidden internal-routing reconstruction exceeds the Source Ceiling; only the recorded event field and coarse order survive | `claim_reduction_required` | no | [MD](markdown/C28-UNSUPPORTED-01_Unsupported_Internal_Structure.md) · [YAML](yaml/C28-UNSUPPORTED-01_Unsupported_Internal_Structure.yaml) |
| `C28-OPTYPE-01` | Operator Decomposition Error | `countercase` | `DECOMPOSE` | DECOMPOSE fails because the declared source is an operator type rather than an occurrence or composite | `failed_transformation` | yes | [MD](markdown/C28-OPTYPE-01_Operator_Decomposition_Error.md) · [YAML](yaml/C28-OPTYPE-01_Operator_Decomposition_Error.yaml) |
| `C28-FRAGMENT-01` | Fragmentation without Source Function | `countercase` | `DECOMPOSE` | the attempted decomposition fragments the source into supported items without supported relations or reconstructible source-function return | `failed_transformation` | yes | [MD](markdown/C28-FRAGMENT-01_Fragmentation_without_Source_Function.md) · [YAML](yaml/C28-FRAGMENT-01_Fragmentation_without_Source_Function.yaml) |
| `C28-ESCAPE-01` | Resolution Escape | `countercase` | `DECOMPOSE` | repeated granularity change displaces rather than answers the counterexample; the finality claim remains failed and the escape route must stop | `mandatory_stop` | no | [MD](markdown/C28-ESCAPE-01_Resolution_Escape.md) · [YAML](yaml/C28-ESCAPE-01_Resolution_Escape.yaml) |
| `C28-FALSEMACRO-01` | False Macro-Asymmetry | `countercase` | `DECOMPOSE` | the macro-Asymmetry claim exceeds the supported local field; local differences survive, but coordinated macrostructure is not established | `claim_reduction_required` | no | [MD](markdown/C28-FALSEMACRO-01_False_Macro_Asymmetry.md) · [YAML](yaml/C28-FALSEMACRO-01_False_Macro_Asymmetry.yaml) |
| `C28-SUBRETYPE-01` | SUB or RETYPE? | `confusion_case` | `DECOMPOSE` | the internal Trajectory reconstruction is retained, while the audit-training calibration function is separated and not validated in this DECOMPOSE record | `partially_admissible` | yes | [MD](markdown/C28-SUBRETYPE-01_SUB_or_RETYPE.md) · [YAML](yaml/C28-SUBRETYPE-01_SUB_or_RETYPE.yaml) |
| `C28-SUBPATH-01` | SUB or New PATH? | `confusion_case` | `DECOMPOSE` | the same-source subpath reconstruction is retained, while the candidate independent sequence is separated for a future COMPOSE claim rather than absorbed into SUB | `partially_admissible` | no | [MD](markdown/C28-SUBPATH-01_SUB_or_New_PATH.md) · [YAML](yaml/C28-SUBPATH-01_SUB_or_New_PATH.yaml) |

| `C28-ANALOGY-01` | Decomposition or Analogy? | `confusion_case` | `DECOMPOSE` | the foreign-domain comparison preserves a bounded gating resemblance but does not establish source-bound decomposition; the stronger identity claim is withdrawn and the result maps to analogy_only | `analogy_only` | no | [MD](markdown/C28-ANALOGY-01_Decomposition_or_Analogy.md) · [YAML](yaml/C28-ANALOGY-01_Decomposition_or_Analogy.yaml) |
| `C28-MODULATOR-01` | Modulator or New Operator? | `confusion_case` | `DECOMPOSE` | the recurrent profile is reconstructed as a bounded modulator of existing operator-typed occurrences; the stronger claim that it constitutes a new operator is withdrawn | `claim_reduction_required` | no | [MD](markdown/C28-MODULATOR-01_Modulator_or_New_Operator.md) · [YAML](yaml/C28-MODULATOR-01_Modulator_or_New_Operator.yaml) |

## WP4 Provisional PATH-Lock Status

- five positive cases, five countercases, and three confusion cases instantiated;
- thirteen Markdown reconstructions and thirteen schema-valid Shared Transformation Records present;
- twelve-stage record audit complete in every case;
- the twenty-question integrated PATH Local Audit passes;
- complete five-part Loss, alternatives, Output mapping, Stop, Non-Capture, Claim Scope, and governance boundaries are present across the corpus;
- all three lock-critical artifacts are present: `C17-LAMBDA-01`, `C17-MACRO-01`, `C17-PROJ-01`;
- all six remaining Chapter-17 integrated duties are complete;
- Part-I lock readiness passes;
- the integrated Chapters 9–17 audit passes;
- Part I — PATH is provisionally locked;
- Chapter 18 Preparation is the next controlled step.

```text
Chapter 17 complete
+ integrated WP4 audit passed
= Part I provisionally locked

Part I provisional lock
≠ final STRATA lock
```


## Chapter 28 WP1 Positive-Set Status

- six Chapter-28 positive cases instantiated;
- six Markdown reconstructions and six schema-valid `DECOMPOSE` Records present;
- twelve-stage record audit and case-specific SUB checks pass in every WP1 case;
- Components and Relations are explicit in every valid reconstruction;
- source-function effect, Resolution Gain, prior disposition, and canonical Output Class remain separate;
- complete five-part Loss fields, alternatives, Stop conditions, and authority boundaries are present;
- the lock-critical Trajectory artifact `C28-TRAJECTORY-01` is complete;
- all eight WP1 Pressure Duties are complete;
- Chapter 28 and Part II remain unlocked;
- Chapter 28 WP2 countercases and first confusion pair are next.

```text
six positive artifacts complete
≠ Chapter 28 case corpus complete
≠ one case validates DECOMPOSE generally
≠ Part II provisionally locked
```


## Chapter 28 WP2 Countercase and Confusion Status

- six countercases and two confusion cases instantiated;
- eight Markdown reconstructions and eight schema-valid `DECOMPOSE` Records present;
- Overfine, Operator-Error, and Fragmentation complete-artifact burdens satisfied;
- Stop, Claim Reduction, Failure, and partial admissibility remain distinct;
- SUB/RETYPE and SUB/new-PATH segments require separate claims and future operation Records;
- the SUB/RETYPE artifact is instantiated but remains pending WP3 chain and integrated Local-Audit closure;
- Chapter 28 and Part II remain unlocked.

```text
WP1 + WP2 artifacts complete
≠ all Chapter-28 targets complete
≠ integrated SUB Local Audit complete
≠ Part II provisionally locked
```


## Chapter 28 WP3 Completion and Lock Readiness

- final Analogy and Modulator/New-Operator confusion artifacts instantiated;
- all sixteen Chapter-28 standalone Artifact Sets complete;
- lock-critical SUB/RETYPE chain separation completed without executing PROJECT_AS;
- integrated SUB Local Audit passed 24/24 questions;
- output mapping remains within the ten canonical classes;
- complete Loss, alternatives, Claim Ceiling, Stop, reduction, Failure, and Non-Capture boundaries checked;
- Chapter 28 and Part II are ready for WP4 but remain unlocked.

```text
WP3 lock readiness
≠ Chapter 28 lock
≠ Part II lock
```


## Chapter 28 WP4 Provisional SUB-Lock Status

- all sixteen Chapter-28 target cases and Artifact Sets are complete;
- all twenty-nine indexed case Records validate;
- all three Chapter-28 lock-critical artifacts are complete;
- Operator Error and Fragmentation complete-artifact burdens are complete;
- the twenty-four-question integrated SUB Local Audit passes;
- complete Loss, alternatives, Claim Ceiling, Stop, reduction, Failure, Non-Capture, chain, and governance boundaries remain visible;
- canonical mappings stay within the closed ten-class inventory and are not routing quotas;
- the integrated Chapters-18–28 audit passes;
- Chapter 28 is provisionally locked;
- Part II — SUB is provisionally locked;
- Chapter 29 Preparation is the next controlled step.

```text
Chapter 28 complete
+ integrated SUB audit passed
= Part II — SUB provisionally locked

Part II provisional lock
≠ final STRATA lock
≠ PROJECT_AS authorization
≠ authority increase
```

## Index Boundary

This index records artifact identity, class, operation, local result, canonical mapping, status, and ownership. It does not determine substantive case truth, select a class automatically, revise canonical prose, or grant application authority.

```yaml
governance:
  authority_inheritance: prohibited
```

Machine-readable companion: [`Case_Index.yaml`](Case_Index.yaml)
