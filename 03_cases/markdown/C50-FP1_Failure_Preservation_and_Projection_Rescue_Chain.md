# C50-FP1 — Failure Preservation and Projection-Rescue Chain

**Gap Package:** B  
**Chapters served:** 38, 41, 50  
**Family served:** `N6`

## 1. Governing sequence

```text
failed PROJECT_AS claim
→ finer DECOMPOSE successor claim
→ broader COMPOSE successor claim
→ new PROJECT_AS successor claim
```

Every arrow opens a new claim and a separate operation occurrence.

## 2. Original failed claim — C50-FP1A

`T50` is labeled a “stabilization trajectory,” but its removal changes no target interpretation or access in `C50`.

**Route:** `failed_transformation`.

## 3. Legitimate successor decomposition — C50-FP1B

The same `T50` reference is reopened as:

```text
request → hold/non-event → repair → release
```

This is a new, narrower same-reference path claim.

**Route:** `admissible_with_bounded_claim`.

## 4. Granularity-escape stop — C50-FP1X

Arbitrary timestamp subdivision adds no praxis difference and only postpones the original objection.

**Route:** `mandatory_stop`.

## 5. Broader composition — C50-FP1C

The finer path and external gate `G50` form new composite `K50`.

```text
K50 ≠ T50 repaired
```

**Route:** `admissible_with_bounded_claim`.

## 6. New independent projection — C50-FP1D

`K50` performs a bounded reopening-threshold function in `H50` under gate-window variation.

**Route:** `admissible_with_bounded_claim`.

## 7. Anti-Immunization result

```text
later success
≠ repaired old claim
≠ erased old failure
≠ inherited authority
```

The original `C50-FP1A` failure remains visible in every successor record.

```yaml
governance:
  authority_inheritance: prohibited
```
