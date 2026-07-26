# PMS-STRATA — Operation Signatures Minified

**Status:** canonical control artifact for corpus production  
**Dependency:** `PMS_STRATA_Claim_Boundary_Minified.md`, PMS Base as represented by `PMS.yaml`, and the current `PMS-STRATA_Structure.md`  
**Function:** compact specification of the three canonical STRATA operations, their inputs, outputs, preservation duties, losses, admissibility requirements, and failure modes

---

## 1. Governing Rule

PMS-STRATA contains exactly three canonical transformation operations:

```text
COMPOSE
DECOMPOSE
PROJECT_AS
```

They answer different questions and produce different kinds of results:

```text
COMPOSE
How may multiple or sequential source structures form a declared composite object?

DECOMPOSE
How may a provisionally compressed occurrence or composite be reconstructed under finer granularity?

PROJECT_AS
What bounded function may an origin-typed object perform within a declared target context?
```

The availability of an operation does not establish its admissibility.

Every operation must remain:

- frame-declared;
- granularity-declared;
- relative-level-declared;
- source-supported;
- claim-bounded;
- loss-aware;
- counterfactually criticizable;
- stoppable;
- open to failure and non-capture;
- without authority inheritance.

No operation changes PMS Base, adds a primitive, or raises the authority of a claim.

---

## 2. Shared Operation Envelope

Every STRATA operation requires a common minimum envelope.

```yaml
source:
  object:
  operator_typing:
  frame:
  granularity:
  relative_level:
  temporal_scope:
  source_basis:

operation:
  kind: COMPOSE | DECOMPOSE | PROJECT_AS
  justification:
  expected_praxeological_difference:
  transformation_context:

target:
  object:
  contextual_function:
  frame:
  granularity:
  relative_level:
  validity_scope:

claim:
  claim_type:
  claim_scope:
  claim_ceiling:

loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:

admissibility:
  relevance_floor_result:
  constitutive_source_trace:
  counterfactual_sensitivity:
  traceability_ceiling_result:
  type_integrity:
  contextual_boundedness:
  result:

alternatives:
  rival_transformations:
  no_transformation_option:
  non_translation:

stop:
  condition:
  reached:
  non_capture_status:

governance:
  authority_inheritance: prohibited
```

The operation-specific records may extend this envelope. They may not remove its governing requirements.

### 2.1 Shared notation

The following notation is compact and relational rather than ontological:

```text
X       source object
S       declared set or sequence of source objects
T_o     origin type
K_c     declared composite object class
F_s     source or coarser function under examination
F_t     contextual target function
Fr_s    source frame
Fr_t    target frame
C_t     declared target or transformation context
g_s     source granularity
g_t     target granularity
ℓ_s     source relative level
ℓ_t     target relative level
τ       temporal scope
J       transformation justification
L       declared loss profile
V       validity scope
R       relevant ordering or relation structure
```

Formulas in this file are specifications of analytical commitments, not empirical laws or claims of mathematical completeness.

---

## 3. Operation Identity Matrix

| Operation | Primary movement | Reference logic | Primary output | Must not be confused with |
|---|---|---|---|---|
| `COMPOSE` | many or sequential → composite | creates a new analytical composite while preserving source trace | sequence, path, trajectory, or other declared composite | chronology, aggregation, projection |
| `DECOMPOSE` | compressed → finer reconstruction | preserves the source object as the reconstruction target while opening internal structure | components, relations, internal temporality, revised source-function status | description, atomization, operator decomposition, new PATH |
| `PROJECT_AS` | origin-typed object → contextual function | preserves source reference and origin type while adding a bounded target function | contextual functional relation | recontextualization, analogy, renaming, origin-type replacement |

Canonical non-equivalences:

```text
COMPOSE
≠
PROJECT_AS
```

```text
DECOMPOSE
≠
PROJECT_AS
```

```text
changed frame
≠
changed granularity
≠
changed relative level
```

```text
new analytical object
≠
new PMS primitive
```

---

## 4. COMPOSE

### 4.1 Canonical definition

`COMPOSE` forms a declared composite analytical object from multiple temporally or structurally related source objects while making selection, ordering, formation, compression, and loss explicit.

```text
many / sequential source structures
→
composite analytical object
```

#### Minimal signature

```text
COMPOSE:
(S, Fr_s, g_s, ℓ_s, τ, R, J)
→
(X_c, K_c, Fr_t, g_t, ℓ_t, L, V)
```

Where:

- `S` is the declared source set or sequence;
- `R` is the ordering and relation structure;
- `X_c` is the resulting composite object;
- `K_c` is its declared analytical object class;
- `L` records preservation, compression, exclusion, uncertainty, and irrecoverable loss;
- `V` limits the result to its warranted validity scope.

Typical target object classes include:

```text
sequence
path
trajectory
event cluster
branch structure
phase
other explicitly declared composite
```

A target function such as `frame-function`, `macro-event function`, or `attractor-function` is not produced by `COMPOSE` alone. Such a claim requires a separate `PROJECT_AS` operation.

### 4.2 Valid source objects

`COMPOSE` may operate on declared relations among:

- configurations;
- transitions;
- events;
- non-events;
- subpaths;
- branch structures;
- partial trajectories;
- operator-typed occurrences;
- composite structures.

A source list alone is insufficient. The relation that makes the elements composable must be stated.

### 4.3 Preconditions

A `COMPOSE` operation requires:

1. identifiable source objects;
2. a declared source frame;
3. a declared temporal scope where temporality is relevant;
4. a warranted temporal or structural ordering;
5. an explicit selection rule;
6. an explicit formation rule;
7. sufficient source support;
8. an expected praxeological difference;
9. a possible loss account;
10. a bounded composition claim.

### 4.4 Constitutive decisions

#### Selection rule

The record must state:

- why included elements are included;
- why omitted elements are omitted;
- which elements are load-bearing;
- which elements are illustrative;
- where selection remains contested.

#### Ordering rule

Permitted ordering forms may include:

- linear order;
- partial order;
- overlapping transitions;
- parallel subpaths;
- uncertain order;
- explicitly retrospective periodization.

#### Formation rule

The formation rule must explain why the result is more than a collection or chronology.

It must identify the relations through which the source structures become:

- a sequence rather than a list;
- a path rather than a chronology;
- a trajectory rather than a path;
- or another declared composite rather than an aggregation.

### 4.5 Preservation duty

`COMPOSE` must preserve, where constitutive to the claim:

- source trace;
- relevant temporal order;
- load-bearing transitions;
- central events and non-events;
- historically relevant asymmetries;
- binding structures;
- branch points and lost alternatives;
- internal heterogeneity necessary to the claim;
- the distinction between source types and the new composite object.

Preservation does not mean total retention. It means that the target claim remains reconstructibly dependent on its source structures.

### 4.6 Loss duty

Every composition must classify:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

Typical composition losses include:

- local detail;
- internal variation;
- parallel minor paths;
- fine temporal resolution;
- separability of local costs;
- historical alternatives no longer recoverable from the composite alone.

No composition is presumed lossless.

### 4.7 Counterfactual sensitivity

Central test:

> Would removing or materially changing a load-bearing source element alter the composite object or its warranted claim?

Possible results:

```text
strongly_sensitive
partially_sensitive
weakly_sensitive
insensitive
underdetermined
untestable
```

A composite that remains unchanged under arbitrarily large source changes risks exceeding the Praxeological Traceability Ceiling.

### 4.8 Valid COMPOSE outputs

Possible outputs include:

- admissible sequence;
- admissible path;
- admissible trajectory;
- admissible declared composite;
- provisional composition;
- competing compositions;
- reduced composition claim;
- failed composition;
- mandatory stop;
- non-capture.

### 4.9 Central failure modes

`COMPOSE` fails or requires reduction when:

- chronology is presented as path;
- aggregation is presented as functional formation;
- no load-bearing relation connects the source objects;
- selection is narratively convenient but not source-supported;
- ordering is imposed retroactively without disclosure;
- teleology determines the source selection;
- relevant non-events, asymmetries, or alternatives disappear;
- compression destroys constitutive heterogeneity;
- the source path is no longer reconstructible;
- the target label remains insensitive to material source changes;
- the composite creates no additional praxeological discrimination;
- a target function is asserted without a separate `PROJECT_AS` record.

### 4.10 Minimal COMPOSE record

```yaml
compose:
  source_objects:
  source_typings:
  source_frame:
  source_granularity:
  source_level:
  temporal_scope:
  ordering_rule:
  selection_rule:
  formation_rule:
  constitutive_relations:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
  target_object:
  target_object_class:
  target_granularity:
  target_level:
  expected_praxeological_difference:
  counterfactual_sensitivity:
  claim_scope:
  stop_condition:
  admissibility_result:
```

### 4.11 COMPOSE completion test

A `COMPOSE` record is not complete unless all answers are explicit:

```text
What is being composed?
Why may these sources be related?
What ordering is used?
What selection is used?
What new composite object is formed?
What remains traceable?
What is lost?
What source change would alter the result?
What claim is licensed?
What target-function claim is not yet licensed?
When must composition stop?
```

---

## 5. DECOMPOSE

### 5.1 Canonical definition

`DECOMPOSE` reconstructs a provisionally compressed operator occurrence or composite as a relational organization of finer structures under declared granularity.

```text
provisionally compressed object
→
finer relational reconstruction
```

#### Minimal signature

```text
DECOMPOSE:
(X, T_o, F_s, Fr_s, g_s, ℓ_s, Q_d, J)
→
(K, R_K, F_s', Fr_t, g_t, ℓ_t, L, V)
```

Where:

- `X` is the identifiable source object;
- `T_o` is its origin type;
- `F_s` is the source or coarser function under examination;
- `Q_d` is the decomposition question;
- `K` is the set of reconstructed finer components;
- `R_K` is their relation and internal temporal structure;
- `F_s'` is the post-decomposition status of the source function;
- `g_t` is a declared finer granularity relative to `g_s`;
- `L` records what remains unavailable or is lost in reconstruction.

The source function may be:

```text
confirmed
refined
internally differentiated
partially preserved
rejected
underdetermined
```

The preservation requirement does not immunize the coarser function. It preserves the source object as a testable reconstruction target.

### 5.2 Valid source objects

`DECOMPOSE` may operate on:

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
- other declared composite structures.

`DECOMPOSE` does not operate on Δ–Ψ operator types as though they were empirical material composites.

```text
operator type
≠
decomposable occurrence
```

### 5.3 Preconditions

A `DECOMPOSE` operation requires:

1. an identifiable source object;
2. a visible origin type;
3. a declared source frame and granularity;
4. a precise decomposition question;
5. a reason why the current compression may be insufficient;
6. an expected additional praxeological difference;
7. a declared finer target granularity;
8. sufficient source support;
9. a criterion for retaining reference to the source object;
10. a test for the coarser function;
11. an explicit stop condition.

### 5.4 Component-and-relation duty

A valid decomposition must identify both:

```text
components
+
relations among components
```

Possible finer structures include:

- operator-typed occurrences;
- local configurations;
- subevents;
- non-events;
- transitions;
- roles;
- resource and access relations;
- subpaths;
- repeated reproduction practices;
- thresholds and feedbacks.

A parts list without relations is fragmentation, not decomposition.

### 5.5 Preservation duty

`DECOMPOSE` must preserve or explicitly test:

- source reference;
- origin type visibility;
- source frame or a marked frame transition;
- relation between source and finer reconstruction;
- relevant internal temporality;
- the coarser function as an object of evaluation;
- uncertainty and inaccessible internal structure.

The source object must remain reconstructible as the object being opened, even where its prior function is revised or rejected.

### 5.6 Granularity duty

A valid decomposition must state:

```yaml
granularity_change:
  source_granularity:
  target_granularity:
  distinctions_added:
  frame_preserved:
  reference_preserved:
  expected_praxeological_difference:
  comparability_status:
```

Finer granularity does not imply:

- deeper truth;
- ontological depth;
- greater authority;
- automatic explanatory superiority;
- final constituents.

### 5.7 Relevance and source tests

#### Resolution-gain test

> Which warranted reconstruction or claim changes because of the added distinctions?

Possible results:

```text
resolution gain
resolution neutral
resolution drift
resolution escape
unsupported
non-capture
```

#### Counterfactual component test

> Would changing or removing this component alter the reconstructed source function?

Possible component statuses:

```text
constitutive
strongly modulating
weakly modulating
replaceable
incidental
underdetermined
```

#### Source-ceiling test

The semantic precision of the finer reconstruction must not exceed the precision supported by the source basis.

### 5.8 Valid DECOMPOSE outputs

Possible outputs include:

- admissible decomposition;
- source function confirmed;
- source function refined;
- source function internally differentiated;
- source function partially preserved;
- source function rejected;
- source function underdetermined;
- heterogeneous source object;
- competing internal models;
- resolution-neutral result;
- unsupported decomposition;
- resolution drift;
- mandatory stop;
- non-capture.

Operation admissibility and source-function effect remain separate. A valid `DECOMPOSE` occurrence may reject the prior source function while the operation itself remains admissible; the prior source claim is then separately recorded as failed, withdrawn, or reduced.

### 5.9 Central failure modes

`DECOMPOSE` fails or requires reduction when:

- a base operator type is treated as a material composite;
- no identifiable source object exists;
- finer details are listed without relations;
- a changed description is presented as a granularity change;
- the source object disappears into fragments;
- the coarser function can no longer be evaluated;
- internal precision exceeds source support;
- additional detail creates no praxeological purchase;
- resolution drift increases complexity without discrimination;
- resolution escape moves an unresolved objection to an ever-finer level;
- a competing path composition is misclassified as decomposition;
- a new contextual function is asserted without a separate `PROJECT_AS` record.

### 5.10 Minimal DECOMPOSE record

```yaml
decompose:
  source_object:
  origin_type:
  source_function:
  source_frame:
  source_granularity:
  source_level:
  temporal_scope:
  decomposition_question:
  insufficiency_of_current_compression:
  expected_difference:
  target_granularity:
  components:
  component_relations:
  internal_temporality:
  source_support:
  source_reference_preserved:
  source_function_result:
  unresolved_structure:
  loss:
  counterfactual_component_test:
  claim_scope:
  stop_condition:
  admissibility_result:
```

### 5.11 DECOMPOSE completion test

A `DECOMPOSE` record is not complete unless all answers are explicit:

```text
What source object is being opened?
Is it an occurrence or composite rather than a base operator type?
Why is the current compression insufficient?
What finer granularity is declared?
Which components are reconstructed?
Which relations make them functionally relevant?
What happens to the coarser function?
What source evidence supports the added detail?
What distinction changes the warranted reconstruction?
When does added resolution become neutral, drifting, or unsupported?
When must decomposition stop?
```

---

## 6. PROJECT_AS

### 6.1 Canonical definition

`PROJECT_AS` projects an origin-typed source object as a bounded function within a declared target context while preserving source reference and origin type.

```text
origin-typed source object
→
contextual target function
```

#### Canonical minimal signature

```text
PROJECT_AS:
(X_g, T_o, C_t)
→
(F_t, g', J, L, V)
```

Expanded relational form:

```text
PROJECT_AS:
(X, T_o, Fr_s, g_s, ℓ_s, C_t, Fr_t, g_t, ℓ_t, J)
→
(X PROJECT_AS F_t, L, V)
```

Where:

- `X` remains the source object;
- `T_o` remains its origin type;
- `C_t` is the declared target context;
- `F_t` is the bounded target function;
- `L` records foregrounding, backgrounding, compression, exclusion, uncertainty, and irrecoverable loss;
- `V` limits the function's validity.

Canonical rule:

```text
same source reference
+
preserved origin type
+
new bounded contextual function
=
admissible projection candidate
```

Not:

```text
new contextual function
=
new origin type
```

### 6.2 Valid source objects

`PROJECT_AS` may operate on an already identified PMS or STRATA object, including:

- operator-typed occurrence;
- configuration;
- event or non-event structure;
- path;
- trajectory;
- recurrent trajectory form;
- phase;
- composite structure;
- operator-weighting or modulating profile.

The source object must already possess an independent source-side reconstruction. Projection cannot substitute for constructing or identifying the source object.

### 6.3 Valid target functions

Possible bounded target functions include:

- frame-function;
- macro-event function;
- attractor-function;
- asymmetry-function;
- binding-function;
- integration-function;
- modulating function;
- higher-level boundary function;
- other explicitly justified derived functions.

These functions are contextual and derived. They are not new Δ–Ψ primitives.

### 6.4 Preconditions

A `PROJECT_AS` operation requires:

1. an identifiable source object;
2. a determined origin type;
3. a declared source frame, granularity, and relative level;
4. a declared target context;
5. a declared target granularity and relative level;
6. a precisely named target function;
7. an expected additional praxeological difference;
8. a constitutive source trace;
9. counterfactual sensitivity;
10. a bounded validity scope;
11. an explicit loss account;
12. at least one relevant alternative, including no projection;
13. a stop condition.

### 6.5 Source-trace duty

The projection must distinguish:

```yaml
constitutive_source_trace:
  load_bearing_features:
  modulating_features:
  foregrounded_features:
  backgrounded_features:
  compressed_features:
  excluded_features:
  uncertain_features:
```

The target function must depend on specific source-side structures rather than on resemblance or terminology alone.

### 6.6 Type-integrity duty

`PROJECT_AS` must preserve:

- source reference;
- origin type;
- relevant historical continuity;
- load-bearing relations;
- the distinction between source level and target level;
- the distinction between origin type and target function;
- the possibility that the projection fails while the source object remains valid.

Canonical non-equivalences:

```text
trajectory
PROJECT_AS
frame-function

≠

trajectory becomes frame as origin type
```

```text
functions as Α
≠
is Α as a new primitive
```

```text
contextual function
≠
person-level property
```

### 6.7 Contextual-boundedness duty

The target function must be bounded by:

- target object or scene;
- target frame;
- temporal scope;
- relative target level;
- affected roles or structures;
- praxeological dimensions;
- validity duration;
- transfer limits;
- claim ceiling.

A locally warranted function does not automatically apply to all later scenes, all members of a group, or all comparable objects.

### 6.8 Counterfactual sensitivity

Central test:

> Would a relevant change in the load-bearing source structure alter, weaken, or defeat the target function?

Possible results:

```text
strongly_sensitive
partially_sensitive
weakly_sensitive
insensitive
underdetermined
untestable
```

A projection that survives contradictory source structures without changing risks becoming label substitution or abstraction without traceable load.

### 6.9 Projection loss

Every projection must disclose:

```yaml
loss:
  preserved:
  foregrounded:
  backgrounded:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

Projection changes analytical visibility even when source reference and origin type are preserved.


### 6.9A Conditional PMS occurrence anchoring

Where `PROJECT_AS` materially depends on PMS operator-typed occurrences or relations, the existing source reference, source basis, Constitutive Source Trace, Counterfactual Sensitivity, and canonical Loss fields must preserve an inspectable route from the warranted occurrence relation to the bounded target-function claim.

```text
operator label
≠ occurrence-level Source Trace

material occurrence variation
≠ abstract operator revision
```

This requirement is conditional and claim-relevant. It does not require a full Δ–Ψ inventory, introduce a new Record field, change dependencies, or permit source typing to be inferred from target fit.

### 6.10 Valid PROJECT_AS outputs

Possible outputs include:

- admissible functional projection;
- admissible narrow projection;
- compatible multiple projections;
- competing projections;
- provisional projection;
- context-dependent projection;
- analogy only;
- label substitution;
- invalid type jump;
- unmarked level mixing;
- mandatory claim reduction;
- mandatory stop;
- non-capture.

`analogy only` is a legitimate bounded result. It records useful similarity without asserting a valid functional projection.

### 6.11 Central failure modes

`PROJECT_AS` fails or requires reduction when:

- no target context is declared;
- the target function is merely a new name;
- the origin type is replaced by the target function;
- source and target levels are unmarked or mixed;
- source trace is absent;
- the projection is insensitive to material source changes;
- a structural analogy is presented as semantic identity;
- formal mapping or executable translation is treated as proof of praxeological preservation;
- a local function is globalized;
- a macrofunction is attributed directly to a person or group essence;
- historical development is flattened into a timeless type;
- a failed source claim is rescued by moving it to another level;
- the projected function becomes a hidden new primitive;
- the projection creates no additional praxeological discrimination.

### 6.12 Minimal PROJECT_AS record

```yaml
project_as:
  source_object:
  origin_type:
  source_frame:
  source_granularity:
  source_level:
  temporal_scope:
  target_context:
  target_object:
  target_function:
  target_frame:
  target_granularity:
  target_level:
  justification:
  expected_praxeological_difference:
  constitutive_source_trace:
  counterfactual_sensitivity:
  source_reference_preserved:
  origin_type_preserved:
  target_function_bounded:
  validity_scope:
  loss:
  alternatives:
  claim_scope:
  stop_condition:
  admissibility_result:
```

### 6.13 PROJECT_AS completion test

A `PROJECT_AS` record is not complete unless all answers are explicit:

```text
What is the independently identified source object?
What is its origin type?
Within what target context is a function claimed?
What exactly is the target function?
Which source features carry that function?
What source change would alter or defeat it?
What remains preserved and what is backgrounded or lost?
How far does the function apply?
What rival projection or no-projection option exists?
Why is this more than recontextualization, analogy, or renaming?
When must projection stop?
```

---

## 7. Operation Classification Gate

Before any STRATA transformation is recorded, classify the analytical movement.

### 7.1 Primary decision sequence

```text
1. Are multiple or sequential source structures being formed into a new composite object?
   → COMPOSE candidate

2. Is an identifiable compressed occurrence or composite being opened under finer granularity while remaining the reconstruction target?
   → DECOMPOSE candidate

3. Is an independently identified origin-typed object being assigned a bounded function within a declared target context?
   → PROJECT_AS candidate

4. Has only the frame, vocabulary, or point of view changed without a new composite, finer reconstruction, or target function?
   → no STRATA transformation yet; possible recontextualization

5. Is only a formal or structural resemblance being asserted?
   → analogy candidate

6. Has only a PMS label been attached without source-dependent discriminative gain?
   → label substitution candidate
```

### 7.2 Boundary tests

#### COMPOSE or chronology?

```text
ordered items only
→ chronology or sequence

ordered transitions with source-supported structural connection and altered action possibilities
→ path candidate

path with sedimentation and historically altered continuation possibilities
→ trajectory candidate
```

#### DECOMPOSE or description?

```text
more words about the same object
≠
finer relational reconstruction
```

`DECOMPOSE` requires added distinctions, component relations, and a declared change in granularity.

#### DECOMPOSE or new PATH?

```text
opening the same path object
→ DECOMPOSE

selecting and forming a different path object
→ new COMPOSE
```

#### DECOMPOSE or PROJECT_AS?

```text
internal constitution or reproduction of the source object
→ DECOMPOSE

bounded function of the source object in a target context
→ PROJECT_AS
```

A case may require both, but each requires a separate record.

#### PROJECT_AS or recontextualization?

```text
new frame or reading only
→ recontextualization

explicit target function with source trace and bounded validity
→ PROJECT_AS candidate
```

#### PROJECT_AS or analogy?

```text
similar form without established semantic and praxeological continuity
→ analogy

source-dependent bounded function in a declared target context
→ PROJECT_AS candidate
```

#### Projection or label substitution?

```text
new terminology without changed reconstruction
→ label substitution

new discriminative target function sensitive to source changes
→ projection candidate
```

---

## 8. Operation Chains

STRATA permits operation chains, including:

```text
COMPOSE → PROJECT_AS
COMPOSE → DECOMPOSE
DECOMPOSE → COMPOSE
DECOMPOSE → PROJECT_AS
PROJECT_AS → DECOMPOSE
COMPOSE → PROJECT_AS → DECOMPOSE
```

Every link in a chain must:

- be independently classified;
- possess its own source and target declaration;
- possess its own justification;
- possess its own loss profile;
- possess its own admissibility result;
- remain independently falsifiable or stoppable;
- preserve prior failures and countercases;
- avoid inheriting authority from earlier or later operations.

A later operation does not retroactively validate an earlier one.

```text
admissible PROJECT_AS
≠
proof that prior COMPOSE was admissible
```

```text
successful DECOMPOSE
≠
rescue of a failed projection
```

```text
more operations
≠
stronger claim
```

---

## 9. Non-Invertibility

The three operations are not symmetric and are not presumed reversible.

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

Reasons include:

- selection and exclusion;
- compression and foregrounding;
- irrecoverable source loss;
- new evidence at finer granularity;
- changed reconstruction questions;
- competing periodizations;
- contextual validity of projected functions.

A reverse movement is a new operation with a new record, not restoration of an untouched original.

---

## 10. Common Admissibility Gate

Every operation must pass the common STRATA rule:

```text
Admissible(T, X, C)
iff
PraxisPurchase
and TraceableLoad
and TypeIntegrity
and ContextualBoundedness
```

Operation-specific emphasis:

```text
COMPOSE
→ ordering, selection, formation, source-path trace

DECOMPOSE
→ added distinction, source support, relation preservation, coarser-function test

PROJECT_AS
→ origin-type preservation, constitutive source trace, target-context boundedness
```

A complete operation assessment must also include:

- reference continuity;
- counterfactual sensitivity;
- loss declaration;
- source ceiling;
- calibration limits;
- alternatives;
- anti-immunization;
- claim ceiling;
- stop;
- non-capture.

---

## 11. Stop, Failure, and Non-Capture

### 11.1 Mandatory stop

An operation must stop where:

- no additional praxeological difference is produced;
- sources no longer support the claimed precision;
- source trace is lost;
- type integrity cannot be maintained;
- target context becomes arbitrary;
- the source object disappears;
- further transformation only repeats a label;
- a counterexample is merely displaced to another level;
- the operation becomes immune to relevant source changes.

### 11.2 Failure

Failure is an explicit result where the attempted operation does not satisfy its own signature or admissibility conditions.

Failure of one operation does not invalidate all source reconstruction and does not authorize a substitute operation without a new claim and record.

### 11.3 Claim reduction

Claim reduction is required where a narrower result remains supported but the original target claim exceeds the operation's evidence, traceability, type integrity, or validity scope.

### 11.4 Non-capture

Non-capture is appropriate where:

- no stable operation classification is warranted;
- the source structure remains only partially reconstructible;
- competing compositions, decompositions, or projections remain equally viable;
- every available operation destroys a constitutive part of the source;
- the structure is better represented outside the present STRATA grammar.

Non-capture is not analytical defeat. It is preservation of a justified limit.

---

## 12. Authority and Use Boundary

No operation licenses:

- person-level essence claims;
- diagnosis;
- personality typing;
- forensic or legal judgment;
- moral ranking;
- irreversible labeling;
- policy enforcement;
- automatic causal attribution;
- automatic normative authority.

Canonical rule:

```text
operation success
=
increased analytical legibility under a bounded claim
```

Not:

```text
operation success
=
more truth, higher rank, or greater authority
```

Technical validation may show that a record conforms to a schema. It does not prove empirical truth, causal adequacy, semantic preservation, or normative legitimacy.

---

## 13. Canonical Compact Forms

### COMPOSE

```text
COMPOSE
=
source plurality or sequence
+
ordering
+
selection
+
formation
+
traceable composite
+
declared loss
```

### DECOMPOSE

```text
DECOMPOSE
=
identifiable compressed source object
+
declared finer granularity
+
components
+
relations
+
coarser-function test
+
source-bounded stop
```

### PROJECT_AS

```text
PROJECT_AS
=
preserved source reference
+
preserved origin type
+
declared target context
+
bounded target function
+
constitutive source trace
+
counterfactual sensitivity
```

### Common negative rule

```text
available transformation
≠
admissible transformation
```

### Common authority rule

```text
more structure
≠
more authority
```

---

## 14. Final Operation Audit

Before accepting any operation, verify:

```text
[ ] The operation is classified as COMPOSE, DECOMPOSE, or PROJECT_AS.
[ ] No two operations are silently collapsed.
[ ] Source object, frame, granularity, relative level, and claim scope are declared.
[ ] The expected praxeological difference is explicit.
[ ] The result differs from chronology, description, recontextualization, analogy, or renaming where relevant.
[ ] Source trace remains inspectable.
[ ] Reference continuity is appropriate to the operation.
[ ] Origin type remains visible and is not replaced by a target function.
[ ] Selection and loss are declared.
[ ] A relevant source change would affect the result where it should.
[ ] The Relevance Floor is not undercut.
[ ] The Traceability Ceiling is not exceeded.
[ ] Alternatives, including no operation, are considered.
[ ] A stop condition is explicit.
[ ] Failure, claim reduction, and non-capture remain possible.
[ ] No analytical, normative, institutional, or person-level authority is inherited.
```

A STRATA operation is complete only when its transformation, boundaries, losses, possible failure, and stopping point are all legible.