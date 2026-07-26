# PMS-STRATA — Claim Type Table

**Status:** Pre-LIMITS Maintenance WP5-synchronized; maintenance gate passed; Reference Freeze not performed  
**Historical local version marker:** Reference Kernel v0.2.44 — Chapter-20-WP3-synchronized claim architecture  
**Repository role:** `04_reference` registry, ceiling, reduction, and audit handoff; not an independent theory source  
**Authority basis:** `PMS.yaml`, `00_source/PMS-STRATA_Structure.md`, `05_minified/*`, the provisionally locked canonical Foundations Chapters 0–8 in `01_blocks/01_foundations.md`, the provisionally controlled Reference Kernel, and `04_reference/Chapter_1_Preparation_Record.md` through `04_reference/Chapter_8_Preparation_Record.md` as non-theory production controls

---

**Current synchronization:** Foundations Chapters 0–8, PATH Chapters 9–17, and SUB Chapters 18–28 are provisionally locked; RETYPE Chapters 29–40 hold a bounded provisional method lock; 29 PATH/SUB case packages are present and indexed; Chapter 41 Preparation and Pre-LIMITS Maintenance WP0–WP5 are complete while canonical Chapter 41 prose remains unstarted; Chapter 41 WP1 is the next controlled production step; the artifact-complete RETYPE lock remains `mandatory_stop`, and Part IV final lock remains unavailable.  
**Historical-layering rule:** Later `pending`, `next controlled step`, availability, or WP-stage statements preserve the local production state at the time of entry unless explicitly marked as current. They do not override this header and remain non-normative provenance until Reference Freeze.  

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

---

## Chapter 10 WP3 Claim Families

| Claim family | Minimum burden | Ceiling / prohibited upgrade |
| --- | --- | --- |
| path comparison | aligned reference, frame, time, granularity, selection, sources, dimensions, and uncertainty | no universal ranking, score, or authority |
| incomparability | identified failed alignment and preserved local findings | no claim that paths have no possible relation |
| endpoint similarity | explicit similarity dimension and retained path differences | no same-path or equivalent-load inference |
| path without strong dependence | warranted path plus weak or absent additional historical constraint | no history erasure and no covert dependence claim |
| minimal path record | path-specific fields within Shared Record plus lineage and claim scope | record completeness ≠ admissibility |
| path Stop | failed load-bearing path plus attempted stronger derivation | preserve weaker findings and re-entry condition |
| path Non-Capture | multiple source-responsible rival paths and no responsible adjudication | no merger, validation, or protective ambiguity |

Canonical route: [`Chapter 10 §§10.11–10.14`](../01_blocks/02_part_i_path.md#10-11-path-comparison).


## Chapter 10 Provisional-Lock Claim Controls

| Claim family | Required Chapter 10 load | Forbidden automatic upgrade |
| --- | --- | --- |
| Path claim | actual traversal, selection, constitutive connection, frame, evidence, loss, alternatives, residue | Trajectory, dependence, causality, function, authority |
| qualified status claim | segment/continuation, reference, temporal cut, availability/initiation/prevention/postponement relation, evidence ceiling | global status essence, motive, responsibility |
| comparison claim | aligned or translated reference, frame, scope, granularity, selection, source and dimensions | ranking, superiority, universal score |
| endpoint claim | declared equivalence dimension and residual differences | Path identity or equivalent historical load |
| non-dependence claim | warranted Path plus bounded absence/weakness of additional historical constraint | no history or no residue |
| record claim | structurally complete Shared-Record view | historical truth or substantive admissibility |

Canonical return: [`Chapter 10 completion boundary`](../01_blocks/02_part_i_path.md#chapter-10-completion-boundary).

---

## Chapter 11 Preparation — Trajectory Claim Families

| Claim family | Minimum declaration | Stronger claim not inherited |
| --- | --- | --- |
| trajectory candidate | warranted Path, sedimentation, residue, changed praxis, historical load, directionality, boundary | warranted Trajectory |
| warranted trajectory | candidate plus applicable Continuity, Admissibility, Loss, Governance, Stop, and Capture tests | Path Dependence |
| attractor sedimentation | bounded `Α` occurrence relation plus temporal stabilization and changed continuation access | attractor-function |
| asymmetry accumulation | bounded `Ω` occurrence relation plus repeated distributional load and present effect | inevitability or legitimacy |
| binding accumulation | bounded `Ψ` occurrence relation plus persistent commitment/breach cost | moral obligation or person state |
| residual accumulation | bounded `Λ` occurrences plus expectation-bound residue and present effect | every absence as Non-Event |
| competing construction | shared material, divergent boundary/selection/profile, separate claims | automatic equivalence or fusion |
| False Trajectory | insufficient sedimentation/load despite chronology, duration, repetition, or coherence | no history or no valid Path material |

Production control: [`Chapter 11 Preparation Record`](Chapter_11_Preparation_Record.md).

## Chapter 11 WP1 — Trajectory Claim Types

| Claim type | Minimum assertion burden | Required ceiling / reduction |
| --- | --- | --- |
| Trajectory candidate | warranted Path, present cut, carrier relation, cumulative/sedimented contribution, persistent residue or present effect, source trace, counterpressure, bounded directionality where claimed | candidate is not yet warranted; later Chapter-11 tests remain open |
| warranted Trajectory | candidate plus applicable continuity, admissibility, loss, governance, boundary, competition, Stop, and Non-Capture duties | no automatic Path Dependence, causal necessity, target function, or authority |
| Historical Sedimentation claim | identified carrier, cumulative or persistent transformation, present praxis effect, source-result sensitivity, repair/reversal pressure, claim ceiling | reduce to duration, recurrence, persistence, local residue, or bounded historical relevance if the full burden fails |
| historical co-determination claim | source-supported contribution of earlier Path structure to the present, with current conditions and rival allocation visible | no exclusive causation or current-condition erasure |
| non-teleological directionality claim | dimension-specific orientation, alternatives, contingencies, reversals, repairs, endpoint-bias test, probability/necessity separation | reduce teleological, progress/decline, destiny, original-plan, or determined-future language |
| teleological Trajectory claim | endpoint-selected history, erased alternatives, inferred destiny or original plan | `claim_reduction_required` or `failed_transformation`; stronger continued derivation may require `mandatory_stop` |

Canonical route: [`Chapter 11 §§11.1–11.4`](../01_blocks/02_part_i_path.md#11-trajectory).

## Chapter 11 WP2 — Profile and Corridor Claim Types

| Claim type | Minimum assertion burden | Required ceiling / reduction |
| --- | --- | --- |
| Attractor Sedimentation claim | bounded `Α` occurrence, temporal carrier, repeated or translated configurations, changed friction/default accessibility, alternatives, repair/erosion, current-condition allocation | no necessity, legitimacy, current dominance, attractor-function, or automatic Path Dependence |
| Asymmetry Accumulation claim | bounded `Ω` occurrence, declared distribution dimensions, temporal carrier, repeated/cumulative load, present differential effect, exit conditions, repair/redistribution | no moral rank, legitimacy, person type, impossible-exit, or exclusive historical causation |
| Binding Accumulation claim | bounded `Ψ` occurrences, carrier, layered or transformed commitments, reliance/coordination investment, present breach or reopening effect, weakening/transfer/conflict/release | no inner-state, consent, moral-duty, enforceability, or mandatory-continuation inference |
| Residual Accumulation claim | warranted expectation frames and windows, `Λ` occurrences, residual carrier, layering/extension/translation, present effect, repair/closure/dormancy, uncertainty | no conversion of absence, silence, or missing information into Non-Event; no permanence claim |
| Changed Action Corridor claim | declared corridor dimensions, profile-specific and current-condition contributions, source-result sensitivity, retained agency, repair/reopening, source and claim scope | no fifth profile, operation, prediction, instruction, determined conduct, or universal corridor ranking |
| multi-profile corridor claim | distinct constitutive carriers and effects for each supported profile, absent/uncertain profiles declared, no compensation | no synthetic Trajectory-strength score or authority increase |

Canonical route: [`Chapter 11 §§11.5–11.9`](../01_blocks/02_part_i_path.md#11-5-attractor-sedimentation).

## Chapter 11 WP3 — Boundary, Compression, Competition, and Record Claim Types

| Claim type | Minimum assertion burden | Required ceiling / reduction |
| --- | --- | --- |
| Trajectory Boundary claim | reference object, frame, start, entry rationale, relevant prehistory, included segments, analytical cut, terminal status, open continuation, disputed periodization, source and claim scope | no natural seam, unique periodization, completed future, or retroactive repair |
| Trajectory Compression claim | preserved load-bearing transitions, Non-Events, profiles, alternatives, reversals, repairs, current-condition pressure, canonical Loss, Counterfactual Sensitivity | no lossless summary, monotonic flattening, macro-label substitution, or Chapter-15 `COMPOSE` completion |
| competing-construction claim | independent Path and sedimentation burdens, common comparison dimensions, declared relation, source asymmetry, no forced synthesis | no automatic equivalence, ranking by detail, or all-rivals-valid inference |
| False-Trajectory diagnosis | identified constitutive failure, weaker-finding preservation, canonical disposition, lineage and re-entry rule | no new object or Output Class; no erasure of history; no stronger derivation from failed premise |
| Minimal-Trajectory-Record claim | Shared Record mapping, field semantics, unknown/absent/excluded distinctions, Loss, alternatives, governance, Chapter-12 handoff | no second schema, field-completeness proof, automatic Path Dependence, target function, or authority |
| Non-Capture claim for competing Trajectories | materially rival source-responsible constructions, unresolved adjudication, explicit source ceiling, no hidden synthesis | no validation of rivals and no protection of unsupported claims |

Canonical route: [`Chapter 11 §§11.10–11.14`](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary).

## Chapter 11 Provisional-Lock Claim Controls

| Claim family | Required Chapter 11 load | Forbidden automatic upgrade |
| --- | --- | --- |
| Trajectory claim | warranted Path, carrier, cumulative relation, present effect, Source–Result Dependency, Boundary, Loss, ceiling | Path Dependence, causality, function, authority |
| profile claim | profile-specific occurrence carrier, temporal trace, present effect, counterpressure, source support | operator fusion, universal strength score, legitimacy |
| corridor claim | declared accessibility dimension, historical contribution, current-condition allocation, uncertainty | eliminated agency, prediction, recommendation |
| Boundary/periodization claim | reference, entry rationale, prehistory, analytical cut, segment lineage, open continuation | natural seam or uniquely true periodization |
| competing-construction claim | independent Path and Trajectory burdens plus common comparison basis | forced synthesis or automatic validation of rivals |
| False Trajectory claim | explicit failed burden and preserved weaker findings | no history, no Path, new object class, new Output Class |
| record claim | structurally complete Shared-Record view | historical truth, admissibility, Path Dependence |

Canonical return: [`Chapter 11 completion boundary`](../01_blocks/02_part_i_path.md#chapter-11-completion-boundary).


---

## Chapter 12 Preparation Claim Controls

| Claim | Minimum support | Required counterpressure | Typical canonical mapping |
| --- | --- | --- | --- |
| no material historical dependence at tested level | adequate current-state reconstruction; history adds no material discrimination | hidden carrier or omitted dimension | `resolution_neutral` where no stronger claim remains active |
| weak order dependence | warranted order relation and bounded local present difference | current-state sufficiency and low sedimented load | `admissible_with_bounded_claim` |
| strong Path Dependence | warranted Trajectory, declared dimension, carrier, present effect, current-state challenge, omission/variation sensitivity, source and claim ceilings | current-only explanation, rival history, modifier/repair, non-determinism | `admissible_with_bounded_claim` or `admissible_but_provisional` |
| strong-to-weak reduction | strong burden fails while local order effect remains | narrower claim must receive its own test | `claim_reduction_required` |
| underdetermined dependence | rival historical/current explanations remain source-responsible | re-entry conditions and missing evidence | `non_capture` |
| failed dependence claim | duration, repetition, narrative, or profile labels lack current discriminative load | preservation of Path/Trajectory and current constraints | `claim_reduction_required`, `resolution_neutral`, or bounded failure routing |
| prohibited stronger use | known failed claim used for prediction, target function, diagnosis, sanction, legitimacy, or authority | no laundering through a new frame or operation | `mandatory_stop` |

Local strength findings are not new Output Classes. Every closed Record maps to the fixed ten-class vocabulary and preserves the original claim, reduction lineage, uncertainty, Loss, Stop, and Non-Capture status.

Production control: [`Chapter 12 Preparation Record`](Chapter_12_Preparation_Record.md).

## Chapter 12 WP1 Claim-Type Synchronization

| Local claim | Minimum burden | Typical bounded disposition |
| --- | --- | --- |
| no material historical dependence at tested level | current-state baseline remains sufficient and detailed Path adds no warranted discrimination | `resolution_neutral` where no stronger active claim remains |
| weak order dependence | warranted order relation, bounded local difference, source trace, and substantial current-state reconstructibility | `admissible_with_bounded_claim` |
| strong Path Dependence candidate | warranted input, declared dimension and cut, historical carrier, present effect, current-state challenge, Source–Result Dependency, and source-bounded omission/comparison pressure | `admissible_but_provisional` until full Chapter-12 duties are met |
| strong claim reduced to weak | strong historical indispensability unsupported while bounded order effect remains | `claim_reduction_required` |
| known failed dependence used for stronger derivation or authority | failed result ignored or laundered through operation, projection, prediction, diagnosis, or authority | `mandatory_stop` |

Local dependence strength is not an Output Class and does not rank objects, persons, histories, or domains.

## Chapter 12 WP2 Claim-Type Synchronization

| Claim | Minimum bounded burden | Ceiling |
| --- | --- | --- |
| Attractor-Dependence claim | recurrence lineage, retained carrier, current friction/default effect, current-state rival, omission/variation pressure | no inevitability, legitimacy, recommendation, or target function |
| Asymmetry-Dependence claim | temporal distribution trace, retained differential carrier, present burden, current-only challenge, source-bounded redistribution pressure | no person ranking, guilt, duty, legitimacy, sanction, or authority |
| Binding-Dependence claim | concrete Binding occurrences, reliance/investment, retained carrier, current enforceability allocation, reopening or release effect | no inner-intention inference, moral obligation, permanent binding, or enforcement authority |
| Residual-Dependence claim | warranted expectation frame and window, Non-Event, retained residue, present effect, current-state rival, repair/closure test | no missing-information inflation, blame, permanence, or person typing |
| multi-profile claim | separate carriers and local results for each profile, non-compensation, no all-profile requirement | no additive score, universal chain, whole-object spread, or authority increase |

All local profile findings map to the ten canonical Output Classes when closed; they are not new classes.

## Chapter 12 WP3 Claim-Type Synchronization

| Claim | Minimum burden | Ceiling / disposition |
| --- | --- | --- |
| persistence across `Φ` | source and target frames, carrier status, current conditions, tested dimension, present effect, Source–Result Dependency | no automatic reset or continuity |
| modifier claim | distinct later occurrence, pre/post carrier status, current effect, omission/comparison result | no erasure, validation, or operator fusion |
| strong Path-Dependence claim | warranted input, dimension, Current-State Baseline, carrier, Historical Omission, source-bounded variation, present effect, Loss and ceilings | no causality, prediction, fate, legitimacy, or whole-object spread |
| failed strong claim | failure reason and retained weaker finding | `claim_reduction_required`, `resolution_neutral`, bounded failure, or Stop as appropriate |
| undecidable dependence | materially rival source-responsible explanations and re-entry condition | `non_capture`; no midpoint score or blended certainty |

Local dependence-strength findings are not new Output Classes and require canonical mapping at claim closure.

## Chapter 12 Provisional-Lock Claim Controls

| Claim | Minimum burden | Canonical routing pressure |
| --- | --- | --- |
| no material historical dependence | current-state sufficiency and no added discriminative load | `resolution_neutral` where no stronger claim remains active |
| weak order dependence | bounded order effect plus substantial current-state reconstructibility | typically `admissible_with_bounded_claim` or reduction from a stronger claim |
| strong Path Dependence | historical indispensability under the complete conjunctive test | `admissible_with_bounded_claim` or `admissible_but_provisional` |
| failed strong claim with weaker support | explicit reduction and preserved lineage | `claim_reduction_required` |
| known failed claim reused for stronger action/function/person claim | anti-laundering breach | `mandatory_stop` |
| materially rival historical/current explanations remain undecidable | source-responsible unresolved competition | `non_capture` |

A local dependence-strength finding is not a new Output Class. Canonical return: [`Chapter 12 completion boundary`](../01_blocks/02_part_i_path.md#chapter-12-completion-boundary).

---

## Chapter 13 Preparation Claim Controls

| Claim | Minimum burden | Maximum bounded effect | Prohibited escalation |
| --- | --- | --- | --- |
| branch-point claim | historical cut, multiple supported continuations, window, frame, source basis | bounded availability finding | necessity or causal proof |
| rejected-branch claim | availability plus documented refusal/non-selection | rejection status and residue | blame or irrationality |
| blocked-branch claim | availability plus identifiable prevention | bounded blockage finding | impossibility or legitimacy judgment |
| aborted-branch claim | initiation trace plus interruption | interrupted continuation and residue | treating attempt as completed Path |
| deferred-branch claim | earlier window plus later continuation conditions | delay-shaped continuation | identity with uninterrupted continuation |
| lost-alternative claim | earlier availability plus later unavailability and loss structure | bounded loss finding | prediction of the unrealized outcome |
| counterfactual-Path claim | documented branch point, bounded variation, retained constraints, source stop | sensitivity and loss inspection | alternate-history completion or forecast |
| non-selection claim | active decision context, window, no selection, consequence | non-selection as praxis structure | inferring intention or guilt |

Local findings map to the fixed ten Output Classes. Branch classes are not Output Classes.

## Chapter 13 WP1 Claim-Type Handoff

| Claim | Minimum support | Claim ceiling |
| --- | --- | --- |
| alternative-space claim | historical cut, window, practical availability, source basis | no exhaustive possibility claim |
| Branch-Point claim | at least two distinct source-supported continuations | no prediction or outcome ranking |
| Realized-Branch claim | actual entry and traversal trace | no rationality, legitimacy, or inevitability |
| Rejected-Branch claim | open availability plus documented refusal/non-selection | no claim that the route would have succeeded |

Branch status is not an Output Class and does not create authority.

## Chapter 13 WP2 Claim-Type Handoff

| Claim type | Minimum support | Prohibited inflation | Typical bounded disposition |
| --- | --- | --- | --- |
| Blocked-Branch claim | earlier availability/preparation plus identifiable prevention relation inside a declared window | impossibility, blame, illegitimacy, override authority | `admissible_with_bounded_claim`, reduction, or `non_capture` |
| Aborted-Branch claim | initiation and partial traversal plus interruption before claimed completion | never-begun treatment, causal totalization, same-label continuity | `admissible_with_bounded_claim` or reduction |
| Deferred-Branch claim | original availability plus deferral trace, changed window, and later candidacy/reachability | uninterrupted identity, unchanged-cost assumption | `admissible_with_bounded_claim`, provisional, or `non_capture` |
| Lost-Alternative claim | earlier availability plus later unavailability/material unreachability and source-supported loss transition | preference ranking, prediction, causal or normative proof | `admissible_with_bounded_claim`, `claim_reduction_required`, or `non_capture` |

These are claim types, not new Output Classes. A strong status claim may reduce to an unrealized candidate, uncertain status, or no supported alternative claim without erasing the realized Path.

## Chapter 13 WP3 Claim-Type Handoff

| Claim | Minimum warrant | Ceiling / reduction route |
| --- | --- | --- |
| bounded Counterfactual-Path claim | source-supported historical entry branch, explicit divergence rule, approximately held-stable conditions, declared source ceiling and horizon | reduce to available-branch claim or open possibility; no success, prediction, or causal proof |
| Non-Selection claim | active selection context, bounded window, available continuations, source-supported absence of selection, Path-forming consequence | reduce to missing decision information or unresolved selection status |
| Alternative-Space Compression claim | material branch field, selection rule, canonical Loss, preserved uncertainty and status differences | reduce Path/Trajectory claim if constitutive alternatives disappear |
| Alternative Status Record claim | owner-bound extension, field support, required Shared-Record fields retained, uncertainty and Output-Class mapping | complete record does not prove availability or status |
| branch-status reduction claim | failed positive burden with weaker supported Path, source-gap, candidate, or current-unavailability finding | no alternative claim where earlier availability is unsupported |

These claims remain source-, frame-, window-, and dimension-bounded. None supplies operation completion, target function, prediction, legitimacy, person judgment, or application authority.

## Chapter 13 Provisional-Lock Claim Controls

Chapter 13 supports only source- and window-bounded claims about historical availability, selection, prevention, initiation, interruption, deferral, later reachability, loss, Non-Selection, compression, and bounded Counterfactual Paths. Each claim must preserve uncertainty and map to the fixed canonical Output Classes.

It does not support claims of unrealized outcome, causality, inevitability, rationality, legitimacy, person character, prediction, completed operation, target function, or application authority.

Canonical return: [`Chapter 13 completion boundary`](../01_blocks/02_part_i_path.md#chapter-13-completion-boundary).

## Chapter 14 Preparation Claim Controls

| Claim | Minimum support | Required ceiling | Typical canonical disposition pressure |
| --- | --- | --- | --- |
| PATH-specific Non-Event | expected occurrence, expectation relation/frame, bounded window, supported non-realization, load, temporal relevance | no motive, blame, causal completeness, or future prediction | `admissible_with_bounded_claim` / `admissible_but_provisional` |
| Delay as `Λ` | due transition, missed or closed window, source support, changed praxis conditions | no intentionality inference | bounded admissibility or reduction |
| repeated Non-Decision | renewed active decision windows, repeated supported non-realization, accumulated load | not refusal automatically | bounded admissibility / `non_capture` |
| Blocked Responsibility | expected action, role architecture, blocking relation, bounded non-realization | no person fault, diagnosis, legal duty, or sanction | `admissible_with_bounded_claim` |
| Missing Repair | independently warranted repair occurrence and window, supported failure, residue | no invented duty | bounded admissibility / reduction |
| Missing Exit | independently warranted or triggered exit/release and window, supported failure | no motive, voluntariness, coercion, or person judgment | bounded admissibility / reduction |
| Non-Event Sedimentation | warranted `Λ` occurrence(s), later carried load, occurrence/interval distinction, competing construction | no automatic Path Dependence | `admissible_but_provisional` |
| False Non-Event | missing expectation, window, source support, load, or relevance | failure does not prove occurrence | `claim_reduction_required`, `failed_transformation`, or `mandatory_stop` |
| unresolved expectation/non-realization structure | positive material structure but decisive source/status distinction unresolved | no forced closure | `non_capture` where warranted |

Local pattern names are not new Output Classes and must map to the ten canonical classes.

## Chapter 14 WP1 Claim-Type Handoff

| Claim | Minimum support | Claim ceiling |
| --- | --- | --- |
| local Non-Event candidate | expected occurrence, warranted expectation relation, frame, bounded window, non-realization support, load | no Path centrality automatically |
| path-forming Non-Event | local `Λ` burden plus material temporal-chain relation | no sedimentation or Path Dependence automatically |
| frame-sensitive Non-Event | explicit comparison of source-supported frames and expectations | no frame arbitrariness or contradiction neutralization |
| Delay-as-Non-Event | warranted time bound, missed window, source support, changed Path load | no intention, blame, breach, or later-outcome claim |
| unresolved occurrence status | expectation/window supported but realization status not established | reduce; do not infer `Λ` |

These findings are not new Output Classes and must map to the fixed canonical vocabulary.

## Chapter 14 WP2 Claim-Type Handoff

| Claim | Minimum support | Claim ceiling |
| --- | --- | --- |
| repeated Non-Decision | renewed decision contexts, warranted expectation, bounded windows, non-realization in each claimed context | no refusal, intention, or sedimentation automatically |
| blocked responsibility | expected occurrence, role architecture, blocking relation, bounded window, non-realization and load | no person blame, duty, diagnosis, legitimacy, or sanction |
| Missing Repair | independent repair expectation, completion condition, window, non-realization, residue | no liability, guaranteed repair success, or exclusive causation |
| Missing Exit | warranted or triggered release occurrence, window, non-realization, continuation load | no motive, coercion, voluntariness, incapacity, or consent claim |
| Non-Event Sedimentation | warranted source `Λ`, occurrence architecture, later carrier, present load, rival pressure | no strong Path Dependence, determinism, operation, or function automatically |

These are local findings, not new Output Classes.

## Chapter 14 WP3 Claim-Type Handoff

| Claim | Minimum support | Claim ceiling |
| --- | --- | --- |
| preservable `Λ` source structure | warranted expectation/frame/window/non-realization, positive sub-events, load, uncertainty, canonical Loss | no completed `COMPOSE` automatically |
| False Non-Event | identified failed constitutive burden | no proof that the expected event occurred |
| complete Minimal Non-Event Record | owner-bound extension, source and uncertainty fields, non-replacement of top-level record | no semantic validity or output mapping automatically |
| claim reduction | strongest weaker statement retained with failed claim history | no retroactive repair by new frame, graph, or label |
| Mandatory Stop | unsupported `Λ` reused for person attribution, sanction, authority, prediction, operation, or function | no continued authoritative use |
| Non-Capture | materially relevant source/non-realization alternatives remain inseparable | no forced positive or negative occurrence finding |

These are local claim types and audit findings, not new Output Classes.

## Chapter 14 Provisional-Lock Claim Controls

Chapter 14 supports only frame-, window-, source-, granularity-, and Claim-Ceiling-bounded claims about expectation-grounded non-realization, Delay, recurring decision contexts, responsibility configuration, Missing Repair, Missing Exit, sedimentation, preservation, failure, reduction, Stop, and Non-Capture.

It does not support hidden-intention, refusal, blame, duty, coercion, motive, diagnosis, legitimacy, sanction, automatic Path Dependence, completed operation, target-function, predictive, or application-authority claims.

Canonical return: [`Chapter 14 completion boundary`](../01_blocks/02_part_i_path.md#chapter-14-completion-boundary).

## Chapter 15 Preparation Claim Controls

| Claim | Minimum support | Claim ceiling | Typical output pressure |
| --- | --- | --- | --- |
| COMPOSE occurrence admissible | typed related sources, selection/order/frame/formation, constitutive trace, Loss, praxis difference | no empirical truth or function inheritance | `admissible` / bounded or provisional variants |
| Sequence composition | warranted order beyond list | no Path claim automatically | bounded admissibility |
| Path composition | actual traversal, selection, relation, evidence, Loss | no Trajectory or dependence automatically | bounded/provisional admissibility |
| Trajectory composition | warranted Path plus sedimentation and historical load | no Path Dependence automatically | provisional admissibility |
| reduced composition | stronger target fails while weaker target remains supported | no laundering of failed stronger claim | `claim_reduction_required` / `partially_admissible` |
| competing composition | materially different source-supported formation | no forced unique capture | `admissible_but_provisional` / `non_capture` |
| target-function claim | separate `PROJECT_AS` record required | no function from object formation alone | Stop or separate operation |
| failed formation | missing relation, formation, traceability, Loss, or praxis gain | target label cannot survive as authority | `failed_transformation` / `mandatory_stop` |

## Chapter 15 WP1 Claim Controls

| Local claim | Minimum WP1 support | Ceiling before WP2/WP3 |
| --- | --- | --- |
| COMPOSE entry candidate | purpose, typed sources, entry burdens, selection, order where claimed, frame, bounded target hypothesis | no formation success |
| source-role claim | declared relation of one source to candidate target | provisional until sensitivity test |
| selection claim | inclusion/omission reasons, contestability, Loss pressure | no unique-best selection automatically |
| ordering claim | source-supported linear, partial, parallel, overlapping, recurrent, or uncertain relation | no causal order automatically |
| frame-bounded candidate | reference object, source/target frame, scope, granularity, level, Claim Boundary/Ceiling | no target function |
| no-composition result | relation or formation burden not supportable without destructive simplification | weaker source findings remain |
| competing candidates | materially supportable selections or frames yield different targets | no forced unique capture |

These are local findings and must map to the ten canonical Output Classes only after the applicable audit.

## Chapter 15 WP2 Claim Controls

| Claim | Minimum WP2 burden | Permitted bounded result | Prohibited inflation |
| --- | --- | --- | --- |
| formation hypothesis | declared target, Formation Rule candidate, constitutive relations, source trace, open Loss | `admissible_but_provisional` or reduction | completed operation |
| Sequence formation | warranted order and target boundary beyond a list | bounded Sequence | Path automatically |
| Path formation | actual traversal, constitutive relations, alternatives/load, preservation, Loss | bounded Path | Trajectory or dependence automatically |
| preservation claim | reconstructible dependence on declared source load | preserved through representation or lineage | total retention or losslessness |
| compression claim | rule, reduced resolution, retained distinctions, recoverability, uncertainty | bounded compression | erasure hidden as summary |
| exclusion claim | explicit material, reason, frame, contestability, target effect | frame-bound exclusion | falsity or global irrelevance |
| uncertainty claim | material unresolved issue and claim consequence | provisionality, reduction, Stop, Non-Capture | forced resolution |
| irrecoverable-loss claim | origin, unavailable structure, target materiality, claim consequence | bounded claim or failure/non-capture | presumed restoration |

Each row remains subordinate to source and claim ceilings and canonical Output Class mapping.

## Chapter 15 WP3 Claim Controls

| Claim | Minimum burden | Bounded route | Prohibited inflation |
| --- | --- | --- | --- |
| composite-object claim | typed target, Formation Rule, constitutive trace, Loss | canonical object claim | every stronger claim |
| constitutive-relation claim | source trace plus material sensitivity | claim-relative constitutive status | causal necessity |
| target-strength claim | class-specific threshold and Claim Ceiling | Sequence, Path, Trajectory, or reduction | upward inheritance |
| no-retyping claim | preserved source typing and separate target object typing | object formation only | target function |
| overelasticity finding | material source-bounded variation with unchanged target | revision, rival composition, reduction, failure | universal invalidity |
| failure claim | identified failed burden and preserved weaker result | reduction, failed transformation, Stop, Non-Capture | source erasure |
| record-completeness claim | Shared Record and `composeDetails` conformance | auditability | semantic truth |

## Chapter 15 Provisional-Lock Claim Controls

| Claim | Minimum burden | Bounded route | Prohibited inflation |
| --- | --- | --- | --- |
| source-field claim | typed and lineaged sources with scope | source collection or ordered field | completed composition |
| composite-object claim | Selection Rule, order, frame, Formation Rule, constitutive trace, typed target, Loss | bounded Sequence, Path, Trajectory, branch structure, phase, or other declared object | every stronger object class |
| constitutive-relation claim | source trace plus material sensitivity | claim-relative constitutive status | causal necessity |
| preservation claim | reconstructible target-to-source dependence | declared preserved load | losslessness |
| compression claim | rule, resolution change, lineage, recoverability, uncertainty impact | bounded compression | erasure or inversion guarantee |
| overelasticity claim | materially relevant source-bounded variation with unchanged target | revision, rival composition, reduction, failure | universal invalidity |
| operation-success claim | complete substantive procedure and canonical output | local `COMPOSE` occurrence | target function or authority |
| record-completeness claim | Shared Record and `composeDetails` conformance | auditability | semantic truth |

Canonical return: [`Chapter 15 completion boundary`](../01_blocks/02_part_i_path.md#chapter-15-completion-boundary).

## Chapter 16 Preparation Claim Controls

| Claim segment | Required support | Boundary pressure | Permitted weaker retention |
| --- | --- | --- | --- |
| chronology | source-supported occurrence and order | may remain below PATH Floor | chronology or partial order |
| Path | transitions, actual traversal, material order, frame, Loss | chronology without gain; omitted load | Sequence or source field |
| Trajectory | Path plus sedimentation and present-bearing historical load | Trajectory without trace; teleology; compression | bounded Path |
| PATH boundary claim | reasoned Purchase and Trace findings | local value treated as final class | retest or underdetermined finding |
| PATH/SUB claim | existing compressed object and valid `DECOMPOSE` occurrence | finer detail used as rescue | new resolution claim |
| PATH/RETYPE claim | origin-typed object and bounded `PROJECT_AS` occurrence | target function used as rescue | separate projection claim |

A boundary result constrains the tested claim. It does not validate or invalidate persons, institutions, norms, causal theories, or interventions.

## Chapter 16 WP1 Claim Controls

| Local claim | Required WP1 burden | Maximum local result before WP2–WP4 |
| --- | --- | --- |
| lower-bound gain | temporal differentiation materially changes the warranted praxis reconstruction | no automatic upper-bound passage |
| neutral chronology | valid order or detail without changed tested reconstruction | bounded chronology/index only |
| below-Floor stronger claim | claimed PATH strength depends on absent purchase | Claim Reduction; source record preserved |
| within-Ceiling target | source-to-result dependency survives bounded removal/reorder pressure | no teleology, omission, or Part-boundary clearance yet |
| above-Ceiling target | target outruns reconstructible constitutive load | failed stronger transformation or Stop where misused |
| Trajectory without trace | direction/sedimentation asserted without reconstructible Path burden | reduction to bounded Path, Sequence, chronology, comparison, or source set |
| compression within Ceiling | rule, retained distinctions, lineage, recoverability, uncertainty, Loss, and Claim Ceiling remain explicit | no losslessness or inversion guarantee |
| punctualized target | extended internal temporality collapsed and target becomes source-indifferent | `failed_transformation` for the stronger target |

Local Floor and Ceiling findings are not canonical Output Classes. Final mapping remains governed by the full audit and Boundary Decision Tree.

## Chapter 16 WP2 Claim Controls

| Local claim | Required WP2 burden | Boundary effect |
| --- | --- | --- |
| bounded directionality | dimension, carrier relations, reversals, alternatives, periodization, Loss, and Claim Ceiling | no purpose, destiny, or global-vector inheritance |
| artificial directionality | source-supported counter-movement or contingency is removed by retrospective line | reduction or failure of the stronger directional claim |
| non-teleological Path | endpoint-independent selection and preserved alternatives | no necessity, prediction, progress, decline, or hidden intention |
| constitutive `Λ` preserved | Chapter-14 threshold plus material target dependence | omission may reduce or fail the PATH claim |
| constitutive `Ω` preserved | source-supported unequal practical load plus target dependence | aggregate may split into bounded Paths |
| later target function | valid separate `PROJECT_AS` from the actual origin object | cannot repair failed stronger PATH claim |
| finer reconstruction | valid separate `DECOMPOSE` of an identified compressed object | no truth priority and no invalid-object rescue |

No local WP2 finding mechanically selects a canonical Output Class.

## Chapter 16 WP3 Claim Controls

| Claim | Required support | Canonical pressure if absent |
| --- | --- | --- |
| temporal differentiation adds PATH purchase | claim-relative baseline, material difference, source-to-difference dependency | `resolution_neutral`, `claim_reduction_required`, or `failed_transformation` as warranted |
| target remains traceable | typed sources, lineage, order, constitutive relation, preserved load, complete Loss, sensitivity | Claim Reduction, Failure, Stop, or Non-Capture |
| bounded Path remains provisional | localized uncertainty with stable bounded target and preserved alternatives | `admissible_but_provisional` |
| stronger claim reduces | failed claim named; surviving sources, target, Loss, and uncertainty retained | `claim_reduction_required` plus separate mapping of surviving claim |
| one integrated PATH object is unavailable | bounded tests leave irreducible traces or periodizations without responsible closure | `non_capture` |
| continued use must stop | known failure is reused beyond source, safety, operation, function, or authority ceiling | `mandatory_stop` |

No row mechanically selects an Output Class from a local Floor or Ceiling value.

## Chapter 16 Provisional-Lock Claim Controls

| Claim | Required support | Maximum local claim |
| --- | --- | --- |
| temporal gain | claim-relative baseline, materially changed praxis reconstruction, source-to-difference dependency | bounded Floor finding |
| traceable Path or Trajectory | typed and lineaged sources, order, constitutive relations, preserved load, complete Loss, sensitivity | bounded Ceiling finding and PATH target claim |
| bounded directionality | dimension, periodization, reversals, alternatives, source support | non-teleological local direction |
| omission failure | prior warrant for `Λ` or `Ω`, material target change when restored | claim reduction or failure of the affected PATH claim |
| provisional PATH object | surviving bounded target plus localized uncertainty | `admissible_but_provisional` |
| Non-Capture | bounded tests showing no adequate single object without false closure | `non_capture` for the integrated claim |

No Chapter-16 claim licenses causal necessity, prediction, person judgment, legitimacy, sanction, target-function assignment, intervention authority, or authority inheritance.

## Chapter 17 Preparation Claim Controls

| Claim | Required support | Prohibited inflation |
| --- | --- | --- |
| admissible PATH case | complete bounded record, Loss, alternatives, Band passage, output mapping | universal PATH validation |
| admissible Trajectory case | Path plus sedimentation, directionality without teleology, source sensitivity | target-function or strong-dependence inheritance |
| Path-Dependence case | dimension-specific historical indispensability and current-state challenge | whole-object dependence or determinism |
| countercase result | identified failure mechanism and preserved weaker findings | decorative rejection without test |
| confusion-case resolution | separated object/operation/frame burdens | category collapse |
| Part-I lock | local audit pass and artifact completion | system-wide validation or authority |

## Chapter 17 WP1 Standalone Case Claim Controls

A standalone positive case separates:

- source claim;
- object-formation claim;
- constitutive-relation claim;
- target-strength claim;
- local result description;
- canonical Output-Class mapping;
- excluded stronger claims;
- authority boundary.

`C17-LAMBDA-01` retains a Trajectory claim while explicitly withholding strong Path Dependence, causal necessity, target function, prediction, person judgment, and application authority.

## Chapter 17 WP2-A Dependence-Claim Controls

A Path-Dependence claim must declare its tested present dimension, current-state-sufficiency burden, historical-indispensability burden, excluded reach, and counterfactual mutation. Whole-object dependence may not be inferred from endpoint difference or recurrence alone.

## Chapter 17 WP2-B Countercase Claim Controls

A failed or reduced PATH claim must preserve its exact object class, failed relation, source-supported residue, proposed weaker route, retest requirement, and authority boundary. Softening rhetoric without changing Selection or Formation does not create a new warrant.


## Chapter 17 WP2-C Claim Controls

| Case | Stronger claim | Preserved weaker finding | Mapping |
|---|---|---|---|
| `C17-OMEGA-01` | uniform Trajectory from equal milestones | differentiated Paths and milestone chronology | `failed_transformation` |
| `C17-FALSEL-01` | central-`Λ` escalation Trajectory | positive event field and explicit source gap | `claim_reduction_required` |

A preserved weaker finding is not pre-authorized as admissible.


## Chapter 17 WP3-A Claim Separation

- `C17-PROJ-01`: current declared-composite Trajectory claim; later Frame-function claim separated and untested.
- `C17-RES-01`: resolution-gain claim rejected while the prior warranted Path and valid refinement remain.
- `C17-ATTR-01`: current Trajectory claim retained; Attractor identity/function claim excluded and deferred.

```text
separated claim
≠ silently executed operation
```


## Chapter 17 WP3-B — PATH Claim and Completion Separation

The case corpus retains Path, Trajectory, and dimension-specific Path-Dependence claims separately from chronology, neutral resolution, target function, and Attractor-function claims. Chapter-level `admissible_but_provisional` records production status and does not overwrite the thirteen case mappings or create a new transformation record.

## Part I — PATH Provisional-Lock Claim Boundary

The lock covers bounded Sequence, Path, Trajectory, dimension-specific Path-Dependence, branch/alternative, Non-Event, and `COMPOSE` claims already tested in Chapters 9–17. It does not cover hidden component claims, target functions, empirical causality, prediction, diagnosis, legitimacy, intervention, or application authority.

## Chapter 18 Preparation — Source-Object Claim Controls

Chapter 18 separates four claim types:

| Claim | Required content | Does not establish |
|---|---|---|
| compressed-source-object claim | reference, origin type, Frame, granularity, level, function, source basis, uncertainty | actual components |
| provisional-elementarity claim | sufficiency for current Frame/granularity/claim | ontological indivisibility |
| decomposition-reason claim | expected praxeological difference, source route, stop condition | a successful `DECOMPOSE` result |
| no-decomposition claim | coarse sufficiency, no purchase, source insufficiency, irrelevance, or calibration loss | permanent undecomposability |

The current/coarser source function is a test target. Preserving it in the record does not immunize it from later refinement or rejection.

## Chapter 18 WP1 — Source-Candidate Claim Separation

| Claim type | Permitted WP1 assertion | Withheld assertion |
|---|---|---|
| SUB-scope claim | finer reconstruction is governed by SUB while `DECOMPOSE` remains a distinct operation | any fourth operation or operation occurrence |
| provisional-elementarity claim | the current analysis stops internal distinctions for declared coordinates, sources, and claim | absolute or ontological elementarity |
| compressed-source-candidate claim | an identifiable occurrence or composite is treated as one unit with bounded unresolved internal questions | discovered components, target granularity, or operation result |
| source-side typing claim | one relevant origin/occurrence typing is declared, with compatible or rival typings preserved | one exclusive true type |
| operator-type boundary claim | Δ–Ψ types are not STRATA decomposition sources | immunity of PMS Base from theoretical critique |
| eligibility claim | a concrete occurrence or composite may enter later admissibility testing | passage of Relevance Floor, source ceiling, continuity, or Chapter-20 procedure |

The WP1 production result `admissible_but_provisional` concerns the bounded corpus-production state. It is not the Output Class of a `DECOMPOSE` record.



## Chapter 18 WP2 — Compression and Entry-Decision Claims

| Claim type | Required support | Prohibited inflation |
|---|---|---|
| necessary-compression claim | relation, uncertainty, comparison, temporal orientation, source precision, or claim ceiling preserved by the coarse unit | compression is inherently correct or final |
| compression-insufficiency claim | source-supported internal distinction plus material effect on a bounded praxis claim | complexity, detail volume, or hidden-depth assertion alone |
| reason-to-decompose claim | coarse claim, expected distinction, source route, gain condition, neutrality condition, and stop condition | discovered components or successful operation result |
| no-decomposition claim | coarse sufficiency, no purchase, source insufficiency, claim irrelevance, calibration loss, or operation mismatch | permanent simplicity, absolute elementarity, or future closure |
| counterexample-pressure claim | a specific occurrence burdens the scope or typing of the coarse claim | automatic finer model or source route |

A Chapter-18 no-decomposition decision is an entry decision. It does not use `resolution_neutral` unless a later `DECOMPOSE` occurrence has actually produced and compared a finer reconstruction.


## Chapter 18 WP3 — Preservation and Source-Entry Claims

| Claim type | Required support | Prohibited inflation |
|---|---|---|
| reference-preservation claim | stable source lineage, declared identity conditions, and explicit coarse-to-finer relation | same label or topic similarity treated as identity |
| source-function test-target claim | current/coarser function and its support/uncertainty status remain explicit | function guaranteed to survive finer reconstruction |
| preservation-compliant revision claim | same reference and claim genuinely tested, with adverse results retained | revision treated as failure of preservation |
| source-entry Stop claim | coarse sufficiency, lack of purchase, source/type/reference boundary, or other controlled reason | simplicity, final closure, or person/causal finding |
| source-entry Non-Capture claim | materially incompatible source-supported reconstructions or unstable reference/relations after bounded testing | protection of a failed or strongest unsupported claim |

Possible later source-function effects—confirmed, refined, internally differentiated, partially preserved, rejected, or underdetermined—remain Chapter-20 local results and must map separately to the ten canonical Output Classes.


## Chapter 18 Provisional-Lock Claim Boundary

| Claim | What Chapter 18 may establish | What remains prohibited or deferred |
|---|---|---|
| source-candidate claim | identifiable occurrence or composite under declared source-side coordinates | hidden component truth or automatic operation warrant |
| compression-insufficiency claim | bounded claim pressure plus expected difference and source route | successful finer reconstruction |
| no-decomposition claim | coarse sufficiency, no purchase, source ceiling, mismatch, or calibration reason | permanent undecomposability or `resolution_neutral` automatically |
| source-readiness claim | complete enough declaration for Chapter-19 testing | target granularity, component relations, source-function effect |
| Chapter-18 lock claim | Contract and local audit passed provisionally | SUB lock, empirical warrant, or authority increase |

## Chapter 19 Preparation Claim Handoff

Chapter 19 prepares four claim families without assigning operation results:

| Claim family | Minimum burden | Does not establish |
| --- | --- | --- |
| granularity-relation claim | source and target resolutions, distinction change, Frame/reference status | actual finer components or truth gain |
| expected-difference claim | bounded praxis reconstruction that may change | predetermined result |
| comparability claim | aligned or translated reference, Frame, time, source, predicate, and distinction basis | empirical equivalence or superiority |
| mismatch claim | non-aligned distinction sets explaining apparent tension | contradiction dissolved or both claims true |

A no-gain pressure remains preparatory until Chapter 20/25. Local comparison descriptions are not canonical Output Classes. Every material coordinate change creates a new testable claim and does not erase prior failure.

## Chapter 19 WP1 Canonical Claim Handoff

| Claim family | WP1 may establish | WP1 does not establish |
| --- | --- | --- |
| granularity-change claim | a declared source-to-target distinction-set change along a bounded dimension | source-supported components, operation success, or truth rank |
| relative-downward claim | object, comparator, relation, and purpose for analytical opening | ontological layer, causal fundamentality, or final constituents |
| stable-Frame claim | continuity of reference, relevance rule, predicate, and bounded scope sufficient to prepare comparison | actual Frame identity by label reuse or valid decomposition automatically |
| changed-Frame claim | a separately declared relevance-rule change and new testable claim | inherited result, repaired prior failure, or `DECOMPOSE` identity |
| expected-difference claim | the bounded praxis reconstruction that a finer distinction set is meant to pressure | predetermined result or Chapter-25 resolution class |

Every material change of Frame, reference, predicate, or comparison dimension remains a new testable claim. WP1 assigns no operation result or canonical Output Class.

## Chapter 19 WP2 Canonical Claim Handoff

| Claim family | WP2 may establish | WP2 does not establish |
| --- | --- | --- |
| distinction-set claim | which units and/or relations become separately testable and which bounded claim they pressure | source-supported final components or operation success |
| local-candidate claim | a bounded source-visible structure with a plausible source-claim relation | necessity, sufficiency, decisive causality, or final component status |
| distributed-candidate claim | a traceable structure carried across time, roles, relations, documents, or institutional sites | macro status, one unified component, or causal production automatically |
| carrying-component claim | contribution to reproduction or constitution of a coarse function | indispensability, causal primacy, or exhaustive explanation |
| disturbing-component claim | source-relevant counterpressure capable of qualifying, weakening, or rejecting a coarse claim | automatic rejection or completed source-function effect |
| fragment claim | failure of the current reference/source/function/relevance/relation burden | universal irrelevance under every Frame or claim |

WP2 assigns no comparability status, `DECOMPOSE` result, Chapter-25 resolution class, or canonical Output Class.

## Chapter 19 WP3 Canonical Claim Handoff

| Claim family | WP3 may establish | WP3 does not establish |
| --- | --- | --- |
| comparability claim | a bounded basis across reference, predicate, Frame, time, source standard, dimension, translation, and Loss | identity, truth rank, mutual substitutability, or global comparability |
| translation claim | a declared mapping between non-identical distinction sets with disclosed residual mismatch | lossless equivalence or automatic semantic translation |
| partial-comparability claim | specified aligned predicates, segments, roles, or dimensions | whole-object comparability |
| incomparability claim | the precise relation currently preventing responsible comparison | plural truth, protection of a failed claim, or permanent impossibility |
| mismatch claim | apparent disagreement explained through non-aligned predicates or distinction sets | substantive contradiction dissolved automatically |
| contradiction-preservation claim | aligned reference, Frame, time, and predicate still support direct affirmation/denial pressure | final operation result or canonical Output Class |
| lower-granularity claim | whether a proposed distinction has a plausible route to changing warranted praxis reconstruction | resolution gain, neutrality, drift, or failure already classified |
| Minimal Granularity Relation claim | exact conceptual coordinate declaration and Shared Record mapping | actual components, source-function effect, DECOMPOSE success, or schema replacement |


## Chapter 19 Provisional-Lock Claim Boundary

| Claim | What Chapter 19 may establish | What remains prohibited or deferred |
|---|---|---|
| granularity-change claim | declared distinction-set relation between source and proposed target resolution | actual finer component truth or operation success |
| component-candidate claim | source-related, claim-relevant carrying, disturbing, or replaceable candidate | necessity, sufficiency, causal priority, or final constituency |
| comparability claim | local aligned or translated comparison basis with Loss | identity, global comparability, or truth ranking |
| mismatch/contradiction claim | apparent mismatch or preserved contradiction under explicit predicates | automatic semantic adjudication |
| coordinate-readiness claim | complete enough relation for Chapter-20 testing | source support, source-function effect, or Output Class |
| Chapter-19 lock claim | Contract and local audit passed provisionally | SUB lock, empirical warrant, or authority increase |

## Chapter 20 Preparation Claim Separation

A Chapter-20 record may contain several claims that must not be fused:

| Claim axis | Question | Typical disposition |
| --- | --- | --- |
| operation claim | Was a valid `DECOMPOSE` occurrence executed? | retained, bounded, provisional, failed, stopped, non-captured |
| source-function claim | What happened to the current/coarser function under finer evidence? | confirmed, refined, differentiated, partially preserved, rejected, underdetermined |
| prior source claim | Does the earlier coarse formulation remain warranted? | retained, narrowed, reformulation required, withdrawn, unresolved |
| resolution claim | Did finer resolution change a warranted reconstruction? | owned fully by Chapter 25; Chapter 20 may prepare no-gain evidence |

Distinct claims require distinct record segments and may receive distinct canonical Output Classes. Class stacking on one undifferentiated claim remains prohibited. Preparation control: [`Chapter_20_Preparation_Record.md`](Chapter_20_Preparation_Record.md).

## Chapter 20 WP1 Claim-Type Return

| Claim | What WP1 may establish | What remains withheld |
| --- | --- | --- |
| operation-identity claim | the proposed transformation is of `DECOMPOSE` form | actual success or admissibility |
| precondition claim | declared entry burdens are present or a burden fails | component or relation support |
| source-identity claim | a bounded occurrence/composite is independently identifiable | final reference continuity under the completed finer model |
| decomposition-question claim | one source-, distinction-, claim-, route-, no-gain-, and Stop-bound question is explicit | answer, source-function effect, or Output Class |
| operator-type boundary claim | Δ–Ψ types are not decomposed | occurrence typing confirmation or rejection |

WP1 claims are procedural and source-entry bounded. They do not inherit higher truth, causality, completeness, or authority from finer resolution.

## Chapter 20 WP2 Claim-Type Return

| Claim | WP2 may establish | WP2 must not infer |
| --- | --- | --- |
| Expected-difference claim | bounded possible change plus no-gain condition | promised discovery or operation success |
| Source-support claim | role-specific source-to-component/relation support | general source sufficiency or truth |
| Component claim | local component status after five burdens | final constituent, necessity, sufficiency, or causal primacy |
| Relation claim | source-supported local organization and uncertainty | automatic causality or new PMS operator |
| Internal-temporality claim | supported order, interval, overlap, delay, persistence, or uncertainty | complete chronology where sources do not carry it |

Source-function effect, operation result, prior source-claim disposition, canonical Output Class, and final Loss remain separate later claims.

## Chapter 20 WP3 Claim-Axis Return

A completed decomposition may carry at least four distinct claim axes:

1. the current operation claim;
2. the source-function effect;
3. the prior source-claim disposition;
4. the canonical governance class for the current claim.

Distinct claims with different results require separate record segments or linked records. One source object does not authorize one undifferentiated class assignment.

Primary site: [§20.9–§20.10](../01_blocks/03_part_ii_sub.md#20-9-preservation-of-source-function).

## Chapter 20 WP4 Claim-Lock Return

| Claim family | Chapter 20 may establish | Chapter 20 does not establish |
|---|---|---|
| operation claim | a bounded generic `DECOMPOSE` occurrence with supported components and relations | universal decomposition success |
| source-function claim | confirmed, refined, differentiated, partially preserved, rejected, or underdetermined under the tested sources | immunity of the coarse function |
| prior-claim disposition | explicit retention, reduction, failure, or unresolved status for the prior claim | automatic identity with the new operation result |
| output-class claim | one canonical class for one clearly segmented claim | automatic or stacked classification |
| authority claim | no authority increase | empirical, causal, institutional, person-level, or application authority |

Primary site: [Chapter-20 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-20-completion-boundary).

## Chapter 21 Preparation Claim Types

| Claim | May be tested in Chapter 21 | Must not be inferred |
|---|---|---|
| Occurrence-typing claim | whether one bounded occurrence is adequately Frame-, Attractor-, Asymmetry-, Impulse-, or Binding-typed | operator essence or universal family rule |
| Production-condition claim | which source-supported structures produce or maintain the occurrence | final constituents, necessity, sufficiency, or causal primacy |
| Stability claim | coarse function persists across internal variation | internal homogeneity or immutable type |
| Distributed-Asymmetry claim | whether local gradients coordinate within the same occurrence | automatic macro-object or target function |
| Binding claim | structural continuity, records, commitments, and breach costs | person property, moral rank, or diagnosis |

Preparation control: [Chapter 21 Preparation Record](Chapter_21_Preparation_Record.md).

## Chapter 21 WP1 Claim-Type Return

| Claim | WP1 may establish | WP1 must not infer |
| --- | --- | --- |
| operator-occurrence claim | one bounded source occurrence is under a declared operator typing | the operator type is composed of observed parts |
| Frame-production claim | supported practices and relations maintain or disturb one Frame occurrence | universal constituents of `□` |
| stable-function claim | a bounded Frame function survives declared internal variation | internal homogeneity or component necessity |
| substitution claim | a replacement may preserve or alter a bounded function | free interchangeability or unchanged costs automatically |
| counterevidence claim | finer evidence can pressure the occurrence typing | rejection of the operator type |
| role claim | a role carries a relation in one occurrence | person property, motive, diagnosis, maturity, or moral rank |

Primary sites: [§21.1–§21.4](../01_blocks/03_part_ii_sub.md#chapter-21-decomposing-operator-typed-occurrences).

## Chapter 21 WP2 Claim-Type Return

WP2 permits bounded occurrence claims about:

- supported differential continuation within one Attractor-typed occurrence;
- repetition without sufficient Attractor load;
- recurrent dynamic transition form;
- dimension-specific gradients within one Asymmetry-typed occurrence;
- coordinated, offsetting, or uncoordinated distributed gradients.

It does not authorize person claims, motive claims, causal sufficiency, macro-object formation, target functions, legitimacy, sanction, or authority. Final source-function effects and canonical Output Classes remain deferred.

Primary sites: [§21.5–§21.9](../01_blocks/03_part_ii_sub.md#21-5-attractor-typed-occurrence).

## Chapter 21 WP3 Claim-Type Return

Occurrence-family claims remain distinct from motive, person, legitimacy, causal-necessity, composite, and target-function claims. The bounded Binding example separates `supported_relational_decomposition`, `internally_differentiated`, reduced prior claim, and `admissible_with_bounded_claim` as four different axes. None may inherit authority from another.

Primary site: [§21.11](../01_blocks/03_part_ii_sub.md#21-11-binding-typed-occurrence).

## Chapter 21 WP4 Claim Boundary Return

Chapter 21 permits bounded claims about the production, maintenance, disturbance, internal variation, substitution, and failure conditions of one source-supported operator-typed occurrence. It does not authorize claims about operator constituents, person identity, motive, diagnosis, moral rank, legitimacy, sanction, universal institutional structure, composed macro-objects, or contextual target functions without their own warranted operations.

Primary site: [Chapter-21 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-21-completion-boundary).

## Chapter 22 Preparation Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| composite-source-entry claim | identifiable constituents, boundary, constitutive relation, function, trace, inherited limits | bundle or label treated as composite |
| internal-composition-map claim | components and relations jointly represented with source support and uncertainty | parts list |
| component-role claim | role relative to bounded composite function, Frame, time, and counterpressure | universal or ontological role |
| operator-weighting claim | declared dimension, occurrence carriers, time, support, counterpressure, changed-reconstruction condition | additive score or dependency revision |
| modulating-profile claim | source-side access, threshold, temporal, cost, exposure, repair, or stabilization relation | operator or person type |
| distributed-function claim | separated elements, coordination, common function, partial-failure effect | aggregation or co-presence |
| redundancy/substitution claim | removal or replacement pressure, preserved function, changed cost/load/Loss | irrelevance or identity |
| internal-conflict claim | supported conflict relation and bounded outcome | automatic composite destruction or legitimacy judgment |
| composite-stability claim | specified stability object, interval, mechanism, and unequal-load status | stable label as proof of stable parts |
| fragmentation-failure claim | source composite or function lost through atomism, relation loss, unsupported role, or local overprivileging | more detail treated as success |

Preparation control: [Chapter 22 Preparation Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP1 Claim-Type Return

| Claim | WP1 may establish | WP1 must not infer |
| --- | --- | --- |
| composite-entry claim | one bounded source object satisfies constituent, boundary, relation, function, trace, and Loss burdens | every bundle, institution label, or multiple typing is a composite |
| lineage claim | composition trace and inherited Loss constrain the current reconstruction | reversal of prior compression or recovery of irrecoverable alternatives |
| map claim | selected components and relations reconstruct the same bounded composite | a parts list is sufficient or arrows prove causality automatically |
| role claim | one element is constitutive, modulating, replaceable, compensatory, or incidental for a declared claim | universal ontology, permanent rank, person rank, or causal sufficiency |
| weighting claim | declared operator occurrences carry different relative loads by function, dimension, time, and source | operator fusion, dependency change, numerical strength, authority, or target function |

Primary site: [§§22.1–22.4](../01_blocks/03_part_ii_sub.md#chapter-22-decomposing-composite-structures).

## Chapter 22 WP2 Claim-Type Return

| Claim type | Required declaration | Prohibited inflation | Primary site |
|---|---|---|---|
| modulating-profile claim | source composite, function, dimension, relation carrier, scope, source support, counterpressure, expected difference | operator/composite/person type, target function, synthetic score | [§22.5](../01_blocks/03_part_ii_sub.md#22-5-modulating-profiles) |
| distributed-function claim | distributed elements, same-composite relation, coordination/dependency, common function, partial-failure effect, support and uncertainty | aggregation, co-presence, silent macro-composition | [§22.6](../01_blocks/03_part_ii_sub.md#22-6-distributed-function) |
| redundancy claim | bounded function overlap, held-constant conditions, removal pressure, source-supported alternatives | universal necessity, sufficiency, causal priority | [§22.7](../01_blocks/03_part_ii_sub.md#22-7-redundant-and-substitutable-components) |
| substitution claim | current/substitute carriers, preserved function, transition conditions, changed cost/burden/access/timing, Loss | equivalence, irrelevance, lossless replacement | [§22.7](../01_blocks/03_part_ii_sub.md#22-7-redundant-and-substitutable-components) |
| threshold claim | function or identity at risk, relation set, supported change sequence, claim-changing difference, source ceiling | universal percentage, resilience or operator score | [§22.7](../01_blocks/03_part_ii_sub.md#22-7-redundant-and-substitutable-components) |
| internal-conflict claim | conflicting relations, incompatibility, common composite, scope, mechanism, support, unresolved structure | automatic destruction, health, legitimacy, sanction | [§22.8](../01_blocks/03_part_ii_sub.md#22-8-internal-conflict) |

## Chapter 22 WP3 Claim-Type Return

| Claim | Required burden | Not implied |
|---|---|---|
| Composite-stability claim | stability object, interval, changing carriers, preserving relations, mechanism, counterpressure, defeat condition | homogeneity, resilience, legitimacy, equal burden |
| Non-fragmenting decomposition claim | same reference, boundary, components plus relations, macrofunction test, inherited/new Loss | maximal detail, anti-macro privilege |
| Failed composite-decomposition claim | identified operation failure on same claim | absence of all useful findings |
| Non-Capture claim | legitimate source/question but no stable finer map within ceiling | prior composite claim rescued |
| Chapter-23 handoff claim | bounded temporal question and retained source/record trace | event/non-event decomposition already completed |

## Chapter 22 WP4 Claim Boundary Return

Chapter 22 permits bounded claims about composite identity, boundary, composition lineage, internal relations, component roles, operator weighting, source-side profiles, distributed function, redundancy, substitution, conflict, stability, and source-function revision. It does not authorize ultimate-part ontology, universal causal rank, numerical operator strength, person profile, legitimacy or sanction judgment, event/Path completion, or contextual target function without their own warranted operations.

Primary site: [Chapter-22 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-22-completion-boundary).

## Chapter 23 Preparation Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| Event-source-entry claim | bounded reference, Frame, temporal scope, praxis-relevant change, source basis | timestamp or label treated as Event |
| Event-boundary claim | beginning, completion, contextual margins, internal phases, rival boundaries | smallest timestamp or retrospective convenience |
| Extended-Event claim | phase continuity, same reference, completion relation, interruption status | duration alone |
| Event-Cluster claim | local Events, binding relation, common bounded claim, operation classification | co-presence or silent COMPOSE |
| Event-Inflation claim | micro-event multiplication without changed praxis reconstruction | detail count as proof |
| Non-Event claim | expected structure, warranted expectation Frame, bounded window, non-realization, praxis difference | missing record or mere absence |
| Non-Event-preservation claim | positive sub-events related to the same higher-level non-realization | internal activity treated as realization |
| delay-structure claim | source-supported postponement, role, capacity, dependency, threshold, and timing relations | intention or obstruction inferred from duration |
| repeated-non-decision claim | repeated deferrals or failed closure under one bounded source reference | person indecisiveness or moral rank |
| internal-temporal-order claim | sequence, overlap, partial order, interruption, threshold, closure, multiple clocks | timestamp list |
| categorical-revision claim | same-reference finer evidence and declared source-function effect | category immunity or unmarked replacement |

Preparation control: [Chapter 23 Preparation Record](Chapter_23_Preparation_Record.md).

## Chapter 23 WP1 Temporal Claim Types

| Claim type | Minimum burden | Must not inherit |
|---|---|---|
| Event-like source-entry claim | bounded reference, category, Frame, coarse boundary, praxis-relevant change, source basis, compression, decomposition question | Event status from timestamp presence |
| Event-boundary claim | beginning, completion, contextual margins, interruption/resumption status, rival boundaries | smallest timestamp as true boundary |
| Extended-Event claim | related phases, continuity/resumption, common completion criterion, split counterpressure | duration, sequence, or common topic alone |
| Event-Cluster claim | local Events, cluster relation, common object or transition environment, cluster boundary, failure condition | silent selection of independent Events |
| Event-unit claim | claim, Frame, source, transition, and reference relevance | observation-tool granularity |
| Event-category-revision claim | same-reference finer evidence and explicit preservation, extension, clustering, splitting, rejection, or underdetermination | category immunity or automatic finer truth |

Primary sites: [§§23.1–23.4](../01_blocks/03_part_ii_sub.md#23-1-event-decomposition).

## Chapter 23 WP2 Temporal Claim Types

| Claim type | Minimum burden | Must not inherit |
|---|---|---|
| Non-Event source-entry claim | expected structure, warranted Expectation Frame, bounded window/completion condition, supported non-realization, praxis difference, Source Ceiling | `Λ` from record absence or retrospective importance |
| Non-Event-preservation claim | same expectation and window plus supported relation of positive sub-events to non-realization | dissolution or preservation from positive-event count alone |
| Delay-structure claim | delayed structure, comparison condition, mechanisms, roles, thresholds, dependencies, effects, uncertainty | intention, obstruction, guilt, or person property from duration |
| Repeated-non-decision claim | related decision opportunities, windows, authority/binding conditions, category alternatives, reference continuity | one continuing Non-Event or PATH status from repetition alone |
| Absent-binding claim | required binding occurrence, capable role/configuration, activation conditions, practical effect, uncertainty | person identity, maturity, moral rank, or operator decomposition |

Primary sites: [§§23.5–23.8](../01_blocks/03_part_ii_sub.md#23-5-non-event-decomposition).



## Chapter 23 WP3 Temporal Claim Types

| Claim | Required support | Prohibited substitution |
| --- | --- | --- |
| Internal temporal order | supported relation among phases, thresholds, interruptions, or completion conditions | timestamp adjacency as dependency |
| Multiple-clock relation | source support for each clock and their bounded relation | precision in one clock as evidence for another |
| Temporal drift/no-gain | finer distinction fails to change warranted praxis reconstruction | detail volume as purchase |
| Event/Non-Event category effect | source boundary, expectation, realization, and category evidence | local category as Output Class |
| Temporal Non-Capture | legitimate question plus unresolved rival maps under Source Ceiling | rescue of coarse claim or invented compromise chronology |

Primary sites: [§§23.9–23.11](../01_blocks/03_part_ii_sub.md#23-9-internal-temporal-order).


## Chapter 23 Provisional-Lock Claim Boundary

| Claim family | Locked burden | Forbidden inference |
| --- | --- | --- |
| Event / Extended Event / Event Cluster | bounded reference, boundary, completion, phases, and relation support | timestamp density as Event truth |
| Non-Event | warranted expectation, bounded window, supported non-realization, praxis difference | missing record or mere absence as `Λ` |
| Delay / repeated non-decision | supported mechanism, roles, thresholds, dependencies, and windows | intention, guilt, person property, or legitimacy |
| Internal temporal order | supported sequence, dependency, overlap, interruption, threshold, and clock relations | chronology precision as causality or truth priority |
| Temporal output | four result axes plus canonical class | local category or effect as Output Class |

Primary site: [Chapter 23](../01_blocks/03_part_ii_sub.md#23-decomposing-events-non-events-and-internal-temporal-structures).

## Chapter 24 Preparation Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| PATH-source-entry claim | bounded source reference/category, boundary, selection/formation rule, coarser function, inherited Loss | raw chronology or label treated as Path |
| Same-Path decomposition claim | compatible reference/boundary, preserved lineage, relational finer map, reconstructible coarse function | same dates or label |
| subpath claim | bounded internal transitions and relation to coarser Path | arbitrary fragment |
| transition-cluster claim | intermediate configurations, transition relations, changed coarse claim | expanded event list |
| turning-point claim | component transitions, changed alternatives/costs/bindings, historical effect, rival candidates | retrospective salience |
| branch-reconstruction claim | source-supported historical availability, status, mechanism, and window | imaginable alternative |
| internal-Frame-change claim | before/after Frames, continuity carriers, changed access/function | source replacement ignored |
| competing-continuation claim | supported corridors and unequal accessibility at analytical cut | prediction or recommendation |
| compression-debt claim | inherited missing/irrecoverable distinctions relevant to current claim | detail volume as recovery |
| Path-Dependence-load claim | source-supported historical profiles and present-condition challenge | hidden substance or score |
| rival-PATH claim | materially different selection, periodization, boundary, Frame, or formation | unmarked DECOMPOSE |

Preparation control: [Chapter 24 Preparation Record](Chapter_24_Preparation_Record.md).

## Chapter 24 WP1 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| PATH-source-entry claim | reference, category, Frame, boundary, coarse function, original selection/formation, inherited Loss, question | raw chronology or retained label |
| formation-lineage claim | inherited selections, recovered/new detail, new analytical selections, continuing Loss | richer account treated as untouched complete history |
| Path-decomposition-reason claim | bounded insufficiency, expected PraxisPurchase, evidence and no-gain condition | more records or timestamps |
| subpath claim | local source/end, transitions, bounded function, relation to coarse Path, support and counterpressure | arbitrary interval, theme, or medium |
| subpath-coherence claim | constitutive/modifying/blocking/compensating/counter-direction relation to same source object | bag of independent courses |
| transition-cluster claim | coarse source/target configurations, intermediates, supported relations, effect and uncertainty | expanded Event list |
| Same-Path operation claim | compatible reference and formation lineage under finer opening | same name or endpoint |
| rival-Path operation claim | materially new selection, periodization, boundary, or macro-formation | hidden inside `DECOMPOSE` |

Primary sites: [§§24.1–24.4](../01_blocks/03_part_ii_sub.md#chapter-24-decomposing-paths-and-trajectories).

## Chapter 24 WP2 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| turning-point claim | component transition, source/target configurations, historical effects, operative window, rivals, reduction condition | retrospective salience or endpoint dependence alone |
| branch-status claim | source, availability window, roles/conditions, mechanism, later reachability, residue, uncertainty | imaginable option or label alone |
| counterfactual-branch claim | then-available conditions, mechanism, explicit uncertainty, bounded sensitivity | later knowledge, idealized option, guaranteed success, verdict |
| internal-Frame-change claim | earlier/later Frames, connecting relation, changed relevance/access, persisted structures, continuity test | same institution or automatic source replacement |
| competing-continuation claim | current configuration, supported routes, entry conditions, unequal accessibility/load, horizon, revision | probability, prediction, legitimacy, recommendation |
| non-linearity claim | supported reversals, interruptions, parallelism, repair, counter-trends, dimension-specific effect | narrative smoothing or automatic trajectory rejection |

Primary sites: [§§24.5–24.8](../01_blocks/03_part_ii_sub.md#24-5-turning-points).

## Chapter 24 WP3 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| inherited-Loss claim | original selection/formation and canonical five-part Loss separated from current operation | treating newly available detail as original recovery |
| compression-debt claim | unresolved constitutive traceability burden and claim effect | score, primitive, person or institutional ranking |
| Path-Dependence-load claim | analytical cut, dimension, historical carrier, interval, present effect, sufficiency challenge, counterevidence, Loss | duration, profile count, determinism, operator fusion |
| Same-Path claim | historical referent, boundary, selection/formation lineage, constitutive transitions, coarse function, Loss | shared dates, archive, endpoint, institution, or label |
| rival-PATH claim | materially different source selection, boundary, formation, macro-object, referent, or PATH question plus separate `COMPOSE` Record | hiding new formation inside `DECOMPOSE` |
| Chapter-24 result claim | four result axes, Loss, Stop/Non-Capture, claim-specific class | compensation across axes or inherited Output Class |
| failed-decomposition claim | completed unsupported or incoherent finer attempt with preserved weaker findings | claim rescue through more detail |

Primary sites: [§§24.9–24.12](../01_blocks/03_part_ii_sub.md#24-9-irrecoverable-compression).

## Chapter 24 Provisional-Lock Claim Return

Chapter 24 controls source-entry, formation-lineage, subpath, transition-cluster, turning-point, branch-availability, counterfactual, Frame-continuity, continuation, Loss, Same-Path/rival-PATH, and Path-Dependence-load claims. Each remains bounded by reference, temporal window, source support, granularity, dimension, Loss, counterpressure, and Claim Ceiling. None authorizes causal sufficiency, prediction, recommendation, person typing, legitimacy, or authority inheritance.

## Chapter 25 Preparation Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| Resolution-Gain claim | coarse/finer comparison, source-supported distinction, changed praxis dimension, changed warranted statement | more detail or complexity |
| Resolution-Neutral claim | valid supported comparison, same tested claim, no changed warranted reconstruction | absence of evidence or unsupported detail |
| Resolution-Drift claim | complexity/support/discrimination comparison, source-object and coarser-function status | source limitation alone |
| Resolution-Escape claim | original claim, counterpressure, granularity change, unanswered burden, retroactive-rescue test | warranted revision conflated with escape |
| Detail-without-Purchase claim | explicit tested claim and unchanged relevant dimensions | universal irrelevance of detail |
| Source-Overreach claim | source precision compared with asserted structural precision | plausible model treated as established |
| Calibration-Loss claim | moving thresholds, incomparable rivals, counterevidence elasticity, revision failure | honest open threshold |
| Decomposition-Fatigue claim | completed current-claim test and no additional structural load | analyst state or permanent undecomposability |
| Mandatory-Stop claim | binding floor, source, coherence, calibration, anti-immunization, or ceiling trigger | stop as mere inconvenience |
| re-entry claim | new source, claim, Frame, comparison basis, relation map, or threshold | prior failure erased |

Preparation control: [Chapter 25 Preparation Record](Chapter_25_Preparation_Record.md).

## Chapter 25 WP1 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| resolution-comparison entry | same tested claim, coarse and finer reconstructions, comparison basis, support, dimensions, change condition | shared topic or detail count |
| Resolution Gain claim | exact changed warranted statement and supporting distinction/relation | “more detail” or stronger wording |
| Resolution Neutrality claim | valid supported comparison and explicit no-change across tested dimensions | unsupported refinement or missing evidence |
| Resolution Drift claim | complexity/inferential growth plus weakened discrimination, relation support, or source coherence | dislike of complexity or display medium |
| Resolution Escape claim | prior burden, coordinate change, unanswered burden, attempted claim rescue | any legitimate refinement after counterpressure |
| warranted-revision claim | prior disposition, counterpressure, new bounded claim, new basis, independent test | retroactive rescue or authority inheritance |

Primary site: [Chapter 25 WP1](../01_blocks/03_part_ii_sub.md#chapter-25-resolution-gain-neutrality-drift-and-escape).

## Chapter 25 WP2 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| purchase claim | tested claim, removable distinction, changed or unchanged warranted dimensions | detail count treated as purchase |
| unsupported-refinement claim | separate component, relation, and claim support status | unsupported no-change called neutrality |
| coarser-function claim | explicit relation from finer components to preserved, distributed, revised, rejected, or underdetermined source function | parts inventory treated as completed decomposition |
| relation-support claim | relata, relation form, source basis, Frame, temporal scope, support status, claim consequence, rivals | graph edge or adjacency treated as historical relation |
| Source-Overreach claim | source-supported precision boundary and the exact excess claim | model or visual precision treated as evidence |
| calibration claim | tested threshold, basis, uncertainty, rival conditions, revision rule, prior disposition | threshold moved after adverse evidence without trace |
| bounded monitoring claim | declared runtime signal, invariant, Stop trigger, and re-entry condition | universal termination, truth, motive, legitimacy, or authority decision |

Primary site: [Chapter 25 WP2](../01_blocks/03_part_ii_sub.md#25-5-detail-without-purchase).

## Chapter 25 WP3 Claim-Axis Return

| Claim position | Required treatment | Prohibited collapse |
|---|---|---|
| local resolution family | name gain, neutral, drift, escape, unsupported, or non_capture | canonical Output Class |
| source-function effect | state confirmed, refined, internally differentiated, partially preserved, rejected, or underdetermined as warranted | local resolution result |
| prior claim disposition | preserve, reduce, reject, or leave unresolved | later claim success |
| canonical Output Class | select exactly one class after all gates | local classification alone |
| re-entry claim | declare materially new basis and new record/segment | erasure of earlier Stop or failure |

## Chapter 25 Provisional-Lock Claim Return

Chapter 25 controls coarse/finer comparison, changed-claim, no-change, purchase, coarser-function, support, source-overreach, calibration, fatigue, local-resolution, Stop, Non-Capture, and re-entry claims. Each remains bounded by the tested proposition, source and relation support, Frame, granularity, Loss, prior disposition, counterpressure, and Claim Ceiling. None authorizes universal halting, automatic semantic truth, person typing, legitimacy, prediction, sanction, or authority inheritance.

## Chapter 26 Preparation Claim Types

| Claim | Required support | Must remain distinct from |
|---|---|---|
| internal-constitution claim | same-reference source support, granularity relation, components and relations, coarser-function trace | target-function claim |
| contextual-target-function claim | origin-typed source object, declared target context, source-traceable function, boundedness, rival pressure | origin type and source function |
| recontextualization claim | changed Frame, question, perspective, or presentation context | automatic `DECOMPOSE` or `PROJECT_AS` occurrence |
| dual-operation claim | two explicit operation occurrences with separate claims, Records, Loss, and results | mixed operation record |
| operation-boundary claim | declared analysis question, internal-structure test, target-function test, reasons, unresolved structure | canonical Output Class |

Preparation control: [Chapter 26 Preparation Record](Chapter_26_Preparation_Record.md).

## Chapter 26 WP1 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| operation-boundary entry | source object, origin type, source function, Frame, granularity, question, context/function proposal, uncertainty, Loss | wording, label, or shared evidence base |
| internal-constitution claim | finer structures and relations traceable to the same source object and source function | component list or operator-type decomposition |
| target-function candidate | retained origin-typed object, declared target context, bounded function, source-traceable features, counterpressure | analogy, interface role, usefulness, or new label |
| granularity-change claim | declared source/target granularity and changed distinction set | target-context change inferred from finer detail |
| origin-type-preservation claim | explicit origin type retained while target function remains contextual | target function renamed as a new source type |
| operation-candidate claim | reasons why the attempted claim is DECOMPOSE, PROJECT_AS, recontextualization, or dual-operation pressure | automatic classification from vocabulary |

Primary site: [Chapter 26 WP1](../01_blocks/03_part_ii_sub.md#chapter-26-the-boundary-between-sub-and-retype).

## Chapter 26 WP2 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| trajectory operation-comparison claim | same origin-typed source, separate SUB and target-function questions, separate outputs and Loss | shared source or evidence treated as one occurrence |
| bounded target-context claim | user/task, conditions, relevant and excluded source dimensions, failure boundary | audience, screen, Reader, or later date alone |
| source-traceable target-function claim | source features plus context-specific functional difference and counterpressure | usefulness, resemblance, analyst intention, or source-feature presence alone |
| Attractor-function candidate | preserved source origin type, declared context, specified attraction/stabilization relation | recurrence inside an Attractor occurrence |
| recontextualization claim | changed Frame, perspective, question, audience, or presentation with no transformation claim yet | automatic DECOMPOSE or PROJECT_AS routing |
| misclassification finding | explicit mismatch between operative claim and apparent vocabulary or label | classification from headings, nouns, or interface layout |

Primary site: [Chapter 26 WP2](../01_blocks/03_part_ii_sub.md#26-5-trajectory-decomposition-and-projection).

## Chapter 26 WP3 Claim-Axis Return

| Claim position | Required treatment | Prohibited collapse |
|---|---|---|
| internal-constitution claim | separate DECOMPOSE occurrence and source-function effect | contextual target function |
| contextual target-function claim | separate PROJECT_AS occurrence with preserved origin type | source type or internal map |
| local boundary finding | use for segmentation and routing | canonical Output Class |
| prior source-claim disposition | preserve across operation changes | later projection success |
| dual-operation chain | declare order, records, handoff, Loss, and independent results | mixed occurrence |
| canonical Output Class | exactly one per Record after all gates | operation candidate alone |

## Chapter 26 Provisional-Lock Claim Return

Chapter 26 controls internal-constitution, contextual-target-function, recontextualization, operation-candidate, dual-operation, chain-order, invalid-collapse, result-axis, Stop, and Non-Capture claims. Each remains bounded by source object, origin type, source function, Frame, granularity, target context, target function, relation support, prior disposition, Loss, and Claim Ceiling. None authorizes origin-type replacement, mixed-operation records, semantic automation, person typing, legitimacy, recommendation, sanction, or authority inheritance.

## Chapter 27 Preparation — SUB Boundary Claim Family

A complete local SUB-boundary claim must identify:

- the source Transformation Record and tested source claim;
- source object, source type, and source function;
- source and target granularity;
- expected and actual additional praxis difference;
- lower- and upper-boundary status;
- Source-Ceiling status;
- component and relation support;
- component-sensitivity findings;
- source-reference, coarser-function, and type-integrity status;
- Stop or re-entry status;
- unresolved structure and canonical Loss;
- separate local result, function effect, prior disposition, and Output Class.

A component-sensitivity claim is bounded to the declared relation map and does not establish universal causality. A source-type claim may remain identifiable while its source-function claim is reduced or rejected.

Preparation control: [Chapter 27 Preparation Record](Chapter_27_Preparation_Record.md).

## Chapter 27 WP1 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| SUB-boundary entry | source object, tested claim/function, source and target granularity, expected difference, source reference, coarser-function pressure, uncertainty, Loss | “more structure” as its own justification |
| lower-boundary claim | supported or possible finer distinction with no changed warranted praxis dimension | falsehood inferred from no purchase |
| Resolution-without-Purchase claim | supported finer map, valid comparison, unchanged claim | unsupported detail relabeled as neutral |
| upper-boundary claim | finer map loses source-reference, relation, or coarser-function anchoring | arbitrary amount of detail treated as the boundary |
| fragmentation claim | supported parts without defensible relation to the source object or one another | component enumeration treated as reconstruction |
| source-reference claim | stable bounded reference or explicit revision/splitting/rejection | same label or repository location |

Primary site: [Chapter 27 WP1](../01_blocks/03_part_ii_sub.md#chapter-27-sub-boundary-conditions).

## Chapter 27 WP2 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| Source-Ceiling claim | bounded source, claim, Frame, granularity, relation type, and finest responsible precision | coherent model or complete graph treated as evidence |
| support-status claim | exact component/relation/function question and local source basis | status treated as universal score or Output Class |
| component-sensitivity claim | bounded component, supported relation map, variation, function effect, assumptions, Loss | local difference treated as universal causality |
| coarser-function traceability claim | explicit translation from material parts/relations to source-function effect | detailed parts list treated as reconstruction |
| type-preservation claim | operator type, occurrence, source-object type claim, and function claim kept distinct | operator type decomposed or initial label immunized |
| type-revision claim | source-supported confirmation, restriction, rival description, rejection, or underdetermination | granularity change erases prior failed typing |

Primary site: [Chapter 27 WP2](../01_blocks/03_part_ii_sub.md#27-5-source-ceiling).

## Chapter 27 WP3 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| resolution-comparison claim | tested claim, coarse/fine basis, changed dimensions, support, Loss | finer treated as automatically better |
| SUB Stop claim | declared bounded continuation condition and preserved findings/dispositions | Stop treated as proof of no finer structure |
| Claim-Reduction claim | exact surviving weaker finding and excluded unsupported remainder | confidence wording used to retain stronger claim |
| SUB Non-Capture claim | legitimate question, bounded source object, unresolved rival structure, preserved Loss | coarse claim restored or rivals averaged |
| SUB admissibility claim | all eight conjunctive gates | detail or formal elegance compensates for failed gate |
| re-entry claim | prior Record, materially new basis, new claim, success/failure/Stop conditions | more compute or visual detail treated as new evidence |

Primary site: [Chapter 27 WP3](../01_blocks/03_part_ii_sub.md#27-9-no-privilege-of-fine-resolution).

## Chapter 27 Provisional-Lock Claim Bundle

| Claim | Required burden | Prohibited shortcut |
|---|---|---|
| bounded SUB admissibility | all eight conjunctive gates | compensatory detail or score |
| Source-Ceiling claim | claim-specific source precision and excluded overreach | model completion |
| component-sensitivity claim | bounded variation, relation map, source function, uncertainty | universal causality |
| type-revision claim | occurrence-level evidence and explicit disposition | forced preservation |
| Stop/Reduction/Non-Capture claim | exact preserved findings, disposition, Loss, continuation boundary | coarse-claim rescue |

Primary site: [Chapter 27 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-27-completion-boundary).

## Chapter 28 Preparation — SUB Case Claim Family

A Chapter-28 case claim must bind:

- case identity and class;
- governing claim, scope, and Claim Ceiling;
- source Record, object, origin type, Frame, and granularity;
- decomposition question and expected additional praxis difference;
- source basis, components, and component relations;
- source-reference, coarser-function, type-integrity, and resolution findings;
- operation-boundary and chain status;
- Counterfactual Sensitivity, Loss, alternatives, uncertainty, and surviving weaker findings;
- local audit, Stop/Non-Capture status, and canonical Output-Class mapping.

A case narrative is not a source claim by itself. A local source-function or resolution description is not a canonical Output Class. A confusion case may contain several candidate claims but requires separate Records for every executed operation.

Preparation control: [Chapter 28 Preparation Record](Chapter_28_Preparation_Record.md).

## Chapter 28 WP1 — Instantiated Positive SUB Claims

The WP1 corpus instantiates six bounded `DECOMPOSE` claims: Frame-occurrence production, Attractor-occurrence maintenance, distributed Asymmetry, structured Non-Event, same-reference Trajectory decomposition, and Resolution Gain. In every case the current finer claim is separately testable and the broader prior claim is preserved as history rather than silently upgraded.

```text
resolution_gain
≠ canonical Output Class automatically
```

## Chapter 28 WP2 — Countercase and Confusion Claims

WP2 instantiates bounded continuation, reduction, failed-operation, failed-reconstruction, anti-escape, local-versus-macro, DECOMPOSE/PROJECT_AS-separation, and DECOMPOSE/COMPOSE-separation claims. Each new operation candidate remains a separately testable claim.

## Chapter 28 WP3 — Analogy, Modulator, Audit, and Lock-Readiness Claims

WP3 instantiates bounded analogy-only, modulator-with-type-reduction, integrated Local-Audit, output-mapping, Loss/alternatives, Stop/Non-Capture, chain-separation, and lock-readiness claims. Readiness is not a lock and creates no target function or authority.

## Part II — SUB Provisional-Lock Claim Boundary

The locked SUB claim type is a bounded reconstruction claim about the internal constitution of the same eligible source object. It may confirm, refine, differentiate, partially preserve, reduce, reject, or leave underdetermined the source-function or source-type claim.

It does not include a contextual target-function claim. Any such claim enters Chapter 29 and RETYPE only as a separate `PROJECT_AS` occurrence with its own context, source trace, Loss, result, and Claim Ceiling.

Primary site: [Part-II SUB lock boundary](../01_blocks/03_part_ii_sub.md#part-ii-sub-provisional-lock-boundary).

## Chapter 29 Preparation — Typed RETYPE Claim

The governing Chapter-29 claim has the bounded form:

```text
Within target context C,
source object X,
while retaining origin type T,
performs bounded function F.
```

The claim must bind source identity, origin type, target context, target function, source-traceable functional relation, expected target-context difference, validity scope, Claim Ceiling, Loss, alternatives, counterpressure, Stop, and Non-Capture. It is not a claim about what X is intrinsically or universally.

```text
target function claim
≠ origin-type claim
≠ operator-identity claim
≠ authority claim
```

Preparation control: [Chapter 29 Preparation Record](Chapter_29_Preparation_Record.md).


## Chapter 29 WP1 Canonical Claim Types

| Claim type | Minimum burden | Prohibited shortcut |
|---|---|---|
| typed RETYPE claim | explicit source object `X`, origin type `T`, target context `C`, and candidate function `F` | target label treated as its own warrant |
| source-entry claim | identifiable source object, source Record, reference, origin type, prior disposition, uncertainty, and inherited Loss | target context retroactively manufactures the source object |
| target-context entry | bounded scene or object, Frame where relevant, relative level, analytical purpose, and immediate Claim Ceiling | “macro,” “system,” or later date as sufficient context |
| origin-type-preservation claim | source type and Record remain visible; function is separately marked; revision remains source-side | function language replaces or immunizes origin typing |
| target-function candidate | specific relational target-side difference and a no-function alternative | relevance, usefulness, resemblance, centrality, or frequency |
| no-additional-function contrast | same source object, different target context, unchanged warranted target reconstruction | source validity treated as automatic target function |

WP1 claim entry does not establish Functional Continuity, execute `PROJECT_AS`, or select a final Output Class.

Primary site: [Chapter 29 WP1](../01_blocks/04_part_iii_retype.md#29-4-target-function).

## Chapter 29 WP2 Canonical Claim Types

| Claim | Required support | What it does not establish |
|---|---|---|
| source-object-integrity claim | retained reference, origin type, history, constitutive relations, prior limits, uncertainty, and Loss | complete reproduction, losslessness, or target-function success |
| load-bearing-source claim | feature-specific relation plus bounded alteration pressure | universal necessity, sole causality, or source-feature ranking |
| Functional-Continuity candidate | specific function, source-to-context relation, target-side difference, and bounded source-change sensitivity | completed `PROJECT_AS`, final Output Class, or cross-context validity |
| Contextual-Boundedness claim | scene, roles, relative level, duration, validity scope, purpose, Claim Ceiling, and Loss | recommendation, sanction, legitimacy, or authority inheritance |
| elasticity finding | materially opposite source structures with invariant target label | automatic final class selection; later routing remains required |

Primary site: [Chapter 29 WP2 completion boundary](../01_blocks/04_part_iii_retype.md#29-8-contextual-boundedness).

## Chapter 29 WP3 Claim and Result Separation

A RETYPE claim keeps four axes distinct:

| Axis | Bounded claim |
|---|---|
| Source integrity | whether X remains identifiable under T with source history, limits, and Loss |
| Target-function effect | whether X produces the specific warranted target-side difference in C |
| Prior disposition | which earlier source or operation result enters the claim |
| Canonical Output Class | the final closed-class mapping after complete operation audit |

No axis automatically determines another. A no-projection result can preserve a valid source object; a failed target function need not fail the source claim; a new context or function creates a new claim occurrence without erasing earlier results.

Primary site: [§29.10](../01_blocks/04_part_iii_retype.md#29-10-functional-projection-as-a-typed-claim).

## Chapter 29 Lock and Chapter 30 Claim Architecture

| Claim or result layer | Required burden | Must remain distinct from |
|---|---|---|
| source claim | source object, origin type, reference, coordinates, prior disposition, inherited Loss | target-function success |
| target-function claim | declared context, function, expected difference, trace, sensitivity, scope | source identity and operator type |
| local `PROJECT_AS` result | operation-specific finding for one delimited claim | canonical Output Class |
| canonical mapping | exactly one of ten classes after full routing | local phrase, sensitivity result, or failure code |
| chapter-level method result | `admissible_but_provisional` for locked Chapter 29 | concrete projection result |

Chapter 30 preparation preserves all five layers and prohibits claim or authority inheritance.

## Chapter 30 WP1 Claim Architecture

| Layer | WP1 declaration | Not established by WP1 |
|---|---|---|
| Source object | independently identifiable `X_g` and source reference | target-function warrant |
| Source typing | visible `T_o` | immutable or exclusive source truth |
| Target entry | preliminary `C_t`, candidate `F_t`, and `g'` | complete target declaration or validity scope |
| Operation controls | pending `J`, current/inherited `L`, pending `V` | operation execution or result |
| Prior status | prior disposition, uncertainty, inherited Loss retained | source-claim upgrade or repair |

The arrow in the minimal signature expresses claim direction, not causality, necessity, or automatic transformation.

Primary site: [§§30.1–30.4](../01_blocks/04_part_iii_retype.md#chapter-30-project-as-signature-context-and-validity-scope).

## Chapter 30 WP2 Claim Controls

| Claim position | Permitted WP2 statement | Not established |
|---|---|---|
| target declaration | a bounded target object/scene and candidate contextual function are declared | actual function warrant |
| projection justification | analytical need, candidate carrier, rival pressure, and expected difference are stated | superiority of the preferred projection |
| Constitutive Source Trace | candidate load-bearing and modulating relations are traceable to sources | causal sufficiency or complete source recovery |
| Counterfactual Sensitivity | bounded source variations and expected claim effects are specified | causal proof, score, or canonical class |

WP2 produces a testable claim packet. It does not execute `PROJECT_AS`, establish the target function, select a sensitivity result, or map an Output Class.

## Chapter 30 WP3 Claim Separation

| Position | Question | May remain independent? |
| --- | --- | --- |
| source-object status | Does the source remain identifiable? | yes |
| origin-type status | How does source typing stand? | yes; not immunized |
| prior disposition | What source-side result is inherited? | yes; never erased by projection |
| local `PROJECT_AS` result | What happened to this bounded target-function claim? | yes |
| canonical Output Class | Which system-wide class maps the executed claim? | yes; exactly one when selected |

```text
valid source + failed projection
≠ invalid source

no-projection
≠ failed_transformation
≠ non_capture by definition
```

Primary site: [Projection Results](../01_blocks/04_part_iii_retype.md#30-12-projection-results).

\n## Chapter 30 Lock and Chapter 31 Family-Claim Discipline\n\n| Claim position | Required status | Prohibited collapse |\n|---|---|---|\n| generic `PROJECT_AS` method | provisionally locked chapter-level method | method completeness into occurrence success |\n| source Trajectory | prior PATH-established claim | family usefulness into source repair |\n| target frame-function | new context-bound claim | origin-type or `□` identity |\n| historical load | constitutive source-to-target relation | duration, salience, or citation alone |\n| family result | independently audited operation occurrence | inherited Chapter-30 result |\n\nPrimary sites: [Chapter 30 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-30-completion-boundary) and [Chapter 31 Preparation Record](Chapter_31_Preparation_Record.md).\n


## Chapter 31 WP1 Claim Architecture

| Claim position | WP1 status | Not established |
|---|---|---|
| source claim | prior PATH Trajectory retained | target-function warrant |
| source selection | declared independent of target fit | substantive independence automatically proven |
| target claim | later configuration and present conditions declared | historical contribution established |
| function claim | concrete bounded frame-function candidate | `□` identity, determinism, or permanent transfer |
| evidence claim | source, target, and retrospective layers separated | evidence interchangeability |
| contrast claim | same source retained across `Y/Z` | positive or no-projection result selected |

Primary site: [Chapter 31 WP1](../01_blocks/04_part_iii_retype.md#chapter-31-trajectory-as-frame-function).


## Chapter 31 WP2 Historical-Load Claim Architecture

| Claim position | Required WP2 statement | Prohibited inference |
|---|---|---|
| source-object warrant | `X` remains a PATH-established Trajectory | valid source automatically performs a target function |
| Historical-Load claim | named source feature is traceably carried, transmitted, or reactivated into a bounded target difference | duration, salience, remembrance, or documentation proves load |
| carrier role | feature is load-bearing, modulating, or unresolved for this claim | every foregrounded feature is constitutive |
| conditioning claim | named praxis dimension, role, level, and time window are affected | necessity, prediction, or causal monopoly |
| multiple-source claim | present and historical rivals remain visible | historical priority or narrative coherence establishes dominance |
| relative-load statement | qualitative relation among supported contributions | percentage, score, ranking, or canonical Output Class |

WP2 establishes this claim architecture without deciding the concrete `Y/Z` result.

Primary site: [Chapter 31 WP2](../01_blocks/04_part_iii_retype.md#31-5-historical-load).


## Chapter 31 WP3 Claim Separation

| Claim | Required support | Does not inherit |
|---|---|---|
| rhetorical-history rejection | missing or failed source/trace/target/sensitivity burdens | source-Trajectory invalidity |
| carrier-sensitivity claim | bounded source variation and target-change reasoning | causal necessity or quantified share |
| same-end pressure claim | supported alternative histories and declared target granularity | identical paths or universal historical irrelevance |
| competing frame-function claim | separate target difference, trace, scope, Loss, and sensitivity | another function's result |
| background relevance claim | contextual usefulness without distinct target work | `PROJECT_AS` success |
| no-projection claim | absence of warranted distinct function for the delimited claim | analytical failure or source erasure |
| failed frame-projection claim | complete family burdens not satisfied | automatic PATH revision |

Primary site: [Chapter 31 WP3](../01_blocks/04_part_iii_retype.md#31-8-rhetorical-history-versus-frame-function).

## Chapter 31 Lock and Chapter 32 Preparation — Claim Separation

| Claim position | Required warrant | Must remain separate from |
|---|---|---|
| source Trajectory claim | prior PATH/COMPOSE record, source boundaries, internal structure, disposition, Loss | Macro-Event function |
| Macro-Event boundary claim | supported start, end, constitutive phases, turning points, adjacent developments | period name or later outcome alone |
| target transition-function claim | wider target Frame and concrete changed possibilities or path structure | causal turning-point proof |
| compression claim | retained multi-resolution trace and exact five-part Loss | punctual occurrence |
| operation-chain claim | separate COMPOSE and PROJECT_AS occurrences and Records | automatic inheritance of result |
| canonical mapping claim | complete executed audit | local family vocabulary or chapter lock |

Primary site: [Chapter 32 Preparation Record](Chapter_32_Preparation_Record.md).


## Chapter 32 WP1 Claim Separation

| Claim position | Required support | What it does not establish |
|---|---|---|
| source Trajectory claim | prior PATH record and source-side boundaries | Macro-Event function |
| projection boundary claim | why this source scope is tested for the target function | target transition gain |
| target-placement claim | wider Path, before/after relation, preceding/following developments | causal turning point |
| Macro-Event function claim | concrete source-traceable transition difference | Event origin type or necessity |
| chapter-method claim | coherent family architecture and open failure routes | occurrence result or authority |

Primary site: [Chapter 32 WP1](../01_blocks/04_part_iii_retype.md#chapter-32-trajectory-as-macro-event).

## Chapter 32 WP2 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| internal-duration claim | source sequence, phases, turning points, uncertainty | target transition gain |
| heterogeneity claim | roles, subpaths, costs, asymmetries, Non-Events, consequences | unitary function or fragmentation automatically |
| phase-load claim | target-relative material sensitivity of phases/relations | score or causal share |
| event-function claim | concrete wider-Path praxis difference | causal turning point, necessity, monopoly |
| descriptive compression claim | bounded legibility gain | Macro-Event function |

Primary site: [Chapter 32 WP2](../01_blocks/04_part_iii_retype.md#32-5-internal-duration).


## Chapter 32 WP3 Claim Separation

| Claim position | Required support | Must remain separate from |
|---|---|---|
| punctualization-error claim | loss of constitutive duration, phase relations, heterogeneity, or origin-type integrity | one-node display alone |
| operation-chain claim | separate `COMPOSE` and `PROJECT_AS` occurrences, Records, Loss, and results | chain-level success shorthand |
| boundary-sensitivity claim | source-supported rival periodizations and changed target consequences | preference for dramatic fit |
| alternative-source claim | improved precision and traceability under a new source claim | silent source substitution |
| no-projection claim | no warranted distinct event function for the declared occurrence | source irrelevance or PATH failure |
| failed projection claim | indispensable family warrant absent or contradicted | automatic source-Trajectory invalidation |

Primary site: [Chapter 32 WP3](../01_blocks/04_part_iii_retype.md#32-8-punctualization-error).

## Chapter 33 Recurrent-Form Claim Stack

| Claim | Required warrant | Must remain separate from |
|---|---|---|
| source-Trajectory claims | prior PATH Records and evidence | recurrent-form and attractor-function result |
| comparability claim | declared Frame, granularity, role, time, evidence, and transition coordinates | mere shared label or count |
| recurrent-form source claim | constitutive recurrence across independently selected trajectories | retrospective motif |
| reproduction/path-influence claim | source-traceable friction, expectation, role, Non-Event, repair/exit, or alternative-cost work | causal sufficiency or determinism |
| target attractor-function claim | bounded later-path difference in declared context | Α identity or person/group type |
| local `PROJECT_AS` result | complete occurrence audit | canonical class or chapter-method result |
| canonical Output Class | post-audit routing of one delimited claim | automatic family label |

Primary site: [Chapter 33 Preparation Record](Chapter_33_Preparation_Record.md).


## Chapter 33 WP1 Claim Separation

| Claim position | Current WP1 status | Non-inheritance rule |
|---|---|---|
| individual Trajectory warrant | prior PATH records retained | one supported Trajectory does not warrant another |
| recurrent-form source warrant | candidate packet declared | multiple trajectories do not automatically form one source |
| comparability warrant | coordinates declared; result open | count or shared label does not establish comparability |
| Pattern Threshold | method declared; not adjudicated | formal completeness does not cross the threshold |
| dynamic attractor-function warrant | candidate in `D`; no result | source-form validity does not establish target function |
| no-projection in `E` | possible; not selected | negative route is not inherited from target contrast |
| local `PROJECT_AS` result | not selected | no automatic route |
| canonical Output Class | not selected | exactly one class only after complete audit |

Primary site: [Chapter 33 WP1](../01_blocks/04_part_iii_retype.md#chapter-33-recurrent-trajectory-form-as-attractor-function).

## Chapter 33 WP2 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| constitutive-repetition claim | source-supported recurrent relation, allowable variation, break conditions | target function |
| reproduction/path-influence claim | temporal availability and persistence/transmission/institutionalization/reactivation pathway | causal sufficiency or probability |
| Attractor-Load claim | concrete bounded later-path difference linked to source carriers | score, causal share, universal law |
| dynamic attractor-function claim | transition-form stabilization trace | static state stabilization |
| static attractor-function claim | configuration/range stabilization trace | recurrent transition form |

Primary site: [Chapter 33 WP2](../01_blocks/04_part_iii_retype.md#33-5-constitutive-repetition).

## Chapter 33 WP3 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| retrospective-motif claim | documented descriptive similarity | recurrent-form source or mechanism |
| recurrent-form source claim | target-blind comparable source set, constitutive relation, variation, break conditions | target-function effect |
| selection/missingness claim | accessible population, inclusion/exclusion, dependence, known omissions | complete population or unbiased sample |
| counterfactual-sensitivity claim | source-constrained phase/frame/role/cost/source/comparison/mechanism/target variation | causal necessity, probability, or prediction |
| rival-account claim | source- and target-specific comparative support | automatic defeat of the attractor claim |
| failed attractor-projection claim | located failure of source, mechanism, target work, or scope | automatic invalidation of each source Trajectory |

Primary site: [Chapter 33 WP3](../01_blocks/04_part_iii_retype.md#33-8-recurrent-form-versus-retrospective-similarity).

## Chapter 33 Lock and Chapter 34 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| source-component claim | independently warranted local occurrences | relational composite |
| source-composite claim | components plus relation topology and boundaries | target function |
| functional-formation claim | concrete target-context praxis difference carried by relations | operator identity or causality |
| emergent-function claim | composite-level visibility plus complete Source Trace | source-free novelty |
| chapter-method lock | complete family architecture and audit | pressure-object result |

## Chapter 34 WP1 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| component claim | independent occurrence warrant | relational composite |
| relation/composite claim | boundaries and relation map | higher-level function |
| target-context claim | level, Frame, granularity, time, roles, praxis dimensions | target effect |
| boundary-function claim | relationally produced target separation | □ identity or legitimacy |
| repeated-Non-Event attractor claim | expectation Frames, temporal relation, later-possibility effect | Α identity or prediction |
| asymmetry/access-function claim | coordinated distributed load and action-corridor difference | Ω identity or moral rank |
| chapter-method claim | coherent family architecture and open failure routes | pressure-object result or authority |

Primary site: [Chapter 34 WP1](../01_blocks/04_part_iii_retype.md#34-1-basic-claim).

## Chapter 34 WP2 Claim Separation

| Claim position | Required support | Must not be inferred from |
|---|---|---|
| commitment occurrence | explicit or practice-supported commitment, role, time, and source basis | commitment vocabulary alone |
| binding-function | continuity, related commitments, breach/revision/exit consequences, target difference | repetition count or formal obligation |
| local integration occurrence | bounded local coordination or repair with residuals disclosed | positive outcome label |
| integration-function | relations among local integrations and target-level coordination | multiple local successes |
| emergent function | composite-level visibility plus component-and-relation Source Trace | unexplained novelty or macro salience |
| component role | claim-bound removal, substitution, modulation, conflict, and scope evidence | score, centrality, or permanent type |
| internal-conflict consequence | source-supported weakening, redirection, split, reduction, Stop, Failure, or Non-Capture | analyst preference for one macrofunction |

Primary site: [Chapter 34 WP2](../01_blocks/04_part_iii_retype.md#34-5-repeated-commitments-as-higher-level-psi-function).

## Chapter 34 WP3 Claim Separation

| Claim position | Required support | Must not be inferred from |
|---|---|---|
| descriptive aggregate | warranted components and declared source boundary | macrofunction vocabulary |
| functional formation | relation topology plus concrete target praxis difference | component accumulation or visibility |
| threshold crossing | qualitative function-specific burdens and live rivals | count, duration, repetition, density, salience, or model completion |
| source-boundary claim | target-blind inclusion and justified alternatives | later target fit |
| higher-level authority claim | prohibited | analytical level, readability, schema validity, or smoke success |
| failed projection | localized failed source-to-target burden | automatic invalidation of all components or source-side claims |

Primary sites: [§34.8](../01_blocks/04_part_iii_retype.md#34-8-aggregation-versus-functional-formation) through [§34.11](../01_blocks/04_part_iii_retype.md#34-11-failed-higher-level-projection).

## Chapter 34 Lock and Chapter 35 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| operator-occurrence claim | source-supported occurrence under canonical dependencies | relative weighting |
| weighting claim | declared qualitative criteria, scope, roles, time, and relation evidence | new operator or prediction |
| modulator claim | contextual access/threshold/timing/persistence difference | operator identity or causality |
| profile-formation claim | stable source-traceable occurrence/modulator relation | formal type or target function |
| profile-projection claim | separate `PROJECT_AS`, target praxis difference, exact Loss, and Counterfactual Sensitivity | person trait or authority |
| chapter-method lock | complete method and audit | pressure-object result |

## Chapter 35 WP1 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| operator-occurrence claim | occurrence identity, source, Frame, role, time, uncertainty | weighting |
| relation claim | support, opposition, sequence, accessibility, persistence | profile |
| weighting claim | qualitative declared dimension and comparison basis | dependency change or numerical dominance |
| modulator claim | contextual condition and tested relation path | operator identity or causality by label |
| profile-formation claim | stable source-traceable occurrence/modulator relation | target function |
| target-placement claim | declared `K/L` coordinates | profile effect |
| profile-function claim | concrete later-praxis difference through `PROJECT_AS` | prediction or authority |

Primary site: [§§35.1–35.4](../01_blocks/04_part_iii_retype.md#35-1-purpose).

## Chapter 35 WP2 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| profile-formation claim | warranted occurrences, relation topology, weighting, modulators, scope, stability and break conditions | target function |
| profile-stability claim | declared window plus role/phase/context counterpressure | permanence or prediction |
| trajectory-form claim | warranted temporal object and change in transition, Λ, attractor, cost, or continuation structure | probability, inevitability, or causal monopoly |
| emergent-profile claim | composite-level visibility plus full reconstructible Source Trace | new operator, entity, or origin type |
| rival-profile claim | same-source comparison criteria and Loss | person/group type or automatic preferred route |
| target-function claim | separate `PROJECT_AS`, concrete target difference, Source Trace and full audit | source-profile truth by itself |

Primary site: [§§35.5–35.7](../01_blocks/04_part_iii_retype.md#35-5-modulating-profile).

## Chapter 35 WP3 Claim Separation

| Claim | Required support | Does not establish |
|---|---|---|
| profile description | warranted source relation topology and bounded stability | formal type or target function |
| profile-formation threshold | source discrimination and break conditions | later-praxis function |
| profile projection | explicit `PROJECT_AS`, target difference, Source Trace, Loss, rivals | origin-type change or prediction |
| profile-function threshold | additional target PraxisPurchase and Counterfactual Sensitivity | causal necessity or authority |
| profile inflation finding | failed purchase or traceability under label pressure | negative person/group verdict |
| add-on stress result | optional adversarial test | STRATA rule or route authority |

Primary site: [§§35.8–35.12](../01_blocks/04_part_iii_retype.md#35-8-profile-versus-type).

## Chapter 35 Lock and Chapter 36 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| candidate projection | complete family-specific `PROJECT_AS` burden | compatibility or preference |
| compatibility claim | explicit non-overlapping or complementary target coordinates/work | forced integration |
| competition claim | shared source and materially overlapping target coordinates/work | one candidate false |
| comparative preference | discriminative gain, traceability, sensitivity, Loss, fit, integrity, parsimony | source identity or absolute truth |
| indeterminacy claim | completed comparison with unresolved responsible selection | candidate Failure automatically |
| non-translation claim | distinct preserved dimensions or Loss profiles | contradiction or tribunal ranking |

## Chapter 36 WP1 Claim Positions

| Claim position | Required object | WP1 status |
|---|---|---|
| source identity claim | stable origin-typed source object | declared, not re-adjudicated |
| candidate-specific source-trace claim | declared load-bearing source subset | required, substantive load open |
| target-coordinate claim | context, level, object, function, scopes, time | declared |
| compatibility claim | non-exclusive target work | method defined, result open |
| competition claim | shared coordinates and overlapping work | method defined, result open |
| alternative/no-projection claim | serious rival or source-only account | retained |
| comparative-preference claim | complete qualitative comparison | not executed |
| canonical Output-Class claim | delimited audited claim | not selected |

Comparative preference cannot inherit source identity, empirical truth, tribunal authority, or application authority.

## Chapter 36 WP2 Claim Positions

| Claim position | Required support | WP2 boundary |
|---|---|---|
| comparative-criteria claim | explicit applicability of eight non-compensatory criteria | no score or automatic ranking |
| discriminative-performance claim | positive case, countercase, material source variation, assumption burden | no coverage-as-discrimination |
| comparative-Loss claim | exact five-part candidate Loss and justified comparison basis | non-comparability remains possible |
| bounded-preference claim | viable candidates plus declared target coordinates and comparative reasons | not source identity or absolute truth |
| co-validity/context-dependence claim | independent family viability and non-exclusive/context-varied target work | no forced integration |
| underdetermination/non-comparability claim | located evidence or comparison-basis limit | not automatic Failure or new Output Class |
| no-projection preference claim | source-only/present-target account with better discrimination | source finding retained |

Primary site: [Chapter 36 WP2 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-36-wp2-completion-boundary).

## Chapter 36 WP3 Claim Positions

| Claim position | Required support | WP3 boundary |
|---|---|---|
| non-translation claim | material change required to transfer target work, scope, Source Trace, or Loss | not contradiction or source-type difference automatically |
| partial-translation claim | explicit common segment plus retained non-equivalent remainder | no silent total equivalence |
| contradiction claim | same delimited claim, compatible scope/evidence, affirmation and denial | not vocabulary difference or competition alone |
| non-comparability claim | located absence of justified common comparison basis | candidates may retain separate findings |
| comparative-governance claim | explicit anti-tribunal, Claim Ceiling, Stop, and authority prohibition | no person, political, legal, institutional, or theory verdict |
| comparison-record claim | references to separate candidate Records and exact comparison fields | no schema expansion, operation merger, or automatic Output mapping |
| comparison-failure claim | exact failed claim position and preserved valid findings | rival success and source invalidation do not follow automatically |

Primary site: [Chapter 36 WP3 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-36-wp3-completion-boundary).

## Chapter 36 Lock and Chapter 37 Claim Separation

| Claim position | Required support | Does not establish |
|---|---|---|
| functional projection | full bounded `PROJECT_AS` burden | source-type identity |
| structural analogy | declared relation of similarity, scope, residuals, counterpressure | semantic preservation or target function |
| symbolic/executable mapping | explicit correspondence and technical validity | praxeological function or empirical truth |
| label-substitution finding | missing discrimination, context, Source Trace, sensitivity, Loss, or alternatives | source object invalidity |
| analogy-only result | useful bounded resemblance under completed audit | failed transformation automatically |

## Chapter 37 WP1 Claim Types

| Claim type | Required declaration | Does not establish |
|---|---|---|
| Functional-projection claim | typed source, source reference, target context/function, PraxisPurchase, Source Trace, Counterfactual Sensitivity, exact Loss, alternatives, Claim Ceiling | source-type replacement, semantic identity, authority |
| Structural-analogy claim | source/target relata, comparison dimension, direction, preserved relation, residuals, incompatibilities, uncertainty, scope | target function, origin-type identity, semantic preservation |
| Cross-domain coordinate claim | source/target domains and objects, target context, mapping direction, proposed correspondence | mapping validity or usefulness |
| Semantic-preservation claim | comparable role, dependence, constraint, consequence, and praxeological load under bounded scope | total equivalence or model superiority |
| Residual claim | source-only, target-only, incompatible, or artificially fitted structure | sixth Loss field or automatic failure |
| Label-substitution pressure claim | missing context, function, discrimination, trace, sensitivity, Loss, or alternatives | final failure route before audit |

Primary site: [Chapter 37 WP1](../01_blocks/04_part_iii_retype.md#37-1-why-the-distinction-matters).

## Chapter 37 WP2 Claim Types

| Claim type | Required support | Does not establish |
|---|---|---|
| Symbolic-mapping claim | declared signs, labels, and correspondence scope | relation preservation, semantic identity, target function |
| Formal-mapping claim | explicit relation schema and preservation conditions | comparable praxeological load or empirical truth |
| Executable-mapping claim | implementation status and target-side technical conditions | semantic preservation, source validity, `PROJECT_AS` |
| Terminal-analogy claim | bounded useful correspondence, residuals, uncertainty, countercases, Claim Ceiling | target function or hidden future upgrade |
| Partial-analogy claim | exact preserved relation and unmapped remainder | percentage similarity or global equivalence |
| Label-substitution claim | missing function/discrimination/trace/sensitivity/Loss/alternatives under bounded audit | source-object invalidity automatically |
| Counterfactual-mapping claim | separate source, target, direction, label, countercase, and no-projection variations | causal or semantic proof |

Primary site: [Chapter 37 WP2](../01_blocks/04_part_iii_retype.md#37-5-symbolic-formal-and-executable-mapping).

## Chapter 37 WP3 Claim Types

| Claim type | May establish | Does not establish |
|---|---|---|
| Analogy-drift claim | an unmarked increase from resemblance to semantic, functional, typological, primitive, or authority load | invalidity of every earlier bounded correspondence |
| Translation-breadth claim | expression, relation, execution, compression, or rendering capacity under declared purpose | semantic superiority, completeness, or valid RETYPE |
| Integrated stress-test claim | sensitivity and boundary findings across source, target, mapping, semantic, residual, rival, and label variation | similarity score, causal equivalence, or automatic Output Class |
| Cross-domain Non-Capture claim | the exact comparison that cannot responsibly be adjudicated | permission to retain a stronger unsupported claim |
| Authority-boundary claim | prohibition of person, domain, theory, governance, recommendation, sanction, or application authority | substantive semantic adjudication |

Primary site: [Chapter 37 WP3](../01_blocks/04_part_iii_retype.md#37-9-analogy-drift).

## Chapter 37 Lock and Chapter 38 Preparation Claim Types

| Claim type | Required support | Does not establish |
|---|---|---|
| Invalid-type-jump claim | explicit source origin type, alleged replacement, operation/context record, and Type-Integrity test | failure of every bounded target function |
| Missing-context claim | absent target object/context/level/Frame/time/scope declaration | substantive target-function falsity automatically |
| Level-mixing claim | identified relative levels and unmarked evidential or object-identity transfer | invalidity of every cross-level relation |
| Granularity-mixing claim | identified fine/coarse positions and missing granularity relation | invalidity of multi-granular analysis |
| Projection-rescue claim | prior failure, changed coordinates, and missing new-claim burden | impossibility of a genuinely new projection |
| Person-level type-jump claim | configuration/composite function rewritten as person/group essence or trait | diagnosis, motive, blame, or rank |
| Scope/temporal-inflation claim | bounded original claim and unsupported widening across scope or time | invalidity of a narrower surviving claim |
| Projection-without-Loss claim | missing exact Loss and visibility-change declaration | automatic total failure rather than possible reduction |

Preparation site: [Chapter 38 Preparation Record](Chapter_38_Preparation_Record.md#7-work-package-allocation).

## Chapter 38 WP1 Claim Forms

| Claim form | Required declaration | Current boundary |
|---|---|---|
| Bounded target-function claim | typed source, target context/object/level/Frame/time/function/scope, Source Trace, exact Loss | may enter `PROJECT_AS` audit |
| Origin-type identity claim | explicit new typing claim and continuity burden | cannot inherit target-function warrant |
| Bounded metaphor | non-literal scope and limited Claim Ceiling | no automatic operation, semantic, type, or output status |
| Ambiguous natural-language claim | intended formal status or explicit unresolved status | review, reduction, or Non-Capture; no invented formalization |

Primary site: [Chapter 38 WP1 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-38-wp1-completion-boundary).

## Chapter 38 WP2 Claim Types

| Claim type | Required support | Does not establish |
|---|---|---|
| Cross-level relation claim | stable objects and levels, named relation, level-specific evidence, countercases, Loss | identity, automatic evidential or functional inheritance |
| Multi-granular claim | stable reference, declared operation/relation, resolution-specific evidence, countercase handling, Loss | fine-detail truth priority or automatic macrofunction |
| Post-failure projection claim | prior-claim reference/disposition, new `PROJECT_AS` record, stable target coordinates, Source Trace, alternatives, Loss | erasure or repair of the original failure |
| Person-participation claim | bounded participation relation, context, time, evidence, uncertainty, Claim Ceiling | essence, diagnosis, rank, motive, stable trait |
| Derived-function claim | source-traceable function, bounded context, retained origin type | PMS operator, new primitive, Δ–Ψ revision |
| Genuine dual-record claim | separate operation records, outputs, coordinates, inter-record relation, Loss | merged operation or inherited result |

Primary site: [Chapter 38 WP2](../01_blocks/04_part_iii_retype.md#38-5-unmarked-level-mixing).

## Chapter 38 WP3 Claim Types

| Claim type | Required support | Does not establish |
|---|---|---|
| Scope-extension claim | widened coordinates, additional source load, new countercases, revised Claim Ceiling and exact Loss | validity of the original or extended claim automatically |
| Temporally bounded function claim | formation, phase, interruption, persistence, dissolution, observation window, excluded periods, uncertainty | permanence, essence, prediction, or person type |
| Projection Loss claim | exact five-part Loss plus foregrounding/backgrounding | projection admissibility automatically |
| Invalid-projection diagnostic claim | original claim reference, local findings, retained valid material, failure continuity, repair boundary, open routes | new operation, schema, Output Class, or truth judgment |
| Reduced projection claim | independently warranted narrower context, scope, relation, time, or Claim Ceiling | preservation or erasure of the invalid stronger claim |

Primary site: [Chapter 38 WP3](../01_blocks/04_part_iii_retype.md#38-10-scope-inflation).



<a id="chapter-38-lock-and-chapter-39-preparation-claim-sync"></a>

## Chapter 39 Prepared Claim Types

| Claim type | Required burden | Failure pressure | Primary site |
|---|---|---|---|
| Lower-boundary claim | concrete additional PraxisPurchase beyond label or source-only description | renaming or functional inertness | Chapter 39 §§39.1–39.3 |
| Upper-boundary claim | constitutive Source Trace and material source dependence | abstraction without traceable load | Chapter 39 §§39.4–39.5 |
| Type-boundary claim | origin type, reference, level relation, and primitive inventory preserved | type replacement or primitive inflation | Chapter 39 §39.6 |
| Context-boundary claim | target context, object, level, Frame, granularity, time, claim and validity scope | arbitrary or globalized function | Chapter 39 §39.7 |
| Counterfactual projection claim | material and irrelevant source variations plus target and function alternatives | invariance under opposite source structures | Chapter 39 §39.8 |
| Alternative-projection claim | rival functions, narrower claim, source-only, analogy-only, and no-projection retained | forced single function | Chapter 39 §39.9 |
| Elasticity claim | stable failure conditions under objections and relocations | function proliferation or endless narrowing | Chapter 39 §39.11 |
| Stop / Non-Capture claim | exact trigger and retained valid material | route collapse | Chapter 39 §§39.12–39.13 |

<a id="chapter-39-wp1-claim-type-sync"></a>

## Chapter 39 WP1 Claim Types

| Claim type | Minimum content | Not established automatically |
|---|---|---|
| Lower-boundary claim | additional bounded praxeological discrimination | complete admissibility |
| Renaming-without-purchase claim | unchanged reconstruction after label removal | Label Substitution or final route |
| Functional-Gain claim | concrete target-side difference relative to source-only rival | Source Trace or causality |
| Upper-boundary claim | abstraction remains within traceable constitutive source load | empirical truth or authority |

Primary site: [Chapter 39 WP1](../01_blocks/04_part_iii_retype.md#39-1-lower-retype-boundary).

<a id="chapter-39-wp2-claim-type-sync"></a>

## Chapter 39 WP2 Claim Types

| Claim type | Required burden | Does not establish automatically |
|---|---|---|
| Constitutive Source Trace claim | features, relations, dependencies, reconstruction path, sensitivity, exact Loss | causality or exhaustive history |
| Type-Integrity claim | origin type, reference, level relation, primitive/person boundary | target-function admissibility |
| Context-Boundary claim | complete bounded target coordinates and validity conditions | Source Trace or PraxisPurchase |
| Counterfactual projection claim | differentiated response to material and irrelevant source/target variation | probability, prediction, or authority |

Primary site: [§§39.5–39.8](../01_blocks/04_part_iii_retype.md#39-5-function-without-source-trace).

<a id="chapter-39-wp3-claim-type-sync"></a>

## Chapter 39 WP3 Claim Types

| Claim | Required burden | Not automatic |
|---|---|---|
| Alternative projection | stable coordinates and candidate-specific warrant | ranking |
| Analogy boundary | preserved relation and residuals | target function |
| Elasticity finding | documented claim relocation or objection absorption | causal proof |
| Stop claim | prohibited continuation | universal failure |
| Non-Capture claim | exact unavailable adjudication and retained material | strongest wording |

<a id="chapter-39-lock-and-chapter-40-preparation-claim-sync"></a>

## Chapter 39 Lock / Chapter 40 Case-Claim Separation

| Claim layer | Required status |
|---|---|
| Chapter-39 family-method claim | provisionally locked; `admissible_but_provisional` |
| `W/A–F` pressure-object claims | unadjudicated |
| Chapter-40 case-family packet | prepared, not executed |
| instantiated case claim | requires separate source, target, trace, sensitivity, Loss, alternatives, audit, and output |
| RETYPE lock claim | limited to actually verified prose and artifact evidence |

```text
case architecture claim
≠ case result claim
≠ RETYPE lock claim
```

## Chapter 40 WP1 Case-Claim Separation

| Layer | Claim status | What it may support | What it may not support |
| --- | --- | --- | --- |
| Case-family prose | bounded demonstration claim | required fields, distinctions, counterpressure, Loss and alternatives | case passage, canonical route, artifact completion |
| Instantiated `PROJECT_AS` Record | delimited operation occurrence | structural validation and later substantive audit | automatic admissibility or truth |
| Local Audit and mapping | executed case disposition | exactly one canonical class for the tested claim | general RETYPE validation or authority |

<a id="chapter-40-wp2-claim-sync"></a>

## Chapter 40 WP2 Countercase Claim Types

| Claim pressure | Claim position tested | Preserved alternatives |
|---|---|---|
| Origin-type replacement | source identity versus target role | bounded function, analogy, source-only |
| Missing target context | formal target-coordinate completeness | metaphor, analogy, completed new claim, Non-Capture |
| Label substitution | Source Trace, PraxisPurchase, sensitivity, Loss, rivals | ordinary-domain description, bounded analogy, no-label |
| Analogy as projection | Semantic Preservation and Target Function | partial analogy, target-only, no-projection |
| Aggregation as macrofunction | composite formation and target-function threshold | descriptive aggregation, narrower composite, source-only |
| Claim rescue | failure continuity and new-claim registration | genuine re-entry, Claim Reduction, no-projection |
| Person-level jump | subject and level of predication | bounded role relation, configuration-only |

Every row remains unadjudicated until Local Audit and canonical mapping.

<a id="chapter-40-wp3-claim-type-sync"></a>

## Chapter 40 WP3 Adjacent Claim Forms

| Confusion | First claim form | Second claim form | Required separation |
| --- | --- | --- | --- |
| RETYPE or SUB | finer reconstruction of same reference object | bounded target function | operation, record, Loss, result |
| RETYPE or COMPOSE | new composite formation | contextual function of composite | source formation before target function |
| Projection or Recontextualization | changed Frame under Φ | specific target function under `PROJECT_AS` | Frame change versus Functional Gain |
| Attractor or Similarity | descriptive/formal recurrence | stabilizing target load | resemblance versus PraxisPurchase |
| Modulator or Operator | contextual condition/profile | PMS primitive or operation | local modulation versus grammar identity |
| Projection or Analogy | bounded correspondence | source-dependent target function | semantics, residuals, function, no-projection |


## Chapter 40 Closure-Claim Segmentation and Chapter 41 Continuity

| Claim | Claim type | Current disposition | Canonical mapping |
|---|---|---|---|
| Chapter-40 Layer-1 architecture is complete | bounded method-completion claim | retained | `admissible_with_bounded_claim` |
| Chapter-40 lock-critical artifacts are complete | artifact-completeness claim | prohibited from continuation under current evidence | `mandatory_stop` |
| `P1–P7`, `N1–N7`, `X1–X6` have substantive results | case claims | not executed | none selected |
| another operation answers the prior artifact gap | recursive chain claim | untested and non-inherited | none selected |

The Chapter-41 rule is that every changed operation, source, context, level, granularity, composite, function, or evidence packet creates a new testable claim while prior dispositions remain visible.

## PMS-grounded RETYPE claim burden

A RETYPE claim that materially depends on PMS occurrences must state, through existing record positions, which warranted occurrence relation carries the target difference and how material variation would affect the claim. The burden remains conditional, source-supported, and claim-relative.

A source object may remain valid even when its projected function is reduced, stopped, failed, analogy-only, or non-capturable.
