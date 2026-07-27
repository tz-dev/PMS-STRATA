# Appendix I — Boundary and Confusion Cases

**Status:** substantive bounded provisional completion  
**Primary prose owners:** Chapters 0, 2, 4, 6, 8, 9, 13–16, 19, 23–26, 29, 31–38, and 41–52  
**Formal boundary owner:** `../07_model/Boundary_Decision_Tree.yaml`  
**Output-class owner:** `../07_model/Output_Classes.yaml`  
**Supporting reference owners:** `../04_reference/Output_Class_Index.md` and `../04_reference/Non_Equivalence_Index.md`  
**Case registry:** `../03_cases/Case_Index.md`  
**Reusable confusion-case template:** `../03_cases/templates/confusion_case_template.md`

---

## I.1 Purpose and Boundary

Appendix I provides a controlled catalogue of cases in which two or more superficially plausible descriptions compete at an operation, object, coordinate, continuity, Stop, capture, or Output-Class boundary.

A confusion case is not merely a difficult example. It is a case in which the analyst must identify **which distinction is load-bearing for the current claim** and preserve the rejected or separated alternative rather than allowing labels, detail, or chain position to settle the result.

```text
confusion case
→ makes a boundary inspectable

confusion case
≠ new rule
≠ automatic precedent
≠ class hierarchy
≠ first-match routing
```

Appendix I does not create a new adjudication layer. The current operation Record remains the owner of the current claim, source, Loss, audit findings, candidate set, collision adjudication, and selected Output Class.

---

## I.2 How to Read a Confusion Case

Every confusion case should identify:

1. the shared source or comparison basis;
2. the competing descriptions or routes;
3. why each route initially appears plausible;
4. the discriminating question;
5. the source feature, type rule, continuity duty, or claim boundary that decides or preserves the collision;
6. the local result for each separated claim or occurrence;
7. the canonical Output Class selected for the delimited tested claim;
8. the non-selected findings that remain preserved;
9. the Loss, Stop, Failure, or Non-Capture state;
10. the re-entry condition, where one exists.

The preferred comparison form is:

```text
same source object or same declared source field
+ same tested question where possible
+ rival operation / class / continuation descriptions
→ explicit discriminating condition
```

Same-source contrast is preferred because it reduces accidental variation. It is not always available. Where different cases are compared, Appendix I states the comparison limit rather than implying experimental equivalence.

---

## I.3 Boundary Families

Appendix I groups confusion cases into four families:

```text
A. object and coordinate boundaries
B. operation-classification boundaries
C. Output-Class collision boundaries
D. chain, continuity, Stop, Failure, and capture boundaries
```

These families overlap. Their separation is navigational, not ontological.

---

## I.4 Object and Coordinate Boundary Cases

### I.4.1 Frame versus Granularity versus Relative Level

A new Frame changes what is analytically foregrounded or contextualized. A granularity change opens or compresses internal differentiation. A relative-level shift locates an object relative to another object or relation within a declared comparison.

```text
new viewpoint
≠ finer resolution
≠ higher relative level
```

**Discriminating questions**

- Did the source object remain the same while internal resolution changed?
- Did the analytical context change without a finer reconstruction?
- Is “higher” or “lower” defined only relative to a declared comparator?
- Is the proposed change actually a target-function claim requiring `PROJECT_AS`?

A label such as “macro”, “micro”, “higher”, or “deeper” is insufficient. The record must declare the changed coordinate and the claim effect.

### I.4.2 Operator Type versus Occurrence versus Composite

[`C28-OPTYPE-01`](../03_cases/markdown/C28-OPTYPE-01_Operator_Decomposition_Error.md) demonstrates the decisive category boundary:

```text
operator type
≠ operator occurrence
≠ composite structure
```

`DECOMPOSE` may open an occurrence or composite. It may not decompose a canonical Δ–Ψ operator type. A dense account of an operator’s possible manifestations does not convert the type into a decomposable occurrence.

### I.4.3 Sequence versus Path versus Trajectory

[`C17-CHRON-01`](../03_cases/markdown/C17-CHRON-01_Chronology_Presented_as_Path.md), [`C17-LINEAR-01`](../03_cases/markdown/C17-LINEAR-01_Simple_Linear_Path.md), and [`C17-HISTORY-01`](../03_cases/markdown/C17-HISTORY-01_Similar_End_States_Different_Histories.md) establish three different burdens:

```text
ordered items
→ Sequence candidate

warranted selective transitions
→ Path candidate

Path + sustained historical load + later effect
→ Trajectory candidate
```

A Trajectory claim therefore cannot be recovered merely by adding duration words to a Path description.

### I.4.4 Trajectory versus Path Dependence

[`C17-WEAKPD-01`](../03_cases/markdown/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.md) preserves a repeated historical pattern while bounding the stronger order-dependence claim.

```text
historical persistence
≠ strong Path Dependence automatically
```

The discriminating burden is whether relevant alternative orderings or predecessor states would change the later reconstruction in the declared dimension.

### I.4.5 Missing Information versus Non-Event

[`C17-LAMBDA-01`](../03_cases/markdown/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.md) and [`C17-FALSEL-01`](../03_cases/markdown/C17-FALSEL-01_False_Central_Non_Event.md) separate a structured expectation-bound non-event from mere absence of data.

A warranted Non-Event requires at minimum:

- a source-supported expectation or action corridor;
- a relevant time window;
- a non-occurrence that changes continuation, cost, exposure, or reconstruction;
- later carryover where claimed.

```text
no record of event
≠ event did not occur
≠ structured Non-Event
```

---

## I.5 Operation-Classification Confusions

### I.5.1 COMPOSE versus Chronological Listing

The question is whether the analyst has declared selection, ordering, formation, and constitutive relations.

```text
list + timestamps
≠ COMPOSE automatically
```

Case contrast: [`C17-LINEAR-01`](../03_cases/markdown/C17-LINEAR-01_Simple_Linear_Path.md) versus [`C17-CHRON-01`](../03_cases/markdown/C17-CHRON-01_Chronology_Presented_as_Path.md).

### I.5.2 COMPOSE versus PROJECT_AS

[`C17-PROJ-01`](../03_cases/markdown/C17-PROJ-01_Path_or_Projection.md) preserves the composed Trajectory while separating a proposed target function for a later `PROJECT_AS` test.

```text
forming a composite object
≠ assigning that object a contextual function
```

The same source material may support both operations, but not in one occurrence or one merged result.

### I.5.3 DECOMPOSE versus New COMPOSE

[`C28-SUBPATH-01`](../03_cases/markdown/C28-SUBPATH-01_SUB_or_New_PATH.md) asks whether a finer same-reference reconstruction remains a decomposition or whether selected components are being formed into a new independent Path.

Use `DECOMPOSE` where the same reference object and source-function question remain primary. Use a new `COMPOSE` occurrence where selected outputs are re-formed into a new composite claim.

### I.5.4 DECOMPOSE versus PROJECT_AS

[`C28-SUBRETYPE-01`](../03_cases/markdown/C28-SUBRETYPE-01_SUB_or_RETYPE.md) retains a finer internal reconstruction but separates a target-side calibration-function proposal.

```text
opening internal structure
≠ functional projection into a target context
```

### I.5.5 PROJECT_AS versus Recontextualization

[`C38-X3`](../03_cases/markdown/C38-X3_PROJECT_AS_or_Recontextualization_Failure.md) shows that changed interpretation or salience alone does not establish a target function.

A valid `PROJECT_AS` claim must identify source-traceable work performed in the target context, not merely a new description.

### I.5.6 PROJECT_AS versus Analogy

[`C40-X6`](../03_cases/markdown/C40-X6_Projection_versus_Structural_Analogy.md) preserves a bounded resemblance without upgrading it into a contextual target function.

```text
structural resemblance
≠ functional continuity
```

### I.5.7 PROJECT_AS versus Origin-Type Replacement

[`C38-N1`](../03_cases/markdown/C38-N1_PROJECT_AS_Origin_Type_Replacement_Failure.md), [`C40-N3`](../03_cases/markdown/C40-N3_PROJECT_AS_Label_Substitution_Failure.md), and [`C40-N7`](../03_cases/markdown/C40-N7_Person_Level_Type_Jump.md) show three distinct failures:

- profile rewritten as PMS operator type;
- label substituted for a demonstrated function;
- configuration-level function transferred to a person.

All fail Type Integrity, but the preserved source and possible narrower claims differ.

---

## I.6 The Fourteen Load-Bearing Output-Class Boundaries

The Formal Model currently registers fourteen load-bearing collision families. The inventory is **not closed**, and no boundary creates a class ranking or default precedence.

### I.6.1 `admissible` versus `admissible_with_bounded_claim`

Use `admissible` where the delimited claim passes as declared under ordinary required boundedness. Use `admissible_with_bounded_claim` where a material restriction of reach is itself the decisive governance result and the narrower claim has already been formulated and passed.

```text
all claims are bounded
≠ all passing claims receive bounded-claim class
```

### I.6.2 `admissible_with_bounded_claim` versus `admissible_but_provisional`

The bounded class records a tested reach restriction. The provisional class records one coherent usable claim with a material unresolved support, calibration, temporal, counterfactual, or rival-reconstruction condition.

Case anchor: [`C49-CAL1`](../03_cases/markdown/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.md) is provisional because the threshold remains materially unresolved.

### I.6.3 `admissible_with_bounded_claim` versus `partially_admissible`

A bounded claim remains one coherent claim. A partial result separates parts, stages, relations, or subclaims with different outcomes.

Case anchor: [`C28-SUBRETYPE-01`](../03_cases/markdown/C28-SUBRETYPE-01_SUB_or_RETYPE.md) retains one DECOMPOSE subclaim while separating the untested projection pressure.

### I.6.4 `partially_admissible` versus `admissible_but_provisional`

Partiality concerns differentiated outcomes across separable components. Provisionality concerns unresolved conditions affecting one coherent claim.

Do not use provisionality to avoid claim splitting, and do not split a coherent claim merely because its calibration remains open.

### I.6.5 `admissible_but_provisional` versus `resolution_neutral`

A provisional claim changes the warranted reconstruction but remains materially open. A resolution-neutral result follows a genuine source-supported resolution test that changes no warranted reconstruction.

Case anchors: [`C49-CAL1`](../03_cases/markdown/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.md) versus [`C17-RES-01`](../03_cases/markdown/C17-RES-01_Path_or_Resolution_Drift.md).

### I.6.6 `admissible_but_provisional` versus `non_capture`

Provisionality retains an adequate coherent claim. Non-Capture records that no adequate retained form of the same delimited capture claim remains after adequate bounded attempts.

Case contrast: [`C49-CAL1`](../03_cases/markdown/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.md) versus [`C52-NC1`](../03_cases/markdown/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.md).

### I.6.7 `partially_admissible` versus `non_capture`

Use partiality where separable retained subclaims remain adequately supportable. Use Non-Capture where the whole capture claim lacks an adequate retained form and the partial captures cannot responsibly be integrated.

### I.6.8 `claim_reduction_required` versus `admissible_with_bounded_claim`

Claim reduction means the current claim must be narrowed and the narrower claim has not yet independently passed. Bounded admissibility means the narrowed claim has already been declared, tested, and passed.

Case anchor: [`C53-CPD1C`](../03_cases/markdown/C53-CPD1C_DECOMPOSE_Q47_Complete_Return_Claim.md) withdraws the complete-return claim and requires a new bounded test.

### I.6.9 `claim_reduction_required` versus `mandatory_stop`

Reduction addresses claim reach. Mandatory Stop prohibits further continuation under the present claim, route, sources, or granularity.

Both may be relevant. Where continuation itself becomes inadmissible, the Stop finding must be preserved even if a narrower future claim is imaginable.

### I.6.10 `mandatory_stop` versus `failed_transformation`

A Stop preserves what has already been responsibly reached and prohibits further continuation. Failure rejects the declared operation claim.

Case contrast:

- [`C28-OVERFINE-01`](../03_cases/markdown/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.md): prior adequate reconstruction preserved; further detail must stop.
- [`C28-OPTYPE-01`](../03_cases/markdown/C28-OPTYPE-01_Operator_Decomposition_Error.md): the declared DECOMPOSE operation fails because its source is the wrong object type.

### I.6.11 `failed_transformation` versus `non_capture`

Failure is operation- and claim-specific. Non-Capture requires multiple adequate bounded attempts and a persistent claim-relative capture limit.

```text
one failed attempt
≠ non_capture
```

Case contrast: [`C40-N3`](../03_cases/markdown/C40-N3_PROJECT_AS_Label_Substitution_Failure.md) versus [`C52-NC1`](../03_cases/markdown/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.md).

### I.6.12 `mandatory_stop` versus `non_capture`

Stop answers whether continuation is permitted. Non-Capture answers whether an adequate retained form of the capture claim exists after adequate attempts.

A Non-Capture record may include a Stop finding, but the two are not synonyms and neither automatically outranks the other.

### I.6.13 `resolution_neutral` versus `claim_reduction_required`

Resolution neutrality preserves the warranted reconstruction after a real finer-resolution test. Claim reduction changes the allowable reach of the claim.

Case contrast: [`C17-RES-01`](../03_cases/markdown/C17-RES-01_Path_or_Resolution_Drift.md) versus [`C28-UNSUPPORTED-01`](../03_cases/markdown/C28-UNSUPPORTED-01_Unsupported_Internal_Structure.md).

### I.6.14 `analogy_only` versus Failed Projection

`analogy_only` requires an affirmative, independently delimited resemblance claim that remains useful after projection is withheld. A failed projection alone does not automatically generate a valid analogy.

Case anchor: [`C40-X6`](../03_cases/markdown/C40-X6_Projection_versus_Structural_Analogy.md).

---

## I.7 Stop, Failure, and Non-Capture Decision Matrix

| Question | Mandatory Stop | Failed Transformation | Non-Capture |
|---|---|---|---|
| What is governed? | continuation | declared operation claim | adequate capture of a delimited claim |
| What may remain? | prior adequate result | source material and possible new claims | partial captures and explicit remainder |
| Minimum burden | binding continuation boundary | decisive operation/type/reference/function failure | adequate bounded attempts plus persistent capture limit |
| Does new evidence permit re-entry? | yes, through a new record when conditions change | yes, through a new claim/operation record | yes, if the limiting condition materially changes |
| Is missing information sufficient? | no | no | no |
| Does later success erase it? | no | no | no |

The matrix is a comparison aid. Final selection still requires the full current Record.

---

## I.8 Same-Source and Chain Confusion Cases

### I.8.1 Competing Projections from One Source

[`C40-P7F`](../03_cases/markdown/C40-P7F_Frame_Function_Candidate.md) and [`C40-P7G`](../03_cases/markdown/C40-P7G_Attractor_Function_Candidate.md) test distinct functions against the same source object.

```text
same source
+ two source-sensitive candidates
≠ one candidate must replace the other
≠ both may be merged automatically
```

The shared package [`C40-P7`](../03_cases/packages/C40-P7_Competing_Projections.md) preserves separate claims, contexts, traces, and results.

### I.8.2 Failure Preservation and Projection Rescue

The [`C50-FP1`](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) chain demonstrates:

```text
failed original PROJECT_AS
→ valid DECOMPOSE successor
→ mandatory Stop on escape route
→ new COMPOSE successor
→ new bounded PROJECT_AS claim
```

The later successes do not repair the original failure.

### I.8.3 Re-entry versus Silent Continuation

[`C49-CAL1`](../03_cases/markdown/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.md) reaches a provisional result and optional Stop. [`C51-RE1`](../03_cases/markdown/C51-RE1_PROJECT_AS_Reentry_After_New_Sources.md) is a new test after materially new sources.

```text
re-entry
≠ resumed old record
≠ retroactive certainty
```

### I.8.4 Projection Followed by Decomposition

[`C54-PD1B`](../03_cases/markdown/C54-PD1B_DECOMPOSE_Q0_Q5_Origin_Trajectory.md) reopens the origin-typed Trajectory rather than decomposing the target function itself.

```text
PROJECT_AS result
≠ new origin object to decompose automatically
```

### I.8.5 Complete Return versus Bounded Reopening

[`C53-CPD1C`](../03_cases/markdown/C53-CPD1C_DECOMPOSE_Q47_Complete_Return_Claim.md) rejects a complete/lossless return after composition and projection while preserving the possibility of a new bounded reopening claim.

```text
return-like movement
≠ inversion
```

---

## I.9 Confusion-Case Recording Protocol

For each confusion case:

```yaml
confusion_case:
  tested_claim:
  shared_source_or_comparison_basis:
  candidate_a:
  candidate_b:
  candidate_c_if_needed:
  initial_plausibility:
  discriminating_question:
  decisive_source_or_type_condition:
  claims_split: true | false
  operation_records_required: []
  preserved_non_selected_findings: []
  stop_failure_non_capture_boundary:
  selected_output_class:
  reentry_condition:
```

This compact protocol is explanatory. Concrete record syntax remains owned by `Transformation_Record.schema.json`.

---

## I.10 Reusable Confusion-Case Template

The file [`confusion_case_template.md`](../03_cases/templates/confusion_case_template.md) is now a reusable Markdown companion for one delimited confusion case or a comparison package containing separately recorded occurrences.

It requires:

- source/comparison basis;
- candidates and initial plausibility;
- operation classification;
- discriminating tests;
- fourteen-boundary check where applicable;
- claim splitting;
- preserved findings;
- Stop, Failure, Non-Capture, Loss, and re-entry boundaries;
- exact YAML Record and package links.

The template never authorizes one Markdown document to replace multiple required operation Records.

---

## I.11 Anti-Patterns in Boundary Adjudication

Do not:

- select the first plausible class;
- treat a Decision Tree branch as a class rank;
- use scores or weights to settle collisions;
- merge separate claims to avoid multiple Records;
- relabel a failure as Stop or Non-Capture because it appears more cautious;
- use provisionality as indefinite immunity;
- use same-source comparison as proof of causal exclusivity;
- infer person, group, moral, political, legal, or clinical status from a structural boundary result;
- treat a case anchor as binding precedent for a new source field.

---

## I.12 Completion Checklist

A boundary/confusion analysis is ready only where:

- the competing descriptions are explicitly stated;
- the comparison basis is declared;
- operation identity is not selected by surface labels;
- object, Frame, granularity, relative level, and target-function changes remain distinct;
- candidate generation is separated from final class selection;
- all applicable load-bearing class collisions are adjudicated;
- claims are split where one class would conceal a material second result;
- Stop, Failure, and Non-Capture are separately assessed;
- earlier results and non-selected material findings remain preserved;
- all five Loss fields remain local to each operation occurrence;
- no hierarchy, scoring, first-match rule, or authority inheritance is introduced.

The bounded Appendix-I result is:

```text
admissible_with_bounded_claim
```

---

## I.13 Handoff

Appendix I hands forward to:

```text
Appendix J
→ optional operator-weighting and trajectory stress tests

Appendix K
→ cross-domain projection and analogy stress tests

Appendix L
→ non-operator remainders and decomposition limits

Appendix N
→ integrated audit template and collision-adjudication fields
```
