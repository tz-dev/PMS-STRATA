# C17-BRANCH-01 — Branching Path

**Case class:** `positive_case`  
**Chapter owner:** Chapter 17 — PATH Cases, Countercases, and Local Audit  
**Operation:** `COMPOSE`  
**Local result:** `admissible branching Path`  
**Canonical Output Class:** `admissible`  
**Record status:** `supported`  
**YAML record:** [`../yaml/C17-BRANCH-01_Branching_Path.yaml`](../yaml/C17-BRANCH-01_Branching_Path.yaml)  
**Canonical chapter section:** [`../../01_blocks/02_part_i_path.md#17-3-case-2-branching-path`](../../01_blocks/02_part_i_path.md#17-3-case-2-branching-path)

---

## 1. Case Statement

The legacy configuration, contemporaneous branch point, realized staged route, rejected immediate route, and later reachability closure form one bounded branching Path under the declared rules.

This is a synthetic method-and-record test. It is not external empirical evidence, domain calibration, causal proof, normative judgment, or application authority.

```text
case readability
≠ empirical truth
≠ target-function assignment
≠ authority increase
```

## 2. Source and Claim Boundary

**Reference boundary:** Only the synthetic migration decision window and later compatibility closure from t0 through t4.

**Frame:** synthetic platform-migration decision frame

**Granularity:** branch-point and continuation granularity

**Relative level:** branching path relative to constituent branch structures and transitions

**Temporal scope:** Synthetic interval t0–t4.

**Source scope:** Exactly the declared legacy configuration, branch point, staged branch, immediate branch, pilot result, phased rollout, and compatibility freeze.

**Validity scope:** Valid only as the bounded synthetic branching Path described by this record.

### Excluded reach

- No claim that the realized staged branch was optimal, rational, legitimate, or inevitable.
- No claim about the unrealized ultimate outcome of immediate cutover.
- No causal or person-level attribution.
- No contextual target function.

### Claim Ceiling

- **Asserted relation:** A source-supported Branch Point connects one starting configuration to two historically available continuations; one is realized, one rejected, and later reachability changes.
- **Reach:** Legacy platform through staged migration and closure of the original immediate-cutover option.
- **Precision:** Branch availability, selection status, realized transitions, and bounded later reachability; exact closure instant remains uncertain.
- **Dependence strength:** The branching Path depends on the contemporaneous alternative field and later closure; no strong Path-Dependence or counterfactual-outcome claim is made.
- **Rationale:** The sources support a bounded branching Path, not inevitability, optimality, causal superiority, known unrealized outcomes, or target function.

## 3. Typed Reconstruction

### Source objects

| Object | Type | Description | Source pointer |
|---|---|---|---|
| `configuration.branch.legacy` | `configuration` | Legacy platform configuration at t0. | `case://pms-strata/configuration.branch.legacy` |
| `branch.branchpoint.migration` | `branch structure` | Migration Branch Point at t1 with two prepared continuations. | `case://pms-strata/branch.branchpoint.migration` |
| `subpath.branch.staged` | `subpath` | Realized staged-migration subpath from pilot to phased rollout. | `case://pms-strata/subpath.branch.staged` |
| `branch.branch.immediate` | `branch structure` | Immediate-cutover continuation rejected during the open t1 window. | `case://pms-strata/branch.branch.immediate` |
| `transition.branch.compatibility-freeze` | `transition as object` | Compatibility-freeze transition at t4 closing the original immediate route. | `case://pms-strata/transition.branch.compatibility-freeze` |

### Constitutive relations

| Relation | From | To | Description |
|---|---|---|---|
| `relation.branch.legacy-to-branchpoint` | `configuration.branch.legacy` | `branch.branchpoint.migration` | The legacy configuration enters a bounded decision window with two prepared continuations. |
| `relation.branch.realized-staged` | `branch.branchpoint.migration` | `subpath.branch.staged` | The staged route is selected and traversed through pilot and phased rollout. |
| `relation.branch.rejected-immediate` | `branch.branchpoint.migration` | `branch.branch.immediate` | Immediate cutover remains historically available but is explicitly rejected while the window is open. |
| `relation.branch.freeze-closes-route` | `subpath.branch.staged` | `transition.branch.compatibility-freeze` | The later compatibility freeze closes the original immediate-cutover continuation. |

### Temporal content

**Starting configuration:** Legacy platform configuration at t0.

**Transitions:**

- Branch Point
- staged pilot and rollout
- compatibility freeze

**Positive events:**

- branch decision
- pilot
- phased rollout
- compatibility freeze

**Non-Events:**

- None declared.

**Branches and alternatives:** Staged route realized; immediate cutover rejected during the open window and later materially unavailable.

## 4. Operation Decision

**Justification:** The source field contains a contemporaneous plural continuation set, explicit selection status, realized traversal, and a later reachability change; together they support a bounded branching Path rather than a linear retrospective story.

**Expected praxeological difference:** The composite preserves selectivity, rejected availability, and later closure, changing how the realized route and future accessibility are reconstructed.

**Selection Rule:** Include the starting configuration, Branch Point, both contemporaneously available continuations, the realized staged subpath, and the compatibility freeze; exclude later imagined alternatives.

**Ordering Rule:** Use partial order: legacy precedes Branch Point; staged and immediate continuations are contemporaneous candidates; staged traversal precedes compatibility freeze.

**Formation Rule:** Form a branching Path only if plural continuations were contemporaneously available, selection status is supported, realized traversal is traceable, and later reachability change remains explicit.

**Target typing:** `path`

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

**Praxeological Purchase:** `gain` — The composite preserves selectivity, rejected availability, and later closure, changing how the realized route and future accessibility are reconstructed.

**Traceability Ceiling:** `within_ceiling` — The Branch Point and later closure remain reconstructible from the branch candidates, selection status, realized subpath, and compatibility freeze.

**Counterfactual Sensitivity:** `strongly_sensitive` — Removing the immediate branch defeats Branch Point plurality; removing the staged traversal defeats realized-Path formation; removing the freeze defeats later closure.

The three findings are non-compensatory. Formal completeness, source volume, or graph density cannot substitute for Purchase or TraceableLoad.

## 6. Five-Part Loss

### `preserved`

- **Branch Point and branch statuses:** The contemporaneous staged and immediate continuations and realized/rejected statuses remain explicit. **Reason:** Alternative-space structure is constitutive. **Re-entry:** Changing branch status requires a new record.
- **later reachability:** Compatibility closure of the original immediate route remains explicit. **Reason:** Later reachability changes the Path. **Re-entry:** Removing closure defeats the lost-reachability component.

### `compressed`

- **minor implementation decisions:** Local pilot and rollout decisions are compressed into one staged subpath. **Reason:** They are not required individually for the bounded branch claim. **Re-entry:** A finer claim requires DECOMPOSE or new source support.

### `excluded`

- **optimality and unrealized outcomes:** Optimality, inevitability, and the ultimate result of immediate cutover are excluded. **Reason:** They exceed the source and claim ceilings. **Re-entry:** Reentry requires independent sources and separate claims.

### `uncertain`

- **exact closure moment:** The precise instant of material unreachability after the compatibility freeze remains uncertain. **Reason:** The source supports bounded closure but not point-exact timing. **Re-entry:** Preserve bounded temporal uncertainty.

### `irrecoverable`

- **internal rejection deliberation:** Fine internal deliberation behind rejection is not recoverable. **Reason:** The source packet records the decision, not its full deliberative process. **Re-entry:** No reentry without new independent sources.

## 7. Alternatives

### Rival compositions

- **`alternative.branch.linearized` — rejected:** Compose only the realized staged route as a linear Path. **Burden:** Removes the rejected branch and later change in alternative availability. **Rationale:** The branch and reachability structure is source-supported and materially changes the Path claim.

### Rival decompositions

- None declared.

### Rival projections

- None declared.

### No-Transformation

- **`alternative.branch.no-composition` — not_selected:** Retain the branch declarations as separate records with no integrated Path. **Burden:** Preserves local facts but cannot express how selection and later closure belong to one bounded migration episode. **Rationale:** The integrated branching Path remains source-supported.

### Non-Translation

- None declared.

### Unresolved

- None declared.

## 8. Counterfactual Sensitivity

Removing the immediate branch defeats Branch Point plurality; removing the staged traversal defeats realized-Path formation; removing the freeze defeats later closure.

Any change in source membership, order, frame, granularity, relative level, target class, compression, or target function is a new testable claim. It does not retroactively repair or erase this result.

## 9. Local Admissibility Audit

| Stage | Completion | Finding | Unresolved |
|---|---|---|---|
| Source and Claim Entry | `complete` | Source and claim packet complete: The bounded claim, source field, scope, ceilings, and authority boundary are explicitly declared. | none |
| Operation Classification | `complete` | Operation correctly classified as COMPOSE: Multiple typed source structures are formed into a new temporal composite through explicit selection, ordering, formation, and constitutive relations. | none |
| Praxeological Relevance Floor | `complete` | Praxeological Purchase established: The composite preserves selectivity, rejected availability, and later closure, changing how the realized route and future accessibility are reconstructed. | none |
| Praxeological Traceability Ceiling | `complete` | Source-to-result dependency remains reconstructible: The Branch Point and later closure remain reconstructible from the branch candidates, selection status, realized subpath, and compatibility freeze. | none |
| Continuity and Type Integrity | `complete` | Type, reference, temporal, and functional boundaries preserved: Source objects retain their origin typings; the target is a derived temporal composite; no contextual function is inferred. | none |
| Counterfactual Sensitivity | `complete` | Load-bearing changes alter or defeat the claim: Removing the immediate branch defeats Branch Point plurality; removing the staged traversal defeats realized-Path formation; removing the freeze defeats later closure. | none |
| Loss and Selection | `complete` | Selection and five-part Loss are explicit: Included and omitted elements, retained distinctions, compression, uncertainty, and irrecoverability are recorded without a lossless presumption. | none |
| Alternatives | `complete` | Material alternatives are preserved: A linearized staged-only Path and No-Composition remain available but fail to preserve the full alternative-space and reachability structure. | none |
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

**Operation-specific result:** A source-supported Branch Point, realized staged subpath, rejected immediate branch, and later reachability closure form one traceable branching Path.

**Local result:** `admissible branching Path`

**Selected canonical Output Class:** `admissible`

**Mapping rationale:** The record satisfies COMPOSE identity, Purchase, TraceableLoad, type and reference integrity, temporal continuity, contextual boundedness, counterfactual sensitivity, source and claim ceilings, complete Loss, alternatives, Stop, Non-Capture, and authority limits.

**Claim disposition:** `maintained` — The declared path claim is retained exactly within its synthetic scope and ceiling.

**Path-Dependence finding:** not claimed; later closure is reconstructed without strong historical-indispensability inflation.

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

- `C17-TEL-01`
- `C17-ALT-01`

A later frame, finer resolution, new composition, or projected function must be recorded as a separate claim and operation occurrence. This case grants no authority to skip those tests.

---

**YAML record:** [`../yaml/C17-BRANCH-01_Branching_Path.yaml`](../yaml/C17-BRANCH-01_Branching_Path.yaml)  
**Case index:** [`../Case_Index.md`](../Case_Index.md)  
**Authority:** case artifact below canonical prose; no independent theory authority.
