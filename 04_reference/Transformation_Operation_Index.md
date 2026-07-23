# PMS-STRATA — Transformation Operation Index

**Status:** Reference Kernel v0.1.34; Chapter-10-WP2-synchronized operation and record navigation  
**Repository role:** `04_reference/*` — terminology and cross-reference layer; not an independent theory source  
**Canonical operation inventory:** `COMPOSE`, `DECOMPOSE`, `PROJECT_AS`  
**Primary control sources:** `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`, `05_minified/PMS_STRATA_Minified_Canonical.md`, `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`, and `05_minified/Chapter_Contracts.md`  
**PMS Base boundary:** `PMS.yaml`

---

## 1. Role, Status, and Authority

This index stabilizes the identity, comparison, navigation, and boundary conditions of the three canonical STRATA operations during Block production while preserving its pre-Block control baseline.

It records:

- the canonical operation inventory;
- the shared anatomy of a STRATA operation occurrence;
- compact signatures and result identities;
- valid source and target classes;
- preservation, continuity, loss, and admissibility duties;
- operation-specific confusion gates;
- operation-chain rules;
- local-result to canonical-output mapping;
- primary definition sites and later operationalization handoffs.

This index does **not**:

- define a fourth operation;
- alter PMS Base or the Δ–Ψ inventory;
- replace the prose of Chapters 4, 15, 20, or 30;
- replace the canonical Minified Kernel;
- create final YAML or JSON Schema fields;
- decide empirical truth, causal adequacy, semantic validity, or normative legitimacy;
- authorize person typing, diagnosis, sanctions, or intervention;
- make a successful transformation more authoritative than its sources and claim type permit.

Canonical authority rule:

```text
more structure
≠
more authority
```

Canonical availability rule:

```text
available transformation
≠
admissible transformation
```

---



### 1.1 Chapter 1 object-model handoff

The provisionally locked Chapter 1 supplies the operation-eligible object vocabulary and category limits used by this index and mirrored in `07_model/Operation_Registry.yaml`:

```text
operator occurrence
composite structure
configuration
event-like object
non-event structure
transition as object
derived analytical object or function
```

This list is an open controlled handoff, not a closed ontology or automatic admissibility rule. Abstract PMS operator types may be referenced for typing but are not themselves STRATA transformation sources and may never be decomposed. Operation-specific source and target contracts remain owned by Chapters 4 and the relevant Parts.

## 2. Canonical Operation Inventory

PMS-STRATA contains exactly three canonical transformation operation types:

```text
COMPOSE
DECOMPOSE
PROJECT_AS
```

No other analytical movement is a fourth STRATA operation.

| Operation type | Canonical question | Transformation direction | Primary result identity | Primary definition site | Full operationalization site |
|---|---|---|---|---|---|
| `COMPOSE` | How may multiple or sequential source structures form a declared composite analytical object? | many or sequential source structures → composite object | new analytical composite | Chapter 4 — The Three STRATA Operations | Chapter 15 — COMPOSE |
| `DECOMPOSE` | How may a provisionally compressed occurrence or composite be reconstructed under finer granularity? | compressed occurrence or composite → finer relational reconstruction | same reference object reconstructed more finely | Chapter 4 — The Three STRATA Operations | Chapter 20 — DECOMPOSE |
| `PROJECT_AS` | What bounded function may an origin-typed source object perform within a declared target context? | origin-typed source object → contextual target function | added bounded functional relation | Chapter 4 — The Three STRATA Operations | Chapter 30 — PROJECT_AS |

Canonical exclusions:

```text
LIMITS
≠
operation
```

```text
Φ Recontextualization
≠
PROJECT_AS
```

```text
PMS operator composition
≠
Σ Integration
≠
STRATA COMPOSE
```

```text
operation chain
≠
compound fourth operation
```

---

## 3. Operation Type, Operation Occurrence, and Operation Chain

### 3.1 Operation type

An **operation type** is one of the three canonical transformation forms: `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

The operation type specifies:

- the transformation question;
- the direction of analytical movement;
- the identity relation between source and result;
- the kind of result that may be produced;
- the preservation and loss duties that apply;
- the characteristic failure modes.

Operation types are not empirical objects and are not themselves decomposable source material.

### 3.2 Operation occurrence

An **operation occurrence** is a particular declared use of one operation type on specified source structures within a bounded transformation context.

Every occurrence remains:

- reference-bound;
- source-bound;
- frame- or context-bound;
- granularity-declared;
- relative-level-declared;
- claim-bound;
- loss-aware;
- independently testable and stoppable.

An operation occurrence is not identical with its output.

```text
operation occurrence
≠
operation type
≠
result object or function
```

### 3.3 Operation chain

An **operation chain** is a sequence of separately declared operation occurrences.

Each link requires its own:

- source and target declaration;
- classification;
- justification;
- expected praxeological difference;
- preservation and continuity assessment;
- loss account;
- admissibility result;
- validity scope;
- Stop and Non-Capture possibility.

No chain creates a new core operation.

---

## 4. Shared Anatomy of a STRATA Operation

Every operation occurrence must make the following declaration families inspectable. These are conceptual requirements, not a final machine schema.

### 4.1 Source declaration

Identify:

- source object or source set;
- source-side typing;
- source frame;
- source granularity;
- source relative level;
- temporal scope where relevant;
- source basis and evidential limits;
- current claim scope.

### 4.2 Operation declaration

Identify:

- operation type;
- transformation question;
- transformation context;
- justification;
- expected praxeological difference;
- operation-specific constitutive decisions;
- alternative operation or no-operation option.

### 4.3 Target declaration

Identify, as appropriate:

- target object;
- target object class;
- target function;
- target frame or target context;
- target granularity;
- target relative level;
- validity scope.

Not every operation produces both a target object and a target function.

```text
COMPOSE
→ target object
```

```text
DECOMPOSE
→ finer reconstruction of the same reference object
```

```text
PROJECT_AS
→ target function in a declared context
```

### 4.4 Claim declaration

Identify:

- claim type;
- claim scope;
- claim ceiling;
- provisional or contested status where applicable;
- what the operation does **not** license.

### 4.5 Preservation and continuity declaration

Assess:

- reference continuity;
- type continuity;
- functional continuity where a function is at issue;
- temporal continuity where historical ordering matters;
- constitutive relations that must remain visible.

### 4.6 Loss declaration

Every operation must disclose at least:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

`PROJECT_AS` may additionally distinguish foregrounded and backgrounded features, but it remains governed by the shared loss categories.

### 4.7 Admissibility declaration

Assess:

- PraxisPurchase;
- TraceableLoad;
- TypeIntegrity;
- Reference Continuity;
- Functional Continuity where applicable;
- Contextual Boundedness;
- Counterfactual Sensitivity;
- Source Ceiling;
- calibration limits;
- alternatives;
- Stop;
- Non-Capture;
- authority ceiling.

### 4.8 Result declaration

Record both:

1. the operation-specific local result; and
2. the mapped canonical output class.

```text
local operation result
→
canonical output class
```

A local result label does not become an eleventh output class.

---

## 5. Comparative Operation Identity Matrix

| Control dimension | `COMPOSE` | `DECOMPOSE` | `PROJECT_AS` |
|---|---|---|---|
| Source plurality | normally multiple or sequential sources | one identifiable compressed occurrence or composite | one independently identified source object |
| Primary movement | formation | finer reconstruction | functional projection |
| Reference logic | forms a new composite while preserving source trace | preserves the source object as reconstruction target | preserves source reference and origin type |
| Granularity relation | may remain stable or change; composition often compresses, but has no fixed granularity direction | target granularity is finer relative to source | may change or remain stable; function relation is primary |
| Relative-level relation | often relatively upward | often relatively downward | contextual function across a declared relation |
| Primary result | composite analytical object | components, relations, internal temporality, and source-function status | bounded target function |
| Source-function role | not primary | confirmed, refined, differentiated, partially preserved, rejected, or underdetermined | source-side identity remains distinct from target function |
| Target-function role | not produced automatically | not assigned by DECOMPOSE | constitutive output relation |
| Main constitutive duty | selection + ordering + formation | components + relations + coarser-function test | source trace + origin-type preservation + contextual boundedness |
| Main lower-bound risk | chronology or aggregation without gain | added detail without purchase | renaming without functional gain |
| Main upper-bound risk | macro-label without path trace or constitutive source-relation trace, as applicable | fragmentation or unsupported microstructure | function without traceable load |
| Central confusion | chronology, aggregation, projection | description, atomization, new PATH, projection | recontextualization, analogy, label substitution, type jump |
| Part emphasis | PATH | SUB | RETYPE |

Shared rule:

```text
operation direction
≠
ontological direction
```

Shared non-compensation rule:

```text
formal elegance or detail quantity
cannot compensate for
missing relevance, traceability, or type integrity
```

---

## 6. `COMPOSE`

### 6.1 Canonical identity

`COMPOSE` forms a declared composite analytical object from multiple temporally or structurally related source objects while making selection, ordering, formation, preservation, compression, and loss explicit.

```text
many or sequential source structures
→
new composite analytical object
```

**Primary definition site:** Chapter 4  
**Full procedure:** Chapter 15  
**Principal Part:** PATH  
**Current control source:** `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`

### 6.2 Minimal analytical signature

```text
COMPOSE:
(S, source coordinates, ordering and relation structure, justification)
→
(composite object, declared object class, target coordinates, loss, validity scope)
```

Where:

- `S` is a declared source set or sequence;
- the ordering and relation structure explains why the sources belong together;
- the result is a new analytical composite;
- loss and validity remain explicit.

This signature is a specification of analytical commitments, not a mathematical law.

### 6.3 Valid source-object families

Possible source objects include:

- configurations;
- transitions;
- events;
- non-events;
- subpaths;
- branch structures;
- partial trajectories;
- operator-typed occurrences;
- prior composite structures.

A source list is not enough. The compositional relation must be stated.

### 6.4 Valid target-object families

Possible composite object classes include:

- sequence;
- path;
- trajectory;
- event cluster;
- branch structure;
- phase;
- another explicitly declared composite.

The following are **not** automatic COMPOSE outputs:

- frame-function;
- macro-event function;
- attractor-function;
- asymmetry-function;
- binding-function;
- integration-function;
- another contextual target function.

Such a function requires a separate `PROJECT_AS` occurrence.

A trajectory object and a path-dependence claim remain distinct:

```text
trajectory
≠
path dependence
```

`COMPOSE` may form a trajectory. Path dependence remains a separately warranted property claim about historical determination.

### 6.5 Preconditions

A COMPOSE candidate requires:

1. identifiable source objects;
2. a declared frame;
3. a declared temporal scope where relevant;
4. a warranted temporal or structural relation;
5. an explicit selection rule;
6. an explicit ordering rule where order matters;
7. an explicit formation rule;
8. sufficient source support;
9. an expected praxeological difference;
10. a possible loss account;
11. a bounded composite claim;
12. an explicit Stop condition.

### 6.6 Selection rule

The selection rule must state:

- why each included source matters;
- why omitted sources are omitted;
- which sources are load-bearing;
- which are illustrative;
- which selections remain contested;
- what alternative selection would produce a rival composition.

Selection is constitutive, not clerical.

```text
selected sources
≠
all available sources
```

### 6.7 Ordering rule

Possible ordering forms include:

- linear order;
- partial order;
- overlapping transitions;
- parallel subpaths;
- uncertain order;
- retrospective periodization disclosed as such.

Temporal order does not by itself establish a path or trajectory.

```text
ordered items
→ possible sequence
```

```text
source-supported connected transitions
→ possible path
```

```text
path + sedimentation + historically altered continuations
→ possible trajectory
```

### 6.8 Formation rule

The formation rule explains why the target is more than a list, chronology, or aggregation.

It must identify:

- constitutive relations;
- transition logic;
- source dependencies;
- structural connection;
- praxeological load added by the composite;
- what object class the result actually satisfies.

### 6.9 Preservation duties

COMPOSE preserves, where constitutive:

- source trace;
- relevant temporal order;
- load-bearing transitions;
- central events and non-events;
- historical asymmetries;
- binding structures;
- branch points and lost alternatives;
- heterogeneity needed for the target claim;
- source-type distinctions.

Preservation is not total retention. It is sufficient reconstructive dependence.

### 6.10 Loss duties

Typical composition losses include:

- fine local detail;
- internal variation;
- parallel minor paths;
- fine temporal resolution;
- separability of local costs;
- visibility of alternatives;
- recoverability of intermediate states.

A COMPOSE claim must not present compression as losslessness.

### 6.11 Counterfactual sensitivity

Core test:

> Would removing, reordering, or materially changing a load-bearing source element alter the composite object or its warranted claim?

Interpretation:

- strong sensitivity supports constitutive load;
- partial sensitivity may support a bounded claim;
- weak sensitivity requires scrutiny;
- insensitivity risks macro-label elasticity;
- underdetermination may require provisional status or claim reduction.

### 6.12 Local result families

Possible local result descriptions include:

- admissible sequence;
- admissible path;
- admissible trajectory;
- admissible path-dependence claim;
- admissible declared composite;
- provisional composition;
- competing compositions;
- reduced composition claim;
- failed composition;
- operation-specific mandatory stop;
- operation-specific non-capture.

These are local descriptions, not canonical output classes.

### 6.13 Central failure modes

COMPOSE fails, requires reduction, or must stop when:

- chronology is presented as path;
- aggregation is presented as functional formation;
- no load-bearing relation connects the sources;
- selection is narratively convenient but unsupported;
- ordering is imposed retroactively without disclosure;
- teleology determines source selection;
- non-events, asymmetries, alternatives, or reversals disappear;
- constitutive heterogeneity is destroyed;
- the source path or constitutive source-relation trace, as applicable, is no longer reconstructible;
- the target label ignores material source changes;
- no additional praxeological discrimination is produced;
- a target function is asserted without `PROJECT_AS`.

### 6.14 COMPOSE confusion gates

#### COMPOSE or chronology?

```text
time-sorted items only
→ chronology or sequence
```

```text
connected transitions with source-supported structural load
→ COMPOSE candidate
```

#### COMPOSE or aggregation?

```text
quantity or co-presence only
→ aggregation
```

```text
constitutive relations produce a new analytical object
→ COMPOSE candidate
```

#### COMPOSE or PROJECT_AS?

```text
new composite object
→ COMPOSE
```

```text
bounded function of an already identified object in a target context
→ PROJECT_AS
```

A typical admissible chain is:

```text
configurations
COMPOSE
trajectory

trajectory
PROJECT_AS
frame-function
```

### 6.15 COMPOSE mandatory-stop conditions

Stop is mandatory where:

- no formation beyond chronology or aggregation is established;
- selection becomes arbitrary;
- source support no longer carries the relation;
- the Relevance Floor is undercut;
- the Traceability Ceiling is exceeded;
- the composite becomes insensitive to source changes;
- further composition merely repeats a macro-label;
- continuation would conceal a prior failed claim.

### 6.16 COMPOSE Non-Capture conditions

Non-Capture may be appropriate where:

- no stable ordering is reconstructible;
- competing compositions remain equally supported;
- every available composition destroys constitutive heterogeneity;
- source gaps prevent identification of load-bearing transitions;
- the object is better left as multiple unresolved structures.

### 6.17 COMPOSE completion gate

Before accepting a COMPOSE occurrence, verify:

- What is being composed?
- Why may the sources be related?
- What selection rule is used?
- What ordering rule is used?
- What formation rule creates the object class?
- What new composite is formed?
- What remains source-traceable?
- What is compressed, excluded, uncertain, or irrecoverable?
- What source change would alter the result?
- What claim is licensed?
- What target-function claim is not yet licensed?
- When must composition stop?

---

## 7. `DECOMPOSE`

### 7.1 Canonical identity

`DECOMPOSE` reconstructs a provisionally compressed operator occurrence or composite as a relational organization of finer structures under declared granularity while preserving or testing the same reference object and its coarser function.

```text
compressed occurrence or composite
→
finer relational reconstruction of the same reference object
```

**Primary definition site:** Chapter 4  
**Full procedure:** Chapter 20  
**Principal Part:** SUB  
**Current control source:** `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`

### 7.2 Minimal analytical signature

```text
DECOMPOSE:
(source object, origin type, source function, source coordinates, decomposition question)
→
(finer components, component relations, internal temporality, source-function result, loss, validity scope)
```

The result is a finer reconstruction of the same reference object, not automatically a new source object and not a contextual target function.

### 7.3 Valid source-object families

DECOMPOSE may operate on the following only insofar as they are concrete occurrences or provisionally compressed composites:

- concrete operator-typed occurrences;
- configurations;
- events;
- non-events;
- transitions;
- institutional or relational arrangements;
- paths;
- trajectories;
- phases;
- branch clusters;
- declared composite structures.

DECOMPOSE does not operate on Δ–Ψ operator types as material composites.

```text
operator type
≠
decomposable occurrence
```

### 7.4 Preconditions

A DECOMPOSE candidate requires:

1. an identifiable source object;
2. visible source-side typing;
3. a declared source frame and granularity;
4. a precise decomposition question;
5. a reason the current compression may be insufficient;
6. an expected additional praxeological difference;
7. a declared finer target granularity;
8. sufficient source support;
9. a criterion for reference preservation;
10. a test for the source or coarser function;
11. an explicit Stop condition.

### 7.5 Decomposition question

The decomposition question must specify what internal structure is being tested.

Examples of question forms:

- Which finer structures constitute this frame-typed occurrence?
- Which repeated practices reproduce this attractor-typed occurrence?
- Which local relations carry this asymmetry-typed occurrence?
- Which subpaths, transitions, and residues carry this trajectory?
- Which delays and blocked responsibilities produce this structured non-event?

The question is about a concrete source object, never about what a PMS operator type is “made of.”

### 7.6 Component-and-relation duty

A valid decomposition reconstructs both:

```text
components
+
relations among components
```

Possible components include:

- finer operator-typed occurrences;
- local configurations;
- subevents;
- non-events;
- transitions;
- roles;
- resource and access relations;
- subpaths;
- reproduction practices;
- thresholds and feedbacks.

Possible relations include:

- temporal order;
- dependency;
- feedback;
- reinforcement;
- compensation;
- substitution;
- asymmetric load distribution;
- conditions of persistence.

A parts list without relations is fragmentation.

### 7.7 Granularity duty

DECOMPOSE must state:

- source granularity;
- target granularity;
- distinctions added;
- whether the frame remains stable;
- whether reference remains stable;
- expected praxeological difference;
- comparability limits.

Finer granularity does not imply:

- deeper truth;
- ontological depth;
- greater authority;
- explanatory superiority;
- final constituents.

### 7.8 Reference and source-function duties

The source object remains the reconstruction target.

The prior source function may be:

- confirmed;
- refined;
- internally differentiated;
- partially preserved;
- rejected;
- underdetermined.

Preservation does not immunize the prior function. It keeps the source object and claim available for critical testing.

Operation admissibility and source-function effect are separate results. A valid `DECOMPOSE` occurrence may reject a prior source-function claim without becoming a `failed_transformation`. The operation receives its own canonical class; the prior source claim is separately recorded as failed, withdrawn, or reduced, as warranted.

### 7.9 Source-support duty

The finer reconstruction must not exceed the semantic and evidential precision of its sources.

Distinguish:

- directly supported components;
- indirectly reconstructed relations;
- uncertain internal structure;
- unavailable structure;
- rival internal models.

```text
formal detail
≠
source-supported detail
```

### 7.10 Resolution-gain test

Core question:

> Which warranted reconstruction or claim changes because of the added distinctions?

Possible local resolution descriptions:

- resolution gain;
- resolution neutral;
- resolution drift;
- resolution escape;
- unsupported;
- non-capture.

Resolution neutrality is a legitimate result but not a strong decomposition gain.

### 7.11 Counterfactual component test

Core question:

> Would changing or removing this component alter the reconstructed source function?

Possible component statuses:

- constitutive;
- strongly modulating;
- weakly modulating;
- replaceable;
- incidental;
- underdetermined.

The component status is not itself a canonical output class.

### 7.12 Local result families

Possible local result descriptions include:

- admissible decomposition;
- source function confirmed;
- source function refined;
- source function internally differentiated;
- source function partially preserved;
- source function rejected;
- source function underdetermined;
- heterogeneous source object;
- competing internal models;
- competing decompositions;
- resolution-neutral result;
- unsupported decomposition;
- resolution drift;
- operation-specific mandatory stop;
- operation-specific non-capture.

### 7.13 Central failure modes

DECOMPOSE fails, requires reduction, or must stop when:

- a base operator type is treated as a material composite;
- no identifiable source object exists;
- finer details are listed without relations;
- changed wording is presented as changed granularity;
- the source object disappears into fragments;
- the coarser function can no longer be evaluated;
- internal precision exceeds source support;
- added detail creates no praxeological purchase and is misreported as gain;
- complexity rises without discrimination;
- an objection is moved to ever-finer detail rather than answered;
- a competing path composition is misclassified as decomposition;
- a contextual function is asserted without `PROJECT_AS`.

### 7.14 DECOMPOSE confusion gates

#### DECOMPOSE or description?

```text
more words or examples about the same object
≠
finer relational reconstruction
```

DECOMPOSE requires added distinctions, relations, and a declared granularity change.

#### DECOMPOSE or atomization?

```text
parts without relations or source-function trace
→ fragmentation
```

```text
finer components + relations + source-object continuity
→ DECOMPOSE candidate
```

#### DECOMPOSE or new PATH?

```text
opening the same path or trajectory object
→ DECOMPOSE
```

```text
selecting and forming a different path object
→ new COMPOSE
```

#### DECOMPOSE or PROJECT_AS?

```text
internal constitution, reproduction, or destabilization
→ DECOMPOSE
```

```text
bounded function in a declared target context
→ PROJECT_AS
```

A case may require both, but the records remain separate.

### 7.15 DECOMPOSE mandatory-stop conditions

Stop is mandatory where:

- the Relevance Floor is undercut;
- sources do not support finer reconstruction;
- the source object is no longer reconstructible;
- components remain unrelated;
- calibration declines as complexity increases;
- further detail merely shifts an unresolved objection;
- the source-function test becomes impossible through fragmentation.

### 7.16 DECOMPOSE Non-Capture conditions

Non-Capture may be appropriate where:

- no stable internal structure can be reconstructed;
- rival decompositions remain equally viable;
- decisive components or relations remain inaccessible;
- every finer reconstruction destroys the coarser reference object;
- no granularity is simultaneously relevant, traceable, and source-supported.

### 7.17 DECOMPOSE completion gate

Before accepting a DECOMPOSE occurrence, verify:

- What source object is being opened?
- Is it an occurrence or composite rather than an operator type?
- Why may the current compression be insufficient?
- What finer granularity is declared?
- Which distinctions are added?
- Which components are reconstructed?
- Which relations make them relevant?
- What happens to the source function?
- What evidence supports the added detail?
- What warranted claim changes?
- When does resolution become neutral, drifting, escaping, or unsupported?
- When must decomposition stop?

---

## 8. `PROJECT_AS`

### 8.1 Canonical identity

`PROJECT_AS` projects an origin-typed source object as a bounded function within a declared target context while preserving source reference and origin type.

```text
origin-typed source object
→
bounded contextual target function
```

**Primary definition site:** Chapter 4  
**Full procedure:** Chapter 30  
**Principal Part:** RETYPE  
**Current control source:** `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`

### 8.2 Minimal analytical signature

```text
PROJECT_AS:
(source object, origin type, source coordinates, target context, justification)
→
(bounded target function, target coordinates, loss, validity scope)
```

Canonical identity rule:

```text
same source reference
+
preserved origin type
+
new bounded contextual function
=
projection candidate
```

Not:

```text
new contextual function
=
new origin type
```

### 8.3 Valid source-object families

PROJECT_AS may operate on an independently identified PMS or STRATA object, including:

- operator-typed occurrence;
- configuration;
- event or non-event structure;
- path;
- trajectory;
- recurrent trajectory form;
- phase;
- composite structure;
- operator-weighting or modulating profile.

Projection cannot replace source-side object construction.

### 8.4 Valid target-function families

Possible bounded functions include:

- frame-function;
- macro-event function;
- attractor-function;
- asymmetry-function;
- binding-function;
- integration-function;
- modulating function;
- higher-level boundary function;
- another explicitly justified derived function.

All such functions remain:

- contextual;
- relational;
- derived;
- source-traceable;
- claim-bounded;
- non-primitive.

### 8.5 Preconditions

A PROJECT_AS candidate requires:

1. an identifiable source object;
2. a determined origin type;
3. declared source frame, granularity, and relative level;
4. a declared target context;
5. declared target granularity and relative level;
6. a precisely named target function;
7. an expected additional praxeological difference;
8. a constitutive source trace;
9. Counterfactual Sensitivity;
10. bounded validity scope;
11. explicit loss;
12. at least one relevant alternative, including no projection;
13. an explicit Stop condition.

### 8.6 Origin-type preservation

The source object remains what it was in its source reconstruction.

```text
trajectory
PROJECT_AS
frame-function

≠

trajectory becomes Frame as origin type
```

```text
functions as Α
≠
is Α as a new primitive
```

A failed projection does not invalidate an independently warranted source object.

### 8.7 Constitutive Source Trace

The projection must distinguish:

- load-bearing source features;
- modulating features;
- foregrounded features;
- backgrounded features;
- compressed features;
- excluded features;
- uncertain features.

The target function must depend on specific source structures rather than terminology, resemblance, or target fit alone.

### 8.8 Contextual boundedness

The target function must be bounded by:

- target object or scene;
- target frame;
- temporal scope;
- relative target level;
- affected roles or structures;
- affected praxeological dimensions;
- validity duration;
- transfer limits;
- claim ceiling.

A locally warranted function does not automatically generalize to all later scenes, all comparable objects, or all members of a group.

### 8.9 Counterfactual sensitivity

Core question:

> Would a relevant change in a load-bearing source structure alter, weaken, or defeat the target function?

Interpretation:

- strong sensitivity supports source dependency;
- partial sensitivity may support a bounded function;
- weak sensitivity requires reduction or additional testing;
- insensitivity risks label substitution;
- underdetermination may require provisional status or Non-Capture.

Counterfactual Sensitivity is a load test, not a causal proof.

### 8.10 Projection loss

Projection changes analytical visibility even while reference and origin type remain preserved.

In addition to the shared loss structure, record where relevant:

- foregrounded source features;
- backgrounded features;
- compressed functional dimensions;
- excluded alternative readings.

No projection is presumed perspective-neutral or lossless.

### 8.11 Local result families

Possible local result descriptions include:

- admissible functional projection;
- admissible narrow projection;
- compatible multiple projections;
- competing projections;
- provisional projection;
- context-dependent projection;
- useful structural analogy;
- label substitution;
- invalid type jump;
- unmarked level mixing;
- mandatory claim reduction;
- operation-specific mandatory stop;
- operation-specific non-capture.

`analogy_only` is a legitimate bounded result. It is not a failed attempt disguised as projection.

### 8.12 Central failure modes

PROJECT_AS fails, requires reduction, or must stop when:

- no target context is declared;
- the target function is merely a new label;
- the origin type is replaced;
- source and target levels are mixed or unmarked;
- source trace is absent;
- the function ignores material source changes;
- analogy is presented as semantic identity;
- formal or executable mapping is treated as praxeological proof;
- a local function is globalized;
- a macrofunction becomes a person or group essence;
- historical development is flattened into a timeless type;
- a failed source claim is rescued by relocation;
- a target function becomes a hidden primitive;
- no additional praxeological discrimination is produced.

### 8.13 PROJECT_AS confusion gates

#### PROJECT_AS or Recontextualization?

```text
new frame or reading only
→ possible Φ Recontextualization
```

```text
explicit target function + source trace + bounded validity
→ PROJECT_AS candidate
```

#### PROJECT_AS or analogy?

```text
similar form without established semantic and praxeological continuity
→ analogy
```

```text
source-dependent function in a declared target context
→ PROJECT_AS candidate
```

#### PROJECT_AS or label substitution?

```text
new PMS terminology without changed reconstruction
→ label substitution
```

```text
discriminative target function sensitive to source changes
→ PROJECT_AS candidate
```

#### PROJECT_AS or origin-type replacement?

```text
X functions as F in context C
→ possible projection
```

```text
X therefore is operator type F or new primitive
→ invalid type jump
```

### 8.14 PROJECT_AS mandatory-stop conditions

Stop is mandatory where:

- no additional functional gain exists;
- Source Trace cannot be established;
- origin type cannot remain visible;
- target context becomes arbitrary;
- analogy and projection cannot be distinguished;
- the function becomes source-insensitive;
- scope inflation cannot be bounded;
- continuation would rescue rather than retest a failed claim.

### 8.15 PROJECT_AS Non-Capture conditions

Non-Capture may be appropriate where:

- no target function satisfies relevance, traceability, type integrity, and boundedness together;
- multiple projections remain equally supported and non-integrable;
- the source object adds no warranted function in the target context;
- every projection destroys constitutive source structure;
- a rival grammar captures the relation more adequately.

### 8.16 PROJECT_AS completion gate

Before accepting a PROJECT_AS occurrence, verify:

- What is the independently identified source object?
- What is its origin type?
- What is the target context?
- What exactly is the target function?
- Which source features carry that function?
- What source change would alter or defeat it?
- What is foregrounded, backgrounded, compressed, excluded, uncertain, or irrecoverable?
- How far and how long does the function apply?
- What rival function or no-projection option exists?
- Why is this more than Recontextualization, analogy, or renaming?
- When must projection stop?

---

## 9. Operation Classification and Confusion Gates

### 9.1 Primary classification sequence

Use the following sequence before recording a STRATA transformation:

```text
1. Are multiple or sequential source structures formed into a new composite object?
   → COMPOSE candidate

2. Is an identifiable compressed occurrence or composite opened under finer granularity while remaining the reconstruction target?
   → DECOMPOSE candidate

3. Is an independently identified origin-typed source object assigned a bounded function in a declared target context?
   → PROJECT_AS candidate

4. Has only the frame, vocabulary, or point of view changed?
   → no STRATA operation yet; possible Recontextualization

5. Is only a formal or structural resemblance asserted?
   → analogy candidate

6. Has only a PMS label been attached without source-dependent gain?
   → label substitution candidate
```

### 9.2 Cross-operation decision matrix

| Question | If yes | If no or insufficient |
|---|---|---|
| Is a new composite object formed from multiple or sequential sources? | `COMPOSE` candidate | continue classification |
| Does the same identifiable source object remain the target of finer reconstruction? | `DECOMPOSE` candidate | possible new `COMPOSE` or other movement |
| Is a bounded target function claimed in a specified target context? | `PROJECT_AS` candidate | possible Recontextualization, analogy, or no transformation |
| Are components and their relations reconstructed? | supports `DECOMPOSE` | description or fragmentation |
| Are selection, order, and formation explicit? | supports `COMPOSE` | chronology or aggregation |
| Are origin type and target function distinct? | supports `PROJECT_AS` | type-integrity failure |
| Does the result change under material source changes? | supports traceable load | elasticity or label risk |

### 9.3 Changed analytical coordinates are not operations by themselves

```text
changed frame
≠
COMPOSE, DECOMPOSE, or PROJECT_AS automatically
```

```text
changed granularity
≠
DECOMPOSE automatically
```

```text
changed relative level
≠
PROJECT_AS automatically
```

The operation is determined by the transformation relation and result identity, not by vertical language alone.

### 9.4 Dual-operation cases

Some cases require more than one operation.

Example:

```text
trajectory
DECOMPOSE
subpaths and internal transitions

trajectory
PROJECT_AS
frame-function in a later context
```

The operations may share a source object but remain separate claims.

### 9.5 Invalid collapse

The following collapses are prohibited:

```text
COMPOSE = PROJECT_AS
```

```text
DECOMPOSE = PROJECT_AS
```

```text
Recontextualization = PROJECT_AS
```

```text
operator decomposition = occurrence decomposition
```

```text
local result label = canonical output class
```

---

## 10. Operation Chains

### 10.1 Canonical chain inventory

At minimum, STRATA must support and later test:

```text
COMPOSE → PROJECT_AS
COMPOSE → DECOMPOSE
DECOMPOSE → COMPOSE
DECOMPOSE → PROJECT_AS
PROJECT_AS → DECOMPOSE
COMPOSE → PROJECT_AS → DECOMPOSE
```

### 10.2 Chain rule

Every link is a new operation occurrence and a new testable claim.

```text
new transformation
=
new testable claim
```

A later operation does not inherit the admissibility of an earlier operation.

```text
admissible step 1
≠
admissible step 2
```

A later successful operation does not erase an earlier failure.

### 10.3 Chain-specific control questions

For each transition between operation occurrences, ask:

- Is the previous result a valid source object for the next operation?
- Does the next operation require a new target context?
- Has the new source frame been declared?
- Does the granularity relation change?
- Are reference and type continuity still appropriate?
- Is loss from the prior operation carried forward?
- Does the next result depend on the prior compressed or projected form?
- Could the next step proceed if the prior step were rejected?
- Is the chain hiding a fourth compound operation?

### 10.4 Chain handoff matrix

| Chain | Valid source handoff to the next occurrence |
|---|---|
| `COMPOSE → PROJECT_AS` | The valid composite object becomes the independently identified source object for a separate projection claim. |
| `COMPOSE → DECOMPOSE` | The composed object is treated as a provisionally compressed composite and opened as the same reference object; the step is not restoration of the pre-composition source set. |
| `DECOMPOSE → COMPOSE` | Selected finer results become a newly declared source set governed by a new selection, ordering, and formation rule. |
| `DECOMPOSE → PROJECT_AS` | The independently identified source object remains the projection source; finer structures may strengthen or defeat the Constitutive Source Trace. |
| `PROJECT_AS → DECOMPOSE` | The next step may open the retained source object, a concrete occurrence of the projected function, or a composite carrying that function. It never decomposes the target function as an operator type. |
| `COMPOSE → PROJECT_AS → DECOMPOSE` | The third occurrence must state which retained object, concrete function occurrence, or composite is opened and must carry forward the separately declared losses of both prior steps. |

### 10.5 Chain-specific loss

Loss accumulates but does not merge into one undifferentiated record.

```text
loss at step 1
+
loss at step 2
≠
one retroactively reconstructed loss profile
```

Each step retains its own loss declaration. The integrated audit may additionally assess cumulative loss.

### 10.6 Chain-specific failure preservation

Record separately:

- original claim;
- original result;
- later transformation claim;
- later result;
- whether the original objection remains;
- whether later success depends on an inadmissible earlier object.

### 10.7 Chain-specific Stop

A chain must stop where:

- the next source object is not independently identifiable;
- prior loss prevents traceable continuation;
- the next operation only relabels the earlier result;
- type or reference continuity is broken;
- claim rescue replaces claim testing;
- cumulative abstraction exceeds the Traceability Ceiling.

---

## 11. Non-Invertibility

### 11.1 Canonical non-inverse relations

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

### 11.2 Why DECOMPOSE after COMPOSE is not restoration

Reasons include:

- COMPOSE selected and excluded source material;
- some compression may be irrecoverable;
- later decomposition may use new sources;
- the decomposition question may differ from the original composition question;
- competing internal models may appear;
- the original alternative space may no longer be reconstructible.

### 11.3 Why COMPOSE after DECOMPOSE is not restoration

Reasons include:

- the finer reconstruction changes available distinctions;
- the new selection rule may differ;
- different relations may become constitutive;
- rejected or revised source functions alter formation;
- multiple admissible recompositions may exist.

### 11.4 Why PROJECT_AS is not type conversion

PROJECT_AS adds a bounded function relation. It does not convert the source object into a new origin type.

A later removal of the projection does not “restore” a changed type because the origin type was never replaced in an admissible projection.

### 11.5 Reverse movement rule

Any reverse-looking movement is a new operation occurrence with:

- a new question;
- new source and target declarations;
- new loss;
- new admissibility;
- new possible failure.

---

## 12. Shared Admissibility, Continuity, and Loss Duties

### 12.1 Common admissibility form

Every operation remains governed by:

```text
Admissible(T, X, C)
iff
PraxisPurchase
and TraceableLoad
and TypeIntegrity
and ContextualBoundedness
```

This compact form is necessary but not exhaustive. A complete assessment also includes continuity, counterfactual testing, loss, source and calibration limits, alternatives, anti-immunization, Stop, Non-Capture, and claim ceiling.

### 12.2 Operation-specific admissibility emphasis

| Operation | Primary relevance question | Primary traceability question | Primary type-integrity question |
|---|---|---|---|
| `COMPOSE` | Does formation produce a warranted new composite distinction? | Can the composite be reconstructed from selected sources and relations? | Are source types distinguished from the new composite object class? |
| `DECOMPOSE` | Do added distinctions change a warranted reconstruction or claim? | Do components and relations remain tied to the same source object and function test? | Is an occurrence or composite opened rather than an operator type? |
| `PROJECT_AS` | Does the target function add contextual discrimination? | Which source features carry the function, and would their change alter it? | Are source reference and origin type preserved separately from target function? |

### 12.3 Relevance Floor

Below the Praxeological Relevance Floor:

```text
additional distinction or transformation
without changed warranted reconstruction
=
distinction without praxeological purchase
```

Operation-specific forms:

- COMPOSE: chronology or grouping without composite gain;
- DECOMPOSE: more detail without changed reconstruction;
- PROJECT_AS: renaming without functional gain.

### 12.4 Traceability Ceiling

Above the Praxeological Traceability Ceiling:

```text
abstraction without traceable load
```

A label without traceable load is a common operation-specific manifestation of this upper-bound failure.

Operation-specific forms:

- COMPOSE: macro-label without path or constitutive relation trace;
- DECOMPOSE: fragments no longer reconstruct the source object;
- PROJECT_AS: target function no longer depends on source structure.

### 12.5 Reference continuity

Reference continuity asks whether the result still refers appropriately to the historical or structural source object.

- COMPOSE creates a new composite but must retain source trace.
- DECOMPOSE retains the source object as reconstruction target.
- PROJECT_AS retains the same source reference while adding a function.

### 12.6 Type continuity

- COMPOSE does not retroactively rewrite component types.
- DECOMPOSE may test a source typing but does not decompose the operator type.
- PROJECT_AS preserves origin type and distinguishes it from target function.

### 12.7 Functional continuity

- COMPOSE may form a composite with a declared object class, but no contextual target function is automatic.
- DECOMPOSE tests how finer structures carry, revise, or defeat the source function.
- PROJECT_AS requires the target function to remain source-dependent and context-bounded.

### 12.8 Temporal continuity

Temporal continuity matters where sequence, duration, sedimentation, path, trajectory, or historical load are constitutive.

It does not require exhaustive detail. It requires preservation of load-bearing temporal structure.

### 12.9 Loss is operation-specific

| Loss dimension | `COMPOSE` | `DECOMPOSE` | `PROJECT_AS` |
|---|---|---|---|
| Typical preservation | source trace, order, transitions, non-events, alternatives | reference object, origin-type visibility, component relations, source-function test | source reference, origin type, historical load, constitutive source features |
| Typical compression | local variation, minor paths, temporal detail | unavailable internal detail, competing microstructure | non-target functions, backgrounded dimensions |
| Typical exclusion | out-of-scope sources and branches | unsupported or irrelevant finer distinctions | alternative contexts or functions outside validity scope |
| Typical uncertainty | order, periodization, intermediate states | component identity, relations, thresholds | source-function load, transfer limits, semantic preservation |
| Typical irrecoverability | alternatives or local costs lost in composition | internal structure absent from sources | dimensions obscured by functional foregrounding |

### 12.10 Non-compensation principle

No operation becomes admissible through compensating strengths where a mandatory gate fails.

Examples:

```text
high formal precision
+
no source support
≠
admissible DECOMPOSE
```

```text
strong narrative coherence
+
no source trace
≠
admissible COMPOSE
```

```text
useful analogy
+
origin-type collapse
≠
admissible PROJECT_AS
```

---

## 13. Local Results and Canonical Output-Class Mapping

### 13.1 Canonical output inventory

Only these ten system-wide classes are canonical:

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

### 13.2 Mapping rule

Every operation-specific result maps to one canonical class.

Where more than one mapping is possible, the record must state the rationale.

### 13.3 COMPOSE mapping

| COMPOSE local result | Canonical class | Mapping condition |
|---|---|---|
| admissible sequence | `admissible` | sequence claim satisfies its declared scope |
| admissible path | `admissible` | actual connected transitions and selection are traceable |
| admissible trajectory | `admissible` | sedimentation and historical load are established |
| admissible declared composite | `admissible` | the declared object class and its constitutive source relations are warranted |
| admissible path-dependence claim | `admissible` or `admissible_with_bounded_claim` | depends on strength and scope of historical determination |
| provisional composition | `admissible_but_provisional` | material source, periodization, or calibration limits remain |
| competing compositions | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one composition is provisionally preferred while a material rival remains; some shared result remains; or no selection is warranted |
| reduced composition claim | `claim_reduction_required` | stronger object class is not supported but a weaker class is |
| failed composition | `failed_transformation` | COMPOSE identity or admissibility fails |
| operation-specific mandatory stop | `mandatory_stop` | continuation is inadmissible |
| operation-specific non-capture | `non_capture` | no adequate composition can preserve the object |

### 13.4 DECOMPOSE mapping

DECOMPOSE requires separate treatment of operation result, canonical class, source-function effect, and prior source-claim result.

| DECOMPOSE operation result | Canonical class | Mapping condition |
|---|---|---|
| admissible decomposition | `admissible`, `admissible_with_bounded_claim`, or `admissible_but_provisional` | select according to whether the operation passes as declared, requires a material claim boundary, or remains usable under material provisional support limits; record source-function effect separately |
| heterogeneous source object | `admissible_with_bounded_claim`, `admissible_but_provisional`, or `partially_admissible` | heterogeneity materially narrows one whole claim, leaves a usable but provisional whole-object claim, or supports only separable parts |
| competing internal models | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one model is provisionally preferred while a material rival remains; a shared partial reconstruction remains; or no warranted retained result is available |
| resolution-neutral result | `resolution_neutral` | a supported finer-resolution test does not change the warranted reconstruction |
| competing decompositions | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one decomposition is provisionally preferred while a material rival remains; partial common structure exists; or no choice is warranted |
| unsupported decomposition | `failed_transformation` | sources do not support the finer reconstruction |
| resolution drift | `mandatory_stop` or `failed_transformation` | continuation must stop, or the attempted decomposition fails |
| operation-specific mandatory stop | `mandatory_stop` | continuation is inadmissible |
| operation-specific non-capture | `non_capture` | no adequate finer reconstruction is available |

Source-function effects remain separately recorded:

| Source-function effect | Control rule |
|---|---|
| confirmed | does not by itself determine the DECOMPOSE canonical class |
| refined | may require a revised source claim but does not automatically produce `admissible_with_bounded_claim` |
| internally differentiated | does not by itself determine whether the whole operation is bounded, provisional, or partial |
| partially preserved | does not by itself classify the DECOMPOSE occurrence |
| rejected | an admissible DECOMPOSE may reject the prior claim without becoming `failed_transformation` |
| underdetermined | may contribute to `admissible_but_provisional` or `non_capture`, but the operation-level rationale remains required |

### 13.5 PROJECT_AS mapping

| PROJECT_AS local result | Canonical class | Mapping condition |
|---|---|---|
| admissible functional projection | `admissible` | all projection duties pass |
| admissible narrow projection | `admissible_with_bounded_claim` | function is warranted only in a narrow context or scope |
| provisional projection | `admissible_but_provisional` | source, counterfactual, or calibration limits remain material |
| context-dependent projection | `admissible` or `admissible_with_bounded_claim` | ordinary declared target-context boundedness supports `admissible`; use the bounded class only where a material narrowing relative to the tested claim is decisive |
| compatible multiple projections | `admissible` or `admissible_with_bounded_claim` | ordinary complete context separation may be `admissible`; material reach restrictions support the bounded class |
| competing projections | `admissible_but_provisional`, `partially_admissible`, or `non_capture` | one projection is provisionally preferred while a material rival remains; partial functions remain; or no warranted selection exists |
| useful structural analogy | `analogy_only` | similarity is retained without functional projection |
| label substitution | `failed_transformation` | no source-dependent functional gain exists |
| invalid type jump | `failed_transformation` | origin type is overwritten or a primitive is invented |
| unmarked level mixing | `failed_transformation` | source and target positions collapse |
| mandatory claim reduction | `claim_reduction_required` | only a weaker function or analogy remains |
| operation-specific mandatory stop | `mandatory_stop` | continuation is inadmissible |
| operation-specific non-capture | `non_capture` | no adequate projection is available |

### 13.6 Mapping cautions

```text
admissible
≠
empirically true
```

```text
failed_transformation
≠
non_capture
```

```text
mandatory_stop
≠
optional stop
```

```text
analogy_only
≠
failed PROJECT_AS in every respect
```

```text
partially_admissible
≠
whole-chain validation
```

Detailed output definitions remain assigned to `04_reference/Output_Class_Index.md`.

---

## 14. Stop, Failure, Claim Reduction, and Non-Capture

### 14.1 Stop

Stop is a positive methodological result.

**Mandatory Stop** applies where continuation would violate relevance, traceability, source, type, context, calibration, or anti-immunization constraints.

**Optional Stop** applies where further transformation may be admissible but is unnecessary for the present claim.

### 14.2 Failure

A failed transformation does not satisfy its own defining or admissibility conditions.

Failure may be local:

- a COMPOSE attempt fails while source objects remain valid;
- a DECOMPOSE attempt fails while the coarser object remains usable;
- a PROJECT_AS attempt fails while the source object remains valid.

Failure of one operation does not authorize silent substitution of another operation.

### 14.3 Claim reduction

Claim reduction is required where a narrower claim remains supported.

Typical reductions include:

```text
trajectory → path
path → sequence
strong path dependence → bounded order dependence
projection → analogy
broad target function → narrow target function
```

Support downgrade and resolution outcome remain separate:

```text
supported → provisional → underdetermined
= support-status change, not Claim Reduction

tested resolution-gain claim
→ resolution-neutral result
→ resolution_neutral
= operation result and output handoff, not Claim Reduction
```

The original stronger claim remains recorded as reduced or failed. It is not silently rewritten.

### 14.4 Non-Capture

Non-Capture preserves the result that the present grammar, source basis, granularity, composition, or projection cannot adequately capture the object or claim.

Possible operation-linked forms include:

- compositional Non-Capture;
- granularity Non-Capture;
- projection Non-Capture;
- source Non-Capture;
- calibration Non-Capture;
- partial capture.

Non-Capture must state:

- what was attempted;
- what remains captured;
- what remains uncaptured;
- why further operation is not warranted;
- whether a rival or external representation may be better;
- possible re-entry conditions.

### 14.5 Stop versus failure versus Non-Capture

| Result | Central meaning | What remains possible |
|---|---|---|
| optional stop | further work is unnecessary | later re-entry under a new question |
| mandatory stop | further continuation would be inadmissible | re-entry only with changed support or claim |
| failed transformation | attempted operation does not satisfy its conditions | another operation may be proposed as a separate claim |
| non-capture | present STRATA route cannot adequately capture the object | rival representation or bounded partial result |

---

## 15. Anti-Immunization and Failure Preservation

### 15.1 Governing rule

```text
A change of frame, granularity, level, composition, or target function
constitutes a new testable reconstruction.
It does not erase the failure of the claim from which it began.
```

### 15.2 Operation-specific escape forms

#### COMPOSE escape

A failed local claim is not answered merely by placing it inside a larger composite.

#### DECOMPOSE escape

A counterexample is not answered merely by introducing ever-finer detail.

#### PROJECT_AS rescue

A failed source typing is not rescued merely because the source object may perform a different function elsewhere.

### 15.3 Required preservation record

Maintain:

- original claim;
- original operation occurrence;
- original objection or failure;
- new operation occurrence;
- new claim;
- independent result;
- relation between the two claims.

### 15.4 Translation success

```text
successful translation into STRATA terms
≠
proof of PMS completeness or superiority
```

Operation success shows bounded analytical legibility, not universal capture.

---

## 16. Authority and Formalization Boundary

### 16.1 Prohibited authority inheritance

```yaml
governance:
  authority_inheritance: prohibited
```

No operation licenses:

- person-level essence claims;
- diagnosis or clinical inference;
- personality typing;
- moral ranking;
- legal or political legitimacy decisions;
- sanctions or irreversible labels;
- automatic causal attribution;
- automatic intervention;
- policy enforcement;
- transfer of formal validity into application authority.

### 16.2 Formal-model boundary

The formal model may check:

- operation identity;
- required declaration presence;
- allowed source and target classes;
- Type Integrity declarations;
- continuity and loss fields;
- admissibility-gate completeness;
- canonical output values;
- explicit Stop and Non-Capture status.

It may not decide automatically:

- empirical truth;
- actual causality;
- semantic adequacy;
- normative validity;
- superiority over rivals;
- warranted person judgment;
- application authority.

```text
valid machine-readable record
≠
valid world claim
```

### 16.3 Schema handoff

Final field names and validation constraints belong to:

- `07_model/Operation_Registry.yaml`;
- `07_model/Transformation_Record.schema.json`;
- `07_model/Admissibility_Rules.yaml`;
- `07_model/Boundary_Decision_Tree.yaml`;
- `07_model/Output_Classes.yaml`.

This Reference Index identifies required semantic families but does not pre-empt Formal Model v0.

---

## 17. Historical Pre-Block Transformation Operation Gate

Before Foundations production, verify:

```text
[ ] Exactly three operation types are registered.
[ ] LIMITS is not treated as an operation.
[ ] Operation type, occurrence, output, and chain are distinct.
[ ] COMPOSE creates a composite object rather than a target function.
[ ] COMPOSE selection, ordering, and formation are separately visible.
[ ] Chronology and aggregation are not accepted as COMPOSE by default.
[ ] DECOMPOSE operates only on occurrences and composites, never operator types.
[ ] DECOMPOSE reconstructs components and relations together.
[ ] DECOMPOSE preserves the same reference object as the reconstruction target.
[ ] Finer granularity carries no truth or authority privilege.
[ ] PROJECT_AS preserves source reference and origin type.
[ ] PROJECT_AS declares a target context and bounded target function.
[ ] Recontextualization, analogy, and label substitution remain distinct from PROJECT_AS.
[ ] No target function becomes a new PMS primitive.
[ ] Each operation declares preservation, continuity, and loss.
[ ] Each operation occurrence is independently tested against the Relevance Floor and Traceability Ceiling, and its result is recorded.
[ ] Counterfactual Sensitivity remains a load test rather than a causal proof.
[ ] Source and calibration limits remain visible.
[ ] Local results map to one of the ten canonical output classes.
[ ] Operations in a chain retain separate records and results.
[ ] Later operations do not validate earlier failed operations retroactively.
[ ] Non-invertibility is explicit.
[ ] Mandatory Stop, failure, claim reduction, and Non-Capture remain distinct.
[ ] No operation creates additional analytical or application authority.
[ ] No person typing, diagnosis, or irreversible labeling is licensed.
```

Gate result:

```text
pass
→ operation vocabulary ready for Foundations and Formal Model v0

fail
→ revise Reference Kernel or Minified control before Block drafting
```

---

## 18. Definition-Site and Reference Handoffs

| Topic | Primary definition site | Operational or limit elaboration | Reference handoff |
|---|---|---|---|
| three-operation inventory | Chapter 4 | Chapters 15, 20, 30 | this index |
| operation occurrence and chain | Chapter 4 | Chapter 7 and Chapter 53 | Glossary; this index |
| COMPOSE | Chapter 4 | Chapter 15; Chapter 16 local limits | this index; later Formal Model |
| DECOMPOSE | Chapter 4 | Chapter 20; Chapters 25–27 local limits | this index; later Formal Model |
| PROJECT_AS | Chapter 4 | Chapter 30; Chapters 37–39 local limits | this index; later Formal Model |
| shared record | Chapter 7 | operation chapters and Chapter 53 | later schemas and appendices |
| origin type and target function | Chapter 5 | Chapters 29–30 and 47 | Glossary; Non-Equivalence Index |
| Relevance Floor | Chapter 6 | Chapter 44 | Admissibility Band Reference |
| Traceability Ceiling | Chapter 6 | Chapter 45 | Admissibility Band Reference |
| Counterfactual Sensitivity | Chapter 6 | Chapter 46 | Admissibility Band Reference |
| continuity | Chapter 5 | Chapter 47 | Glossary; Admissibility Band Reference |
| loss | Chapter 7 | Chapter 48 | this index; later record schema |
| source and calibration limits | Chapter 49 | Chapter 6 common entry conditions | `04_reference/Claim_Type_Table.md`; `04_reference/Evidence_Map.md` |
| anti-immunization | Chapter 50 | Chapter 6 common rule and Chapter 53 integrated audit | Non-Equivalence Index |
| Stop method | Chapter 51 | Chapter 6 output-class architecture; Chapter 53 integrated application | Admissibility Band Reference; Output Class Index; `04_reference/Audit_Checklist.md` |
| Non-Capture method | Chapter 52 | Chapter 6 output-class architecture; Chapter 53 integrated application | Admissibility Band Reference; Output Class Index; `04_reference/Audit_Checklist.md`; later case records |
| integrated audit | Chapter 53 | local audits in Chapters 17, 28, 40 | `04_reference/Audit_Checklist.md` |
| canonical output classes | Chapter 6 | Chapter 53 | Output Class Index |

### 18.1 Current Reference Kernel relations

```text
Glossary.md
→ canonical short definitions and spellings

Operator_Index.md
→ PMS Base operator identity and STRATA relation

Transformation_Operation_Index.md
→ STRATA operation identity, comparison, boundaries, chains, and mapping

Non_Equivalence_Index.md
→ consolidated prohibition and confusion relations

Output_Class_Index.md
→ full canonical result semantics and routing

Claim_Type_Table.md
→ claim families and ceilings

Admissibility_Band_Reference.md
→ complete gate and limit reference
```

### 18.2 Revision policy

This file is **provisionally controlled**, not finally frozen.

During Block production it may grow through:

- clarified operation boundaries;
- validated local result mappings;
- confirmed model fields;
- tested chain rules;
- case-derived confusion patterns;
- corrected cross-references.

It must not grow through:

- a fourth operation;
- redefinition of Δ–Ψ;
- new canonical output classes;
- theory claims originating only in this reference layer;
- silent machine-field invention;
- authority expansion.

Final freeze occurs only after Cases, Conclusion, Front Matter, Appendices, and corpus-wide audit.

---

## Chapter 2 Coordinate Handoff to the Three Operations

[`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) now supplies canonical definitions of frame, granularity, relative level, and restricted micro–meso–macro shorthand. Coordinate difference alone does not determine operation identity; WP1–WP3 now supply the complete Chapter 2 coordinate, scope, and comparison architecture pending integrated WP4 review.

| Coordinate pattern | What Chapter 2 may establish | What remains operation-owned |
| --- | --- | --- |
| stable frame, changed granularity | a controlled resolution difference | whether the occurrence is `DECOMPOSE` under Chapter 20 conditions |
| changed frame, stable granularity | contextual re-bounding | whether any operation occurs; changed frame alone is not `PROJECT_AS` |
| changed relative level | a declared positional relation | whether `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` supplies the relation |
| changed target function | not a Chapter 2 coordinate result by itself | `PROJECT_AS` and Chapter 5 continuity/validity burdens |

Every later operation occurrence must declare source and target coordinates through the existing record paths. A coordinate-complete record can still fail operation identity, traceability, admissibility, Stop, or Non-Capture checks.

## Chapter 2 WP2 Scope Handoff to Operation Records

Every later operation occurrence must consume the Chapter 2 scope declarations without redefining them:

```text
temporal scope
→ bounds the included time and open edges

source scope
→ bounds accessible support, inference, gaps, and uncertainty

claim scope
→ bounds what the operation occurrence may assert
```

These declarations do not identify `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`; do not establish source truth or best periodization; and do not replace operation-specific validity, preservation, loss, or Stop requirements. Existing nested Shared Transformation Record paths remain authoritative.

## Chapter 2 WP3 Coordinate-Change Handoff to Operation Classification

The following Chapter 2 patterns are necessary declarations but not operation proofs:

| Coordinate pattern | Chapter 2 result | Operation-specific question retained |
| --- | --- | --- |
| stable frame, finer granularity | declared resolution change | does Chapter 20 establish `DECOMPOSE` of a compressed occurrence or composite? |
| changed frame, stable granularity | declared relevance-boundary change | is there merely re-bounding, PMS `Φ`, or a Chapter 30 contextual target function? |
| changed relative level | declared positional change under a named relation | was a composite formed, an occurrence opened, or a function projected? |
| multiple valid granularities | plurality without ranking | does a later resolution test change the warranted reconstruction? |
| granularity conflict | comparability and contradiction pressure | which operation, if any, produced the competing source–target claims? |

The Minimal Level Declaration maps to existing source, target, claim, relation, loss, and shared-occurrence paths. It does not add schema fields or waive operation signatures. Every material coordinate change creates a new claim and record burden; it does not inherit an earlier operation result or erase prior failure.

---

## Chapter 2 Provisional-Lock Operation Handoff

Chapter 2 now supplies the locked pre-operation coordinate and scope declaration burden for all three operation families:

```text
source coordinates and scopes
+
target coordinates and scopes
+
coordinate relation and declared change
+
claim scope
+
loss and uncertainty
→ necessary pre-operation declaration
```

This burden is not sufficient to establish operation identity.

| Declared difference | Operation classification still required |
| --- | --- |
| many sources and a new composite target | test `COMPOSE` formation, selection, constitutive relations, and loss |
| compressed occurrence/composite and finer target | test `DECOMPOSE` reference continuity, component reconstruction, and resolution effect |
| origin-typed source and contextual target function | test `PROJECT_AS` origin-type preservation, target function, context, validity, and transfer limits |

The Operation Registry now mirrors Chapter 2 through an open coordinate handoff. The Shared Transformation Record Schema remains unchanged. Formal validation may detect missing declarations; it may not infer the operation, best granularity, substantive contradiction, or admissibility result.

---

## Chapter 3 WP1 — Temporal Objects Before Operation Identity

Canonical source: [`Chapter 3 Sections 3.1–3.5`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

Canonical Chapter 3 temporal categories through trajectory may become source or target objects of later operations, but their category labels do not establish an operation occurrence. Path dependence and the remaining historical-property burdens remain pending WP3.

```text
sequence / path / trajectory claim
≠ COMPOSE occurrence automatically

finer temporal reconstruction
≠ DECOMPOSE occurrence automatically

trajectory used as later frame-function
≠ PROJECT_AS occurrence automatically
```

The correct handoff is:

```text
Chapter 3 temporal object burden
→ Chapter 4 operation classification
→ Chapter 6 admissibility
→ Chapter 7 Shared Transformation Record
→ PATH / SUB / RETYPE procedure
```

A path may later be produced through `COMPOSE`, decomposed through a separate `DECOMPOSE`, or projected as a bounded function through `PROJECT_AS`. Each occurrence requires its own source/target declaration, loss account, test, and output mapping.

## Chapter 3 WP2 — Ordered Historical Objects Before Operation Identity

Canonical source: [`Chapter 3 Sections 3.6–3.8`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Temporal object or claim | What WP2 establishes | What remains separately required |
| --- | --- | --- |
| sequence | selected units and supported declared order | no automatic path, cause, or operation |
| path | actual traversed selective chain with connectedness, trace, and loss | no automatic `COMPOSE`, trajectory, or target function |
| trajectory | path with source-supported retained historical load affecting later praxis | no automatic path dependence, teleology, or PROJECT_AS function |

```text
sequence label
≠ COMPOSE occurrence

path object
≠ completed COMPOSE procedure

trajectory object
≠ PROJECT_AS target function
```

Any later operation must be declared and tested on its own source objects, formation or projection relation, continuity, loss, and admissibility burdens.

## Chapter 3 WP3 — Historical Properties Before Operation Identity

Canonical source: [`Chapter 3 Sections 3.9–3.13`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Historical property or chain | What Chapter 3 establishes | What remains separately required |
| --- | --- | --- |
| path dependence | bounded property burden including current-conditions insufficiency, prior-order/branch relevance, supported counterfactual sensitivity, and traceable carry-over | no automatic `COMPOSE`, causal proof, determinism, or operation identity |
| sedimentation | source-supported accumulated/persistent carrier with declared later praxis effect | no automatic trajectory formation or operator formula |
| bounded irreversibility | declared frame, claim, object relation, restoration criterion, and residual difference/cost | no metaphysical permanence, total loss, or automatic Stop |
| unrealized alternative | source-supported historically available non-traversed continuation | no proof of counterfactual outcome or branch taxonomy completion |
| Minimal Temporal Object Chain | burden progression and downgrade route from configuration through trajectory | no automatic derivation, Shared Transformation Record, or completed `COMPOSE` procedure |

```text
temporal object or historical-property label
≠ COMPOSE occurrence
≠ DECOMPOSE occurrence
≠ PROJECT_AS occurrence
```

A later operation may use these objects or properties only through a separately declared source, target, transformation context, loss account, alternatives test, and output mapping.

---

## Chapter 3 Temporal-Object Handoff

The objects and properties defined in [`Chapter 3`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) may become source or target structures in later operation occurrences, but temporal-object classification does not decide operation identity. Sequence, path, trajectory, or path-dependence language must not silently convert chronology into `COMPOSE`, added detail into `DECOMPOSE`, or reframing into `PROJECT_AS`.

---

## Chapter 4 Preparation Handoff

The Preparation Gate fixed the drafting burden without replacing the now-canonical Chapter 4 Sections 4.1–4.7.

### Closed occurrence inventory

```text
COMPOSE
DECOMPOSE
PROJECT_AS
```

One operation occurrence has exactly one kind. A chain is an ordered sequence of separate occurrences and never a compound fourth operation.

### Signature comparison

| Operation | Source signature | Target relation | Core preservation duty | Core confusion |
| --- | --- | --- | --- | --- |
| `COMPOSE` | multiple or sequential source structures | new composite analytical object | source trace, constitutive relations, ordering and selection burden | chronology, aggregation, summary |
| `DECOMPOSE` | provisionally compressed occurrence or composite | finer reconstruction of same reference object | reference identity, component relations, coarser source-function status | description, added detail, operator-type decomposition, competing path |
| `PROJECT_AS` | origin-typed source object | bounded contextual target function | source reference, origin type, constitutive trace, contextual boundedness | recontextualization, analogy, renaming, type replacement |

### Preparation-origin chain rule, now canonical in Section 4.7

Each link must declare its own occurrence ID, kind, source/target relation, justification, selection, preservation, loss, alternatives, result, and continuation boundary. Earlier success does not validate a later link; later success does not repair a prior failed link.

### Non-invertibility route

```text
DECOMPOSE(COMPOSE(X)) ≠ X
COMPOSE(DECOMPOSE(X)) ≠ X
PROJECT_AS(X) ≠ X as a new origin type
```

Section 4.8 must explain these through selection, compression, reconstruction, context, and type preservation rather than generic undo failure.

### Record boundary

The Minimal Operation Declaration maps to existing `/source/*`, `/operation/*`, `/target/*`, and `/loss/*` paths. Chapter 4 does not create a second record vocabulary. Chapter 7 owns full recording; Chapters 15, 20, and 30 own detailed procedures.

Production-control source: `04_reference/Chapter_4_Preparation_Record.md`.

---

## Chapter 4 WP1 Canonical Signature Return

Canonical Sections 4.1–4.4 now own the core operation identities summarized by this index.

| Operation | Canonical WP1 target | Required preservation | Canonical negative pressure |
| --- | --- | --- | --- |
| `COMPOSE` | new composite analytical object | source trace, constitutive formation, relevant order and heterogeneity | chronology-only source fails composition |
| `DECOMPOSE` | finer reconstruction of same reference object | reference identity, component relations, coarser-claim status | competing path formation fails decomposition |
| `PROJECT_AS` | bounded contextual target function | source reference, origin type, source-dependent function | apt label remains analogy-only or fails |

Canonical return: [`Chapter 4 WP1`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

Direction tendencies, operation chains, non-invertibility, integrated confusion, and the Minimal Operation Declaration are now canonical in Sections 4.1–4.10. Integrated synchronization and provisional lock remain pending WP4.

---

## Chapter 4 WP2 Canonical Direction and Chain Return

### Direction tendencies

| Operation | Common tendency | Non-equivalence |
| --- | --- | --- |
| `COMPOSE` | often relatively wider | relative upwardness is not operation identity or authority |
| `DECOMPOSE` | often finer in granularity | relative downwardness is not sufficient and may leave level stable |
| `PROJECT_AS` | primarily changes contextual function | context or level change alone is not projection |

### Chain rule

```text
one link
= one occurrence
= exactly one operation kind
= one local result
```

Required canonical families:

```text
COMPOSE → PROJECT_AS
COMPOSE → DECOMPOSE
DECOMPOSE → COMPOSE
DECOMPOSE → PROJECT_AS
PROJECT_AS → DECOMPOSE
COMPOSE → PROJECT_AS → DECOMPOSE
```

Every arrow requires a declared source handoff, independent preservation and loss account, and a new admissibility test. Component results remain visible in any integrated chain summary.

---

## Chapter 4 WP3 Non-Invertibility and Declaration Return

### Non-invertibility rule

Every reverse-looking movement is a new occurrence. It must re-declare source, target, kind, preservation, loss, alternatives, uncertainty, and local result.

### Confusion separation

| Confusion | Required separation |
| --- | --- |
| chronology as composition | test formation relation and composite identity |
| detail as decomposition | test same-reference relational reconstruction |
| rival formation as decomposition | distinguish `DECOMPOSE` from new `COMPOSE` |
| label or recontextualization as projection | test target function, source carriage, and validity scope |
| multi-kind occurrence | split into a chain of exclusive occurrences |
| unresolved `COMPOSE` / `DECOMPOSE` identity | retain rival candidates and route to `non_capture` |

### Minimal declaration rule

The Minimal Operation Declaration is conceptual and maps to `/source/*`, `/operation/*`, `/target/*`, `/loss/*`, and the existing claim, alternatives, stop, governance, and result families. It creates no new operation kind or schema.

---

## Chapter 4 Provisional-Lock Operation Route

Canonical operation identity now returns to [`Chapter 4`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as). The index may route the three signatures, chain links, non-invertibility, confusion, Stop, Non-Capture, and declaration burdens, but it may not create a fourth operation, compound kind, inverse operation, or automatic classifier.

---

## Chapter 5 Preparation Handoff — Continuity Across Operations

Chapter 5 does not add an operation. It supplies integrity and continuity criteria consumed by all three existing operation types.

| Operation | Reference burden | Type burden | Functional burden | Temporal burden |
| --- | --- | --- | --- | --- |
| `COMPOSE` | new composite identified while source references remain traceable | source types preserved; new target object typed separately | no target function unless a later `PROJECT_AS` occurrence is declared | ordering and constitutive historical relations remain reconstructible |
| `DECOMPOSE` | same reference object remains the reconstruction target | source typing stays visible or is explicitly revised by a new claim | coarser source-function effect is confirmed, refined, reduced, rejected, or unresolved | internal order and duration are recovered without false completeness |
| `PROJECT_AS` | source reference remains identifiable | origin type is preserved | bounded source-carried target function is required | later function does not erase source path, duration, or historical load |

### Context separation

```text
source/target frame
≠ target context
≠ operation transformation context
```

The future Chapter 5 must define how the transformation context governs purpose, source relevance, target relation, temporal reach, validity scope, and Claim Ceiling. Chapter 4 operation identity remains unchanged.

### Continuity interaction

Each occurrence may carry separate findings for:

```text
reference continuity
type integrity
functional continuity
temporal continuity
contextual boundedness
```

One positive dimension cannot compensate for a failed load-bearing dimension. One failed dimension does not automatically dictate the same result for every claim.

### Record boundary

The Minimal Projection Form maps origin type to `/source/object_typing`, target function to `/target/contextual_function`, transformation context to `/operation/transformation_context`, and continuity findings to existing rule-assessment families. No second schema or new top-level continuity result is created.

Production-control source: `04_reference/Chapter_5_Preparation_Record.md`.

---

## Chapter 5 WP1 Continuity Handoff

Chapter 5 WP1 now supplies the canonical source-side and context-side declarations consumed by transformation analysis:

| Control | Canonical burden |
| --- | --- |
| origin type | source-side analytical typing remains explicit |
| target function | bounded role is declared separately from source and target object typing |
| source-change sensitivity | material changes to load-bearing source features alter, weaken, or defeat the function |
| target context | target-side scene or relation is named |
| transformation context | full source–operation–target validity envelope is declared |

For `PROJECT_AS`:

```text
origin type preserved
+ target function separately bounded
+ transformation context declared
```

Canonical return: [`Chapter 5 WP1`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP2 Continuity Handoff

| Operation | Reference-continuity burden | Type-integrity burden | Functional-continuity burden |
| --- | --- | --- | --- |
| `COMPOSE` | new composite remains traceable to selected source references and formation relation | source types remain visible; target-composite type declared separately | only required where a later function is also claimed |
| `DECOMPOSE` | same reference object remains the reconstruction target | finer typing may confirm or explicitly revise the coarser claim | added detail alone does not establish a target function |
| `PROJECT_AS` | source referent remains visible | origin type preserved; function separate | precise source-carried function must change under material source change |

Continuity findings remain local to each operation occurrence and each function claim. Canonical return: [`Chapter 5 §§5.4–5.6`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP3 Temporal and Contextual Continuity Handoff

| Operation | Temporal-continuity burden | Contextual-boundedness burden |
| --- | --- | --- |
| `COMPOSE` | claim-bearing source order and historical heterogeneity remain traceable in the composite | any later target function requires a separate `PROJECT_AS` occurrence and context |
| `DECOMPOSE` | finer reconstruction preserves the relevant temporal object and discloses uncertain edges | changed context or function is not hidden inside added detail |
| `PROJECT_AS` | later function preserves relevant source order and does not erase earlier failure history | target context, purpose, scope, expiry, and no-authority-transfer rule are explicit |

The Minimal Projection Form maps to existing `/source/*`, `/operation/*`, `/target/*`, `/admissibility/*`, `/loss/*`, alternatives, governance, stop, and result families. Canonical return: [`Chapter 5 §§5.7–5.9`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

---

## Chapter 5 Integrated Continuity Handoff

| Operation | Chapter 5 continuity duty |
| --- | --- |
| `COMPOSE` | new target object remains traceable to selected sources and formation relation; source types remain visible |
| `DECOMPOSE` | same reference object remains visible; finer typing revision is explicit and temporally honest |
| `PROJECT_AS` | origin type remains visible; target function is source-carried, source-sensitive, temporally continuous, and context-bounded |

No operation success inherits continuity across a later link or target context. The Minimal Projection Form is a prose-bound declaration mapped to existing record families, not a fourth operation or second schema.

Canonical return: [`Chapter 5`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

---

## Chapter 6 Provisional-Lock Operation-Admissibility Handoff

The three operation identities remain owned by Chapter 4. Chapter 6 tests delimited occurrences and claims under common and operation-specific burdens without redefining `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

```text
operation identity
≠ admissibility result

operation occurrence available
≠ operation occurrence admissible
```

`COMPOSE` must carry selection, formation, and loss; `DECOMPOSE` must retain the same reference object and relational burden; `PROJECT_AS` must preserve origin type and source-sensitive contextual function. These overlays do not create a fourth operation or an operation ranking.

Canonical return: [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 7 WP1 Operation-Record Synchronization

Every operation occurrence is recorded through the same common envelope but retains its Chapter-4 signature.

| Operation | Source duty | Target duty | Record-specific protection |
| --- | --- | --- | --- |
| `COMPOSE` | many or sequential typed source structures plus selection and formation basis | new composite analytical object | chronology or source set alone is insufficient |
| `DECOMPOSE` | compressed occurrence or composite with retained reference | finer reconstruction of the same reference object | detail may not silently create a competitor object |
| `PROJECT_AS` | origin-typed source object and constitutive features | same reference and typing plus bounded contextual function | function may not replace origin type |

Exactly one operation kind is permitted per occurrence. A chain requires separate linked occurrences. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 7 WP2 Operation-Record Duties

Every operation occurrence now carries the same additional common duties:

| Duty | `COMPOSE` pressure | `DECOMPOSE` pressure | `PROJECT_AS` pressure |
| --- | --- | --- | --- |
| Admissibility | selection and formation must pass the Band | same-reference finer reconstruction must pass the Band | source-carried bounded function must pass the Band |
| Loss | component heterogeneity, order, and alternatives | coarser function and reference visibility | origin type, source features, and contextual limits |
| Alternatives | rival compositions and no composition | rival decompositions or competing object formation | rival projections, analogy, or non-translation |
| Governance | no composite authority inheritance | no detail-to-truth authority | no function-to-type or function-to-authority transfer |

One occurrence still has exactly one operation kind. The common record duties do not flatten the three signatures. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 7 WP3 Chain and Extension Duties

| Record use | Common rule | Operation boundary |
| --- | --- | --- |
| single occurrence | one record occurrence, exactly one kind | no compound operation identity |
| chain | linked occurrence records plus separate chain declaration | chain is not a fourth operation |
| chain handoff | predecessor target becomes declared successor source only after explicit continuity handoff | no inherited admissibility |
| local extension | bounded namespaced detail with control source | no replacement of operation semantics or shared fields |
| integrated audit | preserve occurrence results, losses, Stop, and Non-Capture | no chain-level overwrite |

The three operation signatures remain unchanged. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 7 WP4 Provisional-Lock Synchronization

Chapter 7 is provisionally locked after integrated ownership, redundancy, status, case-duty, prose-to-schema, link, schema, fingerprint, package, and roundtrip audit. The Shared Transformation Record records transformation claims without becoming the transformation, a truth proof, or an authority source. The existing record schema supplies lower-authority structural carriers; its Chapter-7 handoff annotation does not redefine canonical prose. The sixteen Chapter-7 case identifiers remain later production duties rather than completed evidence. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 8 Preparation Operation-Confusion Handoff

The Chapter 8 minimum catalogue audits, but does not redefine, these operation boundaries:

| Non-equivalence | Operation protection |
| --- | --- |
| composition ≠ lossless addition | `COMPOSE` retains selection, formation, compression, exclusion, and loss |
| decomposition ≠ discovery of final constituents | `DECOMPOSE` remains frame-, source-, and reference-bound |
| structural analogy ≠ valid projection | `PROJECT_AS` still requires origin type, target context, function, continuity, and source load |
| projection ≠ operator identity | target function cannot create a PMS primitive |
| recursion ≠ completeness | availability of another operation does not require continuation or total capture |

```text
non-equivalence breach
≠ fourth operation
≠ automatic operation failure class
```

Production control: [`Chapter 8 Preparation Record`](Chapter_8_Preparation_Record.md).

---

## Chapter 8 WP1 Canonical Operation-Confusion Returns

| Audit pair | Canonical return | Operation consequence |
| --- | --- | --- |
| composition ≠ lossless addition | [Section 8.3](../01_blocks/01_foundations.md#83-composition-is-not-lossless-addition) | disclose selection, ordering, formation, preservation, compression, exclusion, uncertainty, and irrecoverable loss |
| decomposition ≠ discovery of final constituents | [Section 8.4](../01_blocks/01_foundations.md#84-decomposition-is-not-discovery-of-final-constituents) | preserve reference, declare resolution and sources, retain revisability, and stop before ontological atomization |

A breach remains a local category-error finding. It does not add an operation or mechanically select an Output Class.

---

## Chapter 8 WP2 Canonical Operation and Chain Returns

| Audit pair | Canonical return | Operation or test consequence |
| --- | --- | --- |
| path ≠ sequence | [Section 8.5](../01_blocks/01_foundations.md#85-path-is-not-sequence) | `COMPOSE` path formation requires traversal, selection, constitutive relation, branch treatment, and loss beyond temporal order |
| path ≠ trajectory | [Section 8.6](../01_blocks/01_foundations.md#86-path-is-not-trajectory) | trajectory formation requires sedimentation and changed continuation possibilities beyond path existence |
| trajectory ≠ path dependence | [Section 8.7](../01_blocks/01_foundations.md#87-trajectory-is-not-path-dependence) | path dependence remains a separately tested property and not an operation identity |
| origin type ≠ target function | [Section 8.8](../01_blocks/01_foundations.md#88-origin-type-is-not-target-function) | `PROJECT_AS` preserves origin type and declares target function separately |
| projection ≠ operator identity | [Section 8.9](../01_blocks/01_foundations.md#89-projection-is-not-operator-identity) | derived contextual function creates no PMS primitive or fourth STRATA operation |
| operator weighting ≠ operator replacement | [Section 8.10](../01_blocks/01_foundations.md#810-operator-weighting-is-not-operator-replacement) | weighting leaves operator names, order, dependencies, and type identity unchanged |

Each stronger temporal or functional move is a new testable claim. Chain summaries may not erase local operation and property-test results.

---

## Chapter 8 WP3 Analogy, Recursion, and Authority Returns

| Audit pair | Canonical return | Operation or audit consequence |
| --- | --- | --- |
| structural analogy ≠ valid projection | [Section 8.11](../01_blocks/01_foundations.md#811-structural-analogy-is-not-valid-projection) | analogy may remain `analogy_only`; `PROJECT_AS` requires a separate origin-typed, context-bound, continuity-tested claim |
| recursion ≠ completeness | [Section 8.12](../01_blocks/01_foundations.md#812-recursion-is-not-completeness) | every recursive occurrence retains one operation kind, one local result, its own loss, and a declared handoff; Stop and Non-Capture remain constitutive |
| legibility ≠ authority | [Section 8.13](../01_blocks/01_foundations.md#813-legibility-is-not-authority) | schema, record, and package validity improve inspection but cannot authorize transformation passage, PMS revision, person typing, or application |
| integrated catalogue use | [Section 8.13](../01_blocks/01_foundations.md#integrated-catalogue-use) | pair checking is an audit sequence, not a fourth operation or automatic routing mechanism |

A new recursive transformation, target function, frame, level, or composite remains a new testable claim and cannot erase an earlier failed, stopped, or non-captured claim.

---

## Chapter 8 WP4 Operation Lock and PATH Entry

Chapter 8 is provisionally locked after confirming that its audit catalogue adds no operation and performs no operation selection.

```text
non-equivalence audit sequence
≠ COMPOSE
≠ DECOMPOSE
≠ PROJECT_AS
≠ fourth operation
```

The bounded Decision-Tree handoff may require segmentation and preserve operation-local findings, but it may not invent an operation or treat a category-error flag as operation failure automatically. PATH enters with the exact three-operation inventory unchanged.

---

## Chapter 9 Preparation — Transition and Operation Boundary

```text
transition object or relation
≠ STRATA transformation operation
```

| Chapter 9 object or claim | Operation status | Later handoff |
| --- | --- | --- |
| temporal-position declaration | no operation identified | may constrain a later operation record |
| order-dependence finding | no operation identified | may support transition and later path formation |
| transition candidate | no operation identified automatically | may become source or target of a later operation |
| warranted transition | still not `COMPOSE` by itself | Chapter 10 may form path objects; Chapter 15 owns the full `COMPOSE` procedure |
| temporal recontextualization | not `PROJECT_AS` automatically | separate `Φ` occurrence or bounded `PROJECT_AS` claim if declared |
| failed transition | valid local result | may trigger reduction, failure, Stop, diagnostic, or non-capture without path formation |

Chapter 9 may use the Shared Transformation Record as a carrier but may not infer an operation from record completeness. It introduces no fourth operation and does not alter the exact signatures of `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

Production control: [`Chapter 9 Preparation Record`](Chapter_9_Preparation_Record.md).

---

## Chapter 9 WP1 — PATH and Operation Separation

| WP1 item | Operation identity | Controlled consequence |
| --- | --- | --- |
| PATH Part | none | contains later procedures but is not an operation |
| `Θ` temporal declaration | none | supports temporal claim fields without selecting an operation |
| temporal-position declaration | none | constrains source/target temporal scope |
| order-dependence finding | none | may support a transition candidate but does not form one automatically |
| temporal object later used in `PROJECT_AS` | separate future occurrence | requires RETYPE target context and origin-type preservation |
| temporal sources later composed | separate future `COMPOSE` occurrence | Chapter 15 owns the procedure |

```text
PATH
≠ COMPOSE

temporal reconstruction
≠ operation occurrence automatically
```

Canonical route: [`Chapter 9 §§9.1–9.4`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

---

## Chapter 9 WP2 — Temporal Relations and Operation Separation

| WP2 item | Operation identity | Controlled consequence |
| --- | --- | --- |
| duration | none | may constrain source/target temporal scope |
| delay structure | none | may support a transition candidate without `Λ` or operation selection |
| framed delayed non-event | none | preserves `Λ` occurrence/object boundary |
| persistence | none | continuity finding, not `COMPOSE` automatically |
| bounded irreversibility | none | criterion-specific historical property claim |
| temporal recontextualization | none | historical relation, not `Φ` or `PROJECT_AS` automatically |

A later composition or projection requires a separate occurrence record. Canonical route: [`Chapter 9 §§9.5–9.9`](../01_blocks/02_part_i_path.md#9-5-duration).

---

## Chapter 9 WP3 — Transition and Operation Separation

| WP3 item | Operation identity | Controlled consequence |
| --- | --- | --- |
| transition candidate | none | delimited temporal relation awaiting local tests |
| warranted transition | none | may become source material for Chapter 10 path claim |
| frame handoff | none | continuity/comparability declaration, not `PROJECT_AS` automatically |
| failed transition | none | preserves endpoints and weaker temporal findings |
| warranted transition set | none | not a path and not a `COMPOSE` occurrence |
| later path composition | separate future `COMPOSE` occurrence | Chapter 10 tests path; Chapter 15 owns full procedure |

```text
transition object or relation
≠ STRATA transformation operation
```

Canonical route: [`Chapter 9 §§9.10–9.12`](../01_blocks/02_part_i_path.md#9-10-transition-preconditions).


## Chapter 9 WP4 — Transition Lock and Later Operation Handoff

| Chapter 9 result | Operation status | Later use |
| --- | --- | --- |
| temporal-position or order finding | no operation selected | may constrain later source/target declarations |
| transition candidate | no operation selected | remains under local transition testing |
| warranted transition | no operation selected | may be supplied to Chapter 10 |
| warranted transition set | not a path and not `COMPOSE` | Chapter 10 tests Path identity; Chapter 15 owns the full `COMPOSE` procedure |
| failed transition | valid local result | preserves endpoints and may trigger reduction, failure, Stop, or Non-Capture |

```text
transition relation
≠ STRATA operation occurrence

Chapter 9 lock
≠ COMPOSE authorization
```

Canonical return: [`Chapter 9`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

---

## Chapter 10 Preparation — Path Object and Operation Boundary

```text
path object
≠ STRATA transformation operation
```

| Chapter 10 object or claim | Operation status | Later handoff |
| --- | --- | --- |
| chronology or sequence | no operation selected | may supply temporal source material |
| path candidate | no operation selected automatically | awaits path threshold and admissibility tests |
| warranted path | still not a completed `COMPOSE` occurrence by itself | may be source/target of later operations; Chapter 15 owns full formation procedure |
| blocked/aborted/deferred status | local path or continuation finding | may affect alternatives, loss, and later operation claims |
| path comparison | no operation selected | may compare results without composing or projecting them |
| minimal path record | Shared Record carrier | record completion does not select or validate an operation |
| later trajectory claim | separate object/claim test | Chapter 11 owns trajectory criteria |
| later path formation through `COMPOSE` | separate operation occurrence | Chapter 15 owns selection, formation, loss, and routing mechanics |

```text
path object formation burden
≠ completed COMPOSE procedure
```

Chapter 10 introduces no fourth operation and does not alter the exact signatures of `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

Production control: [`Chapter 10 Preparation Record`](Chapter_10_Preparation_Record.md).

---

## Chapter 10 WP1 — Path Object and Operation Separation

| WP1 item | Operation identity | Controlled consequence |
| --- | --- | --- |
| chronology or sequence | none | may remain source material below path threshold |
| warranted transition set | none | requires separate chain-level path test |
| path candidate | none | delimited derived object claim before full passage |
| warranted path object | none automatically | may later enter a separately declared operation occurrence |
| path formation represented through `COMPOSE` | separate future occurrence | Chapter 15 owns selection, ordering, preservation, loss, and operation routing |
| path used as `PROJECT_AS` source | separate future occurrence | origin path type remains while target function is context-bound |

```text
path object formation burden
≠ completed COMPOSE procedure
```

Canonical route: [`Chapter 10 §§10.1–10.6`](../01_blocks/02_part_i_path.md#chapter-10-path).

---

## Chapter 10 WP2 — Path Status and Operation Separation

| WP2 status relation | Automatic operation? | Controlled consequence |
| --- | --- | --- |
| realized path | none | actual traversal does not become `COMPOSE` by status alone |
| blocked continuation | none | prevention relation does not create a new operation or realized path segment |
| aborted path | none | cessation and residue remain historical-object properties |
| deferred continuation | none | postponement and continued availability do not select `COMPOSE` or `PROJECT_AS` |
| status change through time | none | each later status is a new bounded claim with lineage |

```text
qualified path status
≠ STRATA operation identity
```

Canonical route: [`Chapter 10 §§10.7–10.10`](../01_blocks/02_part_i_path.md#10-7-realized-path).

