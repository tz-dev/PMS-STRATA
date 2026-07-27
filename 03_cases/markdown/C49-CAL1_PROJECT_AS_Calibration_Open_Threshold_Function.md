# C49-CAL1 — Calibration-Open Threshold Function

**Artifact role:** Markdown companion to one Shared Transformation Record operation occurrence  
**Operation:** `PROJECT_AS`  
**Selected Output Class:** `admissible_but_provisional`  
**YAML Record:** [`C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.yaml`](../yaml/C49-CAL1_PROJECT_AS_Calibration_Open_Threshold_Function.yaml)  
**Package narrative:** [`C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md`](../packages/C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md)  

```text
record companion
≠ duplicate theory source
≠ independent operation occurrence
≠ replacement for the YAML record
```

## 1. Claim

F49 performs a bounded correction-window threshold function in C49, but the exact threshold remains materially unresolved inside [q2,q4]; retain the form provisionally and stop further current analysis after sufficiency.

## 2. Source and Target

**Source object:** `profile.F49` — Synthetic correction-window form with source-supported early/late discrimination and unresolved q3 threshold.

**Source type:** `modulating profile`

**Target object:** `target.F49.C49` — Contextual view of F49 as a calibration-open correction-window threshold function.

**Contextual target function:** `calibration-open correction-window threshold function`

## 3. Operation Occurrence

**Occurrence ID:** `project-as.c49-cal1.01`

**Transformation context:** Gap Package C initial calibration-open result.

**Justification:** Test whether F49 supports a target threshold form while preserving unresolved calibration.

**Expected praxeological difference:** The form separates early correction accessibility from late closure, while the exact q3 boundary remains open.

## 4. Local Adjudication

**Local result:** F49 supports a bounded correction-window threshold form with an unresolved calibration interval; optional Stop follows current sufficiency.

**Canonical mapping:** `admissible_but_provisional`

**Class-selection rationale:** Material calibration openness requires provisional routing.

## 5. Loss Record

### `preserved`

- Threshold form: Early/late correction difference remains supported.
- Calibration interval: Exact threshold remains explicitly open.

### `compressed`

- Local variation: Initial record compresses q2/q4 outcomes into an interval.

### `excluded`

- Universal threshold: Excluded.

### `uncertain`

- q3 threshold position: Absent from initial sources.

### `irrecoverable`

- none declared

## 6. Stop and Non-Capture Boundary

**Stop reached:** `true`

**Stop rationale:** The bounded form is sufficient for the current claim; further work without q3 sources would invent precision.

**Non-Capture asserted:** `false`

**Non-Capture rationale:** Optional Stop is reached after sufficient bounded form identification; re-entry requires new sources and a new record.

## 7. Authority Boundary

No empirical, causal, normative, person, or application authority follows.

```yaml
governance:
  authority_inheritance: prohibited
```

## 8. Package Relation

The full shared source narrative, chain handoffs, comparison conditions, and adjacent operation occurrences remain in [`C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md`](../packages/C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md). This companion isolates only `C49-CAL1` so that every YAML operation Record has one directly corresponding Markdown artifact.
