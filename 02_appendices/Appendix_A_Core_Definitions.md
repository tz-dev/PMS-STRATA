# Appendix A — Core Definitions

**Status:** substantive bounded provisional completion; final Appendix lock remains pending until all Appendices A–N, Reference Freeze, and the Integrated Corpus Audit  
**Repository role:** consolidated definition and navigation supplement; not a competing theory source  
**Authority basis:** `PMS.yaml` → `00_source/PMS-STRATA_Structure.md` → locked or provisionally locked canonical prose in `01_blocks/*` → binding controls in `05_minified/*` → formal operationalization in `07_model/*`  
**Primary inputs:** Chapter 1, Chapter 10, Chapter 18, Chapter 29, `04_reference/Glossary.md`, and `04_reference/Non_Equivalence_Index.md`

---

## A.1 Purpose, Status, and Reading Rule

Appendix A consolidates the core definitions required to read and use PMS-STRATA without repeatedly reconstructing their locations across Foundations, PATH, SUB, and RETYPE. It expands the object tables, path-status taxonomy, source-object taxonomy, and projection terminology explicitly migrated here by the Chapter Contracts.

It does **not** replace the primary definition sites. Where a short definition in this appendix appears more compact than the canonical chapter prose, the chapter remains controlling. Where a term is represented in a schema or registry, the schema or registry operationalizes the term but does not acquire independent semantic authority.

```text
canonical chapter definition
→ primary substantive owner

Appendix A definition
→ consolidated navigation and bounded elaboration

formal field or enum
→ operational encoding
```

The governing production rule remains:

```text
Each concept is defined once,
operationalized locally,
tested repeatedly,
and never re-derived without necessity.
```

Accordingly, Appendix A may:

- consolidate already canonical meanings;
- expose object and status taxonomies that were too bulky for the main chapters;
- name primary definition sites and controlling non-equivalences;
- clarify where one object may enter different operations;
- preserve authority, type, reference, loss, Stop, Failure, and Non-Capture boundaries.

It may not:

- create a fourth core operation;
- add, rename, reorder, decompose, or extend Δ–Ψ;
- turn a derived object or contextual function into a PMS primitive;
- convert analytical coordinates into ontological layers;
- grant finer resolution, larger composition, formal validity, or graph visibility greater authority;
- type, diagnose, rank, sanction, or assign irreversible labels to persons;
- decide empirical truth, causality, legitimacy, normative validity, or application authority.

The appendix is therefore removable without changing the canonical theory. Its value is consolidation, not upstream revision.

### A.1.1 Controlling source pointers

- [Chapter 1 — Object Model](../01_blocks/01_foundations.md#1-object-model-operator-type-operator-occurrence-and-composite-structure) owns the object categories and identity conditions.
- [Chapter 10 — Path](../01_blocks/02_part_i_path.md#10-path) owns the operational path definition and path-status distinctions.
- [Chapter 18 — The Provisionally Compressed Object](../01_blocks/03_part_ii_sub.md#18-the-provisionally-compressed-object) owns provisional elementarity, compressed source objects, and the preservation requirement.
- [Chapter 29 — Functional Projection without Origin-Type Replacement](../01_blocks/04_part_iii_retype.md#29-functional-projection-without-origin-type-replacement) owns the extended RETYPE definitions.
- [Glossary](../04_reference/Glossary.md) supplies controlled short definitions and designated primary locations.
- [Non-Equivalence Index](../04_reference/Non_Equivalence_Index.md) supplies category-collapse guards.
- [Operation Registry](../07_model/Operation_Registry.yaml) formalizes operation identity and operation-specific boundaries.
- [Output Classes](../07_model/Output_Classes.yaml) formalizes the closed ten-class inventory.

---

## A.2 Compact Core-Definition Table

The table gives the shortest usable definitions. Later sections provide expanded taxonomies and boundary notes.

| Term | Short definition | Primary definition site | Central non-equivalence |
| --- | --- | --- | --- |
| **PMS Base** | The governing Δ–Ψ operator grammar and its dependencies as specified in `PMS.yaml`. | `PMS.yaml` | PMS Base ≠ PMS-STRATA |
| **PMS-STRATA** | A bounded transformation discipline for composing, decomposing, and contextually projecting PMS structures across declared analytical coordinates. | Chapter 0 | STRATA ≠ Meta-PMS |
| **operator sign** | The canonical symbol used to denote a PMS operator type. | `PMS.yaml`; Chapter 1 distinction | sign ≠ name ≠ type |
| **operator name** | The canonical label associated with an operator sign and type. | `PMS.yaml`; Chapter 1 distinction | name ≠ type |
| **operator type** | An abstract PMS Base function in the Δ–Ψ grammar, not a concrete empirical object. | Chapter 1 | operator type ≠ occurrence |
| **operator occurrence** | A concrete, reference-, frame-, source-, and claim-bound reconstruction expressing an operator function in one analysis. | Chapter 1 | occurrence ≠ type; occurrence ≠ composite |
| **composite structure** | A selectively formed analytical object whose declared constituent relations are constitutive of the claimed whole. | Chapter 1 | composite ≠ list; composite ≠ lossless sum |
| **configuration** | A temporally located, selectively incomplete, operator-structured praxis constellation relative to a declared frame. | Chapters 1 and 3 | configuration ≠ complete world description |
| **event-like object** | A bounded occurrence or interval reconstructed as making a claim-relevant difference within a declared frame. | Chapter 1; temporal specification in Chapter 3 | event ≠ causal atom |
| **non-event structure** | A source-supported failure, absence, delay, or non-realization relative to an explicit expectation, opportunity, duty, or window. | Chapters 1 and 3 | missing information ≠ non-event |
| **transition** | A source-supported relation from one configuration to another that specifies more than endpoint difference. | Chapters 1, 3, and 9 | state difference ≠ transition |
| **derived analytical object** | A path, trajectory, macro-event, composite, or other analysis-produced object that remains non-primitive and source-bound. | Chapter 1 | derived object ≠ PMS primitive |
| **frame** | The analytical boundary that determines what counts as relevant for the declared reconstruction. | Chapter 2 | frame ≠ granularity |
| **granularity** | The declared resolution at which distinctions and relations are reconstructed. | Chapter 2 | finer granularity ≠ higher truth |
| **relative level** | A position within an explicitly declared source–target or part–whole relation. | Chapter 2 | relative level ≠ ontological layer |
| **transformation context** | The declared context in which an operation is proposed, tested, and bounded. | Chapters 4–7; Chapter 29 for projection | context ≠ frame; context ≠ target function |
| **chronology** | A temporally ordered list or record. | Chapters 3 and 10 | chronology ≠ path |
| **sequence** | An ordered succession of declared objects or occurrences without the full path burden. | Chapter 3 | sequence ≠ path |
| **path** | The actually traversed, selectively reconstructed chain of relevant configurations and transitions within a declared frame. | Chapter 10, with Foundations ownership in Chapter 3 | path ≠ trajectory; path ≠ dependence |
| **trajectory** | A path whose sedimented historical load materially shapes a present configuration or later continuation. | Chapters 3 and 11 | trajectory ≠ teleology; trajectory ≠ path dependence |
| **path dependence** | A property claim that present or later structure remains materially sensitive to the realized path and source-supported alternatives. | Chapters 3 and 12 | path dependence ≠ mere history |
| **provisional elementarity** | The bounded treatment of an object as sufficiently unitary for the present frame, granularity, claim, and source access. | Chapter 18 | provisional elementarity ≠ ontological indivisibility |
| **compressed object** | An occurrence or composite whose internal relations are intentionally left unresolved at the current granularity. | Chapter 18 | compression ≠ error |
| **source function** | The coarser role or analytical work attributed to a source object before decomposition. | Chapter 18; continuity in Chapters 47–48 | source function ≠ immunity from revision |
| **origin type** | The source-side analytical type retained through a PROJECT_AS claim. | Chapters 5 and 29 | origin type ≠ target function |
| **target function** | The bounded contextual work a source object is proposed to perform in a declared target context. | Chapters 5 and 29 | function ≠ operator identity |
| **functional projection** | A bounded source-to-context relation in which an origin-typed object performs a declared target function without origin-type replacement. | Chapter 29 | projection ≠ analogy; projection ≠ label substitution |
| **Source-Object Integrity** | Preservation of enough source reference, type, historical load, and constitutive relations for the target claim to remain traceable to the claimed source. | Chapter 29; system-wide continuity in Chapter 47 | integrity ≠ complete reproduction |
| **Functional Continuity** | The requirement that the proposed target function remains materially dependent on the retained source structure. | Chapters 29 and 47 | continuity ≠ semantic resemblance |
| **COMPOSE** | Forms a new composite analytical object from multiple or sequential source structures under declared selection and relation rules. | Chapters 4 and 15 | composition ≠ lossless addition |
| **DECOMPOSE** | Reconstructs the same occurrence or composite under finer granularity while preserving the source reference as the tested object. | Chapters 4 and 20 | decomposition ≠ discovery of final constituents |
| **PROJECT_AS** | Projects an origin-typed source object as a bounded contextual target function. | Chapters 4 and 30 | projection ≠ origin-type replacement |
| **operation occurrence** | One declared execution of exactly one core operation on one tested claim. | Chapters 4 and 7 | operation type ≠ occurrence ≠ chain |
| **operation chain** | A declared sequence of separately recorded operation occurrences with explicit handoffs and preserved local results. | Chapters 39, 46, 53, and 54 | chain ≠ new operation |
| **canonical Output Class** | One of the ten closed, non-ordinal result classes selected for a delimited tested claim. | Minified Kernel; Output Classes registry | Output Class ≠ local result; class ≠ rank |
| **mandatory Stop** | A positive governance result that prohibits further continuation of the current claim under the current grounds. | Chapters 51 and 53 | Stop ≠ Failure; method Stop ≠ output label automatically |
| **Failure** | A result in which the declared transformation does not carry its operation-specific burden. | Chapters 41, 50, and 53 | failed claim ≠ erased by later success |
| **Non-Capture** | A claim-relative result reached after adequate bounded attempts fail to supply an adequate retained form without invention or destructive integration. | Chapter 52 | uncertainty ≠ Non-Capture; Failure ≠ Non-Capture |

---

## A.3 Object Model and Identity Taxonomy

### A.3.1 Operator sign, name, type, and occurrence

STRATA must keep four layers of reference distinct:

```text
operator sign
→ notation

operator name
→ canonical label

operator type
→ abstract PMS Base function

operator occurrence
→ concrete reconstructed instance
```

The sign and name identify the type in the repository reference. They are not themselves the function. The type is not an empirical aggregate waiting to be opened. The occurrence is the concrete, source-bound object that may be composed, decomposed, compared, or projected.

Only occurrences and composites are eligible for `DECOMPOSE`. A theoretical criticism of an operator type may be legitimate scholarship, but it is not a STRATA decomposition of that type.

```text
operator type
≠ empirical object
≠ decomposable occurrence
```

An occurrence may support competing typings. Such competition concerns the reconstruction of the occurrence; it does not rename or revise the Δ–Ψ inventory.

### A.3.2 Operator occurrence

An operator occurrence requires at minimum:

- a bounded reference object or relation;
- a declared frame and claim;
- a source basis;
- a contextual occurrence of a PMS function;
- visible uncertainty or competing typing where material.

An occurrence is local to the reconstruction. It does not become a global property of a person, institution, theory, or domain. Repeated occurrences can support a pattern claim only through a separately declared transformation or comparison.

```text
repeated occurrence
≠ person type
≠ stable essence
≠ automatic composite
```

### A.3.3 Composite structure

A composite contains multiple identifiable constituents and a declared relation topology. Mere co-presence, adjacency, or repeated mention is insufficient.

A minimal composite declaration identifies:

1. selected constituents;
2. their order where relevant;
3. constitutive relations;
4. formation rule;
5. excluded or compressed material;
6. the new analytical object claimed;
7. the loss introduced by composition.

The composite is new as an analytical object, but not as a PMS primitive. It may preserve its constituents while carrying a relation-dependent function that no isolated constituent carries.

```text
constituents + constitutive relations
→ composite candidate

constituents without constitutive relations
→ list, set, or co-presence only
```

### A.3.4 Configuration

A configuration is not a complete snapshot of reality. It is a selective praxis constellation that preserves the relations needed by a declared claim. Different frames or granularities may yield multiple valid configurations of the same broad scene.

A configuration may include:

- operator occurrences;
- material and institutional carriers;
- roles, access relations, costs, commitments, expectations, and alternatives;
- relevant events and non-events;
- unresolved or uncertain structure.

A configuration remains temporally located even where its relevant features extend across an interval.

### A.3.5 Event-like object

An event-like object is bounded by the tested claim, not necessarily by an instant. It may be punctual, extended, distributed, composite, or retrospectively delimited. What matters is that the source supports treating it as a claim-relevant occurrence or interval.

```text
bounded occurrence or interval
+ claim-relevant difference
+ source support
→ event-like candidate
```

An event does not automatically supply a causal mechanism, a final periodization, or a privileged granularity.

### A.3.6 Non-event structure

A non-event requires an explicit comparison frame. Its minimum burden is:

- what was expected, available, promised, required, or temporally possible;
- the relevant window or condition;
- source support for that expectation or opportunity;
- support for non-realization, delay, blockage, or absence;
- the claim-relevant effect of that non-realization.

Unknown records, documentary silence, or missing information do not by themselves establish a non-event.

```text
missing record
≠ supported non-realization
```

A non-event may participate in transitions, paths, trajectories, composites, or decompositions. It does not thereby become a fourth operation or a new primitive.

### A.3.7 Transition as object

A transition connects source and target configurations through a source-supported change relation. Endpoint difference alone does not disclose the passage between them.

A transition declaration should make visible:

- source and target configurations;
- the relevant changed relations;
- temporal ordering;
- carriers and constraints where known;
- source support;
- uncertainty and omitted intervals;
- whether the transition was realized, blocked, aborted, deferred, or otherwise bounded.

### A.3.8 Derived analytical objects and functions

Derived objects and functions include, among others:

- sequence;
- path;
- trajectory;
- macro-event;
- recurrence or profile object;
- frame-function;
- attractor-function;
- modulating function;
- higher-level composite function.

Their legitimacy depends on the applicable operation and claim. Their derived status never extends Δ–Ψ.

```text
derived object/function
≠ new PMS primitive
≠ new core operation
≠ inherited operator dependency
```

### A.3.9 Identity across transformation

Object identity is a bounded continuity claim, not a result of repeated naming. Depending on the tested claim, relevant dimensions include:

- reference continuity;
- origin-type continuity;
- constitutive-relation continuity;
- source-function continuity;
- temporal continuity;
- historical-load continuity;
- carrier continuity;
- declared loss and uncertainty.

No single dimension guarantees identity in every case. A source may retain historical reference while its function is revised; a target may retain a name while failing reference continuity.

```text
same label
≠ same object

revised function
≠ different reference automatically
```

Where succession or continuity remains unresolved, the correct result may be Claim Reduction, mandatory Stop, or Non-Capture rather than an invented identity.

---

## A.4 Expanded Path and Continuation Taxonomy

### A.4.1 Chronology, sequence, transition set, and path

These objects preserve different burdens:

| Object | Minimum burden | What it does not yet establish |
| --- | --- | --- |
| **chronology** | correct temporal order | common reference, transition, traversal, or constitutive connection |
| **sequence** | ordered succession of declared units | actual traversal or one warranted path |
| **warranted transition set** | individually supported transitions | valid handoff among transitions or a single path |
| **path candidate** | proposed traversal, selection, constitutive connection, and frame | completed source, continuity, admissibility, loss, and alternative burden |
| **warranted path** | actual traversal plus all claim-relevant path burdens | trajectory, strong dependence, causality, or target function |

A detailed chronology may remain below the path threshold. A short record may qualify as a path where the traversal and relation burdens are satisfied.

### A.4.2 Path components

A path may include:

- selected configurations;
- warranted transitions;
- events and non-events;
- branch points;
- source-supported unrealized alternatives;
- blocked, aborted, or deferred continuations;
- open residue;
- relevant carriers and constraints;
- declared uncertainty and loss.

Not every component must be present in every path. Each included component must be justified by the claim and frame.

### A.4.3 Selection and path frame

Path construction is selective. The selection rule should state why units were included, compressed, or excluded and what would change if a load-bearing unit were removed.

The path frame declares at least:

- reference object or relation;
- temporal bounds and periodization;
- frame;
- granularity;
- relative level;
- source and claim scopes;
- inclusion rule;
- comparison basis;
- evidence mode.

A visual line connecting dated nodes is not a path unless these burdens are met.

### A.4.4 Realized path

A realized path is the source-supported traversal actually taken by the bounded reference object. The status concerns realization, not necessity or correctness.

```text
realized
≠ inevitable
≠ justified
≠ causally complete
```

### A.4.5 Blocked path and blocked continuation

A blocked continuation was source-supported as available within a relevant window but could not proceed because a material constraint, exclusion, veto, cost, rule, carrier condition, or other blockage prevented continuation.

Required distinctions:

```text
blocked
≠ rejected
≠ impossible
≠ never available
```

A blocked path may contain realized segments before the blockage. The blockage status belongs to the continuation or bounded path claim, not to every alternative in the scene.

### A.4.6 Aborted path

An aborted path began or materially entered a continuation and was then discontinued before the claimed endpoint or function was realized.

```text
aborted
≠ never begun
≠ blocked automatically
≠ deferred automatically
```

The record must support both initiation and discontinuation. A merely proposed alternative is not an aborted path.

### A.4.7 Deferred path and deferred continuation

A deferred continuation remains open or postponed beyond the tested window without being adequately classified as realized, blocked, rejected, or aborted.

```text
deferred
≠ uninterrupted continuation
≠ realized later automatically
≠ indefinite availability
```

Deferral requires evidence of postponement or retained openness. Documentary silence alone does not establish it.

### A.4.8 Rejected continuation

A rejected continuation was available for decision or uptake and was declined, refused, voted down, or otherwise not selected through a source-supported rejection relation.

```text
rejected
≠ blocked
≠ unavailable
```

The term describes a historical branch status, not a canonical Output Class.

### A.4.9 Unavailable and impossible alternatives

An unavailable alternative was not reachable under the relevant historical frame, resources, costs, bindings, and window. An impossible alternative is the stronger claim and requires correspondingly stronger support.

```text
currently unattractive
≠ historically unavailable

not selected
≠ impossible
```

Counterfactual path work must use source-supported historical availability, not retrospective narrative plausibility.

### A.4.10 Open continuation and open residue

An open continuation remains unresolved at the end of the tested path. Open residue is the set of unresolved commitments, uncertainties, costs, exclusions, expectations, or possible continuations left by the reconstruction.

Open residue does not license indefinite speculation. It marks what remains outside the retained path claim.

### A.4.11 Similar endpoints and different paths

Two paths may reach superficially similar endpoints while differing in:

- costs and exclusions;
- accumulated commitments;
- carrier structure;
- available alternatives;
- unresolved residue;
- asymmetries and expectations;
- reversibility and repair conditions.

```text
same endpoint
≠ same path
≠ same present structure
```

### A.4.12 Path without strong dependence

A path can be valid even where the present configuration is largely determined by current conditions. Path dependence is an additional property claim requiring counterfactual sensitivity and persistent historical load.

```text
reconstructible path
≠ strong path dependence
```

### A.4.13 Trajectory threshold

A path becomes a trajectory candidate when sedimented historical load from the path materially shapes present configuration or reachable continuation. Relevant carriers may include rules, costs, roles, material arrangements, expectations, commitments, exclusions, or learned routines.

Trajectory does not imply teleology. Directionality may be reconstructed without treating the endpoint as intended, necessary, or progressive.

### A.4.14 Historical branch status and Output Class

Branch statuses such as `realized`, `blocked`, `aborted`, `deferred`, `rejected`, and `unavailable` describe source-supported historical relations. They are not canonical Output Classes.

```text
branch status
≠ Output Class
```

A path record may contain several branch statuses and still receive exactly one canonical Output Class for the delimited tested claim.

---

## A.5 Expanded Source-Object Taxonomy for SUB

### A.5.1 Provisional elementarity

Every analytical object is elementary only relative to the current frame, granularity, claim, and source access. Provisional elementarity licenses temporary treatment as a unit; it does not claim final indivisibility.

An object may be left unopened because:

- the current claim does not require finer resolution;
- sources cannot support a responsible internal reconstruction;
- the coarser object retains greater praxeological usefulness;
- decomposition would exceed the Traceability Ceiling or fall below the Relevance Floor;
- the object is an operator type rather than a decomposable occurrence or composite.

### A.5.2 Compressed occurrence

A compressed occurrence is a concrete occurrence treated as a bounded unit while some internal relations remain unresolved. Examples include an extended decision episode, a frame-typed occurrence, a distributed delay, or a rule-bound interaction.

The compression may be adequate, neutral, or insufficient for the tested claim. Compression is not itself an error.

### A.5.3 Compressed composite

A compressed composite is a previously formed analytical object whose internal constituents or relation topology are not fully represented at the current granularity.

A decomposition may reopen:

- selected constituents;
- internal sequence or phase structure;
- relation topology;
- distributed load, asymmetry, or responsibility;
- competing periodizations;
- uncertainty and loss inherited from earlier composition.

`DECOMPOSE` does not invert the earlier composition or recover excluded source material automatically.

### A.5.4 Temporal composite as source

Sequences, paths, and trajectories may become SUB source objects where the tested claim requires finer reconstruction of transitions, branch statuses, sedimented carriers, or periods.

The source object remains the same reference path or trajectory. A different path reconstructed from the same materials is not a finer version of the same object merely because it contains more detail.

### A.5.5 Event-like and macro-event source

An event-like object or bounded macro-event may be decomposed into phases, carriers, roles, sub-events, non-events, or internal transitions where those distinctions affect the source claim.

The reconstruction must preserve the event reference and test whether the coarser event function survives. It may not assume that every event has one true internal segmentation.

### A.5.6 Projection-derived source

An origin-typed object that previously received a target function remains decomposable only through its origin-typed source object or another explicitly declared eligible occurrence/composite. The contextual function itself is not silently treated as an origin object.

```text
PROJECT_AS result
→ target function retained as prior claim

DECOMPOSE successor
→ must identify eligible source object
```

A chain therefore cannot hide a switch from source object to projected function.

### A.5.7 Source-function claim

The source-function claim states the coarser work attributed to the source object before decomposition. DECOMPOSE tests whether finer reconstruction:

- preserves the function;
- qualifies or narrows it;
- reveals several functions;
- renders it resolution-neutral;
- shows drift or escape;
- requires rejection of the prior source-function claim.

The source function is a test target, not a protected conclusion.

```text
preservation requirement
≠ source immunization
```

### A.5.8 Reasons to decompose

A responsible decomposition reason may include:

- unresolved internal relations materially affect the claim;
- a coarse object hides distributed roles, costs, access, or responsibility;
- competing finer reconstructions discriminate among rival claims;
- a source-function claim cannot be tested at the current resolution;
- a transition, event, path, or composite contains load-bearing uncertainty;
- finer resolution may reveal whether the current claim is overstated.

Curiosity, detail appetite, technical possibility, or a preference for micro-description are insufficient by themselves.

### A.5.9 Reasons not to decompose

The correct decision may be not to decompose where:

- no PraxisPurchase is expected;
- source access cannot support internal reconstruction;
- the coarser object already carries the relevant distinction;
- finer resolution would destroy comparability or source function without gain;
- the proposed target is a competing object rather than the same reference object;
- the source is an abstract operator type;
- a Stop condition has been reached.

### A.5.10 Non-operator remainder

A finer reconstruction may expose material, institutional, technical, bodily, environmental, documentary, or other structure that is not responsibly capturable as an operator occurrence. Such remainder must remain representable without being forced into Δ–Ψ.

```text
not operator-typed
≠ irrelevant
≠ nonexistent
```

Appendix L owns the expanded treatment of non-operator remainder and decomposition limits.

### A.5.11 Minimal source-object declaration

Before DECOMPOSE, a source declaration should identify:

```yaml
compressed_object:
reference:
origin_type:
source_frame:
source_granularity:
source_level:
current_function:
known_internal_structure:
unresolved_internal_structure:
decomposition_reason:
```

This reproduces the minimal Chapter-18 source-entry declaration. It is not a complete Shared Transformation Record and does not add fields to `Transformation_Record.schema.json`. Temporal scope, source basis, claim scope, uncertainty, Loss, governance, and other common declarations remain inherited from the Shared Transformation Record where material. Appendix C and Appendix E own the full record and DECOMPOSE template structures.

---

## A.6 Extended RETYPE and Functional-Projection Definitions

### A.6.1 Functional projection

Functional projection is the bounded relation by which an origin-typed source object performs a declared function in a declared target context without becoming a different origin type.

```text
within target context C,
source object X,
while retaining origin type T,
performs bounded function F
```

The relation adds a source-to-context functional claim. It does not rewrite the source record.

### A.6.2 Origin type

The origin type identifies what the source object is in its source reconstruction. It remains visible throughout projection and after the target claim.

Origin-Type Preservation does not make the source typing immune from later evidence. A later source-supported revision must be recorded as a revision of the source claim; it may not occur silently through target-function language.

```text
functions as F in C
≠ becomes F as origin type
```

### A.6.3 Target function

The target function is the precise contextual work attributed to the source object in the target scene. A function must change the warranted reconstruction of a declared praxis dimension, such as:

- relevance or framing;
- available or blocked alternatives;
- costs and commitments;
- access and exclusion;
- roles and responsibility;
- expectation and binding;
- repair, reopening, or continuation conditions.

A function label is only a candidate until its load is traced.

```text
function label
≠ demonstrated function
```

### A.6.4 Target context

The target context identifies where and under what conditions the proposed function is tested. It includes the target object or scene, frame, scope, temporal and source bounds, validity conditions, and claim ceiling.

The same source object may perform a function in one context and no additional function in another.

```text
function in C1
≠ function in C2 automatically
```

### A.6.5 No-additional-function result

A source object may remain historically relevant while adding no distinct function to the target reconstruction. Where removing the proposed source-to-context relation leaves the target account unchanged, no additional target function is warranted for that claim.

```text
historical relevance
≠ distinct target function
```

This does not invalidate the source object. It rejects or reduces only the proposed projection claim.

### A.6.6 Source-Object Integrity

Source-Object Integrity requires enough of the source to remain visible that the target function is genuinely a function of the claimed source object rather than a convenient label. Relevant load may include:

- source reference;
- origin type;
- historical path or load;
- constitutive relations;
- source-function conditions;
- uncertainty and exclusions;
- material carriers where load-bearing.

Integrity does not require complete source reproduction. Projection is selective; its selection and loss must remain inspectable.

### A.6.7 Functional Continuity

Functional Continuity asks whether the proposed target function materially depends on retained source structure. Counterfactual variation is central:

```text
materially alter or remove a load-bearing source relation
→ target reconstruction should change
```

If opposite or materially different source structures support an arbitrarily unchanged target label, the projection approaches the Traceability Ceiling.

Functional Continuity is claim-relative. Different target functions may depend on different source relations.

### A.6.8 Contextual Boundedness

A valid projection declares where, when, for which target object, under which source conditions, and with what claim ceiling the function applies.

```text
contextual function
≠ universal property
```

Ordinary boundedness is required for every PROJECT_AS claim. A canonical result of `admissible_with_bounded_claim` is selected only when a material narrowing of reach or scope is itself the decisive governance result.

### A.6.9 Operator-like target functions

A source object may perform work described with operator language, for example a frame-function or attractor-function. This is controlled functional language, not operator identity.

```text
frame-function
≠ □ operator type

attractor-function
≠ Α operator type

asymmetry-function
≠ Ω operator type
```

The target claim does not inherit the full semantic dependencies or authority of the abstract operator type.

### A.6.10 Multiple and competing functions

One source object may support:

- compatible functions in one context;
- different functions in different contexts;
- competing functions whose claims cannot all be retained;
- no additional function.

Each materially distinct projection is a separate tested claim and normally a separate operation occurrence.

```text
one source object
+ several function candidates
≠ several origin types
```

### A.6.11 Projection without replacement

Projection without replacement requires:

1. source reference remains identifiable;
2. origin type is stated separately;
3. target context and function are explicit;
4. retained source load is declared;
5. loss and exclusions are visible;
6. counterfactual sensitivity is tested;
7. validity scope and claim ceiling are bounded;
8. no PMS primitive or authority is created.

### A.6.12 PROJECT_AS versus recontextualization

Recontextualization changes the interpretive or analytical setting in which an object is described. `PROJECT_AS` requires a distinct target-side function.

```text
changed frame or description
+ unchanged target praxis reconstruction
→ recontextualization only
```

### A.6.13 PROJECT_AS versus COMPOSE

`COMPOSE` forms a new composite analytical object from several source structures. `PROJECT_AS` attributes a bounded contextual function to an already identified source object.

```text
many sources → new composite object
≠
one source object → bounded target function
```

A composite may later be projected, but the two occurrences remain separate.

### A.6.14 PROJECT_AS versus DECOMPOSE

`DECOMPOSE` opens the same eligible source object at finer granularity. `PROJECT_AS` adds a source-to-context functional relation without changing source granularity by definition.

A chain may include both operations, but each requires its own source, target, loss, result, and handoff record.

### A.6.15 Projection versus analogy and label substitution

Analogy identifies a bounded structural resemblance without establishing target-function continuity. Label substitution merely applies a term to a target.

```text
projection
≠ analogy
≠ metaphor
≠ label substitution
```

A useful resemblance may be retained as `analogy_only`. It must not be upgraded to projection without Source-Object Integrity, Functional Continuity, Contextual Boundedness, and the other applicable tests.

---

## A.7 Operations, Occurrences, Chains, and Result Vocabulary

### A.7.1 The closed operation vocabulary

PMS-STRATA recognizes exactly three core operations:

```text
COMPOSE
DECOMPOSE
PROJECT_AS
```

Every admitted operation occurrence must instantiate one of these signatures. A finite declared chain may repeat or combine them. This is a closure rule of the present STRATA grammar, not a proved theorem that every conceivable PMS-relevant transformation is representable.

```text
closed operation vocabulary
≠ proved representational completeness
```

### A.7.2 Operation type, occurrence, and chain

- **operation type** names the reusable signature;
- **operation occurrence** is one execution on a delimited tested claim;
- **operation chain** connects several occurrences through explicit handoffs.

Each occurrence keeps its own:

- source and target;
- frame, granularity, and relative level;
- claim and validity scope;
- selection or reconstruction rule;
- loss profile;
- local result;
- canonical Output Class;
- Stop, Failure, and Non-Capture conditions.

A chain does not average or overwrite its local results.

### A.7.3 Local result and canonical Output Class

Operation-specific findings such as admissible path, resolution gain, frame-function candidate, or source-function rejection are local results. The ten canonical Output Classes provide system-wide governance routing.

```text
local result
≠ canonical Output Class
```

The class inventory is closed, non-ordinal, and non-stackable for one delimited tested claim:

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

Appendix G and Appendix N own the detailed testing and audit templates. `07_model/Output_Classes.yaml` owns the formal class registry.

### A.7.4 Stop, Failure, and Non-Capture

These are not interchangeable:

| Result concept | Governing question |
| --- | --- |
| **mandatory Stop** | Is further continuation of this claim under the current grounds prohibited? |
| **Failure** | Did the declared transformation fail to satisfy its operation burden? |
| **Non-Capture** | After adequate bounded attempts, does no adequate retained form exist for the capture claim without invention or destructive integration? |

A Stop may preserve a valid weaker result. Failure may be followed by a new transformation claim. Non-Capture preserves partial capture and the unresolved remainder. None licenses erasure of prior records.

```text
new transformation
= new testable claim
```

---

## A.8 Protected Distinction Matrix

| Protected distinction | Admissible relation that remains possible | Collapse prohibited |
| --- | --- | --- |
| operator type ≠ operator occurrence | an occurrence may be typed with an operator function | an occurrence becomes the abstract type |
| operator occurrence ≠ composite | occurrences may be constituents of a composite | co-presence treated as one occurrence or composite automatically |
| configuration ≠ complete world description | several configurations may be valid for different claims | selected structure treated as exhaustive reality |
| event ≠ causal atom | event claims may enter causal research later | event label treated as causal proof |
| missing information ≠ non-event | absence may motivate inquiry | silence treated as supported non-realization |
| frame ≠ granularity | both may change in one operation if separately declared | context and resolution collapsed |
| granularity ≠ relative level | finer resolution may occur at a stable relative level | finer treated as lower or truer automatically |
| relative level ≠ ontological layer | local part–whole or source–target relations may be declared | universal hierarchy inferred |
| chronology ≠ sequence ≠ path | chronology may supply material for a path claim | correct order treated as actual traversal |
| path ≠ trajectory | a path may later meet trajectory criteria | historical extension treated as sedimented load |
| trajectory ≠ path dependence | a trajectory may be weakly path-dependent | all history treated as present constraint |
| provisional elementarity ≠ indivisibility | an object may be left unopened for the current claim | temporary unit treated as final constituent |
| compression ≠ error | compression may be analytically adequate | coarse form rejected merely for being coarse |
| decomposition ≠ truth descent | finer reconstruction may add warranted purchase | detail granted automatic priority |
| source preservation ≠ source immunization | a source claim may be revised or rejected | preservation duty used to protect it from evidence |
| origin type ≠ target function | one object may perform a contextual function | function language silently replaces source type |
| projection ≠ recontextualization | recontextualization may be analytically useful | changed description treated as target function |
| projection ≠ analogy | analogy may be retained as analogy | resemblance treated as functional continuity |
| composite ≠ lossless sum | a composite may retain traceable constituents | selection and loss erased |
| operation occurrence ≠ chain | occurrences may be chained | chain treated as a fourth operation or one merged result |
| Output Class ≠ rank | classes route different results | classes ordered from weak to strong |
| Stop ≠ Failure ≠ Non-Capture | one may follow or coexist with preserved weaker findings in separate claims | governance boundaries collapsed |
| formal consistency ≠ truth | models may validate structure | schema validity treated as substantive warrant |
| graph visibility ≠ evidence | Reader views may improve traceability | visualization treated as historical availability or proof |
| more structure ≠ more authority | additional structure may improve inspectability | detail, level, or formality transfers authority |

---

## A.9 Authority and Governance Boundary

Every definition in this appendix remains analytical and claim-bound. No term authorizes:

- diagnosis or person typing;
- moral, political, legal, or institutional ranking;
- causal attribution without independent evidence;
- prediction or intervention;
- sanction, irreversible labeling, or automated action;
- inheritance of authority from PMS Base, an operator type, a higher relative level, a formal model, a successful transformation, or a visualization.

```yaml
governance:
  authority_inheritance: prohibited
```

The appendix also preserves the formal-model boundary:

```text
machine-readable consistency
≠ empirical truth
≠ semantic validity
≠ normative validity
≠ application authority
```

And the Reader boundary:

```text
visualized branch
≠ historically available branch

graph edge
≠ admissible transformation automatically
```

---

## A.10 Definition Ownership and Downstream Handoffs

| Definition family | Primary owner | Appendix A role | Downstream handoff |
| --- | --- | --- | --- |
| PMS Base and authority boundary | `PMS.yaml`; Chapter 0 | minimal orientation only | Front Matter, Appendix G, Appendix N |
| object categories and identity | Chapter 1 | expanded table and taxonomy | Appendix B, C, H, I |
| coordinates | Chapter 2 | short definitions only | Appendix B, C, G |
| temporal object chain | Chapters 3, 9–14 | path-status consolidation | Appendix H, I, J, M |
| COMPOSE | Chapters 4 and 15 | short operation definition only | Appendix D, G, H, N |
| compressed source object | Chapter 18 | expanded source taxonomy | Appendix E, L |
| DECOMPOSE | Chapters 4 and 20 | short operation definition only | Appendix E, G, H, L, N |
| origin type and target function | Chapters 5 and 29 | extended projection definitions | Appendix B, F, H, I, K |
| PROJECT_AS | Chapters 4 and 30 | short operation definition only | Appendix F, G, H, K, N |
| Output Classes | Minified Kernel and `Output_Classes.yaml` | inventory and boundary only | Appendix G, H, I, N |
| case instantiations | `03_cases/*` | no case catalogue here | Appendix H–M |
| integrated audit | Chapter 53 | terminology handoff only | Appendix N |

---

## A.11 Completion Boundary

Appendix A is complete for its assigned migration burden when:

- object categories are consolidated without redefining PMS Base;
- expanded path statuses remain distinct from Output Classes;
- source-object types preserve the operator-type boundary and reasons not to decompose;
- RETYPE definitions preserve origin type, target function, context, and continuity;
- all three operations remain the only core operations;
- primary definition sites are explicit;
- protected non-equivalences and authority limits are visible;
- no new primitive, class, Rule, field requirement, person category, or application authority is introduced.

The present result satisfies those conditions at a substantive bounded provisional level.

```text
Appendix A complete
→ definition consolidation available

Appendix A complete
≠ Reference Freeze
≠ Integrated Corpus Audit
≠ final release lock
```

**Next controlled appendix:** Appendix B — Formal Notation.
