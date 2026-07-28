# C51-RE1 — Re-entry After New Sources

**Artifact role:** Markdown companion to one Shared Transformation Record operation occurrence  
**Operation:** `PROJECT_AS`  
**Selected Output Class:** `admissible_with_bounded_claim`  
**YAML Record:** [`C51-RE1_PROJECT_AS_Reentry_After_New_Sources.yaml`](../yaml/C51-RE1_PROJECT_AS_Reentry_After_New_Sources.yaml)  
**Package narrative:** [`C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md`](../packages/C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md)  

```text
record companion
≠ duplicate theory source
≠ independent operation occurrence
≠ replacement for the YAML record
```

## 1. Claim

After materially new q3 sources N49, F49 performs the same bounded correction-window threshold function in C49 with a narrower context-specific interval [q3.4,q3.6]; this is a new re-entry test and does not rewrite C49-CAL1.

## 2. Source and Target

**Source object:** `profile.F49` — Same origin profile F49 with materially new q3 calibration packet N49.

**Source type:** `modulating profile`

**Target object:** `target.F49.C49.reentry` — Re-entry view of F49 as the same bounded function with narrower context-specific interval [q3.4,q3.6].

**Contextual target function:** `recalibrated bounded correction-window threshold function`

## 3. Operation Occurrence

**Occurrence ID:** `project-as.c51-re1.01`

**Transformation context:** Gap Package C source-triggered re-entry.

**Justification:** Execute the source-triggered re-entry as a new record after optional Stop.

**Expected praxeological difference:** New q3 sources narrow the bounded threshold interval while preserving context and origin type.

## 4. Local Adjudication

**Local result:** Re-entry with N49 narrows the C49 threshold interval while preserving the prior provisional result and optional Stop.

**Canonical mapping:** `admissible_with_bounded_claim`

**Class-selection rationale:** The result passes only as a new source-triggered record.

## 5. Loss Record

### `preserved`

- Prior result and Stop: C49-CAL1 remains provisional and historically preserved.
- Origin profile and context: F49 and C49 remain unchanged.

### `compressed`

- q3 observations: New sources are summarized into a narrower interval.

### `excluded`

- Universal threshold: Still excluded.

### `uncertain`

- External transfer: No calibration beyond C49.

### `irrecoverable`

- none declared

## 6. Stop and Non-Capture Boundary

**Stop reached:** `false`

**Stop rationale:** The new bounded claim is sufficient; future re-entry again requires new sources.

**Non-Capture asserted:** `false`

**Non-Capture rationale:** The new bounded claim is sufficient; future re-entry again requires new sources.

## 7. Authority Boundary

No empirical, causal, normative, person, or application authority follows.

```yaml
governance:
  authority_inheritance: prohibited
```

## 8. Package Relation

The full shared source narrative, chain handoffs, comparison conditions, and adjacent operation occurrences remain in [`C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md`](../packages/C49-CAL1_Calibration_Open_Result_Optional_Stop_and_Reentry.md). This companion isolates only `C51-RE1` so that every YAML operation Record has one directly corresponding Markdown artifact.
