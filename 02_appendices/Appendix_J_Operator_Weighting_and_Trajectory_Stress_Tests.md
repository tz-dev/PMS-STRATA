# Appendix J — Optional Operator-Weighting and Trajectory Stress Tests

**Status:** substantive bounded provisional completion  
**Primary prose owners:** Chapters 3, 11, 12, 14, 21, 22, 24, and 33–35  
**PMS operator authority:** external `PMS.yaml`  
**STRATA operation owner:** `../07_model/Operation_Registry.yaml`  
**Supporting operator reference:** `../04_reference/Operator_Index.md`  
**Case registry:** `../03_cases/Case_Index.md`

---

## J.1 Purpose and Boundary

Appendix J provides optional adversarial stress tests for two areas that are especially prone to inflation:

1. relative practical prominence among concrete Δ–Ψ operator occurrences within a Configuration; and
2. the construction, decomposition, and functional projection of Paths and Trajectories.

The tests are optional because they are not required in every STRATA Record. They become relevant only where a claim depends materially on an operator-occurrence profile, temporal accumulation, historical alternatives, Trajectory identity, Path Dependence, or a Trajectory-derived target function.

```text
stress test
≠ new operation
≠ new operator
≠ mandatory universal score
≠ proof of historical causality
```

Δ–Ψ identities, names, order, and dependencies remain owned exclusively by PMS Base. Appendix J never decomposes, renames, reorders, adds to, or replaces them.

---

## J.2 Operator Weighting Is Occurrence-Relative

Operator weighting describes the relative practical prominence of **concrete operator occurrences** in one declared Configuration, window, role field, or claim.

```text
prominent occurrence
≠ independent operator type

weighting profile
≠ revised Δ–Ψ grammar
```

A profile may state, for example, that one Ω- and Θ-bearing relation is especially load-bearing for continuation cost in a bounded window. It may not claim that Ω or Θ has become a new autonomous operator, moved in the PMS dependency order, or replaced another operator.

### J.2.1 Minimum profile declaration

```yaml
operator_occurrence_profile:
  configuration:
  temporal_window:
  role_or_relation_field:
  tested_claim:
  occurrence_carriers: []
  load_bearing_occurrences: []
  modulating_occurrences: []
  background_occurrences: []
  uncertain_occurrences: []
  excluded_profile_claims: []
  source_variation_tests: []
```

This is an explanatory stress-test view, not a new Shared Record field group.

### J.2.2 Qualitative, non-ordinal descriptors

Permissible descriptions include:

```text
load-bearing for this claim
materially contributory but insufficient alone
modulating timing, reach, or distribution
background relevance
uncertain under present sources
not discriminating for this claim
```

These are claim-relative role descriptions, not a universal scale.

Prohibited forms include:

```text
Ω = 0.8
Θ = 0.6
profile score = 74
operator rank 1 > operator rank 2
```

No number, percentage, or ranking may substitute for source-traceable differences.

---

## J.3 Operator-Profile Integrity Tests

### J.3.1 Occurrence/type test

Ask whether every weighted item is a concrete occurrence or occurrence relation rather than a canonical operator type.

Failure condition:

```text
operator type itself treated as variable component
→ TypeIntegrity failure
```

Case anchor: [`C28-OPTYPE-01`](../03_cases/markdown/C28-OPTYPE-01_Operator_Decomposition_Error.md).

### J.3.2 Configuration-boundedness test

A profile must declare the Configuration, temporal window, relevant roles, and claim. A prominence statement without those bounds becomes a free-standing typology.

```text
prominent here
≠ prominent everywhere
```

### J.3.3 Dependency-preservation test

Remove the profile wording and ask whether any Δ–Ψ identity, order, or dependency has been silently altered. If so, the profile has exceeded STRATA authority.

### J.3.4 Source-variation test

Materially vary or remove a proposed load-bearing occurrence while holding the target question sufficiently stable.

Possible findings:

- target difference disappears;
- target difference narrows;
- only timing or distribution changes;
- no discriminating change occurs;
- sources do not permit the variation test.

Only the first three can support a load-bearing or modulating role, and none proves universal causality.

### J.3.5 Rival-profile test

Construct at least one plausible rival profile or no-distinct-profile account. Ask whether the proposed profile actually discriminates the target reconstruction.

### J.3.6 Person-transfer prohibition

A configuration-level profile may not be transferred to a person or group as a type, diagnosis, moral rank, or durable trait.

Case anchor: [`C40-N7`](../03_cases/markdown/C40-N7_Person_Level_Type_Jump.md).

---

## J.4 Worked Operator-Weighting Stress Family

[`C35-A1`](../03_cases/markdown/C35-A1_PROJECT_AS_Operator_Weighting_Profile.md) tests a bounded Ω/Θ-prominent profile as a modulating target function.

The case carries only because:

- the source configuration and occurrence relations are independently declared;
- prominence is tied to a specific continuation-cost difference;
- varying Ω-related load or Θ-related accumulation changes the function claim;
- the origin remains a configuration profile rather than a PMS operator type;
- the target function is bounded to the declared context.

[`C38-N1`](../03_cases/markdown/C38-N1_PROJECT_AS_Origin_Type_Replacement_Failure.md) is the paired type-boundary countercase. It fails when the profile is rewritten as a canonical operator type.

[`C28-MODULATOR-01`](../03_cases/markdown/C28-MODULATOR-01_Modulator_or_New_Operator.md) preserves recurrence-level modulation without creating a new operator.

Together the cases establish:

```text
recurrent profile
→ may be analytically useful

recurrent profile
≠ new operator
≠ fourth STRATA operation
≠ person type
```

---

## J.5 Optional Operator-Combination Test Vectors

The following combinations are **test vectors only**. Their symbols and dependencies remain owned by PMS Base; Appendix J does not redefine them.

### J.5.1 `Α + Θ`

Test whether an attractor-bearing occurrence and temporal accumulation jointly alter recurrence, continuation friction, or return probability in the declared source field.

Reject the stronger claim where recurrence can be explained by current structure alone or where Θ supplies only chronology without accumulated load.

### J.5.2 `Ω + Θ`

Test whether asymmetry accumulates across time in a way that changes access, exposure, delay cost, exit burden, or repair capacity.

Reject where unequal outcomes are merely observed without a source-supported cumulative relation.

### J.5.3 `Ψ + Θ`

Test whether bindings persist, sediment, or alter breach/reopening costs across a declared temporal window.

Reject moral, personal, or permanent-binding inferences not carried by the sources.

### J.5.4 `Λ + Θ`

Test whether a source-supported Non-Event remains structurally active through expectation, blockage, delay, or later residue.

Reject where the claim is based only on missing records or retrospective absence.

### J.5.5 `Φ`-bearing recontextualization

Where a Φ occurrence is separately warranted, test whether it recontextualizes earlier material. Do not convert every frame change into a Φ occurrence or every recontextualization into `PROJECT_AS`.

These test vectors may coexist in one source field. They do not form a closed typology or permit score-based profile comparison.

---

## J.6 Path and Trajectory Stress-Test Entry Conditions

Before stress-testing a Trajectory claim, declare:

- source occurrences and chronology;
- warranted transition set;
- selection and exclusion;
- branch statuses and relevant alternatives;
- claimed historical load;
- later effect or target-side difference;
- source and target windows;
- present-condition rivals;
- all five Loss fields.

If only chronology is available, stop at chronology. If transitions are warranted but sustained historical load is not, stop at Path. If historical load is supported but order sensitivity is not, withhold strong Path Dependence.

---

## J.7 Trajectory Identity Stress Tests

### J.7.1 Remove-one-transition test

Remove or reverse one proposed load-bearing transition.

Ask whether:

- the Path remains the same;
- the Trajectory identity changes;
- only narrative detail changes;
- the claim becomes underdetermined.

A claim insensitive to every source transition may be a macro-label rather than a traceable Trajectory.

Case anchors: [`C17-LINEAR-01`](../03_cases/markdown/C17-LINEAR-01_Simple_Linear_Path.md) and [`C17-MACRO-01`](../03_cases/markdown/C17-MACRO-01_Macro_Label_without_Traceable_Path.md).

### J.7.2 Similar-end-state test

Hold the endpoint approximately constant while varying the historical route.

[`C17-HISTORY-01`](../03_cases/markdown/C17-HISTORY-01_Similar_End_States_Different_Histories.md) demonstrates that similar present states may carry different path-relative loads in a specified dimension.

```text
same endpoint
≠ same history
≠ same present reconstruction automatically
```

### J.7.3 Present-state sufficiency rival

Construct a rival explanation from present conditions alone. The historical claim carries only where the Trajectory adds source-traceable discrimination.

### J.7.4 False-teleology test

Ask whether the later outcome has been imported backward as the purpose or inevitable direction of earlier events.

Case anchor: [`C17-TEL-01`](../03_cases/markdown/C17-TEL-01_Teleological_Composition.md).

### J.7.5 Omitted-asymmetry test

Reinsert a source-supported asymmetry omitted from the composition. If the resulting role, cost, or continuation structure changes, the original Trajectory may fail.

Case anchor: [`C17-OMEGA-01`](../03_cases/markdown/C17-OMEGA-01_Composition_through_Omitted_Asymmetry.md).

### J.7.6 Central Non-Event test

Remove the proposed Λ-bearing Non-Event and ask whether the Path or later structural load changes.

Case contrast: [`C17-LAMBDA-01`](../03_cases/markdown/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.md) versus [`C17-FALSEL-01`](../03_cases/markdown/C17-FALSEL-01_False_Central_Non_Event.md).

---

## J.8 Historical Alternative Status Tests

At each claimed branch point, classify alternatives only where source support permits:

```text
realized
blocked
aborted
deferred
rejected
unavailable
open continuation
```

Protected distinctions:

```text
available
≠ retrospectively imaginable

rejected
≠ blocked

blocked
≠ impossible

aborted
≠ never begun

deferred
≠ uninterrupted continuation
```

A branch may be visualized in the Reader only where its status, historical cut, source basis, and temporal window are declared.

```text
visualized branch
≠ historically available branch
```

Case anchor: [`C17-BRANCH-01`](../03_cases/markdown/C17-BRANCH-01_Branching_Path.md).

---

## J.9 Trajectory versus Attractor-Function

[`C17-ATTR-01`](../03_cases/markdown/C17-ATTR-01_Trajectory_or_Attractor.md) preserves a Trajectory while withholding an Attractor-function claim. [`C40-P3`](../03_cases/markdown/C40-P3_Recurrent_Trajectory_Form_as_Attractor_Function.md) tests the stronger contextual function separately.

The discriminating questions are:

- Is recurrence present in the source Trajectory?
- Does the recurrent form change continuation friction in the target context?
- Can present conditions alone explain the recurrence?
- Does source variation weaken or remove the target function?
- Is the function bounded without changing the origin type?

```text
recurrent Trajectory
≠ Attractor-function automatically
```

---

## J.10 Trajectory as Frame-Function or Macro-Event

### J.10.1 Frame-function stress

[`C40-P1`](../03_cases/markdown/C40-P1_Trajectory_as_Bounded_Frame_Function.md) tests whether a Trajectory structures relevance and interpretation in a declared target context.

The function fails where only retrospective narration changes or the target scene is unchanged under source variation.

### J.10.2 Macro-Event stress

[`C40-P2`](../03_cases/markdown/C40-P2_Trajectory_as_Macro_Event.md) treats a source Trajectory as a bounded Macro-Event function while preserving the origin Trajectory.

The stress test must preserve:

```text
periodization
+ constitutive transitions
+ internal heterogeneity
+ Loss
```

A broad label without traceable internal Path fails, as shown by [`C17-MACRO-01`](../03_cases/markdown/C17-MACRO-01_Macro_Label_without_Traceable_Path.md).

---

## J.11 Decomposing Trajectories

[`C28-TRAJECTORY-01`](../03_cases/markdown/C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.md) demonstrates same-reference reopening into supported subpaths, relations, internal temporality, and residual binding.

Stress questions:

- Does the source Trajectory remain the reference object?
- Are components source-supported rather than retrospectively invented?
- Does the decomposition preserve residual binding?
- Is the finer reconstruction still above the Relevance Floor?
- Has a target function been smuggled into DECOMPOSE?

[`C17-RES-01`](../03_cases/markdown/C17-RES-01_Path_or_Resolution_Drift.md) provides a resolution-neutral contrast. [`C28-OVERFINE-01`](../03_cases/markdown/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.md) provides the mandatory-Stop boundary.

---

## J.12 Order Dependence versus Strong Path Dependence

A weak order-dependent effect may be bounded to one dimension without supporting a total historical-determination claim.

Stress protocol:

1. declare the dimension of claimed dependence;
2. identify source-supported alternative orderings;
3. hold endpoints or current conditions sufficiently stable;
4. test which later relation changes;
5. state where the comparison is impossible or underdetermined;
6. preserve present-condition rivals.

[`C17-WEAKPD-01`](../03_cases/markdown/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.md) is the bounded positive anchor.

```text
some order sensitivity
≠ global Path Dependence
≠ determinism
```

---

## J.13 False-Trajectory Diagnostic Matrix

| Proposed form | Diagnostic defect | Likely preserved remainder | Case anchor |
|---|---|---|---|
| chronology as Path | no warranted transitions | chronology/sequence | `C17-CHRON-01` |
| teleological Trajectory | later outcome defines prior direction | events and chronology | `C17-TEL-01` |
| macro-label | absent constitutive trace | broad descriptive label | `C17-MACRO-01` |
| omitted asymmetry | load-bearing role/cost relation excluded | partial event field | `C17-OMEGA-01` |
| false central Non-Event | missing expectation/blockage basis | event field without Λ claim | `C17-FALSEL-01` |
| repeated pattern as strong dependence | alternatives/order sensitivity weak | repeated pattern with bounded claim | `C17-WEAKPD-01` |
| Trajectory as Attractor automatically | no separate target-function test | Trajectory only | `C17-ATTR-01` |

The matrix suggests tests; it does not select Output Classes mechanically.

---

## J.14 Graph and Reader Stress Boundary

The Reader may display:

- source chronology;
- realized Path;
- branch statuses;
- Trajectory segments;
- operator-occurrence profiles;
- historical carriers;
- source variations;
- alternative histories;
- Loss and uncertainty;
- blocked or stopped continuations.

It must preserve:

```text
rendered prominence
≠ operator authority

line thickness
≠ evidential strength automatically

3D depth
≠ ontological level

visible branch
≠ historical availability
```

Any visual encoding of operator weighting must use declared qualitative roles or source-backed categories, never inferred numerical weights.

---

## J.15 Optional Stress-Test Worksheet

```yaml
trajectory_or_profile_stress_test:
  claim_id:
  source_reference:
  temporal_window:
  configuration_or_trajectory:
  operator_occurrence_profile:
    load_bearing: []
    modulating: []
    background: []
    uncertain: []
  transition_set: []
  branch_statuses: []
  historical_load_claim:
  present_state_rival:
  source_variation_tests: []
  omitted_relation_tests: []
  false_trajectory_tests: []
  path_dependence_dimension:
  target_function_if_separately_tested:
  loss:
    preserved: []
    compressed: []
    excluded: []
    uncertain: []
    irrecoverable: []
  required_new_operation_records: []
  bounded_findings: []
  prohibited_inferences: []
```

The worksheet is a view over existing Record duties. It is not a new schema.

---

## J.16 Completion Checklist

An operator-weighting or Trajectory stress test is ready only where:

- all weighted items are concrete occurrences or relations;
- Δ–Ψ identity, order, and dependencies remain untouched;
- no score, rank, percentage, or compensatory weight is used;
- Configuration, temporal window, roles, and claim are declared;
- load-bearing and modulating occurrences are distinguished;
- source variation and rival profiles are tested;
- chronology, Path, Trajectory, and Path Dependence remain separate;
- historical alternatives carry declared statuses and source support;
- present-condition rivals are considered;
- false-teleology, omitted-asymmetry, macro-label, and Non-Event confusions are tested where relevant;
- any target function receives a separate `PROJECT_AS` occurrence;
- any finer reopening receives a separate `DECOMPOSE` occurrence;
- all five Loss fields remain explicit;
- graph or Reader visibility is not treated as evidence or authority.

The bounded Appendix-J result is:

```text
admissible_with_bounded_claim
```

---

## J.17 Handoff

Appendix J hands forward to:

```text
Appendix K
→ cross-domain projection and analogy stress tests

Appendix L
→ decomposition limits and non-operator remainders

Appendix M
→ consolidated case and countercase index

Reader
→ optional source-backed profile, Path, Trajectory, branch, Loss, and 3D views
```
