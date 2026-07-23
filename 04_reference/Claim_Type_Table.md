# PMS-STRATA — Claim Type Table

**Status:** Reference Kernel v0.2.40 — Chapter-10-WP2-synchronized claim architecture  
**Repository role:** `04_reference` registry, ceiling, reduction, and audit handoff; not an independent theory source  
**Authority basis:** `PMS.yaml`, `00_source/PMS-STRATA_Structure.md`, `05_minified/*`, the provisionally locked canonical Foundations Chapters 0–8 in `01_blocks/01_foundations.md`, the provisionally controlled Reference Kernel, and `04_reference/Chapter_1_Preparation_Record.md` through `04_reference/Chapter_8_Preparation_Record.md` as non-theory production controls

---

## 1. Role, Status, and Authority

This file is the provisional Gate 3 registry for claim architecture in PMS-STRATA.

It distinguishes what a claim asserts from where it applies, how strongly it is supported, what ceiling constrains it, what operation produced or tested it, and which canonical output class governs its result.

It is a reference and audit artifact. It does not replace current or future canonical prose, the Shared Transformation Record, the Output Class Index, the Admissibility Band, operation-specific procedures, case judgment, or the later formal model.

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
→ terminology, registry, mapping, and audit navigation
```

Before Block lock, the Minified Kernel and Chapter Contracts remain the operative control sources. This table may consolidate and distinguish their claim vocabulary but may not enlarge the authority or empirical reach of a claim.

This table may:

- register controlled claim families and operations-specific claim forms;
- distinguish claim type, claim reach, claim ceiling, support mode, support status, evidence availability, record-level status declaration, claim disposition, record role, and output class;
- identify minimum source, continuity, counterfactual, calibration, and loss burdens;
- document admissible reduction relations without creating a universal rank;
- identify external-warrant and prohibited claim categories;
- preserve failed, withdrawn, rival, and successor claims across operation chains;
- provide a bounded handoff to the later formal model.

This table may not:

- create a closed universal enum of all possible claims;
- turn PATH-specific claim types into a system-wide hierarchy;
- treat support status or output class as a claim type;
- infer empirical truth, actual causality, semantic adequacy, or model superiority;
- authorize person typing, diagnosis, ranking, sanction, legitimacy judgment, or intervention;
- create a new PMS primitive, a fourth STRATA operation, or an ontology of real strata;
- define machine fields not already fixed by the canonical kernel;
- convert a successful transformation into authority beyond its sources, Claim Ceiling, and independent Authority Ceiling.

```text
more structure
≠
more authority
```

---

## 2. Meaning and Limits of Claim Type

A **claim type** identifies the kind of structural, temporal, compositional, decompositional, functional, analogical, continuity, capture, or governance assertion made by a claim.

It answers:

```text
What kind of relation, object attribution, structural assertion, functional assertion, or governance assertion is being made?
```

It does not by itself answer:

- how far the assertion reaches;
- whether the claim is supported, provisional, contested, underdetermined, or unsupported;
- which source or calibration ceiling applies;
- whether the operation is admissible;
- which canonical output class results;
- whether the claim is empirically true;
- whether action, sanction, diagnosis, or authority is justified.

Canonical separations:

```text
claim type
≠
claim scope
≠
claim ceiling
≠
support status
≠
record-level status declaration
≠
operation-specific result
≠
canonical output class
```

```text
claim family
≠
claim type
≠
universal rank
```

A **claim family** is a registry grouping of structurally related claim types. A **claim type** is the declared assertion kind of one tested claim. A family is not a Record class, Output Class, or pre-authorized machine field.

### 2.1 Open registry, controlled vocabulary

The table is open to domain-specific wording but closed against unmarked category creation. Local wording must map to an existing claim family. A genuinely new structural assertion remains non-canonical pending explicit Reference Kernel revision and cannot be treated as a canonical claim type before that revision.

```text
open domain vocabulary
≠
unbounded claim architecture
```

```text
new local wording
→ map to an existing family

new structural assertion
→ non-canonical pending Reference Kernel revision
```

### 2.2 Claim type and sentence wording

Different sentences can instantiate the same claim type. Similar wording can instantiate different claim types.

Example:

```text
"History frames the present."
```

can be:

- a rhetorical analogy;
- a trajectory-to-frame-function projection claim;
- an unsupported label substitution;
- a broad generalization above the claim ceiling.

Classification depends on the asserted relation, source trace, target context, counterfactual burden, and scope—not the surface vocabulary alone.

---

## 3. Claim Architecture Overview

PMS-STRATA uses a multidimensional claim architecture rather than a single ladder.

```text
claim domain
+
primary claim family
+
operation or method context
+
reference object and typing
+
claim reach
+
source and continuity burden
+
claim ceiling
+
support status
+
record-level status declaration
+
record role
+
operation-specific result
+
canonical output class
```

### 3.1 Dimension matrix

| Dimension | Question | Examples | Not equivalent to |
| --- | --- | --- | --- |
| Claim domain | What role does the claim play? | system boundary; transformation; warrant; capture | claim type |
| Primary claim family | Which registry grouping contains the assertion? | temporal formation; source function; target function; analogy | claim type, scope, or status |
| Operation context | Which operation tests or produces it? | COMPOSE; DECOMPOSE; PROJECT_AS | a fourth operation |
| Reference and typing | What object remains the same, and how is it typed? | reference object; origin type; occurrence typing | operator type replacement |
| Reach | Where and how far does it apply? | frame-bound; temporal; context-bound; generalizing | support strength |
| Warrant burden | What must carry the claim? | source trace; continuity; counterfactual load; calibration | citation count |
| Claim ceiling | What is the maximum warranted structural and source-supported assertion? | bounded by source, type, context, continuity, calibration, and loss; assessed under an independent authority ceiling | Traceability Ceiling alone |
| Support status | How well is the claim presently carried? | supported; provisional; contested; underdetermined; unsupported | support mode, availability, disposition, or claim type |
| Record-level status declaration | How are support, resolution, disposition, and capture information preserved without flattening them? | separate support-status, resolution-result, claim-disposition, and capture statements | one mixed status enum or output class |
| Record role | How does it relate to other claims? | initial; prior; revised; rival; successor | output class |
| Operation-specific result | What occurred locally? | admissible path; source function refined; analogy only | canonical class |
| Canonical output class | What governance result applies? | admissible; reduction required; non_capture | truth value |

### 3.2 Claim family, claim type, and claim role

The registry distinguishes grouping, asserted relation, and the role a claim plays within a transformation record.

| Layer | Meaning | Example | Not equivalent to |
| --- | --- | --- | --- |
| Claim family | Registry grouping of structurally related claim types | Projection family | a canonical claim type or universal rank |
| Claim type | Declared assertion kind of one tested claim | functional-projection claim | scope, support status, or output class |
| Claim role within an operation | How the claim contributes to the record | primary transformation claim; supporting claim; scope qualifier; rival claim; governance claim | claim family |

Typical role distinctions:

| Claim wording | Role in the record |
| --- | --- |
| functional-projection claim | primary transformation claim |
| target-function claim | constitutive subclaim of the projection |
| source-trace claim | supporting warrant claim |
| validity-scope claim | scope and boundary claim |
| narrow projection | materially bounded form of the primary claim, not a separate universal family |
| competing-projection claim | rival or compatibility claim |

The same family may contain primary, supporting, scope, rival, and governance claims. These roles do not become new Output Classes or machine fields.

### 3.3 No universal strength score

PMS-STRATA permits local reduction relations such as trajectory → path or projection → analogy. These relations do not combine into a universal numerical or ordinal scale.

```text
local reduction relation
≠
global claim score
```

A path claim may be stronger than a sequence claim with respect to transition structure, while an analogy claim and a component-role claim are not points on the same axis.

---

## 4. System Claims versus Transformation Claims

### 4.1 System and boundary claims

System claims state the method's own scope, authority, and failure conditions.

| Controlled claim | Core assertion | Designated primary site | Application or elaboration | Boundary |
| --- | --- | --- | --- | --- |
| governing claim | what STRATA positively specifies | Chapter 0 | system-wide application | not an empirical result |
| claim boundary | what STRATA or a record may not assert | Chapter 0 | final closure in Chapter 57 | not an output class |
| final claim boundary | restated terminal authority limit | Chapter 57 | none | not a new broader claim |
| authority-boundary claim | what authority cannot be inherited | Chapter 0 | Chapters 6 and 53 | not application authorization |
| negative-capability claim | where stopping or non-capture is methodically required | Chapter 51 | Non-Capture elaboration in Chapter 52; integration in Chapter 53 | not immunity from criticism |

System claims govern the method. They are not normal claims about a particular transformed object and do not receive authority from an operation occurrence.

### 4.2 Transformation claims

Transformation claims concern a concrete occurrence of `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` and its declared source, reference object, coordinates, loss, alternatives, and result.

```text
transformation claim
≠
operation type
```

A transformation claim is occurrence-bound. Reusing an operation type in a new context creates a new claim.

### 4.3 Warrant and governance claims

Warrant and governance claims assess whether a transformation claim is supportable and how it must be limited.

Examples:

- admissibility claim;
- continuity claim;
- source-support claim;
- counterfactual-load claim;
- calibration claim;
- stop claim;
- non-capture claim;
- rival-comparison claim.

They do not become a fourth core operation.

---

## 5. Claim Type, Scope, Ceiling, Status, and Output

### 5.1 Controlled separation table

| Layer | Canonical meaning | Typical values or forms | Must not be used as |
| --- | --- | --- | --- |
| Claim type | kind of asserted relation | path claim; source-function claim; target-function claim | scope, status, or class |
| Claim scope/reach | where and how far the claim applies | reference-bound; frame-bound; temporal; context-bound | claim type |
| Claim ceiling | maximum warranted assertion, including relation, reach, precision, generality, functional scope, and dependence strength | source-, context-, type-, continuity-, calibration-, and loss-bounded maximum; separately subject to the Authority Ceiling | confidence score or universal rank |
| Support status | current support condition | supported; provisional; contested; underdetermined; unsupported | support mode, evidence availability, claim disposition, record-level status declaration, or output class |
| Record-level status declaration | record architecture that preserves separate support, resolution, disposition, and capture information | separate declarations rather than one mixed list | claim type, claim disposition, or output class |
| Record role | relation to other claims | prior; revised; rival; successor | claim family or claim disposition |
| Operation-specific result | local description of what occurred | admissible path; source function rejected; analogy only | new class |
| Canonical output class | system-wide governance result | exact ten-class vocabulary | truth or authority verdict |

### 5.2 Same claim type, different output

The same claim type can receive different output classes in different records.

```text
path claim
→ admissible
→ admissible_with_bounded_claim
→ admissible_but_provisional
→ claim_reduction_required
→ failed_transformation
→ non_capture
```

The class depends on the tested record, not on the claim family alone.

### 5.3 Same output, different claim types

`admissible` can govern a sequence claim, decomposition claim, source-function claim, projection claim, continuity claim, or another properly delimited claim. The class does not erase the claim type.

---

## 6. Object and Typing Claims

Object and typing claims establish what is being transformed and which type boundaries must remain visible. They do not classify persons or decompose PMS operator types.

### 6.1 Operator-occurrence typing claim

| Field | Controlled content |
| --- | --- |
| Claim domain | Object and typing |
| Operation or method context | All Parts; Chapter 1 and operation-specific records |
| Asserted relation | A concrete reference object is reconstructed as expressing a PMS operator function or belonging to another declared analytical object class. |
| Minimum warrant | Identifiable reference object; occurrence-level source support; declared context and claim boundary; explicit distinction from the operator type. |
| Required continuity | Reference Continuity and Type Integrity. |
| Counterfactual burden | Would materially changed occurrence features defeat or revise the typing? |
| Maximum ordinary reach | Reference-object and occurrence bound. |
| Typical reduction | Narrow the occurrence typing, mark mixed typing, or leave underdetermined. |
| Prohibited inflation | Operator-type decomposition; person typing; type immutability; new primitive. |
| Designated primary site | [Chapter 1 WP1](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure). |
| Application sites | Chapters 20–21 and 47. |

### 6.2 Origin-type claim

| Field | Controlled content |
| --- | --- |
| Claim domain | Object and typing |
| Operation or method context | PROJECT_AS; Chapters 5 and 30 |
| Asserted relation | The source object retains a declared origin type while a contextual target function is tested. |
| Minimum warrant | Source-object identity; declared source basis; origin-type support; explicit origin/target separation. |
| Required continuity | Type Integrity and Reference Continuity. |
| Counterfactual burden | Would the source still be identifiable as the same origin-typed object if the projected function failed? |
| Maximum ordinary reach | Source-object bound; preserved across the PROJECT_AS record. |
| Typical reduction | Revise the occurrence typing in a separate claim or withdraw PROJECT_AS. |
| Prohibited inflation | Target function replacing origin type; authority inheritance. |
| Designated primary site | Chapter 5. |
| Application sites | Chapters 29–30 and 47. |

### 6.3 Object-class claim

| Field | Controlled content |
| --- | --- |
| Claim domain | Object and typing |
| Operation or method context | All operations |
| Asserted relation | A source, target, component, composite, or remainder belongs to a declared analytical object class. |
| Minimum warrant | Explicit class criteria and reference relation. Configuration claims require bounded temporal location, frame relativity, operator structure, praxis relevance, and selective incompleteness; event-like claims require realized relevant change and a bounded unit; non-event-structure claims require supported expectation, bounded condition, non-realization, and praxeological load; transition-object claims require identifiable configurations, supported order, intervening structure, changed praxis conditions, and a declared boundary; derived-object or function claims require identified sources, declared operation or chain, formation rule, constitutive trace, bounded coordinates and loss, non-primitive status, and a stop condition. |
| Required continuity | Reference Continuity; Type Integrity where operator occurrences are involved. |
| Counterfactual burden | Would altered constitutive criteria change the class assignment? |
| Maximum ordinary reach | Record and object bound. |
| Typical reduction | Use a more generic class, reduce a non-event to a source-gap claim, reduce a transition to endpoint difference, reduce a purported derived object to analytical shorthand or descriptive grouping, or leave the class provisional. |
| Prohibited inflation | Derived analytical object treated as PMS primitive; missing information treated as non-event structure; dated occurrence treated as relevant event-like change; endpoint difference treated as transition. |
| Designated primary site | [Chapter 1](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure). |
| Application sites | Chapters 4, 7, 15, 20, and 30. |

### 6.4 Reference-identity claim

| Field | Controlled content |
| --- | --- |
| Claim domain | Object and typing |
| Operation or method context | All operations and chains |
| Asserted relation | Two descriptions, resolutions, or transformation positions concern the same bounded historical or structural reference object. |
| Minimum warrant | Bounded reference; supported typing; constitutive relations; function where relevant; temporal or historical continuity where relevant; declared uncertainty, loss, and identity limit. |
| Required continuity | Minimum object-identification burden from Chapter 1; full Reference Continuity and related criteria from Chapter 5 where the operation requires them. |
| Counterfactual burden | What change would defeat the claimed reference relation, and which evidence would discriminate continuation, replacement, succession, or reconstitution? |
| Maximum ordinary reach | Across the declared comparison, operation, or record chain only. |
| Typical reduction | State partial or bounded continuity, state a succession relation without exact identity, create a new source object and record, stop the stronger identity claim, or record Non-Capture for an undistortable forced classification. |
| Prohibited inflation | Same label treated as same object; changed label treated as discontinuity; historical lineage treated as functional invariance; identity assumed after projection; Non-Capture used to retain a stopped claim. |
| Designated primary site | [Chapter 1](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) for the minimum object-identity claim family; Chapter 5 for full continuity criteria. |
| Application sites | Chapters 5, 7, and 47. |

### 6.5 Object-typing audit

```text
operator-occurrence typing claim
≠
operator type
```

```text
object typing
≠
person typing
```

```text
origin-type claim
≠
target-function claim
```

An occurrence typing can be revised by new source-supported analysis. Such revision does not alter the PMS operator type and does not authorize silent origin-type replacement within the same PROJECT_AS occurrence.

---

## 7. COMPOSE and PATH Claim Types

PATH has the most explicit operations-specific claim vocabulary. The sequence → path → trajectory relation is a local object-formation reduction path, not a global scale for all claims.

### 7.1 PATH and COMPOSE registry

| Claim type | Asserted relation | Minimum warrant | Does not imply | Typical reduced form | Designated primary site | Application sites |
| --- | --- | --- | --- | --- | --- | --- |
| sequence claim | Selected temporal ordering among declared analytical units. | Typed units; declared ordering basis; supported order; bounded coordinates and scopes. | path, trajectory, causality, or total order where only partial order is supported | chronology, partial sequence, or unresolved internal order | Chapter 3 §3.6 | Chapters 9 and 15 |
| path claim | Actually traversed selectively reconstructed chain of relevant configurations and transitions. | Sequence; traversal trace; selection rule; constitutive relation; branch/omission and loss disclosure. | complete chronology, complete causality, trajectory, or path dependence | sequence or chronology claim | Chapter 3 §3.7 | Chapters 10 and 15 |
| branch-closure claim | A relevant alternative became unavailable, excluded, prohibitively costly, or structurally closed. | Identified branch; closure mechanism; timing; counterfactual alternative. | all unchosen options were impossible | weaker exclusion or cost claim | Chapter 11 | Chapter 15 |
| trajectory claim | A path carries source-supported historical load that conditions later praxis. | Path support; retained load; traceable later effect; bounded claim; loss disclosure. | duration, teleology, inevitability, or path dependence | path or localized carry-over claim | Chapter 3 §3.8 | Chapters 11–12 and 15 |
| sedimentation claim | Earlier structures leave durable load in later configurations. | Traceable residue, expectation, role, cost, exclusion, or binding. | trajectory as a whole; determinism | localized persistence claim | Chapter 13 | Chapters 12 and 31 |
| path-dependence claim | Earlier ordering materially constrains later possibility or cost. | Path trace; alternatives; historical load; specified dependence strength. | trajectory alone; inevitability | weak order dependence | Chapter 14 | Chapter 15 |
| declared-composite claim | Selected source structures form a new analytical object under a declared formation rule. | Selection; ordering where relevant; constitutive relations; loss profile. | parts list; target function | narrower composite or no-composition | Chapter 15 | Chapter 17 |
| formation-rule claim | A specified relation makes the sources constitutive of the new composite. | Rule capable of discriminating included, compressed, and excluded sources. | narrative convenience | descriptive grouping | Chapter 15 | Chapter 17 |
| constitutive-relation claim | A source relation is load-bearing for composite identity. | Source trace and removal/change test. | mere co-occurrence | modulating relation | Chapter 15 | Chapter 46 |

### 7.2 Sequence claim

A sequence claim asserts relevant temporal order. It does not assert that one configuration structured the transition to the next or that alternatives were closed.

```text
sequence claim
≠
path claim
```

### 7.3 Path claim

A path claim adds structured transition and alternative relations. It must identify what makes the order praxeologically load-bearing rather than merely chronological.

```text
chronology
≠
path
```

### 7.4 Trajectory claim

A trajectory claim adds repeated or sedimented historical load. It can be admissible even when strong path dependence is not established.

```text
path
≠
trajectory
≠
path dependence
```

### 7.5 Path-dependence claim

The minimum controlled distinction is:

```text
weak order dependence
≠
strong path dependence
```

Weak order dependence states that order matters to the observed result. Strong path dependence additionally requires a materially constrained later possibility space, cost structure, lock-in, or branch closure that cannot be reduced to simple succession.

### 7.6 COMPOSE-specific composite claims

COMPOSE can create a declared composite without creating a path, trajectory, or target function.

```text
composite claim
≠
parts-list claim
```

```text
COMPOSE result
≠
PROJECT_AS target-function claim
```

### 7.7 PATH claim ceiling examples

| Available support | Maximum ordinary claim | Blocked inflation |
| --- | --- | --- |
| ordering only | sequence claim | path or trajectory |
| ordering plus supported transition structure | path claim | trajectory or path dependence |
| path plus recurrence and sedimentation | trajectory claim | strong path dependence |
| traceable branch closure or cost dependence | bounded path-dependence claim | historical inevitability |
| selected sources plus formation rule, no temporal dependence | declared-composite claim | path or target function |

---

## 8. DECOMPOSE and SUB Claim Types

SUB claims reconstruct finer relations within the same reference object. They never decompose PMS operator types and never gain truth priority merely through finer resolution.

### 8.1 SUB registry

| Claim type | Asserted relation | Primary operation or test |
| --- | --- | --- |
| decomposition claim | A compressed occurrence or composite can be reconstructed at finer granularity as the same reference object. | DECOMPOSE |
| internal-structure claim | Specified components and relations organize the source object. | DECOMPOSE |
| component-relation claim | Relations among components are reconstructed across declared role, substitutability, compensation, and remainder axes. | DECOMPOSE |
| constitutive-component claim | Changing or removing the component would materially alter the reconstructed source function or object identity. | DECOMPOSE plus counterfactual test |
| modulating-component claim | The component changes intensity, timing, direction, or expression without carrying the source function alone. | DECOMPOSE |
| replaceable-component claim | The source function can be maintained through alternative components or arrangements. | DECOMPOSE plus alternative model |
| compensatory-component claim | The component offsets, restores, or redistributes functional load under declared conditions. | DECOMPOSE plus alternative and counterfactual test |
| incidental-component claim | The feature is present but does not carry material constitutive, modulating, substitutive, or compensatory load for the tested claim. | DECOMPOSE plus Relevance Floor test |
| source-function claim | The coarser source object performs a specified function that finer analysis may confirm, refine, differentiate, partially preserve, reject, or leave underdetermined. | DECOMPOSE |
| resolution-gain claim | Finer distinctions are tested for whether they change the warranted praxis reconstruction. | Valid granularity comparison |
| heterogeneity claim | Different internal configurations or component roles coexist within the same coarse source object. | DECOMPOSE |
| competing-internal-model claim | More than one source-supported finer reconstruction remains materially viable. | DECOMPOSE plus rival comparison |

### 8.2 Decomposition claim

A decomposition claim must declare:

- the compressed source object;
- the decomposition question;
- expected praxeological difference;
- chosen granularity;
- components and relations;
- source support;
- source-function test;
- loss and alternatives.

```text
decomposition claim
≠
claim of final constituents
```

### 8.3 Component-role claims

The component-role vocabulary is relational, occurrence-bound, and multidimensional. It does not form a single reduction ladder.

| Tested axis | Controlled local results |
| --- | --- |
| Functional load | constitutive; strongly modulating; weakly modulating; incidental; underdetermined |
| Substitutability | replaceable; non-replaceable; conditionally replaceable |
| Compensation | compensatory; non-compensatory; unresolved |
| Remainder status | integrated; residual; uncaptured |

A component can be strongly modulating and replaceable, compensatory and non-replaceable, or incidental without being a weaker form of a modulating component.

```text
component-role claim
≠
residual or remainder status
```

Local claim reduction must name the axis being reduced. No component role becomes an ontology of component kinds or a stable person, institution, or domain type.

### 8.4 Source-function claims

A source-function claim concerns the coarser object. DECOMPOSE can produce a separate source-function effect:

```text
confirmed
refined
internally differentiated
partially preserved
rejected
underdetermined
```

Canonical separation:

```text
DECOMPOSE operation result
≠
source-function effect
≠
prior source-claim result
```

A valid DECOMPOSE may reject the prior source-function claim while the operation remains admissible.

### 8.5 Resolution claims and results

The tested claim is a `resolution-gain claim`. Resolution neutrality is a local result and a canonical Output Class, not a parallel regular claim type.

```text
tested claim:
resolution-gain claim

possible local results:
resolution gain
resolution-neutral result
resolution drift
resolution escape

canonical output when the valid test changes no warranted reconstruction:
resolution_neutral
```

Unsupported detail, atomization, resolution drift, or resolution escape does not qualify as resolution neutrality.

### 8.6 SUB claim ceiling examples

| Available support | Maximum ordinary claim | Blocked inflation |
| --- | --- | --- |
| plausible component list without relations | descriptive component hypothesis | decomposition claim |
| supported components and relations | internal-structure claim | final constituents |
| change/removal sensitivity | constitutive-component claim | universal necessity |
| multiple supported internal arrangements | competing-internal-model claim | single final decomposition |
| valid finer test with no changed reconstruction | resolution-neutral result for the tested resolution-gain claim | resolution gain |
| finer evidence undermines coarse function | source-function claim with a rejected or refined source-function effect | failed DECOMPOSE automatically |

---

## 9. PROJECT_AS and RETYPE Claim Types

RETYPE claims concern bounded contextual function. Origin type remains visible, and the target function never becomes a new PMS primitive.

### 9.1 RETYPE registry

| Claim type | Asserted relation | Primary operation or test |
| --- | --- | --- |
| functional-projection claim | An origin-typed source object performs a bounded contextual target function. | PROJECT_AS |
| target-function claim | A precisely named function exists in a declared target context and depends on source-side load. | PROJECT_AS |
| contextual-function claim | The function holds only under specified frame, time, level, and application conditions. | PROJECT_AS |
| narrow-projection claim | A materially restricted target-function claim has been tested and retained. | PROJECT_AS |
| multiple-compatible-projection claim | More than one bounded function can coexist without erasing distinct target contexts or source traces. | PROJECT_AS plus compatibility audit |
| competing-projection claim | More than one materially incompatible projection remains viable or unresolved. | PROJECT_AS plus rival comparison |
| structural-analogy claim | A declared resemblance is useful while functional projection, semantic preservation, or identity is not established. | Analogy audit; not a fourth operation |
| source-trace claim | Specified source features carry, modulate, or limit the projected function. | Constitutive Source Trace |
| validity-scope claim | The projected function is valid only within declared contextual and temporal limits. | PROJECT_AS |

### 9.2 Functional-projection claim

A functional-projection claim requires at minimum:

- identifiable source object;
- declared origin type;
- source and target coordinates;
- specific target context;
- precisely named target function;
- expected praxis difference;
- Constitutive Source Trace;
- Counterfactual Sensitivity;
- validity scope;
- claim ceiling;
- loss and alternatives.

```text
origin-type claim
≠
target-function claim
```

### 9.3 Target-function claim

The target function must remain dependent on concrete source-side features. A target label, resemblance, translation success, or semantic fit is insufficient.

```text
target function
≠
target label
```

### 9.4 Analogy claim

A structural-analogy claim preserves declared resemblance without asserting a source-traceable contextual function.

```text
analogy claim
≠
functional projection claim
≠
label substitution
```

An analogy claim can be intentionally tested as the maximum warranted assertion on the declared projection-to-analogy axis. It does not presuppose a failed PROJECT_AS occurrence.

### 9.5 Competing projection claims

Three distinct outcomes must remain available:

- one coherent candidate is currently supportable while a material rival remains open → provisional claim;
- separable projections or subclaims receive different results → partial claim structure;
- no adequate projection remains without distortion → non-capture claim.

Competing projections do not automatically imply one of these results without record-specific judgment.

### 9.6 RETYPE claim ceiling examples

| Available support | Maximum ordinary claim | Blocked inflation |
| --- | --- | --- |
| similar terminology or form only | structural-analogy claim | functional projection |
| source trace without counterfactual sensitivity | provisional projection hypothesis | admissible target-function claim |
| source trace plus context and change sensitivity | bounded target-function claim | origin-type replacement |
| one supportable candidate with unresolved serious rival | provisional projection claim | rival dismissal |
| multiple compatible functions with separate contexts | multiple-compatible-projection claim | single totalizing type |
| no source-dependent functional difference | analogy or failed projection claim | label substitution as PROJECT_AS |

---

## 10. Continuity and Integrity Claims

Continuity claims support transformation identity. They are distinct claim families and cannot substitute for one another.

| Claim type | Core question | Minimum burden | Does not imply | Designated primary site | Application sites |
| --- | --- | --- | --- | --- | --- |
| reference-continuity claim | Does the transformation concern the same reference object? | identity criteria across records or resolutions | same label is sufficient | Chapter 5 | Chapter 47 |
| type-integrity claim | Does the origin or occurrence type remain visible without silent replacement? | typed source and explicit revision rule | occurrence typing is immutable | Chapter 5 | Chapter 47 |
| functional-continuity claim | Does the source or target function depend on identified load-bearing structure? | source trace and change sensitivity | semantic similarity is sufficient | Chapter 5 | Chapters 30 and 47 |
| temporal-continuity claim | Does relevant order and historical load remain traceable across compression? | declared compression and preserved temporal relations | complete chronology is required | Chapter 5 | Chapters 3, 15, and 47 |
| contextual-boundedness claim | Is the claim confined to a specified target context and validity scope? | declared frame, time, level, and limits | arbitrary locality | Chapter 5 | Chapter 39 |

### 10.1 Continuity does not guarantee admissibility

A continuity claim can pass while another mandatory gate fails. Conversely, a transformation can preserve reference continuity while revising a source-function claim.

```text
continuity passed
≠
all admissibility conditions passed
```

### 10.2 Continuity and chains

Every chain handoff must state which object, type, function, and temporal relation continues into the next operation. No later operation inherits continuity automatically.

---

## 11. Admissibility and Governance Claims

Governance claims classify the warrant and permitted continuation of a transformation record. They are not claims about empirical truth or application legitimacy.

| Claim family | Core assertion | Required basis | Output interaction |
| --- | --- | --- | --- |
| admissibility claim | The declared operation and claim lie within the Admissibility Band. | all applicable gates and operation conditions | one canonical output class |
| PraxisPurchase claim | The distinction changes a warranted praxis reconstruction. | declared practical difference and countercase | supports entry above the Relevance Floor |
| TraceableLoad claim | The transformation remains reconstructibly dependent on source load. | source trace, loss, continuity, counterfactual burden | supports staying below the Traceability Ceiling |
| source-support claim | Available sources warrant the asserted detail and reach. | source resolution, relevance, and limitations | constrains Claim Ceiling |
| calibration claim | Thresholds and distinctions discriminate rather than merely restate labels. | comparators, rival cases, or explicit limits | often provisional if open |
| stop claim | Further continuation is mandatory or optional to stop. | identified stop condition and re-entry rule | may map to mandatory_stop or retain another class with optional stop |
| rival-comparison claim | Alternatives have been identified and tested to the permitted degree. | serious rival or no-transformation option | may support provisional, partial, failure, or non-capture |
| authority-boundary claim | No result licenses diagnosis, sanction, ranking, legitimacy, or automatic action. | PMS and STRATA governance limits | no authority inheritance |

### 11.1 Mandatory common checks

The record must address as applicable:

```text
PraxisPurchase
TraceableLoad
TypeIntegrity
Reference Continuity
Functional Continuity
Contextual Boundedness
Counterfactual Sensitivity
Source Ceiling
Claim Ceiling
Stop
Non-Capture
loss
```

A claim does not need to pass every check to receive a legitimate negative, bounded, provisional, stop, failure, or non-capture result. It must expose the result of each applicable check.

---

## 12. Capture, Non-Capture, and Rival Claims

Capture claims state what the present method and record can adequately reconstruct. They must not be used as rhetorical closure.

```text
capture claim
≠
capture status field
```

```text
Non-Capture
≠
non-capture claim
≠
non_capture
```

`Non-Capture` is the methodological concept; a non-capture claim states a record-bound capture limit; `non_capture` is the canonical Output Class.

| Claim type | Required statement | Blocked shortcut |
| --- | --- | --- |
| capture claim | what object, relation, or function is adequately reconstructed | full capture implied by one successful operation |
| partial-capture claim | which separable structures are captured and which remain outside | automatic partially_admissible |
| non-capture claim | what cannot be adequately captured, under which limiting condition, and with what re-entry possibility | immunity from criticism |
| rival claim | a materially different reconstruction or no-transformation option remains viable | rival superiority without testing |
| alternative-account claim | a different account explains the same source material with less or different transformation | dismissal by label |

### 12.1 Capture is claim-relative

A record may capture ordering but not path formation, path formation but not path dependence, internal components but not their final relation, or analogy but not projection.

```text
capture of one claim type
≠
capture of all stronger or adjacent claims
```

### 12.2 Partial capture and output class

Partial capture does not automatically produce `partially_admissible`. The class depends on the tested claim and may coexist with `admissible_but_provisional`, `partially_admissible`, `mandatory_stop`, or `non_capture`. Separability of captured structures does not by itself establish separable admissibility results.

### 12.3 Non-Capture requirements

A non-capture claim must identify:

1. the tested claim;
2. what remains uncaptured;
3. the limiting source, type, context, calibration, loss, or grammar condition;
4. why forced reduction would distort rather than responsibly narrow;
5. any plausible rival or external method;
6. a re-entry condition where one exists.

---

## 13. Claim Relations, Dispositions, and Failure Preservation

Claim relations describe how claims are connected in a record sequence. Claim dispositions describe what happened to a claim. Neither is a claim type.

```text
claim relation or record role
≠
claim disposition
```

### 13.1 Claim relations and record roles

| Record role | Meaning | Preservation rule |
| --- | --- | --- |
| initial claim | first declared claim tested in a record | remains identifiable after revision |
| current tested claim | claim presently under audit | receives the operation-specific result and output class |
| prior claim | earlier claim relevant to a later record | cannot be silently overwritten |
| revised claim | same intended issue restated with corrected content or scope | requires explicit relation to prior claim |
| reduced claim | narrower claim proposed after overreach | must be retested before admissibility is assigned |
| successor claim | new claim produced by a new transformation, frame, level, or target function | does not repair the prior claim retroactively |
| alternative claim | different plausible account retained for comparison | must remain visible where material |
| rival claim | materially incompatible candidate | cannot be dismissed by formal preference alone |

### 13.2 Claim dispositions

| Disposition | Meaning | Preservation rule |
| --- | --- | --- |
| maintained | claim remains actively asserted within its recorded scope | later records do not silently widen it |
| withdrawn | claim is no longer maintained | withdrawal reason remains recorded |
| failed | claim did not survive its required test | failure persists across later transformations |
| superseded without erasure | a successor or revised claim is now current | the prior claim and its result remain traceable |

### 13.3 Anti-immunization rule

```text
new transformation
=
new testable claim
```

```text
successor claim
≠
repaired prior claim
```

A switch of frame, granularity, relative level, operation, composition, or target function cannot erase an earlier failure. The new claim receives a new record and result.

### 13.4 Operation result and prior claim result

A later operation can be admissible while a prior claim fails. The record must preserve both results.

---

## 14. Claim Reach and Generalization

Claim reach states where and how far a claim applies. It is not a claim type and not a confidence score.

| Reach marker | Meaning | Default ceiling implication |
| --- | --- | --- |
| reference-object bound | applies only to the identified object | no class-wide generalization |
| operation-occurrence bound | applies only to one COMPOSE, DECOMPOSE, or PROJECT_AS occurrence | no inheritance to later operations |
| frame-bound | applies within one declared frame | new frame requires a new claim |
| context-bound | applies within one target context and validity scope | no cross-context transfer |
| temporal | applies within a declared period or order relation | no indefinite persistence |
| local relational | applies to a specified relation among components or actors | no global property claim |
| cross-level | connects declared relative levels under continuity and traceability | no ontological layer claim |
| cross-context | compares or projects across contexts with explicit transfer burden | often requires bounded or provisional result |
| category-wide | applies to a declared object category | requires repeated and calibrated support |
| generalizing | extends beyond observed records | requires independent external support |
| universal | asserts unrestricted applicability | normally above STRATA authority unless independently established |

### 14.1 Reach control rules

```text
local function
≠
global property
```

```text
one target context
≠
all later contexts
```

```text
repeated cases
≠
universal law
```

### 14.2 Material narrowing

A claim can be ordinarily context-bounded and still receive `admissible`. `admissible_with_bounded_claim` is reserved for a material narrowing that is itself the decisive governance result.

---

## 15. Support Status, Record-Level Status, and Resolution-Test Results

Support status describes the current condition of support for a claim. Resolution-test results describe what a valid granularity comparison produced. Claim disposition records whether a claim is maintained, withdrawn, failed, or superseded without erasure. A record-level status declaration preserves these axes and any capture statement without collapsing them into one mixed status enum. None of these dimensions is a claim type or canonical Output Class.

```text
support mode
≠
support status
≠
evidence availability
≠
claim disposition
≠
record-level status declaration
≠
resolution-test result
≠
canonical output class
```

### 15.1 Support status

The controlled pre-Block semantic inventory is:

| Support status | Meaning | Does not automatically imply |
| --- | --- | --- |
| supported | current sources and tests adequately carry the delimited claim | empirical truth or `admissible` |
| provisional | the claim remains usable while material source, calibration, rival, or counterfactual limits remain | `admissible_but_provisional` without class audit |
| contested | a serious objection, contradiction, or rival remains active | claim failure |
| underdetermined | available grounds do not discriminate among materially different claims | `non_capture` in every case |
| unsupported | current sources and tests do not carry the declared claim at the required relation, reach, precision, or functional load | claim disposition `failed`, source-object invalidity, or one mechanically fixed output class |

```text
unsupported claim
≠
failed claim automatically
```

### 15.2 Record-level status declaration

A record-level status declaration is an architecture, not a flat enum. It keeps at least the following information separate where applicable:

| Record-level axis | Controlled content | Not equivalent to |
| --- | --- | --- |
| support status | supported; provisional; contested; underdetermined; unsupported | support mode or output class |
| resolution-test result | resolution gain; resolution-neutral result; resolution drift; resolution escape | support status |
| claim disposition | maintained; withdrawn; failed; superseded without erasure | support status |
| capture statement | what remains captured or uncaptured, under which limiting condition and re-entry possibility | generic record status `non-capture` or automatic `non_capture` |

### 15.3 Resolution-test results

| Resolution-test result | Meaning | Does not automatically imply |
| --- | --- | --- |
| resolution gain | finer distinctions change the warranted reconstruction | higher truth |
| resolution-neutral result | valid finer test produces no changed reconstruction | failed transformation |
| resolution drift | detail increases without praxeological discrimination | non-capture automatically |
| resolution escape | unresolved objection is moved indefinitely to finer detail | legitimate continuation |

### 15.4 Status is not class

```text
support status: provisional
≠
canonical class: admissible_but_provisional automatically
```

The class requires a complete governance result for the tested claim.

### 15.5 Support downgrade is not claim-type reduction

```text
supported
→ provisional
```

This is an illustrative support-status change, not a universal hierarchy. `contested`, `underdetermined`, and `unsupported` describe different conditions rather than mandatory stages. No support-status change by itself converts a trajectory claim into a path claim or a projection claim into an analogy claim.

```text
illustrative support change
≠
universal status hierarchy
```

---

## 16. Claim Ceiling Matrix

The Claim Ceiling is the maximum warranted structural and source-supported assertion—including its relation, reach, precision, generality, functional scope, and dependence strength—permitted by the combined source, operation, continuity, context, calibration, and loss constraints. It remains separately subject to the Authority Ceiling, which is not a gradual Claim Ceiling dimension.

```text
available source support
+
operation identity
+
reference and type integrity
+
continuity
+
context and scope
+
counterfactual load
+
calibration
+
loss
→
maximum warranted structural and source-supported claim

separately:

maximum warranted structural and source-supported claim
+
Authority Ceiling satisfied
→
permitted STRATA claim
```

```text
claim ceiling
≠
Source Ceiling
≠
Praxeological Traceability Ceiling
```

### 16.1 Ceiling controls

| Control | Primary question | Primarily constrains | Typical result when exceeded |
| --- | --- | --- | --- |
| Praxeological Relevance Floor | Does the distinction create praxeological purchase? | whether the claim merits transformation at all | resolution_neutral, mandatory_stop, or failure depending on operation |
| Source Ceiling | Do sources support the detail, precision, and inference? | claim detail and evidential reach | bounded, provisional, reduction, stop, or non-capture |
| Praxeological Traceability Ceiling | Can the abstraction still be reconstructed from load-bearing source structure? | abstraction and cross-level reach | claim reduction, failure, stop, or non-capture |
| Type Integrity | Are source and origin types preserved without silent replacement? | typing and PROJECT_AS claims | failure or mandatory stop |
| Reference Continuity | Does the claim concern the same reference object? | cross-resolution and chain claims | new record, reduction, or failure |
| Functional Continuity | Does the asserted function depend on identified source structure? | source- and target-function claims | analogy_only, reduction, or failure |
| Contextual Boundedness | Is validity confined to declared conditions? | transfer and generalization | bounded claim or reduction |
| Counterfactual Sensitivity | Would relevant source change alter the claim? | constitutive and functional load claims | provisional, reduction, analogy, or failure |
| Calibration Limits | Are thresholds and distinctions discriminative? | strength and comparison claims | provisional, partial, reduction, or non-capture |
| Loss | What cannot be preserved or reconstructed? | completeness, reversibility, and continuity claims | bounded, provisional, partial, or non-capture |
| Anti-Immunization | Does a new claim preserve prior failure? | successor and rescue claims | mandatory stop or separate new record |
| Authority Ceiling | Does the claim exceed structural method authority? | normative, person, legal, political, and intervention claims | mandatory stop or prohibited claim |

### 16.2 Ceiling is record-specific

The same claim type can have different ceilings in different records because source quality, context, loss, and alternatives differ.

### 16.3 No compensation rule

Formal elegance, detail, citations, or model consistency cannot compensate for missing praxeological relevance, traceable load, Type Integrity, or source support.

---

## 17. Claim Reduction Relations

Claim reduction preserves the most extensive or demanding claim available on the declared local reduction axis that remains supportable and testable without disguising failure. A reduced claim must be stated and tested as a new or revised claim.

### 17.1 Object-formation reduction

```text
trajectory claim
→
path claim
→
sequence claim
```

### 17.2 Historical-determination reduction

```text
strong path-dependence claim
→
weak order-dependence claim
```

### 17.3 Functional reduction

```text
functional-projection claim
→
structural-analogy claim
```

```text
broad target-function claim
→
limited contextual-function claim
```

### 17.4 Component-role revision

Component-role revision is axis-specific rather than linear.

```text
functional-load claim
→ revise among constitutive / strongly modulating / weakly modulating / incidental / underdetermined
```

```text
substitutability claim
→ revise among replaceable / conditionally replaceable / non-replaceable
```

```text
compensation claim
→ revise among compensatory / non-compensatory / unresolved
```

A change on one axis does not automatically determine another.

### 17.5 Scope reduction

```text
category-wide claim
→
context-bound claim
→
reference-object-bound claim
```

This sequence is available only where the reduced claim remains substantively meaningful.

### 17.6 Resolution effect

```text
supported resolution test
+
no changed reconstruction
:
resolution-gain claim
→
resolution-neutral result
```

This is a claim effect after a valid test, not a universal reduction rank.

### 17.7 Reduction is not automatic admissibility

```text
claim_reduction_required
→ revise claim
→ test revised claim
→ assign new output class
```

A proposed reduction does not inherit the support or output class of the stronger failed claim.

---

## 18. Output-Class Handoff

The Output Class Index governs the exact ten classes. This table states only how claim architecture constrains their use.

| Claim situation | Canonical output interaction | Claim effect |
| --- | --- | --- |
| claim passes as declared within ordinary boundedness | `admissible` | retain the tested claim |
| materially narrower claim has already been tested and passes | `admissible_with_bounded_claim` | retain explicit narrowed reach |
| coherent claim remains usable while material support, calibration, or rival limits remain | `admissible_but_provisional` | retain with provisional status and open condition |
| valid resolution test changes no warranted reconstruction | `resolution_neutral` | withdraw resolution-gain claim; retain prior reconstruction |
| only declared resemblance is warranted | `analogy_only` | retain analogy; withdraw stronger projection or identity claim if made |
| separable claim components receive different results | `partially_admissible` | retain passing components and record non-passing components |
| current claim is too strong and a weaker claim must still be tested | `claim_reduction_required` | formulate and retest reduced claim |
| further continuation would violate a mandatory boundary | `mandatory_stop` | stop current operation; state re-entry condition |
| declared operation does not carry the claim | `failed_transformation` | record claim and operation failure without invalidating source object automatically |
| no adequate retained claim remains without distortion or false closure | `non_capture` | state limiting condition, uncaptured object, and possible rival or re-entry |

### 18.1 Critical distinctions

```text
bounded
≠
provisional
≠
partial
```

```text
claim_reduction_required
≠
already tested bounded claim
```

```text
failed transformation
≠
invalid source object
```

```text
non_capture
≠
missing information alone
```

### 18.2 Rival claims and output

Where competing reconstructions or projections remain:

- use `admissible_but_provisional` when one coherent candidate is presently supportable but a material rival remains unresolved;
- use `partially_admissible` when separable claims or components receive distinct results;
- use `non_capture` when no adequate retained claim remains without distortion;
- use `failed_transformation` when the declared operation itself fails its conditions.

No default priority applies. The selected class must name the primary governance result for the delimited claim.

---

## 19. Source and Calibration Burdens

Claim families carry different minimum burdens. A table entry does not prove that the burden is met.

| Claim family | Minimum source burden | Counterfactual or rival burden | Calibration requirement |
| --- | --- | --- | --- |
| typing claim | occurrence-level identifying evidence | changed features should be able to revise typing | criteria distinguish neighboring types |
| sequence claim | supported temporal ordering | alternative order considered where material | ordering uncertainty stated |
| path claim | transitions, alternatives, branch points | changed transition or alternative structure affects claim | path distinguished from chronology |
| trajectory claim | repetition, sedimentation, historical load | removed persistence or residue weakens claim | trajectory distinguished from path |
| path-dependence claim | order-sensitive later possibilities or costs | alternative path would materially alter result | weak versus strong dependence distinguished |
| composite claim | selected sources and formation rule | removed constitutive source changes composite | formation distinguished from aggregation |
| decomposition claim | finer source support and relations | component change affects source reconstruction | gain distinguished from drift |
| component-role claim | role-specific evidence | change/removal test for constitutive role | constitutive, modulating, replaceable distinguished |
| source-function claim | coarse function plus finer relation | component change alters or preserves function | effect separately recorded |
| target-function claim | Constitutive Source Trace | source change alters projected function | projection distinguished from analogy |
| analogy claim | declared structural resemblance | breaking point or disanalogy stated | not treated as semantic identity |
| continuity claim | traceable object/type/function relation | specified break condition | continuity type distinguished |
| non-capture claim | documented limit and failed adequate alternatives | rival or re-entry condition where available | not used as immunity |

### 19.1 Citation is not source load

```text
citation
≠
TraceableLoad
```

A source reference supports a claim only when the record identifies how the source bears the asserted object, relation, function, or limit.

### 19.2 Calibration cannot be inferred from notation

```text
formal precision
≠
calibration
```

Threshold, strength, and comparative claims require discriminative cases, rivals, or explicit uncertainty—not merely more exact symbols.

---

## 20. External-Warrant Claims

Some claims can be structurally represented by STRATA but cannot be established by STRATA alone.

| External-warrant claim | What STRATA may contribute | What additional authority is required | Blocked inheritance |
| --- | --- | --- | --- |
| empirical truth claim | structured hypothesis, source trace, and bounded reconstruction | domain evidence and appropriate empirical method | admissibility → truth |
| actual causal claim | counterfactual sensitivity and candidate mechanism structure | causal design, evidence, or domain method | sensitivity → causality |
| semantic adequacy claim | typed mapping and declared meaning relation | linguistic, interpretive, or domain validation | formal correspondence → semantics |
| predictive-validity claim | explicit variables, thresholds, and competing structures | out-of-sample or domain-appropriate validation | formal model → prediction |
| rival-superiority claim | structured comparison and limiting conditions | adequate comparative evidence and criteria | non-capture → rival superiority |
| normative-validity claim | clarified structural stakes and alternatives | independent normative argument and legitimate process | structure → moral authority |
| policy-effectiveness claim | bounded structural scenario and risks | policy evidence, governance, and accountability | projection → policy mandate |

### 20.1 External warrant is not prohibition

External-warrant claims are not necessarily forbidden. They must be marked as exceeding STRATA's self-sufficient authority and must not inherit validation from a successful structural transformation.

```text
structural reconstruction
≠
empirical proof
```

---

## 21. Prohibited Claim Registry

The following claims cannot be licensed under STRATA authority. Some may belong to other legitimate domains under their own methods and governance; STRATA cannot confer them through transformation structure.

| Prohibited claim category | Blocked inference | Why STRATA cannot license it | Nearest admissible formulation |
| --- | --- | --- | --- |
| person typing | operator occurrence or profile → person essence | STRATA classifies structures and records, not persons | describe bounded observed occurrence or role structure |
| clinical diagnosis | structural pattern → diagnosis | requires clinical authority, evidence, and safeguards | state non-diagnostic structural observation |
| mental-state inference | external structure → hidden internal state | not licensed by structural correspondence | state observed action or declared report only |
| moral ranking | structural difference → moral worth | no moral hierarchy follows from operator or output class | state bounded structural asymmetry or obligation |
| legal or political legitimacy judgment | formal relation → legitimacy | requires legal, political, and institutional authority | state relevant structural conditions without verdict |
| sanction entitlement | failed claim or asymmetry → punishment | methodological output is not enforcement authority | record failure and governance boundary |
| policy enforcement claim | projection → mandatory policy | PROJECT_AS does not authorize intervention | state a bounded analytical scenario |
| irreversible label | provisional pattern → permanent identity | revisability and non-capture must remain possible | use occurrence-bound, revisable wording |
| automatic intervention recommendation | admissibility result → required action | PraxisPurchase is not action prescription | state structural implication and external decision need |
| authority inheritance | successful transformation → new mandate | more structure does not create authority | retain original authority ceiling |
| new PMS primitive | derived object/function → operator | STRATA does not extend PMS Base | retain derived analytical status |
| ontology of real strata | analytical level → objective layer of reality | relative levels are analytical relations | state declared analytical level |
| final constituents claim | decomposition → ultimate parts | DECOMPOSE is provisional and reference-bound | state current finer reconstruction |
| universal scale claim | local reduction relations → one global rank | claim families are multidimensional | use local comparison only |
| full-capture guarantee | successful audit → complete representation | loss and Non-Capture remain possible | state captured and uncaptured structure |
| PMS superiority claim from translation success | mapping → model superiority | translation success does not compare total adequacy | state bounded formal correspondence |

### 21.1 Governance rule

```yaml
governance:
  authority_inheritance: prohibited
```

### 21.2 Mandatory stop on prohibited inflation

Where a transformation record begins to license a prohibited claim, current STRATA continuation receives `mandatory_stop`. A reduced claim may be formulated and tested in a new or explicitly revised record. An external-warrant question may be handed to an appropriate method without inheriting STRATA validation. Formal elegance or source quantity cannot compensate for the authority violation.

---

## 22. Operation Chains and Successor Claims

Operations chains require separate records and claim results.

### 22.1 Chain rule

```text
one operation occurrence
→ one operation-specific result
→ one canonical output class
```

A chain can contain multiple claims and classes. An integrated result may summarize the chain but cannot erase component results.

### 22.2 Required chain families

| Chain | Claim handoff | Preservation requirement |
| --- | --- | --- |
| COMPOSE → PROJECT_AS | composite-object claim becomes source for a separate target-function claim | COMPOSE does not pre-authorize projection |
| COMPOSE → DECOMPOSE | composite claim becomes source for finer reconstruction | decomposition does not restore original sources losslessly |
| DECOMPOSE → COMPOSE | finer reconstructed structures become selected sources for a new composite claim | new formation rule and loss required |
| DECOMPOSE → PROJECT_AS | finer source trace may support a separate target-function claim | source-function effect remains recorded |
| PROJECT_AS → DECOMPOSE | source object, concrete projected-function occurrence, or function-carrying composite may be opened | target function is not decomposed as an operator type |
| COMPOSE → PROJECT_AS → DECOMPOSE | composite, projection, and finer reconstruction each receive separate claims | later admissibility does not validate earlier failure |

### 22.3 Successor-claim requirements

A successor claim must state:

- its prior claim or source record;
- what changed: frame, granularity, level, operation, composition, or target function;
- which prior result remains preserved;
- its new source and claim ceiling;
- its own operation-specific result and output class.

### 22.4 Non-invertibility and claim preservation

```text
DECOMPOSE(COMPOSE(X))
≠
X
```

```text
COMPOSE(DECOMPOSE(X))
≠
X
```

```text
PROJECT_AS(X)
≠
X as a new origin type
```

These are claim constraints as well as operation constraints.

---

## 23. Formal Model Handoff

The later formal model may operationalize claim architecture but may not treat this reference table as a complete ontology or automatic decision procedure.

### 23.1 Permitted formal checks

The model may validate:

- presence of a declared claim type or controlled family;
- where the claim is a transformation claim, compatibility with COMPOSE, DECOMPOSE, or PROJECT_AS;
- declared scope and validity conditions;
- reference, origin-type, source-function, and target-function separation;
- required source, continuity, counterfactual, loss, and alternative fields;
- exact ten-class output vocabulary;
- preservation of prior and successor claim identifiers;
- explicitly declared prohibited categories, forbidden controlled values, authority-boundary declarations, and required stop branches;
- mapping consistency across declared fields and records.

### 23.2 Prohibited automatic decisions

Formal validation of declared categories is not semantic classification of free prose. The model may not infer that an undeclared statement constitutes person typing, diagnosis, moral ranking, or legitimacy judgment merely from its wording.

The model may not automatically decide:

- empirical truth or actual causality;
- semantic or normative validity;
- substantive source adequacy;
- which rival is best;
- whether a real person or institution has a type;
- diagnosis, sanction, legitimacy, policy mandate, or intervention;
- application authority;
- complete capture.

### 23.3 No new machine fields here

Terms such as claim domain, family, reach, role, support mode, support status, evidence availability, record-level status declaration, and claim disposition describe conceptual dimensions. Reference prose controls their semantic distinctions and permitted meanings. Formal Model v0 may mirror those meanings through machine field names, enum spellings, nesting, validation, and schema constraints; it may not create or close the semantics independently.

```text
conceptual dimension
≠
pre-authorized schema field
```

---

## 24. Definition-Site and Reference Map

| Claim architecture element | Designated primary definition site | Operation-specific application | Reference handoff |
| --- | --- | --- | --- |
| claim type | Chapter 7 — Shared Transformation Record | Chapters 15, 20, 30, and 53 | Glossary; this table |
| claim boundary | Chapter 0 | all chapters | Glossary; Claim Boundary Minified |
| claim ceiling | Chapter 5 | Chapters 15, 20, 30, 49, and 53 | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Evidence_Map.md` |
| support mode | Chapter 7 | Chapter 49 and operation records | `04_reference/Evidence_Map.md`; `04_reference/Glossary.md` |
| support status | Chapter 7 | Chapters 49 and 53 | `04_reference/Evidence_Map.md`; `04_reference/Glossary.md`; `04_reference/Output_Class_Index.md` |
| evidence availability | Chapter 49 | Chapter 7 and operation records | `04_reference/Evidence_Map.md`; `04_reference/Glossary.md` |
| authority ceiling | Chapter 0 | integrated use in Chapters 53 and 56 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `04_reference/Admissibility_Band_Reference.md`; `04_reference/Glossary.md` |
| record-level status declaration | Chapter 7 | all operation, chain, case, and integrated-audit records | `04_reference/Glossary.md`; `04_reference/Output_Class_Index.md`; `04_reference/Evidence_Map.md` |
| object and typing claims | [Chapter 1](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) | all three operations | Operator Index; Non-Equivalence Index |
| sequence, path, trajectory, path dependence | Chapter 3 and Chapters 9–14 | Chapter 15 and Chapter 17 | Transformation Operation Index |
| composite-formation claims | Chapter 4 | Chapter 15 | Transformation Operation Index |
| decomposition and component-role claims | Chapter 4 | Chapters 20–28 | Transformation Operation Index |
| source-function claims | Chapter 5 | Chapters 20–28 | Output Class Index for result separation |
| target-function and projection claims | Chapter 5 | Chapters 29–40 | Transformation Operation Index |
| analogy claims | Chapter 8 conceptual boundary; Chapter 37 elaboration | Chapters 37–40 | Non-Equivalence Index |
| continuity claims | Chapter 5 | Chapters 15, 20, 30, and 47 | Glossary |
| admissibility and output interaction | Chapter 6 | Chapters 17, 28, 40, and 53 | Output Class Index |
| record roles and successor claims | Chapter 7 | operation chains and Chapter 50 | Transformation Operation Index |
| canonical output architecture for stop and non-capture results | Chapter 6 | Chapters 51–53 | Output Class Index |
| stop concept and stop claims | Chapter 51 | Chapter 53 integrated application | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Evidence_Map.md` for source and stop evidence routing |
| Non-Capture concept and non-capture claims | Chapter 52 | Chapter 53 integrated application | Output Class Index; Non-Equivalence Index |
| general authority boundary | Chapter 0 | all Parts | Claim Boundary Minified |
| prohibited claim registry | Chapter 56 | Chapter 57 final closure | Claim Boundary Minified |

### 24.1 Reference division of labor

```text
Glossary
→ short definitions and spelling

Claim Type Table
→ claim-family, reach, ceiling, reduction, and authority architecture

Transformation Operation Index
→ operation identity and local result mappings

Output Class Index
→ exact canonical result classes and collision rules

Non-Equivalence Index
→ category-collapse controls

Admissibility Band Reference
→ full gate and boundary reference
```

No reference artifact replaces the designated chapter definition site.

---

## 25. Historical Pre-Block Claim Gate

Before Foundations drafting began, the following checks had to be executable and recordable. They remain a historical baseline; Chapter-0 claim and authority routes now resolve to the provisionally re-locked canonical prose.

### 25.1 Architecture gate

- [ ] Claim type is distinct from claim scope, ceiling, support status, record-level status declaration, role, local result, and output class.
- [ ] No closed universal claim enum has been invented.
- [ ] No universal rank or confidence score has been introduced.
- [ ] System claims and transformation claims remain separate.
- [ ] Warrant and governance claims are not treated as a fourth operation.

### 25.2 Operation gate

- [ ] Exactly `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS` are used.
- [ ] PATH claim vocabulary is complete without becoming system-wide rank.
- [ ] SUB claims concern occurrences and composites, never operator types.
- [ ] RETYPE claims preserve origin type and bounded target function.
- [ ] Analogy and functional projection remain distinct.
- [ ] Source-function effect remains separate from DECOMPOSE result.

### 25.3 Ceiling and support gate

- [ ] Claim reach is declared.
- [ ] Source Ceiling, Traceability Ceiling, and Claim Ceiling remain distinct.
- [ ] Support mode, support status, evidence availability, claim disposition, record-level status declaration, and output class remain separated.
- [ ] Counterfactual and rival burdens are stated where applicable.
- [ ] Loss limits completeness, reversibility, and transfer claims.
- [ ] Material generalization requires independent support.

### 25.4 Result and preservation gate

- [ ] Each operation occurrence has a local result and one canonical output class.
- [ ] Prior, revised, reduced, rival, withdrawn, failed, and successor claims remain distinguishable.
- [ ] A reduced claim is retested rather than automatically admitted.
- [ ] Later transformation does not erase earlier failure.
- [ ] Stop and Non-Capture remain positive possible results.

### 25.5 Authority gate

- [ ] No person typing or diagnosis is licensed.
- [ ] No moral ranking, legitimacy judgment, sanction, or automatic recommendation is licensed.
- [ ] No new PMS primitive or ontology of strata is created.
- [ ] External-warrant claims do not inherit proof from STRATA admissibility.
- [ ] `governance.authority_inheritance: prohibited` remains operative.

### 25.6 Completion result

Failure of a gate does not require rhetorical rescue. The correct result may be claim reduction, mandatory stop, failed transformation, or non-capture.

---

## 26. Revision and Freeze Policy

This table is provisionally complete for Reference Kernel v0 when:

1. all claim families required by Foundations, PATH, SUB, RETYPE, and LIMITS are represented;
2. every family has a designated primary definition or application site;
3. claim type, reach, ceiling, support mode, support status, evidence availability, record-level status declaration, claim disposition, record role, local result, and output class remain separated;
4. no entry creates a universal hierarchy, new primitive, fourth operation, or authority transfer;
5. operation-specific mappings remain synchronized with the Minified Kernel and Output Class Index;
6. Chapter Contracts contain no conflicting rival-result mappings;
7. Glossary and Non-Equivalence Index contain the central claim-type controls;
8. semantic distinctions are controlled in prose while machine field names, enum spellings, nesting, and schema constraints remain deferred to Formal Model v0;
9. cases can add domain-specific wording without silently expanding the canonical architecture;
10. later Blocks can define each concept once, apply it locally, and test it repeatedly without re-derivation.

Revision rule:

```text
new domain claim wording
→ map to an existing claim family
→ declare scope and ceiling
→ test non-equivalences

genuinely new structural assertion
→ remain non-canonical
→ require definition site, non-equivalences, operation or method relation, ceiling, output handoff, audit, and Reference Kernel revision
→ only then enter the controlled registry
```

Freeze remains provisional until the relevant Blocks, cases, conclusion, front matter, and appendices are complete. Final Reference Freeze occurs only after the prescribed production sequence.

---

**End of Claim Type Table v0.2.12**

---

## Chapter 2 WP1–WP3 Claim Handoff

Chapter 2 WP1–WP3 does not create a universal hierarchy of coordinate, scope, comparison, or declaration claims. It canonically establishes frame, granularity, relative-level, scope, comparability, plurality, and Minimal Level Declaration burdens while leaving integrated lock review to WP4:

| Claim family | Assertion burden | Minimum declared support | Prohibited inflation |
| --- | --- | --- | --- |
| frame declaration claim | this reconstruction is bounded by a stated relevance and inside/outside relation | reference object, source support, included/excluded relevance, claim reach | frame treated as natural or exhaustive |
| granularity declaration claim | this distinction density is used for the bounded reconstruction | declared distinctions, source accessibility, analytical purpose | fineness treated as truth or authority |
| relative-level claim | this object occupies a stated position in a declared relation | comparison objects, relation type, local direction, frame, claim | level treated as absolute rank or ontology |
| scope declaration claim | the reconstruction or claim is bounded in time, source access, and reach | temporal, source, and claim boundaries with gaps and exclusions | local scope silently generalized |
| granularity-comparability claim | two reconstructions can or cannot be compared for a specified claim | shared or translated reference, claim, frame, and distinction relation | mismatch treated as automatic agreement or disagreement |

The coordinate, scope, comparison, and minimal-declaration claim families now route to [`Chapter 2 WP1–WP3`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level). Integrated synchronization and lock are complete under Chapter 2 WP4. None is a closed machine enum, strength rank, or Output Class. A failed coordinate claim cannot be rescued by changing frame, granularity, or relative level without a new record and new testable claim.

### Chapter 2 WP2 scope-claim families

| Claim family | Minimum declaration burden | Prohibited promotion | Current owner |
| --- | --- | --- | --- |
| temporal-scope claim | included span, entry boundary, endpoint or open edge, relevant preconditions and later effects, uncertainty | open edge → completed historical or non-event claim | Chapter 2 WP2 |
| source-scope claim | source basis, directly supported distinctions, inference, gaps, uncertainty, speculative edge | missing material → positive structure or authority | Chapter 2 WP2 |
| bounded claim-scope claim | object, predicate, coordinates, temporal/contextual reach, generalization status, exclusions, re-entry | local occurrence → type, institution, person, causal, normative, or universal claim | Chapter 2 WP2 |

These families are prose-governed claim burdens, not new canonical Output Classes or machine enums. `claim_reduction_required`, `admissible_with_bounded_claim`, and `mandatory_stop` remain canonical result mappings owned by the Output Class architecture.

### Chapter 2 WP3 comparison-claim families

| Claim family | Minimum burden | Invalid inflation | Primary route |
| --- | --- | --- | --- |
| coordinate-change claim | reference continuity plus explicit changed and stable coordinates | coordinate movement → operation identity | Chapter 2 WP3 |
| granularity-relation claim | named comparison basis plus source-supported distinction sets and loss | finer → truer, deeper, or more authoritative | Chapter 2 WP3 |
| multiple-valid-granularity claim | local purchase, traceable load, bounded claim, disclosed loss, rival availability | plurality → universal equivalence or total integration | Chapter 2 WP3 |
| granularity-comparability claim | same or related object, translatable frame and predicate, declared scopes, cross-resolution trace | mismatch → contradiction or automatic neutrality | Chapter 2 WP3 |
| substantive-contradiction claim | incompatible answers to the same bounded predicate after comparability review | micro/macro wording → coexistence by default | Chapter 2 WP3 |
| minimal-declaration status claim | conceptual slots completed and mapped to existing record paths | complete declaration → support, validity, or operation proof | Chapter 2 WP3 and Chapter 7 |

---

## Chapter 2 Provisional-Lock Claim Architecture

Chapter 2 adds no new canonical Output Class. It fixes the coordinate and scope burden for claims already typed elsewhere.

| Claim family | Minimum Chapter 2 declaration | Typical reduction pressure |
| --- | --- | --- |
| frame-bounded reconstruction | analytical frame, reference object, relevance boundary, exclusions | frame label without bounded relevance |
| granularity claim | declared distinction set and comparison relation where changed | fineness asserted as truth or depth |
| relative-level claim | positioned object, comparator, relation, purpose | absolute “higher/lower” language |
| temporal-scope claim | included interval, relevant preconditions, open edges | later events or non-events inferred beyond the interval |
| source-scope claim | accessible materials, inference boundary, gaps, uncertainty | source access treated as source truth or completeness |
| claim-scope claim | claim object, predicate, reach, exclusions | local evidence generalized to institution, person, or universal pattern |
| coordinate-change claim | source and target coordinates plus what changed and remained stable | coordinate change treated as operation proof |
| resolution-comparison claim | comparable reference, predicate, scope, translation, and loss | `resolution_neutral` inferred from added detail alone |

A complete coordinate declaration does not raise the Claim Ceiling. A material coordinate change creates a new testable claim; it does not inherit an earlier result or erase a prior failed claim.

---

## Chapter 3 Canonical Temporal Claim Family

| Claim family | Minimum support burden | Typical ceiling or reduction |
| --- | --- | --- |
| configuration claim | bounded time/location, relevant relation set, frame/source/claim scope | no total state-of-world claim |
| event claim | realized relevant change, temporal placement, object boundary | no causal atom or transition claim automatically |
| non-event claim | supported expectation, bounded realization condition, non-realization, praxeological load | reduce to source gap if occurrence status is unknown |
| transition claim | identifiable configurations, order, intervening structure, changed praxis conditions, relation boundary | reduce to endpoint difference if connecting relation is unsupported |
| sequence claim | selected units and declared ordering basis | no path claim from order alone |
| path claim | actual traversal, constitutive relation, selection, source trace, alternatives/loss | reduce to sequence when traversal or relation is unsupported |
| trajectory claim | path plus sedimented historical load affecting later possibilities | reduce to path when sedimentation burden fails |
| path-dependence claim | present insufficiency without history plus order-sensitive counterfactual and trace | trajectory may remain while property claim is reduced/stopped |
| irreversibility claim | bounded restoration criterion, frame, claim, cost/condition comparison | no absolute metaphysical irreversibility |
| alternative-availability claim | historical or structural evidence that the alternative was available/relevant | reduce to imagined possibility or omit when unsupported |

A stronger temporal label never raises the Source or Claim Ceiling. Downward claim reduction preserves warranted lower-burden objects without treating the failed stronger claim as successful.



## Chapter 3 WP1 — Temporal Object Claim Types

| Claim type | Minimum assertion burden | Typical ceiling / reduction | Primary definition |
| --- | --- | --- | --- |
| configuration identification | bounded reference, temporal location, relevant relation set, praxis conditions, source and claim scope, disclosed selection | reduce to partial relation description where the configuration boundary or relation set is under-supported | [Chapter 3 WP1](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| state-adequacy claim | declared state variable, temporal location, source support, and proof that omitted relations do not alter the tested narrow claim | require configuration reconstruction where hidden relations, expectations, or action corridors matter | [Chapter 3 WP1](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| event identification | bounded occurrence, temporal placement, positive realization, frame relevance, source support | no automatic causal, transition, institutional, or normative extension | [Chapter 3 WP1](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| non-event identification | expected occurrence, warranted expectation relation, bounded realization condition, supported non-realization, praxeological load | missing records require uncertainty or `claim_reduction_required`; insistence without support requires `mandatory_stop` | [Chapter 3 WP1](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| transition identification | source and target configurations, supported temporal order, intervening realized/non-realized structure, changed praxis conditions, bounded relation | endpoint difference alone supports only a difference claim, not transition | [Chapter 3 WP1](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |

These claim types do not create operation identity, causal proof, path formation, trajectory, or path dependence. Their support and disposition remain separately auditable.

## Chapter 3 WP2 — Ordered Historical Claim Types

Canonical source: [`Chapter 3 Sections 3.6–3.8`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Claim type | Minimum support burden | Required reduction boundary |
| --- | --- | --- |
| sequence identification | declared units, ordering basis, supported order, bounded coordinates and scopes | reduce to partial order or chronology where internal order or analytical selection is under-supported |
| path identification | warranted sequence, bounded reference object, actual traversal, selection rule, constitutive connectedness, source trace, branch/omission/loss disclosure | reduce to sequence or chronology where traversal or connectedness is absent; insistence may require `mandatory_stop` |
| trajectory identification | warranted path, source-supported historical carry-over, traceable effect on later praxis conditions, bounded claim | reduce to path or localized persistence where sedimented later effect is not established |
| directionality claim | bounded supported patterned continuation pressure | reduce teleological, inevitable, or destiny language; refusal of reduction may require `mandatory_stop` |
| competing-trajectory claim | separately declared frames, selections, supports, losses, and rival relations | preserve co-validity or underdetermination; do not create an unrestricted master trajectory |

Local reduction remains:

```text
trajectory claim fails
→ path may remain

path claim fails
→ sequence may remain

sequence claim fails
→ chronology may remain
```

## Chapter 3 WP3 — Historical Property Claim Types

| Claim type | Minimum assertion burden | Typical ceiling / reduction | Primary definition |
| --- | --- | --- | --- |
| path-dependence property claim | bounded present/later relation, warranted path or trajectory, current-conditions insufficiency, prior-order/branch relevance, supported counterfactual sensitivity, traceable carry-over, uncertainty | reduce to trajectory or bounded historical relevance where the property burden fails | [Chapter 3 §3.9](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| sedimentation claim | identified historical contribution, accumulation/persistence relation, source-supported carrier, later praxis effect, bounded scope, loss/uncertainty | reduce to historical persistence or trajectory where later effect or carrier is weak | [Chapter 3 §3.10](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| bounded irreversibility claim | frame, claim, object relation, restoration criterion, source-supported residual difference/cost, uncertainty and re-entry | reduce to bounded residual-load statement; stop absolute or criterion-free claims | [Chapter 3 §3.11](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| unrealized-alternative claim | bounded branch point, identifiable alternative, source-supported availability, conditions, non-traversal, later relevance | reduce to provisional possibility or omit when availability is unsupported | [Chapter 3 §3.12](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |
| Minimal Temporal Object Chain claim | every stage's burden, relation, support, loss, and downgrade route | retain the strongest warranted lower-burden object | [Chapter 3 §3.13](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) |

These are claim families, not new Output Classes or closed machine enums.

---

## Chapter 3 Temporal Claim Handoff

Claims routed through [`Chapter 3`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) must state the strongest supported temporal object or property and preserve downward reduction. A failed path-dependence claim may retain a trajectory; a failed trajectory claim may retain a path; a failed path claim may retain a sequence; a failed sequence claim may retain chronology. New labels, frames, granularities, levels, or target functions do not erase a prior failed claim.

---

## Chapter 4 Preparation — Operation-Identity Claim Types

The Chapter 4 Preparation Gate assigns the following claim burdens without pre-empting canonical prose:

| Claim type | Minimum assertion burden | Required reduction / stop boundary |
| --- | --- | --- |
| `COMPOSE` occurrence claim | multiple or sequential typed source structures, ordering/selection rule, constitutive relation, new composite target identity, preservation and loss account | reduce to chronology, aggregation, summary, or unclassified relation where composite formation is unsupported |
| `DECOMPOSE` occurrence claim | provisionally compressed occurrence/composite, stable reference object, finer relational reconstruction, source trace, coarser-function status | reduce to description or added detail; stop if a competing object is substituted or operator type is targeted |
| `PROJECT_AS` occurrence claim | origin-typed source object, preserved source reference/type, declared target context, bounded source-dependent function, alternatives and validity scope | reduce to recontextualization or `analogy_only`; stop type replacement or unbounded function claims |
| operation-chain claim | separately identified occurrences, link order, each link’s source/target, local result, loss, and continuation relation | split collapsed multi-operation claims; a failed link retains no inherited validity |
| non-invertibility claim | named operation pair or projection relation plus selection, compression, reconstruction, context, or type-preservation reason | do not inflate to metaphysical irreversibility, total loss, or exemption from preservation |
| three-operation closure claim | candidate fourth movement tested against coordinate change, audit act, chain, local procedure, output, confusion, and non-capture | retain closure only within STRATA’s declared grammar; unresolved external pressure remains non-capture or Base-revision pressure |

```text
operation identity claim
≠ coordinate claim
≠ temporal-object claim
≠ admissibility claim
≠ application authority
```

Primary production-control route: `04_reference/Chapter_4_Preparation_Record.md`. Canonical operation-grammar ownership is now Chapter 4 Sections 4.1–4.10; integrated lock remains pending WP4.

---

## Chapter 4 WP1 — Canonical Operation-Identity Claims

Canonical Sections 4.1–4.4 now own the following bounded claims:

| Claim | Canonical burden | Local failure route |
| --- | --- | --- |
| three-operation closure | candidate movement is reduced to coordinate change, existing operation, local procedure, audit/output condition, or unresolved pressure | no hidden fourth operation; retain Stop, Non-Capture, or revision pressure |
| `COMPOSE` occurrence | typed multiple/sequential sources, selection, ordering where relevant, constitutive formation, new composite target, preservation and loss | `failed_transformation` where chronology or aggregation is mislabeled |
| `DECOMPOSE` occurrence | compressed occurrence/composite, same reference object, finer relational reconstruction, source trace, coarser-claim test | failure where a competing object replaces the source or an operator type is targeted |
| `PROJECT_AS` occurrence | origin-typed source, declared target context, bounded source-dependent function, origin-type preservation | `analogy_only`, claim reduction, failure, or Stop where function trace or type integrity fails |

Canonical route: [`Chapter 4 WP1–WP3`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as). Integrated synchronization and lock remain pending WP4.

---

## Chapter 4 WP2 — Canonical Direction and Chain Claims

| Claim family | Minimum declaration burden | Required reduction or stop |
| --- | --- | --- |
| transformation-direction claim | typed source, target relation, one operation kind, preservation and loss | reduce directional metaphor where signature is absent |
| operation/coordinate relation claim | operation identity plus separately declared frame, granularity, relative level, scopes, comparator, and purpose | reject level or coordinate movement as operation proof |
| chain-handoff claim | prior target availability, stable or revised identity, successor source role, handoff uncertainty | split or stop where textual succession replaces handoff |
| link-local validity claim | independent justification, source/target, preservation, loss, alternatives, and local Output Class | no validity inheritance from adjacent links |
| chain-integrated claim | ordered local results, retained failures, explicit summary relation | reject flattened verdicts that erase component results |
| later-link-failure claim | earlier local result retained within scope; later failure separately recorded | do not invalidate earlier result or rescue later claim by adjacency |

Canonical return: [`Chapter 4 §4.5–4.7`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

---

## Chapter 4 WP3 — Canonical Non-Invertibility and Declaration Claims

| Claim family | Minimum declaration burden | Reduction, Stop, or Non-Capture boundary |
| --- | --- | --- |
| non-invertibility claim | specified prior and later occurrences, selection/reconstruction/context difference, preservation and loss comparison | reject total-loss or metaphysical irreversibility inflation |
| reverse-looking operation claim | new occurrence identity, source, target, kind, loss, and local result | no automatic inverse or untouched restoration |
| operation-confusion claim | candidate signatures, source–target test, coordinate-only alternative, chain test | keep identity open where signature burden is unmet |
| collapsed-chain claim | separated links, explicit handoff, local results | `mandatory_stop` until separation |
| unresolved identity claim | rival `COMPOSE`/`DECOMPOSE` candidates, limiting condition, re-entry evidence | `non_capture`; neither strong claim protected |
| Minimal Operation Declaration completeness | all conceptual slots mapped to existing record families | completeness does not establish admissibility, truth, or authority |

Canonical return: [`Chapter 4 §4.8–4.10`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

---

## Chapter 4 Operation-Claim Handoff

Claims routed through [`Chapter 4`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) must declare one occurrence, one operation kind, a typed source relation, the appropriate target relation, preservation, loss, alternatives, uncertainty, and a local result. Chain claims retain link-local outputs. A later failed link does not erase an earlier bounded result, and an earlier result does not validate a later link.

---

## Chapter 5 Preparation — Continuity and Function Claim Types

The Chapter 5 Preparation Gate assigns the following claim burdens without pre-empting canonical prose:

| Claim type | Minimum assertion burden | Required reduction / stop boundary |
| --- | --- | --- |
| origin-type claim | identifiable source object, source reconstruction, declared analytical type, revision status | reject operator-type inflation, permanent essence, or retrospective replacement |
| target-function claim | target context, bounded relational function, source trace, validity scope, source-change sensitivity | reduce to analogy or contextual description where function burden is unmet |
| transformation-context claim | operation purpose, source/target relation, coordinates, relevant sources, temporal reach, validity and claim ceiling | reject frame-only or target-context-only substitution |
| reference-continuity claim | stable or explicitly derived referent, constitutive relations, temporal/reference boundary, source bridge | reduce or fail where only naming persists |
| type-integrity claim | visible source typing, separate target typing/function, explicit revision rather than replacement | Stop insisted origin-type replacement or primitive inflation |
| functional-continuity claim | specific load-bearing source features, target relation, material source-change effect, bounded scope | `analogy_only`, claim reduction, failure, or Non-Capture where source dependence is absent or unresolved |
| temporal-continuity claim | relevant historical order, duration/load, declared compression and loss | reject timeless-property and exhaustive-detail claims |
| contextual-boundedness claim | target context, temporal and relational limits, validity scope, exclusions, re-entry | require a new claim for later, parallel, wider, or unrelated contexts |

```text
continuity claim
≠ one binary status
≠ automatic admissibility
≠ truth proof
≠ authority
```

Primary production-control route: `04_reference/Chapter_5_Preparation_Record.md`. Canonical claim ownership remains future Chapter 5 prose; Chapter 47 later systematizes failure and audit relations.

---

## Chapter 5 WP1 Claim-Type Synchronization

| Claim | Required declaration | Current WP1 boundary |
| --- | --- | --- |
| origin-type claim | identified source object and warranted source-side analytical typing | does not prove permanence or full continuity |
| target-function claim | target context, purpose, validity scope, load-bearing source features, source-change sensitivity | does not prove authority or global validity |
| compatible multi-function claim | separate context, function, trace, scope, and local result for each occurrence | same source does not create universal functional elasticity |
| transformation-context claim | source–operation–target relation, relevant coordinates and sources, temporal reach, Claim Ceiling, uncertainty | context declaration does not prove admissibility |

Canonical return: [`Chapter 5 §§5.1–5.3`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP2 — Canonical Continuity Claims

| Claim family | Minimum burden | Local reduction or failure route |
| --- | --- | --- |
| reference-identity claim | bounded referent, source boundary, constitutive relation, source trace | narrow the referent or withhold identity where the bridge is absent |
| reference-continuity claim | operation-specific source–target reference relation, preserved or revised constitutive bridge, loss disclosure | nominal sameness may reduce or fail; substitution requires a new object claim |
| type-integrity claim | explicit source type, target-object type where applicable, separate target function, no hidden replacement | reject function-to-type collapse; Stop remains available if replacement is insisted upon |
| type-continuity claim | warranted preservation or explicit evidence-based revision, downstream effect disclosure | provisionality or claim reduction where a component typing remains unresolved |
| functional-continuity claim | precise function, target context, source features, source-change sensitivity, scope and alternatives | `analogy_only`, `claim_reduction_required`, or `failed_transformation` where source carriage fails |
| mixed-continuity claim | separate local result for each continuity dimension | no compensatory aggregate verdict |

Canonical return: [`Chapter 5 §§5.4–5.6`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP3 — Temporal, Contextual, and Projection-Form Claims

| Claim family | Minimum burden | Reduction, Stop, or Non-Capture route |
| --- | --- | --- |
| temporal-continuity claim | relevant order, duration or carry-over, source-to-target bridge, bounded target time, non-erasure | reduce timeless or exhaustive claims; Stop insisted permanent identity |
| contextual-boundedness claim | target context, purpose, validity scope, temporal reach, exclusions, revision conditions | new context requires new test; Stop authority inheritance |
| context-transfer claim | stable source identity, material context relation, source-feature relevance, revised scope and loss | no automatic transfer from similarity or prior admissibility |
| Minimal Projection Form completeness | existing source, operation, target, continuity, loss, alternatives, governance, and result families | completeness does not establish truth or admissibility |
| rival-function claim | identified source, rival bounded functions, limiting condition, discriminating re-entry evidence | `non_capture`; neither strong function protected |

Canonical return: [`Chapter 5 §§5.7–5.9`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

---

## Chapter 5 Integrated Continuity Claim Handoff

| Claim family | Required Chapter 5 burden | Failure or reduction route |
| --- | --- | --- |
| origin-type claim | source-side typing remains visible and separately revisable | reject retrospective function-to-type replacement |
| reference-continuity claim | referent and constitutive bridge remain traceable | new object claim, reduction, failure, or unresolved result |
| type-integrity claim | source type, target-object type, and function remain distinct | `failed_transformation` or `mandatory_stop` if replacement is insisted upon |
| functional-continuity claim | precise source-carried function responds to material source change | `analogy_only`, reduction, or failure |
| temporal-continuity claim | relevant order, load, and prior result history remain visible | bounded reduction or failure where history is erased |
| contextual-transfer claim | new context, purpose, scope, expiry, and trace receive a new test | `mandatory_stop` for inherited validity or authority |
| unresolved rival-function claim | rivals, limiting condition, and re-entry evidence remain explicit | `non_capture` without protecting either strong claim |

Canonical return: [`Chapter 5`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 6 Admissibility-Claim Preparation Handoff

Chapter 6 assesses a delimited transformation claim rather than assigning global admissibility to an object or concept.

| Claim axis | Chapter 6 question | Non-equivalence |
| --- | --- | --- |
| relevance claim | which warranted reconstruction changes? | added detail ≠ added finding |
| traceability claim | which source structures carry and constrain the result? | citation ≠ TraceableLoad |
| counterfactual-load claim | would a material declared source change alter the result? | sensitivity ≠ causality |
| integrity claim | are referent, origin type, and function kept distinct? | semantic attraction ≠ Type Integrity |
| boundedness claim | where, when, and for what purpose does the result apply? | contextual fit ≠ global validity |
| routing claim | which canonical class governs the delimited claim after full review? | local finding ≠ Output Class |

Claim Reduction requires an explicit weaker formulation and retest. A material bounded-claim result is not interchangeable with an unrevised overclaim. Mandatory Stop, Failure, and Non-Capture remain distinct claim dispositions.

Production control: [`Chapter 6 Preparation Record`](Chapter_6_Preparation_Record.md).

---

## Chapter 6 WP1 Lower-Bound Claim Synchronization

| Claim | Required WP1 declaration | Current boundary |
| --- | --- | --- |
| operating-range claim | operation occurrence, source object, context, delimited claim, and source basis | positive floor finding does not complete full admissibility |
| PraxisPurchase claim | proposed distinction, changed praxis dimension, prior and revised warranted reconstruction, source support | importance, usefulness, or actionability alone do not pass |
| resolution-gain claim | one or more warranted claims must change because of the added distinction | more detail alone does not strengthen the claim |
| resolution-neutral claim | supported valid comparison, same tested object, no changed warranted reconstruction, no hidden defect | not automatic from any no-gain result |
| lower-bound Stop claim | repeated or evasive continuation after no additional purchase | voluntary cessation is not a new Output Class; refusal may route to `mandatory_stop` |
| relevance-without-actionability claim | closed corridor, cost, exposure, commitment, or irreversibility changes the reconstruction | no recommendation or intervention authority follows |

Canonical return: [`Chapter 6 §§6.1–6.4`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP2 Source-Load Claim Handoff

| Claim | Required support | Local failure pressure | Canonical-routing boundary |
| --- | --- | --- | --- |
| Traceability Ceiling pass | reconstructible source-result dependency | citation or label without load | positive finding is not full admissibility |
| TraceableLoad | constitutive source objects, relations, temporality, loss, and source-change response | source-indifferent result | no compensation by usefulness or purchase |
| counterfactual sensitivity | bounded relevant source change and expected target response | arbitrary or causalized counterfactual | local finding is not causal proof or Output Class |
| source-limited dependency | named gap, rival possibilities, retained narrower claim, re-entry condition | hidden gap or invented Non-Event | provisionality or reduction requires explicit surviving claim |

Canonical return: [`Chapter 6 WP2`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP3 Integrated Claim and Routing Handoff

| Claim pattern | Required disposition | Boundary |
| --- | --- | --- |
| purchase, load, type, and boundedness all supported | positive route remains subject to all applicable surrounding checks | no universal or inherited validity |
| useful function with invalid type replacement | reject type claim; preserve and retest bounded function or analogy | semantic attraction cannot repair Type Integrity |
| cited source with exchanged referent | fail same-reference claim; declare a new object if warranted | citation does not preserve formation identity |
| stronger claim exceeds load but narrower form is testable | `claim_reduction_required` | reformulation and retest precede passage |
| separable claim segments receive different findings | `partially_admissible` may be available | no averaging or stacked class for one claim |
| continued derivation after a failed load-bearing gate | `mandatory_stop` | prior valid findings remain visible |
| rival mappings cannot be responsibly selected | `non_capture` | neither rival claim is protected |
| weighted score or fixed threshold substitutes for conjunction | `mandatory_stop` for the scale claim | local bounded comparison may remain descriptive |

Canonical return: [`Chapter 6 WP3`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 Provisional-Lock Claim Handoff

Chapter 6 requires claim segmentation before admissibility routing. A bounded local function, universal projection, type claim, reference claim, and authority claim may receive different findings and must not be averaged into one score.

```text
stronger claim fails
+ narrower claim remains testable
→ claim_reduction_required
→ reformulate
→ retest
```

A positive floor finding is not full admissibility, a `sensitive` counterfactual finding is not causal proof, and complete formal declaration is not substantive passage. Canonical routing remains limited to the ten Output Classes.

Canonical return: [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 7 Preparation — Record, Status, and Relation Claims

Chapter 7 will control the record-level declaration architecture without replacing substantive claim typing.

| Record claim or axis | What it declares | What it does not establish |
| --- | --- | --- |
| transformation-record claim | that a delimited transformation claim has been recorded under the shared envelope | truth or admissibility |
| declaration-completeness claim | that every applicable common duty is explicitly represented | epistemic completeness |
| source-basis claim | which source items bear on which claim components | proof or causal sufficiency |
| operation-occurrence claim | one occurrence identity and exactly one operation kind | warrant for the operation |
| chain claim | ordered relation among occurrence records and a distinct integrated claim | inherited passage from local results |
| support status | current support relation | canonical Output Class |
| resolution-test result | gain, neutrality, drift, escape, or non-applicability | claim disposition |
| claim disposition | maintained, withdrawn, failed, or superseded without erasure | operation result class |
| capture statement | claim-relative capture and limit declaration | automatic Non-Capture |
| routing-state claim | routed or formal-diagnostic process state | substantive validity |
| extension claim | bounded local declaration beyond the common envelope | permission to bypass shared duties |

A successor, reduced, split, rival, or chain-level claim remains a new delimited claim with its own record relation. Prior failure, loss, Stop, and Non-Capture are not erased.

---

## Chapter 7 WP1 Claim Architecture

Chapter 7 WP1 makes the following claim units recordable without redefining their upstream semantics:

| Claim unit | Required declaration | Failure pressure |
| --- | --- | --- |
| tested transformation claim | bounded statement, scope, validity, and authority boundary | undelimited or overwritten claim history |
| source reference claim | identified source referent and source scope | nominal continuity without referent continuity |
| source typing claim | analytical type under which the source enters | hidden retyping or operator substitution |
| source-load claim | constitutive features and relations carrying the result | generic source listing |
| operation-identity claim | one occurrence and one kind | collapsed chain or compound kind |
| operation-justification claim | source–target signature rationale | self-warranting explanation |
| expected-difference claim | proposed changed reconstruction | expectation treated as finding |
| target-object claim | object produced or reconstructed | object/function collapse |
| target-function claim | bounded contextual role with occurrence origin | timeless or universalized function |

Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 7 WP2 Recorded Claim Families

| Recorded claim family | Required declaration | Prohibited shortcut | Canonical return |
| --- | --- | --- | --- |
| admissibility finding | governing rule, delimited claim, source basis, local finding, limitation, routing basis | field completion → passage | [Chapter 7 §7.5](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record) |
| loss classification | affected item or relation, one of five categories, reason, relevance, source/occurrence pointer where available | empty array → no loss proved | Chapter 7 §7.6 |
| rival transformation | separate operation, source–target relation, target claim, loss profile, and record identity | rivals forced into one occurrence | Chapter 7 §7.7 |
| no-transformation claim | reason the source should remain untransformed for the tested purpose | no transformation → fourth operation | Chapter 7 §7.7 |
| non-translation claim | reason the proposed movement is not responsibly representable as a STRATA operation | named alternative → rival operation automatically | Chapter 7 §7.7 |
| governance limit | Claim Ceiling, Authority Ceiling, Stop/Non-Capture pointers, prohibited inferences, external warrant | schema validity → authority | Chapter 7 §7.8 |

These are recordable claim units, not closed machine enums or automatic Output Classes.

---

## Chapter 7 WP3 Status and Integrated-Use Claim Families

| Claim family | Required declaration | Permitted disposition | Boundary |
| --- | --- | --- | --- |
| support claim | source-relative support status and evidence availability | maintained, revised, contested, or failed | support ≠ route |
| resolution claim | applicable resolution-test result and compared object | maintained, neutral, drifted, or escaped | test finding ≠ Output Class |
| capture claim | claim-relative statement, captured structure, limit, and re-entry | maintained, reduced, or non-captured | limit ≠ automatic `non_capture` |
| chain claim | ordered occurrence references, handoffs, and preserved local findings | maintained, reduced, failed, or stopped | chain claim ≠ occurrence claim |
| extension claim | owner, control source, purpose, bounded payload, non-replacement assertion | admitted, reduced, or stopped | extension ≠ authority or primitive |
| routing claim | one selected canonical class for one delimited claim | routed or formal-diagnostic state | formal diagnostic has no Output Class |

---

## Chapter 7 WP4 Provisional-Lock Synchronization

Chapter 7 is provisionally locked after integrated ownership, redundancy, status, case-duty, prose-to-schema, link, schema, fingerprint, package, and roundtrip audit. The Shared Transformation Record records transformation claims without becoming the transformation, a truth proof, or an authority source. The existing record schema supplies lower-authority structural carriers; its Chapter-7 handoff annotation does not redefine canonical prose. The sixteen Chapter-7 case identifiers remain later production duties rather than completed evidence. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 8 Preparation Claim-Control Handoff

| Claim form | Permitted use | Prohibited inflation |
| --- | --- | --- |
| non-equivalence claim | deny unmarked identity, category collapse, or authority transfer | treat the pair as an empirical counterclaim |
| relational claim across a pair | declare comparison, analogy, operation, property test, or contextual function | inherit the other term’s type, scope, success, or authority |
| bounded-superiority claim | state that one reconstruction performs better for a declared claim | convert local performance into higher truth |
| analogy claim | retain useful resemblance, including `analogy_only` | treat resemblance as valid `PROJECT_AS` automatically |
| category-collapse finding | identify a violated distinction | select a canonical Output Class without full routing |
| authority-transfer finding | identify illegitimate truth or entitlement inheritance | infer that formal or technical work has no analytic value |

Production control: [`Chapter 8 Preparation Record`](Chapter_8_Preparation_Record.md). These claim forms do not add Output Classes or replace Chapter 6 and Chapter 7 routing.

---

## Chapter 8 WP1 Claim-Control Synchronization

| Claim pattern | Permitted bounded form | Prohibited inflation |
| --- | --- | --- |
| granularity comparison | finer reconstruction performs better for a declared claim under named sources and scope | finer means truer or more authoritative as such |
| relative-level claim | object is relatively wider, narrower, or otherwise located under a declared frame, reference set, and axis | relative position becomes ontological layer or explanatory rank |
| composition claim | a new composite is formed under declared selection, ordering, formation, preservation, and loss | composite equals complete lossless sum |
| decomposition claim | the same reference object is reconstructed at a finer, revisable resolution | selected components become final constituents or deeper essence |

A non-equivalence breach is a claim-control finding, not a canonical Output Class. Routing remains claim-relative under Chapters 6 and 7.

---

## Chapter 8 WP2 Claim-Control Synchronization

| Claim pattern | Permitted bounded form | Prohibited inflation |
| --- | --- | --- |
| sequence-to-path claim | supported sequence supplies selected inputs to a separately warranted path formation | temporal order is already actual traversal and constitutive path identity |
| path-to-trajectory claim | a source-traceable path may develop trajectory form through sedimentation and altered continuation possibilities | every realized or long path is a trajectory |
| trajectory property claim | a trajectory is separately tested for bounded path-dependence properties | trajectory existence proves inevitability or complete historical determination |
| projection claim | origin type is preserved while a source-sensitive target function is declared separately | target function replaces origin type |
| operator-like function claim | derived contextual function remains bounded and non-primitive | projection creates or becomes a PMS operator |
| weighting claim | relative load among existing occurrences is declared under named dimensions and scope | dominance deletes dependencies, replaces grammar, or creates a person type |

Each stronger relation is a new claim. Valid weaker claims do not compensate for failed stronger claims, and failed stronger claims do not erase valid weaker results.

---

## Chapter 8 WP3 Claim-Control Synchronization

| Claim pattern | Permitted bounded form | Prohibited inflation |
| --- | --- | --- |
| structural analogy | declared dimensions of resemblance and disanalogy, bounded scope, and `analogy_only` where projection burdens are unmet | resemblance treated as semantic preservation, origin-type identity, or automatic `PROJECT_AS` passage |
| recursive transformation | a new occurrence-level claim with separate source, target, admissibility, loss, alternatives, governance, and local result | repeated operations treated as complete capture, cumulative certainty, or inherited warrant |
| legibility claim | improved inspectability, reproducibility, or field-level validation for a declared purpose | formal precision, schema validity, or package success treated as empirical truth or authority |
| catalogue-breach claim | pair-specific category-collapse finding followed by claim segmentation and normal routing | one global failure label or automatic Output Class for every breach |
| re-entry claim | new evidence or a newly delimited question addressing the recorded limiting condition | vocabulary, frame, level, composite, or target-label change treated as erasure of the prior failed claim |

WP3 preserves the canonical distinction between local audit findings and routed Output Classes.

---

## Chapter 8 WP4 Claim and Routing Lock

A Chapter-8 non-equivalence finding is a claim-control input, not a claim disposition or canonical Output Class. The audit must delimit the tested identity or authority transfer, preserve any weaker relation, and then apply the ordinary continuity, admissibility, loss, alternatives, governance, and routing burdens.

```text
non-equivalence breach
≠ failed claim automatically
≠ failed transformation automatically
≠ mandatory stop automatically
```

All eighteen `C8-*` identifiers remain assigned later case duties. Foundations is provisionally complete; Chapter 9 may consume these claim controls but may not redefine them.

---

## Chapter 9 Preparation — Temporal and Transition Claim Architecture

| Claim type | Minimum declared burden | Characteristic overclaim | Weaker claim to preserve |
| --- | --- | --- | --- |
| temporal-position claim | reference, frame, temporal relation, precision/uncertainty, source basis | timestamp treated as self-interpreting position | bounded before/after or disputed-position claim |
| order-dependence claim | supported order, tested praxis difference, counterfactual order sensitivity | succession or narrative order treated as causal/path dependence | chronology or sequence-order claim |
| duration-relevance claim | interval, frame, affected praxis dimension, source trace | longer duration treated as greater truth or sedimentation | metric-duration statement |
| delay-as-transition claim | deferred relation between configurations and changed cost/expectation/alternative | elapsed time treated as intentional obstruction | bounded temporal spacing claim |
| delay-as-non-event claim | expected occurrence, warranted expectation, realization condition, non-realization, praxis load | silence or missing information treated as `Λ` | delay-as-structure or unresolved interval |
| persistence claim | retained structure across a supported interval and changing context | unchanged snapshot treated as persistence or sedimentation | repeated observation or bounded continuity claim |
| bounded-irreversibility claim | restoration criterion, residual difference/cost, frame, scope, ceiling | metaphysical permanence | bounded non-restoration claim |
| temporal-recontextualization claim | later frame/event, changed legibility, preserved earlier trace | retroactive erasure or automatic `Φ`/`PROJECT_AS` identity | changed-reading claim |
| transition claim | two configurations, warranted temporal relation, change object, source trace, frame, changed praxis conditions, residue | before/after pair or causal story | configuration comparison, chronology, Formal Diagnostic, or rival transition candidates |

```text
transition claim
≠ path claim
≠ causal claim
≠ operation claim
```

Prepared case duties `C9-SCOPE-01` through `C9-NC-01` remain non-evidence production assignments. Canonical drafting is pending. Production control: [`Chapter 9 Preparation Record`](Chapter_9_Preparation_Record.md).

---

## Chapter 9 WP1 — Executed Temporal Claim Controls

| Claim | Canonical WP1 burden | Local route pressure |
| --- | --- | --- |
| PATH-scope claim | temporal reconstruction only; no operation or target-function implication | segment function claims to RETYPE |
| `Θ`-supported claim | declared temporal contribution plus object- and claim-specific burden | reduce automatic trajectory or path-dependence upgrade |
| temporal-position claim | object, position form, relation/interval, frame, scope, precision, source, uncertainty, dependency | bounded position may survive disputed exact date |
| order-dependence claim | ordered elements, supported basis, tested claim, praxis dimension, counterfactual reorder, reconstruction change, ceiling | causal or path-dependence inflation prohibited |
| source-/document-order claim | exact source or record ordering relation | may not substitute for historical order |

```text
bounded relative order
≠ fabricated exact date

order-sensitive claim
≠ causal claim
```

Canonical control: [`Chapter 9 §§9.1–9.4`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

---

## Chapter 9 WP2 — Executed Temporal Claim Controls

| Claim | Canonical burden | Boundary |
| --- | --- | --- |
| duration claim | bounded interval, reference relation, source continuity, praxis difference, uncertainty, ceiling | metric duration ≠ relevant duration |
| delay-structure claim | deferred relation plus changed costs, bindings, alternatives, asymmetry, or later meaning | delay ≠ non-event automatically |
| framed-non-event delay | expected occurrence, warranted expectation, bounded condition, non-realization, load | elapsed time or silence insufficient |
| persistence claim | declared continuity criterion across changing events/configurations | persistence ≠ stasis or sedimentation |
| bounded irreversibility | before/after relation, restoration criterion, residual difference/cost, ceiling | formal reversal ≠ full restoration |
| temporal-recontextualization claim | later event/frame changes earlier legibility while trace remains | historical relation ≠ `Φ` ≠ `PROJECT_AS` |

Canonical control: [`Chapter 9 §§9.5–9.9`](../01_blocks/02_part_i_path.md#9-5-duration).

---

## Chapter 9 WP3 — Transition Claim Types

| Claim type | Minimum burden | Not established automatically |
| --- | --- | --- |
| transition candidate | delimited endpoints, comparison basis, temporal relation, declared gaps | warranted transition |
| warranted transition | applicable preconditions, continuity, trace, admissibility, loss, routing | path, trajectory, causality |
| frame-handoff claim | source/target frames, invariant relation, loss, bounded scope | frame identity |
| transition-failure claim | delimited failed relation plus preserved weaker findings | absence of temporal information |
| transition non-capture | rival source-responsible constitutive relations and re-entry condition | truth of either rival |
| warranted-transition-set handoff | individually routed local records | composed path |


## Chapter 9 Provisional-Lock Claim Boundary

| Claim | Required burden | Stronger claim not inherited |
| --- | --- | --- |
| warranted transition | delimited configurations, comparison basis, temporal and constitutive relation, frame, trace, loss, local routing | path, trajectory, causality, intention, authority |
| failed transition | explicit failed relation plus preserved endpoints and weaker temporal findings | absence of temporal information |
| Chapter 10 handoff | individually delimited transition records and unresolved limits | Path identity or `COMPOSE` passage |
| Chapter 9 lock claim | contract, case-duty, reference, model, schema, link, and package audit | empirical transition truth or scientific validation |

```text
warranted transition set
≠ path automatically

chapter lock
≠ claim truth proof
```

Canonical control: [`Chapter 9`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

---

## Chapter 10 Preparation — Path Claim Families

| Claim family | Required declaration | Invalid inflation | Weaker retained form |
| --- | --- | --- | --- |
| path claim | bounded reference object, traversed configurations/transitions, selection rule, constitutive relation, frame, evidence, loss, residue | chronology, plausible route, endpoint identity, or narrative coherence treated as path | chronology, sequence, transition set, or path candidate |
| path-selection claim | relevance criterion, inclusion, compression, exclusion, uncertainty, alternatives | cherry-picking or endpoint-driven inevitability | bounded component set or rival selection |
| path-frame claim | start/end or open edge, roles, institutions, environments, scopes, periodization rationale | objective universal path boundary | bounded/provisional frame |
| realized-path claim | supported traversal to endpoint or open continuation | necessity, rationality, intention, or closure | traversed segment |
| blocked-continuation claim | prior availability/preparation plus blocking condition | imagined alternative labeled blocked | bounded unrealized alternative note |
| aborted-path claim | initiation/authorization/partial traversal plus cessation and residue | never-started route labeled aborted | blocked or non-selected alternative |
| deferred-continuation claim | continued availability plus postponement and temporal load | missing information or permanent non-realization labeled deferred | delay or unresolved continuation |
| path-comparison claim | comparable frame, scope, selection, evidence, alternatives, and praxis dimensions | endpoint comparison or universal path score | partial comparison or formal diagnostic |
| path-without-strong-dependence claim | warranted path plus weak additional historical constraint | path treated as strong dependence automatically | path retained; dependence claim refused |
| minimal-record claim | path fields mapped into Shared Record with lineage, loss, alternatives, governance, and routing | complete record treated as path proof | formal diagnostic or reduced record claim |

```text
path claim
≠ trajectory claim
≠ path-dependence claim
≠ causal claim
≠ operation claim
```

Prepared cases `C10-DEF-01` through `C10-NC-01` are production obligations, not evidence. Production control: [`Chapter 10 Preparation Record`](Chapter_10_Preparation_Record.md).

---

## Chapter 10 WP1 — Executed Path Claim Controls

| Claim | Required WP1 support | Ceiling / reduction route |
| --- | --- | --- |
| path candidate | bounded reference, selected configurations/transitions, traversal claim, frame, selection, evidence, loss | candidate ≠ warranted path |
| warranted path | candidate plus conjunctive source, continuity, admissibility, loss, alternative, governance, and routing support | no trajectory, dependence, causality, or function inheritance |
| chronology claim | supported temporal ordering | chronology may remain below path threshold |
| component-role claim | source-supported role in the bounded path claim | inclusion ≠ constitutive role automatically |
| path-selection claim | explicit inclusion, compression, exclusion, alternatives, uncertainty, and lineage | retrospective coherence ≠ inevitability |
| path-frame claim | reference, periodization, scope, level, granularity, environments, and comparison basis | frame declaration ≠ historical continuity |
| indirect traversal claim | explicit inferential bridge and load-bearing gap assessment | direct-observation wording prohibited |

Canonical route: [`Chapter 10 §§10.1–10.6`](../01_blocks/02_part_i_path.md#chapter-10-path). The [`Preparation Record`](Chapter_10_Preparation_Record.md) remains production history.

---

## Chapter 10 WP2 — Qualified Path-Status Claim Controls

| Claim | Required WP2 support | Ceiling / reduction route |
| --- | --- | --- |
| realized-path claim | warranted traversal through the declared segment and temporal cut | no necessity, intention, success, closure, trajectory, or dependence inheritance |
| open-endpoint claim | explicit analytical cut, source ceiling, or unresolved continuation | open endpoint ≠ historical completion |
| blocked-continuation claim | prior availability/preparation, identifiable blocking condition, prevention relation, and resulting load | imagined possibility or mere non-selection requires blocked-status refusal |
| aborted-path claim | initiation/authorization/partial traversal, cessation point or interval, and residue | never-started route cannot be labeled aborted |
| deferred-continuation claim | specific continuation, postponement, continued bounded availability/commitment, and delay load | silence, permanent non-realization, or uninterrupted identity cannot be inferred |
| status-lineage claim | temporal cut, prior status, later status, and continuity/identity re-test | later realization does not erase earlier block, abortion, or deferral |

Canonical route: [`Chapter 10 §§10.7–10.10`](../01_blocks/02_part_i_path.md#10-7-realized-path). Status claims remain claim types or local findings, not canonical Output Classes.

