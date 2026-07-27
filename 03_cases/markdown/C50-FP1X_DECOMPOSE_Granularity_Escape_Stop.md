# C50-FP1X — Granularity Escape Stop

**Artifact role:** Markdown companion to one Shared Transformation Record operation occurrence  
**Operation:** `DECOMPOSE`  
**Selected Output Class:** `mandatory_stop`  
**YAML Record:** [`C50-FP1X_DECOMPOSE_Granularity_Escape_Stop.yaml`](../yaml/C50-FP1X_DECOMPOSE_Granularity_Escape_Stop.yaml)  
**Package narrative:** [`C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md`](../packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md)  

```text
record companion
≠ duplicate theory source
≠ independent operation occurrence
≠ replacement for the YAML record
```

## 1. Claim

After C50-FP1A fails, T50 should be subdivided into ever finer timestamp fragments until some later projection becomes defensible, even though the added fragments change no path, source function, alternative, or target effect.

## 2. Source and Target

**Source object:** `trajectory.T50` — Coarse synthetic trajectory T50 with a rhetorically stabilized label and separately source-supported finer phase packet.

**Source type:** `trajectory`

**Target object:** `trajectory.T50.microtimestamps` — Unsupported timestamp subdivision of T50.

## 3. Operation Occurrence

**Occurrence ID:** `decompose.c50-fp1x.01`

**Transformation context:** Gap Package B granularity-escape failure.

**Justification:** Test the explicit granularity-escape route separately.

**Expected praxeological difference:** None is declared beyond more timestamps; this absence triggers Stop.

## 4. Local Adjudication

**Local result:** Granularity escape is stopped; all prior dispositions remain visible.

**Canonical mapping:** `mandatory_stop`

**Class-selection rationale:** Continuation is unnecessary and objection-displacing.

## 5. Loss Record

### `preserved`

- Prior results: C50-FP1A failure and C50-FP1B bounded path remain.

### `compressed`

- Timestamp fragments: Factual subdivision may be noted.

### `excluded`

- Continuation claim: Further decomposition is excluded.

### `uncertain`

- No additional uncertainty: The problem is lack of purchase, not hidden data.

### `irrecoverable`

- none declared

## 6. Stop and Non-Capture Boundary

**Stop reached:** `true`

**Stop rationale:** Further subdivision adds no PraxisPurchase and only postpones the original objection.

**Non-Capture asserted:** `false`

**Non-Capture rationale:** Mandatory Stop is reached below the Relevance Floor for this continuation.

## 7. Authority Boundary

Stop authorizes no substantive verdict or authority.

```yaml
governance:
  authority_inheritance: prohibited
```

## 8. Package Relation

The full shared source narrative, chain handoffs, comparison conditions, and adjacent operation occurrences remain in [`C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md`](../packages/C50-FP1_Failure_Preservation_and_Projection_Rescue_Chain.md). This companion isolates only `C50-FP1X` so that every YAML operation Record has one directly corresponding Markdown artifact.
