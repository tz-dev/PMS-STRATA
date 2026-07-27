# PMS-STRATA — Transformation Operation Index

**Status:** corpus-wide-lock-integration-synchronized; Reference Freeze not performed
**Historical local version marker:** Reference Kernel v0.1.38 — Chapter-20-WP3-synchronized operation and record navigation  
**Repository role:** `04_reference/*` — terminology and cross-reference layer; not an independent theory source  
**Canonical operation inventory:** `COMPOSE`, `DECOMPOSE`, `PROJECT_AS`  
**Primary control sources:** `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`, `05_minified/PMS_STRATA_Minified_Canonical.md`, `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`, and `05_minified/Chapter_Contracts.md`  
**PMS Base boundary:** `PMS.yaml`

---

**Current synchronization:** Foundations Chapters 0–8, PATH Chapters 9–17, and SUB Chapters 18–28 retain their existing bounded provisional locks; RETYPE Chapters 29–40, LIMITS Chapters 41–53, and Conclusion Chapters 54–57 hold final bounded artifact-complete locks under `admissible_with_bounded_claim`; the corpus-wide route, boundary, Loss, Stop/Failure/Non-Capture, and authority integration surface is complete under `admissible_with_bounded_claim`; 59 case operation Records instantiate all ten Output Classes and all six required minimum chain families; Front Matter is substantively complete at bounded provisional status; Appendices A and B are substantively complete; Appendix C is the next controlled step, followed by Appendices D–N, Reference Freeze, Corpus Audit including the rule-guided Block iteration, Model Finalization, derivatives, Reader with controlled graph/3D-path visualization, and release.  
**Historical-layering rule:** Later `pending`, `next controlled step`, availability, or WP-stage statements preserve the local production state at the time of entry unless explicitly marked as current. They do not override this header and remain non-normative provenance until Reference Freeze.  

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

Production-control source: `../_workfiles/chapter_preparation/Chapter_4_Preparation_Record.md`.

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

Production-control source: `../_workfiles/chapter_preparation/Chapter_5_Preparation_Record.md`.

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

Production control: [`Chapter 8 Preparation Record`](../_workfiles/chapter_preparation/Chapter_8_Preparation_Record.md).

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

Production control: [`Chapter 9 Preparation Record`](../_workfiles/chapter_preparation/Chapter_9_Preparation_Record.md).

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

Production control: [`Chapter 10 Preparation Record`](../_workfiles/chapter_preparation/Chapter_10_Preparation_Record.md).

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

---

## Chapter 10 WP3 — Comparison, Record, and Operation Separation

| WP3 relation | Automatic operation? | Controlled consequence |
| --- | --- | --- |
| path comparison | none | comparison does not compose, decompose, or project the paths by itself |
| same endpoint / different path | none | endpoint relation does not create path identity or target function |
| path without strong dependence | none | weak dependence does not invalidate the path or select an operation |
| Minimal Path Record | none | record view does not replace the Shared Record or complete `COMPOSE` |
| Stop / Non-Capture | none | routing preserves or blocks claims without creating a fourth operation |
| Chapter-11 handoff | none | warranted path is input to a new trajectory test, not a completed transformation chain |

```text
path object comparison
≠ STRATA operation occurrence
```

Canonical route: [`Chapter 10 §§10.11–10.14`](../01_blocks/02_part_i_path.md#10-11-path-comparison).


## Chapter 10 WP4 — Path Lock and Later Operation Handoff

| Chapter 10 result | Operation status | Later use |
| --- | --- | --- |
| chronology or sequence | no operation selected | may remain a weaker temporal result |
| path candidate | no operation selected | remains under the conjunctive Path gate |
| warranted path | no operation selected | may be supplied to Chapter 11 or become source material for a later operation |
| qualified Path status | not an operation or Output Class | remains segment-, continuation-, claim-, and cut-relative |
| Minimal Path Record | compact Shared-Record view | does not complete `COMPOSE` |
| failed Path | valid local result | preserves components and may trigger reduction, failure, Stop, or Non-Capture |

```text
warranted path object
≠ completed COMPOSE record

Chapter 10 lock
≠ COMPOSE authorization
```

Canonical return: [`Chapter 10`](../01_blocks/02_part_i_path.md#chapter-10-path).

---

## Chapter 11 Preparation — Trajectory Object and Operation Boundary

```text
trajectory object
≠ STRATA transformation operation
```

| Chapter 11 object or claim | Operation status | Later handoff |
| --- | --- | --- |
| warranted Path substrate | no new operation selected | may support a Trajectory claim |
| Trajectory candidate | no operation selected automatically | awaits sedimentation, continuity, admissibility, loss, and routing tests |
| warranted Trajectory | still not a completed `COMPOSE` occurrence by itself | may be source/target of later operations |
| operator-profile accumulation | local historical finding | does not fuse operators or select `COMPOSE` |
| competing Trajectory constructions | no operation selected | may remain bounded, incomparable, failed, or non-captured |
| Minimal Trajectory Record | Shared Record carrier | record completion does not validate an operation |
| later Path-Dependence claim | separate property test | Chapter 12 owns graded dependence |
| later Trajectory formation through `COMPOSE` | separate operation occurrence | Chapter 15 owns complete selection, formation, compression, loss, and routing mechanics |
| later frame-/event-/attractor-function | separate `PROJECT_AS` occurrence | RETYPE owns target-function validity |

```text
trajectory object formation burden
≠ completed COMPOSE procedure
```

Chapter 11 introduces no fourth operation and does not alter the exact signatures of `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

Production control: [`Chapter 11 Preparation Record`](../_workfiles/chapter_preparation/Chapter_11_Preparation_Record.md).

## Chapter 11 WP1 — Trajectory Object versus Operation Occurrence

Chapter 11 WP1 tests whether a warranted Path qualifies as a Trajectory object. It does not select or complete a STRATA operation automatically.

| Chapter-11 WP1 result | Operation status | Later route |
| --- | --- | --- |
| warranted Path substrate | no new operation selected | may enter the Trajectory threshold test |
| Trajectory candidate | object/claim status only | remains subject to later Chapter-11 duties |
| warranted Trajectory | derived temporal object, not an operation occurrence by itself | may later become source or target of a separately declared operation |
| failed Trajectory | stronger object claim fails; weaker Path/local findings may remain | no stronger chain may inherit validity |
| non-teleological directionality | property of the bounded historical object | not `PROJECT_AS`, prediction, or causal mechanism |

```text
Trajectory classification
≠ COMPOSE occurrence automatically
≠ PROJECT_AS function
≠ fourth operation
```

Chapter 15 retains complete `COMPOSE` mechanics. RETYPE retains contextual target functions. Canonical route: [`Chapter 11 §§11.1–11.4`](../01_blocks/02_part_i_path.md#11-trajectory).

## Chapter 11 WP2 — Profile Accumulation and Operation Boundary

WP2 profile declarations and Changed Action Corridors classify historical load within a candidate Trajectory. They do not select or complete a STRATA operation.

| WP2 result | Operation status | Protected later route |
| --- | --- | --- |
| Attractor / Asymmetry / Binding / Residual profile | occurrence-level historical-load claim | Chapter 12 may test dependence; Chapter 15 retains `COMPOSE` mechanics |
| Changed Action Corridor | integrative present-effect declaration | not `PROJECT_AS`, prediction, or recommendation |
| multi-profile Trajectory description | several separately traced burdens | no fourth operation and no synthetic score |
| failed profile claim | local recurrence, inequality, commitment, absence, or present constraint may remain where warranted | stronger chain cannot inherit the failed profile |

```text
profile accumulation
≠ COMPOSE occurrence automatically

Changed Action Corridor
≠ PROJECT_AS target function
≠ operation
```

Canonical route: [`Chapter 11 §§11.5–11.9`](../01_blocks/02_part_i_path.md#11-5-attractor-sedimentation).

## Chapter 11 WP3 — Boundary, Compression, and Operation Boundary

WP3 completes the object-level Trajectory specification without completing a STRATA operation.

| WP3 result | Operation status | Protected later route |
| --- | --- | --- |
| Trajectory Boundary | scope and lineage declaration for a derived temporal object | not `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` |
| Trajectory Compression | preservation and Loss duty for representing the object | Chapter 15 retains full `COMPOSE` selection and formation mechanics |
| competing constructions | comparison of rival object constructions | synthesis would require a new separately tested claim and, where applicable, operation record |
| False Trajectory | failed or reduced object claim | stronger operation chain cannot inherit the failed object |
| Minimal Trajectory Record | compact view inside Shared Transformation Record | no second schema and no operation completion |

```text
Trajectory Compression
≠ completed COMPOSE occurrence

Trajectory object
≠ PROJECT_AS target function
```

Canonical route: [`Chapter 11 §§11.10–11.14`](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary).

## Chapter 11 WP4 — Trajectory Lock and Later Operation Handoff

| Chapter 11 result | Operation status | Later use |
| --- | --- | --- |
| Trajectory candidate | no operation selected automatically | remains under the conjunctive Trajectory burden |
| warranted Trajectory | derived temporal object, not a completed operation occurrence by itself | may enter Chapter 12 property testing or later operation Records |
| profile accumulation | local historical-load claim | does not fuse operators or select `COMPOSE` |
| Changed Action Corridor | present-effect declaration | not `PROJECT_AS`, prediction, or recommendation |
| competing construction | no operation selected | may remain bounded, failed, incomparable, or non-captured |
| Minimal Trajectory Record | compact Shared-Record view | does not complete `COMPOSE` |
| failed Trajectory | valid local result with weaker findings preserved | stronger derivation may require Stop |

```text
Chapter 11 provisional lock
≠ completed COMPOSE occurrence
≠ PROJECT_AS authorization
≠ fourth operation
```

Chapter 15 retains selection, formation, compression, Loss, alternatives, and routing for `COMPOSE`. RETYPE retains target-function assignment. Canonical return: [`Chapter 11 completion boundary`](../01_blocks/02_part_i_path.md#chapter-11-completion-boundary).


---

## Chapter 12 Preparation — Property Test and Operation Boundary

```text
Path-Dependence test
≠ STRATA operation
```

| Chapter-12 item | Operation status | Controlled later use |
| --- | --- | --- |
| weak order dependence | property finding; no operation selected | may qualify a Path without creating a Trajectory or composite operation |
| strong Path Dependence | property finding; no operation selected | may become a bounded claim about a warranted Trajectory |
| historical-omission or alternative-history test | admissibility/counterpressure test | does not perform `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` |
| `Α/Ω/Ψ/Λ + Θ` carrier | occurrence-level historical support | does not fuse operators or select an operation |
| `Φ`, `Χ`, `Σ`, later `Ψ` modifier | separately warranted operator occurrence | does not erase the prior Path or automatically select `PROJECT_AS` |
| Minimal Path-Dependence Claim View | Shared Record carrier | field completion does not validate an operation or causal claim |
| later Chapter-15 formation | separate `COMPOSE` occurrence | retains selection, formation, compression, loss, and routing burden |
| later Chapter-24 carrier analysis | separate `DECOMPOSE` occurrence | opens occurrences/composites, not the operator type or property itself |
| later target function | separate `PROJECT_AS` occurrence | cannot inherit dependence warrant as function validity |

A successful property test does not complete an operation. A failed property test cannot be repaired by a later operation, frame, granularity, or function without a new claim and preserved lineage.

Production control: [`Chapter 12 Preparation Record`](../_workfiles/chapter_preparation/Chapter_12_Preparation_Record.md).

## Chapter 12 WP1 Property/Operation Boundary

```text
Path-Dependence property test
≠ COMPOSE
≠ DECOMPOSE
≠ PROJECT_AS
```

The test qualifies a warranted Path, Trajectory, or bounded segment at a declared present cut and dependence dimension. It does not itself form a new composite, open a source object, or assign a contextual target function. Later operation occurrences require separate Records and do not inherit the property result as authorization.

Primary route: [§12.1](../01_blocks/02_part_i_path.md#12-1-path-dependence-as-a-property).

## Chapter 12 WP2 Profile/Operation Boundary

Dependence-bearing `Α + Θ`, `Ω + Θ`, `Ψ + Θ`, and `Λ + Θ` profiles are property-support relations inside a Path/Trajectory reconstruction. They are not fourth operations and do not themselves complete `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

```text
profile support
≠ operation occurrence
≠ target-function assignment
```

A later operation must receive its own Record, source, target, loss, admissibility, Stop, and Non-Capture tests. No profile inherits operation or application authority.

## Chapter 12 WP3 Property-Test and Operation Boundary

The Chapter-12 Path-Dependence test evaluates a property of a warranted Path or Trajectory. It is not `COMPOSE`, `DECOMPOSE`, `PROJECT_AS`, or a fourth operation.

```text
Path-Dependence property test
≠ transformation operation
```

A later `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` occurrence requires its own source, target, loss, admissibility, Stop, Non-Capture, and lineage Record. No supported dependence claim inherits operation or target-function authority.

## Chapter 12 WP4 — Path-Dependence Lock and Operation Handoff

| Chapter-12 result | Operation status | Later use |
| --- | --- | --- |
| weak or strong dependence finding | property result; no operation selected | may qualify a warranted Path or Trajectory |
| Historical-Omission or Alternative-History test | admissibility counterpressure | not `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` |
| dependence-bearing profile | occurrence-level support relation | no fused operator or operation completion |
| modifier finding | separately typed occurrence relation | no reset or target-function assignment |
| Minimal Claim View | Shared Record view | no second schema or operation completion |
| failed dependence claim | local result with weaker findings preserved | stronger reuse may require Stop |

```text
Chapter 12 provisional lock
≠ completed COMPOSE occurrence
≠ DECOMPOSE result
≠ PROJECT_AS authorization
≠ fourth operation
```

Canonical return: [`Chapter 12 completion boundary`](../01_blocks/02_part_i_path.md#chapter-12-completion-boundary).

---

## Chapter 13 Preparation — Alternative Status and Operation Boundary

Branch identification and Alternative Status testing are property/object analyses inside PATH. They are not a fourth STRATA operation.

```text
alternative-space analysis
≠ COMPOSE occurrence
≠ DECOMPOSE occurrence
≠ PROJECT_AS occurrence
```

Chapter 13 supplies alternative structures to Chapter 15. Only Chapter 15 owns the full `COMPOSE` selection, formation, preservation, compression, and Loss procedure. A historical alternative is also not identical to the Shared Record's rival-transformation alternatives.

## Chapter 13 WP1 — Branch Analysis and Operation Boundary

Alternative-space, Branch-Point, Realized-Branch, and Rejected-Branch analysis remains inside PATH object/property reconstruction.

```text
branch analysis
≠ COMPOSE occurrence
≠ DECOMPOSE occurrence
≠ PROJECT_AS occurrence
```

Chapter 15 retains full `COMPOSE`; later operations require separate Records and cannot inherit branch warrant as authorization.

## Chapter 13 WP2 — Status Analysis and Operation Boundary

Blocked, Aborted, Deferred, and Lost analysis remains PATH object/property reconstruction. None is a fourth STRATA operation or a completed `COMPOSE` occurrence.

```text
branch-status reconstruction
≠ COMPOSE completion
≠ DECOMPOSE
≠ PROJECT_AS
```

WP2 supplies status-bearing source material to Chapter 15. Chapter 15 alone owns full `COMPOSE` selection, formation, compression, exclusion, and irrecoverable-loss procedure. A later same-labelled continuation also requires its own continuity or new-claim test; it is not inherited through status notation.

## Chapter 13 WP3 — Counterfactual, Record, and Operation Boundary

| WP3 result | Operation status | Protected later route |
| --- | --- | --- |
| source-bounded Counterfactual Path | historical analytical pressure, not an operation | Chapter 15 may use it in `COMPOSE`; Chapter 46 owns general sensitivity |
| Non-Selection finding | Path-forming relation, not operation completion | Chapter 14 tests `Λ`; Chapter 15 tests composition |
| Alternative-Space Compression declaration | representation and Loss control, not completed `COMPOSE` | Chapter 15 owns source selection, formation, target object, and result |
| Alternative Status Record extension | Shared-Record view, not a fourth operation or new schema | supports later audit only |
| blocked/lost/other branch status | source material, not target function | RETYPE requires a separate `PROJECT_AS` record |

The top-level Shared-Record `alternatives` field continues to represent rival transformations. Chapter-13 historical alternatives remain in the owner-bound extension payload. No operation or authority is inherited from branch analysis.

## Chapter 13 Provisional-Lock Operation Boundary

Chapter 13 reconstructs source-bounded historical alternatives and their statuses. This reconstruction is not itself a fourth operation and does not complete `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

Chapter 15 retains `COMPOSE` selection, ordering, formation rule, target object, preservation, compression, exclusion, irrecoverable loss, and operation result. A valid branch finding may become a source object or Loss declaration only through a separate operation record. RETYPE receives no target function from branch status.

```text
branch finding
≠ completed COMPOSE
≠ PROJECT_AS result
```

Canonical return: [`Chapter 13 completion boundary`](../01_blocks/02_part_i_path.md#chapter-13-completion-boundary).

## Chapter 14 Preparation — Non-Event and Operation Boundary

Non-Event identification is not a fourth operation.

| Chapter-14 finding | Operation relation | Prohibited inference |
| --- | --- | --- |
| local `Λ` occurrence | may become a source object for later `COMPOSE` | established `Λ` equals completed composition |
| sedimented Non-Event load | may support later Path/Trajectory composition under Chapter 15 | repetition automatically authorizes `COMPOSE` |
| positive sub-events plus governing non-realization | later `COMPOSE` must preserve both roles or disclose Loss | positive event language erases `Λ` |
| Minimal Non-Event Record | bounded Shared-Record view; carrier decision deferred to WP3 | record completeness proves the claim |
| internal positive events inside a Non-Event interval | Chapter 23 may later `DECOMPOSE` the occurrence/composite | decomposition removes the higher-level Non-Event without remainder |
| contextual use of `Λ` | requires a separate `PROJECT_AS` occurrence | local `Λ` assigns a target function automatically |

```text
Non-Event classification
≠ COMPOSE
≠ DECOMPOSE
≠ PROJECT_AS
```

## Chapter 14 WP1 — Non-Event Analysis and Operation Boundary

Expectation, window, source-supported non-realization, and Delay analysis reconstruct PATH objects and occurrences.

```text
identifying a Λ candidate
≠ COMPOSE occurrence
≠ DECOMPOSE occurrence
≠ PROJECT_AS occurrence
```

Chapter 15 owns complete `COMPOSE`; Chapter 23 owns internal Non-Event decomposition; RETYPE owns any later target-function assignment.

## Chapter 14 WP2 — Pattern Reconstruction and Operation Boundary

Reconstructing repeated Non-Decision, blocked responsibility, Missing Repair, Missing Exit, or Non-Event Sedimentation remains object- and occurrence-level PATH analysis.

```text
pattern reconstruction
≠ COMPOSE occurrence
≠ DECOMPOSE occurrence
≠ PROJECT_AS occurrence
```

Chapter 15 owns `COMPOSE`; Chapter 23 owns internal Non-Event decomposition; RETYPE owns contextual target functions.

## Chapter 14 WP3 — Preservation and Operation Handoff

Chapter 14 supplies preservable `Λ` source structure. It does not execute an operation.

```text
local Λ finding
≠ COMPOSE
≠ DECOMPOSE
≠ PROJECT_AS
```

Chapter 15 owns composite formation and Loss; Chapter 23 owns internal decomposition; RETYPE owns contextual target functions.

## Chapter 14 Provisional-Lock Operation Boundary

Chapter 14 reconstructs and preserves source-bounded Non-Event structures. This reconstruction is not itself a fourth operation and does not complete `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

Chapter 15 retains source selection, ordering, formation, target-object construction, preservation, compression, exclusion, irrecoverable loss, and operation result. Chapter 23 retains finer reconstruction of a compressed Non-Event occurrence. RETYPE receives no target function from `Λ` status.

```text
local Λ finding
≠ completed COMPOSE
≠ DECOMPOSE result
≠ PROJECT_AS result
```

Canonical return: [`Chapter 14 completion boundary`](../01_blocks/02_part_i_path.md#chapter-14-completion-boundary).

## Chapter 15 Preparation — Complete COMPOSE Procedure Boundary

Chapter 15 is the primary PATH procedure site for `COMPOSE`.

```text
identified sources
+ warranted relations
+ declared selection/order/frame
+ formation rule
+ constitutive trace
+ five-part Loss
+ bounded target claim
→ COMPOSE candidate
```

| Finding | Operation meaning | Prohibited shortcut |
| --- | --- | --- |
| chronology or collection | source field below formation threshold | label it Path or Trajectory |
| admissible Sequence/Path/Trajectory composite | result of a bounded COMPOSE occurrence | assign macro-event, frame, or attractor function |
| reduced composition claim | supported weaker target retained | treat reduction as no result |
| failed formation | operation candidate does not produce warranted composite | reuse target label as authority |
| competing compositions | multiple source-supported formations remain | force unique capture |

A later `DECOMPOSE` is a new operation with new Loss and cannot prove that prior `COMPOSE` was lossless. A later `PROJECT_AS` is required for target-function use.

## Chapter 15 WP1 — COMPOSE Entry Procedure

WP1 establishes the operation-entry sequence:

```text
purpose and praxis difference
→ conjunctive preconditions
→ typed source field
→ explicit selection
→ warranted order
→ declared composition frame
→ WP2 formation and Loss test
```

A connected graph, source list, chronology, coarser frame, target label, or complete entry record does not complete `COMPOSE`. No-composition and competing-composition routes remain positive analytical outcomes.

WP1 does not perform `DECOMPOSE` or assign a contextual function through `PROJECT_AS`.

## Chapter 15 WP2 — COMPOSE Formation and Loss Procedure

```text
typed selected ordered framed sources
→ Formation Rule and constitutive relations
→ declared target-object threshold
→ preserved source trace
→ compressed/excluded/uncertain/irrecoverable Loss
→ WP3 claim and sensitivity tests
```

WP2 separates a formation hypothesis from a formation finding and both from a completed `COMPOSE` occurrence. It requires exactly the canonical Loss structure and keeps Chapter 24 `DECOMPOSE`, Chapter 48 general Loss, and RETYPE `PROJECT_AS` ownership protected.

```text
formed composite
≠ target function

external recoverability
≠ lossless composition
```

## Chapter 15 WP3 — COMPOSE Claim, Sensitivity, Failure, and Record

```text
formed target
→ segmented composition claim
→ no-retyping check
→ counterfactual-sensitivity and overelasticity test
→ failure/reduction/Stop/Non-Capture routing
→ complete Shared Transformation Record
```

The existing `composeDetails` schema carrier remains sufficient. Schema validity supports auditability but cannot establish substantive formation, constitutive status, operation success, target function, Output Class, or authority.

## Chapter 15 Provisional-Lock COMPOSE Procedure

```text
typed selected sources
→ warranted order
→ declared Composition Frame
→ Formation Rule and constitutive relations
→ typed composite target
→ complete canonical Loss
→ segmented claim and sensitivity test
→ canonical result
```

Chapter 15 is the complete PATH-specific procedure site for `COMPOSE`. It does not perform Chapter-24 `DECOMPOSE`, assign RETYPE functions through `PROJECT_AS`, or confer authority. The existing Shared Transformation Record and `composeDetails` remain sufficient for audit declaration.

Canonical return: [`Chapter 15 completion boundary`](../01_blocks/02_part_i_path.md#chapter-15-completion-boundary).

## Chapter 16 Preparation — PATH Boundary and Operation Handoff

Chapter 16 applies the Admissibility Band to PATH reconstruction and `COMPOSE` results. It does not add an operation.

| Boundary finding | Operation consequence | Not implied |
| --- | --- | --- |
| below Relevance Floor | added temporal differentiation lacks purchase; reduce or stop the tested claim | source falsehood |
| within Band | bounded PATH result remains eligible for full audit | empirical truth or authority |
| above Traceability Ceiling | target loses reconstructible source load; reduce, fail, stop, or retain Non-Capture as warranted | abstraction universally prohibited |
| PATH→SUB move | new `DECOMPOSE` claim only where an existing composite is opened | rescue of prior PATH failure |
| PATH→RETYPE move | new `PROJECT_AS` claim only with preserved origin type | retroactive target-object repair |

Local boundary findings remain separate from canonical Output Classes and operation results.

## Chapter 16 WP1 — COMPOSE Result under PATH Boundary Pressure

A Chapter-15 `COMPOSE` occurrence does not inherit PATH-boundary passage.

```text
complete COMPOSE procedure
≠ lower-bound gain
≠ upper-bound traceability automatically
```

WP1 tests whether temporal differentiation adds praxeological purchase and whether the resulting composite remains source-sensitive and reconstructible. A valid chronology may remain below a stronger target threshold; a formally complete composite may exceed the Ceiling.

No `DECOMPOSE` or `PROJECT_AS` occurrence is performed. Later finer reconstruction or target-function assignment remains a new operation and cannot repair a failed PATH claim retroactively.

## Chapter 16 WP2 — PATH Boundaries to `DECOMPOSE` and `PROJECT_AS`

```text
failed PATH claim
+ PROJECT_AS label
≠ repaired origin object

failed PATH claim
+ finer detail
≠ completed DECOMPOSE
```

A lawful `PROJECT_AS` must name the actual origin-typed object and record a new bounded target-function claim. A lawful `DECOMPOSE` must open an identified compressed occurrence or composite while preserving the same reference object, Type Integrity, source lineage, uncertainty, and Loss.

Interface expansion, nested graph display, data volume, contextual usefulness, or later operation success never erase an earlier failed PATH claim.

## Chapter 16 WP3 — Boundary Results and Later Operations

A PATH boundary finding governs the current claim. It does not execute `DECOMPOSE` or `PROJECT_AS`.

```text
failed PATH claim
+ finer graph
≠ completed DECOMPOSE

failed PATH claim
+ contextual function
≠ completed PROJECT_AS
```

A lawful later operation is a new testable claim with a separate record and preserves the earlier result, inherited uncertainty, Loss, and Claim Ceiling.

## Chapter 16 Provisional-Lock PATH Boundary Procedure

Chapter 16 introduces no fourth operation. It applies the existing Admissibility Band to temporal objects and `COMPOSE` results, while keeping later `DECOMPOSE` and `PROJECT_AS` occurrences separate.

```text
PATH boundary finding
≠ DECOMPOSE occurrence
≠ PROJECT_AS occurrence
```

A finer graph is not `DECOMPOSE` automatically. A useful contextual function is not proof of the origin Path or Trajectory. Any lawful later operation is a new testable claim with its own Shared Record, Loss, ceilings, and output mapping.

Canonical return: [`Chapter 16 completion boundary`](../01_blocks/02_part_i_path.md#chapter-16-completion-boundary).

## Chapter 17 Preparation — Case and Operation Handoff

Chapter 17 tests actual PATH-side `COMPOSE` occurrences and operation confusions. Each operation-bearing case must use a separate Shared Transformation Record and preserve:

- source and target typing;
- Selection, Ordering, Frame, and Formation Rules;
- constitutive relations;
- five-part Loss;
- Counterfactual Sensitivity;
- result and canonical mapping.

The Path-or-Projection confusion case must keep the PATH reconstruction and any later `PROJECT_AS` occurrence in separate records. Additional detail or interface expansion is not automatically `DECOMPOSE`.

## Chapter 17 WP1 — Case-Level COMPOSE Records

Three standalone `COMPOSE` occurrences are now registered through case artifacts:

| Case | Source field | Target | Mapping |
|---|---|---|---|
| `C17-LINEAR-01` | four ordered configuration/transition structures | bounded Path | `admissible` |
| `C17-BRANCH-01` | Branch Point, realized route, rejected route, later closure | branching Path | `admissible` |
| `C17-LAMBDA-01` | expectation, central `Λ`, positive sub-events, later carriers, repair | source-sensitive Trajectory | `admissible` |

No record assigns a contextual target function. Any such claim remains a separate `PROJECT_AS` occurrence.

## Chapter 17 WP2-A — Comparative and Weak-Dependence COMPOSE Cases

The two WP2-A records remain single `COMPOSE` occurrences. The first forms a comparative Path-Dependence object from two source-traceable Paths; the second forms a repeated-pattern Path and tests current-state sufficiency. Neither executes `DECOMPOSE` or `PROJECT_AS`.

```text
comparative composition
≠ target-function projection

current-state test
≠ decomposition
```

## Chapter 17 WP2-B — Reduced and Failed COMPOSE Occurrences

`C17-CHRON-01`, `C17-MACRO-01`, and `C17-TEL-01` remain explicit `COMPOSE` attempts. The first requires Claim Reduction; the latter two fail. None silently switches to `DECOMPOSE` or `PROJECT_AS`, and every weaker route requires a new record.


## Chapter 17 WP2-C — Final Countercase COMPOSE Occurrences

`C17-OMEGA-01` and `C17-FALSEL-01` remain explicit `COMPOSE` attempts. The first fails; the second requires Claim Reduction. Neither silently becomes `DECOMPOSE` or `PROJECT_AS`, and every differentiated Path, chronology, or event-field route requires a new record.


## Chapter 17 WP3-A Operation Separation

`C17-PROJ-01` and `C17-ATTR-01` instantiate `COMPOSE` for origin temporal objects and preserve pending function claims without executing `PROJECT_AS`. `C17-RES-01` instantiates a separate `DECOMPOSE` resolution test on a prior Path composite; interface expansion alone remains non-operative. Every changed operation requires a new record.


## Chapter 17 WP3-B — PATH Operation Closure

PATH closes with `COMPOSE` as its governing operation and preserves one `DECOMPOSE` confusion-case record solely to test the PATH/SUB boundary. No operation inherits success from another occurrence. A later Frame- or Attractor-function remains a new `PROJECT_AS` claim and record.

## Part I — PATH Provisional-Lock Operation Boundary

`COMPOSE` is the governing PATH operation. The single Chapter-17 `DECOMPOSE` record tests resolution neutrality and the PATH/SUB boundary without changing PATH ownership. No `PROJECT_AS` record is executed. The lock does not authorize later operations; each future operation requires a new record and testable claim.

## Chapter 18 Preparation Handoff — Compressed Source Entry

Chapter 18 prepares the input to `DECOMPOSE`; it does not execute the operation.

A valid preparation declaration includes:

- source reference and lineage;
- origin/source type;
- source Frame, granularity, relative level, and temporal scope;
- current/coarser source function;
- known and unresolved internal structure;
- decomposition reason or no-decomposition reason;
- source and function uncertainty;
- preservation, Stop, and Non-Capture boundaries.

```text
compressed source declaration
≠ DECOMPOSE occurrence
≠ component discovery
```

The same reference object must remain the later reconstruction target. The coarse function remains open to confirmation, refinement, differentiation, partial preservation, rejection, or underdetermination. Chapter 19 owns the granularity relation; Chapter 20 owns procedure and result.

## Chapter 18 WP1 — Pre-DECOMPOSE Source-Candidate Boundary

Chapter 18 WP1 canonically defines the entry architecture preceding `DECOMPOSE`:

```text
identifiable occurrence or composite
+ bounded source-side typing and coordinates
+ known / unresolved distinction
→ possible source candidate
```

This is not an operation signature extension and not an operation occurrence. Chapter 19 still owns the source-to-target granularity relation. Chapter 20 still owns decomposition question, components, relations, source support, preservation testing, Loss, and result.

The following shortcuts remain prohibited:

- `SUB` treated as a fourth operation;
- operator-type decomposition;
- Path or Trajectory lock treated as decomposition permission;
- prior `COMPOSE` treated as losslessly invertible;
- eligible occurrence treated as admissible `DECOMPOSE`;
- unresolved internal structure treated as discovered components.

Canonical sites: [§18.1](../01_blocks/03_part_ii_sub.md#18-1-purpose-of-sub) and [§18.4](../01_blocks/03_part_ii_sub.md#18-4-operator-type-versus-decomposable-occurrence).



## Chapter 18 WP2 — Pre-Operation Compression Decision

Chapter 18 WP2 remains upstream of the `DECOMPOSE` operation:

```text
necessary compression assessment
→ insufficiency pressure, if any
→ well-formed reason or no-decomposition decision
→ Chapter 19 granularity relation
→ Chapter 20 DECOMPOSE, if warranted
```

Compression is not registered as a fourth operation. A reason to decompose does not select target granularity, populate components, reconstruct relations, or assign an Output Class. A no-decomposition decision does not execute `DECOMPOSE` and therefore is not a `resolution_neutral` operation result.

Canonical sites: [§18.5](../01_blocks/03_part_ii_sub.md#18-5-why-compression-is-necessary), [§18.6](../01_blocks/03_part_ii_sub.md#18-6-why-compression-can-become-insufficient), [§18.7](../01_blocks/03_part_ii_sub.md#18-7-reasons-to-decompose), [§18.8](../01_blocks/03_part_ii_sub.md#18-8-reasons-not-to-decompose).


## Chapter 18 WP3 — DECOMPOSE Source-Entry Completion

Chapter 18 now supplies the complete source-entry package for a possible later `DECOMPOSE` occurrence:

```text
source reference
+ source-side typing and coordinates
+ current/coarser function under test
+ known and unresolved internal structure
+ reason to decompose or not decompose
+ inherited Loss and uncertainty
+ Stop and Non-Capture availability
```

The package does not include target granularity, discovered components, component relations, source-function effect, operation result, target function, or automatic Output Class. Chapter 19 owns the granularity relation; Chapter 20 owns operation execution.

```text
source readiness ≠ DECOMPOSE success
source preservation ≠ source immunization
```

Canonical sites: [§18.9](../01_blocks/03_part_ii_sub.md#18-9-preservation-requirement) and [§18.10](../01_blocks/03_part_ii_sub.md#18-10-minimal-source-declaration).


## Chapter 18 Provisional-Lock Handoff

The provisionally locked source-side sequence is:

```text
occurrence or composite identified
→ provisional elementarity or compression declared
→ reason to decompose / not decompose bounded
→ source preservation and uncertainty retained
→ Minimal Source Declaration
→ Chapter 19 granularity test
→ Chapter 20 DECOMPOSE, only if warranted
```

No arrow inherits admissibility, truth, target function, or authority. `DECOMPOSE` is not executed in Chapter 18. Primary site: [Chapter 18 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-18-completion-boundary).

## Chapter 19 Preparation — Granularity Gate before DECOMPOSE

Chapter 19 prepares the coordinate relation required before the Chapter-20 procedure:

```text
Chapter 18 source object and reason
→ Chapter 19 source-to-target granularity relation
→ Chapter 20 DECOMPOSE occurrence
```

The gate requires explicit source and target granularities, distinction-set change, Frame/reference status, expected praxis difference, and comparison rationale. Coordinate completion does not establish operation identity, component discovery, operation success, or Output Class.

The eight-field Minimal Granularity Relation is conceptual and maps to existing Shared Record paths plus controlled `extensions`; it is not a parallel schema.

## Chapter 19 WP1 — Canonical Coordinate Gate

The canonical handoff is now:

```text
Chapter 18 source declaration
→ Chapter 19 WP1 granularity direction, comparator, Frame status, and expected difference
→ Chapter 19 WP2–WP3 component and comparison architecture
→ Chapter 20 DECOMPOSE procedure
```

WP1 establishes a necessary coordinate gate, not operation identity. It withholds source-supported component discovery, component relations, comparability classification, the Minimal Granularity Relation, source-function effect, operation result, and Chapter-25 resolution outcome.

Primary site: [Chapter 19 WP1](../01_blocks/03_part_ii_sub.md#chapter-19-granularity-change-and-the-logic-of-decomposition).

## Chapter 19 WP2 — Canonical Component-Eligibility Gate

The coordinate handoff now includes a component-eligibility layer before Chapter 20:

```text
Chapter 19 WP1
→ changed distinction set and coordinate direction

Chapter 19 WP2
→ local/distributed candidate forms and conjunctive component burden

Chapter 19 WP3
→ comparability, mismatch, Lower Granularity Question, Minimal Granularity Relation

Chapter 20
→ actual component/relation reconstruction and DECOMPOSE result
```

WP2 does not execute `DECOMPOSE`. It permits carrying, disturbing, and replaceable component candidates while withholding actual component status, necessity, sufficiency, causality, source-function effect, and operation result.

Primary sites: [§19.5–§19.7](../01_blocks/03_part_ii_sub.md#19-5-change-of-distinction-set).

## Chapter 19 WP3 — Canonical Granularity-Relation Handoff

```text
Chapter 18
→ compressed source object and reason

Chapter 19
→ source-to-target granularity relation,
comparison basis, Lower Granularity Question,
and exact Minimal Granularity Relation

Chapter 20
→ actual component/relation reconstruction,
source-function test, DECOMPOSE Record, and result
```

Chapter 19 comparison descriptions are not operations or Output Classes. The eight-field Minimal Granularity Relation maps to existing Shared Record carriers and controlled `extensions`; it does not execute `DECOMPOSE` or replace the schema.

Primary sites: [§19.8–§19.11](../01_blocks/03_part_ii_sub.md#19-8-granularity-comparability).


## Chapter 19 Provisional-Lock Handoff

The provisionally locked coordinate sequence is:

```text
Chapter-18 source declaration
→ source-to-target granularity relation
→ distinction-set and comparison burden
→ Minimal Granularity Relation
→ Chapter-20 Preparation Gate
→ DECOMPOSE procedure, only if warranted
```

No arrow inherits truth, source support, component status, operation success, target function, or authority. Primary site: [Chapter-19 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-19-completion-boundary).

## Chapter 20 Preparation — Complete DECOMPOSE Procedure

The prepared procedure requires:

```text
identifiable compressed source
+ precise decomposition question
+ declared granularity relation
+ source-supported components
+ component relations
+ internal temporality where applicable
+ source-function test
+ Loss, Stop, Non-Capture
+ separated Output mapping
```

Four result axes remain distinct:

```text
local operation result
≠ source-function effect
≠ prior source-claim disposition
≠ canonical Output Class
```

Chapter 20 owns the generic procedure. Chapters 21–24 own source-family applications; Chapter 25 owns the full resolution taxonomy; Chapter 26 owns operation-boundary adjudication. Preparation control: [`../_workfiles/chapter_preparation/Chapter_20_Preparation_Record.md`](../_workfiles/chapter_preparation/Chapter_20_Preparation_Record.md).

## Chapter 20 WP1 — DECOMPOSE Entry Procedure

WP1 fixes the first four procedural stages:

```text
1. preserve exact DECOMPOSE identity
2. test conjunctive preconditions
3. restate independently identifiable source object
4. formulate one precise decomposition question
```

The procedure consumes Chapter-18 source entry and Chapter-19 granularity relation without inheriting operation warrant or success. Generic detail, atomization, operator-type decomposition, preferred-conclusion questions, new-Path selection, and target-function assignment remain excluded.

Primary sites: [§20.1–§20.4](../01_blocks/03_part_ii_sub.md#20-1-definition).

## Chapter 20 WP2 — DECOMPOSE Reconstruction Procedure

WP2 adds the middle procedural stages:

```text
5. declare expected additional difference and no-gain
6. map claim-specific source support and precision ceiling
7. establish components through five conjunctive burdens
8. reconstruct component relations and conditional internal temporality
```

A list of details or components does not complete `DECOMPOSE`. Source-function effect, operation result, canonical Output Class, final Loss, failure, and the complete Record remain pending.

Primary sites: [§20.5–§20.8](../01_blocks/03_part_ii_sub.md#20-5-expected-additional-difference).

## Chapter 20 WP3 — DECOMPOSE Result and Record Completion

WP3 completes the generic procedure:

```text
9. test source-function effect without immunization
10. separate local result, source-function effect, prior claim disposition, and canonical class
11. disclose non-invertibility and operation-switch boundaries
12. route Failure, Mandatory Stop, and Non-Capture separately
13. complete the sixteen-field DECOMPOSE view within the Shared Transformation Record
```

A rejected source function may coexist with a successful `DECOMPOSE` occurrence. A new Path requires `COMPOSE`; a contextual target function requires `PROJECT_AS`.

Primary sites: [§20.9–§20.13](../01_blocks/03_part_ii_sub.md#20-9-preservation-of-source-function).

## Chapter 20 WP4 — Generic DECOMPOSE Procedure Lock

Chapter 20 is provisionally locked as the complete generic `DECOMPOSE` procedure: explicit source and question, declared granularity relation, expected difference and no-gain condition, source-support mapping, component and relation reconstruction, conditional internal temporality, source-function testing, four-axis result separation, Loss, Output-Class mapping, non-invertibility, Failure/Stop/Non-Capture, and the complete Record view.

```text
complete generic DECOMPOSE procedure
≠ completed occurrence-family theory
≠ full resolution taxonomy
≠ SUB lock
```

Primary site: [Chapter-20 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-20-completion-boundary).

## Chapter 21 Preparation — Family-Specific DECOMPOSE Application

Chapter 21 reuses the complete Chapter-20 procedure across Frame-, Attractor-, Asymmetry-, Impulse-, and Binding-typed occurrences. It changes the family-specific question and evidence burden, not the operation identity.

Dynamic Attractor target-function claims remain `PROJECT_AS`; formation of a new macro-object from local asymmetries remains `COMPOSE`.

Preparation control: [Chapter 21 Preparation Record](../_workfiles/chapter_preparation/Chapter_21_Preparation_Record.md).

## Chapter 21 WP1 — Frame-Family DECOMPOSE Application

WP1 reuses the Chapter-20 generic procedure for one Frame-typed occurrence. It adds only family-specific burdens: formation/function separation, source-supported boundary practices, heterogeneous maintenance, substitution, counterevidence, layered typing, and person-inference prohibition.

```text
family-specific application
≠ new operation
≠ operator redefinition
```

Primary sites: [§21.1–§21.4](../01_blocks/03_part_ii_sub.md#chapter-21-decomposing-operator-typed-occurrences).

## Chapter 21 WP2 — Attractor/Asymmetry DECOMPOSE Application

WP2 reuses the generic Chapter-20 procedure for Attractor- and Asymmetry-typed occurrences. A broader object assembled from several occurrences requires `COMPOSE`; a contextual Attractor-, Frame-, governance-, or other target function requires `PROJECT_AS`.

```text
occurrence-level DECOMPOSE
≠ broader-object COMPOSE
≠ target-function PROJECT_AS
```

Primary sites: [§21.5–§21.9](../01_blocks/03_part_ii_sub.md#21-5-attractor-typed-occurrence).

## Chapter 21 WP3 — Impulse/Binding DECOMPOSE Application

WP3 applies the generic Chapter-20 procedure to Impulse- and Binding-typed occurrences, then completes occurrence-family Failure, Stop, Non-Capture, and result-axis logic. Selecting several activations or commitments into a new object still requires `COMPOSE`; assigning a contextual function still requires `PROJECT_AS`.

Primary sites: [§21.10](../01_blocks/03_part_ii_sub.md#21-10-impulse-typed-occurrence)–[§21.12](../01_blocks/03_part_ii_sub.md#21-12-failed-operator-occurrence-decomposition).

## Chapter 21 WP4 Operation Lock

Chapter 21 is provisionally locked as a family-specific application of the Chapter-20 `DECOMPOSE` procedure. A broader object assembled from several occurrences still requires `COMPOSE`; a contextual target function still requires `PROJECT_AS`. The five families do not add a fourth operation or modify an operation signature.

Primary site: [Chapter-21 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-21-completion-boundary).

## Chapter 22 Preparation — Composite DECOMPOSE Application

Chapter 22 prepares `DECOMPOSE` for already-composite source objects. The operation must retain the same bounded composite reference while reconstructing the internal composition map, component roles, distributed function, redundancy, substitution, conflict, stability, inherited composition trace, and Loss.

```text
DECOMPOSE(COMPOSE(X))
≠ X
```

The operation does not undo prior selection or recover irrecoverable sources. Selecting several previously separate structures into a new macro-object remains `COMPOSE`; assigning a contextual higher-level function remains `PROJECT_AS`.

Preparation control: [Chapter 22 Preparation Record](../_workfiles/chapter_preparation/Chapter_22_Preparation_Record.md).

## Chapter 22 WP1 — Composite DECOMPOSE Entry and Map

WP1 reuses the Chapter-20 generic `DECOMPOSE` procedure for already-composite source objects. It establishes source-entry, inherited-Loss, map, role, trace, and operator-weighting burdens without performing a new `COMPOSE`, assigning a `PROJECT_AS` target function, or completing the Chapter-22 operation result.

Primary site: [§§22.1–22.4](../01_blocks/03_part_ii_sub.md#chapter-22-decomposing-composite-structures).

## Chapter 22 WP2 — Composite DECOMPOSE Middle Procedure

Within the same bounded source composite, `DECOMPOSE` may reconstruct source-side modulation, distributed function, redundancy, substitution, qualitative thresholds, and internal conflict. Same-reference continuity and the declared composite boundary remain mandatory.

```text
opening supported distribution or conflict inside the same composite
→ DECOMPOSE

forming a new object from previously separate structures
→ COMPOSE

assigning a contextual target function
→ PROJECT_AS
```

Primary sites: [§§22.5–22.8](../01_blocks/03_part_ii_sub.md#22-5-modulating-profiles).  
Execution control: [Chapter 22 Preparation/Execution Record](../_workfiles/chapter_preparation/Chapter_22_Preparation_Record.md).

## Chapter 22 WP3 Operation Return

`DECOMPOSE` remains the sole operation while the same bounded source composite is reconstructed through stability, non-fragmentation, Failure/Stop/Non-Capture, and Record discipline. Forming a new macro-object requires `COMPOSE`; assigning a contextual temporal, governance, or profile function requires `PROJECT_AS`.

Primary sites: [§§22.9–22.11](../01_blocks/03_part_ii_sub.md#22-9-composite-stability).

## Chapter 22 WP4 Operation Lock

Chapter 22 is provisionally locked as relational `DECOMPOSE` of already-composite source objects. A newly assembled macro-object still requires `COMPOSE`; a contextual higher-level function still requires `PROJECT_AS`. Composite decomposition does not invert a prior `COMPOSE` occurrence and does not add a fourth operation.

Primary site: [Chapter-22 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-22-completion-boundary).

## Chapter 23 Preparation — Temporal DECOMPOSE Application

Chapter 23 prepares `DECOMPOSE` for apparently punctual Events, Extended Events, Event Clusters, Non-Events, delay structures, and repeated non-decisions. The same bounded source reference must remain visible while phases, sub-events, temporal relations, expectations, delays, thresholds, and completion conditions are reconstructed.

Selecting independent Events into a new Event Cluster may require `COMPOSE`. Constructing a Path or Trajectory remains PATH/Chapter-24 work. Assigning a contextual higher-level function remains `PROJECT_AS`.

```text
finer temporal map of the same source
≠ new Path automatically
≠ target function
```

Preparation control: [Chapter 23 Preparation Record](../_workfiles/chapter_preparation/Chapter_23_Preparation_Record.md).

## Chapter 23 WP1 Temporal DECOMPOSE Return

Chapter 23 WP1 applies `DECOMPOSE` where an independently warranted coarse Event-like source object is opened into finer phases, thresholds, role shifts, completion relations, or locally distinguishable Events while the same source reference remains testable.

```text
coarse Event opened into related finer structure
→ DECOMPOSE candidate

independent Events selected and related into a new cluster
→ COMPOSE claim

new contextual temporal function assigned
→ PROJECT_AS claim
```

A category revision from apparently punctual Event to Extended Event or Event Cluster does not itself create a fourth operation. Primary sites: [§23.1](../01_blocks/03_part_ii_sub.md#23-1-event-decomposition) and [§23.3](../01_blocks/03_part_ii_sub.md#23-3-event-cluster).

## Chapter 23 WP2 DECOMPOSE Application

`DECOMPOSE` opens the same bounded Non-Event source object into expectation support, positive sub-events, delay mechanisms, role and threshold relations, repeated decision opportunities, and absent binding occurrences. It does not form a new Event Cluster or Path silently, infer a target function, or derive intention from duration.

```text
positive internal Events found
≠ switch from DECOMPOSE to Event-only account automatically

broader realized sequence newly formed
→ possible COMPOSE/PATH claim, not hidden WP2 continuation
```

Primary sites: [§§23.5–23.8](../01_blocks/03_part_ii_sub.md#23-5-non-event-decomposition).



## Chapter 23 WP3 — Temporal DECOMPOSE Completion

Temporal `DECOMPOSE` reconstructs supported internal order, overlap, partial order, thresholds, interruptions, and multiple clocks while preserving or warrantably revising the same Event/Non-Event reference object. Timestamp multiplication without changed praxis reconstruction is drift/no-gain pressure. New Event-cluster formation may require `COMPOSE`; broader Path/Trajectory reconstruction belongs to Chapter 24/PATH; contextual target function belongs to `PROJECT_AS`. Primary sites: [§§23.9–23.11](../01_blocks/03_part_ii_sub.md#23-9-internal-temporal-order).


## Chapter 23 Provisionally Locked — Temporal DECOMPOSE

Temporal `DECOMPOSE` opens the same bounded Event-like or Non-Event source object through source-supported phases, boundaries, expectations, non-realization, delays, internal order, and multiple clocks. New clustering of independent Events requires `COMPOSE`; broader Path/Trajectory reconstruction belongs to Chapter 24/PATH; contextual target function belongs to `PROJECT_AS`. Primary site: [Chapter 23](../01_blocks/03_part_ii_sub.md#23-decomposing-events-non-events-and-internal-temporal-structures).

## Chapter 24 Preparation — PATH-Source DECOMPOSE Classification

Chapter 24 prepares `DECOMPOSE` for PATH-produced source objects. Same-reference opening requires the source Path or Trajectory, original selection and formation rule, coarser function, and inherited Loss to remain reconstructible.

A materially different periodization, source selection, boundary, or formation rule may create a rival PATH object and therefore requires a separate `COMPOSE` occurrence. Assigning a contextual higher-level function remains `PROJECT_AS`.

```text
same Path opened under finer resolution
≠ rival Path newly composed
≠ contextual target function
```

Preparation control: [Chapter 24 Preparation Record](../_workfiles/chapter_preparation/Chapter_24_Preparation_Record.md).

## Chapter 24 WP1 PATH-Source DECOMPOSE Return

Chapter 24 WP1 applies `DECOMPOSE` where one independently warranted PATH-produced source object is opened through finer subpaths, intermediate configurations, and transition clusters while historical reference, formation lineage, and coarse function remain testable.

```text
same formed Path opened under finer resolution
→ DECOMPOSE candidate

materially new selection, periodization, or Path
→ COMPOSE candidate

Path assigned a contextual target function
→ PROJECT_AS candidate
```

Primary sites: [§24.1](../01_blocks/03_part_ii_sub.md#24-1-path-objects-as-sub-objects) and [§24.4](../01_blocks/03_part_ii_sub.md#24-4-transition-clusters).

## Chapter 24 WP2 PATH-Decomposition Return

`DECOMPOSE` remains applicable while turning-point, branch, internal-Frame, and continuation maps open the same PATH-produced source object under preserved historical reference and formation lineage.

```text
same source Path opened through turning points and branches
→ DECOMPOSE candidate

new counterfactual or rival Path formed
→ COMPOSE candidate

completed Path assigned a contextual target function
→ PROJECT_AS candidate
```

Primary sites: [§§24.5–24.8](../01_blocks/03_part_ii_sub.md#24-5-turning-points).

## Chapter 24 WP3 Operation and Non-Inverse Return

```text
same formed PATH object opened under finer resolution
→ DECOMPOSE candidate

materially new source selection, boundary, periodization, formation, macro-object, or referent
→ separate COMPOSE candidate

completed Path assigned a bounded target-context function
→ PROJECT_AS candidate

SUB(PATH(X))
≠ X
```

A rival `COMPOSE` may be admissible without making the original `DECOMPOSE` failed automatically. Every transformation keeps its own claim, Loss, result axes, and Record.

Primary sites: [§§24.9–24.11](../01_blocks/03_part_ii_sub.md#24-9-irrecoverable-compression).

## Chapter 24 Provisional-Lock Operation Return

```text
same formed PATH object opened under finer resolution
→ DECOMPOSE candidate

materially new selection, boundary, periodization, formation, macro-object, referent, or PATH question
→ separate COMPOSE candidate

bounded contextual target function
→ PROJECT_AS candidate
```

Each route requires its own Record, Loss, admissibility result, Claim Ceiling, and Stop/Non-Capture test. Chapter-24 closure adds no fourth operation.

## Chapter 25 Preparation — Resolution Classification after DECOMPOSE

Chapter 25 evaluates a completed or attempted finer reconstruction by comparing the coarse and finer claims, source support, relations, coarser function, calibration, and changed PraxisPurchase. It does not create a fourth operation.

```text
DECOMPOSE occurrence
→ local resolution assessment
→ separate canonical routing
```

A warranted finer claim after a failed coarse claim is a new testable claim; local support must not be transferred backward as retroactive rescue. Operation-boundary questions involving contextual function remain Chapter-26 work.

Preparation control: [Chapter 25 Preparation Record](../_workfiles/chapter_preparation/Chapter_25_Preparation_Record.md).

## Chapter 25 WP1 Resolution-Comparison Return

Chapter 25 WP1 evaluates a completed or attempted finer reconstruction. The comparison remains inside the declared `DECOMPOSE` claim only while the same tested burden and source object remain controlled. A materially new object or formation requires a separate `COMPOSE` claim; a contextual target function requires `PROJECT_AS`.

```text
same tested claim compared across warranted resolutions
→ resolution classification candidate

new source object or formation
→ separate COMPOSE candidate

new contextual target function
→ PROJECT_AS candidate
```

A granularity change after counterpressure does not repair the prior claim automatically.

Primary site: [§§25.1–25.4](../01_blocks/03_part_ii_sub.md#chapter-25-resolution-gain-neutrality-drift-and-escape).

## Chapter 25 WP2 Purchase, Support, and Calibration Return

A `DECOMPOSE` comparison succeeds only where finer components and relations remain source-supported and reconstructively connected to the coarser source function. Loss of that connection may require claim reduction, Failure, Stop, or a separately declared transformation; added formal structure cannot preserve operation status by itself.

A monitoring or parallel kernel may track declared runtime states, threshold versions, claim effects, support changes, and Stop conditions. Such monitoring is an implementation function, not a fourth STRATA operation and not a universal termination decider.

Primary site: [§§25.5–25.8](../01_blocks/03_part_ii_sub.md#25-5-detail-without-purchase).

## Chapter 25 WP3 Transformation Mapping

- [§25.9](../01_blocks/03_part_ii_sub.md#25-9-decomposition-fatigue) establishes Decomposition Fatigue as a bounded Stop marker.
- [§25.10](../01_blocks/03_part_ii_sub.md#25-10-resolution-classification) maps six local resolution families through existing formal fields and preserves four result axes.
- [§25.11](../01_blocks/03_part_ii_sub.md#25-11-stop-reentry-and-completion) completes Mandatory Stop, Non-Capture, re-entry, the nineteen-field Record view, and the Chapter-26 handoff.

Stop does not become a fourth operation, and re-entry is a new testable claim rather than continuation without disposition.

## Chapter 25 Provisional-Lock Operation Return

```text
same source object and tested claim opened at finer resolution
→ DECOMPOSE result assessment

materially new source selection or composite formation
→ separate COMPOSE candidate

bounded contextual target function assigned
→ separate PROJECT_AS candidate
```

Resolution Gain, Neutrality, Drift, Escape, unsupported refinement, Non-Capture, Stop, and re-entry are results or controls, not operations. A runtime or parallel kernel may monitor declared invariants and enforce bounded Stop conditions; it neither becomes a fourth operation nor decides universal halting or semantic truth.

## Chapter 26 Preparation — SUB/RETYPE Operation Test

The prepared decision burden asks:

1. Is finer internal source structure being opened?
2. Is granularity the primary changed coordinate?
3. Does the source object remain the explanation target?

If so, `DECOMPOSE` pressure is present.

Or:

1. Does the origin-typed source object remain a unit?
2. Is a bounded function asserted in another declared context?
3. Must origin type and target function be kept distinct?

If so, `PROJECT_AS` pressure is present.

A changed Frame without a target function may remain recontextualization. Dual-operation cases require linked but separate Records, claims, Loss declarations, and results.

Preparation control: [Chapter 26 Preparation Record](../_workfiles/chapter_preparation/Chapter_26_Preparation_Record.md).

## Chapter 26 WP1 Operation-Boundary Return

| Question | Primary operation pressure | Required preservation |
|---|---|---|
| What finer structures constitute or destabilize the source object? | `DECOMPOSE` | same bounded source reference and source-function traceability |
| What bounded function does the retained source object perform in a declared target context? | `PROJECT_AS` | origin type, contextual boundedness, separate target-function warrant |
| Has only the perspective, audience, or display changed? | neither operation established automatically | prior claim and source object remain visible |
| Are both internal structure and contextual function claimed? | dual-operation pressure | separate occurrences, claims, Records, Loss, and results |

The linguistic surface does not determine operation identity. No fourth operation is created.

Primary site: [Chapter 26 WP1](../01_blocks/03_part_ii_sub.md#chapter-26-the-boundary-between-sub-and-retype).

## Chapter 26 WP2 Operation-Boundary Return

| Comparison | Operation pressure | Boundary safeguard |
|---|---|---|
| Trajectory opened into subpaths, transition clusters, Non-Events, authority changes, and residues | `DECOMPOSE` | source object remains explanatory target |
| retained Trajectory proposed as a calibration, warning, coordination, or comparison object in a bounded context | `PROJECT_AS` | origin type preserved; target context and function separately warranted |
| Attractor occurrence opened into recurrence and maintenance relations | `DECOMPOSE` | occurrence opened; operator type protected |
| retained occurrence or Trajectory asserted to perform an Attractor-function elsewhere | `PROJECT_AS` | source recurrence is not automatic functional proof |
| changed Frame or graph view without either claim | neither operation established automatically | recontextualization remains possible |

Subtle and reverse misclassification are resolved by the operative claim, not by vocabulary. No fourth operation is introduced.

Primary site: [Chapter 26 WP2](../01_blocks/03_part_ii_sub.md#26-5-trajectory-decomposition-and-projection).

## Chapter 26 WP3 Transformation Mapping

- [§26.10](../01_blocks/03_part_ii_sub.md#26-10-sub-retype-decision-test) completes claim-segment-specific routing among DECOMPOSE, PROJECT_AS, recontextualization, dual-operation pressure, underdetermination, and invalid collapse.
- [§26.11](../01_blocks/03_part_ii_sub.md#26-11-dual-operation) requires separate operation occurrences, Records, Loss, results, and explicit link order.
- [§26.12](../01_blocks/03_part_ii_sub.md#26-12-invalid-collapse) routes mixed claims through segmentation, Failure, Stop, or Non-Capture and completes the nineteen-field boundary view and Chapter-27 handoff.

Dual operation does not add a fourth operation, and operation-boundary findings do not become Output Classes.

## Chapter 26 Provisional-Lock Operation Return

```text
internal constitution opened
+ granularity primarily changed
+ source object remains explanation target
→ DECOMPOSE candidate

origin-typed source object retained
+ bounded target context declared
+ source-traceable target function asserted
→ PROJECT_AS candidate

changed legibility without either claim
→ recontextualization only

both claims required
→ ordered chain of separate operation occurrences
```

Every operation link requires a separate Record, Loss declaration, result, and Stop/Non-Capture test. No success, failure, support, or authority transfers automatically across links.

## Chapter 27 Preparation — Local SUB Boundary Test

The prepared local test for `DECOMPOSE` requires conjunctively:

```text
AdditionalPraxisDifference
and SourceSupport
and SourceReferencePreserved
and ComponentRelationsReconstructible
and CoarserFunctionTraceableOrExplicitlyRevised
and TypeIntegrityMaintainedOrExplicitlyRevised
and GranularityDeclared
and StopConditionDefined
```

The lower boundary detects distinction without purchase. The upper boundary detects fragmentation without reconstructive anchoring. Source Ceiling, component sensitivity, coarser-function traceability, Stop, Claim Reduction, Failure, and Non-Capture remain separate findings or routes rather than new operations.

A granularity change never erases a prior failed claim. Re-entry requires a materially new basis and a new testable claim.

Preparation control: [Chapter 27 Preparation Record](../_workfiles/chapter_preparation/Chapter_27_Preparation_Record.md).

## Chapter 27 WP1 Local DECOMPOSE Boundary Return

| Boundary question | Local pressure | Required preservation |
|---|---|---|
| Does the additional distinction change a warranted praxis dimension? | admissible-range or Lower-Boundary pressure | tested claim and comparison basis |
| Is supported finer detail claim-neutral? | Resolution Neutrality candidate | support, comparability, and prior disposition |
| Do finer parts remain related to the same source object? | admissible-range or Upper-Boundary pressure | source reference and relation support |
| Can the finer findings return to the coarser function? | reconstruction, revision, reduction, or fragmentation pressure | explicit function-effect translation |

No new operation is created. Crossing a boundary changes the local admissibility result; it does not transform `DECOMPOSE` into another operation automatically.

Primary site: [Chapter 27 WP1](../01_blocks/03_part_ii_sub.md#chapter-27-sub-boundary-conditions).

## Chapter 27 WP2 DECOMPOSE Support Return

| WP2 question | Required declaration | Non-substitution |
|---|---|---|
| What is the finest responsible claim? | local Source Ceiling by component, relation, time, function, counterfactual, and type | model coherence is not source support |
| What load does a component carry? | bounded variation, supported relation map, source-function effect, assumptions, Loss | local sensitivity is not universal causality |
| Does the finer map reconstruct the source function? | explicit coarser-function translation | component inventory is not reconstruction |
| Does type integrity survive? | operator/occurrence/object/function levels plus explicit revision | initial type label is not protected from evidence |

No new operation or routing class is created. WP2 remains an internal `DECOMPOSE` admissibility and traceability test.

Primary site: [Chapter 27 WP2](../01_blocks/03_part_ii_sub.md#27-5-source-ceiling).

## Chapter 27 WP3 Complete DECOMPOSE Boundary Test

| Gate | Required question | Failure cannot be compensated by |
|---|---|---|
| Praxis difference | what warranted claim changes? | more detail |
| Source Support | what components and relations are carried? | model coherence |
| Source Reference | is the same object preserved or explicitly revised? | shared label |
| Relation reconstruction | how do parts connect? | component inventory |
| Coarser function | how is the source function affected? | local detail alone |
| Type integrity | what type claim survives or is revised? | nominal type retention |
| Granularity | what distinction set changed? | interface or rendering change |
| Stop | when is continuation unnecessary or inadmissible? | recursive decomposition |

Primary site: [Chapter 27 WP3](../01_blocks/03_part_ii_sub.md#27-9-no-privilege-of-fine-resolution).

## Chapter 27 Provisional-Lock DECOMPOSE Boundary

```text
eligible DECOMPOSE occurrence
+ eight conjunctive local gates
+ Stop / Reduction / Failure / Non-Capture / re-entry controls
→ bounded local SUB result
```

This lock adds no operation and does not pre-empt Chapter-28 cases or the SUB Part lock. Primary site: [Chapter 27 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-27-completion-boundary).

## Chapter 28 Preparation — Case-Level DECOMPOSE Discipline

Each Chapter-28 case executes or evaluates `DECOMPOSE` only through the existing signature. Cases involving a PATH source inherit an earlier `COMPOSE` history but require a distinct `DECOMPOSE` Record. A rival PATH claim requires a new `COMPOSE` occurrence. A contextual target function requires a separate `PROJECT_AS` occurrence.

```text
COMPOSE source
→ DECOMPOSE test

DECOMPOSE finding
→ possible separate COMPOSE or PROJECT_AS claim
```

No success, failure, support, Loss, Stop, or authority transfers automatically across links. Analogy and recontextualization remain non-operation results unless an actual operation claim is separately established.

Preparation control: [Chapter 28 Preparation Record](../_workfiles/chapter_preparation/Chapter_28_Preparation_Record.md).

## Chapter 28 WP1 — Six Executed DECOMPOSE Occurrences

WP1 instantiates six independent `DECOMPOSE` occurrences. The Frame, Attractor, Asymmetry, Non-Event, Trajectory, and Resolution-Gain sources remain bounded occurrences or composites. No case executes a new `COMPOSE` or `PROJECT_AS`; any such later claim requires a separate Record, Loss structure, and result.

## Chapter 28 WP2 — Attempted DECOMPOSE and Separated Operation Pressure

Eight primary records assess attempted DECOMPOSE claims. The SUB/RETYPE case registers a future PROJECT_AS claim; the SUB/new-PATH case registers a future COMPOSE claim. Neither secondary operation is executed or allowed to inherit the primary record’s support, Loss, or result.

## Chapter 28 WP3 — Final SUB Case Routing

The Analogy case does not establish DECOMPOSE and retains only bounded resemblance. The Modulator case preserves occurrence-level effects without adding an operator. SUB/RETYPE and SUB/new-PATH remain separated into future PROJECT_AS and COMPOSE claims with independent Records, Loss, results, and classes.

## Part II — SUB Provisional-Lock Operation Handoff

`DECOMPOSE` is provisionally locked as a bounded same-reference reconstruction operation across Chapters 18–28. The lock preserves separate occurrences for rival `COMPOSE` and later `PROJECT_AS` claims.

```text
successful DECOMPOSE
≠ successful COMPOSE
≠ successful PROJECT_AS

Part II lock
→ Chapter 29 Preparation
→ PROJECT_AS remains unexecuted until separately warranted
```

Primary site: [Chapter 28 and Part II completion boundary](../01_blocks/03_part_ii_sub.md#part-ii-sub-provisional-lock-boundary).

## Chapter 29 Preparation — PROJECT_AS Conceptual Entry

Chapter 29 prepares but does not execute the existing `PROJECT_AS` operation.

```text
origin-typed source object X
+ declared target context C
+ source-traceable bounded function F
→ PROJECT_AS candidate
```

A prior `COMPOSE` may form X and a prior `DECOMPOSE` may expose relevant source traces. Those operations remain separate occurrences with separate Records, Loss, and results. Their success does not establish the target function.

```text
successful COMPOSE or DECOMPOSE
≠ successful PROJECT_AS
```

Chapter 30 alone owns the complete operation signature and record specification.

Preparation control: [Chapter 29 Preparation Record](../_workfiles/chapter_preparation/Chapter_29_Preparation_Record.md).


## Chapter 29 WP1 — Typed PROJECT_AS Candidate Entry

Chapter 29 WP1 establishes the conceptual entry packet for later `PROJECT_AS` without executing the operation:

```text
identified source object X
+ retained origin type T
+ declared target context C
+ specific candidate function F
→ typed PROJECT_AS candidate
```

A prior `COMPOSE` or `DECOMPOSE` may supply the source object or finer source trace. Each remains a separate occurrence with separate Record, Loss, and result. The same source object is tested in one candidate function-bearing context and one no-additional-function context. Chapter 30 retains ownership of the full signature, tests, alternatives, Loss, and operation result.

Primary site: [Chapter 29 WP1](../01_blocks/04_part_iii_retype.md#29-1-purpose-of-retype).

## Chapter 29 WP2 — PROJECT_AS Integrity and Continuity Burdens

WP2 remains pre-operational. It supplies the burdens that Chapter 30 must later operationalize for each `PROJECT_AS` occurrence:

```text
retained source object and origin type
+ load-bearing source trace
+ source-to-context functional relation
+ bounded source variation
+ declared target scope and Loss
→ PROJECT_AS assessment packet
```

The packet does not execute `PROJECT_AS`, select a final function result, or map a canonical Output Class. A prior `COMPOSE` or `DECOMPOSE` remains a separate occurrence and cannot transfer support or Loss automatically.

Primary sites: [§29.6](../01_blocks/04_part_iii_retype.md#29-6-source-object-integrity) through [§29.8](../01_blocks/04_part_iii_retype.md#29-8-contextual-boundedness).

## Chapter 29 WP3 — PROJECT_AS Boundary Consolidation

WP3 fixes the non-replacement and chain-segmentation rules before Chapter 30 operationalizes `PROJECT_AS`.

```text
Φ changes legibility
COMPOSE forms a new object
DECOMPOSE opens internal constitution
PROJECT_AS tests a bounded contextual function
```

A prior `COMPOSE` or `DECOMPOSE` may supply the source object or source trace. Neither transfers operation success, Loss, result, Output Class, or authority to `PROJECT_AS`. Every changed context, function, source typing, or scope creates a new testable claim and separate Record.

Primary sites: [§29.11](../01_blocks/04_part_iii_retype.md#29-11-retype-versus-recontextualization), [§29.12](../01_blocks/04_part_iii_retype.md#29-12-retype-versus-compose), and [§29.13](../01_blocks/04_part_iii_retype.md#29-13-retype-versus-decompose).

## Chapter 29 Provisional Lock and Chapter 30 Operation Preparation

Chapter 29 provisionally locks the conceptual `PROJECT_AS` burden without executing an occurrence. Chapter 30 now owns the complete operation procedure.

```text
Chapter 29 typed projection architecture
→ Chapter 30 PROJECT_AS operation procedure

conceptual lock
≠ operation success
```

Chapter 30 must retain separate source and target declarations, exact operation identity, Constitutive Source Trace, Counterfactual Sensitivity, validity scope, five-part Loss, alternatives including no-projection, local result, canonical mapping, and independent chain Records. No new operation or mixed occurrence is permitted.

Preparation control: [Chapter 30 Preparation Record](../_workfiles/chapter_preparation/Chapter_30_Preparation_Record.md).

## Chapter 30 WP1 — PROJECT_AS Operation Entry

WP1 operationalizes the entry side of the existing `PROJECT_AS` signature:

```text
PROJECT_AS:
(X_g, T_o, C_t)
→
(F_t, g', J, L, V)
```

The signature is an accountability map, not a causal or automatic function. WP1 fixes operation identity, symbol roles, conjunctive preconditions, and the complete source declaration including source reference, coordinates, basis, prior disposition, uncertainty, and inherited five-part Loss.

```text
entry packet complete
≠ target declaration complete
≠ Constitutive Source Trace complete
≠ projection executed
≠ result selected
```

Primary sites: [Chapter 30 WP1](../01_blocks/04_part_iii_retype.md#chapter-30-project-as-signature-context-and-validity-scope) and [WP1 Execution Record](../_workfiles/chapter_preparation/Chapter_30_Preparation_Record.md#16-wp1-execution-record).

## Chapter 30 WP2 — PROJECT_AS Target and Test Packet

WP2 extends the operation-entry packet without executing the operation:

```text
complete source declaration
+ complete target declaration
+ projection justification
+ expected praxeological difference
+ candidate Constitutive Source Trace
+ bounded Counterfactual Sensitivity architecture
→ testable PROJECT_AS packet
```

Target object and target function remain distinct. Source pointer and Constitutive Source Trace remain distinct. Sensitivity remains non-causal and non-canonical. Full validity scope, current projection Loss, alternatives, local result, canonical mapping, and complete Record remain owned by WP3.

Primary site: [Chapter 30 WP2](../01_blocks/04_part_iii_retype.md#30-5-target-declaration).

## Chapter 30 WP3 — Complete PROJECT_AS Operation View

`PROJECT_AS` now has a complete generic procedure through §§30.1–30.13:

```text
source entry
→ target declaration
→ justification and expected difference
→ Constitutive Source Trace
→ Counterfactual Sensitivity
→ Validity Scope
→ projection visibility + exact five-part Loss
→ alternatives including no-projection
→ local result + canonical mapping
→ Shared Record integration
```

The operation remains non-invertible, context-bound, non-causal, non-automatic, and non-authorizing. Any `COMPOSE` or `DECOMPOSE` alternative requires a separate occurrence and record. Chapter 30 selects no family-specific result.

Primary site: [PROJECT_AS Record](../01_blocks/04_part_iii_retype.md#30-13-project-as-record).

\n## Chapter 30 Provisional Lock and Chapter 31 Family Handoff\n\nThe complete generic `PROJECT_AS` procedure is provisionally locked without executing the pressure object. Chapter 31 instantiates one family claim only: `Trajectory → bounded frame-function in declared later context`. It inherits the procedure, not a result.\n\n```text\nChapter 30 method lock ≠ PROJECT_AS occurrence\nChapter 31 family test ≠ fourth operation\n```\n\nPrimary sites: [Chapter 30 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-30-completion-boundary) and [Chapter 31 Preparation Record](../_workfiles/chapter_preparation/Chapter_31_Preparation_Record.md).\n


## Chapter 31 WP1 — PROJECT_AS Family Entry

The family candidate instantiates the existing operation without executing it:

```text
PROJECT_AS(
  documented_trajectory_X,
  origin_type = Trajectory,
  target_context = later_configuration_Y_or_Z,
  candidate_function = bounded_frame_function
)
```

WP1 completes source and target family declarations, present-condition visibility, concrete target-difference specification, evidence-layer separation, and the same-source contrast. Historical Load, relative-load comparison, Counterfactual Sensitivity, alternatives, Loss result, local result, and canonical mapping remain open.

Primary sites: [Chapter 31 WP1](../01_blocks/04_part_iii_retype.md#chapter-31-trajectory-as-frame-function) and [WP1 Record](../_workfiles/chapter_preparation/Chapter_31_Preparation_Record.md#14-wp1-execution-record).


## Chapter 31 WP2 — `PROJECT_AS` Family Overlay

For trajectory-to-frame-function projection, WP2 adds the following family-specific burdens to the existing `PROJECT_AS` procedure:

- separate PATH source warrant from target-function warrant;
- identify source-traceable Historical-Load carriers;
- distinguish load-bearing from modulating features;
- name conditioned praxis dimensions, roles, levels, and time windows;
- prohibit determinism, inevitability, prediction, and causal monopoly;
- retain present and other historical frame sources;
- state relative load qualitatively and source-bound, without scoring.

These burdens do not create a fourth operation, a new schema, a target-function enum, or a result route. The same source `X` remains under open `Y/Z` pressure until WP3.

Primary site: [Chapter 31 WP2](../01_blocks/04_part_iii_retype.md#31-5-historical-load).


## Chapter 31 WP3 — `PROJECT_AS` Family Discrimination Overlay

The trajectory-to-frame-function family now includes rhetorical-history rejection, trace-role separation, four-route counterfactual pressure, same-end/different-history testing, competing projections, background relevance, no-projection, and failed-projection routes.

Each rival function, target context, role-set, time window, granularity, or praxis dimension remains a separate `PROJECT_AS` claim and Record. A present-frame account or Φ-only recontextualization is not silently converted into `PROJECT_AS`.

```text
same source + different function
→ new PROJECT_AS occurrence

failed frame projection
≠ failed source Trajectory
```

Primary site: [Chapter 31 WP3](../01_blocks/04_part_iii_retype.md#31-8-rhetorical-history-versus-frame-function).

## Chapter 31 Lock and Chapter 32 Preparation — Operation Chain

The trajectory-to-frame-function family is provisionally locked as a method without an executed anchor result. The next family preserves an explicit operation chain:

```text
COMPOSE(configurations, transitions, events, non-events)
→ Trajectory M

PROJECT_AS(Trajectory M, wider Path B)
→ bounded Macro-Event function candidate
```

The operations require separate occurrences, Records, Loss profiles, alternatives, and results. Failure of the Macro-Event projection does not automatically invalidate the source `COMPOSE` result.

Primary sites: [Chapter 31 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-31-completion-boundary) and [Chapter 32 Preparation Record](../_workfiles/chapter_preparation/Chapter_32_Preparation_Record.md).


## Chapter 32 WP1 — PROJECT_AS Family Entry

The family candidate instantiates the existing operation without executing it:

```text
PROJECT_AS(
  documented_trajectory_M,
  origin_type = Trajectory,
  target_context = wider_path_B_or_C,
  candidate_function = bounded_macro_event_function
)
```

WP1 completes source entry, Macro-Event function grammar, wider target-Frame declaration, boundary warrant, anti-label control, Origin-Type Preservation, and the same-source `B/C` contrast. Duration, heterogeneity, transition gain, Counterfactual Sensitivity, alternatives, Loss result, local result, and canonical mapping remain open.

Primary sites: [Chapter 32 WP1](../01_blocks/04_part_iii_retype.md#chapter-32-trajectory-as-macro-event) and [WP1 Record](../_workfiles/chapter_preparation/Chapter_32_Preparation_Record.md#14-wp1-execution-record).

## Chapter 32 WP2 — PROJECT_AS Preservation and Function Layer

WP2 adds the family-specific preservation and function requirements to the existing operation:

```text
PROJECT_AS(Trajectory M, wider Path B)
→ preserve duration and relevant heterogeneity
→ disclose visibility and exact five-part Loss
→ name a bounded transition difference
→ retain causal and alternative-source pressure
```

It does not execute the occurrence or merge it with the prior `COMPOSE` that formed `M`.

Primary sites: [§32.5](../01_blocks/04_part_iii_retype.md#32-5-internal-duration), [§32.6](../01_blocks/04_part_iii_retype.md#32-6-internal-heterogeneity), and [§32.7](../01_blocks/04_part_iii_retype.md#32-7-event-function).


## Chapter 32 WP3 — Operation-Chain and Failure Discipline

```text
COMPOSE(source structures)
→ Trajectory M
→ separate Record, Loss, and result

PROJECT_AS(Trajectory M, wider Path B or C)
→ Macro-Event function test
→ separate Record, Loss, and result
```

Phase, boundary, source-object, and target variation may narrow, stop, fail, or leave the projection uncaptured. A material source change returns the analysis to a new PATH/`COMPOSE` claim before a new `PROJECT_AS` occurrence. Projection failure does not automatically invalidate the prior source occurrence.

Primary sites: [§32.9](../01_blocks/04_part_iii_retype.md#32-9-macro-event-versus-compose) and [§32.11](../01_blocks/04_part_iii_retype.md#32-11-failed-macro-event-projection).

## Chapter 32 Lock — Separate Source Formation and Macro-Event Projection

```text
COMPOSE(source configurations and transitions)
→ Trajectory M
→ prior PATH Record, Loss, and result

PROJECT_AS(Trajectory M, wider Path B)
→ bounded Macro-Event function test
→ separate Record, Loss, and result
```

Chapter 32 provisionally locks this family method without adjudicating `M/B/C`.

Primary site: [Chapter 32 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-32-completion-boundary).

## Chapter 33 Preparation — Recurrent Form and Attractor-Function

The candidate source must be formed from multiple independently warranted and sufficiently comparable Trajectories. Source formation and later projection remain separate occurrences.

```text
COMPOSE/RECONSTRUCT comparable Trajectories
→ recurrent trajectory form R

PROJECT_AS(R, later path field D)
→ bounded dynamic attractor-function candidate
```

A material change in trajectory selection, comparison coordinates, or constitutive form requires a new source claim before a new `PROJECT_AS` occurrence.

Primary site: [Chapter 33 Preparation Record](../_workfiles/chapter_preparation/Chapter_33_Preparation_Record.md).


## Chapter 33 WP1 — PROJECT_AS Family Entry

The family candidate instantiates the existing operation without executing it:

```text
PROJECT_AS(
  recurrent_trajectory_form_R,
  origin_type = derived_recurrent_form_composite,
  target_context = later_path_field_D_or_E,
  candidate_function = bounded_dynamic_attractor_function
)
```

Source formation across Trajectories remains analytically prior to the projection occurrence. Material changes to source trajectories, boundaries, comparison coordinates, or constitutive form require a new source claim before a new `PROJECT_AS` claim.

Primary sites: [Chapter 33 WP1](../01_blocks/04_part_iii_retype.md#chapter-33-recurrent-trajectory-form-as-attractor-function) and [WP1 Record](../_workfiles/chapter_preparation/Chapter_33_Preparation_Record.md#14-wp1-execution-record).

## Chapter 33 WP2 — PROJECT_AS Recurrence/Load Layer

WP2 adds family-specific source and target burdens to the existing operation:

```text
PROJECT_AS(recurrent form R, later path field D)
→ preserve constitutive/variable/background/uncertain/incompatible positions
→ require temporally directed reproduction or path influence
→ state concrete bounded Attractor Load and later-path difference
→ separate dynamic and static function claims
```

The occurrence remains unexecuted and does not inherit success from the `COMPOSE` operations that formed the source Trajectories or recurrent composite.

Primary site: [Chapter 33 WP2](../01_blocks/04_part_iii_retype.md#33-5-constitutive-repetition).

## Chapter 33 WP3 PROJECT_AS Return

For the recurrent-form-to-attractor-function family, `PROJECT_AS` must preserve:

- independently warranted source Trajectories and target-blind recurrent-form source formation;
- comparison coordinates, source-position distinctions, break conditions, and known missingness;
- temporal reproduction/path-influence pathway and concrete later-path work;
- same-source `D/E` contrast and present/rival source pressure;
- exact five-part Loss, Validity Scope, Claim Ceiling, Stop, and Non-Capture;
- separate dynamic/static claims and outcomes.

Retrospective motif, source selection, common Frame, independent regeneration, multiple forms, static-only function, descriptive recurrence, and no stable source remain alternatives. Failed `PROJECT_AS` does not retroactively rewrite each PATH source claim.

Primary site: [Chapter 33 WP3](../01_blocks/04_part_iii_retype.md#33-8-recurrent-form-versus-retrospective-similarity).

## Chapter 33 Lock and Chapter 34 PROJECT_AS Entry

Chapter 33 provisionally locks the recurrent-form family without executing the `R/D/E` occurrence. Chapter 34 prepares:

```text
independently warranted relational composite Q
PROJECT_AS
bounded higher-level function in H
```

Source-composite formation, `DECOMPOSE`, and `PROJECT_AS` remain separate occurrences with separate Records, Loss profiles, and results.

## Chapter 34 WP1 — PROJECT_AS Composite-Family Entry

The existing operation receives one derived relational-composite source and one declared higher-level target context:

```text
PROJECT_AS(Q, origin_type = derived relational composite, target_context = H or I)
→ boundary-, attractor-, or asymmetry/access-function candidate
```

WP1 requires independently warranted components and relations, full target coordinates, same-source `H/I` contrast, concrete target difference, and operator/non-authority boundaries. It does not execute `PROJECT_AS`, select component load, establish functional formation, or choose an Output Class.

Primary sites: [Chapter 34 WP1](../01_blocks/04_part_iii_retype.md#chapter-34-composite-structures-as-higher-level-functions) and [WP1 Record](../_workfiles/chapter_preparation/Chapter_34_Preparation_Record.md#13-wp1-execution-record).

## Chapter 34 WP2 — PROJECT_AS Family-Load Layer

WP2 adds binding-, integration-, and emergence-specific burdens to the existing operation:

```text
PROJECT_AS(relational composite Q, target H or I)
→ preserve commitment or integration occurrence trace
→ require continuity, relation topology, and concrete target work
→ retain partiality, contradiction, substitution, and smaller-subset pressure
→ keep Ψ/Σ identity and source-free emergence prohibited
```

Component formation or revision remains source-side work; `DECOMPOSE` may inspect the composite; `PROJECT_AS` alone tests the bounded target function. These are separate occurrences with separate Records, Loss, and results. WP2 does not execute the `Q/H/I` projection.

Primary sites: [Chapter 34 WP2](../01_blocks/04_part_iii_retype.md#34-5-repeated-commitments-as-higher-level-psi-function) and [WP2 Record](../_workfiles/chapter_preparation/Chapter_34_Preparation_Record.md#14-wp2-execution-record).

## Chapter 34 WP3 — PROJECT_AS Formation and Failure Layer

WP3 completes the family audit burden for an eventual executed projection:

```text
PROJECT_AS(relational composite Q, target H or I)
→ distinguish aggregation from functional formation
→ test qualitative target-difference threshold
→ vary subset, relations, Frame, target conditions, and function candidate
→ prohibit authority increase
→ localize Reduction, Stop, Failure, and Non-Capture
```

The source composite may remain valid when the projection fails. A materially changed source boundary, relation map, target context, or function candidate is a new testable claim. No `Q/H/I` operation result is selected.

Primary sites: [Chapter 34 WP3](../01_blocks/04_part_iii_retype.md#34-8-aggregation-versus-functional-formation) and [WP3 Record](../_workfiles/chapter_preparation/Chapter_34_Preparation_Record.md#15-wp3-execution-record).

## Chapter 34 Lock and Chapter 35 PROJECT_AS Entry

Chapter 34 provisionally locks the composite-function family without executing `Q/H/I`. Chapter 35 prepares two distinct claim positions:

```text
source-supported operator weighting and modulating profile formation
≠
PROJECT_AS(profile, declared target context, bounded target function)
```

Profile description may remain source-side and functionally inert. Profile projection requires a separate occurrence, Record, Loss profile, Counterfactual Sensitivity result, and canonical route.

## Chapter 35 WP1 — Weighting and Modulation before PROJECT_AS

Weighting and modulation are analytical relations within a source Configuration/Composite; they are not STRATA operations.

```text
source opening required → DECOMPOSE occurrence
new relational source composite required → COMPOSE occurrence
bounded profile function in K or L tested → PROJECT_AS occurrence
weighting/modulation declaration → no fourth operation
```

WP1 declares the source packet and stable `K/L` target coordinates. It does not form a profile, execute `PROJECT_AS`, establish a target difference, or select an Output Class.

Primary sites: [Chapter 35 WP1](../01_blocks/04_part_iii_retype.md#chapter-35-operator-weighting-modulation-and-emergent-functional-profiles) and [WP1 Record](../_workfiles/chapter_preparation/Chapter_35_Preparation_Record.md#13-wp1-execution-record).

## Chapter 35 WP2 — Profile Formation before Projection

WP2 forms no fourth operation. Source-side profile formation may depend on earlier `DECOMPOSE` or `COMPOSE` records, but the claim that the profile performs a bounded function in `K` requires a later, separately declared `PROJECT_AS` occurrence.

```text
source-side profile relation established
≠ PROJECT_AS executed

profile organizes P
≠ profile functions in K
```

Primary sites: [§§35.5–35.7](../01_blocks/04_part_iii_retype.md#35-5-modulating-profile) and [WP2 Record](../_workfiles/chapter_preparation/Chapter_35_Preparation_Record.md#14-wp2-execution-record).

## Chapter 35 WP3 — Explicit Profile Projection

A source-side profile claim is not itself `PROJECT_AS`. Profile projection requires a new declared occurrence with its own target context, target function, Source Trace, Loss, Counterfactual Sensitivity, result, and no-projection alternative.

```text
profile formed in P ≠ profile projected in K
failed projection ≠ source occurrences invalid
```

Primary sites: [§35.9](../01_blocks/04_part_iii_retype.md#35-9-profile-projection) and [WP3 Record](../_workfiles/chapter_preparation/Chapter_35_Preparation_Record.md#15-wp3-execution-record).

## Chapter 35 Lock and Chapter 36 Projection Comparison

Chapter 36 compares separately declared `PROJECT_AS` candidates. Comparison is not a fourth operation and cannot repair an incomplete candidate Record.

```text
PROJECT_AS candidate A + PROJECT_AS candidate B
→ comparison claim

comparison claim ≠ PROJECT_AS occurrence
≠ COMPOSE of functions
≠ source-type selection
```

Primary site: [Chapter 36 Preparation](../_workfiles/chapter_preparation/Chapter_36_Preparation_Record.md).

## Chapter 36 WP1 — Comparison Entry after `PROJECT_AS`

Chapter 36 compares candidate `PROJECT_AS` claims only after each candidate declares its own source subset, target context, target level, target object, function, Claim Scope, validity scope, temporal scope, Source Trace, Loss, and alternatives.

Compatibility and competition are comparison descriptions, not fourth operations. Merging candidates may require a new `COMPOSE` or `PROJECT_AS` claim; it cannot be performed by label combination.

Primary site: [§§36.1–36.4](../01_blocks/04_part_iii_retype.md#36-1-multiple-plausible-functions).

## Chapter 36 WP2 — Comparison after Candidate-Specific `PROJECT_AS` Burdens

WP2 compares only projection candidates that remain viable under their own family methods. Comparison is not a fourth operation and cannot repair an incomplete `PROJECT_AS` occurrence.

```text
candidate family audit
→ comparative criteria
→ discriminative-performance test
→ bounded local comparison description

comparison
≠ operation
≠ automatic route or Output Class
```

Primary site: [WP2 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-36-wp2-completion-boundary).

## Chapter 36 WP3 — Projection Comparison Record without a Fourth Operation

The Projection Comparison Record is a view over separately executed candidate `PROJECT_AS` Records. It references candidate source subsets, target coordinates, Source Trace, exact Loss, alternatives, local descriptions, Stop, and Non-Capture without becoming `COMPOSE`, `DECOMPOSE`, `PROJECT_AS`, or a fourth operation.

```text
candidate PROJECT_AS records
→ controlled comparison view

comparison view
≠ merged operation record
≠ automatic route or Output Class
```

Primary site: [§36.10](../01_blocks/04_part_iii_retype.md#36-10-projection-comparison-record).

## Chapter 36 Lock and Chapter 37 Mapping Boundary

A valid cross-domain projection remains a complete `PROJECT_AS` occurrence. Structural analogy and symbolic mapping are not fourth operations and do not inherit a `PROJECT_AS` result.

```text
mapping relation ≠ PROJECT_AS automatically
analogy_only ≠ failed operation automatically
```

Primary site: [Chapter 37 Preparation](../_workfiles/chapter_preparation/Chapter_37_Preparation_Record.md).

## Chapter 37 WP1 — `PROJECT_AS` versus Analogy and Mapping

A valid cross-domain functional projection remains a complete `PROJECT_AS` occurrence. Structural analogy and formal mapping describe bounded correspondences but perform no STRATA operation by themselves. Label assignment performs neither `PROJECT_AS` nor another operation.

```text
mapping declaration
≠ PROJECT_AS occurrence

structural analogy
≠ fourth operation

shared notation
≠ operation execution
```

Primary site: [§37.2 Valid Functional Projection](../01_blocks/04_part_iii_retype.md#37-2-valid-functional-projection).

## Chapter 37 WP2 — Mapping Status and `PROJECT_AS`

Symbolic, formal, executable, analogy-only, and partial-analogy statuses are mapping descriptions. They do not execute a STRATA operation. Only a separately warranted source-dependent target-function claim constitutes `PROJECT_AS`.

```text
formal mapping completed
≠ PROJECT_AS completed

executable mapping completed
≠ target function established

analogy terminates
≠ failed operation automatically
```

Primary site: [§§37.5–37.7](../01_blocks/04_part_iii_retype.md#37-5-symbolic-formal-and-executable-mapping).

## Chapter 37 WP3 — Drift, Translation, and Operation Boundaries

A transition from analogy to target-function claim is a new `PROJECT_AS` claim, not a hidden completion of the analogy. Analogy drift, translation, symbolic mapping, formal mapping, and executable mapping are not STRATA operations.

```text
analogy becomes function claim
→ new PROJECT_AS burden

translation completed
≠ transformation operation completed
```

Primary site: [§§37.9–37.12](../01_blocks/04_part_iii_retype.md#37-9-analogy-drift).

## Chapter 37 Lock and Chapter 38 New-Claim Discipline

A projection after failure is a new independently testable `PROJECT_AS` claim. It requires its own target coordinates, Source Trace, exact Loss, alternatives, and result. Relocation does not erase the earlier disposition.

Separately declared cross-level, cross-granular, or dual-operation Records are not level mixing merely because they concern the same reference object.

Preparation site: [Chapter 38 Preparation Record](../_workfiles/chapter_preparation/Chapter_38_Preparation_Record.md#6-scientific-pressure-and-counterfactual-architecture).

## Chapter 38 WP1 — Type, Context, Metaphor, and `PROJECT_AS`

`PROJECT_AS` assigns a bounded target function while preserving origin type. A type-identity statement is a separate claim; bounded metaphor performs no STRATA operation. Completing missing target coordinates opens a new testable projection candidate rather than validating the incomplete claim retroactively.

```text
functions as T in C
→ PROJECT_AS candidate

is T as origin type
≠ PROJECT_AS result

bounded metaphor
≠ transformation operation
```

Primary site: [§§38.1–38.4](../01_blocks/04_part_iii_retype.md#38-1-invalid-type-jump).

## Chapter 38 WP2 — Cross-Level, Multi-Granular, and Post-Failure Operation Discipline

Cross-level or multi-granular analysis requires a declared relation or separate operation record. A projection after failure is a new `PROJECT_AS` claim; it retains the earlier disposition and carries new target coordinates, Source Trace, counterfactual variations, alternatives, and exact Loss.

```text
new level ≠ new operation automatically
relocation after failure ≠ rescue
COMPOSE output used by PROJECT_AS ≠ mixed operation
multiple declared records ≠ fourth operation
```

Primary site: [§§38.5–38.7](../01_blocks/04_part_iii_retype.md#38-5-unmarked-level-mixing).

## Chapter 38 WP3 — Scope Extension, Temporal Bound, and Invalid-View Discipline

Every material widening of context, object, population, level, period, or similarity class is a new `PROJECT_AS` claim. The original bounded claim remains separately testable. The Invalid Projection Record is a diagnostic view over existing records and does not add a fourth operation.

```text
bounded PROJECT_AS in C
+ proposed extension to C2
→ new PROJECT_AS claim

invalid-projection view
≠ transformation operation
≠ replacement Shared Transformation Record
```

Primary site: [§§38.10 and 38.13](../01_blocks/04_part_iii_retype.md#38-10-scope-inflation).



<a id="chapter-38-lock-and-chapter-39-preparation-operation-sync"></a>

## Chapter 38 Lock → Chapter 39 Local PROJECT_AS Gate

Chapter 38 closes the invalid-projection taxonomy while preserving every changed context, level, granularity, scope, time, function, evidence packet, or operation as a new independently testable claim. Chapter 39 applies the lower and upper RETYPE boundaries to complete `PROJECT_AS` candidates.

```text
new target coordinates
→ new PROJECT_AS occurrence

new occurrence
≠ rescue of earlier failure
```

The Chapter-39 gate remains a local audit over `PROJECT_AS`; it is not a fourth operation and does not merge with `COMPOSE` or `DECOMPOSE`.

<a id="chapter-39-wp1-operation-sync"></a>

## Chapter 39 WP1 — Local `PROJECT_AS` Boundary Entry

A `PROJECT_AS` candidate must add bounded Functional Gain above the lower RETYPE boundary and remain capable of constitutive Source Trace below the upper boundary. Source-only relevance, renaming, or target fit does not complete the operation.

```text
source remains relevant ≠ PROJECT_AS established
new label ≠ operation occurrence
```

Primary site: [§§39.1–39.4](../01_blocks/04_part_iii_retype.md#39-1-lower-retype-boundary).

<a id="chapter-39-wp2-operation-sync"></a>

## Chapter 39 WP2 — `PROJECT_AS` Source, Type, Context, and Sensitivity Gates

A `PROJECT_AS` candidate remains incomplete until it provides Constitutive Source Trace, preserves Type Integrity, declares complete target coordinates, and responds discriminatorily to material, irrelevant, removal, opposite-source, target-condition, context, time, and function variation.

```text
strong target fit
≠ completed PROJECT_AS occurrence
```

Primary site: [§§39.5–39.8](../01_blocks/04_part_iii_retype.md#39-5-function-without-source-trace).

<a id="chapter-39-wp3-operation-sync"></a>

## Chapter 39 WP3 — Complete Local `PROJECT_AS` Gate

A bounded `PROJECT_AS` claim must survive alternatives, analogy, elasticity, Stop, Non-Capture, exact Loss, and terminal-route discipline. New context, function, or source subset is a new testable claim.

Primary site: [§39.14](../01_blocks/04_part_iii_retype.md#39-14-retype-admissibility-test).

<a id="chapter-39-lock-and-chapter-40-preparation-operation-sync"></a>

## Chapter 39 Lock / Chapter 40 Operation Routing

The Chapter-39 gate is provisionally locked as a local `PROJECT_AS` test. Chapter 40 prepares separate case records for `PROJECT_AS` and must preserve operation boundaries in confusion cases.

```text
DECOMPOSE then PROJECT_AS
→ two records

COMPOSE then PROJECT_AS
→ two records

Φ recontextualization without target function
≠ PROJECT_AS
```

The Chapter-40 case architecture creates no fourth operation and no merged multi-operation record.

## Chapter 40 WP1 Case/Operation Routing

Each positive family is a prospective `PROJECT_AS` occurrence with a source-locked packet and complete target coordinates. `P4` requires a separately warranted prior `COMPOSE`; no operation result is inherited. Compatible and competing projection families require separate candidate claims, Loss, audits, and mappings. Canonical family prose is not a Transformation Record.

<a id="chapter-40-wp2-operation-sync"></a>

## Chapter 40 WP2 Operation Separation

The countercases preserve exactly three operations:

- Origin-type and context cases test bounded `PROJECT_AS` claims without changing source type.
- Mere aggregation may require a separate warranted `COMPOSE` before any later higher-level `PROJECT_AS`.
- Claim rescue through a changed context, function, level, or source subset requires a new `PROJECT_AS` occurrence and retained prior disposition.

```text
new claim coordinates → new operation occurrence
new occurrence ≠ prior failure erased
countercase view ≠ fourth operation
```

Primary site: [§§40.9–40.15](../01_blocks/04_part_iii_retype.md#40-9-countercase-1-origin-type-replacement).

<a id="chapter-40-wp3-operation-sync"></a>

## Chapter 40 WP3 Operation Separation

The six confusion cases preserve exact routing boundaries:

```text
DECOMPOSE then PROJECT_AS → two records and two Loss ledgers
COMPOSE then PROJECT_AS → two records and two results
Φ recontextualization without a specific target function ≠ PROJECT_AS
analogy or mapping ≠ PROJECT_AS automatically
```

A controlled sequence of operations is not a merged operation or a fourth operation. No route or operation result is selected in WP3.


## Chapter 40 Exact Lock Routing and Chapter 41 Recursive-Operation Handoff

Chapter 40 separates two closure claims:

- Layer-1 case architecture and audit readiness → `admissible_with_bounded_claim`;
- artifact-complete Chapter-40/RETYPE lock → `mandatory_stop` until required artifacts exist.

Neither mapping applies to `P1–P7`, `N1–N7`, or `X1–X6`, which remain unexecuted.

Chapter 41 receives the governing chain rule:

```text
new operation occurrence
→ new claim
→ separate Record
→ separate Loss
→ separate result

new operation occurrence
≠ answer to prior objection automatically
```

LIMITS does not route or execute an operation.

## PROJECT_AS — PMS occurrence anchoring

For PMS-derived sources, `PROJECT_AS` uses existing `source_reference`, `source_basis`, `constitutive_source_trace`, `counterfactual_sensitivity`, and canonical `loss` positions to preserve an inspectable occurrence-level route where material.

```text
concrete occurrence relation varied
≠ abstract operator revised

successful source formation
≠ successful PROJECT_AS
```
## Chapter 41 WP1 Recursive-Continuation Control

Every recursive continuation remains separately declared:

```text
prior operation result preserved
+ fresh expected praxeological difference
+ separate Record
+ separate five-part Loss
+ separate result if executed
→ recursive operation candidate
```

`DECOMPOSE` may reveal finer source structure without repairing a prior failed projection. `COMPOSE` may form a valid broader composite without validating an earlier target function. Chain passage is distinct from local operation passage.

Primary sites: [§41.2](../01_blocks/05_part_iv_limits.md#41-2-recursive-availability), [§41.3](../01_blocks/05_part_iv_limits.md#41-3-the-risk-of-infinite-decomposition), and [§41.4](../01_blocks/05_part_iv_limits.md#41-4-the-risk-of-unlimited-composition).

## Chapter 41 WP2 — Projection and Chain-Admissibility Control

A `PROJECT_AS` occurrence requires target context, constitutive Source Trace, Counterfactual Sensitivity, TypeIntegrity, bounded validity, exact Loss, alternatives, and a separate result if executed. A technically available projection may end in Optional Stop where no additional praxeological purchase exists.

Every operation chain retains two cumulative burdens:

```text
local passage for each operation
+ admissible relation between operation occurrences
→ possible chain passage
```

Local success does not guarantee chain passage, and chain coherence cannot repair a failed local operation. Primary sites: [§41.5](../01_blocks/05_part_iv_limits.md#41-5-the-risk-of-arbitrary-projection) and [§41.7](../01_blocks/05_part_iv_limits.md#41-7-analytical-self-immunization).

## Chapter 41 WP3 — Constitutive Operation and Chain Control

LIMITS governs operation entry, formation, result disposition, reuse, and handoff. Every operation occurrence retains a separate claim and result; every chain relation is independently tested. Constraint, Loss, and disposition continuity may pass forward, while authority never does.

```text
local operation passage
+ handoff passage
+ later operation passage
→ possible chain passage
```

Primary sites: [§41.8](../01_blocks/05_part_iv_limits.md#41-8-limits-as-constitutive-structure) and [§41.9](../01_blocks/05_part_iv_limits.md#41-9-governing-limits-principle).


## Chapter 41 Lock and Chapter 42 Anti-Ontology Operation Route

Chapter 41 is provisionally locked at method-rationale scope. Chapter 42 receives the operation-specific anti-ontology rule:

```text
DECOMPOSE ≠ discovery of final constituents
COMPOSE ≠ revelation of an ultimate whole
PROJECT_AS ≠ ontological promotion
```

Each operation remains a bounded reconstruction occurrence with declared source, Frame, granularity, Claim Scope, Loss, alternatives, and no authority inheritance.

Primary route: [Chapter 42 Preparation Record](../_workfiles/chapter_preparation/Chapter_42_Preparation_Record.md).

## Chapter 42 WP1 — Relative Direction without Ontological Direction

`DECOMPOSE`, `COMPOSE`, and `PROJECT_AS` may involve relative downward, upward, or contextual movement. Direction words describe declared analytical relations; they do not indicate descent to fundamental reality, ascent to a more real whole, or passage into a new ontological stratum.

WP1 establishes the relational premise only. Final-constituent, ultimate-composite, and ontological-promotion controls remain assigned to WP2. Primary site: [§42.3](../01_blocks/05_part_iv_limits.md#42-3-no-discrete-reality-layers).

## Chapter 42 WP2 Operation Anti-Ontology Matrix

```text
DECOMPOSE → no final constituents
COMPOSE → no ultimate composite
PROJECT_AS → no ontological promotion
```

All three remain source-, Frame-, granularity-, Loss-, continuity-, and Claim-Scope-bound.


## Chapter 42 WP3 — Corrective Anti-Ontology Forms

- `DECOMPOSE` may reconstruct finer components and relations but its bounded formulation must expressly avoid final-constituent claims.
- `COMPOSE` may form a wider analytical object but must retain selection, compression, exclusion, uncertainty, irrecoverable Loss, alternatives, and no-totality status.
- `PROJECT_AS` may assign a bounded target function while preserving origin type, reference identity, Source Trace, sensitivity, context, and no ontological promotion.

A bounded rewrite corrects ontology drift but does not select an operation result or Output Class.

Primary site: [§42.9](../01_blocks/05_part_iv_limits.md#42-9-corrective-formulation).

## Chapter 42 Lock and Chapter 43 Comparative Operation Discipline

Chapter 43 adds no operation. Comparison is an audit relation among already declared reconstructions, not `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`.

```text
DECOMPOSE toward finer granularity
≠ finer wins

COMPOSE toward wider scope
≠ wider explains more

comparison of operation outputs
≠ fourth operation
≠ automatic route selection
```

Each candidate retains its own source, coordinates, operation status, Loss, alternatives, and disposition. The comparison cannot overwrite a prior operation result or transfer authority between candidates.


## Chapter 43 WP1 — Directional Non-Privilege across Operations

`DECOMPOSE` toward finer granularity and `COMPOSE` toward wider scope carry symmetrical burdens of warrant but retain distinct signatures and failure modes. Comparison is not a fourth operation and does not alter prior operation results.

```text
DECOMPOSE direction
≠ finer preferred

COMPOSE direction
≠ wider preferred
```

`PROJECT_AS` remains relevant only where a bounded target function is separately claimed; WP1 creates no projection result. Primary sites: [§§43.1–43.3](../01_blocks/05_part_iv_limits.md#43-1-symmetrical-limitation).

## Chapter 43 WP2 — Comparison, Co-Validity, and Non-Merger

Scale comparison is not a fourth operation. Multiple warranted reconstructions do not require `COMPOSE`; integration is a new transformation claim only where selection, order, constitutive relations, alternatives, and Loss are declared. `RC`, `RF`, and `RH` remain unadjudicated.

```text
co-valid reconstructions
≠ mandatory COMPOSE
```

Primary sites: [§43.5](../01_blocks/05_part_iv_limits.md#43-5-scale-relative-performance) and [§43.6](../01_blocks/05_part_iv_limits.md#43-6-coarse-and-fine-co-validity).


## Chapter 43 WP3 — Comparative View and Operation Separation

Comparison among coarse, fine, and wider candidates is not a fourth operation. A comparison view may reference existing `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` Records without merging them. Any actual new decomposition, composition, projection, or integration remains a new operation occurrence and requires its own Record.

```text
comparison view
≠ COMPOSE
≠ DECOMPOSE
≠ PROJECT_AS
≠ integrated-chain result
```

Primary sites: [§43.8](../01_blocks/05_part_iv_limits.md#43-8-comparative-granularity-test) and [§43.10](../01_blocks/05_part_iv_limits.md#43-10-limits-record-view-control).

## Chapter 43 Lock and Chapter 44 Operation Boundary

The three-operation inventory remains closed. Chapter 44 tests lower-bound PraxisPurchase for an operation occurrence or declared distinction; it does not create a fourth operation. A lower-bound finding remains distinct from operation identity and maps to a canonical Output Class only after all applicable checks.

```text
additional DECOMPOSE detail ≠ resolution gain automatically
additional COMPOSE scope ≠ greater relevance automatically
additional PROJECT_AS function language ≠ PraxisPurchase automatically
```


## Chapter 44 WP1 — Relevance-Floor Application across Operations

The Relevance Floor is not a fourth operation. It tests whether a declared `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` occurrence changes a warranted reconstruction for its claim. Each operation retains its own signature, Record, Loss, alternatives, and failure possibility.

```text
operation available
≠ added distinction relevant
```

Primary sites: [Chapter 44](../01_blocks/05_part_iv_limits.md#chapter-44-praxeological-relevance-floor) and [WP1 Execution Record](../_workfiles/chapter_preparation/Chapter_44_Preparation_Record.md#chapter-44-wp1-execution-record).

## Chapter 44 WP2 — Operation-Local Lower-Bound View

The Changed-Reconstruction Test applies to all three operations without changing their signatures:

```text
finer DECOMPOSE output
≠ automatic PraxisPurchase

larger COMPOSE inventory
≠ automatic PraxisPurchase

more elaborate PROJECT_AS description
≠ automatic PraxisPurchase
```

Each operation must identify the exact claim changed by the added distinction. A lower-bound view is a controlled view of the existing operation Record, not a fourth operation or second record grammar.
## Chapter 44 WP3 — Operation-Local Stop and Re-entry

The Relevance-Floor view applies to each operation occurrence or separately delimited handoff:

```text
supported operation detail + unchanged claim
→ possible resolution-neutral local finding

continued operation below the floor
→ Mandatory Lower Stop for that route

new source/question/Frame/granularity/reference/claim
→ new testable operation or comparison claim
```

The earlier operation disposition remains visible. Re-entry is not a fourth operation, and the Relevance-Floor view is not a second operation record.


## Chapter 44 lock and Chapter 45 operation handoff

Chapter 44 supplies the lower-bound method for all three operations. Chapter 45 is prepared to supply the upper-bound method: `COMPOSE` must preserve selection and relation load, `DECOMPOSE` must retain same-reference and source-function return, and `PROJECT_AS` must preserve origin reference, origin type, and constitutive source dependence. No operation receives a pass from availability, detail, breadth, or citation volume.

## Chapter 45 WP1 — Operation-local upper-bound burdens

- `COMPOSE` must retain selection, order, constitutive relation, heterogeneity, and declared Loss sufficient to reconstruct the composite from its sources.
- `DECOMPOSE` must return finer structures to the same reference object or disclose where fragmentation breaks that return.
- `PROJECT_AS` must preserve origin type and identify why source features support the bounded target function rather than merely resemble its label.

The Traceability Ceiling tests operation occurrences and handoffs. It is not a fourth operation and does not grant a chain-level pass from one locally traceable occurrence.

## Chapter 45 WP2 operation-specific upper-bound status

- `COMPOSE` requires selection, order, relation trace, compression, exclusion, and a target claim sensitive to load-bearing source-relation change.
- `DECOMPOSE` requires supported finer structure, same-reference continuity, source-function return, and a claim sensitive to load-bearing finer-relation change.
- `PROJECT_AS` requires preserved origin type, bounded target context, Constitutive Source Trace, and a target-function warrant sensitive to load-bearing source change.

These are variants of one Traceability Ceiling, not new operation signatures.

## Chapter 45 WP3 upper-bound closure

- `COMPOSE` may compress extensively while remaining traceable if selection, order, relation topology, heterogeneity, and five-part Loss remain reconstructible.
- `DECOMPOSE` requires return to the same reference object and coarser function; supported fragments without return path trigger upper-bound pressure.
- `PROJECT_AS` requires preserved origin type, bounded context, and a source-dependent target function; label stability across opposed sources without invariant triggers elasticity pressure.
- Mandatory Upper Stop ends the current unsupported route; Claim Reduction registers a narrower residual claim for retest.

No fourth operation is introduced.

## Chapter 45 lock and Chapter 46 operation handoff

Chapter 45 supplies complete source-trace and dependency burdens for all three operations. Chapter 46 is prepared to vary order, branch, event, or non-event for `COMPOSE`; component or relation for `DECOMPOSE`; and the declared source feature carrying a bounded target function for `PROJECT_AS`. These are test forms, not new operation signatures or empirical causal proofs.

## Chapter 46 WP1 — Shared counterfactual entry burden

Every `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` sensitivity test must begin with one declared operation occurrence, source baseline, load-bearing feature, bounded modification, expected target response, Claim Scope, and source basis. WP1 does not yet define the three operation-specific modification forms; that ownership remains WP2.

## Chapter 46 WP2 — Operation-specific Counterfactual Sensitivity forms

- `COMPOSE`: pressure declared selection, order, branch, event/non-event, or constitutive relation load.
- `DECOMPOSE`: pressure a component or relation while preserving the same reference object and source-function-return burden.
- `PROJECT_AS`: pressure the origin-side feature or relation declared to carry the bounded target function.

These are test forms, not operation redefinitions. See [§46.4](../01_blocks/05_part_iv_limits.md#46-4-operation-specific-tests).

## Chapter 46 WP3 — sensitivity completion without operation expansion

The three operation-specific variation forms remain unchanged. Source discipline, `untestable`, `underdetermined`, claim effects, and the Shared-Record view do not create a fourth operation or a second transformation grammar.

```text
Counterfactual Sensitivity view
≠ operation
≠ route selection
≠ Output Class
```

Primary sites: [§46.7](../01_blocks/05_part_iv_limits.md#46-7-counterfactual-source-discipline)–[§46.10](../01_blocks/05_part_iv_limits.md#46-10-shared-record-view-limits-and-handoff).

## Chapter 46 lock and Chapter 47 operation handoff

Chapter 47 will audit continuity separately across `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS`: composites do not rewrite component types, decomposition must retain the same reference object, and projection must preserve origin type while sustaining a bounded source-dependent target function. No new operation or unified binary continuity result is introduced.

## Chapter 47 WP1 — continuity declarations across operations

Every operation occurrence must keep Reference, Functional, and where relevant Temporal Continuity separately inspectable; typing remains a view under `TypeIntegrity`. WP1 operationalizes only Reference Continuity and Reference Discontinuity.

```text
DECOMPOSE detail retention
≠ same referent automatically

COMPOSE component inclusion
≠ component reference preserved automatically

PROJECT_AS name persistence
≠ origin referent preserved automatically
```

No operation result or chain result is selected for `N0/CR/CT/CF/CTM/CC`.

## Chapter 47 WP2 — operation-specific type and function burdens

| Operation | Type burden | Function burden |
|---|---|---|
| `COMPOSE` | retain component types; declare composite type separately | reconstruct any emergent composite function through constitutive relations |
| `DECOMPOSE` | open occurrences/composites, never operator types | return finer findings to the same source function where claimed |
| `PROJECT_AS` | retain origin type beside target function | keep the function source-dependent, contextual, and bounded |

These are continuity controls, not new operation signatures or automatic result routes.

## Chapter 47 WP3 — operation-specific temporal and matrix control

`COMPOSE` must preserve claim-bearing order and historical load; `DECOMPOSE` must retain the temporal identity of the same source object; `PROJECT_AS` must retain the temporal source relation carrying the bounded target function. The dimension-specific continuity matrix is a Shared-Record view, not a fourth operation, second grammar, score, or chain verdict.

## Chapter 47 WP4 and Chapter 48 Preparation — operation selection and Loss

Every `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS` occurrence is selective, but each retains its own signature. Chapter 48 will distinguish selected and omitted elements, preserved relations, compression, exclusion, uncertainty, and irrecoverability without adding a fourth operation, a sixth Loss field, or a second record grammar.

## Chapter 48 WP1 — operation-specific selection and first Loss fields

`COMPOSE` selects elements, order, periodization, relations, alternatives, and composite identity. `DECOMPOSE` selects finer differences, components, relations, thresholds, and the source-function return. `PROJECT_AS` selects foregrounded source features, target context, bounded function, and validity scope while retaining origin type. `preserved`, `compressed`, and `excluded` remain common Loss fields applied through each operation's existing signature, not new operations or schemas.

## Chapter 48 WP2 operation-selection additions

- `COMPOSE` must disclose selection of periods, paths, relation bundles, alternatives, and component-to-composite return paths; merging may create current-operation irrecoverability.
- `DECOMPOSE` must preserve the same reference object while selecting distinctions and thresholds; fragmentation may destroy Source-Function Return.
- `PROJECT_AS` must disclose selected source features, rival functions, target context, and validity scope; stable target wording cannot conceal uncertain or irrecoverable source-function dependence.

All three operations remain subject to one five-field Loss record and no new operation signature is created.

## Chapter 48 WP3 operation and Loss-disclosure additions

Every `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS` occurrence requires the same exact five-field Loss declaration while retaining operation-specific burdens. Compression Debt may reopen a later `SUB`, revise a `PATH` claim, or narrow a `RETYPE` projection, but no reopening is an inverse operation and no fourth operation is created. Hidden Loss must also be tested at operation handoffs where an intermediate result is treated as lossless.

## Chapter 48 WP4 and Chapter 49 operation-source preparation

Each `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS` occurrence must declare its source basis, direct support, inferred structure, missing structure, inferential distance, and applicable source/calibration limits. Operation signatures remain unchanged; Source Ceiling may constrain an operation claim but does not create a fourth operation or automatically select Non-Capture.

## Chapter 49 WP1 — operation-specific source burdens

`COMPOSE` requires source support for selected occurrences, ordering or branching, constitutive relations, and composite identity. `DECOMPOSE` requires support for finer components, their relations, and return to the same reference object. `PROJECT_AS` requires support for the origin object, load-bearing source feature, target context, and bounded source-function dependency. Formal detail cannot supply a missing operation-specific bridge.

## Chapter 49 WP2 — operation-relative calibration

`COMPOSE` comparisons require inspectable element selection, order, periodization, constitutive relations, and composite identity. `DECOMPOSE` comparisons require a stable reference object, declared resolution, component relations, and return path. `PROJECT_AS` comparisons require visible origin type, source feature, target context, bounded function, and a threshold-failing source modification.

## Chapter 49 WP3 — operation-relative Source Ceiling

`COMPOSE` may reach the Source Ceiling before a unique branch, path-dependence relation, or composite identity is warranted. `DECOMPOSE` may reach it before a component boundary or internal dependency is source-supported. `PROJECT_AS` may reach it before a constitutive source-function dependency is established. A local ceiling restricts only the unsupported continuation and does not automatically fail every bounded claim.

## Chapter 49 WP4 and Chapter 50 Preparation — successor-operation separation

A warranted `DECOMPOSE`, `COMPOSE`, or `PROJECT_AS` successor may be analytically useful while the original claim remains failed or reduced. Every successor operation must declare its own source object, coordinates, Loss, target claim, and test burden and retain a link to the original objection and disposition.

## Chapter 50 successor-operation control

A changed Frame, granularity, relative level, composition, source basis, operation occurrence, or target function creates a new testable reconstruction. `DECOMPOSE` must not become Granularity Escape; `COMPOSE` must not become Higher-Level Escape; `PROJECT_AS` must not become Projection Rescue. Every successor occurrence receives independent PraxisPurchase, TraceableLoad, TypeIntegrity, continuity, Loss, Claim Scope, and Claim Ceiling burdens.

## Chapter 51 operation-specific Stop control

`COMPOSE` stops where temporal or composite continuation becomes arbitrary, source-detached, or objection-moving. `DECOMPOSE` stops where finer structure loses PraxisPurchase, source support, or the same reference object. `PROJECT_AS` stops where target function is unnecessary, source-untraceable, type-overwriting, analogy-confused, or context-arbitrary. Re-entry requires a new or revised record and changed material condition.

## Chapter 52 operation-specific capture control

`COMPOSE` may reach compositional Non-Capture where no admissible composite preserves heterogeneity, alternatives, or Non-Events. `DECOMPOSE` may reach granularity Non-Capture only after relevant resolutions are tested. `PROJECT_AS` may reach projection Non-Capture only where no bounded target function passes PraxisPurchase, Source Trace, sensitivity, and TypeIntegrity. One failed operation never proves a general capture limit.

## Chapter 53 integrated chain control

Every operation occurrence in a chain retains its own record, justification, Loss, scope, local result, and failure possibility. A local success does not imply chain success, and a later operation cannot erase an earlier handoff failure. The integrated route connects records; it does not collapse them.

## Chapter 54 chain synthesis

Every operation occurrence in an integrated chain retains an independent record, source basis, justification, coordinates, five-field Loss profile, local result, Claim Ceiling, and failure possibility. Handoffs are separately testable continuity claims. `DECOMPOSE(COMPOSE(X))`, `COMPOSE(DECOMPOSE(X))`, and `PROJECT_AS(X)` are not identity returns.

## Chapter 55 operation-capability index

`COMPOSE` supports bounded temporal composition, `DECOMPOSE` supports finer reconstruction of the same reference object, and `PROJECT_AS` supports contextual target functions with retained origin type. These are methodological capabilities, not guarantees of passage. Stop, Failure, and Non-Capture remain available for every operation and chain.

## Chapter 56 operation exclusions

`COMPOSE` does not create ultimate totality or higher-level privilege; `DECOMPOSE` does not discover final constituents or finer-resolution truth priority; `PROJECT_AS` does not automatically retype origins or operate losslessly. Further operation availability does not create a duty to continue.

## Chapter 57 terminal transformation rule

Every bounded transformation must identify its source object; declare frame, granularity, and relative level; specify exactly `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS`; state expected praxis difference; retain constitutive Source Trace; preserve reference and TypeIntegrity; disclose Selection and five-field Loss; permit counterfactual failure; bound validity scope; and preserve Stop and Non-Capture. The ten conditions are conjunctive and non-compensatory.



## RETYPE Lock Package 1 synchronization

Registers `project-as.c40-p1.01` as one lock-critical positive PROJECT_AS occurrence linked to prior COMPOSE record `case.c17-lambda-01.compose.01`.

## RETYPE Lock Package 2 synchronization

Registers `project-as.c40-n3.01` as a failed `PROJECT_AS` occurrence linked to prior `COMPOSE` record `case.c17-linear-01.compose.01`. The occurrence demonstrates that operation declaration, target vocabulary, bounded context, and preserved origin type are insufficient without constitutive source-function dependence.

## RETYPE Lock Package 3 synchronization

Registers `project-as.c40-x6.01` as an attempted `PROJECT_AS` boundary occurrence linked to `case.c17-lambda-01.compose.01`. The retained result is `analogy_only`; no fourth operation is created. A future functional projection requires a new `PROJECT_AS` occurrence.

## Appendix B Formal-Notation Handoff

[`Appendix B — Formal Notation`](../02_appendices/Appendix_B_Formal_Notation.md) now consolidates the display syntax for `T_i`, operation kinds, source/target coordinates, the three canonical signatures, handoffs, chains, local results, canonical classes, and inherited Loss. Operation identity and occurrence burdens remain owned by the Minified signatures, canonical prose, Operation Registry, and Transformation Record Schema.
