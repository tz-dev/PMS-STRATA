# PMS-STRATA Confusion-Case Companion Template

**Template status:** reusable Markdown companion; no theory authority  
**Record rule:** every operation occurrence discussed here requires its own schema-valid YAML Transformation Record  
**Package rule:** use one shared package narrative only where several separately recorded occurrences share a source, comparison, or chain context

---

## 1. Case Identity

```yaml
case_id:
title:
case_class: confusion_case
record_ids: []
package_id:
primary_boundary_family:
```

State whether this document is:

- the companion for one operation Record; or
- a shared package narrative linking multiple separately recorded occurrences.

```text
one Markdown package
≠ one merged operation Record
```

---

## 2. Tested Claim and Comparison Basis

**Tested claim**

> [one delimited claim]

**Shared source or comparison basis**

- Source reference:
- Source type:
- Frame:
- Granularity:
- Relative level:
- Temporal scope:
- Source scope:
- Same-source comparison available: yes / no
- Comparison limitation:

---

## 3. Competing Candidates

### Candidate A

- Label:
- Proposed operation or class:
- Initial plausibility:
- Required source burden:
- Claim effect if retained:

### Candidate B

- Label:
- Proposed operation or class:
- Initial plausibility:
- Required source burden:
- Claim effect if retained:

### Candidate C, where necessary

- Label:
- Proposed operation or class:
- Initial plausibility:
- Required source burden:
- Claim effect if retained:

Do not invent extra candidates merely to create symmetry.

---

## 4. Boundary Classification

Check all that apply and explain:

```yaml
boundary_classification:
  object_or_coordinate:
    operator_type_vs_occurrence_vs_composite:
    frame_vs_granularity_vs_relative_level:
    sequence_vs_path_vs_trajectory:
    trajectory_vs_path_dependence:
    missing_information_vs_non_event:
  operation:
    compose_vs_listing:
    compose_vs_project_as:
    decompose_vs_compose:
    decompose_vs_project_as:
    project_as_vs_recontextualization:
    project_as_vs_analogy:
    project_as_vs_origin_type_replacement:
  continuity:
    reference:
    type:
    function:
    temporal:
    loss:
    authority:
  result:
    output_class_collision_ids: []
    stop_vs_failure_vs_non_capture:
  chain:
    handoff_or_inversion_confusion:
```

---

## 5. Discriminating Question

> [the one question whose answer materially separates the candidates]

Examples:

- Is a new composite object being formed, or is an existing object assigned a bounded target function?
- Does finer reconstruction retain the same reference object and source function?
- Does one coherent usable claim remain, or only separable partial captures?
- Is continuation prohibited, or did the declared operation itself fail?

---

## 6. Decisive Source, Type, or Boundary Condition

- Decisive source feature:
- Constitutive Source Trace:
- Type-integrity condition:
- Continuity condition:
- Counterfactual/source-variation test:
- Claim Ceiling:
- Authority Ceiling:

Explain why the condition is decisive without claiming causal exclusivity unless externally warranted.

---

## 7. Operation Records Required

| Record ID | Operation | Claim | Source | Target | Local result | Selected class |
|---|---|---|---|---|---|---|
| `[ID]` | `COMPOSE / DECOMPOSE / PROJECT_AS` |  |  |  |  |  |

Each row must link to one YAML Record and one same-basename Markdown companion.

---

## 8. Claim Splitting and Candidate Preservation

```yaml
claim_splitting:
  required:
  reason:
  retained_claims: []
  rejected_or_withheld_claims: []
  untested_successor_claims: []

preserved_non_selected_findings: []
```

Do not select one class for an undifferentiated whole claim where material subclaims receive different outcomes.

---

## 9. Fourteen Output-Class Boundary Check

Assess only applicable boundaries:

```yaml
class_boundaries:
  admissible_vs_bounded_claim:
  bounded_claim_vs_provisional:
  bounded_claim_vs_partial:
  partial_vs_provisional:
  provisional_vs_resolution_neutral:
  provisional_vs_non_capture:
  partial_vs_non_capture:
  claim_reduction_vs_bounded_claim:
  claim_reduction_vs_mandatory_stop:
  mandatory_stop_vs_failed_transformation:
  failed_transformation_vs_non_capture:
  mandatory_stop_vs_non_capture:
  resolution_neutral_vs_claim_reduction:
  analogy_only_vs_failed_projection:
```

For every applicable boundary, record:

- why both candidates were plausible;
- which constitutive condition discriminates them;
- whether claim splitting is required;
- which non-selected finding remains preserved.

No first-match or ranking rule is permitted.

---

## 10. Loss

For each operation occurrence, preserve a separate five-field Loss declaration:

```yaml
loss:
  preserved: []
  compressed: []
  excluded: []
  uncertain: []
  irrecoverable: []
```

Do not merge or average Loss across Records.

---

## 11. Stop, Failure, and Non-Capture

```yaml
boundary_result:
  mandatory_stop:
    reached:
    condition:
    preserved_result:
    reentry_condition:
  failed_transformation:
    reached:
    decisive_failure:
    preserved_source_material:
    possible_new_claims: []
  non_capture:
    asserted:
    adequate_bounded_attempts: []
    partial_captures: []
    persistent_remainder:
    distortion_if_forced:
    reentry_condition:
```

```text
missing information
≠ failure
≠ stop
≠ non-capture
```

---

## 12. Final Adjudication

- Selected Output Class:
- Route ID:
- Local operation result:
- Claim disposition:
- Validity scope:
- Excluded reach:
- Selection rationale:
- Preserved non-selected findings:

The class belongs to the delimited tested claim, not to the source object globally.

---

## 13. Re-entry and Successor Claims

- Material change required for re-entry:
- New sources required:
- New context or target required:
- New operation Record required:
- Prior result preserved:

```text
new transformation
= new testable claim
```

---

## 14. Claim and Authority Boundary

This case does not establish:

- empirical or causal truth beyond its sources;
- semantic or normative validity;
- person, group, clinical, moral, political, or legal classification;
- application authority;
- new PMS operator identity;
- a fourth STRATA operation;
- an eleventh Output Class;
- class hierarchy or universal precedent.

```yaml
governance:
  authority_inheritance: prohibited
```

---

## 15. Artifact Links

- YAML Record(s):
- Markdown Companion(s):
- Shared Package Narrative, if any:
- Canonical chapter owner(s):
- Appendix I boundary reference:
- Formal routing owner:

---

## 16. Completion Check

- [ ] candidates stated fairly
- [ ] comparison basis declared
- [ ] operation identity established
- [ ] object and coordinate distinctions preserved
- [ ] applicable class collisions adjudicated
- [ ] claims split where necessary
- [ ] all five Loss fields present per occurrence
- [ ] Stop, Failure, and Non-Capture separately assessed
- [ ] earlier findings preserved
- [ ] re-entry condition explicit
- [ ] authority boundary explicit
- [ ] YAML/Markdown links resolve
