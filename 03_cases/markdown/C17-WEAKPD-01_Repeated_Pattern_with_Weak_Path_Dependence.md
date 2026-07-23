# C17-WEAKPD-01 — Repeated Pattern with Weak Path Dependence

**Case class:** `positive_case`  
**Chapter owner:** Chapter 17 — PATH Cases, Countercases, and Local Audit  
**Operation:** `COMPOSE`  
**Local result:** `admissible repeated-pattern Path with weak order dependence`  
**Canonical Output Class:** `admissible_with_bounded_claim`  
**Record status:** `supported`  
**YAML record:** [`../yaml/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.yaml`](../yaml/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.yaml)  
**Canonical chapter section:** [`../../01_blocks/02_part_i_path.md#17-6-case-5-repeated-pattern-with-weak-path-dependence`](../../01_blocks/02_part_i_path.md#17-6-case-5-repeated-pattern-with-weak-path-dependence)

---

## 1. Case Statement

Eight recurring queue-allocation cycles form a bounded repeated-pattern Path with weak order dependence, while the current scheduling rule, role access, and queue state remain sufficient to reconstruct the next assignment without the full cycle history.

This is a synthetic method-and-record test. It is not external empirical evidence, domain calibration, causal proof, normative judgment, or application authority.

```text
case readability
≠ empirical truth
≠ target-function assignment
≠ authority increase
```

## 2. Source and Claim Boundary

**Reference boundary:** Only the synthetic queue-allocation cycles W1–W8 and current carrier conditions at W9.

**Frame:** synthetic weekly queue-allocation pattern frame

**Granularity:** cycle-cluster, current-rule, role-access, and queue-state granularity

**Relative level:** repeated-pattern Path relative to weekly cycles and current carrier conditions

**Temporal scope:** Synthetic weekly cycles W1–W8 plus current state W9.

**Source scope:** Exactly the early and later cycle clusters, current scheduling rule, role-access configuration, current queue state, and next-assignment transition.

**Validity scope:** Valid only as the bounded repeated-pattern Path and weak historical contribution described by this record.

### Excluded reach

- No strong Path-Dependence or historical-indispensability claim.
- No claim that repetition creates an Attractor target function.
- No prediction beyond the declared next-assignment conditions.
- No quality, person, legitimacy, intervention, or authority claim.

### Claim Ceiling

- **Asserted relation:** Repeated cycles establish a bounded Path and weak order effect, while current carriers explain most present continuation.
- **Reach:** Cycles W1–W8, current rule/access/queue conditions, and the declared next assignment.
- **Precision:** Recurrence, one bounded early order effect, current-state sufficiency, and absence of strong historical indispensability.
- **Dependence strength:** Weak order dependence only; removing the first four cycles reduces historical description but does not materially change current role distribution, cost structure, or reachable next assignment.
- **Rationale:** The packet supports recurrence and weak dependence but not strong Path Dependence, an Attractor function, prediction, causal mechanism, or authority.

## 3. Typed Reconstruction

### Source objects

| Object | Type | Description | Source pointer |
|---|---|---|---|
| `subpath.weakpd.early` | `subpath` | Early weekly allocation cycles W1–W4. | `case://pms-strata/subpath.weakpd.early` |
| `subpath.weakpd.later` | `subpath` | Later weekly allocation cycles W5–W8. | `case://pms-strata/subpath.weakpd.later` |
| `operator.weakpd.rule` | `operator-typed occurrence` | Current scheduling-rule occurrence governing assignment order. | `case://pms-strata/operator.weakpd.rule` |
| `configuration.weakpd.access` | `configuration` | Current role-access configuration. | `case://pms-strata/configuration.weakpd.access` |
| `configuration.weakpd.queue` | `configuration` | Current queue state before assignment. | `case://pms-strata/configuration.weakpd.queue` |
| `transition.weakpd.next` | `transition as object` | Next assignment transition generated from current carriers. | `case://pms-strata/transition.weakpd.next` |

### Constitutive relations

| Relation | From | To | Description |
|---|---|---|---|
| `relation.weakpd.recurrence` | `subpath.weakpd.early` | `subpath.weakpd.later` | The later cycles reproduce the same bounded assignment pattern established in the early cluster. |
| `relation.weakpd.rule-queue` | `operator.weakpd.rule` | `configuration.weakpd.queue` | The current rule orders the current queue under the declared frame. |
| `relation.weakpd.access-next` | `configuration.weakpd.access` | `transition.weakpd.next` | Current role access constrains the next assignment. |
| `relation.weakpd.queue-next` | `configuration.weakpd.queue` | `transition.weakpd.next` | The current queue state supplies the item selected by the rule and access configuration. |

### Temporal content

**Starting configuration:** Early recurring allocation cycles W1–W4.

**Transitions:**

- early recurrence
- later recurrence
- current carrier configuration
- next assignment

**Positive events:**

- weekly assignments W1–W8
- next assignment W9+

**Non-Events:**

- None declared.

**Branches and alternatives:** Path-only, chronology, No-Composition, and later PROJECT_AS routes remain separate.

## 4. Operation Decision

**Justification:** The cycles support a repeated-pattern Path, while explicit present carriers permit a separate current-state-sufficiency test that limits the dependence claim.

**Expected praxeological difference:** The history identifies recurrence and initial stabilization, while the present carriers show that strong historical indispensability is not warranted.

**Selection Rule:** Include the two cycle clusters and all current carriers needed for the next assignment; exclude unrelated queue activity and later function labels.

**Ordering Rule:** Use W1–W4 < W5–W8 < W9 < W9+ while permitting bounded reordering within the early cluster for sensitivity testing.

**Formation Rule:** Form a repeated-pattern Path from recurrent cycles, then retain only weak dependence if removal or reordering of early cycles leaves current role distribution, cost structure, and next assignment materially unchanged under the current carriers.

**Target typing:** `repeated-pattern path with weak dependence`

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

**Praxeological Purchase:** `gain` — The history identifies recurrence and initial stabilization, while the present carriers show that strong historical indispensability is not warranted.

**Traceability Ceiling:** `within_ceiling` — Recurrence traces to both cycle clusters; current continuation traces primarily to the current rule, access, and queue state.

**Counterfactual Sensitivity:** `partially_sensitive` — Removing W1–W4 or reordering two early cycles reduces historical narrative but leaves the W9 role distribution, costs, and next assignment unchanged; changing the current rule, access, or queue changes the result.

The three findings are non-compensatory. Formal completeness, source volume, or graph density cannot substitute for Purchase or TraceableLoad.

## 6. Five-Part Loss

### `preserved`

- **recurrence and present carriers:** Both cycle clusters, current rule, role access, queue state, and next assignment remain explicit. **Reason:** They separate historical contribution from current-state sufficiency. **Re-entry:** Changing a current carrier requires a new record.
- **weak dependence boundary:** Early history contributes to stabilization but is not indispensable to current continuation. **Reason:** The case exists to prevent strong-dependence inflation. **Re-entry:** A strong dependence claim requires a separate failed-or-reduced record.

### `compressed`

- **individual cycle detail:** Eight cycles are compressed into early and later clusters. **Reason:** The repeated-pattern claim does not require every micro-event. **Re-entry:** Finer cycle reconstruction requires DECOMPOSE or a new record.

### `excluded`

- **strong dependence and target function:** Strong historical indispensability, Attractor function, prediction, motive, quality, and authority are excluded. **Reason:** They exceed the tested claim and operation. **Re-entry:** Reentry requires separate records.

### `uncertain`

- **micro-negotiation:** Fine negotiation within cycles remains uncertain. **Reason:** The synthetic packet does not represent it. **Re-entry:** Preserve local uncertainty.

### `irrecoverable`

- **unrecorded cycle microstates:** Unrecorded microstates within the compressed cycle clusters cannot be recovered. **Reason:** They were not encoded. **Re-entry:** No reconstruction without new source declarations.

## 7. Alternatives

### Rival compositions

- **`alternative.weakpd.path-only` — not_selected:** Retain the repeated-pattern Path while making no Path-Dependence claim. **Burden:** Preserves recurrence but withholds the supported bounded early order contribution. **Rationale:** The packet supports weak order dependence without strong historical indispensability.

### Rival decompositions

- None declared.

### Rival projections

- None declared.

### No-Transformation

- **`alternative.weakpd.no-composition` — not_selected:** Retain each cycle and current carrier separately. **Burden:** Preserves source declarations but withholds recurrence and Path formation. **Rationale:** The repeated pattern is source-supported.

### Non-Translation

- None declared.

### Unresolved

- None declared.

## 8. Counterfactual Sensitivity

Removing W1–W4 or reordering two early cycles reduces historical narrative but leaves the W9 role distribution, costs, and next assignment unchanged; changing the current rule, access, or queue changes the result.

Any change in source membership, order, frame, granularity, relative level, target class, compression, or target function is a new testable claim. It does not retroactively repair or erase this result.

## 9. Local Admissibility Audit

| Stage | Completion | Finding | Unresolved |
|---|---|---|---|
| Source and Claim Entry | `complete` | Source and claim packet complete: The bounded claim, source field, scope, ceilings, and authority boundary are explicitly declared. | none |
| Operation Classification | `complete` | Operation correctly classified as COMPOSE: Multiple typed source structures are formed into a new temporal composite through explicit selection, ordering, formation, and constitutive relations. | none |
| Praxeological Relevance Floor | `complete` | Praxeological Purchase established: The history identifies recurrence and initial stabilization, while the present carriers show that strong historical indispensability is not warranted. | none |
| Praxeological Traceability Ceiling | `complete` | Source-to-result dependency remains reconstructible: Recurrence traces to both cycle clusters; current continuation traces primarily to the current rule, access, and queue state. | none |
| Continuity and Type Integrity | `complete` | Type, reference, temporal, and functional boundaries preserved: Source objects retain their origin typings; the target is a derived temporal composite; no contextual function is inferred. | none |
| Counterfactual Sensitivity | `complete` | Load-bearing changes alter or defeat the claim: Removing W1–W4 or reordering two early cycles reduces historical narrative but leaves the W9 role distribution, costs, and next assignment unchanged; changing the current rule, access, or queue changes the result. | none |
| Loss and Selection | `complete` | Selection and five-part Loss are explicit: Included and omitted elements, retained distinctions, compression, uncertainty, and irrecoverability are recorded without a lossless presumption. | none |
| Alternatives | `complete` | Material alternatives are preserved: A chronology of eight cycles, a repeated Path without any dependence claim, and later Attractor-function projection remain separate routes. | none |
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

**Operation-specific result:** Recurrence and bounded early order contribution are retained while strong historical indispensability is excluded by current-state sufficiency.

**Local result:** `admissible repeated-pattern Path with weak order dependence`

**Selected canonical Output Class:** `admissible_with_bounded_claim`

**Mapping rationale:** The repeated Path has Purchase and TraceableLoad, but the dependence claim is materially narrower than strong historical indispensability because current carriers explain the tested continuation.

**Claim disposition:** `maintained` — The bounded repeated-pattern and weak-dependence claim is maintained; strong Path Dependence is excluded.

**Path-Dependence finding:** weak only; current scheduling rule, role access, and queue state are sufficient for the tested next assignment.

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

- `C17-HISTORY-01`
- `C17-ATTR-01`

A later frame, finer resolution, new composition, or projected function must be recorded as a separate claim and operation occurrence. This case grants no authority to skip those tests.

---

**YAML record:** [`../yaml/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.yaml`](../yaml/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.yaml)  
**Case index:** [`../Case_Index.md`](../Case_Index.md)  
**Authority:** case artifact below canonical prose; no independent theory authority.
