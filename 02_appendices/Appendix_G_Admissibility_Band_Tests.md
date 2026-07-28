# Appendix G — Admissibility Band Tests

**Status:** substantive bounded provisional completion  
**Primary prose owners:** Chapters 6 and 41–53  
**Binding compact control:** `../05_minified/PMS_STRATA_Admissibility_Band_Minified.md`  
**Formal rule owner:** `../07_model/Admissibility_Rules.yaml`  
**Output routing owners:** `../07_model/Output_Classes.yaml` and `../07_model/Boundary_Decision_Tree.yaml`

---

## G.1 Purpose and Boundary

Appendix G provides a reusable test catalogue for determining whether one delimited STRATA transformation claim remains within the Praxeological Admissibility Band.

The band is bounded by:

```text
Praxeological Traceability Ceiling
─────────────────────────────
admissible transformation
─────────────────────────────
Praxeological Relevance Floor
```

Below the floor, further distinction produces no warranted praxis-relevant change. Above the ceiling, the result no longer carries reconstructible structural load from its sources.

Appendix G operationalizes the existing tests. It does not create a numerical scale, a scoring system, a class hierarchy, a universal threshold, or an automatic substantive decision procedure.

```text
usable test catalogue
≠ mechanical classifier
≠ empirical truth procedure
≠ causal proof
≠ authority grant
```

The test object is always claim-relative:

```text
operation occurrence T_i
+ source object X
+ transformation context C_x
+ tested claim Q
+ declared source basis S
```

No object is globally admissible or inadmissible apart from a specified operation and claim.

---

## G.2 Entry Conditions

Before applying the band tests, confirm that the packet contains:

1. one delimited tested claim;
2. exactly one registered operation occurrence, unless the record scope is an integrated chain;
3. source reference, origin typing, coordinates, and source scope;
4. target object or target function as applicable;
5. declared claim and validity scopes;
6. a five-field Loss declaration;
7. alternatives, rivals, or an explicit bounded no-alternative statement;
8. prior failures, limits, stops, or reductions where relevant;
9. sufficient information to distinguish substantive failure from formal incompleteness.

If these entry conditions are absent, emit a noncanonical formal diagnostic. Do not route missing input mechanically to `failed_transformation`, `mandatory_stop`, or `non_capture`.

```text
incomplete packet
≠ failed transformation
≠ mandatory stop
≠ non-capture
```

---

## G.3 Non-Compensation Rule

Every load-bearing test is non-compensatory.

```text
formal elegance
+ high detail
+ many citations
≠ compensation for missing PraxisPurchase
≠ compensation for missing TraceableLoad
≠ compensation for TypeIntegrity failure
```

No majority vote, weighted average, threshold sum, or score is admissible.

```text
12 audit stages completed
≠ 12 passes

15 positive findings + 1 decisive type failure
≠ admissible
```

The final Output Class must reflect the full applicable pattern for the current claim. The order of tests is evaluative, not a precedence ranking among classes.

---

## G.4 Lower-Bound Test — PraxisPurchase

### G.4.1 Governing question

> Which warranted reconstruction must be formulated differently because this distinction or transformation was introduced?

A transformation has praxeological purchase only where it changes at least one warranted statement concerning praxis structure, such as:

- action corridors;
- cost, exposure, or risk distribution;
- roles or asymmetries;
- expectation structures and non-events;
- commitment, binding, delay, duration, or irreversibility;
- path, trajectory, or path-dependence reconstruction;
- source-function reconstruction;
- bounded target function;
- claim scope;
- failure, stop, or capture boundary.

### G.4.2 Required declaration

```yaml
relevance_floor_test:
  proposed_difference:
  affected_praxis_dimensions: []
  changed_reconstruction:
  changed_claim:
  source_support:
  result: gain | neutral | below_floor | underdetermined
  stop_required:
```

This compact declaration is explanatory; the actual record uses the shared Rule Assessment and operation-specific result fields.

### G.4.3 Result values

The controlled lower-bound results are:

```text
gain
neutral
below_floor
underdetermined
```

They are local findings, not canonical Output Classes.

### G.4.4 Positive test

The lower-bound test passes where at least one source-supported difference changes the warranted reconstruction and the change is relevant to the current claim.

Examples:

- a hidden asymmetry changes who bears delay costs;
- a previously omitted non-event changes the reconstructed path;
- a component relation changes the source-function assessment;
- source variation removes a proposed target function;
- a finer distinction reveals that the original claim must be bounded or reduced.

### G.4.5 Neutrality test

A genuine refinement may be correct yet produce no further praxis finding.

```text
source-supported refinement
+ no changed warranted reconstruction
→ resolution_neutral may be available
```

Neutrality requires an actual supported comparison. It is not a synonym for missing evidence, editorial repetition, or operation failure.

### G.4.6 Below-floor test

The result lies below the floor where:

- only terminology changes;
- more micro-detail repeats the same functional result;
- extra event segmentation changes no path, role, cost, or claim;
- additional distinctions cannot be supported by the source basis;
- complexity grows without improved discrimination;
- decomposition is continued merely because further decomposition is possible.

The canonical countercase is [`C28-OVERFINE-01`](../03_cases/markdown/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.md), where finer analysis no longer provides praxeological purchase and a mandatory stop is reached.

### G.4.7 Relevance-floor comparison protocol

Compare, where possible:

```text
R_coarse
versus
R_fine
```

Ask:

1. Does the finer reconstruction change a load-bearing relation?
2. Does it alter the claim, not merely the prose?
3. Does it expose a countercase or stop condition?
4. Can the changed result be traced to the added distinction?
5. Would removing that distinction restore the coarser result?

A negative answer to all five questions strongly indicates neutrality or below-floor analysis, but the final local result still requires substantive judgment.

---

## G.5 Upper-Bound Test — TraceableLoad

### G.5.1 Governing question

> Does the target result remain reconstructibly dependent on its declared source load?

Traceable load requires more than citation. The record must show:

```text
source identification
+ structural mapping
+ functional dependency
+ temporal or relational dependency
+ Loss disclosure
+ claim limitation
```

### G.5.2 Required declaration

```yaml
traceability_ceiling_test:
  source_objects: []
  load_bearing_features: []
  mapped_target_components: []
  dependency_statement:
  source_variation_effect:
  disclosed_loss:
  retained_claim_limit:
  result: within_ceiling | claim_reduction | above_ceiling | underdetermined
```

### G.5.3 Controlled results

```text
within_ceiling
claim_reduction
above_ceiling
underdetermined
```

`claim_reduction` here is a boundary signal. It is not itself the canonical Output Class `claim_reduction_required` until routing establishes that the original claim must be reduced and no already-tested narrower claim has yet passed.

### G.5.4 Constitutive source-trace test

For each load-bearing source feature, state:

1. which claim component it supports;
2. which target component or function depends on it;
3. how the dependency operates;
4. what source variation would change;
5. what remains outside the trace.

A trace fails where source entries are decorative, interchangeable, or unable to constrain the result.

### G.5.5 Source-variation test

Vary or remove one declared load-bearing feature.

```text
material source change
+ arbitrarily unchanged target result
→ traceability failure signal
```

Sensitivity need not be binary. The result may weaken, narrow, change form, become provisional, or fail. What is prohibited is claiming constitutive load while treating relevant source changes as immaterial without explanation.

### G.5.6 Above-ceiling patterns

Typical upper-bound failures include:

- a macro-label with no warranted path;
- a target function that survives arbitrary removal of its alleged source carriers;
- a composite that hides selection and constitutive relations;
- a decomposition that invents unsupported internal structure;
- a projection supported only by analogy or label similarity;
- a claim whose reach exceeds its source and calibration support.

The canonical macro countercase is [`C17-MACRO-01`](../03_cases/markdown/C17-MACRO-01_Macro_Label_without_Traceable_Path.md).

---

## G.6 TypeIntegrity Test

### G.6.1 Governing question

> Are source type, operation type, target object, and target function kept distinct throughout the transformation?

The test verifies:

- operator type is not treated as an occurrence;
- occurrence is not treated as composite;
- DECOMPOSE does not open a PMS operator type;
- PROJECT_AS preserves the source origin type;
- COMPOSE does not silently create a target function;
- Frame, Granularity, and Relative Level are not substituted for one another;
- derived objects or functions are not promoted to PMS primitives.

### G.6.2 Type table

| Operation | Admissible source | Admissible result | Decisive type error |
|---|---|---|---|
| COMPOSE | multiple or sequential source structures | declared composite object | automatic target function or primitive |
| DECOMPOSE | compressed occurrence or composite | finer reconstruction of same reference object | operator-type decomposition or new reference object |
| PROJECT_AS | independently origin-typed object | bounded target function in declared context | origin-type replacement |

### G.6.3 Hard failure examples

- [`C28-OPTYPE-01`](../03_cases/markdown/C28-OPTYPE-01_Operator_Decomposition_Error.md): operator-type decomposition error;
- [`C38-N1`](../03_cases/markdown/C38-N1_PROJECT_AS_Origin_Type_Replacement_Failure.md): origin-type replacement;
- [`C40-N7`](../03_cases/markdown/C40-N7_Person_Level_Type_Jump.md): prohibited person-level type jump.

TypeIntegrity failure cannot be repaired by higher relevance, stronger traceability, or greater formal detail.

---

## G.7 Continuity Tests

Continuity is claim-relative. It does not require exhaustive sameness.

### G.7.1 Reference Continuity

Ask whether the transformation still concerns the declared reference object or a valid new composite with disclosed provenance.

```text
same label
≠ same reference
```

A nominal successor that lacks the earlier constitutive relations does not inherit reference continuity. See [`C47-CP1C`](../03_cases/markdown/C47-CP1C_PROJECT_AS_Nominal_Referent_Shift_Failure.md).

### G.7.2 Functional Continuity

Ask whether the source function is preserved, refined, differentiated, rejected, or left underdetermined in a way consistent with the operation.

For PROJECT_AS, ask whether the target function remains dependent on the origin-typed source in the declared context.

### G.7.3 Temporal Continuity

Preserve only claim-bearing temporal structure, not exhaustive chronology. Verify that omission of ordering, duration, delay, branch status, or historical load does not silently change the claim.

### G.7.4 Loss Continuity

In a chain, every occurrence keeps its own Loss profile.

```text
L_chain = ⟨L_1, L_2, …, L_n⟩
```

Later operations may add new Loss. They do not erase earlier compression, exclusion, uncertainty, or irrecoverability.

### G.7.5 Authority Continuity

Authority does not flow upward with reference or function.

```text
valid source relation
≠ inherited application authority
```

---

## G.8 ContextualBoundedness Test

Declare:

- source frame;
- target frame where applicable;
- source and target granularity;
- relative level relation;
- temporal scope;
- transformation context;
- validity scope;
- excluded reach.

The same object may support one claim in one context and not another.

For PROJECT_AS, use a comparison context where possible:

```text
F_t present in C_1
F_t absent or materially different in C_2
```

A target function stated as universally present, with no context boundary, normally exceeds the admissible claim.

---

## G.9 CounterfactualSensitivity Test

### G.9.1 Governing question

> Which relevant source-grounded change would alter the reconstructed result?

Controlled sensitivity classes are:

```text
strongly_sensitive
partially_sensitive
weakly_sensitive
insensitive
underdetermined
untestable
```

These are not causal proof and not empirical experiments by themselves.

### G.9.2 Operation-specific tests

#### COMPOSE

Vary:

- source selection;
- ordering;
- formation rule;
- constitutive relation;
- omitted event or non-event.

Ask whether the composite identity, path, trajectory, or claim changes.

#### DECOMPOSE

Vary:

- one proposed component;
- one component relation;
- internal temporality;
- source-function assumption;
- target granularity.

Ask whether the finer reconstruction or source-function assessment changes.

#### PROJECT_AS

Vary:

- a constitutive source feature;
- the target context;
- the target role relation;
- historical load;
- the comparison context.

Ask whether the target function weakens, disappears, or changes.

### G.9.3 Historical alternatives

A counterfactual historical branch is admissible only where its status, time window, resources, constraints, and source basis are declared.

```text
visualized branch
≠ historically available branch
```

Distinguish:

```text
rejected
blocked
aborted
deferred
unavailable
```

These branch statuses are not Output Classes.

---

## G.10 SelectionAndLoss Test

Audit the five fields:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

For every operation, ask:

1. What was selected?
2. What relation made the selection constitutive?
3. What was compressed?
4. What was excluded and why?
5. What remains uncertain?
6. What cannot be recovered from the resulting artifact?
7. How does the Loss affect the claim ceiling?

An empty field must be an explicit bounded statement, not an omission.

```text
no identified irrecoverable loss under current scope
≠ no irrecoverable loss exists universally
```

---

## G.11 Alternatives Test

The Alternatives test preserves at least the applicable members of:

```text
rival compositions
rival decompositions
rival projections
no transformation
non-translation
narrower claim
unresolved alternative
```

The selected route must explain why alternatives were not chosen. Alternatives are not merely decorative objections.

A valid no-transformation result may show that the source object should remain at its current form for the current claim. A valid non-translation result may preserve a structural analogy without permitting PROJECT_AS.

---

## G.12 SourceCeiling and Calibration Tests

### G.12.1 Source Ceiling

Ask whether the claim exceeds what the source basis can reconstruct.

Possible effects:

- retain the claim;
- bound the claim;
- qualify the claim;
- separate subclaims;
- reduce the claim;
- withdraw the claim;
- mark a capture limit.

### G.12.2 Calibration states

Controlled calibration states are:

```text
discriminating
calibration_open
case_dependent
non_discriminating
not_calibratable_with_present_sources
```

A calibration-open claim may remain usable if one coherent bounded claim survives and the unresolved threshold is explicit. See [`C49-CAL1`](../03_cases/markdown/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.md).

New material sources may license a new record and a new test, not silent continuation. See [`C51-RE1`](../03_cases/markdown/C51-RE1_PROJECT_AS_Reentry_After_New_Sources.md).

### G.12.3 No universal thresholds

Appendix G does not define a fixed threshold for:

- when a sequence becomes a path;
- when a path becomes a trajectory;
- when recurrence becomes an attractor-function;
- when detail becomes too fine;
- when a composite becomes too large;
- when analogy becomes projection.

All thresholds remain relational to source, frame, context, granularity, and claim.

---

## G.13 Anti-Immunization Test

A new transformation is a new claim.

```text
new frame
new granularity
new composite
new target function
→ new testable claim
```

It does not repair an earlier failed claim unless that earlier claim is independently retested and passes.

Required questions:

1. Which prior claim failed, was reduced, stopped, or bounded?
2. Is the new claim genuinely distinct?
3. Does the record preserve the earlier result?
4. Has a new source object, context, or claim scope been declared?
5. Is success being used rhetorically to erase the predecessor?

The chain package [`C50-FP1`](../03_cases/packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md) demonstrates correct preservation: later DECOMPOSE, COMPOSE, and PROJECT_AS successes do not repair the initial failed projection.

---

## G.14 Stop Test

### G.14.1 Mandatory Stop

Mandatory Stop is reached when further continuation under the present claim would be inadmissible, for example because:

- no praxeological purchase remains;
- the next step would exceed traceability;
- TypeIntegrity would fail;
- source support cannot sustain further resolution;
- the operation is being used to escape an objection;
- the claim has reached its ceiling;
- the remaining route would require invention.

Required declaration:

```yaml
stop_assessment:
  reached: true
  mode: mandatory
  stop_condition:
  preserved_result:
  prohibited_continuation:
  reentry_conditions:
```

### G.14.2 Optional Stop

Optional Stop records sufficiency:

```text
adequate bounded result reached
+ no material benefit from continuation
→ optional stop
```

Optional Stop is not an Output Class. It may accompany a usable result.

### G.14.3 Stop versus failure

```text
mandatory_stop
→ continuation is prohibited or structurally unavailable

failed_transformation
→ the declared operation does not carry its claim
```

The distinction is claim- and route-specific. Appendix I examines the boundary collisions in detail.

---

## G.15 Non-Capture Test

Genuine Non-Capture requires more than missing information or one failed attempt.

Required conditions:

1. the capture object or claim is clearly delimited;
2. multiple adequate bounded attempts have been made where alternatives are available;
3. each attempt preserves what it captures and what it leaves uncaptured;
4. no adequate retained form of the same capture claim remains;
5. forced integration would distort or invent source function;
6. rival or external methods have been considered where appropriate;
7. a re-entry condition is stated.

Controlled forms are:

```text
source_non_capture
granularity_non_capture
compositional_non_capture
projection_non_capture
calibration_non_capture
semantic_non_capture
partial_capture
```

The genuine case is [`C52-NC1`](../03_cases/markdown/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.md).

```text
missing information
≠ non-capture

failed transformation
≠ non-capture

partial capture
≠ automatically non-capture of every narrower claim
```

---

## G.16 Claim Ceiling and Authority Ceiling

### G.16.1 Claim Ceiling

State the strongest claim actually supported after all tests.

A claim ceiling must declare:

- retained claim;
- excluded reach;
- unresolved conditions;
- source and calibration limits;
- effects of Loss;
- whether a new narrower claim requires a separate record.

### G.16.2 Authority Ceiling

Independently confirm:

```yaml
governance:
  authority_inheritance: prohibited
  formal_validation_not_substantive_validation_acknowledged: true
  application_authority_not_granted: true
```

No transformation authorizes:

- person typing or diagnosis;
- moral ranking;
- political or legal legitimacy decisions;
- sanction or irreversible labels;
- automatic action recommendations;
- authority inheritance from source, method, formal model, or visualization.

---

## G.17 Twelve-Stage Integrated Test Sequence

| Stage | Test focus | Principal carriers | Required preservation |
|---:|---|---|---|
| 1 | Source and claim entry | source, scope, ceilings | incomplete packet remains diagnostic |
| 2 | Operation classification | Operation Registry | exactly one operation occurrence |
| 3 | Relevance Floor | PraxisPurchase | neutral/below-floor findings remain visible |
| 4 | Traceability Ceiling | TraceableLoad | constitutive source load and claim limits |
| 5 | Continuity and Type Integrity | type/reference/function/time/context | no category collapse |
| 6 | Counterfactual Sensitivity | source and context variation | sensitivity class and limits |
| 7 | Loss and Selection | five Loss fields | local Loss cannot be overwritten |
| 8 | Alternatives | rivals, no transformation, non-translation | rejected alternatives remain recorded |
| 9 | Source and Calibration Limits | Source Ceiling, Calibration | calibration-open conditions preserved |
| 10 | Anti-Immunization | claim history | earlier failures and stops preserved |
| 11 | Stop and Non-Capture | stop, capture boundary, claim reduction | no false closure |
| 12 | Claim and Authority Ceiling | final retained claim and governance | no authority inheritance |

The sequence is ordered because later tests depend on earlier declarations. It is not a class ranking and does not create Audit Stage 13 for output mapping.

---

## G.18 Operation-Specific Test Matrix

| Test | COMPOSE | DECOMPOSE | PROJECT_AS |
|---|---|---|---|
| PraxisPurchase | composite changes warranted path/configuration claim | finer structure changes reconstruction or establishes neutrality | target function changes bounded contextual reconstruction |
| TraceableLoad | source selection, order, relations remain reconstructible | components and relations remain source-supported | target function depends on source features and target context |
| TypeIntegrity | composite not primitive or automatic function | source is occurrence/composite, not operator type | origin type preserved |
| Reference Continuity | new composite provenance explicit | same reference object preserved | source reference preserved |
| Functional Continuity | source functions not silently replaced | source-function effect declared | target function source-dependent |
| Counterfactual | vary selection/order/relations | vary component/relation/granularity | vary source feature/context |
| Loss | selection and compression central | uncertainty and irrecoverability central | excluded contexts and functional limits central |
| Stop | unjustified aggregation or recursion | overfine detail or escape | type jump, analogy, or source-insensitive function |

---

## G.19 Boundary Result Matrix

| Finding pattern | Permissible next interpretation | Not yet established |
|---|---|---|
| gain + within ceiling + type integrity | plausible admissible candidate | final class |
| neutral supported resolution test | plausible `resolution_neutral` candidate | general operation success |
| below floor + continuation prohibited | plausible `mandatory_stop` candidate | failed operation by default |
| above ceiling but narrower claim possible | claim-reduction handoff | passed narrower claim |
| calibration open with usable coherent claim | plausible provisional candidate | non-capture |
| hard type failure | plausible failed-transformation candidate | mandatory stop automatically |
| capture limit after adequate attempts | plausible non-capture candidate | non-capture without collision audit |

Candidate generation is not final selection. All ten classes remain available for the delimited claim until collision adjudication is complete.

---

## G.20 Worked Test Routes

### G.20.1 Within-band COMPOSE

[`C17-LINEAR-01`](../03_cases/markdown/C17-LINEAR-01_Simple_Linear_Path.md) demonstrates a bounded path composition:

- source sequence and transitions are declared;
- ordering matters;
- the path claim changes under source variation;
- no automatic trajectory or path-dependence claim is inferred;
- Loss remains explicit.

### G.20.2 Below-floor DECOMPOSE

[`C28-OVERFINE-01`](../03_cases/markdown/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.md):

- finer distinctions are technically available;
- no further warranted reconstruction changes;
- continuation would create detail without purchase;
- mandatory stop preserves the sufficient coarser result.

### G.20.3 Above-ceiling COMPOSE

[`C17-MACRO-01`](../03_cases/markdown/C17-MACRO-01_Macro_Label_without_Traceable_Path.md):

- a macro-label is proposed;
- constitutive path structure is absent;
- source variation cannot constrain the label;
- the transformation fails.

### G.20.4 Bounded PROJECT_AS

[`C40-P1`](../03_cases/markdown/C40-P1_Trajectory_as_Bounded_Frame_Function.md):

- origin trajectory remains independently typed;
- target frame-function is context-bounded;
- source features carry the function;
- origin-type replacement is prohibited.

### G.20.5 Calibration-open PROJECT_AS

[`C49-CAL1`](../03_cases/markdown/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.md):

- a coherent bounded function remains;
- the exact threshold is unresolved;
- optional stop records present sufficiency;
- new sources later permit a new re-entry record.

### G.20.6 Genuine Non-Capture

[`C52-NC1`](../03_cases/markdown/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.md):

- rival bounded decompositions each capture different load;
- no source-supported priority or integration exists;
- forced synthesis would distort the source object;
- the whole capture claim receives `non_capture`.

---

## G.21 Completion Checklist

An Admissibility Band test is ready only where:

- the tested claim is delimited;
- the operation occurrence is correctly classified;
- PraxisPurchase is answered with a changed-reconstruction statement;
- TraceableLoad identifies constitutive source dependence;
- TypeIntegrity and continuity are explicit;
- context and validity scope are bounded;
- source variation and alternatives are tested;
- all five Loss fields are populated;
- source and calibration ceilings are declared;
- prior failures, stops, reductions, and capture limits remain preserved;
- Stop and Non-Capture are separately assessed;
- Claim Ceiling and Authority Ceiling are explicit;
- no scoring, compensation, first-match routing, or class ranking is used;
- candidate generation remains distinct from final Output Class selection.

The bounded Appendix-G result is:

```text
admissible_with_bounded_claim
```

---

## G.22 Handoff

Appendix G hands forward to:

```text
Appendix H
→ valid and invalid recurring transformation patterns

Appendix I
→ boundary and confusion cases between operations and Output Classes

Appendix N
→ integrated twelve-stage audit template
```
