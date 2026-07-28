# PMS-STRATA — Output Class Index

**Status:** active Reference Kernel artifact; corpus-audit synchronized 
**Repository role:** closed ten-class output vocabulary and collision control; not an independent theory or authority source 
**Authority basis:** `PMS.yaml` → `00_source/PMS-STRATA_Structure.md` → `01_blocks/*` → `05_minified/*`; formal, case, appendix, and Reader artifacts remain subordinate to their canonical owners 
**Reference Freeze duty:** open bounded duty; this artifact may be corrected for ownership, routing, duplication, and carrier consistency without broadening any claim 

---

## 1. Role, Status, and Authority

This file is the active Reference registry for canonical PMS-STRATA output classes.

It consolidates the fixed system-wide result vocabulary, distinguishes it from local operation results and record status, and provides controlled mapping and selection guidance during canonical corpus maintenance while preserving the closed canonical inventory.

It is a reference and audit artifact. It does not replace the canonical prose, the Minified Kernel, the Formal Model, or case-specific judgment.

Authority order:

```text
PMS.yaml
→ unchanged PMS Base

00_source/PMS-STRATA_Structure.md
→ architecture and chapter blueprint

01_blocks/* 
→ canonical corpus prose

05_minified/*
→ binding control artifacts,
 subordinate to canonical corpus prose

04_reference/*
→ terminology, indexing, mapping, and audit navigation
```

The Minified Kernel remains a binding compact control source for the class inventory and compact meanings, subordinate to canonical prose.

This index may:

- register the exact ten canonical values;
- distinguish classes from local results, record status, and method concepts;
- provide operation-specific mapping guidance;
- state collision and selection rules;
- identify primary definition and application sites;
- route controlled requirements to the Formal Model.

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

Chapter 1 uses canonical Output Classes only for bounded local examples and chapter-audit dispositions. A chapter-level bounded status is not an eleventh class, a chapter rank, or proof that any case passes. `mandatory_stop`, `claim_reduction_required`, `failed_transformation`, and `non_capture` remain available for object-category and identity failures.

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

### 23.2 Reference/formal boundary

The tables in this index are reference structures, not YAML or JSON schemas. Formal spellings and validation constraints belong to `07_model/Output_Classes.yaml`; that carrier may not redefine the prose-owned class meanings.

---
