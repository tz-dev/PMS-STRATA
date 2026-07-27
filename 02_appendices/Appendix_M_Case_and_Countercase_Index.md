# Appendix M — Case and Countercase Index

**Status:** substantive bounded provisional completion  
**Authority:** publishable navigation and comparison layer only; no independent theory, evidence, or adjudication authority  
**Primary owners:** `03_cases/Case_Index.md`, `03_cases/Case_Index.yaml`, `03_cases/Case_Artifact_Pairing.csv`  
**Current inventory:** 59 paired operation Records, 59 same-basename Markdown companions, 10 shared package narratives

## M.1 Purpose and boundary

Appendix M provides a stable human-readable route into the instantiated PMS-STRATA case corpus. It does not reproduce full case narratives, recompute a route, rank cases, or turn one fixture into precedent. The local YAML Record remains the structured carrier for one operation occurrence; its same-basename Markdown companion remains the readable account of that same occurrence; a package narrative is used only where several distinct occurrences share a source field, comparison, continuity problem, or chain handoff.

```text
case resemblance ≠ automatic adjudication
index entry ≠ theory source
package narrative ≠ merged operation Record
coverage role ≠ authority rank
```

The index records what the current corpus contains. It does not claim that the corpus exhausts every future case family, every domain, or every possible chain. New cases require new Records, current sources, and a fresh audit.

## M.2 Artifact model

```text
59 YAML operation Records
↔ 59 exact Markdown companions
+ 10 multi-record package narratives
+ Case_Index.md / Case_Index.yaml / Case_Artifact_Pairing.csv
```

| Artifact | Unit represented | May contain several occurrences? | Adjudicative role |
|---|---|---:|---|
| YAML Record | one delimited operation occurrence | no | stores the complete structured audit and selected route |
| Markdown companion | the same occurrence as its paired YAML | no | explains the Record without creating a second claim |
| Package narrative | shared source, comparison, continuity, or chain context | yes | preserves relations among separate Records; never merges local results |
| Case Index | registry and navigation | yes | no new adjudication |

## M.3 Corpus inventory

| Axis | Distribution |
|---|---|
| Case class | 30 positive · 16 countercase · 13 confusion |
| Operation | 16 COMPOSE · 25 DECOMPOSE · 18 PROJECT_AS |
| Lock-critical flag | 21 yes · 38 no |
| Direct Output-Class coverage | 10/10 canonical classes |
| Minimum operation-chain coverage | 6/6 required chain families |
| Pairing | 59/59 YAML ↔ Markdown |

### M.3.1 Operation × case-class matrix

| Operation | Positive | Countercase | Confusion | Total |
|---|---:|---:|---:|---:|
| `COMPOSE` | 9 | 5 | 2 | 16 |
| `DECOMPOSE` | 11 | 6 | 8 | 25 |
| `PROJECT_AS` | 10 | 5 | 3 | 18 |

### M.3.2 Output-Class coverage

| Canonical Output Class | Count | Instantiated cases |
|---|---:|---|
| `admissible` | 4 | `C17-BRANCH-01` · `C17-LAMBDA-01` · `C17-LINEAR-01` · `C28-TRAJECTORY-01` |
| `admissible_with_bounded_claim` | 26 | `C17-ATTR-01` · `C17-HISTORY-01` · `C17-PROJ-01` · `C17-WEAKPD-01` · `C28-FRAME-01` · `C28-ATTR-01` · `C28-ASYM-01` · `C28-NONEVENT-01` · `C28-GAIN-01` · `C40-P1` · `C40-P2` · `C40-P3` · `C47-CP1A` · `C47-CP1B` · `C54-CD1A` · `C54-CD1B` · `C54-DC1A` · `C54-DC1B` · `C54-DP1A` · `C54-DP1B` · `C54-PD1B` · `C35-A1` · `C50-FP1B` · `C50-FP1C` · `C50-FP1D` · `C51-RE1` |
| `admissible_but_provisional` | 3 | `C40-P7F` · `C40-P7G` · `C49-CAL1` |
| `resolution_neutral` | 1 | `C17-RES-01` |
| `analogy_only` | 2 | `C28-ANALOGY-01` · `C40-X6` |
| `partially_admissible` | 2 | `C28-SUBRETYPE-01` · `C28-SUBPATH-01` |
| `claim_reduction_required` | 6 | `C17-CHRON-01` · `C17-FALSEL-01` · `C28-UNSUPPORTED-01` · `C28-FALSEMACRO-01` · `C28-MODULATOR-01` · `C53-CPD1C` |
| `mandatory_stop` | 3 | `C28-OVERFINE-01` · `C28-ESCAPE-01` · `C50-FP1X` |
| `failed_transformation` | 11 | `C17-MACRO-01` · `C17-OMEGA-01` · `C17-TEL-01` · `C28-OPTYPE-01` · `C28-FRAGMENT-01` · `C40-N3` · `C40-N7` · `C47-CP1C` · `C38-N1` · `C38-X3` · `C50-FP1A` |
| `non_capture` | 1 | `C52-NC1` |

Direct coverage means that at least one routed case Record selects the class. It does not establish class frequency, desirability, severity, or rank.

## M.4 Complete Record index

The source/target column is a compressed orientation aid. The linked Record remains authoritative for the actual claim, source trace, target, Loss, audit, alternatives, and route.

### M.4.1 PATH / Chapter 17

| ID and title | Class | Operation | Output | Source → target summary | Coverage role | Artifacts |
|---|---|---|---|---|---|---|
| `C17-ATTR-01` — Trajectory or Attractor? | `confusion_case` | `COMPOSE` | `admissible_with_bounded_claim` | A maintenance history with two connected cycles, partial repair, residual backlog, and changed continuation costs. → Bounded synthetic trajectory for C17-ATTR-01: Trajectory or Attractor?. | Chapter 17 | [MD](../03_cases/markdown/C17-ATTR-01_Trajectory_or_Attractor.md) · [YAML](../03_cases/yaml/C17-ATTR-01_Trajectory_or_Attractor.yaml) |
| `C17-BRANCH-01` — Branching Path | `positive_case` | `COMPOSE` | `admissible` | Typed source set containing the synthetic migration Branch Point, realized and rejected continuations, and later… → Bounded synthetic path for C17-BRANCH-01: Branching Path. | Chapter 17 | [MD](../03_cases/markdown/C17-BRANCH-01_Branching_Path.md) · [YAML](../03_cases/yaml/C17-BRANCH-01_Branching_Path.yaml) |
| `C17-CHRON-01` — Chronology Presented as Path | `countercase` | `COMPOSE` | `claim_reduction_required` | Four dated status-update events with directly declared temporal order. → Purported implementation Path formed from the four dated updates. | Chapter 17 | [MD](../03_cases/markdown/C17-CHRON-01_Chronology_Presented_as_Path.md) · [YAML](../03_cases/yaml/C17-CHRON-01_Chronology_Presented_as_Path.yaml) |
| `C17-FALSEL-01` — False Central Non-Event | `countercase` | `COMPOSE` | `claim_reduction_required` | Three positive events and one undocumented interval in a review-and-escalation episode. → Purported escalation Trajectory centered on an unsupported expected review Non-Event. | Chapter 17 | [MD](../03_cases/markdown/C17-FALSEL-01_False_Central_Non_Event.md) · [YAML](../03_cases/yaml/C17-FALSEL-01_False_Central_Non_Event.yaml) |
| `C17-HISTORY-01` — Similar End States, Different Histories | `positive_case` | `COMPOSE` | `admissible_with_bounded_claim` | Typed paired source set containing two parallel unit histories, formally similar endpoints, and present… → Bounded synthetic comparative path-dependence object for C17-HISTORY-01: Similar End States, Different Histories. | Chapter 17 | [MD](../03_cases/markdown/C17-HISTORY-01_Similar_End_States_Different_Histories.md) · [YAML](../03_cases/yaml/C17-HISTORY-01_Similar_End_States_Different_Histories.yaml) |
| `C17-LAMBDA-01` — Trajectory with a Central Non-Event | `positive_case` | `COMPOSE` | `admissible` | Typed source set containing the baseline configuration, central review Non-Event structure, positive sub-events,… → Bounded synthetic trajectory for C17-LAMBDA-01: Trajectory with a Central Non-Event. | Chapter 17 · lock-critical | [MD](../03_cases/markdown/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.md) · [YAML](../03_cases/yaml/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.yaml) |
| `C17-LINEAR-01` — Simple Linear Path | `positive_case` | `COMPOSE` | `admissible` | Typed source set containing the synthetic intake, verification, authorization, and activation structures. → Bounded synthetic path for C17-LINEAR-01: Simple Linear Path. | Chapter 17 | [MD](../03_cases/markdown/C17-LINEAR-01_Simple_Linear_Path.md) · [YAML](../03_cases/yaml/C17-LINEAR-01_Simple_Linear_Path.yaml) |
| `C17-MACRO-01` — Macro-Label without Traceable Path | `countercase` | `COMPOSE` | `failed_transformation` | A heterogeneous twelve-year regional source field with branch, Λ, reversal, fallback, and repair load. → Purported progressive national modernization Trajectory covering Y1–Y12. | Chapter 17 · lock-critical | [MD](../03_cases/markdown/C17-MACRO-01_Macro_Label_without_Traceable_Path.md) · [YAML](../03_cases/yaml/C17-MACRO-01_Macro_Label_without_Traceable_Path.yaml) |
| `C17-OMEGA-01` — Composition through Omitted Asymmetry | `countercase` | `COMPOSE` | `failed_transformation` | A two-track implementation field with shared milestones and unequal access, exposure, exit, and repair load. → Purported uniform rollout Trajectory defined by shared milestones while omitting unequal practical load. | Chapter 17 | [MD](../03_cases/markdown/C17-OMEGA-01_Composition_through_Omitted_Asymmetry.md) · [YAML](../03_cases/yaml/C17-OMEGA-01_Composition_through_Omitted_Asymmetry.yaml) |
| `C17-PROJ-01` — Path or Projection? | `confusion_case` | `COMPOSE` | `admissible_with_bounded_claim` | A service-coordination history with review-mediated change, repeated rotation, redistributed burden, and residual… → Bounded synthetic trajectory for C17-PROJ-01: Path or Projection?. | Chapter 17 · lock-critical | [MD](../03_cases/markdown/C17-PROJ-01_Path_or_Projection.md) · [YAML](../03_cases/yaml/C17-PROJ-01_Path_or_Projection.yaml) |
| `C17-RES-01` — Path or Resolution Drift? | `confusion_case` | `DECOMPOSE` | `resolution_neutral` | One prior warranted three-transition service Path treated as a provisionally compressed composite for the… → A finer relational reconstruction of the same service Path with hourly distinctions retained and no material… | Chapter 17 | [MD](../03_cases/markdown/C17-RES-01_Path_or_Resolution_Drift.md) · [YAML](../03_cases/yaml/C17-RES-01_Path_or_Resolution_Drift.yaml) |
| `C17-TEL-01` — Teleological Composition | `countercase` | `COMPOSE` | `failed_transformation` | Heterogeneous pilot outcomes, a federated branch, central selection, and later adoption. → Purported inevitable centralized-development Trajectory from pilots to adoption. | Chapter 17 | [MD](../03_cases/markdown/C17-TEL-01_Teleological_Composition.md) · [YAML](../03_cases/yaml/C17-TEL-01_Teleological_Composition.yaml) |
| `C17-WEAKPD-01` — Repeated Pattern with Weak Path Dependence | `positive_case` | `COMPOSE` | `admissible_with_bounded_claim` | Typed source set containing eight cycle declarations, current scheduling rule, role access, queue state, and… → Bounded synthetic repeated-pattern path with weak dependence for C17-WEAKPD-01: Repeated Pattern with Weak Path… | Chapter 17 | [MD](../03_cases/markdown/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.md) · [YAML](../03_cases/yaml/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.yaml) |

### M.4.2 SUB / Chapter 28

| ID and title | Class | Operation | Output | Source → target summary | Coverage role | Artifacts |
|---|---|---|---|---|---|---|
| `C28-FRAME-01` — Frame-Typed Occurrence | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | one bounded intake-review Frame occurrence whose coarse function is coordinated admissibility of requests. → admissible bounded decomposition of one Frame-typed occurrence into source-supported production and maintenance… | Chapter 28 | [MD](../03_cases/markdown/C28-FRAME-01_Frame_Typed_Occurrence.md) · [YAML](../03_cases/yaml/C28-FRAME-01_Frame_Typed_Occurrence.yaml) |
| `C28-ATTR-01` — Attractor-Typed Occurrence | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | one recurring workaround configuration typed as an Attractor occurrence. → admissible bounded decomposition of an Attractor-typed occurrence into recurrence-maintaining relations. | Chapter 28 | [MD](../03_cases/markdown/C28-ATTR-01_Attractor_Typed_Occurrence.md) · [YAML](../03_cases/yaml/C28-ATTR-01_Attractor_Typed_Occurrence.yaml) |
| `C28-ASYM-01` — Distributed Asymmetry | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | one distributed workload-and-access Asymmetry occurrence across three roles and two decision windows. → admissible bounded reconstruction of a distributed Asymmetry occurrence without single-center inflation. | Chapter 28 | [MD](../03_cases/markdown/C28-ASYM-01_Distributed_Asymmetry.md) · [YAML](../03_cases/yaml/C28-ASYM-01_Distributed_Asymmetry.yaml) |
| `C28-NONEVENT-01` — Structured Non-Event | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | one expected review that did not occur within a declared window despite positive preparation events. → admissible bounded decomposition of a structured Non-Event through expectation, blockage, positive sub-events,… | Chapter 28 | [MD](../03_cases/markdown/C28-NONEVENT-01_Structured_Non_Event.md) · [YAML](../03_cases/yaml/C28-NONEVENT-01_Structured_Non_Event.yaml) |
| `C28-TRAJECTORY-01` — Admissible Trajectory Decomposition | `positive_case` | `DECOMPOSE` | `admissible` | one previously warranted review-governance Trajectory from intake through formal closure, residual binding, and… → admissible same-reference Trajectory decomposition with explicit subpaths, relations, residual binding, Loss, and… | Chapter 28 · lock-critical | [MD](../03_cases/markdown/C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.md) · [YAML](../03_cases/yaml/C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.yaml) |
| `C28-GAIN-01` — Resolution Gain | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | one coarse occurrence previously summarized as authority concentration. → Resolution Gain through source-supported differentiation of access, sequencing, binding, and repair with… | Chapter 28 | [MD](../03_cases/markdown/C28-GAIN-01_Resolution_Gain.md) · [YAML](../03_cases/yaml/C28-GAIN-01_Resolution_Gain.yaml) |
| `C28-OVERFINE-01` — Overfine Analysis below the Relevance Floor | `countercase` | `DECOMPOSE` | `mandatory_stop` | one already adequate review-occurrence reconstruction whose relevant access, threshold, closure, and repair… → supported microdetail adds no warranted Praxis difference; continuation below the Relevance Floor must stop while… | Chapter 28 · lock-critical | [MD](../03_cases/markdown/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.md) · [YAML](../03_cases/yaml/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.yaml) |
| `C28-UNSUPPORTED-01` — Unsupported Internal Structure | `countercase` | `DECOMPOSE` | `claim_reduction_required` | one coordination occurrence with directly recorded entry, review, and closure events but no source-supported… → the hidden internal-routing reconstruction exceeds the Source Ceiling; only the recorded event field and coarse… | Chapter 28 | [MD](../03_cases/markdown/C28-UNSUPPORTED-01_Unsupported_Internal_Structure.md) · [YAML](../03_cases/yaml/C28-UNSUPPORTED-01_Unsupported_Internal_Structure.yaml) |
| `C28-OPTYPE-01` — Operator Decomposition Error | `countercase` | `DECOMPOSE` | `failed_transformation` | the canonical Frame operator type Δ–Ψ treated as though it were a material occurrence with detachable internal… → DECOMPOSE fails because the declared source is an operator type rather than an occurrence or composite. | Chapter 28 · lock-critical | [MD](../03_cases/markdown/C28-OPTYPE-01_Operator_Decomposition_Error.md) · [YAML](../03_cases/yaml/C28-OPTYPE-01_Operator_Decomposition_Error.yaml) |
| `C28-FRAGMENT-01` — Fragmentation without Source Function | `countercase` | `DECOMPOSE` | `failed_transformation` | one service occurrence for which several isolated artifacts are recorded but their internal relations and return… → the attempted decomposition fragments the source into supported items without supported relations or… | Chapter 28 · lock-critical | [MD](../03_cases/markdown/C28-FRAGMENT-01_Fragmentation_without_Source_Function.md) · [YAML](../03_cases/yaml/C28-FRAGMENT-01_Fragmentation_without_Source_Function.yaml) |
| `C28-ESCAPE-01` — Resolution Escape | `countercase` | `DECOMPOSE` | `mandatory_stop` | one closure occurrence whose earlier claim that closure ended reconsideration was already defeated by… → repeated granularity change displaces rather than answers the counterexample; the finality claim remains failed… | Chapter 28 | [MD](../03_cases/markdown/C28-ESCAPE-01_Resolution_Escape.md) · [YAML](../03_cases/yaml/C28-ESCAPE-01_Resolution_Escape.yaml) |
| `C28-FALSEMACRO-01` — False Macro-Asymmetry | `countercase` | `DECOMPOSE` | `claim_reduction_required` | three bounded local sites with different access delays and repair costs but no source-supported coordinated or… → the macro-Asymmetry claim exceeds the supported local field; local differences survive, but coordinated… | Chapter 28 | [MD](../03_cases/markdown/C28-FALSEMACRO-01_False_Macro_Asymmetry.md) · [YAML](../03_cases/yaml/C28-FALSEMACRO-01_False_Macro_Asymmetry.yaml) |
| `C28-SUBRETYPE-01` — SUB or RETYPE? | `confusion_case` | `DECOMPOSE` | `partially_admissible` | one review-governance Trajectory internally opened into closure, residual binding, and reopening while also being… → the internal Trajectory reconstruction is retained, while the audit-training calibration function is separated… | Chapter 28 · lock-critical | [MD](../03_cases/markdown/C28-SUBRETYPE-01_SUB_or_RETYPE.md) · [YAML](../03_cases/yaml/C28-SUBRETYPE-01_SUB_or_RETYPE.yaml) |
| `C28-SUBPATH-01` — SUB or New PATH? | `confusion_case` | `DECOMPOSE` | `partially_admissible` | one previously composed Trajectory whose finer source packet preserves one internal subpath but also exposes a… → the same-source subpath reconstruction is retained, while the candidate independent sequence is separated for a… | Chapter 28 | [MD](../03_cases/markdown/C28-SUBPATH-01_SUB_or_New_PATH.md) · [YAML](../03_cases/yaml/C28-SUBPATH-01_SUB_or_New_PATH.yaml) |
| `C28-ANALOGY-01` — Decomposition or Analogy? | `confusion_case` | `DECOMPOSE` | `analogy_only` | one bounded coordination occurrence compared with a foreign-domain hydraulic-network model whose resemblance does… → the foreign-domain comparison preserves a bounded gating resemblance but does not establish source-bound… | Chapter 28 | [MD](../03_cases/markdown/C28-ANALOGY-01_Decomposition_or_Analogy.md) · [YAML](../03_cases/yaml/C28-ANALOGY-01_Decomposition_or_Analogy.yaml) |
| `C28-MODULATOR-01` — Modulator or New Operator? | `confusion_case` | `DECOMPOSE` | `claim_reduction_required` | one recurrent weighting profile that changes threshold salience and repair burden across several Frame- and… → the recurrent profile is reconstructed as a bounded modulator of existing operator-typed occurrences; the… | Chapter 28 | [MD](../03_cases/markdown/C28-MODULATOR-01_Modulator_or_New_Operator.md) · [YAML](../03_cases/yaml/C28-MODULATOR-01_Modulator_or_New_Operator.yaml) |

### M.4.3 RETYPE / Chapters 35, 38, and 40

| ID and title | Class | Operation | Output | Source → target summary | Coverage role | Artifacts |
|---|---|---|---|---|---|---|
| `C40-P1` — Trajectory as Bounded Frame-Function | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | The bounded Q0–Q5 workload-review Trajectory with central Non-Event instantiated in C17-LAMBDA-01. → A derived contextual view in which composite.c17-lambda-01 performs one bounded historical frame-function for… | Chapter 40 · lock-critical | [MD](../03_cases/markdown/C40-P1_Trajectory_as_Bounded_Frame_Function.md) · [YAML](../03_cases/yaml/C40-P1_Trajectory_as_Bounded_Frame_Function.yaml) |
| `C40-P2` — Trajectory as Macro-Event | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | The bounded Q0–Q5 workload-review Trajectory with central Non-Event instantiated in C17-LAMBDA-01. → A derived contextual view in which composite.c17-lambda-01 performs one bounded non-punctualized Macro-Event… | Chapter 40 | [MD](../03_cases/markdown/C40-P2_Trajectory_as_Macro_Event.md) · [YAML](../03_cases/yaml/C40-P2_Trajectory_as_Macro_Event.yaml) |
| `C40-P3` — Recurrent Trajectory Form as Attractor-Function | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | Bounded synthetic recurrent transition-form composite R3 reconstructed across three independently warranted… → Bounded later transition and reopening configuration in C3 whose route accessibility, role expectations, resource… | Chapter 40 | [MD](../03_cases/markdown/C40-P3_Recurrent_Trajectory_Form_as_Attractor_Function.md) · [YAML](../03_cases/yaml/C40-P3_Recurrent_Trajectory_Form_as_Attractor_Function.yaml) |
| `C40-N3` — PROJECT_AS Label-Substitution Failure | `countercase` | `PROJECT_AS` | `failed_transformation` | The bounded service-activation Path instantiated and retained by C17-LINEAR-01. → Attempted contextual view in which composite.c17-linear-01 is labeled as an eligibility-gate function in R1… | Chapter 40 · lock-critical | [MD](../03_cases/markdown/C40-N3_PROJECT_AS_Label_Substitution_Failure.md) · [YAML](../03_cases/yaml/C40-N3_PROJECT_AS_Label_Substitution_Failure.yaml) |
| `C40-X6` — Projection versus Structural Analogy | `confusion_case` | `PROJECT_AS` | `analogy_only` | The bounded Q0–Q5 workload-review Trajectory with central Non-Event independently instantiated in C17-LAMBDA-01. → Synthetic executable state-transition trace used as the comparison target; not a transformed identity of the… | Chapter 40 · lock-critical | [MD](../03_cases/markdown/C40-X6_Projection_versus_Structural_Analogy.md) · [YAML](../03_cases/yaml/C40-X6_Projection_versus_Structural_Analogy.yaml) |
| `C40-P7F` — Historical Frame-Function Candidate | `positive_case` | `PROJECT_AS` | `admissible_but_provisional` | Bounded recurrent transition-form composite R7 reconstructed from the same three independently warranted C17… → One C7 contextual view in which R7 performs a bounded historical frame-function for credible interpretations,… | Chapter 40 / Chapter 36 | [MD](../03_cases/markdown/C40-P7F_Frame_Function_Candidate.md) · [YAML](../03_cases/yaml/C40-P7F_Frame_Function_Candidate.yaml) · [Package](../03_cases/packages/C40-P7_Competing_Projections.md) |
| `C40-P7G` — Dynamic Attractor-Function Candidate | `positive_case` | `PROJECT_AS` | `admissible_but_provisional` | Bounded recurrent transition-form composite R7 reconstructed from the same three independently warranted C17… → One C7 contextual view in which R7 performs a bounded dynamic attractor-function for transition access, departure… | Chapter 40 / Chapter 36 | [MD](../03_cases/markdown/C40-P7G_Attractor_Function_Candidate.md) · [YAML](../03_cases/yaml/C40-P7G_Attractor_Function_Candidate.yaml) · [Package](../03_cases/packages/C40-P7_Competing_Projections.md) |
| `C40-N7` — Person-Level Type Jump | `countercase` | `PROJECT_AS` | `failed_transformation` | Bounded relational configuration C3 in which recurrent form R3 performs a dynamic attractor-function and p7… → Attempted target view in which role-holder p7 is assigned an intrinsic attractor-type or binding-type property… | Chapter 40 / Chapter 38 | [MD](../03_cases/markdown/C40-N7_Person_Level_Type_Jump.md) · [YAML](../03_cases/yaml/C40-N7_Person_Level_Type_Jump.yaml) |
| `C35-A1` — Operator-Weighting Profile as Modulating Function | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | Configuration-bound operator-weighting profile with Ω exposure and Θ accumulation prominent relative to the… → Contextual view of W35 as a bounded continuation-cost modulating function in H35.; function: bounded… | Chapter 35 · lock-critical | [MD](../03_cases/markdown/C35-A1_PROJECT_AS_Operator_Weighting_Profile.md) · [YAML](../03_cases/yaml/C35-A1_PROJECT_AS_Operator_Weighting_Profile.yaml) · [Package](../03_cases/packages/C35-A1_Operator_Weighting_Profile_and_RETYPE_Type_Boundary.md) |
| `C38-N1` — Origin-Type Replacement Failure | `countercase` | `PROJECT_AS` | `failed_transformation` | Configuration-bound operator-weighting profile with Ω exposure and Θ accumulation prominent relative to the… → Invalid view that declares W35 to be Ω or a new Ω/Θ operator type.; function: invalid source-type replacement | Chapter 38 · lock-critical | [MD](../03_cases/markdown/C38-N1_PROJECT_AS_Origin_Type_Replacement_Failure.md) · [YAML](../03_cases/yaml/C38-N1_PROJECT_AS_Origin_Type_Replacement_Failure.yaml) · [Package](../03_cases/packages/C35-A1_Operator_Weighting_Profile_and_RETYPE_Type_Boundary.md) |
| `C38-X3` — Projection or Φ-Recontextualization | `confusion_case` | `PROJECT_AS` | `failed_transformation` | Configuration-bound operator-weighting profile with Ω exposure and Θ accumulation prominent relative to the… → Re-described W35 under frame R35 with unchanged action conditions.; function: no PROJECT_AS function established | Chapter 38 · lock-critical | [MD](../03_cases/markdown/C38-X3_PROJECT_AS_or_Recontextualization_Failure.md) · [YAML](../03_cases/yaml/C38-X3_PROJECT_AS_or_Recontextualization_Failure.yaml) · [Package](../03_cases/packages/C35-A1_Operator_Weighting_Profile_and_RETYPE_Type_Boundary.md) |

### M.4.4 LIMITS and integrated chains / Chapters 47–54

| ID and title | Class | Operation | Output | Source → target summary | Coverage role | Artifacts |
|---|---|---|---|---|---|---|
| `C52-NC1` — Competing Decompositions of a Compressed Handoff Occurrence | `confusion_case` | `DECOMPOSE` | `non_capture` | One compressed synthetic handoff occurrence labelled “handoff failure,” bounded from partial transfer through… → Attempted single finer reconstruction of H0 that identifies one decisive constitutive internal relation while… | Chapter 52 | [MD](../03_cases/markdown/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.md) · [YAML](../03_cases/yaml/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.yaml) |
| `C47-CP1A` — Compose Distributed Access Composite | `positive_case` | `COMPOSE` | `admissible_with_bounded_claim` | Four bounded local asymmetry occurrences in one synthetic coordination field. → Derived distributed access composite formed from A1–A4 and their constitutive relation topology. | Chapter 47 / Chapter 34 | [MD](../03_cases/markdown/C47-CP1A_COMPOSE_Distributed_Access_Composite.md) · [YAML](../03_cases/yaml/C47-CP1A_COMPOSE_Distributed_Access_Composite.yaml) · [Package](../03_cases/packages/C47-CP1_COMPOSE_to_PROJECT_AS_Continuity_Chain.md) |
| `C47-CP1B` — Project Composite as Higher-Level Access Function | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | The exact derived relational composite output of C47-CP1A. → Bounded H47 target view in which Q47 performs higher-level access work.; function: bounded higher-level access… | Chapter 47 / Chapter 34 | [MD](../03_cases/markdown/C47-CP1B_PROJECT_AS_Higher_Level_Access_Function.md) · [YAML](../03_cases/yaml/C47-CP1B_PROJECT_AS_Higher_Level_Access_Function.yaml) · [Package](../03_cases/packages/C47-CP1_COMPOSE_to_PROJECT_AS_Continuity_Chain.md) |
| `C47-CP1C` — Nominal Referent-Shift Projection Failure | `countercase` | `PROJECT_AS` | `failed_transformation` | A later source reusing label Q47 after substituting A2/A4 and dissolving load-bearing relations. → Attempted same access function in H47* despite changed source referent and absent relation topology.; function:… | Chapter 47 / Chapter 34 | [MD](../03_cases/markdown/C47-CP1C_PROJECT_AS_Nominal_Referent_Shift_Failure.md) · [YAML](../03_cases/yaml/C47-CP1C_PROJECT_AS_Nominal_Referent_Shift_Failure.yaml) · [Package](../03_cases/packages/C47-CP1_COMPOSE_to_PROJECT_AS_Continuity_Chain.md) |
| `C54-CD1A` — Compose Bounded Path P54 | `positive_case` | `COMPOSE` | `admissible_with_bounded_claim` | A54–D54 local occurrences with declared order and one side branch. → Bounded ordered path A54→B54→C54 with inherited side-branch exclusion and transition uncertainty. | Chapter 54 | [MD](../03_cases/markdown/C54-CD1A_COMPOSE_Bounded_Path_P54.md) · [YAML](../03_cases/yaml/C54-CD1A_COMPOSE_Bounded_Path_P54.yaml) · [Package](../03_cases/packages/C54-CD1_COMPOSE_to_DECOMPOSE_Non_Invertibility_Chain.md) |
| `C54-CD1B` — Reopen P54 Without Inversion | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | The same bounded path P54 produced by C54-CD1A. → Finer reconstruction of the same P54 path with B54a/B54b distinction and inherited Loss. | Chapter 54 | [MD](../03_cases/markdown/C54-CD1B_DECOMPOSE_Reopen_P54.md) · [YAML](../03_cases/yaml/C54-CD1B_DECOMPOSE_Reopen_P54.yaml) · [Package](../03_cases/packages/C54-CD1_COMPOSE_to_DECOMPOSE_Non_Invertibility_Chain.md) |
| `C54-DC1A` — Decompose Coordination Bundle B55 | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | Compressed coordination occurrence bundle. → Same B55 bundle reconstructed into five components and four relations. | Chapter 54 | [MD](../03_cases/markdown/C54-DC1A_DECOMPOSE_B55.md) · [YAML](../03_cases/yaml/C54-DC1A_DECOMPOSE_B55.yaml) · [Package](../03_cases/packages/C54-DC1_DECOMPOSE_to_COMPOSE_Reformation_Chain.md) |
| `C54-DC1B` — Compose New Residual-Load Composite K55 | `positive_case` | `COMPOSE` | `admissible_with_bounded_claim` | Reconstructed R55v, R55h, R55d components with inherited relations and uncertainty. → New residual-load composite formed from review, hold, and residual debt. | Chapter 54 | [MD](../03_cases/markdown/C54-DC1B_COMPOSE_K55.md) · [YAML](../03_cases/yaml/C54-DC1B_COMPOSE_K55.yaml) · [Package](../03_cases/packages/C54-DC1_DECOMPOSE_to_COMPOSE_Reformation_Chain.md) |
| `C54-DP1A` — Decompose H56 Before Projection | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | Compressed coordination incident occurrence. → Finer same-reference H56 reconstruction with correction-window and residual-load relations. | Chapter 54 | [MD](../03_cases/markdown/C54-DP1A_DECOMPOSE_H56.md) · [YAML](../03_cases/yaml/C54-DP1A_DECOMPOSE_H56.yaml) · [Package](../03_cases/packages/C54-DP1_DECOMPOSE_to_PROJECT_AS_Threshold_Function_Chain.md) |
| `C54-DP1B` — Project H56 as A56 Threshold Function | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | Origin-typed finer reconstruction from C54-DP1A. → Bounded correction-window threshold function in A56.; function: correction-window threshold function in A56 | Chapter 54 | [MD](../03_cases/markdown/C54-DP1B_PROJECT_AS_A56_Threshold_Function.md) · [YAML](../03_cases/yaml/C54-DP1B_PROJECT_AS_A56_Threshold_Function.yaml) · [Package](../03_cases/packages/C54-DP1_DECOMPOSE_to_PROJECT_AS_Threshold_Function_Chain.md) |
| `C54-PD1B` — Reopen Origin Trajectory After Projection | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | Origin-typed workload-review trajectory previously projected in C40-P2. → Finer phase-cluster reconstruction of the same origin trajectory. | Chapter 54 | [MD](../03_cases/markdown/C54-PD1B_DECOMPOSE_Q0_Q5_Origin_Trajectory.md) · [YAML](../03_cases/yaml/C54-PD1B_DECOMPOSE_Q0_Q5_Origin_Trajectory.yaml) · [Package](../03_cases/packages/C54-PD1_PROJECT_AS_to_DECOMPOSE_Origin_Source_Chain.md) |
| `C53-CPD1C` — Complete-Return Claim After Compose and Projection | `confusion_case` | `DECOMPOSE` | `claim_reduction_required` | Origin-typed Q47 composite from C47-CP1A, previously projected in C47-CP1B. → Attempted complete and lossless finer reconstruction of Q47 after projection. | Chapter 53 | [MD](../03_cases/markdown/C53-CPD1C_DECOMPOSE_Q47_Complete_Return_Claim.md) · [YAML](../03_cases/yaml/C53-CPD1C_DECOMPOSE_Q47_Complete_Return_Claim.yaml) · [Package](../03_cases/packages/C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain.md) |
| `C50-FP1A` — Failed Coarse Frame-Function Claim | `countercase` | `PROJECT_AS` | `failed_transformation` | Coarse synthetic trajectory T50 with a rhetorically stabilized label and separately source-supported finer phase… → Attempted stabilizing frame-function view in C50.; function: unsupported stabilizing frame-function | Chapter 50 · lock-critical | [MD](../03_cases/markdown/C50-FP1A_PROJECT_AS_Failed_Coarse_Frame_Function.md) · [YAML](../03_cases/yaml/C50-FP1A_PROJECT_AS_Failed_Coarse_Frame_Function.yaml) · [Package](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) |
| `C50-FP1B` — Narrower Path Successor | `positive_case` | `DECOMPOSE` | `admissible_with_bounded_claim` | Coarse synthetic trajectory T50 with a rhetorically stabilized label and separately source-supported finer phase… → Same T50 reference reopened as R50→H50a→P50→L50. | Chapter 50 · lock-critical | [MD](../03_cases/markdown/C50-FP1B_DECOMPOSE_Narrower_Path_Reconstruction.md) · [YAML](../03_cases/yaml/C50-FP1B_DECOMPOSE_Narrower_Path_Reconstruction.yaml) · [Package](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) |
| `C50-FP1X` — Granularity Escape Stop | `confusion_case` | `DECOMPOSE` | `mandatory_stop` | Coarse synthetic trajectory T50 with a rhetorically stabilized label and separately source-supported finer phase… → Unsupported timestamp subdivision of T50. | Chapter 50 · lock-critical | [MD](../03_cases/markdown/C50-FP1X_DECOMPOSE_Granularity_Escape_Stop.md) · [YAML](../03_cases/yaml/C50-FP1X_DECOMPOSE_Granularity_Escape_Stop.yaml) · [Package](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) |
| `C50-FP1C` — Broader Coordination Composite | `positive_case` | `COMPOSE` | `admissible_with_bounded_claim` | C50-FP1B finer path and external gate occurrence G50 with declared relations. → New path-gate-reopening composite formed from the finer T50 path and G50. | Chapter 50 · lock-critical | [MD](../03_cases/markdown/C50-FP1C_COMPOSE_Broader_Coordination_Composite.md) · [YAML](../03_cases/yaml/C50-FP1C_COMPOSE_Broader_Coordination_Composite.yaml) · [Package](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) |
| `C50-FP1D` — New Independent Threshold Projection | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | New path-gate-reopening composite from C50-FP1C. → Contextual view of K50 as a bounded reopening-threshold function in H50.; function: bounded reopening-threshold… | Chapter 50 · lock-critical | [MD](../03_cases/markdown/C50-FP1D_PROJECT_AS_New_Threshold_Function.md) · [YAML](../03_cases/yaml/C50-FP1D_PROJECT_AS_New_Threshold_Function.yaml) · [Package](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) |
| `C49-CAL1` — Calibration-Open Threshold Function | `confusion_case` | `PROJECT_AS` | `admissible_but_provisional` | Synthetic correction-window form with source-supported early/late discrimination and unresolved q3 threshold. → Contextual view of F49 as a calibration-open correction-window threshold function.; function: calibration-open… | Chapter 49 · lock-critical | [MD](../03_cases/markdown/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.md) · [YAML](../03_cases/yaml/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.yaml) · [Package](../03_cases/packages/C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md) |
| `C51-RE1` — Re-entry After New Sources | `positive_case` | `PROJECT_AS` | `admissible_with_bounded_claim` | Same origin profile F49 with materially new q3 calibration packet N49. → Re-entry view of F49 as the same bounded function with narrower context-specific interval [q3.4,q3.6].; function:… | Chapter 51 · lock-critical | [MD](../03_cases/markdown/C51-RE1_PROJECT_AS_Reentry_After_New_Sources.md) · [YAML](../03_cases/yaml/C51-RE1_PROJECT_AS_Reentry_After_New_Sources.yaml) · [Package](../03_cases/packages/C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md) |

## M.5 Shared package narratives

| Package | Member Records | Shared function |
|---|---|---|
| [C35-A1_Operator_Weighting_Profile_and_RETYPE_Type_Boundary](../03_cases/packages/C35-A1_Operator_Weighting_Profile_and_RETYPE_Type_Boundary.md) | `C35-A1` · `C38-N1` · `C38-X3` | one positive operator-occurrence profile and two RETYPE boundary failures |
| [C40-P7_Competing_Projections](../03_cases/packages/C40-P7_Competing_Projections.md) | `C40-P7F` · `C40-P7G` | same-source competing frame-function and attractor-function projections |
| [C47-CP1_COMPOSE_to_PROJECT_AS_Continuity_Chain](../03_cases/packages/C47-CP1_COMPOSE_to_PROJECT_AS_Continuity_Chain.md) | `C47-CP1A` · `C47-CP1B` · `C47-CP1C` | COMPOSE → PROJECT_AS continuity chain plus nominal-referent failure |
| [C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry](../03_cases/packages/C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md) | `C49-CAL1` · `C51-RE1` | calibration-open result, optional Stop, and changed-ground re-entry |
| [C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) | `C50-FP1A` · `C50-FP1B` · `C50-FP1X` · `C50-FP1C` · `C50-FP1D` | preserved failed claim followed by new DECOMPOSE, Stop, COMPOSE, and PROJECT_AS claims |
| [C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain](../03_cases/packages/C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain.md) | `C53-CPD1C` | three-step chain and complete-return claim boundary |
| [C54-CD1_COMPOSE_to_DECOMPOSE_Non_Invertibility_Chain](../03_cases/packages/C54-CD1_COMPOSE_to_DECOMPOSE_Non_Invertibility_Chain.md) | `C54-CD1A` · `C54-CD1B` | COMPOSE → DECOMPOSE non-invertibility |
| [C54-DC1_DECOMPOSE_to_COMPOSE_Reformation_Chain](../03_cases/packages/C54-DC1_DECOMPOSE_to_COMPOSE_Reformation_Chain.md) | `C54-DC1A` · `C54-DC1B` | DECOMPOSE → COMPOSE reformation without restoration |
| [C54-DP1_DECOMPOSE_to_PROJECT_AS_Threshold_Function_Chain](../03_cases/packages/C54-DP1_DECOMPOSE_to_PROJECT_AS_Threshold_Function_Chain.md) | `C54-DP1A` · `C54-DP1B` | DECOMPOSE → PROJECT_AS threshold-function chain |
| [C54-PD1_PROJECT_AS_to_DECOMPOSE_Origin_Source_Chain](../03_cases/packages/C54-PD1_PROJECT_AS_to_DECOMPOSE_Origin_Source_Chain.md) | `C54-PD1B` | PROJECT_AS → DECOMPOSE return to the origin-typed source object |

A package may support several chapters, but package count is not chapter count. Chapters without a genuine multi-record relation need no package narrative.

## M.6 Coverage roles

The case corpus performs four distinct coverage roles:

1. **Positive instantiation:** demonstrates a bounded transformation that carries its declared claim.
2. **Countercase pressure:** exposes a false composition, decomposition, projection, rescue route, or authority transfer.
3. **Confusion-boundary separation:** distinguishes neighboring operations, objects, coordinates, or Output Classes.
4. **Integrated-chain preservation:** tests handoffs while keeping each occurrence, Loss profile, Stop, Failure, and Non-Capture result separate.

The current chapter coverage matrix reports 56 covered, two partially covered, and zero missing chapter rows. The two partial rows are the same-source comparison duties in Chapters 16 and 25. They are not missing case files and are not silently closed by Appendix M.

## M.7 Reading routes

### By operation

- `COMPOSE`: begin with `C17-LINEAR-01`, then `C17-BRANCH-01`, `C17-MACRO-01`, and the C54 non-invertibility packages.
- `DECOMPOSE`: begin with `C28-TRAJECTORY-01`, then Resolution Gain/Neutrality, Overfine Stop, Operator-Type Failure, and `C52-NC1`.
- `PROJECT_AS`: begin with `C40-P1`, then competing projections, analogy/recontextualization/type-jump failures, calibration, and chain successors.

### By result boundary

- bounded versus provisional: compare `C40-P1`, `C40-P7F/G`, and `C49-CAL1`;
- Stop versus Failure: compare `C28-OVERFINE-01`, `C28-OPTYPE-01`, and `C50-FP1X`;
- Failure versus Non-Capture: compare `C40-N3` and `C52-NC1`;
- Analogy versus Projection Failure: compare `C40-X6` and `C38-X3`;
- Resolution Neutrality versus Claim Reduction: compare `C17-RES-01` and `C28-UNSUPPORTED-01`.

### By chain

Read the package narrative first, then each occurrence Record in sequence, then compare the local routing and Loss fields. Never infer a chain-level class by averaging local classes.

## M.8 Reader and graph handoff

Appendix M supplies stable identifiers and links for future Reader filters, Record Trace panels, package graphs, and 3D path views. A Reader may group by operation, case class, Output Class, chapter, package, chain position, or lock-critical role. It must not infer evidential strength, historical availability, causal force, class rank, or authority from node size, color, depth, or connectivity.

```text
index topology ≠ theory topology
visible package edge ≠ new operation
3D proximity ≠ semantic equivalence
many links ≠ stronger warrant
```

## M.9 Completion boundary

Appendix M is complete for the present 59-Record corpus. It remains bounded provisional until Reference Freeze and the Integrated Corpus Audit confirm that identifiers, links, chapter ownership, and final Block wording remain aligned. A later case addition must update the YAML Index, Markdown Index, pairing manifest, Output-Class coverage, package membership where applicable, and this Appendix in one controlled revision.
