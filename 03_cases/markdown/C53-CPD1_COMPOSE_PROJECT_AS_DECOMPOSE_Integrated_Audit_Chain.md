# C53-CPD1 — COMPOSE → PROJECT_AS → DECOMPOSE Integrated Audit Chain

**Chain:** `COMPOSE → PROJECT_AS → DECOMPOSE`  
**Records:** existing `C47-CP1A`, existing `C47-CP1B`, new `C53-CPD1C`  
**Required failure preserved:** `C47-CP1C`  
**Integrated result:** `partially_admissible` with final `claim_reduction_required`

## 1. Occurrence A — COMPOSE

`C47-CP1A` forms origin-typed composite `Q47`.

**Local route:** `admissible_with_bounded_claim`.

## 2. Occurrence B — PROJECT_AS

`C47-CP1B` projects `Q47` as a bounded H47 access function while preserving origin type.

**Local route:** `admissible_with_bounded_claim`.

## 3. Occurrence C — DECOMPOSE

The declared claim asks whether projection and chain completion permit complete, exact, lossless recovery of Q47's constituent history. They do not.

A bounded A2a/A2b reopening is source-supported, but:

- exact contribution weights remain unknown;
- compressed microhistory remains unavailable;
- prior COMPOSE and PROJECT_AS Loss remain attached;
- the H47 target function is not a decomposable source container.

**Local route:** `claim_reduction_required`.

## 4. Required failure preservation

`C47-CP1C` remains `failed_transformation`: a syntactically complete source-insensitive projection is not repaired by the later chain.

## 5. Integrated result

```text
two bounded local successes
+ one final claim reduction
+ preserved source-insensitive failure
+ separate five-part Loss per occurrence
→ partially_admissible chain view
```

No chain average or narrative completion overwrites local results.

```yaml
governance:
  authority_inheritance: prohibited
```
