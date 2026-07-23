# C17-ATTR-01 — Trajectory or Attractor?

**Case class:** `confusion_case`  
**Chapter owner:** Chapter 17  
**Current operation:** `COMPOSE`  
**Separated later operation:** possible `PROJECT_AS` — not executed  
**Local result:** `admissible single Trajectory with Attractor-function claim withheld`  
**Canonical mapping:** `admissible_with_bounded_claim`  
**Lock-critical:** no  
**Artifact status:** instantiated and locally audited

```text
repeated course within one history
≠ Attractor function automatically
```

## 1. Confusion Claim

A maintenance program passes through recurring escalation, temporary repair, and renewed backlog over one declared history. The source-sensitive sequence forms a Trajectory. Because the course contains repetition, the analyst calls the Trajectory an Attractor.

PATH may reconstruct the historical object. It may not assign an Attractor-function merely from recurrence inside that object.

## 2. Source and Claim Boundary

**Frame:** one synthetic maintenance-program history  
**Temporal scope:** M0–M8  
**Granularity:** configurations, repeated subpaths, repair transitions, residual backlog, endpoint  
**Relative level:** source structures relative to one composed Trajectory  
**Claim Ceiling:** one historical Trajectory only

An Attractor-function would require a declared target context and evidence that the origin-typed Trajectory performs a recurrent stabilizing function there. That is a RETYPE question.

## 3. Typed Reconstruction

| Source object | Type | Time | Constitutive contribution |
|---|---|---|---|
| `configuration.attr.baseline` | configuration | M0 | Initial maintenance arrangement. |
| `subpath.attr.cycle-a` | subpath | M1–M3 | Escalation, temporary repair, renewed backlog. |
| `subpath.attr.cycle-b` | subpath | M4–M6 | A second course-form with altered burden. |
| `transition.attr.partial-repair` | transition | M6–M7 | Repair changes but does not reset the history. |
| `configuration.attr.endpoint` | configuration | M8 | Endpoint with residual backlog and changed continuation costs. |

The two cycles are historically connected rather than treated as independent universal repetitions.

## 4. COMPOSE Decision

**Selection Rule:** retain both cycles, their differences, partial repair, and endpoint residue.

**Ordering Rule:** `M0 < M1–M3 < M4–M6 < M6–M7 < M8`.

**Formation Rule:** form one Trajectory where earlier cycles alter later repair cost, backlog, and continuation options.

The target remains a single historically located object. It is not a new PMS primitive and not an Attractor occurrence by identity.

## 5. Attractor Boundary

Recurrence can support an Attractor hypothesis only through a separate function claim. A valid later record would need to show:

- a declared target context;
- recurrence beyond merely one narrated history where relevant;
- a bounded stabilizing function;
- origin type preserved as `trajectory`;
- source changes that alter the projected function;
- no label substitution.

```text
Trajectory with repetition
≠ trajectory becomes Attractor
```

## 6. Admissibility Findings

| Test | Result | Finding |
|---|---|---|
| Praxis Purchase | `gain` | Historical order changes repair costs and endpoint options. |
| Traceable Load | `within_ceiling` | Both cycles, repair, and residue remain constitutive. |
| Counterfactual Sensitivity | `strongly_sensitive` | Removing the first cycle changes later burden and the target. |
| Type Integrity | pass | The target remains a Trajectory. |
| Functional Continuity | not applicable | No Attractor-function is assigned. |
| Claim Ceiling | bounded | Recurrence is retained without RETYPE inflation. |

## 7. Loss

### preserved

- both cycles, their asymmetry, partial repair, endpoint residue, and historical order;
- separation between Trajectory and possible Attractor-function.

### compressed

- repeated micro-events within each maintenance cycle.

### excluded

- universal recurrence, prediction, Attractor identity, target function, organizational quality, and authority.

### uncertain

- whether the same course-form recurs in other contexts.

### irrecoverable

- unencoded actor-level causal mechanisms and deliberations.

## 8. Alternatives

- bounded Path without Trajectory sedimentation claim;
- repeated-pattern description without any Attractor hypothesis;
- later separate `PROJECT_AS` record for a bounded Attractor-function;
- No-Composition retaining the cycles separately.

## 9. Local Audit and Mapping

All twelve audit stages are complete. The Trajectory claim is retained only after the Attractor-function reach is explicitly withheld.

```text
admissible single Trajectory
with Attractor-function claim withheld

→ admissible_with_bounded_claim
```

## 10. Stop, Non-Capture, and Governance

No mandatory Stop is reached because the function claim is withheld. Reasserting Attractor identity through relabeling would require Stop or failure under a new record.

`non_capture` is not selected because the bounded historical Trajectory remains adequately captured.

```yaml
governance:
  authority_inheritance: prohibited
```

## 11. Artifact Links

**YAML record:** [`../yaml/C17-ATTR-01_Trajectory_or_Attractor.yaml`](../yaml/C17-ATTR-01_Trajectory_or_Attractor.yaml)  
**Case index:** [`../Case_Index.md`](../Case_Index.md)
