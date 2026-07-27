# C17-HISTORY-01 — Similar End States, Different Histories

**Case class:** `positive_case`  
**Chapter owner:** Chapter 17 — PATH Cases, Countercases, and Local Audit  
**Operation:** `COMPOSE`  
**Local result:** `admissible dimension-specific Path-Dependence claim across similar endpoints`  
**Canonical Output Class:** `admissible_with_bounded_claim`  
**Record status:** `supported`  
**YAML record:** [`../yaml/C17-HISTORY-01_Similar_End_States_Different_Histories.yaml`](../yaml/C17-HISTORY-01_Similar_End_States_Different_Histories.yaml)  
**Canonical chapter section:** [`../../01_blocks/02_part_i_path.md#17-5-case-4-similar-end-states-different-histories`](../../01_blocks/02_part_i_path.md#17-5-case-4-similar-end-states-different-histories)

---

## 1. Case Statement

Two service units with the same formal weekly-allocation endpoint remain historically different in present burden, reversibility, and residual repair because their source-sensitive Paths differ in review timing, workaround persistence, asymmetric load, and repair sequence.

This is a synthetic method-and-record test. It is not external empirical evidence, domain calibration, causal proof, normative judgment, or application authority.

```text
case readability
≠ empirical truth
≠ target-function assignment
≠ authority increase
```

## 2. Source and Claim Boundary

**Reference boundary:** Only the two synthetic service-unit Paths from their declared baselines to the formally similar weekly-allocation endpoints.

**Frame:** synthetic paired service-unit history comparison frame

**Granularity:** parallel configuration, transition, Non-Event, and residual-load granularity

**Relative level:** comparative path-dependence object relative to two constituent unit Paths

**Temporal scope:** Synthetic interval A0–A3 and B0–B5.

**Source scope:** Exactly the two typed parallel histories, their endpoint-similarity declaration, and the present residual burden, reversibility, and repair-corridor observations.

**Validity scope:** Valid only as the dimension-specific comparison of the two synthetic Paths and their present historical load.

### Excluded reach

- No whole-object claim that every present feature is historically determined.
- No claim that the endpoint protocols are technically different in every respect.
- No causal necessity, motive, institutional ranking, legitimacy, or target function.
- No prediction that either unit will continue on a fixed course.

### Claim Ceiling

- **Asserted relation:** Endpoint similarity coexists with source-sensitive historical difference in present burden, reversibility, and residual repair dimensions.
- **Reach:** The two declared unit histories and the three present dependence dimensions only.
- **Precision:** Parallel ordering, early versus deferred review, explicit versus workaround-mediated redistribution, accumulated Ω-load, late repair, and present residue.
- **Dependence strength:** Strong historical indispensability is supported only for present burden, reversibility, and residual repair; current technical protocol status remains adequately describable from the present endpoint.
- **Rationale:** The packet supports dimension-specific Path Dependence across similar endpoints and does not support total historical determination, causal necessity, quality ranking, target function, or authority.

## 3. Typed Reconstruction

### Source objects

| Object | Type | Description | Source pointer |
|---|---|---|---|
| `configuration.history.a-baseline` | `configuration` | Unit A baseline allocation configuration. | `case://pms-strata/configuration.history.a-baseline` |
| `transition.history.a-review` | `transition as object` | Unit A early review and explicit redistribution transition. | `case://pms-strata/transition.history.a-review` |
| `configuration.history.a-endpoint` | `configuration` | Unit A weekly-allocation protocol endpoint with low backlog. | `case://pms-strata/configuration.history.a-endpoint` |
| `configuration.history.b-baseline` | `configuration` | Unit B baseline allocation configuration. | `case://pms-strata/configuration.history.b-baseline` |
| `non-event.history.b-review` | `non-event structure` | Unit B expected review not realized in the declared window. | `case://pms-strata/non-event.history.b-review` |
| `subpath.history.b-workaround` | `subpath` | Centralized workaround persisting after the missed review. | `case://pms-strata/subpath.history.b-workaround` |
| `operator.history.b-omega` | `operator-typed occurrence` | Uneven workload and exit-cost concentration in Unit B. | `case://pms-strata/operator.history.b-omega` |
| `transition.history.b-repair` | `transition as object` | Late redistribution reducing but not erasing backlog and exit cost. | `case://pms-strata/transition.history.b-repair` |
| `configuration.history.b-endpoint` | `configuration` | Unit B weekly-allocation protocol endpoint with residual backlog and elevated exit cost. | `case://pms-strata/configuration.history.b-endpoint` |

### Constitutive relations

| Relation | From | To | Description |
|---|---|---|---|
| `relation.history.a-route` | `configuration.history.a-baseline` | `configuration.history.a-endpoint` | Early review and explicit redistribution connect Unit A baseline to the low-residue endpoint. |
| `relation.history.b-delay-workaround` | `non-event.history.b-review` | `subpath.history.b-workaround` | The missed review leaves the centralized workaround in place. |
| `relation.history.b-workaround-omega` | `subpath.history.b-workaround` | `operator.history.b-omega` | Workaround persistence accumulates uneven workload and exit cost. |
| `relation.history.b-omega-repair` | `operator.history.b-omega` | `transition.history.b-repair` | Late redistribution reduces but does not erase accumulated burden. |
| `relation.history.endpoint-comparison` | `configuration.history.a-endpoint` | `configuration.history.b-endpoint` | The endpoints share a formal protocol label while differing in present burden, reversibility, and repair residue. |

### Temporal content

**Starting configuration:** Two synthetic service units with separately declared baseline configurations.

**Transitions:**

- Unit A early review and explicit redistribution
- Unit B missed review
- Unit B workaround persistence
- Unit B asymmetric burden accumulation
- Unit B late partial repair
- paired endpoint comparison

**Positive events:**

- early review
- explicit redistribution
- workaround activity
- late partial repair

**Non-Events:**

- Unit B expected review not realized

**Branches and alternatives:** Endpoint-only comparison, parallel Paths, and No-Composition remain available.

## 4. Operation Decision

**Justification:** The paired source field preserves two traceable histories and shows that identical endpoint labels do not erase dimension-specific present historical load.

**Expected praxeological difference:** Historical comparison changes reconstruction of present backlog burden, exit reversibility, and repair corridor while leaving current technical protocol similarity intact.

**Selection Rule:** Include the load-bearing structures from both unit Paths, the endpoint-similarity relation, and present residual dimensions; exclude motive, quality ranking, and unrelated technical detail.

**Ordering Rule:** Use two parallel orders A0 < A1 < A3 and B0 < B1–B2 < B2–B3 < B3–B4 < B4 < B5, then compare the two endpoints without collapsing their histories.

**Formation Rule:** Form a comparative Path-Dependence object only where a present dimension changes under bounded substitution of one unit history for the other while formally similar endpoint features remain fixed.

**Target typing:** `comparative path-dependence object`

```text
typed source structures
+ explicit selection
+ warranted order
+ formation rule
+ constitutive relations
+ complete Loss
→ bounded COMPOSE candidate
```

## 5. Admissibility Band Findings

**Praxeological Purchase:** `gain` — Historical comparison changes reconstruction of present backlog burden, exit reversibility, and repair corridor while leaving current technical protocol similarity intact.

**Traceability Ceiling:** `within_ceiling` — The present burden, reversibility, and residual-repair differences remain reconstructible from the early-review route versus the delayed-review/workaround/Ω/late-repair route.

**Counterfactual Sensitivity:** `strongly_sensitive` — Substituting Unit A history for Unit B while holding the endpoint protocol label fixed removes the declared backlog, exit-cost, and repair-residue difference; removing fine historical detail outside these dimensions does not alter the bounded claim.

The three findings are non-compensatory. Formal completeness, source volume, or graph density cannot substitute for Purchase or TraceableLoad.

## 6. Five-Part Loss

### `preserved`

- **parallel histories:** Both unit routes, the missed review, workaround, Ω-load, repair, endpoints, and endpoint similarity remain explicit. **Reason:** They are constitutive to the bounded comparison. **Re-entry:** Changing either route requires a new record.
- **dependence dimensions:** Present burden, reversibility, and residual repair remain separated from technically similar endpoint features. **Reason:** The claim is dimension-specific. **Re-entry:** Broader dependence requires separate testing.

### `compressed`

- **local implementation detail:** Fine local actions inside each unit are compressed into load-bearing configurations and transitions. **Reason:** The comparison does not require every micro-event. **Re-entry:** A finer reconstruction requires DECOMPOSE or a new record.

### `excluded`

- **total determination and quality ranking:** Whole-object historical determination, motive, causal necessity, quality, legitimacy, prediction, and target functions are excluded. **Reason:** They exceed the source and authority ceilings. **Re-entry:** Reentry requires separate claims and warrant.

### `uncertain`

- **fine burden allocation:** Exact internal distribution of backlog and exit cost remains uncertain. **Reason:** The packet supports a difference but not complete allocation. **Re-entry:** Preserve bounded uncertainty.

### `irrecoverable`

- **actor-level causal mechanism:** Actor-level causal mechanisms cannot be recovered from the synthetic packet. **Reason:** They were not encoded. **Re-entry:** No causal claim without new sources.

## 7. Alternatives

### Rival compositions

- **`alternative.history.endpoint-only` — not_selected:** Compare only the two present protocol configurations. **Burden:** Preserves endpoint similarity but cannot represent present historical load in the declared dimensions. **Rationale:** The bounded historical-difference claim has additional source-sensitive Purchase.
- **`alternative.history.parallel-paths` — not_selected:** Retain two independent Paths without composing a comparative dependence object. **Burden:** Preserves both histories but withholds the tested present-dimension comparison. **Rationale:** The packet supports the bounded comparative claim.

### Rival decompositions

- None declared.

### Rival projections

- None declared.

### No-Transformation

- **`alternative.history.no-composition` — not_selected:** Retain all source structures and endpoint observations without an integrated comparative object. **Burden:** Preserves source material while withholding any dependence claim. **Rationale:** The three specified present dimensions remain source-sensitive.

### Non-Translation

- None declared.

### Unresolved

- None declared.

## 8. Counterfactual Sensitivity

Substituting Unit A history for Unit B while holding the endpoint protocol label fixed removes the declared backlog, exit-cost, and repair-residue difference; removing fine historical detail outside these dimensions does not alter the bounded claim.

Any change in source membership, order, frame, granularity, relative level, target class, compression, or target function is a new testable claim. It does not retroactively repair or erase this result.

## 9. Local Admissibility Audit

| Stage | Completion | Finding | Unresolved |
|---|---|---|---|
| Source and Claim Entry | `complete` | Source and claim packet complete: The bounded claim, source field, scope, ceilings, and authority boundary are explicitly declared. | none |
| Operation Classification | `complete` | Operation correctly classified as COMPOSE: Multiple typed source structures are formed into a new temporal composite through explicit selection, ordering, formation, and constitutive relations. | none |
| Praxeological Relevance Floor | `complete` | Praxeological Purchase established: Historical comparison changes reconstruction of present backlog burden, exit reversibility, and repair corridor while leaving current technical protocol similarity intact. | none |
| Praxeological Traceability Ceiling | `complete` | Source-to-result dependency remains reconstructible: The present burden, reversibility, and residual-repair differences remain reconstructible from the early-review route versus the delayed-review/workaround/Ω/late-repair route. | none |
| Continuity and Type Integrity | `complete` | Type, reference, temporal, and functional boundaries preserved: Source objects retain their origin typings; the target is a derived temporal composite; no contextual function is inferred. | none |
| Counterfactual Sensitivity | `complete` | Load-bearing changes alter or defeat the claim: Substituting Unit A history for Unit B while holding the endpoint protocol label fixed removes the declared backlog, exit-cost, and repair-residue difference; removing fine historical detail outside these dimensions does not alter the bounded claim. | none |
| Loss and Selection | `complete` | Selection and five-part Loss are explicit: Included and omitted elements, retained distinctions, compression, uncertainty, and irrecoverability are recorded without a lossless presumption. | none |
| Alternatives | `complete` | Material alternatives are preserved: Endpoint-only comparison, two independent Paths without a dependence claim, and No-Composition remain available; total historical determination is not selected. | none |
| Source and Calibration Limits | `complete` | Source and calibration limits declared: The synthetic packet discriminates the tested positive case from defined mutations but supplies no external empirical calibration. | none |
| Anti-Immunization | `complete` | No failed claim is repaired by relabeling: Any changed source set, order, frame, granularity, target class, or target function requires a new testable claim. | none |
| Stop and Non-Capture | `complete` | Stop and Non-Capture assessed and not reached: An adequate bounded composite remains; stronger excluded claims remain prohibited rather than silently retained. | none |
| Claim and Authority Ceiling | `complete` | Claim and authority ceilings maintained: The result remains synthetic, bounded, non-causal, non-normative, non-diagnostic, and non-authoritative. | none |

**Local audit result:** `pass`  
**Stages complete:** `12/12`  
**Warnings:** `0`  
**Errors:** `0`

This local audit tests the declared case and record. It does not replace Chapter 17's later integrated PATH Local Audit or Chapter 53's system-wide audit.

## 10. Result and Canonical Mapping

**Operation-specific result:** Two formally similar endpoints remain historically different in three present dimensions under a source-sensitive paired Path comparison.

**Local result:** `admissible dimension-specific Path-Dependence claim across similar endpoints`

**Selected canonical Output Class:** `admissible_with_bounded_claim`

**Mapping rationale:** Purchase and TraceableLoad support a paired comparative object, but the claim must remain materially narrowed to the tested present dimensions.

**Claim disposition:** `maintained` — The dimension-specific dependence claim is maintained; the broader total-determination claim is not retained.

**Path-Dependence finding:** supported only for present burden, reversibility, and residual repair; not supported for every present feature or technical protocol identity.

## 11. Stop, Non-Capture, and Governance

**Stop assessment:** `not reached` — The bounded composition remains above the Relevance Floor and below the Traceability Ceiling; no integrity failure makes continuation inadmissible.

**Non-Capture assessment:** `not reached` — The record adequately captures the bounded temporal composite while preserving exclusions, uncertainty, alternatives, and stronger unclaimed routes.

**Governance boundary:** No target function, causality, person judgment, legitimacy, sanction, application authority, or authority inheritance.

```yaml
governance:
  authority_inheritance: prohibited
```

## 12. Counterpressure and Re-entry

Countercase and confusion-case duties linked to this case:

- `C17-WEAKPD-01`
- `C17-OMEGA-01`

A later frame, finer resolution, new composition, or projected function must be recorded as a separate claim and operation occurrence. This case grants no authority to skip those tests.

---

**YAML record:** [`../yaml/C17-HISTORY-01_Similar_End_States_Different_Histories.yaml`](../yaml/C17-HISTORY-01_Similar_End_States_Different_Histories.yaml)  
**Case index:** [`../Case_Index.md`](../Case_Index.md)  
**Authority:** case artifact below canonical prose; no independent theory authority.
