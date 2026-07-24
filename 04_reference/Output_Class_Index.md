# PMS-STRATA — Output Class Index

**Status:** Reference Kernel v0.1.15 — Chapter-20-WP3-synchronized output mapping registry  
**Repository role:** `04_reference/*` — output vocabulary and mapping support; not an independent theory source

## 1. Role, Status, and Authority

This file is the provisional Gate 3 registry for canonical PMS-STRATA output classes.

It consolidates the fixed system-wide result vocabulary, distinguishes it from local operation results and record status, and provides controlled mapping and selection guidance during Block production while preserving the completed pre-Block inventory gate.

It is a reference and audit artifact. It does not replace the canonical prose, the Minified Kernel, the later formal model, or case-specific judgment.

Authority order:

```text
PMS.yaml
→ unchanged PMS Base

00_source/PMS-STRATA_Structure.md
→ architecture and chapter blueprint

01_blocks/* after lock
→ canonical corpus prose

05_minified/*
→ binding control artifacts,
  subordinate to locked canonical corpus prose

04_reference/*
→ terminology, indexing, mapping, and audit navigation
```

Before Block lock, the Minified Kernel remains the operative control source for the class inventory and compact meanings.

This index may:

- register the exact ten canonical values;
- distinguish classes from local results, record status, and method concepts;
- provide operation-specific mapping guidance;
- state collision and selection rules;
- identify primary definition and application sites;
- hand controlled requirements to the later formal model.

This index may not:

- introduce an eleventh class;
- rank the classes as a maturity or truth scale;
- decide empirical truth, causality, semantic validity, or application authority;
- erase local results through a global class;
- replace operation-specific audits;
- treat formal validation as substantive judgment;
- create person, group, clinical, moral, political, or legal classifications.

```text
more structure
≠
more authority
```

---

### Chapter 1 local-result boundary

Chapter 1 uses canonical Output Classes only for bounded local example and chapter-audit dispositions. Its provisional lock maps to `admissible_but_provisional`; that mapping is not an eleventh class, a chapter rank, or proof that later cases will pass. `mandatory_stop`, `claim_reduction_required`, `failed_transformation`, and `non_capture` remain available for object-category and identity failures.

---

## 2. Canonical Inventory and Spelling

Exactly these ten values are canonical:

```text
admissible
admissible_with_bounded_claim
admissible_but_provisional
resolution_neutral
analogy_only
partially_admissible
claim_reduction_required
mandatory_stop
failed_transformation
non_capture
```

### 2.1 Spelling rule

Canonical values use lowercase `snake_case`.

Readable prose forms such as “admissible with bounded claim”, “mandatory stop”, and “non-capture” are not additional values.

```text
prose rendering
≠
new canonical class
```

### 2.2 Closed inventory

Local labels, case outcomes, record-status values, claim effects, and audit notes do not expand this inventory.

```text
local result label
≠
new system-wide class
```

### 2.3 Compact inventory matrix

| Canonical class | Core governance question | Primary distinction |
|---|---|---|
| `admissible` | Does the declared operation and claim pass as stated? | admissible ≠ true |
| `admissible_with_bounded_claim` | Is a material narrowing of reach or scope itself the decisive governance result? | ordinary boundedness ≠ bounded-claim output |
| `admissible_but_provisional` | Is it usable while material support or calibration limits remain? | provisional ≠ partial |
| `resolution_neutral` | Did valid refinement produce no changed reconstruction? | neutral ≠ failed |
| `analogy_only` | Is resemblance retained without valid projection? | analogy ≠ substitution |
| `partially_admissible` | Which separable parts pass and which do not? | partial ≠ whole validation |
| `claim_reduction_required` | Must the current claim be weakened and retested? | reduction required ≠ already bounded |
| `mandatory_stop` | Would further continuation be inadmissible? | mandatory ≠ optional stop |
| `failed_transformation` | Did the declared operation fail its own test? | failure ≠ non-capture |
| `non_capture` | Does adequate capture remain unavailable under present conditions? | non-capture ≠ immunity |

### 2.4 Ordinary boundedness versus bounded-claim output

Every admissible STRATA claim is already context-, source-, frame-, and scope-bounded. That ordinary requirement does not automatically produce `admissible_with_bounded_claim`.

```text
ordinary contextual boundedness
≠
bounded-claim output
```

Use `admissible_with_bounded_claim` only when a material narrowing relative to the initially tested or normally expected claim is itself the decisive governance result.

---

## 3. Output Architecture

PMS-STRATA distinguishes four result layers:

```text
methodological concept
≠
operation-specific result
≠
record-level status declaration
≠
canonical output class
```

### 3.1 Methodological concept

A method concept names a general rule or result logic.

Examples:

```text
claim reduction
mandatory stop
Non-Capture
resolution neutrality
```

The corresponding canonical values are not identical to those concepts:

```text
claim reduction ≠ claim_reduction_required
mandatory stop ≠ mandatory_stop
Non-Capture ≠ non_capture
```

### 3.2 Operation-specific result

An operation-specific result describes what occurred within one COMPOSE, DECOMPOSE, or PROJECT_AS occurrence.

Examples:

```text
admissible trajectory
source function refined
useful structural analogy
failed composition
competing projections
```

It remains visible alongside the canonical class.

### 3.3 Record-level status declaration

Record status is the record-level declaration architecture that preserves separate axes rather than one mixed enum.

| Record-level axis | Representative controlled content | Separation rule |
| --- | --- | --- |
| support status | supported; provisional; contested; underdetermined; unsupported | does not mechanically determine a class |
| resolution-test result | resolution gain; resolution-neutral result; resolution drift; resolution escape | remains distinct from support status |
| claim disposition | maintained; withdrawn; failed; superseded without erasure | records what happened to a claim, not how well it is supported |
| capture statement | captured or uncaptured structure, limiting condition, and re-entry possibility | not a generic record status `non-capture` and not automatic `non_capture` |

```text
support status: provisional
≠
automatic admissible_but_provisional
```

### 3.4 Canonical output class

The canonical class normalizes the system-wide governance result for a specified operation occurrence or integrated claim.

It does not erase:

- the local result;
- the source-function effect;
- the prior claim result;
- the stop trigger;
- the loss record;
- or the uncaptured remainder.

### 3.5 Required result separation

For DECOMPOSE in particular:

```text
operation result
≠
source-function effect
≠
prior source-claim result
```

A valid DECOMPOSE may reject the prior source-function claim without becoming `failed_transformation`.

---

## 4. Single-Class and Multi-Record Rules

### 4.1 Single-class rule

For each clearly delimited operation occurrence or separately tested claim:

```text
one operation-specific result
+
one canonical output class
```

Where a local result can map to more than one class, the actual record must select one and state the reason.

### 4.2 No class stacking as substitute for reasoning

Avoid unstructured outputs such as:

```text
admissible + provisional + partial + stop
```

Instead separate the claim, operation, stage, or subclaim that receives each result.

### 4.3 Operation chains

Each operation occurrence in a chain retains its own class.

Example:

```text
COMPOSE
→ admissible

PROJECT_AS
→ claim_reduction_required

DECOMPOSE
→ admissible_but_provisional
```

### 4.4 Integrated result

An Integrated STRATA Audit may assign a final class to the whole audited claim or chain.

```text
integrated result
≠
replacement of component results
```

The final class must preserve earlier failure, stop, partiality, and non-capture records.

### 4.5 New transformation rule

```text
new transformation
=
new testable claim
```

A later admissible operation does not retroactively change an earlier class.

---

## 5. Non-Ordinal Navigation Families

The ten classes are not a score, maturity ladder, confidence scale, or ranking of persons, theories, or cases.

```text
admissible
>
provisional
>
partial
>
failed
```

is not a valid STRATA ordering.

For navigation only, the classes can be grouped by their primary governance function:

| Navigation family | Classes | Function |
|---|---|---|
| Retained admissibility result | `admissible`, `admissible_with_bounded_claim`, `admissible_but_provisional` | retain a tested transformation claim under stated conditions |
| Qualified retained result | `resolution_neutral`, `analogy_only`, `partially_admissible` | preserve a valid neutral, analogical, or explicitly partial result |
| Required governance action | `claim_reduction_required`, `mandatory_stop` | require revision or termination before further claim use |
| Failure or capture-boundary result | `failed_transformation`, `non_capture` | record failed operation or an explicit boundary of adequate capture |

These groups are non-authoritative navigation aids.

```text
navigation family
≠
new output class
```

---
## 6. `admissible`

### 6.1 Canonical meaning

The declared operation satisfies all applicable common and operation-specific requirements for the claim and scope already stated, without a further output-relevant restriction beyond ordinary STRATA boundedness.

### 6.2 Use when

- the operation identity is correct;
- PraxisPurchase and TraceableLoad are sufficient for the declared claim;
- Type Integrity, Reference Continuity, Functional Continuity, Contextual Boundedness, Counterfactual Sensitivity, Source Ceiling, Claim Ceiling, Stop, Non-Capture, and loss duties have been addressed as applicable;
- no material output-relevant scope reduction or provisional support condition remains the primary governance result;
- no further claim reduction is required as the present governance result.

### 6.3 Do not use as

- empirical truth;
- causal proof;
- semantic or normative validity;
- application authorization;
- authority inheritance;
- a claim of completeness.

### 6.4 Claim effect

The tested claim may be retained in its declared form and scope. Any later extension is a new testable claim.

### 6.5 Representative local results

- `admissible sequence`;
- `admissible path`;
- `admissible trajectory`;
- `admissible declared composite`;
- `admissible decomposition`;
- `admissible functional projection`;

### 6.6 Central non-equivalences

```text
`admissible` ≠ true
```

```text
`admissible` ≠ unlimited
```

```text
`admissible` ≠ immune from revision
```

```text
`admissible` ≠ `admissible_with_bounded_claim`
```

### 6.7 Re-entry and continuation

A new source, frame, scope, granularity, level, operation, or target function requires a new record rather than automatic inheritance.

### 6.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Integrated taxonomy site:** Chapter 53.
- **Operation-specific application sites:** Chapters 17, 28, and 40.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 7. `admissible_with_bounded_claim`

### 7.1 Canonical meaning

The transformation is warranted, but a material narrowing of context, time, level, object, function, population of cases, or generality is itself the decisive governance result.

### 7.2 Use when

- the transformation passes only after a material narrowing relative to the initially tested or normally expected claim is made explicit;
- the relevant limitation concerns reach or scope rather than unresolved support alone;
- ordinary Contextual Boundedness required of every STRATA claim would not by itself justify this class;
- the bounded claim itself has already been tested;
- the record states what is outside the valid claim.

### 7.3 Do not use as

- a merely provisional record;
- a still-unrevised overclaim;
- partial admissibility across incompatible subclaims;
- automatic weakness or low value.

### 7.4 Claim effect

Retain the tested narrower claim. Do not present the broader formulation as if it had passed.

### 7.5 Representative local results

- `admissible path-dependence claim under a materially narrowed historical scope`;
- `admissible decomposition with a separately recorded narrowed source claim`;
- `heterogeneous source object with a materially narrowed whole-object claim`;
- `admissible narrow projection`;
- `context-dependent projection whose valid reach is materially narrower than the tested claim`;
- `compatible multiple projections with materially separated contexts`;

### 7.6 Central non-equivalences

```text
`admissible_with_bounded_claim` ≠ `admissible_but_provisional`
```

```text
bounded claim ≠ untested reduced claim
```

```text
contextual boundedness ≠ global transfer
```

```text
ordinary contextual boundedness ≠ bounded-claim output
```

### 7.7 Re-entry and continuation

Expansion beyond the stated boundary requires a new test. The bounded class does not authorize scope inheritance.

### 7.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Method elaboration:** Chapter 39.
- **Integrated taxonomy site:** Chapter 53.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 8. `admissible_but_provisional`

### 8.1 Canonical meaning

The operation is coherent and sufficiently supported for controlled use, while material source, counterfactual, calibration, temporal, or rival-reconstruction limits remain unresolved.

### 8.2 Use when

- the claim is usable under current support;
- the unresolved issue concerns evidential or calibration stability rather than scope alone;
- the record names the material uncertainty and its claim effect;
- the claim remains revisable without being treated as failed.

### 8.3 Do not use as

- a synonym for narrow scope;
- a generic label for incomplete writing;
- a record status automatically converted into a class;
- partial admissibility across separate subclaims.

### 8.4 Claim effect

Retain the current claim with an explicit provisional qualifier and a stated re-entry or revision condition.

### 8.5 Representative local results

- `provisional composition`;
- `provisional path`;
- `admissible decomposition with unresolved source-function support`;
- `provisional projection`;
- `currently preferred reconstruction with a material unresolved rival`;
- `calibration-sensitive structural form`;

### 8.6 Central non-equivalences

```text
`admissible_but_provisional` ≠ `admissible_with_bounded_claim`
```

```text
provisional support ≠ failed transformation
```

```text
support status `provisional` ≠ automatic class assignment
```

```text
`admissible_but_provisional` ≠ `non_capture`
```

### 8.7 Re-entry and continuation

New sources, calibration criteria, rival comparison, or counterfactual tests may strengthen, narrow, split, or defeat the claim.

### 8.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Method elaboration:** Chapter 49.
- **Integrated taxonomy site:** Chapter 53.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 9. `resolution_neutral`

### 9.1 Canonical meaning

A finer-resolution or explicit granularity test is permissible, but the added distinctions do not change the warranted praxis reconstruction or claim.

### 9.2 Use when

- a genuine resolution comparison has occurred;
- the finer distinctions are source-supported;
- the tested reconstruction remains materially unchanged;
- the result records the absence of resolution gain rather than pretending additional discovery.

### 9.3 Do not use as

- generic lack of findings;
- unsupported decomposition;
- failed transformation;
- non-capture;
- proof that no finer distinction could ever matter.

### 9.4 Claim effect

Retain the prior warranted reconstruction; record that this particular refinement produced no additional praxis finding.

### 9.5 Representative local results

- `resolution-neutral result`;
- `valid finer reconstruction with no changed source-function claim`;
- `negative Changed-Reconstruction Test`;

### 9.6 Central non-equivalences

```text
`resolution_neutral` ≠ resolution gain
```

```text
`resolution_neutral` ≠ `failed_transformation`
```

```text
`resolution_neutral` ≠ `non_capture`
```

### 9.7 Re-entry and continuation

A different distinction, source basis, frame, or claim may justify a new resolution test. Repetition without changed grounds is unnecessary.

### 9.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Method elaboration:** Chapters 25, 27, and 44.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 10. `analogy_only`

### 10.1 Canonical meaning

A useful and declared structural resemblance is retained, while semantic preservation or a source-traceable contextual target function is not established.

### 10.2 Use when

- the resemblance has explanatory or comparative value;
- the relation is explicitly marked as analogy;
- PROJECT_AS duties are not claimed as satisfied;
- the limits and breaking points of the analogy remain visible.

### 10.3 Do not use as

- label substitution;
- operator identity;
- valid functional projection;
- semantic equivalence;
- a failed result in every respect.

### 10.4 Claim effect

Retain only the analogy claim. Withdraw or reduce any stronger projection, identity, or semantic-preservation claim.

### 10.5 Representative local results

- `useful structural analogy`;
- `projection reduced to analogy`;
- `cross-domain mapping with unestablished semantic preservation`;

### 10.6 Central non-equivalences

```text
`analogy_only` ≠ label substitution
```

```text
`analogy_only` ≠ valid projection
```

```text
`analogy_only` ≠ `failed_transformation` in every respect
```

### 10.7 Re-entry and continuation

Where a stronger PROJECT_AS claim is later proposed, it requires a declared target context, target function, Constitutive Source Trace, Counterfactual Sensitivity, validity scope, and loss disclosure. An `analogy_only` result need not originate in a failed PROJECT_AS attempt.

### 10.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Method elaboration:** Chapters 37 and 39.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 11. `partially_admissible`

### 11.1 Canonical meaning

Clearly identified stages, parts, relations, or subclaims satisfy the applicable tests while other parts require reduction, separation, rejection, or unresolved status.

### 11.2 Use when

- the admissible and inadmissible portions can be named;
- the retained parts remain independently traceable;
- the class does not average incompatible results;
- the record preserves local failures or non-capture rather than hiding them.

### 11.3 Do not use as

- general uncertainty;
- a merely provisional whole claim;
- a narrow but fully admissible claim;
- a substitute for separate operation results in a chain.

### 11.4 Claim effect

Retain only the specified admissible components or subclaims. Record the remainder separately.

### 11.5 Representative local results

- `competing compositions with a shared admissible core`;
- `admissible decomposition with a separately recorded partially preserved source-function claim`;
- `heterogeneous source object where only specified parts remain warranted`;
- `competing internal models with common structure`;
- `competing projections with separable partial functions`;
- `integrated claim with explicitly separable admissible and non-admissible components`;

### 11.6 Central non-equivalences

```text
`partially_admissible` ≠ `admissible_with_bounded_claim`
```

```text
`partially_admissible` ≠ `admissible_but_provisional`
```

```text
partial admissibility ≠ whole-operation validation
```

```text
`partially_admissible` ≠ `non_capture`
```

### 11.7 Re-entry and continuation

Separated failed, provisional, or uncaptured parts may be retested through their own records; the retained partial result does not validate them.

### 11.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Method elaboration:** Chapter 52.
- **Integrated taxonomy site:** Chapter 53.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 12. `claim_reduction_required`

### 12.1 Canonical meaning

The currently tested claim is too strong, but a weaker object class, function, level, scope, confidence, or relation remains supportable enough to justify revision and retesting.

### 12.2 Use when

- the stronger claim does not pass;
- a specific weaker formulation remains available;
- the weaker claim has not yet been treated as automatically validated;
- the reduction preserves the original failure or overreach.

### 12.3 Do not use as

- an already tested bounded claim;
- silent rewriting of the original claim;
- automatic admissibility of the proposed weaker claim;
- mandatory stop in every case.

### 12.4 Claim effect

Revise the claim explicitly, preserve the prior result, and run a new test before assigning a new class.

### 12.5 Representative local results

- `trajectory → path`;
- `path → sequence`;
- `strong path dependence → weak order dependence`;
- `projection → analogy`;
- `broad function → narrow function`;
- `supported resolution test, but no changed reconstruction: resolution-gain claim → resolution-neutral result`;
- `mandatory claim reduction`;

### 12.6 Central non-equivalences

```text
`claim_reduction_required` ≠ `admissible_with_bounded_claim`
```

```text
claim reduction ≠ concealment of failure
```

```text
revised claim ≠ unchanged original claim
```

### 12.7 Re-entry and continuation

The reduced claim re-enters as a new testable claim with its own source, scope, loss, and result.

### 12.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Method elaboration:** Chapter 51.
- **Operation-specific application sites:** Chapters 17, 28, and 40.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 13. `mandatory_stop`

### 13.1 Canonical meaning

Continuation of the present operation under the present conditions would violate the Relevance Floor, Traceability Ceiling, Source Ceiling, Type Integrity, contextual boundedness, calibration, or anti-immunization constraints.

### 13.2 Use when

- the current continuation—not merely the analyst’s preference—would be inadmissible;
- the trigger and preserved result are stated;
- optional stopping is insufficient to describe the boundary;
- re-entry conditions, if any, are explicit.

### 13.3 Do not use as

- optional stop;
- methodological defeat;
- failed transformation in every case;
- non-capture in every case;
- permanent prohibition under all future conditions.

### 13.4 Claim effect

End the current operation. Preserve any valid prior result and record what cannot be continued.

### 13.5 Representative local results

- `operation-specific mandatory stop`;
- `resolution drift that must not continue`;
- `source ceiling reached`;
- `continued projection would violate type integrity`;
- `continued composition would lose traceable load`;

### 13.6 Central non-equivalences

```text
`mandatory_stop` ≠ optional stop
```

```text
`mandatory_stop` ≠ `failed_transformation` in every case
```

```text
stop ≠ erasure of prior result
```

### 13.7 Re-entry and continuation

Re-entry requires a new record and changed grounds such as new sources, a different claim, or a newly justified calibration. Unrecorded continuation is prohibited.

### 13.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Stop-method elaboration:** Chapter 51.
- **Operation-specific application sites:** Chapters 16, 27, and 39.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 14. `failed_transformation`

### 14.1 Canonical meaning

The declared operation does not satisfy its defining identity or one or more necessary admissibility conditions and therefore does not establish the claimed transformation result.

### 14.2 Use when

- chronology is presented as COMPOSE without formation;
- a parts list is presented as DECOMPOSE without relational reconstruction;
- label substitution or an invalid type jump is presented as PROJECT_AS;
- source support or constitutive trace is insufficient for the declared operation;
- the result fails rather than merely requiring continued caution.

### 14.3 Do not use as

- invalidity of the source object itself;
- non-capture;
- a successful DECOMPOSE that rejects a prior source-function claim;
- proof that every alternative operation will fail.

### 14.4 Claim effect

Reject the declared transformation result. Preserve valid source objects, prior claims, analogies, or reduced alternatives separately where warranted.

### 14.5 Representative local results

- `failed composition`;
- `unsupported decomposition`;
- `resolution drift where the attempted decomposition itself fails`;
- `label substitution`;
- `invalid type jump`;
- `unmarked level mixing`;

### 14.6 Central non-equivalences

```text
`failed_transformation` ≠ `non_capture`
```

```text
failed operation ≠ invalid source object
```

```text
rejected prior source-function claim ≠ failed DECOMPOSE transformation
```

### 14.7 Re-entry and continuation

A materially revised operation is a new claim and must not be recorded as retroactive success of the failed operation.

### 14.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Operation-specific application sites:** Chapters 15, 20, and 30.
- **Integrated taxonomy site:** Chapter 53.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 15. `non_capture`

### 15.1 Canonical meaning

The present STRATA grammar, source basis, granularity, composition, calibration, or projection cannot adequately capture the declared object, relation, or function without distortion, unsupported extension, or false closure.

### 15.2 Use when

- the captured and uncaptured portions are identified;
- the limiting condition is stated;
- attempted operations and alternatives are documented;
- the result remains open to a rival or future reconstruction without presuming one.

### 15.3 Do not use as

- missing information alone;
- failed transformation;
- immunity from criticism;
- proof of rival superiority;
- a protective label for a weak claim.

### 15.4 Claim effect

State what remains uncaptured and reduce any totalizing claim. Preserve partial capture where justified.

### 15.5 Representative local results

- `competing path constructions with no warranted selection`;
- `source function underdetermined with no adequate retained result`;
- `competing internal models that cannot be integrated`;
- `operation-specific non-capture`;
- `projection non-capture`;
- `integrated non-capture`;

### 15.6 Central non-equivalences

```text
`non_capture` ≠ `failed_transformation`
```

```text
`non_capture` ≠ missing information alone
```

```text
`non_capture` ≠ immunity from criticism
```

```text
Non-Capture ≠ proof of rival superiority
```

### 15.7 Re-entry and continuation

Re-entry requires a changed limiting condition, new source basis, new calibration, different operation, or rival framework. The original non-capture remains recorded.

### 15.8 Primary handoffs

- **Designated primary class-definition site:** Chapter 6.
- **Non-Capture-method elaboration:** Chapter 52.
- **Operation-specific application sites:** Chapters 16, 27, and 39.
- **Integrated taxonomy site:** Chapter 53.
- **Current control sources:** `05_minified/PMS_STRATA_Minified_Canonical.md` and `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`.
- **Operation mapping:** `04_reference/Transformation_Operation_Index.md`.
- **Boundary references:** `04_reference/Non_Equivalence_Index.md`.

---

## 16. Class Collision and Selection Rules

Collision rules do not create a mechanical ranking. They identify the primary governance question that the class must answer.

### 16.1 `admissible` versus `admissible_with_bounded_claim`

```text
ordinary contextual boundedness
≠
bounded-claim output
```

- Use `admissible` when the claim already contains its regularly required context, source, frame, and scope limits and passes without a further material narrowing as the output result.
- Use `admissible_with_bounded_claim` when a material restriction relative to the initially tested or normally expected claim is itself the decisive governance result.

### 16.2 Bounded versus provisional

Ask separately:

1. What is the actually tested claim and its declared validity scope?
2. Is a material scope restriction itself the principal result?
3. Within that delimited scope, do source, counterfactual, calibration, temporal, or rival limits remain materially provisional?

| Situation | Class |
|---|---|
| A materially narrower claim has been revised, tested, and passes; reach or scope is the primary governance issue. | `admissible_with_bounded_claim` |
| One coherent delimited claim is usable, but material support, calibration, temporal, or rival uncertainty remains. | `admissible_but_provisional` |
| Both conditions are present. | State the scope boundary and provisional condition separately. No default precedence applies; select the class that records the primary governance result for that delimited claim and justify it. Split claims or record segments where one class would conceal a material second result. |

No class is assigned merely because the prose contains the words “bounded” or “provisional”.

### 16.3 Bounded versus partial

```text
one whole claim passes under materially narrower reach
→ admissible_with_bounded_claim
```

```text
specified separable parts have different admissibility results
→ partially_admissible
```

### 16.4 Partial versus provisional

```text
different subclaims or stages
have different outcomes
→ partially_admissible
```

```text
one coherent claim remains usable
but support or rival comparison is unsettled
→ admissible_but_provisional
```

### 16.5 Provisional versus non-capture

```text
one coherent claim remains usable
under a material provisional qualifier
→ admissible_but_provisional
```

```text
no adequate claim remains available
without distortion, unsupported extension, or false closure
→ non_capture
```

### 16.6 Partial versus non-capture

```text
specified separable parts remain warranted
→ partially_admissible
```

```text
no adequate retained claim remains,
even after separating the parts
→ non_capture
```

### 16.7 Reduction required versus bounded admissibility

```text
current claim must still be weakened
→ claim_reduction_required
```

```text
narrow claim has already been revised,
tested, and passed
→ admissible_with_bounded_claim
```

`claim_reduction_required` is a process result. It does not pre-authorize the reduced claim.

### 16.8 Mandatory stop versus failed transformation

| Question | Result |
|---|---|
| Has the attempted operation already failed its identity or necessary conditions? | `failed_transformation` |
| Would further continuation cross a mandatory boundary while a prior result may remain valid, partial, provisional, or unresolved? | `mandatory_stop` |

Both can occur in one case only if they refer to separately delimited stages or claims.

### 16.9 Failed transformation versus non-capture

```text
declared operation fails its test
→ failed_transformation
```

```text
no adequate reconstruction remains available
without distortion or false closure
→ non_capture
```

A failed operation does not establish that the object is uncapturable. Non-capture does not retroactively make every attempted operation invalid.

### 16.10 Stop versus non-capture

A method record may contain both a stop trigger and a non-capture statement.

- Use `mandatory_stop` when the primary result is that the present continuation is inadmissible.
- Use `non_capture` when the primary claim is that adequate capture remains unavailable after the bounded tests.

The non-selected method result remains in its own record field.

### 16.11 Resolution neutral versus claim reduction

Use `resolution_neutral` only after a supported resolution test establishes that the additional distinction produces no changed reconstruction.

Use `claim_reduction_required` when a previously stronger claim must be reformulated and retested. Unsupported refinement instead points to `failed_transformation` or `mandatory_stop`, depending on whether the attempted operation has failed or continuation must cease.

### 16.12 Analogy only versus failed projection

A PROJECT_AS claim may fail while a bounded analogy survives.

Record separately:

```text
PROJECT_AS result
→ failed_transformation

retained relation
→ analogy_only
```

This is not class stacking for one claim; it is result separation between the failed projection and the surviving analogy claim.

## 17. COMPOSE / PATH Result Mapping

### 17.1 Mapping table

| Local COMPOSE or PATH result | Canonical class | Selection condition |
|---|---|---|
| admissible sequence | `admissible` | temporal ordering is established for the declared sequence claim |
| admissible path | `admissible` | connected realized transitions and selection are traceable |
| admissible trajectory | `admissible` | sedimentation and historical load are established |
| admissible declared composite | `admissible` | constitutive source relations and the declared object class are warranted |
| admissible path-dependence claim | `admissible` or `admissible_with_bounded_claim` | select according to the warranted strength and historical scope; state the rationale |
| provisional path | `admissible_but_provisional` | the path is usable but source, periodization, or branch uncertainty remains material |
| provisional composition | `admissible_but_provisional` | composition passes under material source, ordering, or calibration limits |
| competing path constructions | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one candidate is provisionally preferred while a material rival remains; a shared partial structure remains; or no warranted selection is available |
| competing compositions | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one composition is provisionally preferred while a material rival remains; shared composite claims remain; or no formation rule is supportable |
| reduced composition claim | `claim_reduction_required` | a weaker object class or historical claim must be reformulated and retested |
| failed composition | `failed_transformation` | COMPOSE identity or admissibility fails |
| operation-specific mandatory stop | `mandatory_stop` | further composition would become inadmissible |
| operation-specific non-capture | `non_capture` | no adequate composition preserves the relevant source load |

### 17.2 COMPOSE cautions

```text
chronology
≠
COMPOSE
```

```text
aggregation
≠
formation of a composite
```

```text
admissible trajectory
≠
admissible path-dependence claim
```

COMPOSE forms an analytical object. It does not automatically assign a contextual target function.

---

## 18. DECOMPOSE / SUB Result Mapping

### 18.1 Two-axis result requirement

Every DECOMPOSE record must distinguish:

```text
DECOMPOSE operation result and canonical class
≠
source-function effect
≠
prior source-claim result
```

The source-function effect is not itself a canonical class and does not determine the operation class by itself.

### 18.2 DECOMPOSE operation-result mapping

| Local DECOMPOSE or SUB operation result | Canonical class | Selection condition |
|---|---|---|
| admissible decomposition | `admissible`, `admissible_with_bounded_claim`, or `admissible_but_provisional` | select according to whether the operation passes as declared, requires a material claim boundary, or remains usable under material provisional support limits; record source-function effect separately |
| heterogeneous source object | `admissible_with_bounded_claim`, `admissible_but_provisional`, or `partially_admissible` | heterogeneity materially narrows one whole claim, leaves a usable but provisional whole-object claim, or supports only separable parts |
| competing internal models | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one model is provisionally preferred while a material rival remains; a common partial reconstruction remains; or no warranted retained result is available |
| resolution-neutral result | `resolution_neutral` | a supported finer-resolution test does not change the warranted reconstruction |
| competing decompositions | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one decomposition is provisionally preferred while a material rival remains; shared partial structure exists; or no warranted decomposition can be selected |
| unsupported decomposition | `failed_transformation` | source support is insufficient for the claimed finer reconstruction |
| resolution drift | `mandatory_stop` or `failed_transformation` | select according to whether continuation must cease or the attempted operation already fails |
| operation-specific mandatory stop | `mandatory_stop` | further decomposition is inadmissible |
| operation-specific non-capture | `non_capture` | no adequate finer reconstruction remains available |

### 18.3 Source-function effect table

| Source-function effect | What it says | What it does not determine by itself |
|---|---|---|
| confirmed | the finer reconstruction supports the prior source-function claim | the canonical class of the DECOMPOSE occurrence |
| refined | the source-function claim requires a more precise formulation | whether the operation result is bounded, provisional, partial, or otherwise classified |
| internally differentiated | heterogeneous carriers or relations are now explicit | that only a bounded-claim class is possible |
| partially preserved | specified parts of the prior function remain warranted | whether the operation as a whole is partial, admissible, provisional, or failed |
| rejected | the prior source-function claim does not survive the finer reconstruction | that the DECOMPOSE occurrence failed |
| underdetermined | the finer reconstruction does not settle the prior source-function claim | whether a usable provisional operation result or non-capture is primary |

### 18.4 Source-function rejection rule

```text
admissible DECOMPOSE
+
source function rejected
≠
failed_transformation
```

The operation result, canonical class, source-function effect, and prior source-claim result remain separate.

| Result layer | Illustrative result |
|---|---|
| DECOMPOSE operation | admissible decomposition |
| Canonical output class | `admissible` |
| Source-function effect | rejected |
| Prior source claim | withdrawn, failed, or separately reduced and retested |

This table is explanatory prose, not a final record schema.

## 19. PROJECT_AS / RETYPE Result Mapping

### 19.1 Mapping table

| Local PROJECT_AS or RETYPE result | Canonical class | Selection condition |
|---|---|---|
| admissible functional projection | `admissible` | origin type, Source Trace, context, function, sensitivity, and loss duties pass |
| admissible narrow projection | `admissible_with_bounded_claim` | the function is warranted only within a narrow context or scope |
| context-dependent projection | `admissible` or `admissible_with_bounded_claim` | ordinary declared target-context boundedness supports `admissible`; use the bounded class only when a material narrowing relative to the tested claim is the decisive result |
| provisional projection | `admissible_but_provisional` | source, counterfactual, calibration, or rival limits remain material |
| compatible multiple projections | `admissible` or `admissible_with_bounded_claim` | use `admissible` where declared context separation is ordinary and complete; use the bounded class where material reach restrictions are decisive |
| competing projections | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one projection is provisionally preferred while a material rival remains; partial functions remain; or no warranted selection is available |
| useful structural analogy | `analogy_only` | resemblance is retained without source-traceable functional projection |
| analogy only | `analogy_only` | the local result already states the bounded analogy outcome |
| label substitution | `failed_transformation` | no source-dependent functional gain is established |
| invalid type jump | `failed_transformation` | origin type is overwritten or a primitive is invented |
| unmarked level mixing | `failed_transformation` | source and target positions collapse |
| mandatory claim reduction | `claim_reduction_required` | only a weaker function, context, or analogy remains supportable |
| operation-specific mandatory stop | `mandatory_stop` | further projection is inadmissible |
| operation-specific non-capture | `non_capture` | no adequate target function can be established |

### 19.2 PROJECT_AS cautions

```text
Φ Recontextualization
≠
PROJECT_AS
```

```text
structural analogy
≠
valid functional projection
```

```text
target function
≠
origin type
```

A failed projection may leave the source object and a bounded analogy intact.

---

## 20. Record-Level Status and Method-Concept Separation

### 20.1 Record-level status architecture

| Record-level axis | What it says | What it does not decide |
|---|---|---|
| support status | whether the delimited claim is supported, provisional, contested, underdetermined, or unsupported | automatic canonical class |
| resolution-test result | what a valid granularity comparison produced | support status or operation failure automatically |
| claim disposition | whether a claim is maintained, withdrawn, failed, or superseded without erasure | source-object validity or support status automatically |
| capture statement | what remains captured or uncaptured and under which limiting condition | automatic canonical `non_capture` without a completed Non-Capture test |

```text
record status
≠
one flat mixed status enum
```

### 20.2 Method-concept matrix

| Method concept | Canonical value | Separation rule |
|---|---|---|
| admissible transformation | one of the ten canonical classes, selected according to the actual governance result | the method concept does not settle scope, provisionality, partiality, failure, stop, or capture boundary |
| resolution neutrality | `resolution_neutral` | class applies only after a valid resolution test |
| structural analogy | `analogy_only` where projection is not established | analogy is not automatically a valid or invalid PROJECT_AS |
| claim reduction | `claim_reduction_required` | method action and output identifier remain distinct |
| mandatory stop | `mandatory_stop` | broader stop discipline also includes optional stop |
| failed transformation | `failed_transformation` | prose concept and machine value have distinct roles |
| Non-Capture | `non_capture` | the concept includes forms and records beyond the value spelling |

---

## 21. Operation Chains and Integrated Results

### 21.1 Required chain discipline

For each chain:

```text
operation occurrence
→ local result
→ canonical class
→ loss account
→ preserved prior results
```

This applies to at least:

```text
COMPOSE → PROJECT_AS
COMPOSE → DECOMPOSE
DECOMPOSE → COMPOSE
DECOMPOSE → PROJECT_AS
PROJECT_AS → DECOMPOSE
COMPOSE → PROJECT_AS → DECOMPOSE
```

### 21.2 No retroactive validation

A later `admissible` class cannot erase an earlier `failed_transformation`, `mandatory_stop`, or `non_capture` result.

### 21.3 Integrated partiality

Use `partially_admissible` for an integrated claim only when the admissible and non-admissible parts are explicitly separable and retained.

Do not use it as an average of chain results.

### 21.4 Integrated non-capture

An integrated `non_capture` result may be appropriate when no chain-level reconstruction can retain the relevant heterogeneity, source trace, and type integrity.

The individual operation results remain visible.

### 21.5 Integrated failure

An integrated `failed_transformation` must identify which declared integrated transformation or claim failed. It must not turn a successful component into a failed operation.

---

## 22. Claim, Stop, Failure, and Re-Entry Effects

| Canonical class | Immediate claim effect | Continuation effect | Re-entry requirement |
|---|---|---|---|
| `admissible` | retain claim as tested | continuation optional and separately justified | new extension requires new test |
| `admissible_with_bounded_claim` | retain bounded claim only | no scope transfer | test any expansion |
| `admissible_but_provisional` | retain with explicit provisional qualifier | further support work may continue | new evidence or calibration |
| `resolution_neutral` | retain prior warranted reconstruction | further identical refinement unnecessary | new distinction or grounds |
| `analogy_only` | retain the bounded analogy claim; withdraw any stronger projection if one was made | resemblance alone does not authorize PROJECT_AS | a later projection claim requires full projection duties |
| `partially_admissible` | retain specified parts only | separate unresolved or failed parts | separate records |
| `claim_reduction_required` | current claim not retained as stated | revise before further use | test reduced claim |
| `mandatory_stop` | preserve result reached before boundary | current continuation prohibited | changed grounds and new record |
| `failed_transformation` | reject declared transformation result | no retroactive rescue | materially new operation claim |
| `non_capture` | state captured and uncaptured structure | avoid false closure | changed limiting condition or rival framework |

### 22.1 Re-entry is not continuation

```text
re-entry
≠
unrecorded continuation
```

### 22.2 Claim ceiling remains independent

A canonical class does not raise the permitted claim type or authority ceiling.

```text
admissible output
≠
authority inheritance
```

---

## 23. Formal Model Handoff

The later `07_model/Output_Classes.yaml` may formalize:

- the exact ten-value enum;
- machine-readable identifiers;
- required descriptive fields;
- operation applicability metadata;
- prohibited extra values;
- mappings used by validation examples;
- structural requirements for rationale and re-entry fields.

It may not automatically decide:

- empirical truth;
- causal adequacy;
- semantic or normative validity;
- whether a claim deserves application authority;
- which class is substantively correct merely because fields are complete.

Output classes classify transformation records and claims. They are not person types, institution types, diagnoses, rankings, sanctions, or legitimacy judgments.

### 23.1 Structural validation versus judgment

```text
valid enum value
≠
valid substantive classification
```

```text
schema completeness
≠
truth proof
```

### 23.2 No premature schema

The tables in this index are reference structures, not final YAML or JSON schemas.

`07_model/Output_Classes.yaml` remains unchanged until Formal Model v0.

---

## 24. Historical Pre-Block Output-Class Gate

Before Foundations production, verify:

1. Exactly ten canonical values are used.
2. Every value uses exact lowercase `snake_case`.
3. No local result, record-level status declaration, support status, claim disposition, or method concept is treated as an eleventh class.
4. Each operation occurrence can receive one justified canonical class.
5. Multi-operation chains preserve component classes.
6. Integrated results do not overwrite local failure, stop, or non-capture.
7. `admissible` remains distinct from a bounded-claim output: ordinary Contextual Boundedness does not automatically require `admissible_with_bounded_claim`.
8. `admissible_with_bounded_claim` remains distinct from `admissible_but_provisional` and `partially_admissible`.
9. `admissible_but_provisional` and `partially_admissible` each remain distinct from `non_capture`.
10. `claim_reduction_required` remains distinct from an already tested bounded claim.
11. `resolution_neutral` is used only for a valid resolution or granularity test.
12. `analogy_only` remains distinct from label substitution and valid projection.
13. `mandatory_stop` remains distinct from optional stop and automatic failure.
14. `failed_transformation` remains distinct from non-capture.
15. A successful DECOMPOSE may reject a prior source claim without becoming failed.
16. Stop triggers and re-entry conditions remain in the record.
17. No output class implies empirical truth, causal proof, diagnosis, sanction, or authority inheritance.
18. Formal validation remains bounded to structure and allowed values.
19. Claim Type Table remains the separate place for claim-type and claim-ceiling architecture.

Failure of this gate requires correction before the Output Class Index is treated as provisionally stable.

---

## 25. Definition-Site and Reference Map

| Subject | Designated primary definition site | Method elaboration | Principal application sites | Reference handoff |
|---|---|---|---|---|
| canonical output system and all ten class identifiers | Chapter 6 | Chapter 53 integrated taxonomy | Chapters 17, 28, and 40 | this index |
| operation-specific result | Chapter 6 | Chapter 7 record architecture | Chapters 17, 28, 40, and 53 | Transformation Operation Index; Glossary |
| record-level status declaration | Chapter 7 | operation and case records | all operation and audit records | Glossary; Claim Type Table; Evidence Map |
| bounded-claim result | Chapter 6 | Chapter 39 contextual limits | Chapters 17, 28, 40, and 53 | Non-Equivalence Index; later Claim Type Table |
| provisional admissibility | Chapter 6 | Chapter 49 source and calibration limits | Chapters 17, 28, 40, and 53 | later Admissibility Band Reference |
| resolution neutrality | Chapter 6 | Chapters 25, 27, and 44 | SUB and resolution audits | Glossary; Non-Equivalence Index |
| analogy-only result | Chapter 6 | Chapters 37 and 39 | RETYPE and cross-domain audits | Non-Equivalence Index |
| partial admissibility | Chapter 6 | Chapters 52 and 53 | mixed claims and integrated audits | later Claim Type Table |
| claim-reduction-required result | Chapter 6 | Chapter 51 | Chapters 17, 28, 40, and 53 | Glossary; later Claim Type Table |
| mandatory-stop output class | Chapter 6 | Chapter 51 stop method | local boundaries in Chapters 16, 27, and 39 | Glossary; `04_reference/Audit_Checklist.md` |
| failed-transformation output class | Chapter 6 | operation failure specifications | Chapters 15, 20, 30, and 53 | Transformation Operation Index |
| non-capture output class | Chapter 6 | Chapter 52 Non-Capture method | local boundaries and Chapter 53 | Glossary; Admissibility Band Reference; `04_reference/Audit_Checklist.md` |
| integrated result | Chapter 53 | integrated cases and audits | integrated audit records | `04_reference/Audit_Checklist.md` and later Case Index |

### 25.1 Claim Type Table boundary

This index may state whether a claim is retained, bounded, provisional, partial, reduced, failed, or not adequately captured.

It does not define the complete claim-type taxonomy, claim-reach relations, evidential and support conditions, or final Claim Ceiling matrix.

Those belong in:

```text
04_reference/Claim_Type_Table.md
```

---

## 26. Revision and Freeze Policy

This is a provisional Reference Kernel artifact.

During Block and case production it may be updated when:

- a local result lacks a clear mapping;
- a collision rule produces ambiguity;
- a class definition conflicts with canonical prose;
- a new case reveals an uncovered but non-new result family;
- model formalization exposes a structural inconsistency;
- a claim-type distinction requires a clearer handoff.

It may not be updated merely to:

- create a more attractive synonym;
- add a case-specific label as a system-wide class;
- rank classes;
- make failure or non-capture less visible;
- protect a preferred transformation;
- inherit authority from technical implementation.

Final freeze occurs only after:

```text
Cases
→ Conclusion and Front Matter
→ Appendices
→ Reference Freeze
```

---

## 27. Compact Control Summary

```text
local operation result
→ one justified canonical output class
```

```text
canonical output class
≠
truth status
≠
causal proof
≠
authority grant
```

```text
bounded
≠
provisional
≠
partial
```

```text
claim reduction required
≠
already admissible bounded claim
```

```text
mandatory stop
≠
failed transformation
≠
non-capture
```

```text
new transformation
=
new testable claim
```

The output system remains valid only where it preserves operation identity, claim boundaries, local results, loss, failure, stop, and non-capture without converting governance classification into substantive authority.

---

## Chapter 2 Coordinate and Scope Output Handoff

Chapter 2 does not create a new Output Class. It constrains when existing classes may be used for coordinate and scope claims.

| Chapter 2 pressure | Canonical class candidate | Boundary |
| --- | --- | --- |
| bounded local claim under declared coordinates and scopes | `admissible_with_bounded_claim` | not truth certification |
| valid finer/coarser comparison with no changed warranted reconstruction | `resolution_neutral` | not mere detail increase |
| one resolution preserves only separable parts | `partially_admissible` | failed part remains explicit |
| claim exceeds temporal, source, or claim scope | `claim_reduction_required` | original overclaim remains recorded |
| hierarchy lacks comparator/relation or reduction is refused | `mandatory_stop` | Stop is not a finding |
| forced universal scale destroys locally valid relations | `non_capture` | no protection for weak local claims |

A coordinate switch creates a new testable claim. It cannot be used to remap an earlier failed result into an admissible class without a new full test.

---

## Chapter 3 Output-Class Handoff

Chapter 3 examples route only through the canonical ten-class vocabulary. Typical bounded routes include `admissible_with_bounded_claim` for a supported local temporal object, `claim_reduction_required` when a stronger historical property fails but a weaker object remains, `mandatory_stop` when unsupported inflation is continued, and `non_capture` when competing trajectory constructions cannot be responsibly closed.

---

## Chapter 4 Output-Class Handoff

Operation classification and operation success remain separate. Chapter 4 examples may route to `admissible_with_bounded_claim`, `analogy_only`, `resolution_neutral`, `claim_reduction_required`, `mandatory_stop`, `failed_transformation`, or `non_capture`, but no Output Class becomes an operation and no Stop or Non-Capture result protects an unsupported strong claim.

---

## Chapter 5 Continuity Output Handoff

Chapter 5 creates no new Output Class. Mixed continuity findings remain visible and map only at the local or integrated result layer.

| Continuity pressure | Candidate canonical route | Boundary |
| --- | --- | --- |
| supported source-sensitive local function | `admissible_with_bounded_claim` | not global validity or authority |
| unresolved but separable continuity component | `admissible_but_provisional` or `partially_admissible` | local findings remain explicit |
| metaphorical association below function threshold | `analogy_only` | not `PROJECT_AS` proof |
| material source change weakens strong function | `claim_reduction_required` | original overclaim remains recorded |
| type replacement or authority transfer insisted upon | `mandatory_stop` | Stop is a governance result, not substantive proof |
| continuity or projection claim fails | `failed_transformation` | valid source object may remain |
| rival functions cannot be responsibly closed | `non_capture` | neither strong rival is protected |

A new target context is a new testable claim and cannot remap an earlier failure into success without a new full test.

## Chapter 6 Admissibility-Band Output Handoff

Chapter 6 creates no new Output Class. It supplies substantive boundary findings that later routing maps to the existing ten-class vocabulary.

| Band pressure | Possible canonical route | Required separation |
| --- | --- | --- |
| all applicable burdens pass as declared | `admissible` | not truth certification |
| material narrowed scope passes after retest | `admissible_with_bounded_claim` | not unrevised Claim Reduction |
| coherent claim remains under material support limitation | `admissible_but_provisional` | not generic incompleteness |
| valid supported refinement changes no warranted reconstruction | `resolution_neutral` | not below-floor unsupported detail |
| bounded resemblance remains below projection threshold | `analogy_only` | not label substitution |
| separable components receive different results | `partially_admissible` | no averaging or class stacking |
| current claim must be weakened and retested | `claim_reduction_required` | weaker claim not pre-authorized |
| continuation crosses a mandatory boundary | `mandatory_stop` | earlier valid findings remain |
| declared operation does not succeed | `failed_transformation` | weaker remainder may survive |
| relevant structure cannot be responsibly selected or integrated | `non_capture` | rival strong claims not protected |

`below_floor`, `sensitive`, `insensitive`, `underdetermined`, or a stop trigger are local findings, not automatic canonical classes.

Production control: [`Chapter 6 Preparation Record`](Chapter_6_Preparation_Record.md).

---

## Chapter 6 WP1 Lower-Bound Output Route

WP1 does not create a `gain`, `neutral`, `below_floor`, or `underdetermined` Output Class. These are local lower-bound findings.

| WP1 condition | Candidate canonical route | Boundary |
| --- | --- | --- |
| supported distinction changes a warranted reconstruction | full-band assessment remains required | positive floor finding alone does not authorize `admissible` |
| supported comparison shows the distinction is not load-bearing | `resolution_neutral` | only where reference, typing, comparison, and source support remain valid |
| stronger claim depends on inert detail | `claim_reduction_required` or `failed_transformation` after full routing | no automatic class from the floor finding alone |
| repeated refinement continues after purchase is exhausted | `mandatory_stop` when continuation is prohibited and insisted upon | earlier valid neutral result remains visible |
| available sources cannot determine whether the distinction changes the claim | `admissible_but_provisional`, reduction, failure, or `non_capture` may later be considered | no mechanical route from uncertainty alone |

```text
resolution_neutral
= valid no-gain result
≠ generic below-floor bucket
```

Canonical return: [`Chapter 6 WP1`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP2 Upper-Bound Output Route

WP2 introduces no Output Class. `TraceableLoad` pass/fail and the five Counterfactual Sensitivity findings remain local rule results.

| Upper-bound condition | Candidate later route | Boundary |
| --- | --- | --- |
| source-result dependency supported | full integrated assessment remains required | positive ceiling finding alone does not authorize `admissible` |
| strong claim exceeds load but a narrower claim is testable | `claim_reduction_required` | narrower claim must be restated and retested |
| only bounded resemblance remains | `analogy_only` | no forced `PROJECT_AS` |
| declared target is source-independent | `failed_transformation` may apply after full routing | citation or utility cannot compensate |
| source gap leaves one coherent bounded claim | `admissible_but_provisional` may apply | gap and re-entry condition must be explicit |
| rival source mappings cannot be responsibly selected | `non_capture` may apply after integrated review | underdetermined finding alone is insufficient |
| analyst insists rhetorical fit replaces missing load | `mandatory_stop` may apply | earlier valid local findings remain visible |

Canonical return: [`Chapter 6 WP2`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP3 Integrated Output Routing

Chapter 6 preserves exactly ten canonical Output Classes. Local band and rule findings remain inputs to substantive routing rather than automatic aliases.

| Canonical class | Chapter-6 boundary role |
| --- | --- |
| `admissible` | all applicable load-bearing requirements pass for the declared claim and scope |
| `admissible_with_bounded_claim` | positive passage depends on an explicit material restriction that has been retested |
| `admissible_but_provisional` | one coherent bounded claim survives with named material support or counterfactual limits |
| `resolution_neutral` | valid refinement adds no praxis finding and conceals no other defect |
| `analogy_only` | bounded resemblance remains without established source-traceable projection |
| `partially_admissible` | separable stages or subclaims retain different outcomes |
| `claim_reduction_required` | present claim must be weakened, restated, and retested before passage |
| `mandatory_stop` | continuation crosses a binding boundary under present conditions |
| `failed_transformation` | the declared operation does not establish its required result |
| `non_capture` | relevant structure exceeds responsible selection or integration under the current basis |

```text
below_floor ≠ resolution_neutral automatically
insensitive ≠ failed_transformation automatically
underdetermined ≠ non_capture automatically
stop trigger ≠ mandatory_stop automatically
```

Canonical return: [`Chapter 6 WP3`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 Provisional-Lock Output Boundary

Chapter 6 preserves exactly ten canonical Output Classes and creates no aliases from local Rule findings.

```text
below_floor
≠ resolution_neutral automatically

insensitive
≠ failed_transformation automatically

underdetermined
≠ non_capture automatically

stop trigger
≠ mandatory_stop automatically
```

Class selection remains claim-relative and substantive after segmentation, full applicable-Rule review, alternatives, loss, continuity, boundary adjudication, and route justification. No weighted score or threshold selects a class.

Canonical return: [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 7 Preparation — Record Status and Output Boundary

The Shared Transformation Record will preserve separate support, resolution, disposition, capture, routing, and canonical-result axes.

```text
support_status
≠ resolution_test_result
≠ claim_disposition
≠ capture_statement
≠ routing_state
≠ canonical Output Class
```

For a `routed` record, exactly one of the ten canonical Output Classes is selected for each delimited tested claim after substantive adjudication. A `formal_diagnostic` record has no canonical Output Class.

The following mappings are prohibited:

```text
provisional support
→ admissible_but_provisional automatically

failed claim disposition
→ failed_transformation automatically

capture limit present
→ non_capture automatically

formal diagnostic
→ failure, stop, or non-capture automatically
```

Chapter 7 records and separates these axes. Chapter 6 retains ownership of Output Class selection semantics.

---

## Chapter 7 WP1 Output Boundary

WP1 uses canonical outputs only where the case already reaches a substantive boundary. It does not define the status/result routing architecture reserved for Section 7.9.

```text
record syntax
≠ canonical Output Class
```

- `C7-OP-02` reaches `mandatory_stop` because the occurrence collapses two operation kinds.
- `C7-REC-02` may later route to `claim_reduction_required` or `failed_transformation`, but WP1 does not infer the class from syntax alone.
- `C7-SRC-01` may remain formal-diagnostic or support a narrower claim; underdetermination alone is not `non_capture`.

Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 7 WP2 Output-Routing Boundary

WP2 records Admissibility findings, Loss, Alternatives, and Governance but does not define the Section-7.9 status architecture.

| WP2 condition | Possible later route | Boundary |
| --- | --- | --- |
| all record families complete | any canonical class remains possible | completeness does not select the class |
| local Rule finding such as `underdetermined` | provisional, reduced, failed, diagnostic, or non-capture routes may remain possible | local finding is not an Output Class |
| explicit empty loss category | no direct Output-Class consequence | empty ≠ no loss proved |
| rival operation identified | sibling record and separate route | rivalry does not decide either claim |
| non-translation identified | no STRATA operation for that claim; analogy or failure may remain separately testable | non-translation is not a fourth operation or Output Class |
| prohibited authority inference | `mandatory_stop` for the continuation | bounded prior analytical result may remain |

Canonical Output Class ownership remains in Chapter 6 and the Output-Class registry; Section 7.9 will define record-axis separation.

---

## Chapter 7 WP3 Status-to-Output Routing Boundary

| Record-axis finding | Canonical routing consequence |
| --- | --- |
| `support_status: provisional` | no automatic class; bounded or provisional routes remain separately testable |
| `resolution_test_result: resolution_neutral` | no automatic class; canonical `resolution_neutral` still requires full conditions |
| `claim_disposition: failed` | no automatic `failed_transformation`; segment and lineage must be inspected |
| `capture_limit_present: true` | no automatic `non_capture`; constitutive claim-relative boundary required |
| `routing_state: routed` | exactly one of the ten canonical classes per delimited claim |
| `routing_state: formal_diagnostic` | no canonical Output Class |
| chain-level summary | preserves, but does not replace, occurrence-level classes |

Formal Diagnostics remain process states outside the ten-class inventory.

---

## Chapter 7 WP4 Provisional-Lock Synchronization

Chapter 7 is provisionally locked after integrated ownership, redundancy, status, case-duty, prose-to-schema, link, schema, fingerprint, package, and roundtrip audit. The Shared Transformation Record records transformation claims without becoming the transformation, a truth proof, or an authority source. The existing record schema supplies lower-authority structural carriers; its Chapter-7 handoff annotation does not redefine canonical prose. The sixteen Chapter-7 case identifiers remain later production duties rather than completed evidence. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 8 WP4 Non-Equivalence Routing Boundary

A foundational non-equivalence breach is not an eleventh Output Class and does not mechanically select one of the ten canonical classes.

```text
pair breach
→ local audit finding
→ claim segmentation and full routing burden
```

Depending on the delimited claim and surrounding findings, later routing may preserve a bounded claim, require reduction, retain analogy only, stop continuation, mark transformation failure, or preserve Non-Capture. The pair itself does not decide among them.

## Chapter 9 Provisional-Lock Routing Boundary

Chapter 9 preserves the closed ten-class system and keeps local temporal states separate from canonical outputs.

```text
transition candidate
≠ Output Class

formal_diagnostic
≠ Output Class

failed transition claim
≠ failed_transformation automatically
```

A delimited claim may route to `admissible_with_bounded_claim`, `claim_reduction_required`, `failed_transformation`, `mandatory_stop`, `non_capture`, or another applicable canonical class only after the full local rule pattern is considered. No eleventh class or transition-specific score is introduced. Canonical return: [`Chapter 9`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

## Chapter 10 Provisional-Lock Routing Boundary

Chapter 10 preserves the closed ten-class system and keeps Path candidates, evidence states, qualified statuses, comparison findings, and formal diagnostics separate from canonical outputs.

```text
path candidate ≠ Output Class
qualified path status ≠ Output Class
incomparability ≠ new Output Class
formal_diagnostic ≠ Output Class
failed Path claim ≠ failed_transformation automatically
```

A delimited claim may route to an applicable canonical class only after the full rule pattern is considered. No eleventh class, Path-status class, comparison score, ranking class, or automatic route selector is introduced. Canonical return: [`Chapter 10`](../01_blocks/02_part_i_path.md#chapter-10-path).

## Chapter 11 Provisional-Lock Routing Boundary

Chapter 11 local findings must map only to the ten canonical Output Classes. `Trajectory candidate`, profile status, construction relation, `False Trajectory`, and record completeness are not additional Output Classes.

| Local Chapter 11 state | Possible canonical routing boundary |
| --- | --- |
| complete bounded Trajectory burden | `admissible`, `admissible_with_bounded_claim`, or `admissible_but_provisional` |
| weaker surviving claim after overreach | `claim_reduction_required` or `partially_admissible` |
| known failed Trajectory used for stronger derivation | `mandatory_stop` |
| substantive Trajectory burden fails | `failed_transformation` where the operation-level claim fails |
| materially rival source-responsible constructions remain undecidable | `non_capture` |
| additional detail adds no praxeological purchase | `resolution_neutral` where applicable |

No route is automatic. False Trajectory diagnosis, field completeness, model validity, or Chapter 11 lock cannot select an Output Class without the full rule pattern.

## Chapter 12 Provisional-Lock Routing Boundary

Chapter 12 introduces no new Output Class. Local dependence-strength findings map to the fixed canonical vocabulary. Supported bounded claims may route to `admissible_with_bounded_claim` or `admissible_but_provisional`; failed stronger claims with preserved weaker support route to `claim_reduction_required`; no additional historical purchase may route to `resolution_neutral`; known anti-laundering misuse routes to `mandatory_stop`; materially rival undecidable explanations may route to `non_capture`.

```text
local dependence strength
≠ canonical Output Class
```

Canonical return: [`Chapter 12 completion boundary`](../01_blocks/02_part_i_path.md#chapter-12-completion-boundary).

## Chapter 13 Provisional-Lock Routing Boundary

Chapter 13 introduces no branch-status Output Class. Local findings such as realized, rejected, blocked, aborted, deferred, lost, unresolved, or not established map to the fixed canonical vocabulary. Supported bounded claims may route to `admissible_with_bounded_claim` or `admissible_but_provisional`; overclaimed statuses with preserved weaker support route to `claim_reduction_required`; unsupported additions without praxeological purchase may route to `resolution_neutral`; known anti-laundering misuse routes to `mandatory_stop`; materially relevant but unresolved status relations may route to `non_capture`.

```text
branch status
≠ canonical Output Class
```

Canonical return: [`Chapter 13 completion boundary`](../01_blocks/02_part_i_path.md#chapter-13-completion-boundary).

## Chapter 14 Provisional-Lock Routing Boundary

Chapter 14 introduces no Non-Event-status Output Class. Local findings such as warranted `Λ`, Delay, repeated Non-Decision, Blocked Responsibility, Missing Repair, Missing Exit, sedimented, false, unresolved, or not established map to the fixed canonical vocabulary.

Supported bounded claims may route to `admissible_with_bounded_claim` or `admissible_but_provisional`; overclaimed `Λ` or sedimentation with preserved weaker support routes to `claim_reduction_required`; source- or resolution-limited claims may route to `resolution_neutral`; known anti-laundering misuse routes to `mandatory_stop`; materially relevant but unresolved expectation/non-realization relations may route to `non_capture`.

```text
Non-Event finding
≠ canonical Output Class
```

Canonical return: [`Chapter 14 completion boundary`](../01_blocks/02_part_i_path.md#chapter-14-completion-boundary).

## Chapter 15 Provisional-Lock Output Routing

Chapter 15 introduces no COMPOSE-specific Output Class. Local object, relation, strength, Loss, sensitivity, overelasticity, or failure findings map to the fixed ten-class vocabulary.

Supported bounded compositions may route to `admissible`, `admissible_with_bounded_claim`, or `admissible_but_provisional`; unresolved resolution may route to `resolution_neutral`; stronger overclaimed targets with preserved weaker findings route to `claim_reduction_required`; locally mixed results may route to `partially_admissible`; unsuccessful operation claims route to `failed_transformation`; known misuse for sanction, target function, or authority routes to `mandatory_stop`; irreducible materially supported compositions may route to `non_capture`.

```text
COMPOSE finding
≠ canonical Output Class
```

Canonical return: [`Chapter 15 completion boundary`](../01_blocks/02_part_i_path.md#chapter-15-completion-boundary).

## Chapter 16 Provisional-Lock Output Routing

Chapter 16 introduces no boundary-specific Output Class. Local Floor and Ceiling values map to the fixed ten-class vocabulary only after the full claim, source, Loss, sensitivity, governance, Stop, and Non-Capture pattern is assessed.

Supported bounded PATH claims may route to `admissible`, `admissible_with_bounded_claim`, or `admissible_but_provisional`; neutral detail may route to `resolution_neutral`; an overclaimed target with preserved weaker findings routes to `claim_reduction_required`; mixed local results may route to `partially_admissible`; a source-indifferent or destructive target routes to `failed_transformation`; known reuse beyond ceilings routes to `mandatory_stop`; irreducible adequate alternatives route to `non_capture`.

```text
boundary value pair
≠ automatic Output-Class selector
```

Canonical return: [`Chapter 16 completion boundary`](../01_blocks/02_part_i_path.md#chapter-16-completion-boundary).

## Chapter 17 WP1 Case Mapping Synchronization

All three WP1 cases map their bounded current claim to the existing canonical class `admissible`.

| Local result | Canonical class | Boundary |
|---|---|---|
| admissible bounded Path | `admissible` | no Trajectory or dependence inflation |
| admissible branching Path | `admissible` | no counterfactual-outcome or optimality claim |
| admissible source-sensitive Trajectory with central `Λ` | `admissible` | no strong Path Dependence or target function |

The mapping is reasoned in each record. It is not selected by schema validity, audit completion, case title, or index entry.

## Chapter 17 WP2-A Case Mapping Synchronization

`C17-HISTORY-01` and `C17-WEAKPD-01` map to `admissible_with_bounded_claim` because each retains a separately tested temporal claim only after material narrowing of broader historical reach.

```text
materially narrowed supported dependence claim
→ admissible_with_bounded_claim

schema-valid record
≠ automatic class selection
```

## Chapter 17 WP2-B Case Mapping Synchronization

`C17-CHRON-01` maps to `claim_reduction_required` because a precise weaker chronology remains source-grounded but untested. `C17-MACRO-01` and `C17-TEL-01` map to `failed_transformation` because their declared `COMPOSE` occurrences lack necessary constitutive formation.

```text
local audit pass
≠ transformation success
```


## Chapter 17 WP2-C Case Mapping Synchronization

`C17-OMEGA-01` maps to `failed_transformation` because the declared target removes constitutive source load. `C17-FALSEL-01` maps to `claim_reduction_required` because a precise event-field formulation remains source-grounded while the central `Λ` must be withdrawn.


## Chapter 17 WP3-A Case Mapping Synchronization

- `C17-PROJ-01` → `admissible_with_bounded_claim` because the source-sensitive Trajectory passes only after the Frame-function reach is separated.
- `C17-RES-01` → `resolution_neutral` because a valid source-supported refinement leaves the warranted reconstruction unchanged.
- `C17-ATTR-01` → `admissible_with_bounded_claim` because the Trajectory passes only after Attractor identity/function reach is excluded.

The mappings remain reasoned case results, not automated routing precedents.


## Chapter 17 WP3-B — Integrated PATH Output Census

The thirteen records instantiate: `admissible` (3), `admissible_with_bounded_claim` (4), `resolution_neutral` (1), `claim_reduction_required` (2), and `failed_transformation` (3). `admissible_but_provisional`, `partially_admissible`, `analogy_only`, `mandatory_stop`, and `non_capture` remain canonically available and are not manufactured to satisfy a quota. Counts do not route claims.

## Part I — PATH Provisional-Lock Output Boundary

The thirteen PATH case records retain their five-class census. The Part-level result `admissible_but_provisional` records provisional corpus closure and is not a fourteenth case, a class quota, a rank, or an automatic route. All ten canonical Output Classes remain available for later operations and cases.

## Chapter 20 Preparation Output-Mapping Boundary

Chapter 20 must retain four separate axes:

```text
local DECOMPOSE result
≠ source-function effect
≠ prior source-claim disposition
≠ canonical Output Class
```

Examples:

- `supported decomposition` is a local result, not an alias for `admissible`;
- `rejected` is a source-function effect, not an alias for `failed_transformation`;
- `insufficient source support` may route to `failed_transformation`, `mandatory_stop`, or `non_capture` depending on the tested claim and continuation boundary;
- a valid source-supported no-gain test may map to `resolution_neutral`;
- competing internal models do not automatically map to `non_capture`.

Primary preparation control: [`Chapter_20_Preparation_Record.md`](Chapter_20_Preparation_Record.md).

## Chapter 20 WP3 DECOMPOSE Mapping Return

Chapter 20 distinguishes open local decomposition results from the ten canonical classes. Mapping occurs only after source support, component relations, source-function effect, Loss, ceilings, Stop, Non-Capture, and distinct-claim separation are assessed.

Key mappings include:

- valid source-supported no-gain test → `resolution_neutral`;
- operation identity/procedure failure → possible `failed_transformation`;
- inadmissible continuation → `mandatory_stop`;
- no stable supported finer model → possible `non_capture`;
- successful operation with material unresolved support → possible `admissible_but_provisional`;
- successful operation after a tested material narrowing → possible `admissible_with_bounded_claim`.

No mapping is automatic. `analogy_only` is not a successful same-reference `DECOMPOSE` result.

Primary site: [§20.10](../01_blocks/03_part_ii_sub.md#20-10-decomposition-output).

## Chapter 20 WP4 Output-Mapping Lock

Chapter 20 is provisionally locked with the four result axes kept separate. Local operation descriptions and source-function effects remain non-class values. Canonical Output Classes are assigned only to a clearly segmented claim after source support, component relations, Loss, ceilings, Stop, and Non-Capture are assessed. No automatic mapper or class stacking on an undifferentiated claim is authorized.

Primary site: [Chapter-20 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-20-completion-boundary).

## Chapter 21 Preparation Output Boundary

Occurrence-family descriptions and source-function effects remain non-class values. A heterogeneous occurrence, rejected source typing, competing family model, or stable function with substitution receives a canonical Output Class only after the generic Chapter-20 gates are applied to a clearly segmented claim. No family-specific class or automatic mapper is authorized.

Preparation control: [Chapter 21 Preparation Record](Chapter_21_Preparation_Record.md).

## Chapter 21 WP3 Output-Mapping Return

The bounded Binding example maps a successful relational decomposition with an internally differentiated source function and reduced prior homogeneous claim to `admissible_with_bounded_claim`. The mapping is claim-specific and non-automatic. Type forcing or missing support may require `failed_transformation` or `claim_reduction_required`; inadmissible continuation requires `mandatory_stop`; absence of a stable supported family model may yield `non_capture` without preserving the original typing.

Primary sites: [§21.11](../01_blocks/03_part_ii_sub.md#21-11-binding-typed-occurrence) and [§21.12](../01_blocks/03_part_ii_sub.md#21-12-failed-operator-occurrence-decomposition).

## Chapter 21 WP4 Output-Mapping Lock

Chapter 21 is provisionally locked with local operation result, source-function effect, prior source-claim disposition, and canonical Output Class kept separate. Family names and source-function effects are not classes. `admissible_with_bounded_claim`, `failed_transformation`, `claim_reduction_required`, `mandatory_stop`, and `non_capture` remain claim-specific possibilities only after the generic Chapter-20 gates are applied; no automatic family mapper is authorized.

Primary site: [Chapter-21 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-21-completion-boundary).

## Chapter 22 Preparation — Composite Output Discipline

Local Chapter-22 findings such as constitutive, modulating, replaceable, compensatory, incidental, distributed, redundant, substitutable, integrated conflict, residual conflict, or stable-through-repair are not Output Classes. They describe component roles, relations, or source-function effects. Final routing must use only the ten canonical classes after the Chapter-20 result axes, Loss, Stop, and Non-Capture checks remain separate.

```text
local composite description
≠ canonical Output Class
```

Preparation control: [Chapter 22 Preparation Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP3 Output-Class Return

Composite stability, conflict integration, redundancy, substitution, local operation result, Source-Function Effect, and prior source-claim disposition are not Output Classes. The bounded current claim maps to exactly one canonical class only after reference, relation, support, Loss, Stop, and non-compensation burdens are tested.

The R-17C anchor maps the supported but internally differentiated composite decomposition to `admissible_with_bounded_claim`; this does not validate stronger inherited claims. `resolution_neutral`, `admissible_but_provisional`, `partially_admissible`, `claim_reduction_required`, `mandatory_stop`, `failed_transformation`, and `non_capture` remain available only under their own conditions.

Primary sites: [§22.10](../01_blocks/03_part_ii_sub.md#22-10-decomposition-of-a-composite-without-fragmentation) and [§22.11](../01_blocks/03_part_ii_sub.md#22-11-failed-composite-decomposition).

## Chapter 22 WP4 Output-Mapping Lock

Chapter 22 is provisionally locked with local operation result, source-function effect, prior source-claim disposition, and canonical Output Class kept separate. Component roles, weighting, profiles, conflict outcomes, and stability mechanisms are not classes. `admissible_with_bounded_claim`, `partially_admissible`, `claim_reduction_required`, `mandatory_stop`, `failed_transformation`, and `non_capture` remain claim-specific possibilities only after the complete Chapter-20 and Chapter-22 gates are applied; no automatic composite mapper is authorized.

Primary site: [Chapter-22 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-22-completion-boundary).

## Chapter 23 Preparation — Temporal Output Discipline

Event, Extended Event, Event Cluster, Non-Event, delay structure, repeated non-decision, categorical preservation, category revision, Event Inflation, and temporal granularity drift are source categories, local findings, failure descriptions, or resolution pressures. They are not canonical Output Classes.

Final routing must use only the ten canonical classes after local operation result, Source-Function Effect, prior source-claim disposition, Loss, Stop, and Non-Capture remain separate.

```text
local temporal category or effect
≠ canonical Output Class
```

Preparation control: [Chapter 23 Preparation Record](Chapter_23_Preparation_Record.md).



## Chapter 23 WP3 Output Boundary

Event, Extended Event, Event Cluster, Non-Event, Delay Structure, Repeated Non-Decision, `confirmed`, `refined`, `internally_differentiated`, `partially_preserved`, `rejected`, and `underdetermined` are local categories or effects, not canonical Output Classes. Chapter 23 keeps local operation result, category/Source-Function Effect, prior source-claim disposition, and canonical Output Class separate. Temporal Non-Capture does not confirm the coarse Event or Non-Event claim. Primary site: [§23.11](../01_blocks/03_part_ii_sub.md#23-11-event--non-event-confusion-results-and-completion).


## Chapter 23 Provisional-Lock Output Boundary

Chapter 23 is locally `admissible_but_provisional`. Event-like categories and the effects `confirmed`, `refined`, `internally_differentiated`, `partially_preserved`, `rejected`, and `underdetermined` remain local results rather than Output Classes. Failure, Mandatory Stop, and Non-Capture remain distinct, and `non_capture` does not rescue a coarse Event or Non-Event claim. Primary site: [Chapter 23 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-23-completion-boundary).

## Chapter 24 Preparation — PATH-Decomposition Output Discipline

Path, Trajectory, subpath, transition cluster, turning-point status, branch status, internal Frame change, competing continuation, compression debt, Path-Dependence profile, Same-Path status, and rival PATH classification are source categories, local findings, or operation-boundary determinations. They are not canonical Output Classes.

Final routing must use only the ten canonical classes after local operation result, source-function effect, prior claim disposition, Loss, Stop, and Non-Capture remain separate.

```text
local PATH-decomposition finding
≠ canonical Output Class
```

Preparation control: [Chapter 24 Preparation Record](Chapter_24_Preparation_Record.md).

## Chapter 24 WP3 Output Boundary

Path, Trajectory, subpath, transition cluster, turning point, branch status, internal Frame change, competing continuation, compression debt, Path-Dependence profile, Same-Path status, rival-PATH status, local operation result, source-function effect, and prior source-claim disposition are not canonical Output Classes.

The bounded R-24 illustration maps a supported relational decomposition with an internally differentiated source function and reduced prior claim to `admissible_with_bounded_claim`. This mapping does not establish complete history, one privileged periodization, Path Dependence in every dimension, causal sufficiency, legitimacy, prediction, or recommendation.

`claim_reduction_required`, `partially_admissible`, `mandatory_stop`, `failed_transformation`, and `non_capture` remain available only under their own conditions. Non-Capture does not rescue a coarse Path or Trajectory claim.

Primary sites: [§§24.11–24.12](../01_blocks/03_part_ii_sub.md#24-11-decomposition-versus-alternative-path-construction).

## Chapter 24 Provisional-Lock Output-Class Return

The chapter-level method maps to `admissible_but_provisional`. Application results remain claim-specific and must separately state local operation result, Path/Trajectory source-function effect, prior source-claim disposition, and one canonical Output Class. Turning-point status, branch status, compression debt, Same-Path/rival-PATH status, continuation accessibility, and Path-Dependence load are not Output Classes.

## Chapter 25 Preparation — Resolution Result and Output Discipline

The Chapter-25 local families are gain, neutral, drift, escape, unsupported, and non-capture. They do not form a second canonical Output-Class inventory.

Formal mapping remains distributed: the first four use the existing `resolution_test_result` vocabulary where applicable; unsupported refinement is expressed through support, claim disposition, Failure/Stop routing, and reason; Non-Capture uses the canonical `non_capture` class and capture statement.

```text
local resolution result
≠ source-function effect
≠ prior claim disposition
≠ canonical Output Class
```

Only a valid, supported, claim-complete neutral finding may route to the canonical class `resolution_neutral`.

Preparation control: [Chapter 25 Preparation Record](Chapter_25_Preparation_Record.md).

## Chapter 25 Provisional-Lock Output-Class Return

The chapter-level method maps to `admissible_but_provisional`. Application results must separately state local resolution family, source-function effect, prior source-claim disposition, and one canonical Output Class. `gain`, `neutral`, `drift`, `escape`, `unsupported`, Decomposition Fatigue, calibration state, Stop status, and re-entry condition are not additional Output Classes; only a valid supported neutral result may map to `resolution_neutral`.

## Chapter 26 Preparation Output-Class Boundary

Local operation-boundary findings such as `decompose_candidate`, `project_as_candidate`, `recontextualization_only`, `dual_operation_required`, `operation_boundary_underdetermined`, or `invalid_collapse_detected` are not canonical Output Classes.

A boundary finding must remain separate from:

- source-function or target-function effect;
- prior source-claim disposition;
- canonical Output Class.

Invalid collapse may create `claim_reduction_required`, `mandatory_stop`, `failed_transformation`, or `non_capture` pressure, but no mapping is automatic.

Preparation control: [Chapter 26 Preparation Record](Chapter_26_Preparation_Record.md).

## Chapter 26 Provisional-Lock Output-Class Return

The chapter-level method maps to `admissible_but_provisional`. Local boundary findings such as `decompose_candidate`, `project_as_candidate`, `recontextualization_only`, `dual_operation_required`, `operation_boundary_underdetermined`, and `invalid_collapse_detected` are not canonical Output Classes. Each actual operation Record receives exactly one canonical class; a dual-operation chain may therefore contain two independently classified Records.

## Chapter 27 Preparation — Boundary Findings and Output Mapping

Local findings such as `lower_boundary_reached`, `upper_boundary_exceeded`, Source-Ceiling status, component sensitivity, coarser-function status, and type-integrity status are not canonical Output Classes.

Possible canonical pressure includes:

- `resolution_neutral` where supported detail changes no warranted claim;
- `admissible_with_bounded_claim` where a limited finer reconstruction passes;
- `claim_reduction_required` where a weaker finding survives;
- `mandatory_stop` where continuation would cross a local boundary or fill source gaps;
- `failed_transformation` where source reference or relational reconstruction collapses;
- `non_capture` where responsible rival decompositions cannot be discriminated.

No mapping is automatic. Local boundary result, source-function effect, prior source-claim disposition, and canonical Output Class remain separate axes.

Preparation control: [Chapter 27 Preparation Record](Chapter_27_Preparation_Record.md).

## Chapter 27 Provisional-Lock Output Mapping Boundary

Chapter 27 preserves the ten canonical Output Classes without adding a local class list. Lower-boundary Neutrality, upper-boundary fragmentation, Source-Ceiling pressure, Claim Reduction, Stop, Failure, and Non-Capture remain local findings or routing burdens until the complete Record warrants exactly one canonical class.

Primary site: [Chapter 27 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-27-completion-boundary).

## Chapter 28 Preparation — SUB Case Mapping Discipline

Chapter-28 local descriptions such as admissible decomposition, source function confirmed/refined/differentiated/partially preserved/rejected, competing decompositions, unsupported decomposition, Resolution Drift, or Resolution Escape are not additional Output Classes.

Mapping pressure includes:

- bounded valid reconstruction → `admissible`, `admissible_with_bounded_claim`, or `admissible_but_provisional`;
- supported no-change → `resolution_neutral`;
- weaker surviving finding → `partially_admissible` or `claim_reduction_required`;
- analogy without source-bound reconstruction → `analogy_only`;
- prohibited continuation → `mandatory_stop`;
- failed source/reference/relation/operation claim → `failed_transformation`;
- responsible single capture unavailable → `non_capture`.

No mapping is automatic. Each actual Record receives exactly one canonical class, and every separate operation occurrence is classified independently.

Preparation control: [Chapter 28 Preparation Record](Chapter_28_Preparation_Record.md).

## Chapter 28 WP1 Positive Mapping Results

The six positive records select exactly one canonical class each: `C28-TRAJECTORY-01` selects `admissible`; the Frame, Attractor, Asymmetry, Non-Event, and Resolution-Gain cases select `admissible_with_bounded_claim`. Source-function effect and `resolution_gain` remain separate axes and do not mechanically determine the mapping.

## Chapter 28 WP2 Mapping Results

WP2 selects `mandatory_stop` for Overfine and Resolution Escape, `claim_reduction_required` for Unsupported Structure and False Macro-Asymmetry, `failed_transformation` for Operator Error and Fragmentation, and `partially_admissible` for both operation-confusion cases. These mappings remain claim-specific and non-automatic.

## Chapter 28 WP3 Mapping Results

`C28-ANALOGY-01` maps to `analogy_only`; `C28-MODULATOR-01` maps to `claim_reduction_required`. The complete Chapter-28 set uses only canonical classes. `resolution_neutral` and `non_capture` remain available even though no standalone Chapter-28 target selects them finally.

## Chapter 28 and Part II Provisional-Lock Output Discipline

The sixteen Chapter-28 standalone targets select seven of the ten canonical classes: one `admissible`, five `admissible_with_bounded_claim`, one `analogy_only`, two `partially_admissible`, three `claim_reduction_required`, two `mandatory_stop`, and two `failed_transformation`.

The census is descriptive, not a quota or routing rule. `admissible_but_provisional`, `resolution_neutral`, and `non_capture` remain available. The chapter- and Part-level result `admissible_but_provisional` is not a thirtieth case Record and does not overwrite individual mappings.

Primary site: [Chapter 28 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-28-completion-boundary).
