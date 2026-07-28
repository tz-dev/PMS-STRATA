# PMS-STRATA — Claim Type Table

**Status:** active Reference Kernel artifact; corpus-audit synchronized 
**Repository role:** claim-family, reach, ceiling, reduction, and authority routing; not an independent theory or authority source 
**Authority basis:** `PMS.yaml` → `00_source/PMS-STRATA_Structure.md` → `01_blocks/*` → `05_minified/*`; formal, case, appendix, and Reader artifacts remain subordinate to their canonical owners 
**Reference Freeze duty:** open bounded duty; this artifact may be corrected for ownership, routing, duplication, and carrier consistency without broadening any claim 

---

## 1. Role, Status, and Authority

This file is the active Reference registry for claim architecture in PMS-STRATA.

It distinguishes what a claim asserts from where it applies, how strongly it is supported, what ceiling constrains it, what operation produced or tested it, and which canonical output class governs its result.

It is a reference and audit artifact. It does not replace canonical prose, the Shared Transformation Record, the Output Class Index, the Admissibility Band, operation-specific procedures, case judgment, or the Formal Model.

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
- provide a bounded handoff to the Formal Model.

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

The table is open to domain-specific wording but closed against unmarked category creation. Local wording must map to an existing claim family. A genuinely new structural assertion remains non-canonical subject to explicit Reference Kernel revision and cannot be treated as a canonical claim type before that revision.

```text
open domain vocabulary
≠
unbounded claim architecture
```

```text
new local wording
→ map to an existing family

new structural assertion
→ non-canonical unless an explicit Reference Kernel revision establishes it
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
| Designated primary site | [Chapter 1](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure). |
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

The controlled semantic inventory is:

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

The Formal Model may operationalize claim architecture but may not treat this reference table as a complete ontology or automatic decision procedure.

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
