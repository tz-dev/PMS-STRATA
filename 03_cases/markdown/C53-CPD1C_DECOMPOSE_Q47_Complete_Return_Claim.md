# C53-CPD1C — Complete-Return Claim After Compose and Projection

**Artifact role:** Markdown companion to one Shared Transformation Record operation occurrence  
**Operation:** `DECOMPOSE`  
**Selected Output Class:** `claim_reduction_required`  
**YAML Record:** [`C53-CPD1C_DECOMPOSE_Q47_Complete_Return_Claim.yaml`](../yaml/C53-CPD1C_DECOMPOSE_Q47_Complete_Return_Claim.yaml)  
**Package narrative:** [`C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain.md`](../packages/C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain.md)  

```text
record companion
≠ duplicate theory source
≠ independent operation occurrence
≠ replacement for the YAML record
```

## 1. Claim

After Q47 is composed and projected as a bounded H47 access function, DECOMPOSE can recover the complete constituent history and exact contribution topology of Q47 without inherited Loss.

## 2. Source and Target

**Source object:** `composite.Q47` — Origin-typed Q47 composite from C47-CP1A, previously projected in C47-CP1B.

**Source type:** `derived relational composite`

**Target object:** `candidate.reconstruction.Q47.complete` — Attempted complete and lossless finer reconstruction of Q47 after projection.

## 3. Operation Occurrence

**Occurrence ID:** `decompose.c53-cpd1c.01`

**Transformation context:** C53-CPD1 integrated COMPOSE→PROJECT_AS→DECOMPOSE audit chain.

**Justification:** The integrated audit tests whether the projected composite can be losslessly reopened; the operation is correctly identified but the complete-return claim exceeds inherited source and Loss ceilings.

**Expected praxeological difference:** A bounded A2a/A2b split may add resolution, but exact contribution topology and complete microhistory cannot be recovered.

## 4. Local Adjudication

**Local result:** The complete/lossless reopening claim fails; a weaker bounded same-reference decomposition is proposed for separate retest.

**Canonical mapping:** `claim_reduction_required`

**Class-selection rationale:** The operation is correctly identified, but the declared complete/lossless claim materially exceeds inherited source and Loss ceilings.

## 5. Loss Record

### `preserved`

- Q47 reference and prior local results: C47-CP1A/B remain valid within their own scopes.
- Inherited composition and projection Loss: Selection, compressed microhistory, target compression, and uncertainty remain visible.

### `compressed`

- A2 microdetail into A2a/A2b: A bounded split is available but not complete.

### `excluded`

- Lossless complete-return claim: Exact constituent history, contribution weights, and excluded microhistory are not retained.

### `uncertain`

- Contribution weights and missing microhistory: Remain underdetermined/unavailable.

### `irrecoverable`

- Compressed non-load-bearing microhistory: Some detail is unavailable from the composite and target function alone.

## 6. Stop and Non-Capture Boundary

**Stop reached:** `false`

**Stop rationale:** The stronger claim requires reduction; a weaker bounded reopening is proposed but not pre-authorized.

**Non-Capture asserted:** `false`

**Non-Capture rationale:** The stronger claim requires reduction; a weaker bounded reopening is proposed but not pre-authorized.

## 7. Authority Boundary

No chain completion, finer detail, or target function grants stronger authority.

```yaml
governance:
  authority_inheritance: prohibited
```

## 8. Package Relation

The full shared source narrative, chain handoffs, comparison conditions, and adjacent operation occurrences remain in [`C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain.md`](../packages/C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain.md). This companion isolates only `C53-CPD1C` so that every YAML operation Record has one directly corresponding Markdown artifact.
