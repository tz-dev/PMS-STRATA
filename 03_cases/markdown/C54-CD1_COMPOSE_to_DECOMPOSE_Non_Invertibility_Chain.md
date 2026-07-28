# C54-CD1 — COMPOSE → DECOMPOSE Non-Invertibility Chain

**Chain:** `COMPOSE → DECOMPOSE`  
**Records:** `C54-CD1A`, `C54-CD1B`  
**Integrated result:** `admissible_with_bounded_claim`  
**Primary owner:** Chapter 54 — Integrated STRATA Model

## 1. Chain question

Can a bounded path first be composed and then reopened at finer resolution while the same reference object, inherited Loss, and non-invertibility remain explicit?

## 2. Source fixture

```text
A54 → B54 → C54
D54 = source-supported side branch
u54 = unresolved transition mechanism
```

## 3. Occurrence A — COMPOSE

`A54 → B54 → C54` forms path composite `P54`. `D54` is explicitly excluded from the bounded path claim and `u54` remains uncertain.

**Route:** `admissible_with_bounded_claim`.

## 4. Occurrence B — DECOMPOSE

`P54` is reopened into:

```text
A54 → B54a → B54b → C54
```

The proposal/revision distinction adds resolution, but `D54` is not retroactively restored and `u54` is not solved.

**Route:** `admissible_with_bounded_claim`.

## 5. Non-invertibility

```text
DECOMPOSE(COMPOSE(X))
≠ X

reopening
≠ inversion

same reference object
≠ identical representation
```

## 6. Chain result

Both local results remain valid and separately Loss-bearing. The integrated chain is boundedly admissible; no lossless-return claim is retained.

```yaml
governance:
  authority_inheritance: prohibited
```
