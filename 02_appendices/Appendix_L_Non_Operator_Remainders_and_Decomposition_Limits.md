# Appendix L — Non-Operator Remainders and Limits of Decomposition

**Status:** substantive bounded provisional completion  
**Authority:** appendix-level remainder, limit, Stop, and Non-Capture guide only  
**Primary owners:** Chapters 18, 22, 25, 27, 41, 49–53; Minified Kernel; Admissibility Rules; Output Classes  
**Case anchors:** `C28-FRAGMENT-01`, `C28-OPTYPE-01`, `C28-UNSUPPORTED-01`, `C28-OVERFINE-01`, `C28-NONOP-01`, `C52-NC1`, `C49-CAL1`, `C51-RE1`

## L.1 Purpose and boundary

This appendix consolidates what may remain after bounded decomposition and why a remainder does not automatically become a new PMS operator, primitive, cause, entity, or hidden layer. It also specifies when decomposition should stop and when a delimited capture claim legitimately ends in `non_capture`.

```text
remainder
≠ new operator
≠ hidden essence
≠ proof of deeper truth
≠ automatic Non-Capture
```

DECOMPOSE opens occurrences and composites, never operator types. Finer resolution has no truth priority.

## L.2 Remainder families

A remainder is claim-relative. The same source material may be captured for one claim and remain outside another.

### L.2.1 Source-supported non-operator remainder

A source-supported feature may materially affect the reconstruction without satisfying the identity, dependency, or grammar conditions of any PMS operator.

Examples include:

- a local timing irregularity;
- an unclassified residual relation;
- a domain-specific constraint;
- an unresolved coordination residue;
- a source-supported feature with no warranted operator mapping.

The correct response is to retain it as a non-operator remainder, not force it into Δ–Ψ.

### L.2.2 Residual relation

Components may be supported while their exact relation remains unresolved. The relation itself is then a remainder.

```text
supported components
+ unsupported relation
→ residual relation
not:
→ free relation invention
```

### L.2.3 Unresolved internal temporality

The source may support phases or partial ordering without supporting a total chronology, unique transition order, duration, or threshold.

### L.2.4 Source-function remainder

A finer model may reconstruct internal parts yet fail to explain how the source object performed its previously warranted function. The missing return is a source-function remainder.

### L.2.5 Granularity remainder

No available granularity may simultaneously satisfy PraxisPurchase, TraceableLoad, Type Integrity, and source-function continuity. The responsible result may be a Stop or Non-Capture, depending on whether an adequate retained claim remains.

### L.2.6 Irrecoverable remainder

Some information may have been excluded, destroyed, never recorded, or rendered non-discriminable. `irrecoverable` must be declared in the Loss record rather than silently represented as uncertainty.

## L.3 Remainder declaration

A disciplined remainder entry should state:

```yaml
remainder:
  claim_relative_to:
  source_reference:
  observed_or_supported_feature:
  unresolved_relation_or_function:
  why_not_operator:
  effect_on_current_claim:
  distortion_if_forced:
  external_method_or_rival:
  reentry_condition:
```

This is an explanatory view, not a new Shared Record field family. The actual record uses existing Source, Loss, Alternatives, Capture Boundary, Result, and Extension carriers.

## L.4 Limits of decomposition

### L.4.1 Type limit

Operator types are not decomposed. A claim such as “split Ω into smaller operators” is a category error unless it refers to a concrete Ω-bearing occurrence or composite.

```text
operator type
≠ compressed occurrence
≠ compressed composite
```

`C28-OPTYPE-01` is the central countercase.

### L.4.2 Reference limit

A valid DECOMPOSE occurrence must preserve the same reference object. If the finer reconstruction creates a different object, the operation has drifted or escaped.

### L.4.3 Source-support limit

Internal structure cannot be invented merely because a finer story is plausible. Unsupported components or relations trigger claim reduction, Stop, or Failure depending on the executed claim.

### L.4.4 Source-function limit

Fragmentation is not decomposition. Components and relations must return to the source function or explicitly revise its disposition.

`C28-FRAGMENT-01` shows supported fragments without a reconstructible function return.

### L.4.5 PraxisPurchase limit

Further detail below the Relevance Floor should not be mistaken for progress. `C28-OVERFINE-01` demonstrates an analysis that increases microdetail without changing the warrantable reconstruction.

### L.4.6 Traceability limit

A finer model above the Traceability Ceiling is not rescued by complexity, mathematical elegance, or visual density.

### L.4.7 Calibration limit

The source may support a bounded form while leaving an exact threshold unresolved. This may justify `admissible_but_provisional` and Optional Stop rather than Failure or Non-Capture. `C49-CAL1` is the key route; `C51-RE1` demonstrates re-entry after materially new sources.

### L.4.8 Anti-immunization limit

A decomposition may not be protected from criticism by changing frame, granularity, or claim after each counterexample.

```text
new granularity
→ new claim
→ new record
not:
→ repaired old claim
```

## L.5 Resolution outcomes

The local resolution test distinguishes:

```text
resolution_gain
resolution_neutral
resolution_drift
resolution_escape
```

### Resolution gain

The finer reconstruction changes a warrantable claim while preserving reference, source function, and traceability.

### Resolution neutral

More detail does not materially change the reconstruction. This can map to `resolution_neutral` where the executed claim is exactly a resolution claim.

### Resolution drift

The analysis gradually substitutes a different question, function, or object.

### Resolution escape

The target no longer reconstructs the same reference object or leaves the declared operation boundary.

Neither drift nor escape should be hidden by claiming that finer detail is inherently superior.

## L.6 Stop at decomposition limits

### Mandatory Stop

A mandatory Stop is reached where continuation under the current claim would violate a decisive boundary, such as:

- operator-type decomposition;
- unsupported microstructure;
- reference escape;
- source-function abandonment;
- authority-sensitive person typing;
- continuation above the Traceability Ceiling;
- repeated non-discriminating detail after sufficiency.

The Stop record preserves:

```text
condition
mode
preserved result
blocked continuation
re-entry conditions
```

### Optional Stop

Optional Stop applies when the current bounded result is sufficient and more analysis is unnecessary rather than forbidden.

```text
sufficiency
+ no material new source
→ optional Stop
```

Optional Stop is not an Output Class.

## L.7 Genuine Non-Capture

`non_capture` is a positive and bounded result. It is not a synonym for ignorance, missing fields, failure, or difficulty.

Required conditions:

1. a delimited capture claim;
2. the correct operation classification;
3. multiple or otherwise adequate bounded attempts;
4. preserved partial capture;
5. a material persistent remainder;
6. no adequate retained form of the same claim;
7. forced integration would distort, invent, or erase load-bearing structure;
8. rivals or external methods remain open;
9. re-entry requires materially changed grounds.

```text
adequate bounded attempts exhausted
+ no adequate retained whole-claim form
+ partial capture preserved
+ forced integration prohibited
→ non_capture
```

### L.7.1 What Non-Capture is not

```text
missing source
≠ non_capture

one failed attempt
≠ non_capture

weak claim under pressure
≠ non_capture shield

unwillingness to reduce claim
≠ non_capture
```

### L.7.2 Non-Capture forms

The controlled local vocabulary may distinguish claim-relative forms such as:

- granularity non-capture;
- composition non-capture;
- projection non-capture;
- cross-domain non-capture;
- source-function non-capture.

These forms explain the limiting condition. They do not create new Output Classes.

## L.8 Canonical case routes

### `C28-FRAGMENT-01`

Supported items are listed without supported relations or source-function return. The problem is fragmentation, not genuine finer reconstruction.

### `C28-OPTYPE-01`

The source is an operator type rather than an occurrence or composite. DECOMPOSE is inapplicable and continuation requires Stop or Failure according to the executed claim.

### `C28-UNSUPPORTED-01`

Plausible internal structure lacks source support. Detail does not compensate for TraceableLoad failure.

### `C28-OVERFINE-01`

Additional microdetail changes no warrantable claim. The result sits below the Praxeological Relevance Floor.

### Non-operator remainder rule

The positive rule is distributed across Chapters 27 and 52 and the Non-Equivalence Index: a source-supported remainder may be retained without promotion to a new operator. No standalone `C28-NONOP-01` Record is asserted.

### `C52-NC1`

Two source-traceable decompositions capture different load-bearing relations. A third integrated candidate is tested but would require unsupported priority or causal integration. Partial capture remains; the whole unique-decomposition claim receives `non_capture`.

### `C49-CAL1` and `C51-RE1`

Calibration uncertainty leaves an adequate provisional claim and therefore does not trigger Non-Capture. New sources permit re-entry in a new record.

## L.9 Remainder decision sequence

```text
1. Is the source an occurrence or composite?
   no → do not DECOMPOSE the operator type

2. Is the same reference object preserved?
   no → drift or escape

3. Are components and relations source-supported?
   no → reduce, Stop, or fail

4. Does the finer form return to the source function?
   no → fragmentation / source-function remainder

5. Does added detail change a warrantable claim?
   no → resolution_neutral or Stop after sufficiency

6. Is the result traceable and bounded?
   no → claim reduction, Stop, or failure

7. Does an adequate retained claim remain?
   yes → retain bounded/provisional/partial result
   no  → test genuine Non-Capture conditions
```

This sequence is not first-match routing. The complete Shared Record and collision adjudication remain required.

## L.10 External-method and rival-superiority clause

A remainder may be better addressed by another method. STRATA must permit:

- domain-specific causal analysis;
- process instrumentation;
- archival reconstruction;
- statistical or simulation methods;
- semantic or legal interpretation;
- deliberate non-translation.

```text
STRATA non-capture
≠ object uncapturable by all methods

external method superior for claim Q
≠ new STRATA primitive
```

## L.11 Reader and graph boundary

The Reader may display captured components, residual relations, uncertain edges, Stop points, rival decompositions, and Non-Capture boundaries. It may not convert graph gaps into hidden entities or missing operators.

```text
unrendered remainder
≠ non-existence

visible residual node
≠ new primitive

more 3D depth
≠ deeper truth
```

## L.12 Completion boundary

Appendix L is complete when it allows a user to preserve non-operator remainders, identify decomposition limits, distinguish Optional and Mandatory Stop, and route genuine Non-Capture without immunizing weak claims or inventing operators from residuals.
