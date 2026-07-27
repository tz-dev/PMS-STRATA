# PMS-STRATA Countercase Companion Template

**Template status:** reusable human-readable companion template  
**Schema owner:** `../../../07_model/Transformation_Record.schema.json`  
**Pattern guide:** `../../../02_appendices/Appendix_H_Valid_and_Invalid_Transformation_Patterns.md`

> Copy this file for one countercase companion. Replace every bracketed placeholder. The YAML record remains the structured source for the operation occurrence and adjudication.

```text
countercase companion
≠ YAML Transformation Record
≠ second operation occurrence
≠ second adjudication
≠ theory source
```

---

## 1. Countercase Identity

- **Case ID:** `[CASE-ID]`
- **Title:** `[TITLE]`
- **Case class:** `countercase`
- **Operation:** `[COMPOSE | DECOMPOSE | PROJECT_AS]`
- **YAML record:** [`[same-basename.yaml]`](../yaml/[same-basename.yaml])
- **Package narrative:** `[path or not applicable]`
- **Chapter owner:** `[chapter]`

---

## 2. Apparently Plausible Claim

State the claim in its strongest fair form before rejecting or stopping it.

> `[CLAIM]`

### Why it initially appears plausible

- `[surface pattern, source feature, or familiar inference]`
- `[second plausibility source]`
- `[why an analyst might select this operation]`

Do not caricature the claim. A useful countercase tests a credible failure mode.

---

## 3. Source and Scope

### Source reference

`[SOURCE OBJECT]`

### Origin typing

`[ORIGIN TYPE]`

### Coordinates

- **Frame:** `[FRAME]`
- **Granularity:** `[GRANULARITY]`
- **Relative level:** `[RELATIVE LEVEL]`
- **Temporal scope:** `[TEMPORAL SCOPE]`
- **Source scope:** `[SOURCE SCOPE]`
- **Transformation context:** `[CONTEXT]`

### Source ceiling

`[WHAT THE SOURCES CAN AND CANNOT SUPPORT]`

---

## 4. Operation Classification

### Declared operation

`[OPERATION]`

### Why this is the tested operation

`[CLASSIFICATION RATIONALE]`

### Neighboring operation not selected

- `[COMPOSE / DECOMPOSE / PROJECT_AS / no transformation]`
- Reason: `[RATIONALE]`

A countercase must not reject the wrong operation and then generalize the failure to all possible transformations.

---

## 5. Decisive Structural Defect

Name the load-bearing defect precisely.

```text
[DEFECT LABEL]
```

Examples include:

- chronology presented as Path;
- operator-type decomposition;
- fragmentation without source function;
- origin-type replacement;
- label substitution;
- analogy presented as projection;
- source-insensitive target function;
- granularity escape;
- hidden Loss;
- authority inheritance.

### Defect explanation

`[WHY THE CLAIM DOES NOT CARRY]`

### Counterfactual exposure

`[WHICH SOURCE OR CONTEXT CHANGE REVEALS THE DEFECT]`

---

## 6. Admissibility Findings

| Test | Finding | Rationale |
|---|---|---|
| PraxisPurchase | `[finding]` | `[rationale]` |
| TraceableLoad | `[finding]` | `[rationale]` |
| TypeIntegrity | `[finding]` | `[rationale]` |
| Reference Continuity | `[finding]` | `[rationale]` |
| Functional Continuity | `[finding]` | `[rationale]` |
| Temporal Continuity | `[finding]` | `[rationale]` |
| Contextual Boundedness | `[finding]` | `[rationale]` |
| Counterfactual Sensitivity | `[finding]` | `[rationale]` |
| Source Ceiling | `[finding]` | `[rationale]` |
| Calibration | `[finding]` | `[rationale]` |
| Selection and Loss | `[finding]` | `[rationale]` |
| Alternatives | `[finding]` | `[rationale]` |
| Claim Ceiling | `[finding]` | `[rationale]` |
| Authority Ceiling | `[finding]` | `[rationale]` |
| Stop | `[finding]` | `[rationale]` |
| Non-Capture | `[finding]` | `[rationale]` |

One decisive failure may govern the route. Positive findings do not compensate for it.

---

## 7. Loss Record

```yaml
loss:
  preserved:
    - "[preserved feature]"
  compressed:
    - "[compressed feature or bounded none statement]"
  excluded:
    - "[excluded feature or bounded none statement]"
  uncertain:
    - "[uncertainty]"
  irrecoverable:
    - "[irrecoverable loss or bounded none statement]"
```

A failed transformation may still preserve valuable source findings. Do not erase them.

---

## 8. Alternatives and Salvage

### Rival transformation

`[RIVAL COMPOSE / DECOMPOSE / PROJECT_AS / NONE]`

### No-transformation option

`[WHY THE SOURCE MAY NEED TO REMAIN UNTRANSFORMED]`

### Analogy or non-translation option

`[SEPARATE ANALOGY CLAIM OR NOT APPLICABLE]`

### Narrower claim

`[POSSIBLE REDUCED CLAIM]`

State whether the narrower claim has already been tested. If not, the countercase may support `claim_reduction_required` but does not validate the reduced claim.

---

## 9. Stop, Failure, and Non-Capture Boundary

- **Stop reached:** `[true | false]`
- **Stop mode:** `[mandatory | optional | not applicable]`
- **Stop condition:** `[condition]`
- **Operation failure:** `[yes/no and rationale]`
- **Capture limit asserted:** `[yes/no]`
- **Adequate bounded attempts exhausted:** `[yes/no]`

Explain why the selected route is not confused with neighboring forms:

```text
[selected route]
≠ [neighboring class 1]
≠ [neighboring class 2]
```

---

## 10. Selected Result

### Local operation result

`[LOCAL RESULT]`

### Selected Output Class

`[ONE OF THE TEN CANONICAL CLASSES]`

### Claim disposition

`[retain | bound | qualify | separate | reduce | withdraw | mark_capture_limit]`

### Selection rationale

`[WHY THIS CLASS GOVERNS THE CURRENT DELIMITED CLAIM]`

The selected class must come from the YAML record after full candidate and collision assessment.

---

## 11. Failure Preservation and Re-entry

### Preserved earlier result

`[PRIOR FAILURE / STOP / LIMIT / NONE]`

### What a successor claim would need to change

- `[new source]`
- `[new context]`
- `[new granularity]`
- `[new claim scope]`

### Re-entry condition

`[MATERIAL CONDITION]`

A successor record is a new test. It does not rewrite this countercase.

---

## 12. Claim and Authority Boundary

This countercase does not establish:

- `[excluded inference]`
- empirical or causal truth beyond the source basis;
- person typing or diagnosis;
- moral, political, legal, or institutional legitimacy;
- sanction or irreversible labels;
- automatic action recommendations;
- authority inheritance.

```text
failed transformation
≠ failed source object
≠ failed person
≠ universal impossibility
```

---

## 13. Artifact Boundary

The YAML record owns the structured occurrence and routing. This companion explains it for human review. A multi-record package narrative may provide shared context but cannot merge local results.
