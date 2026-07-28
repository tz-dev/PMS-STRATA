# C54-DP1 — DECOMPOSE → PROJECT_AS Threshold-Function Chain

**Chain:** `DECOMPOSE → PROJECT_AS`  
**Records:** `C54-DP1A`, `C54-DP1B`  
**Integrated result:** `admissible_with_bounded_claim`

## 1. Source fixture

Compressed occurrence `H56` contains entry delay, workaround, correction window, closure, and residual load.

## 2. DECOMPOSE

`H56` is reopened as the same reference object. The correction window becomes visible; its exact duration remains uncertain. No target function is created.

## 3. PROJECT_AS

The origin-typed finer reconstruction performs a bounded correction-window threshold function in `A56`, where removing or closing the window changes the target reconstruction. Comparison context `B56` remains source-insensitive and receives no projection.

```text
finer reconstruction
≠ automatic function

target function
≠ origin type
```

## 4. Integrated result

Both operations pass with bounded claims. Source uncertainty and DECOMPOSE Loss remain attached to the PROJECT_AS handoff.

```yaml
governance:
  authority_inheritance: prohibited
```
