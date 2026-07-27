# PMS-STRATA — Chapter Contracts

**Status:** Gate 2 complete, accepted chapter contract set — production round 4 of 4  
**Completed scope:** Chapters 0–57 plus Front Matter — all chapter and orientation contracts  
**Target corpus blocks:** `01_blocks/00_front_matter.md` through `01_blocks/06_conclusion.md`  
**Governing authority basis:** `PMS.yaml`, `00_source/PMS-STRATA_Structure.md`, the completed Gate 1 minified kernel, and `05_minified/Block_Contracts.md`  
**Status and navigation input:** `README.md`

---

## 1. Contract Function

These contracts constrain chapter production. They are not chapter summaries and do not substitute for the later prose.

A chapter is complete only when it has produced its assigned claim and distinctions, preserved its dependencies and non-claims, survived the required counterpressure, respected the redundancy guard, supported its model and appendix handoffs, and passed its completion test.

The governing rule is:

```text
Each concept is defined once,
operationalized locally,
tested repeatedly,
and never re-derived without necessity.
```

For Foundations this means:

```text
Chapter 0  → claim and authority boundary
Chapter 1  → object model
Chapter 2  → analytical coordinates
Chapter 3  → temporal object chain
Chapter 4  → operation grammar
Chapter 5  → type, function, context, and continuity
Chapter 6  → admissibility band
Chapter 7  → shared record
Chapter 8  → non-equivalence audit layer
```

No chapter may obtain authority from its position, length, level of formalization, or model relation.

---

## 2. Round 1 Global Rules

1. PMS Base remains the sole source of the Δ–Ψ operator grammar and dependencies.
2. No Foundation chapter may introduce a new operator, primitive, fixed stratum, universal scale, person type, or application authority.
3. Definitions belong to one primary chapter and are only referenced or operationalized elsewhere.
4. `frame`, `granularity`, `relative level`, and `transformation context` remain distinct.
5. `operator type`, `operator occurrence`, `composite structure`, and `derived analytical object` remain distinct.
6. `configuration`, `event`, `non-event`, `transition`, `sequence`, `path`, `trajectory`, and `path dependence` remain distinct.
7. `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS` remain the only core operations.
8. `origin type` and `target function` never collapse.
9. The Admissibility Band is non-compensatory and non-numeric.
10. Formal records and schemas may check declarations and consistency, not truth, causality, semantic adequacy, or normative validity.
11. Claim Reduction, Mandatory Stop, Failure, and Non-Capture remain available throughout.
12. Add-on lenses are absent from the Foundations architecture except as later optional stress vectors.

---

## 3. Canonical Chapter Contract Schema

```yaml
chapter:
  number:
  title:
  role_in_work:
  governing_question:
  required_claim:
  required_distinctions:
  dependencies:
  must_not_claim:
  required_example:
  required_counterpressure:
  redundancy_guard:
  model_relation:
  appendix_migration:
  completion_test:
```

The YAML blocks below are the actual contracts.

---

## 4. Chapter 0 — Position and Claim Boundary

```yaml
chapter:
  number: '0'
  title: Position and Claim Boundary
  role_in_work:
    primary_function: Establish why PMS-STRATA is required, what kind of discipline it is, and the maximum claim it
      may make.
    canonical_status: Primary definition site for the positive scope, negative scope, No Meta-PMS rule, No Ontology
      of Layers rule, and initial governing claim.
    handoff: Authorizes Chapters 1–8 to define a bounded transformation grammar without granting them additional theoretical
      or application authority.
  governing_question: Why does PMS require an explicit vertical transformation discipline, and how can that discipline
    be introduced without becoming a superior PMS layer, an ontology of strata, or a mechanism for escaping failure?
  required_claim:
    governing_claim: PMS-STRATA specifies how praxis structures may be composed, decomposed, and functionally projected across declared granularities and relative levels—while preserving source traceability, origin-type integrity, transformation loss, claim boundaries, stop, and non-capture. It does not turn analytical recursion into ontological totality, greater authority, or immunity from failure.
    required_subclaims:
    - STRATA specifies transformations between declared analytical positions; it does not generate independent domain
      findings.
    - STRATA depends on PMS Base and cannot revise the Δ–Ψ grammar or its canonical dependencies.
    - Relative levels and granularities are analytical relations and resolutions, not ontological layers.
    - Analytical recursion does not create meta-authority, practical authority, or immunity from counterexamples.
    - More structure is not more authority.
  required_distinctions:
  - bounded transformation discipline versus new theory layer
  - methodological specification versus domain finding
  - analytical relative level versus ontological layer
  - additional legibility versus additional authority
  - recursive availability versus recursive necessity
  - claim boundary versus later admissibility test
  dependencies:
    hard:
    - PMS.yaml
    - 00_source/PMS-STRATA_Structure.md
    - PMS_STRATA_Claim_Boundary_Minified.md
    - PMS_STRATA_Minified_Canonical.md
    status_and_navigation_alignment:
    - README.md
    inherited_constraints:
    - No new PMS base operator.
    - No changed Δ–Ψ dependency.
    - No person-level typing.
    - No automatic normative or application authority.
    - Stop and Non-Capture remain legitimate outputs.
  must_not_claim:
  - STRATA is a meta-PMS, superior PMS layer, or external tribunal over PMS Base.
  - Reality is composed of objectively discrete micro, meso, macro, or other strata.
  - STRATA proves recursive completeness, lossless transformation, or universal translatability.
  - STRATA automatically generates valid macro-objects or higher-level functions.
  - A failed claim can be dissolved by moving to another frame, granularity, level, or function.
  - Formal precision, technical implementation, or corpus size increases truth or authority.
  required_example:
    minimal_case: Show an otherwise plausible PMS reconstruction that silently moves from a local occurrence to a
      higher-level claim, then show how an explicit STRATA declaration makes the movement testable and bounded.
    restriction: The example must remain non-domain-specific and must not pre-empt the full operation definitions
      of Chapter 4.
  required_counterpressure:
  - A higher-level reconstruction may be more legible while remaining no more authoritative than the source claim.
  - A vertical transformation may be available but inadmissible.
  - A structure may remain non-captured even after multiple plausible transformations.
  - A change of analytical position may produce a new claim while leaving the original failure intact.
  redundancy_guard:
    defines_here:
    - positive and negative scope of STRATA
    - No Meta-PMS
    - No Ontology of Layers
    - governing claim
    - initial claim boundary
    references_only:
    - full object definitions from Chapter 1
    - coordinate definitions from Chapter 2
    - operation signatures from Chapter 4
    - admissibility criteria from Chapter 6
    - record fields from Chapter 7
    must_not_duplicate:
    - Chapter 6 admissibility mechanics
    - Chapter 8 non-equivalence catalogue
    - Chapter 41–53 LIMITS systematization
    - Chapter 57 final claim boundary
    handoff_rule: Chapter 8 converts existing definitions into audit non-equivalences; it does not restate Chapter
      0 as a second claim-boundary chapter.
  model_relation:
    supplies:
    - global claim ceiling
    - authority inheritance prohibition
    - permitted core operation count
    - legitimate terminal outputs including stop and non-capture
    does_not_supply:
    - empirical truth conditions
    - causal proof
    - automatic application decisions
    model_artifacts:
    - PMS-STRATA.yaml
    - Output_Classes.yaml
    - Admissibility_Rules.yaml
  appendix_migration:
    retain_in_chapter:
    - governing claim
    - No Meta-PMS
    - No Ontology of Layers
    - initial claim boundary
    migrate:
    - expanded valid/invalid claim examples to Appendix_H_Valid_and_Invalid_Transformation_Patterns.md
    - extended confusion cases to Appendix_I_Boundary_and_Confusion_Cases.md
  completion_test:
  - The chapter states one clear positive governing claim and one explicit negative boundary.
  - The relationship to PMS Base is dependent but non-revisionary.
  - Relative levels are described only as analytical relations.
  - Failure, Stop, Claim Reduction, and Non-Capture remain possible.
  - No application, person-typing, causal, predictive, or normative authority is implied.
  - Every later foundational chapter can inherit a bounded mandate without borrowing new authority.
```

---

## 5. Chapter 1 — Object Model: Operator Type, Operator Occurrence, and Composite Structure

```yaml
chapter:
  number: '1'
  title: 'Object Model: Operator Type, Operator Occurrence, and Composite Structure'
  role_in_work:
    primary_function: Define the classes of objects on which STRATA transformations may operate and the identity conditions
      that keep those objects distinguishable across transformation.
    canonical_status: Primary definition site for operator type, operator occurrence, composite structure, configuration
      as object, event-like object, non-event structure, transition as object, derived analytical object, and object
      identity across transformation.
    handoff: Provides Chapters 2–7 with typed source and target objects and prevents operations from acting on undefined
      or category-confused entities.
  governing_question: What exactly is being composed, decomposed, or projected, and what must remain identifiable
    for a transformation to count as operating on the claimed source object?
  required_claim:
    core: STRATA operates on concrete occurrences, configurations, events, non-events, transitions, and composites;
      it does not decompose or transform the abstract Δ–Ψ operator types themselves.
    identity_rule: Object identity across transformation is a bounded claim involving reference, origin type, constitutive
      relations, function, and temporal continuity; no single criterion guarantees identity in every case.
    derived_object_rule: Path, trajectory, macro-event, frame-function, attractor-function, modulating profile, and
      higher-level composite function are derived analytical objects or functions, not new PMS primitives.
  required_distinctions:
  - operator sign versus operator name versus operator type
  - operator type versus operator occurrence
  - operator occurrence versus composite structure
  - configuration versus complete world description
  - event-like object versus causal atom
  - structured non-event versus mere absence or missing information
  - transition as object versus simple difference of states
  - derived analytical object versus new PMS primitive
  - reference identity versus nominal sameness
  dependencies:
    hard:
    - Chapter 0
    - PMS.yaml
    - PMS_STRATA_Minified_Canonical.md
    operator_constraints:
    - Canonical operator functions and dependencies come only from PMS Base.
    - The PMS Base term operator_layers may not be converted into an ontology of real strata.
  must_not_claim:
  - A base operator is an empirical object with decomposable material parts.
  - An operator occurrence is identical with its abstract operator type.
  - A composite must reduce to one dominant operator.
  - An event is necessarily punctual, causally isolated, or internally simple.
  - A non-event is any absence, unknown event, or missing record.
  - Derived analytical objects extend the Δ–Ψ grammar.
  - Reference identity is preserved merely because the same label is reused.
  required_example:
    minimal_case: Contrast the Frame operator type with one concrete frame-typed occurrence, then show how several
      occurrences and relations can form a composite without changing the operator type.
    secondary_case: Show a non-event structure whose expectation frame is explicit and distinguish it from missing
      information.
  required_counterpressure:
  - One occurrence may support competing operator typings without revising PMS Base.
  - A stable composite function may coexist with internal heterogeneity and conflict.
  - A transformation may preserve historical reference while revising the source function.
  - A nominally identical target may fail the reference-continuity test.
  redundancy_guard:
    defines_here:
    - object categories
    - minimal object identity criteria
    - derived analytical object status
    chapter_3_boundary: Chapter 1 defines the object classes; Chapter 3 defines their temporal relations and the stronger
      sequence–path–trajectory chain.
    chapter_5_boundary: Chapter 1 introduces identity dimensions; Chapter 5 defines origin type, target function,
      and continuity requirements in the projection context.
    chapter_7_boundary: Chapter 1 defines objects; Chapter 7 records them and may not add object categories.
    must_not_duplicate:
    - full path and trajectory definitions
    - operation signatures
    - admissibility tests
  model_relation:
    supplies:
    - object category registry
    - source-object and target-object type constraints
    - derived-object non-primitive flag
    - reference identity fields
    model_artifacts:
    - PMS-STRATA.yaml
    - Transformation_Record.schema.json
    - Operation_Registry.yaml
    model_limit: The model may validate declared object categories and fields; it may not determine empirical object
      identity.
  appendix_migration:
    retain_in_chapter:
    - canonical object definitions
    - foundational object distinctions
    - identity criteria
    migrate:
    - expanded definition tables to Appendix_A_Core_Definitions.md
    - formal object notation to Appendix_B_Formal_Notation.md
    - edge-case catalogues to Appendix_H_Valid_and_Invalid_Transformation_Patterns.md
  completion_test:
  - Every valid operation source in later chapters belongs to a defined object category.
  - Operator type and operator occurrence cannot be confused.
  - Only occurrences and composites are decomposable.
  - Event-like object and non-event structure remain frame-bound and source-bound.
  - Derived objects are explicitly non-primitive.
  - At least one counterexample shows that name continuity is insufficient for object identity.
  - Chapter 3 can add temporal relations without redefining the object model.
```

---

## 6. Chapter 2 — Frame, Granularity, and Relative Level

```yaml
chapter:
  number: '2'
  title: Frame, Granularity, and Relative Level
  role_in_work:
    primary_function: Define the analytical coordinates required to locate every STRATA source, target, and transformation.
    canonical_status: Primary definition site for frame, granularity, relative level, temporal scope, source scope,
      claim scope, and the minimal level declaration.
    handoff: Supplies every later chapter and every transformation record with a non-ontological coordinate system.
  governing_question: How can a reconstruction declare context, resolution, relative position, time, sources, and
    claim reach without collapsing these dimensions into one vague language of levels?
  required_claim:
    core: 'Frame, granularity, and relative level are independent but related analytical coordinates: frame bounds
      relevance, granularity specifies resolution, and relative level specifies position within a declared relation.'
    plurality_rule: Multiple granularities may be valid for the same object and claim family; no resolution possesses
      automatic truth priority.
    level_rule: Micro, meso, and macro are optional relational abbreviations only when their comparison relation is
      explicit.
  required_distinctions:
  - frame versus granularity
  - frame versus transformation context
  - granularity versus relative level
  - relative level versus ontological layer
  - source level versus target level
  - temporal scope versus trajectory
  - source scope versus claim scope
  - changed frame versus changed granularity
  - changed granularity versus changed relative level
  - granularity mismatch versus substantive contradiction
  dependencies:
    hard:
    - Chapter 0
    - Chapter 1
    - PMS_STRATA_Minified_Canonical.md
    coordinate_inputs:
    - defined reference object from Chapter 1
    - bounded claim from Chapter 0
  must_not_claim:
  - Frames, granularities, or levels are universal natural units.
  - Finer granularity is deeper, truer, or more authoritative.
  - Higher relative level is more comprehensive or more valid.
  - A frame change automatically constitutes a vertical operation.
  - A granularity change automatically changes the source object or its function.
  - Micro, meso, and macro are fixed cross-domain classes.
  - Granularity difference automatically resolves a real disagreement.
  required_example:
    minimal_case: 'Use one conversation as a source object and show: stable frame with finer granularity, changed
      frame with stable granularity, and changed relative level within an explicitly declared comparison relation.'
    record_output: Complete the minimal level declaration for each of the three variants.
  required_counterpressure:
  - Two reconstructions may both be valid at different granularities without being mutually reducible.
  - Two analyses may appear contradictory because their granularities are not comparable.
  - A changed frame may be mere recontextualization rather than PROJECT_AS.
  - The same object may occupy different relative positions in different declared relations.
  redundancy_guard:
    defines_here:
    - all analytical coordinate terms
    - minimal level declaration
    - multiple-valid-granularity rule
    chapter_4_boundary: Chapter 2 defines coordinates; Chapter 4 defines the operation that relates source and target
      coordinates.
    chapter_5_boundary: Chapter 2 distinguishes frame from transformation context; Chapter 5 specifies how transformation
      context governs a target function.
    chapter_7_boundary: Chapter 7 records these coordinates without redefining them.
    limits_boundary: Chapters 42–45 apply anti-ontology and admissibility pressure to these coordinates; they do not
      replace the primary definitions.
  model_relation:
    supplies:
    - frame field
    - source_granularity and target_granularity fields
    - source_level and target_level fields
    - temporal_scope
    - source_scope
    - claim_scope
    - granularity relation declarations
    model_artifacts:
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    - Boundary_Decision_Tree.yaml
    model_limit: Schemas may require coordinate declarations but may not infer a universal hierarchy or determine
      the best granularity.
  appendix_migration:
    retain_in_chapter:
    - canonical coordinate definitions
    - minimal level declaration
    - coordinate-change distinctions
    migrate:
    - formal coordinate notation to Appendix_B_Formal_Notation.md
    - extended mismatch patterns to Appendix_I_Boundary_and_Confusion_Cases.md
  completion_test:
  - Frame, granularity, relative level, and transformation context are non-confusable.
  - Every level term is relational and locally declared.
  - No universal micro–meso–macro hierarchy is implied.
  - The minimal level declaration is sufficient for all three operation families.
  - At least one case demonstrates multiple valid granularities.
  - At least one countercase demonstrates that granularity mismatch does not automatically neutralize disagreement.
  - Later chapters can reference coordinate terms without redefining them.
```

---

## 7. Chapter 3 — Configuration, Event, Non-Event, Transition, Path, and Trajectory

```yaml
chapter:
  number: '3'
  title: Configuration, Event, Non-Event, Transition, Path, and Trajectory
  role_in_work:
    primary_function: Define the temporal object chain and the additional structural burden required at each transition
      from configuration to trajectory.
    canonical_status: Primary definition site for configuration versus state, event, non-event, transition, sequence,
      path, trajectory, path dependence as a property, sedimentation, irreversibility, and unrealized alternatives.
    handoff: Provides PATH with temporally typed objects while preventing chronology, duration, or Θ alone from being
      mistaken for path dependence.
  governing_question: What additional structure is required to move from a configuration and event relation to a sequence,
    path, trajectory, and path-dependence claim?
  required_claim:
    chain: configuration → transition → sequence → path → trajectory is a burden-increasing analytical chain, not
      an automatic derivation.
    trajectory_rule: A trajectory is a temporally ordered path with sedimented historical load that changes present
      meaning, costs, or continuation possibilities without implying teleology.
    path_dependence_rule: Path dependence is a property of historical determination, not a separate object class and
      not an automatic consequence of temporal duration.
    theta_rule: Θ enables temporal structuring but does not alone establish trajectory formation, sedimentation, or
      path dependence.
  required_distinctions:
  - state versus configuration
  - event versus non-event
  - event versus transition
  - transition versus state difference
  - chronology versus sequence
  - sequence versus path
  - path versus trajectory
  - trajectory versus path dependence
  - duration versus sedimentation
  - directionality versus teleology
  - irreversibility claim versus metaphysical absolute irreversibility
  - unrealized alternative versus unconstrained counterfactual fiction
  dependencies:
    hard:
    - Chapter 0
    - Chapter 1
    - Chapter 2
    - PMS.yaml
    operator_constraints:
    - Θ supports temporal ordering.
    - Λ requires an expectation frame and is not missing information.
    - Α + Θ, Ω + Θ, Ψ + Θ, and Λ + Θ may carry stronger sedimentation claims when source-supported.
  must_not_claim:
  - Chronological order is sufficient for a path.
  - Any path is automatically a trajectory.
  - Any trajectory is strongly path-dependent.
  - Θ alone creates path dependence, sedimentation, or recontextualization.
  - A trajectory has a necessary goal or teleological direction.
  - An event must be punctual or causally isolated.
  - A non-event is merely absent data.
  - An unrealized alternative was historically available without source support.
  - Irreversibility is absolute, metaphysical, or context-free.
  required_example:
    minimal_case: Construct one minimal chain from two configurations through a transition and sequence, then state
      the extra evidence needed before calling it a path and the further burden needed before calling it a trajectory.
    negative_variant: Show a temporally ordered chronology that fails to become a path.
  required_counterpressure:
  - Two similar end configurations may carry different costs, bindings, and residues because their paths differ.
  - A trajectory may be reconstructible while path dependence remains weak.
  - A long duration may contain no sedimentation relevant to the claim.
  - A central apparent non-event may fail because no expectation frame is supported.
  - Several competing trajectory constructions may remain co-valid or underdetermined.
  redundancy_guard:
    chapter_1_boundary: Chapter 1 defines configuration, event-like object, non-event structure, and transition as
      object categories; Chapter 3 defines their temporal relations and stronger temporal chain.
    chapter_9_12_boundary: Chapter 3 provides canonical definitions; PATH Chapters 9–12 operationalize temporal order,
      path, trajectory, and path dependence without redefining them.
    chapter_6_boundary: Chapter 3 states object burdens; Chapter 6 judges whether a specific distinction or composition
      is admissible.
    must_not_duplicate:
    - COMPOSE procedure
    - full branch taxonomy
    - PATH local audit
  model_relation:
    supplies:
    - temporal object categories
    - object-chain constraints
    - path-dependence property field
    - sedimentation and irreversibility declarations
    - unrealized-alternative status
    model_artifacts:
    - PMS-STRATA.yaml
    - Operation_Registry.yaml
    - Boundary_Decision_Tree.yaml
    model_limit: The model may validate the declared chain and required fields but may not infer historical availability,
      causality, or path dependence from timestamps alone.
  appendix_migration:
    retain_in_chapter:
    - canonical temporal definitions
    - minimal temporal object chain
    - path-dependence distinction
    migrate:
    - formal temporal notation to Appendix_B_Formal_Notation.md
    - expanded trajectory and weighting tests to Appendix_J_Operator_Weighting_and_Trajectory_Stress_Tests.md
    - full cases to Chapters 17 and the case repository
  completion_test:
  - Every step in the temporal object chain states its additional burden.
  - Sequence, path, trajectory, and path dependence are non-confusable.
  - Θ alone is explicitly insufficient for strong trajectory or path-dependence claims.
  - Non-events require an expectation frame.
  - Directionality remains non-teleological.
  - Irreversibility remains frame-bound and claim-bound.
  - PATH can operationalize these objects without adding a new definition layer.
```

---

## 8. Chapter 4 — The Three STRATA Operations: COMPOSE, DECOMPOSE, and PROJECT_AS

```yaml
chapter:
  number: '4'
  title: 'The Three STRATA Operations: COMPOSE, DECOMPOSE, and PROJECT_AS'
  role_in_work:
    primary_function: Define the identity, direction, source/target relation, preservation burden, loss burden, and
      characteristic confusion of each STRATA core operation.
    canonical_status: Primary prose definition site for COMPOSE, DECOMPOSE, PROJECT_AS, operation chains, non-invertibility,
      and minimal operation declaration.
    handoff: Supplies PATH, SUB, RETYPE, the Shared Transformation Record, and Formal Model v0 with one mutually exclusive
      but chainable operation grammar.
  governing_question: How can vertical analytical movement be classified as composition, decomposition, or functional
    projection so that each movement carries its own source, target, preservation, loss, and failure conditions?
  required_claim:
    operation_count: 'STRATA has exactly three core operations: COMPOSE, DECOMPOSE, and PROJECT_AS.'
    compose: COMPOSE forms a new composite analytical object from multiple or sequential source objects and must declare
      ordering, selection, preservation, compression, and loss.
    decompose: DECOMPOSE reconstructs the finer relational structure of a provisionally compressed occurrence or composite
      while retaining the source object as the reference and test target.
    project_as: PROJECT_AS preserves source reference and origin type while assigning a bounded target function within
      a declared target context.
    chain_rule: Operations may be chained, but every link requires a separate declaration, loss account, admissibility
      test, and possibility of failure.
    non_invertibility:
    - DECOMPOSE(COMPOSE(X)) ≠ X
    - COMPOSE(DECOMPOSE(X)) ≠ X
    - PROJECT_AS(X) ≠ X as a new origin type
  required_distinctions:
  - operation identity versus common direction metaphor
  - source object versus target object
  - target object versus target function
  - composition versus aggregation or chronology
  - decomposition versus description or added detail
  - decomposition versus formation of a competing PATH object
  - functional projection versus recontextualization
  - functional projection versus analogy or renaming
  - operation chain versus collapsed multi-operation claim
  - non-invertibility versus simple reversibility failure
  dependencies:
    hard:
    - Chapters 0–3
    - PMS_STRATA_Operation_Signatures_Minified.md
    - PMS_STRATA_Minified_Canonical.md
    required_inputs:
    - typed source objects from Chapter 1
    - declared analytical coordinates from Chapter 2
    - temporal object distinctions from Chapter 3
  must_not_claim:
  - There is a fourth implicit core operation.
  - Chronological enumeration is sufficient for COMPOSE.
  - Any finer description is DECOMPOSE.
  - DECOMPOSE applies to abstract PMS operator types.
  - A frame change or Φ recontextualization is automatically PROJECT_AS.
  - PROJECT_AS replaces the origin type.
  - Operation direction is ontological ascent or descent.
  - Operation chains inherit validity from earlier links.
  - Any operation is lossless or automatically reversible.
  required_example:
    shared_source_family: 'Use one small source family to show three different questions: compose occurrences into
      a path, decompose the path into internal transitions, and project the path as a bounded frame-function in a
      later context.'
    record_requirement: Each example must include a minimal operation declaration and must make clear that the three
      outputs are not interchangeable.
  required_counterpressure:
  - A chronology may fail COMPOSE because no structural relation or praxeological gain is established.
  - Additional detail may fail DECOMPOSE because the source object and coarser function are no longer reconstructible.
  - A rhetorically apt label may fail PROJECT_AS because source trace or target context is missing.
  - A dual-operation case may require DECOMPOSE followed by PROJECT_AS rather than one collapsed claim.
  - A later operation may fail even when the earlier operation was admissible.
  redundancy_guard:
    defines_here:
    - core operation identities
    - minimal operation declaration
    - non-invertibility
    - chain separation rule
    chapter_7_boundary: Chapter 4 defines what operations are; Chapter 7 defines how any operation is recorded. Record
      fields may not create operation semantics.
    operational_part_boundary: Chapters 15, 20, and 30 specify the detailed procedures of COMPOSE, DECOMPOSE, and
      PROJECT_AS respectively; they operationalize but do not redefine the core signatures.
    chapter_8_boundary: Chapter 8 converts operation distinctions into non-equivalence audit rules.
    must_not_duplicate:
    - full admissibility band
    - operation-specific case corpora
  model_relation:
    supplies:
    - canonical operation enum
    - source and target signatures
    - required declarations
    - preservation and loss duties
    - central failure modes
    - operation-chain constraints
    model_artifacts:
    - Operation_Registry.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    model_limit: Formal classification may flag missing declarations or category conflicts; it may not establish semantic
      adequacy or empirical validity.
  appendix_migration:
    retain_in_chapter:
    - operation definitions
    - direction and identity distinctions
    - non-invertibility
    - minimal operation declaration
    migrate:
    - full operation record templates to Appendices D–F
    - expanded valid/invalid patterns to Appendix H
    - confusion decision cases to Appendix I
  completion_test:
  - COMPOSE, DECOMPOSE, and PROJECT_AS are mutually distinguishable.
  - No fourth core operation is implied.
  - Each operation has explicit source, target, preservation, loss, and central failure conditions.
  - Operator types remain non-decomposable.
  - Origin type remains preserved under PROJECT_AS.
  - Operations may chain only through separate records.
  - All three non-invertibility statements are present and correctly interpreted.
  - The operation registry can be built without adding prose semantics not found in the chapter.
```

---

## 9. Chapter 5 — Origin Type, Target Function, and Transformation Context

```yaml
chapter:
  number: '5'
  title: Origin Type, Target Function, and Transformation Context
  role_in_work:
    primary_function: Define the identity and continuity discipline that allows an object to perform a bounded function
      in another context without becoming a different origin type.
    canonical_status: Primary definition site for origin type, target function, transformation context, reference
      identity, type integrity, functional continuity, temporal continuity, and contextual boundedness.
    handoff: Provides Chapter 6 with integrity criteria and RETYPE with the non-replacement grammar required for PROJECT_AS.
  governing_question: What must remain continuous, and what may change, when a source object is reconstructed or projected
    across contexts, granularities, or relative levels?
  required_claim:
    origin_type_rule: The origin type identifies the source object within its source reconstruction and may not be
      retrospectively overwritten by a later target function.
    target_function_rule: A target function is a bounded, relational role performed within a declared target context;
      it is not a new primitive, global property, or permanent identity.
    continuity_rule: A valid transformation must preserve or explicitly qualify reference, type, functional, and where
      relevant temporal continuity.
    context_rule: Transformation context determines the target function, validity scope, relevant sources, and claim
      ceiling.
  required_distinctions:
  - origin type versus target function
  - source frame versus target frame
  - frame versus transformation context
  - reference continuity versus nominal continuity
  - type integrity versus functional similarity
  - functional continuity versus metaphorical association
  - temporal continuity versus timeless identity
  - contextual boundedness versus generalization
  - projection without replacement versus full retyping
  dependencies:
    hard:
    - Chapters 0–4
    - PMS_STRATA_Operation_Signatures_Minified.md
    required_inputs:
    - source object identity from Chapter 1
    - source/target coordinates from Chapter 2
    - operation identity from Chapter 4
  must_not_claim:
  - A target function changes the source object’s origin type.
  - Functional similarity proves operator identity.
  - A projection is valid without a declared target context.
  - A local target function applies automatically to later or parallel contexts.
  - Historical development becomes a timeless property.
  - Reference continuity is guaranteed by using the same name.
  - Functional continuity is source-independent.
  - A successful projection creates a new PMS primitive or grants authority.
  required_example:
    minimal_projection: Show a reconstructed trajectory retaining origin type trajectory while performing a bounded
      frame-function in one later configuration.
    required_declaration:
    - source object
    - origin type
    - source level
    - target context
    - target level
    - target function
    - validity scope
    - load-bearing source features
  required_counterpressure:
  - The same source object may support different compatible functions in different target contexts.
  - A relevant source change must weaken, alter, or defeat the target function.
  - A later function may be valid while the original source claim remains provisional.
  - A projection may preserve reference but fail type integrity.
  - A useful analogy may remain below the threshold of functional continuity.
  redundancy_guard:
    defines_here:
    - origin type
    - target function
    - transformation context
    - reference/type/functional/temporal continuity
    - contextual boundedness
    chapter_6_boundary: Chapter 5 defines integrity and continuity criteria; Chapter 6 uses them as non-compensatory
      admissibility conditions.
    chapter_29_30_boundary: RETYPE Chapters 29–30 operationalize projection and PROJECT_AS; they reference these definitions.
    chapter_47_boundary: Chapter 47 systematizes continuity failures within LIMITS but may not create competing definitions.
    chapter_1_boundary: Chapter 1 defines general object identity; Chapter 5 specifies identity and continuity across
      transformation.
  model_relation:
    supplies:
    - origin_type field
    - target_function field
    - transformation_context field
    - reference continuity status
    - type integrity status
    - functional continuity status
    - temporal continuity status
    - validity scope
    model_artifacts:
    - Transformation_Record.schema.json
    - Admissibility_Rules.yaml
    - PMS-STRATA.yaml
    model_limit: The model may require continuity declarations and detect direct type replacement; it may not determine
      semantic continuity automatically.
  appendix_migration:
    retain_in_chapter:
    - canonical type/function/context definitions
    - continuity criteria
    - minimal projection form
    migrate:
    - formal notation to Appendix B
    - expanded PROJECT_AS schema to Appendix F
    - continuity edge cases to Appendices H and I
  completion_test:
  - Origin type and target function are non-confusable.
  - Transformation context is distinct from frame and explicitly bounds the function.
  - Reference, type, functional, and temporal continuity each have separate criteria.
  - A projection cannot be stated without validity scope and source trace.
  - At least one example shows the same source supporting different context-bound functions.
  - At least one counterexample shows nominal sameness without real continuity.
  - Chapter 6 can use the integrity conditions without redefining them.
```

---

## 10. Chapter 6 — The STRATA Admissibility Band

```yaml
chapter:
  number: '6'
  title: The STRATA Admissibility Band
  role_in_work:
    primary_function: Define the non-compensatory operating range within which any STRATA transformation can count
      as warranted.
    canonical_status: Primary definition site for the Praxeological Relevance Floor, Praxeological Traceability Ceiling,
      PraxisPurchase, TraceableLoad, Counterfactual Sensitivity, unified admissibility test, and No Universal STRATA
      Scale rule.
    handoff: Supplies every operation, local audit, output classification, LIMITS chapter, and formal model with one
      shared admissibility grammar.
  governing_question: When does additional resolution, composition, or functional projection produce a warranted praxeological
    distinction, and when does it become detail without purchase or abstraction without traceable load?
  required_claim:
    band: A STRATA transformation is admissible only within a relational band above distinction without praxeological
      purchase and below abstraction without traceable load.
    unified_test: Admissible(T, X, C) iff PraxisPurchase and TraceableLoad and TypeIntegrity and ContextualBoundedness.
    non_compensation: 'The required conditions are non-compensatory: strength on one dimension cannot cancel failure
      on another.'
    counterfactual_rule: A relevant change in a declared load-bearing source structure should alter the composed object,
      decomposed source function, or projected target function.
    scale_rule: The band is not a universal numeric scale and has no fixed smallest element or largest legitimate
      composite.
  required_distinctions:
  - additional detail versus additional praxeological finding
  - Praxeological Relevance Floor versus source ceiling
  - Praxeological Traceability Ceiling versus citation presence
  - traceable load versus exhaustive reproduction
  - counterfactual sensitivity versus causal proof
  - type integrity versus semantic attraction
  - contextual boundedness versus global validity
  - admissibility result versus truth verdict
  - claim reduction versus failed transformation
  - mandatory stop versus non-capture
  dependencies:
    hard:
    - Chapters 0–5
    - PMS_STRATA_Admissibility_Band_Minified.md
    - PMS_STRATA_Minified_Canonical.md
    inherited_criteria:
    - object identity from Chapter 1
    - coordinates from Chapter 2
    - operation identity from Chapter 4
    - type and continuity integrity from Chapter 5
  must_not_claim:
  - Admissibility can be represented as a universal score whose dimensions compensate for one another.
  - More detail automatically satisfies the Relevance Floor.
  - More citations automatically satisfy the Traceability Ceiling.
  - Counterfactual sensitivity proves causality.
  - A formally valid record is an admissible transformation.
  - The band supplies universal thresholds for paths, trajectories, attractors, or macrofunctions.
  - Admissibility implies empirical truth, normative validity, or application authority.
  - Failure can always be repaired by another transformation.
  required_example:
    lower_boundary: A correct but finer distinction that changes no warranted reconstruction and therefore yields
      resolution without praxeological purchase.
    upper_boundary: A rhetorically powerful macro-label that remains unchanged across materially different source
      structures and therefore lacks traceable load.
    within_band: One transformation that changes a relevant praxis dimension, preserves source trace and type integrity,
      and has a bounded validity scope.
  required_counterpressure:
  - A very detailed decomposition may remain resolution-neutral or require stop.
  - A highly elegant composition may fail because its constitutive path cannot be reconstructed.
  - A useful analogy may be retained as analogy_only rather than forced into projection.
  - A source-limited case may require provisional output rather than binary success or failure.
  - No available transformation may satisfy all conditions, making non-capture appropriate.
  redundancy_guard:
    defines_here:
    - the two band boundaries
    - unified admissibility logic
    - counterfactual sensitivity as load test
    - No Universal STRATA Scale
    chapter_5_boundary: Chapter 5 defines type, function, continuity, and context; Chapter 6 uses them as admissibility
      requirements.
    chapter_7_boundary: Chapter 6 defines the tests; Chapter 7 provides fields for recording their results.
    limits_boundary: Chapters 44–53 expand, apply, and audit the band; they do not create a second admissibility system.
    model_boundary: Admissibility_Rules.yaml formalizes declarations and result classes but does not replace prose
      judgment.
  model_relation:
    supplies:
    - admissibility rule families
    - non-compensatory gate logic
    - boundary result states
    - counterfactual sensitivity classes
    - claim-reduction and stop triggers
    - canonical output mapping
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - PMS-STRATA.yaml
    model_limit: The model may detect missing or incompatible declarations and map outputs; it may not decide empirical
      relevance, semantic adequacy, or causal truth.
  appendix_migration:
    retain_in_chapter:
    - canonical boundary definitions
    - unified admissibility formula
    - praxis-relevant dimensions
    - counterfactual core question
    - No Universal STRATA Scale
    migrate:
    - expanded test catalogue to Appendix G
    - valid and invalid patterns to Appendix H
    - boundary confusion cases to Appendix I
  completion_test:
  - Both lower and upper boundaries are explicit and non-symmetric in failure mode.
  - PraxisPurchase, TraceableLoad, TypeIntegrity, and ContextualBoundedness are all required.
  - The gate is explicitly non-compensatory.
  - Counterfactual Sensitivity is defined as a load test rather than causal proof.
  - At least one example falls below, within, and above the band.
  - Claim Reduction, Mandatory Stop, Failure, and Non-Capture remain distinct possible outputs.
  - No universal scale or fixed threshold is implied.
  - Formal Model v0 can encode the rule families without claiming automatic truth determination.
```

---

## 11. Chapter 7 — Shared Transformation Record

```yaml
chapter:
  number: '7'
  title: Shared Transformation Record
  role_in_work:
    primary_function: Define one shared declaration and audit structure for COMPOSE, DECOMPOSE, PROJECT_AS, and their
      chains.
    canonical_status: Primary definition site for the common source, operation, target, admissibility, loss, alternatives,
      governance, and record-status field families.
    handoff: Supplies cases, operation-specific records, the formal schema, and the Integrated STRATA Audit with a
      common trace structure.
  governing_question: What must every transformation disclose so that its source, operation, target, admissibility,
    loss, alternatives, limits, and status remain reviewable across all STRATA parts?
  required_claim:
    core: Every STRATA transformation uses the same shared record envelope, with operation-specific extensions permitted
      only when they do not bypass common declaration duties.
    record_boundary: The record makes a transformation inspectable and comparable; it does not prove that the reconstruction
      is true, causally correct, semantically adequate, or normatively valid.
    chain_rule: Every operation in a chain receives its own record segment and output status.
  required_distinctions:
  - transformation versus transformation record
  - record completeness versus transformation admissibility
  - record status versus canonical output class
  - source basis versus proof
  - operation justification versus automatic warrant
  - preserved versus compressed versus excluded versus uncertain versus irrecoverable
  - rival transformation versus non-translation
  - claim ceiling versus authority inheritance
  - local extension versus bypass of shared fields
  dependencies:
    hard:
    - Chapters 0–6
    - PMS_STRATA_Minified_Canonical.md
    required_inputs:
    - object categories from Chapter 1
    - coordinates from Chapter 2
    - operation identities from Chapter 4
    - continuity fields from Chapter 5
    - admissibility tests and outputs from Chapter 6
  must_not_claim:
  - A syntactically complete record is empirically or semantically valid.
  - The schema can decide truth, causality, normative validity, or correct interpretation.
  - Operation-specific fields may remove shared source, loss, alternative, or governance duties.
  - The record creates a fourth operation or new object class.
  - A single record may collapse multiple operations into one undifferentiated step.
  - Unknown structure can be converted into precise fields without source support.
  - Technical validation increases claim authority.
  required_example:
    minimal_record: Provide one compact shared record for an admissible transformation with all seven field families
      populated.
    negative_variant: Provide a syntactically complete record whose source trace is insufficient and show that formal
      completeness does not prevent failed_transformation or claim_reduction_required.
  required_counterpressure:
  - A record may be complete but semantically unsupported.
  - A record may be incomplete because non-capture is the correct result rather than because the analyst failed to
    fill fields.
  - A chain may contain one admissible operation followed by one failed operation.
  - Two rival transformations may require separate records rather than forced integration.
  - A field may remain underdetermined when sources do not support greater precision.
  redundancy_guard:
    defines_here:
    - shared field families
    - record status
    - local extension rule
    - integrated use
    chapter_4_boundary: Chapter 4 defines operation semantics; Chapter 7 records them and may not revise them.
    chapter_6_boundary: Chapter 6 defines admissibility criteria; Chapter 7 records their results and may not turn
      fields into automatic judgment.
    appendix_boundary: Appendices C–F contain expanded schemas and templates; the chapter retains the canonical envelope
      only.
    model_boundary: Transformation_Record.schema.json mirrors the record contract and may not become the primary theory
      source.
  model_relation:
    supplies:
    - top-level record structure
    - required field families
    - status values
    - operation-chain representation
    - governance field including authority_inheritance prohibited
    model_artifacts:
    - Transformation_Record.schema.json
    - PMS-STRATA.schema.json
    - PMS-STRATA.yaml
    model_limit: Schema validation can test presence, type, and allowed values; it cannot validate the truth or adequacy
      of the populated claims.
  appendix_migration:
    retain_in_chapter:
    - canonical shared envelope
    - field-family purposes
    - record status
    - local and integrated use rule
    migrate:
    - full schema to Appendix C
    - COMPOSE template to Appendix D
    - DECOMPOSE template to Appendix E
    - PROJECT_AS template to Appendix F
    - integrated audit template to Appendix N
  completion_test:
  - The record supports all three operations without flattening their differences.
  - Every shared field family has a clear purpose.
  - Loss, alternatives, governance, stop, and non-capture cannot be omitted by local extensions.
  - Operation chains require separate records or explicit record segments.
  - Record status and canonical output class are distinguishable and mappable.
  - A negative example demonstrates that schema validity is not theoretical validity.
  - The JSON schema can be built from the record without adding new semantic authority.
```

---

## 12. Chapter 8 — Foundational Non-Equivalences

```yaml
chapter:
  number: '8'
  title: Foundational Non-Equivalences
  role_in_work:
    primary_function: Convert the Foundations definitions into a compact cross-block set of prohibited equivalences
      used by drafting, model validation, cases, and audits.
    canonical_status: Primary collection site for foundational non-equivalence rules; not a second definition layer
      and not a second claim-boundary chapter.
    handoff: Provides PATH, SUB, RETYPE, LIMITS, Chapter Contracts, the Non-Equivalence Index, and the Boundary Decision
      Tree with reusable category-error tests.
  governing_question: Which tempting equivalences would collapse the distinctions established in Chapters 0–7 and
    thereby create ontological drift, type inflation, level mixing, false authority, or immunity from failure?
  required_claim:
    core: STRATA remains coherent only if its primary distinctions are preserved as explicit non-equivalences across
      all later operations and outputs.
    audit_rule: A non-equivalence does not prohibit comparison, relation, analogy, or transformation; it prohibits
      unmarked identity and authority transfer.
    minimum_catalogue:
    - finer granularity ≠ higher truth
    - relative level ≠ ontological layer
    - composition ≠ lossless addition
    - decomposition ≠ discovery of final constituents
    - path ≠ sequence
    - path ≠ trajectory
    - trajectory ≠ path dependence
    - origin type ≠ target function
    - projection ≠ operator identity
    - operator weighting ≠ operator replacement
    - structural analogy ≠ valid projection
    - recursion ≠ completeness
    - legibility ≠ authority
  required_distinctions:
  - non-equivalence versus non-relation
  - analogy versus identity
  - functional projection versus type replacement
  - greater resolution versus greater warrant
  - higher composition versus greater explanation
  - formal precision versus empirical validation
  - recursive possibility versus complete capture
  - operator weighting versus changed grammar
  - derived object versus primitive
  dependencies:
    hard:
    - Chapters 0–7
    - PMS_STRATA_Minified_Canonical.md
    definition_rule: Every non-equivalence must point back to primary definitions already established in Chapters
      0–7.
  must_not_claim:
  - The chapter introduces new object, operation, level, or admissibility definitions.
  - Every analogy or cross-level relation is invalid.
  - Non-equivalence means the terms can never be related or transformed.
  - The list is exhaustive for every future domain.
  - A non-equivalence itself proves a specific empirical counterclaim.
  - The chapter replaces the Claim Boundary, Admissibility Band, or Integrated Audit.
  - Formalizing the list guarantees compliance in actual analysis.
  required_example:
    comparison_matrix: For at least four non-equivalences, show one invalid identity claim and one admissible relational
      or transformational claim.
    mandatory_pairs:
    - origin type versus target function
    - path versus trajectory
    - structural analogy versus valid projection
    - legibility versus authority
  required_counterpressure:
  - A finer reconstruction may genuinely outperform a coarser one for a declared claim without becoming higher truth.
  - A trajectory may validly perform a frame-function without becoming a Frame operator type.
  - A structural analogy may remain useful even when PROJECT_AS is inadmissible.
  - A composition may form a new object while remaining lossy and non-total.
  - A technically valid implementation may still be semantically wrong or empirically unsupported.
  redundancy_guard:
    defines_here:
    - the canonical non-equivalence catalogue
    - the audit meaning of non-equivalence
    must_reference:
    - Chapter 0 for claim and authority boundaries
    - Chapter 1 for object distinctions
    - Chapter 2 for coordinate distinctions
    - Chapter 3 for temporal distinctions
    - Chapter 4 for operation distinctions
    - Chapter 5 for type/function continuity
    - Chapter 6 for admissibility
    - Chapter 7 for record boundaries
    must_not_duplicate:
    - full definitions from Chapters 0–7
    - detailed operation procedures
    - full LIMITS audit
    reference_handoff: The later Non_Equivalence_Index.md may index and cross-reference the catalogue but may not
      create parallel canonical wording.
  model_relation:
    supplies:
    - prohibited identity constraints
    - decision-tree confusion branches
    - schema cross-field consistency checks
    - audit flags
    model_artifacts:
    - Boundary_Decision_Tree.yaml
    - Admissibility_Rules.yaml
    - PMS-STRATA.schema.json
    model_limit: The model can flag explicit equivalence violations; it cannot reliably infer every semantic collapse
      from natural language.
  appendix_migration:
    retain_in_chapter:
    - canonical non-equivalence statements
    - brief explanation of each
    - minimal valid/invalid contrasts
    migrate:
    - expanded pattern catalogue to Appendix H
    - confusion cases to Appendix I
    - cross-domain analogy stress tests to Appendix K
    - index entries to 04_reference/Non_Equivalence_Index.md
  completion_test:
  - Every listed non-equivalence maps to a primary definition in Chapters 0–7.
  - The chapter introduces no new theoretical primitive or parallel definition.
  - Non-equivalence is distinguished from prohibition of relation or transformation.
  - At least four pairs include both invalid and admissible contrast examples.
  - Legibility, formal precision, and technical implementation are explicitly denied authority inheritance.
  - The catalogue can be used by later audits and the decision tree without rewriting the Foundations.
  - Completion of Chapter 8 leaves no unresolved type or operation question blocking PATH.
```

---


## 13. Foundations Cross-Chapter Dependency Chain

```text
Chapter 0
→ authorizes a bounded Foundations mandate

Chapter 1
→ defines valid source and target object categories

Chapter 2
→ locates those objects in frame, granularity, level, time, source, and claim scope

Chapter 3
→ defines the temporal relations among relevant objects

Chapter 4
→ defines the three transformations that may relate them

Chapter 5
→ defines identity, type, function, context, and continuity across transformation

Chapter 6
→ determines the shared admissibility range

Chapter 7
→ records every transformation and its limits

Chapter 8
→ converts the whole foundation into reusable non-equivalence tests
```

This is a production dependency, not a hierarchy of truth or authority.

---

## 14. Foundations Redundancy Matrix

| Concept family | Primary definition chapter | Later use without redefinition |
|---|---:|---|
| STRATA purpose and claim boundary | 0 | 6, 8, 41, 53, 57 |
| Object categories and general identity | 1 | 3–7, PATH, SUB, RETYPE |
| Frame, granularity, relative level, scopes | 2 | 4–7 and all operational parts |
| Temporal object chain | 3 | PATH and later cross-operation cases |
| Core operation identities | 4 | Chapters 15, 20, 30 and model registry |
| Origin type, target function, continuity | 5 | 6, RETYPE, Chapter 47 |
| Admissibility Band | 6 | local audits, LIMITS, formal rules |
| Shared Transformation Record | 7 | cases, schemas, integrated audit |
| Non-equivalence catalogue | 8 | reference index, decision tree, audits |

---

## 15. Round 1 Completion Gate

Round 1 is provisionally complete only when:

- exactly nine chapter contracts exist for Chapters 0–8;
- every contract contains all canonical schema fields;
- each core term has one primary definition site;
- the 1/3, 4/7, 5/6, 2/7, and 0/8 redundancy boundaries are explicit;
- no contract modifies PMS Base or introduces a fourth operation;
- Θ alone is explicitly insufficient for strong trajectory or path-dependence claims;
- operator types remain non-decomposable;
- origin type and target function remain distinct;
- the Admissibility Band remains non-compensatory and non-numeric;
- model relations remain validation and operationalization relations rather than truth authority;
- Stop and Non-Capture are present before any operational block begins;
- Chapter 8 closes Foundations without creating a second definition layer;
- PATH can begin after Foundations without an unresolved object, coordinate, temporal, operation, type, record, or admissibility question.

**Round status after generation:** `provisionally_complete`  
**Next contract round:** Chapters 9–28 — PATH and SUB, produced as two internal subpasses (9–17 and 18–28) within output 2/4

---

# ROUND 2 OF 4 — PATH AND SUB CHAPTER CONTRACTS

## 16. Round 2 Function and Global Rules

Round 2 adds the complete contracts for Chapters 9–28. It is produced as two internal subpasses:

```text
PATH  → Chapters 9–17
SUB   → Chapters 18–28
```

The round is governed by these constraints:

1. PATH forms temporal analytical objects through `COMPOSE`; it does not assign later contextual functions.
2. Θ enables temporal structure but does not alone establish trajectory or path dependence.
3. Non-events, alternatives, asymmetries, bindings, and loss remain visible in temporal composition.
4. SUB applies to occurrences and composites, never to the Δ–Ψ operator types themselves.
5. Finer granularity has no automatic truth, depth, or authority privilege.
6. Components without relations do not constitute a decomposition.
7. The coarser source function may be confirmed, refined, differentiated, partially preserved, rejected, or left underdetermined.
8. `DECOMPOSE` and `PROJECT_AS` remain separate operations even when used on the same source object.
9. Every chapter preserves Claim Reduction, Mandatory Stop, Failure, and Non-Capture.
10. Every operation-specific result must map to the canonical output system.

The YAML blocks below are the actual contracts.

---

## Chapter 9 — Temporal Order and Transition

```yaml
chapter:
  number: '9'
  title: Temporal Order and Transition
  role_in_work:
    primary_function: Establish the temporal primitives and transition conditions required before PATH can form paths
      or trajectories.
    canonical_status: Primary PATH definition site for temporal position, order dependence, duration, delay, persistence,
      temporal recontextualization, and transition validity.
    handoff: Provides Chapter 10 with warranted transitions rather than isolated states or chronology.
  governing_question: When does a temporal difference constitute a reconstructible transition rather than two disconnected
    descriptions?
  required_claim:
    core: A transition is a frame-bound, source-supported relation between configurations whose events, non-events,
      order, and changed praxis conditions are reconstructible.
    theta_boundary: Θ enables temporal structuring but does not alone establish path dependence, sedimentation, trajectory,
      or recontextualization.
    failure_rule: Two states without a warranted temporal and structural relation do not constitute a transition.
  required_distinctions:
  - temporal position versus calendar timestamp
  - order dependence versus mere succession
  - duration versus metric time alone
  - delay as transition structure versus delay as framed non-event
  - persistence versus stasis
  - transition versus difference between snapshots
  - temporal recontextualization versus retroactive erasure
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    chapter_handoff:
    - Chapter 3 supplies the object chain; Chapter 9 operationalizes its transition step.
    inherited_constraints:
    - No deterministic temporal law.
    - No unmarked frame change.
    - No causal proof from sequence.
  must_not_claim:
  - Θ alone creates a trajectory or path dependence.
  - A before/after pair automatically forms a transition.
  - Delay is always intentional obstruction.
  - Irreversibility is absolute or metaphysical.
  - A later frame erases the prior sequence.
  required_example:
    minimal_case: Two configurations separated by a documented delay and non-decision; show which fields establish
      a transition and which remain uncertain.
    restriction: Do not yet compose the transitions into a path.
  required_counterpressure:
  - Unknown temporal order may require a provisional or failed transition.
  - The same event order may carry different praxis consequences under different frames.
  - A frame change between configurations can invalidate direct comparison if unmarked.
  redundancy_guard:
    defines_here:
    - temporal position and order dependence
    - transition preconditions and structure
    - transition failure
    references_only:
    - general object definitions from Chapter 3
    - path definition from Chapter 10
    - full non-event logic from Chapter 14
    - COMPOSE procedure from Chapter 15
    must_not_duplicate:
    - Chapter 3 foundational definitions
    - Chapter 10 path selection
    - Chapter 12 path-dependence tests
  model_relation:
    supplies:
    - transition record fields
    - temporal-order validation conditions
    - transition failure flags
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can validate declared configurations, temporal order, and changed fields; it cannot infer
      actual transition causality.
  appendix_migration:
    retain_in_chapter:
    - temporal primitives
    - transition preconditions
    - minimal transition record
    - transition failure
    migrate:
    - extended temporal notation to Appendix B
    - transition record template details to Appendix D
    - confusion examples to Appendix I
  completion_test:
  - At least two configurations and a temporal relation are explicit.
  - Events and non-events are separately representable.
  - Changed frames, action corridors, asymmetries, bindings, and residue can be declared.
  - Θ is not treated as sufficient for trajectory or path dependence.
  - A failed transition remains a valid output.
```

---

<a id="chapter-10-path"></a>

## Chapter 10 — Path

```yaml
chapter:
  number: '10'
  title: Path
  role_in_work:
    primary_function: Define path as a selectively reconstructed realized sequence of relevant configurations and
      transitions.
    canonical_status: Primary PATH definition site for realized, blocked, aborted, and deferred paths, path frames,
      evidence, and path comparison.
    handoff: Supplies Chapter 11 with a path object that may or may not qualify as a trajectory.
  governing_question: What additional structure turns chronology or a sequence into a warranted path?
  required_claim:
    core: A path is the actually traversed, selectively reconstructed sequence of relevant configurations and transitions
      within a declared frame.
    selection_rule: Path construction must disclose inclusion, compression, evidence, unrealized alternatives, and
      open residue.
    non_dependence_rule: A path may be valid without strong path dependence.
  required_distinctions:
  - chronology versus sequence versus path
  - realized path versus blocked, aborted, or deferred continuation
  - path endpoint versus open continuation
  - path reconstruction versus retrospective plausibilization
  - same endpoint versus same path
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 9 warranted transitions
    chapter_handoff:
    - Receives transition objects from Chapter 9 and supplies path objects to Chapters 11–15.
    conditional:
    - Alternative claims depend on Chapter 13 source discipline.
  must_not_claim:
  - Chronological ordering is sufficient for a path.
  - Every non-realized possibility was genuinely available.
  - A path implies necessity, rationality, or strong dependence.
  - Similar endpoints imply equivalent praxis structure.
  - Path boundaries are objective and universal.
  required_example:
    minimal_case: Construct a short path from three configurations, including one blocked continuation and one open
      residue.
    restriction: Do not upgrade the path to a trajectory without Chapter 11 criteria.
  required_counterpressure:
  - A correct chronology can remain below the path threshold.
  - Two path constructions from the same materials may differ because of periodization or selection.
  - A current state may be largely present-determined despite a reconstructible path.
  redundancy_guard:
    defines_here:
    - path definition
    - path components and frame
    - realized, blocked, aborted, and deferred path
    - minimal path record
    references_only:
    - trajectory criteria from Chapter 11
    - path dependence from Chapter 12
    - branch ontology from Chapter 13
    - COMPOSE procedure from Chapter 15
    must_not_duplicate:
    - Chapter 9 temporal primitives
    - Chapter 11 sedimentation
    - Chapter 15 selection and loss mechanics
  model_relation:
    supplies:
    - path object schema
    - path evidence and alternative fields
    - path-specific result labels
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may check that a path has configurations, transitions, frame, evidence status, and claim
      scope; it cannot decide which elements are historically salient.
  appendix_migration:
    retain_in_chapter:
    - definition and path variants
    - comparison criteria
    - minimal path record
    migrate:
    - expanded path taxonomies to Appendix A
    - record mechanics to Appendix D
    - case variants to Appendix M
  completion_test:
  - The chapter cleanly separates chronology, sequence, and path.
  - Path selection and evidence are explicit.
  - Blocked, aborted, and deferred paths are not collapsed.
  - A path can exist without strong path dependence.
  - Similar endpoints with different histories remain distinguishable.
```

---

## Chapter 11 — Trajectory

```yaml
chapter:
  number: '11'
  title: Trajectory
  role_in_work:
    primary_function: Define trajectory as a path with sedimented historical load that shapes present configuration
      and future continuations.
    canonical_status: Primary PATH definition site for trajectory, historical sedimentation, non-teleological directionality,
      trajectory boundaries, and competing constructions.
    handoff: Supplies Chapter 12 with the developed object whose degree of path dependence can be tested.
  governing_question: When does a path become a trajectory rather than remain a sequence of transitions?
  required_claim:
    core: A trajectory is a temporally ordered path whose repeated and irreversible structure historically co-determines
      the present configuration and continuation possibilities.
    additional_requirements:
    - sedimentation
    - cumulative change
    - persistent residue
    - changed action corridors
    - historical load
    anti_teleology: Directionality may be reconstructed without necessity, destiny, progress, decline, or original
      plan.
  required_distinctions:
  - path versus trajectory
  - duration versus sedimentation
  - directionality versus teleology
  - historical load versus narrative coherence
  - trajectory boundary versus arbitrary periodization
  - single trajectory versus competing trajectory constructions
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 9
    - Chapter 10
    operator_load:
    - Α + Θ
    - Ω + Θ
    - Ψ + Θ
    - Λ + Θ
    handoff:
    - Supplies Chapter 12, Chapter 15, SUB Chapter 24, and RETYPE Chapters 31–33.
  must_not_claim:
  - Every long path is a trajectory.
  - Θ alone creates sedimentation.
  - A trajectory is deterministic or teleological.
  - Internal variation invalidates every trajectory claim.
  - One periodization is uniquely true.
  - A trajectory is already a frame-function, macro-event, or attractor-function.
  required_example:
    minimal_case: Compare a merely ordered path with a trajectory that shows accumulated asymmetry, persistent residue,
      and changed exit costs.
    restriction: The later contextual function of the trajectory remains unclaimed.
  required_counterpressure:
  - A repeated pattern may still show weak historical load.
  - Competing periodizations may both remain admissible.
  - A macro-label can fail if the underlying transitions and non-events cannot be traced.
  redundancy_guard:
    defines_here:
    - trajectory definition
    - sedimentation and changed action corridors
    - directionality without teleology
    - trajectory boundary and competing constructions
    - minimal trajectory record
    references_only:
    - path definition from Chapter 10
    - path-dependence property from Chapter 12
    - COMPOSE mechanics from Chapter 15
    - RETYPE projection families
    must_not_duplicate:
    - Chapter 12 strong and weak dependence
    - Chapter 15 compression accounting
    - Chapter 31–33 target functions
  model_relation:
    supplies:
    - trajectory object schema
    - sedimentation fields
    - competing construction status
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may require sedimentation-related declarations; it cannot determine whether historical
      load is substantively sufficient.
  appendix_migration:
    retain_in_chapter:
    - trajectory criteria
    - false trajectory conditions
    - minimal trajectory record
    migrate:
    - expanded operator-combination tests to Appendix J
    - trajectory case sets to Appendix M
    - notation to Appendix B
  completion_test:
  - A trajectory requires more than duration and chronology.
  - Sedimentation is tied to specified operator combinations and praxis effects.
  - Directionality is explicitly non-teleological.
  - Competing trajectory constructions remain possible.
  - No target function is assigned in this chapter.
```

---

## Chapter 12 — Path Dependence and Sedimentation

```yaml
chapter:
  number: '12'
  title: Path Dependence and Sedimentation
  role_in_work:
    primary_function: Specify path dependence as a graded property of historical determination rather than a separate
      object class.
    canonical_status: Primary PATH definition site for weak order dependence, strong path dependence, and the operator
      combinations that carry sedimented load.
    handoff: Provides Chapter 13 and Chapter 15 with a testable account of how prior sequence changes current costs,
      meanings, and reachability.
  governing_question: How can historical dependence be established without converting history into determinism?
  required_claim:
    core: Path dependence is present where current meaning, costs, roles, or continuation possibilities cannot be
      adequately reconstructed without the prior path.
    graded_rule: Order dependence, trajectory, and strong path dependence are distinct; not every trajectory is strongly
      path-dependent.
    operator_rule: Strong forms require traceable combinations such as Α+Θ, Ω+Θ, Ψ+Θ, or Λ+Θ; Θ alone is insufficient.
  required_distinctions:
  - path dependence as property versus trajectory as object
  - weak order dependence versus strong dependence
  - historical load versus determinism
  - sedimentation versus repetition alone
  - recontextualization versus reset
  - modifier versus erasure
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 10 path
    - Chapter 11 trajectory
    operator_dependencies:
    - Α + Θ
    - Ω + Θ
    - Ψ + Θ
    - Λ + Θ
    later_use:
    - Chapter 13 lost alternatives
    - Chapter 15 trajectory claims
    - Chapter 24 decomposition of dependence
  must_not_claim:
  - Every trajectory is strongly path-dependent.
  - Duration or repetition alone establishes dependence.
  - Historical load makes alternatives impossible.
  - Χ, Σ, Ψ, or Φ resets the path.
  - Path dependence is fate, essence, or causal necessity.
  required_example:
    minimal_case: Hold the present configuration approximately constant while varying the prior path and show changed
      costs, roles, or credibility.
    restriction: Counterfactual variation must remain source-bounded.
  required_counterpressure:
  - The present may be adequately reconstructed without detailed history.
  - A long history may add no discriminative load.
  - New events can change a path without erasing its prior consequences.
  redundancy_guard:
    defines_here:
    - path dependence as property
    - weak and strong forms
    - operator-combination load
    - path-dependence test and failure
    references_only:
    - trajectory definition from Chapter 11
    - branch and alternative details from Chapter 13
    - general counterfactual theory from Chapter 46
    must_not_duplicate:
    - Chapter 11 trajectory object
    - Chapter 46 system-wide counterfactual sensitivity
  model_relation:
    supplies:
    - path-dependence claim fields
    - strength/status classes
    - failure and claim-reduction rules
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can record the claimed historical dependencies and test fields; it cannot prove causal
      necessity.
  appendix_migration:
    retain_in_chapter:
    - graded dependence criteria
    - operator-combination logic
    - test questions
    - failure conditions
    migrate:
    - extended stress tests to Appendix J
    - counterfactual forms to Appendix G
    - case index material to Appendix M
  completion_test:
  - Path dependence remains a property, not a new primitive.
  - Weak and strong dependence are distinguishable.
  - Θ alone is explicitly insufficient.
  - Determinism and teleology are rejected.
  - Failure to establish dependence can reduce a claim to path or trajectory.
```

---

## Chapter 13 — Branches, Aborts, Delays, and Unavailable Alternatives

```yaml
chapter:
  number: '13'
  title: Branches, Aborts, Delays, and Unavailable Alternatives
  role_in_work:
    primary_function: Preserve the alternative space that makes realized paths selective rather than retrospectively
      linear.
    canonical_status: Primary PATH definition site for branch points, realized, rejected, blocked, aborted, deferred,
      and lost alternatives, and source-bounded counterfactual paths.
    handoff: Supplies Chapter 14 and Chapter 15 with alternative structures that composition must preserve or disclose
      as loss.
  governing_question: Which unrealized continuations were genuinely available, and how did selection, blockage, delay,
    or loss shape the realized path?
  required_claim:
    core: Alternative-space claims are valid only where earlier availability, temporal window, blocking structure,
      and later reachability are source-supported.
    selection_rule: Realized paths are intelligible relative to relevant alternatives, including non-selection and
      delay.
    loss_rule: COMPOSE must disclose compression or disappearance of material alternatives.
  required_distinctions:
  - available alternative versus imagined counterfactual
  - rejected versus blocked branch
  - aborted versus never-begun path
  - deferred versus uninterrupted continuation
  - lost alternative versus currently unattractive option
  - non-selection versus absence of decision context
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 10 path
    - Chapter 12 path dependence
    handoff:
    - Feeds Chapter 15 selection and Chapter 16 boundary tests.
    source_constraint:
    - Availability must be supported at the historical decision point.
  must_not_claim:
  - Every imaginable alternative was available.
  - Retrospective plausibility establishes historical reachability.
  - Blocked and impossible are equivalent.
  - Delay leaves the path unchanged.
  - Unrealized alternatives prove what would have happened.
  required_example:
    minimal_case: At one branch point classify one realized, one rejected, one blocked, and one later-lost continuation
      with evidence status.
    restriction: No free counterfactual storytelling.
  required_counterpressure:
  - The source may support the realized branch but not the alternative space.
  - A deferred path may become structurally different during delay.
  - Non-selection may close alternatives without a positive decision event.
  redundancy_guard:
    defines_here:
    - branch and alternative classes
    - availability and temporal-window criteria
    - alternative status record
    - alternative-space compression
    references_only:
    - general path variants from Chapter 10
    - non-event detail from Chapter 14
    - COMPOSE loss mechanics from Chapter 15
    - general counterfactual limits from Chapter 46
    must_not_duplicate:
    - Chapter 10 blocked/aborted/deferred path overview
    - Chapter 46 general counterfactual sensitivity
  model_relation:
    supplies:
    - alternative record fields
    - availability status classes
    - source-support and later-reachability fields
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may validate that availability and evidence status were declared; it cannot establish historical
      possibility from syntax.
  appendix_migration:
    retain_in_chapter:
    - branch taxonomy
    - source-bounded counterfactual rule
    - alternative status record
    migrate:
    - large counterfactual case sets to Appendix G
    - confusion patterns to Appendix I
    - case index to Appendix M
  completion_test:
  - Every alternative claim names its historical window and source basis.
  - Blocked, rejected, aborted, deferred, and lost remain distinct.
  - Non-selection can be represented as praxis structure.
  - Alternative compression is disclosed.
  - Counterfactual paths remain bounded and non-predictive.
```

---

## Chapter 14 — Non-Events within Paths and Trajectories

```yaml
chapter:
  number: '14'
  title: Non-Events within Paths and Trajectories
  role_in_work:
    primary_function: Operationalize Λ within temporal composition without converting missing information or ordinary
      absence into structured non-events.
    canonical_status: Primary PATH definition site for expectation-grounded non-events, repeated non-decision, missing
      repair, missing exit, and non-event sedimentation.
    handoff: Supplies Chapter 15 with Λ structures that must remain visible through composition.
  governing_question: When does an absence become a path-forming non-event, and how can its temporal load be preserved?
  required_claim:
    core: A non-event is a frame- and expectation-bound non-realization that makes a warranted difference to transitions,
      alternatives, costs, roles, or sedimentation.
    preservation_rule: COMPOSE may compress a non-event but may not translate it into positive event language or infer
      it from missing records.
    source_rule: Expectation frame and expected window must be supported.
  required_distinctions:
  - non-event versus absence
  - non-event versus missing source
  - delay as Λ versus delay as observed event chain
  - non-decision versus refusal
  - missing repair versus undefined duty
  - missing exit versus person-level motive
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 9 transition
    - Chapter 10 path
    - Chapter 13 alternatives
    operator_basis:
    - Λ
    - Λ + Θ
    - possible Α/Ω/Ψ interactions
    later_use:
    - Chapter 15 COMPOSE
    - Chapter 23 SUB decomposition
  must_not_claim:
  - Every absence is Λ.
  - Missing data proves non-occurrence.
  - Every delay is intentional.
  - A non-event can be decomposed into positive events with no remainder.
  - Non-event structure licenses blame or person attribution.
  required_example:
    minimal_case: A documented expected decision repeatedly fails to occur; reconstruct the expectation frame, window,
      persistence, affected alternatives, and costs.
    restriction: Keep agency and blame underdetermined unless independently supported.
  required_counterpressure:
  - An alleged central non-event may fail because no expectation frame existed.
  - Positive sub-events may coexist with preservation of the higher-level non-event.
  - Repeated non-events may shape a trajectory more than isolated events.
  redundancy_guard:
    defines_here:
    - PATH-specific non-event logic
    - expectation-frame requirements
    - non-event sedimentation
    - false non-event
    - minimal non-event record
    references_only:
    - foundational non-event definition from Chapter 3
    - branch classification from Chapter 13
    - SUB internal non-event decomposition from Chapter 23
    - source limits from Chapter 49
    must_not_duplicate:
    - Chapter 3 general definition
    - Chapter 23 decomposition mechanics
    - Chapter 49 missing source distinction
  model_relation:
    supplies:
    - non-event record fields
    - expectation support fields
    - false-non-event failure class
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may require expectation and source fields; it cannot infer a normatively binding expectation
      or hidden intention.
  appendix_migration:
    retain_in_chapter:
    - expectation-grounded definition
    - preservation rules
    - false non-event criteria
    - minimal record
    migrate:
    - expanded Λ patterns to Appendix J
    - record template detail to Appendix D
    - countercases to Appendix I
  completion_test:
  - Absence, missing source, and non-event remain separate.
  - Expectation frame and expected window are mandatory.
  - Λ survives composition as Λ.
  - Person blame is not inferred.
  - False non-event and claim reduction remain available.
```

---

<a id="chapter-15-compose-selection-formation-and-compression"></a>

## Chapter 15 — COMPOSE: Selection, Formation, and Compression

```yaml
chapter:
  number: '15'
  title: 'COMPOSE: Selection, Formation, and Compression'
  role_in_work:
    primary_function: Provide the complete PATH-specific operationalization of COMPOSE.
    canonical_status: Primary procedure site for source selection, temporal ordering, formation, preservation, compression,
      exclusion, irrecoverable loss, target object, and composition claims.
    handoff: Produces admissible or failed sequence, path, trajectory, and path-dependence objects for Chapter 16
      boundaries, Chapter 17 cases, SUB, and RETYPE.
  governing_question: Under what conditions may multiple or sequential structures be composed into a new analytical
    object?
  required_claim:
    core: COMPOSE forms a new composite analytical object from selected, ordered source structures while disclosing
      formation rule, traceable load, and information loss.
    identity_rule: The new composite does not retroactively change the origin types of its components.
    retype_boundary: COMPOSE does not itself assign frame-, macro-event-, attractor-, or other target functions.
  required_distinctions:
  - selection versus discovery
  - temporal ordering versus narrative sequencing
  - formation versus aggregation
  - preserved versus compressed versus excluded versus irrecoverable
  - composite object versus contextual target function
  - composition claim versus path-dependence claim
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapters 9–14
    kernel:
    - PMS_STRATA_Operation_Signatures_Minified.md
    later_use:
    - Chapter 16
    - Chapter 17
    - SUB Chapter 24
    - RETYPE Chapters 31–34
  must_not_claim:
  - COMPOSE is lossless addition.
  - Any chronology can be composed into a path.
  - A macro-label is sufficient target formation.
  - Composition automatically establishes trajectory or path dependence.
  - COMPOSE assigns a higher-level operator function.
  - The composite inherits more authority.
  required_example:
    minimal_case: Compose configurations and transitions into a trajectory with explicit selection, ordering, formation,
      preserved load, compressed detail, excluded material, and irrecoverable loss.
    restriction: Include at least one alternative composition or no-composition option.
  required_counterpressure:
  - Removing a claimed constitutive transition may leave the target label unchanged, exposing overelasticity.
  - A composition may preserve chronology but destroy asymmetry or non-event load.
  - The correct result may be sequence, reduced path claim, stop, or non-capture.
  redundancy_guard:
    defines_here:
    - complete COMPOSE procedure
    - PATH-specific source and target objects
    - composition loss accounting
    - composition claims and failure
    - COMPOSE record
    references_only:
    - generic operation identity from Chapter 4
    - system-wide loss concepts from Chapter 48
    - RETYPE target functions
    - formal registry fields
    must_not_duplicate:
    - Chapter 4 operation definition
    - Chapter 48 general loss ontology
    - Chapter 30 PROJECT_AS procedure
  model_relation:
    supplies:
    - COMPOSE registry fields
    - selection and formation validation
    - counterfactual composition test
    - PATH output mappings
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may validate declarations and output mapping; it cannot determine whether the selected
      history is substantively best.
  appendix_migration:
    retain_in_chapter:
    - preconditions
    - selection/order/formation rules
    - loss categories
    - failure conditions
    - COMPOSE record
    migrate:
    - full record template to Appendix D
    - pattern catalogue to Appendix H
    - case files to Appendix M
  completion_test:
  - Source objects and target object are typed.
  - Selection, ordering, and formation rules are distinct.
  - Loss categories are complete.
  - Counterfactual sensitivity is applied to constitutive elements.
  - COMPOSE does not pre-empt PROJECT_AS.
  - Failure, reduction, stop, and non-capture map to canonical outputs.
```

---

## Chapter 16 — PATH Boundary Conditions

```yaml
chapter:
  number: '16'
  title: PATH Boundary Conditions
  role_in_work:
    primary_function: Apply the Admissibility Band and local anti-immunization rules to PATH and COMPOSE.
    canonical_status: Primary PATH site for chronology below the lower boundary, macro-labels above the upper boundary,
      temporal compression, teleology, omitted Λ/Ω load, and PATH-specific stop/non-capture.
    handoff: Defines the local gate that Chapter 17 cases and audit must enforce.
  governing_question: Where does temporal reconstruction become too weak to count as PATH or too abstract to retain
    a traceable path?
  required_claim:
    core: PATH is admissible only where temporal differentiation creates praxeological purchase and composition remains
      traceable to configurations, transitions, non-events, asymmetries, alternatives, and historical load.
    lower_boundary: Chronology or detail without trajectory gain falls below the Relevance Floor.
    upper_boundary: A trajectory or macro-label without reconstructible path load exceeds the Traceability Ceiling.
  required_distinctions:
  - lower boundary versus upper boundary
  - chronology without gain versus trajectory without trace
  - compression versus punctualization
  - directionality versus teleology
  - PATH versus SUB
  - PATH versus RETYPE
  - stop versus non-capture
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapters 9–15
    limits:
    - Chapter 6 Admissibility Band
    handoff:
    - Constrains Chapter 17 and later LIMITS consolidation.
  must_not_claim:
  - More dates automatically strengthen PATH.
  - Longer time range increases explanatory authority.
  - A macro-label can replace path trace.
  - Omitted asymmetry or non-events are harmless detail loss.
  - A RETYPE claim can be made inside PATH.
  - Moving to SUB or RETYPE erases a failed PATH claim.
  required_example:
    minimal_case: Contrast an admissible trajectory, a chronology below the floor, and a macro-label above the ceiling
      using the same broad materials.
    restriction: Show claim reduction and mandatory stop where appropriate.
  required_counterpressure:
  - A path may remain provisional because order is uncertain.
  - A trajectory may be inadmissible because alternatives and local reversals are erased.
  - Non-capture may be superior to forced periodization.
  redundancy_guard:
    defines_here:
    - PATH-specific lower and upper boundaries
    - temporal compression and teleology failures
    - PATH/SUB/RETYPE boundaries
    - PATH stop and non-capture
    references_only:
    - general admissibility definition from Chapter 6
    - full LIMITS systematization Chapters 41–53
    - case catalogue Chapter 17
    must_not_duplicate:
    - Chapter 6 common gate logic
    - Chapter 41–53 integrated limits
  model_relation:
    supplies:
    - PATH boundary decision branches
    - PATH stop triggers
    - PATH-specific failure mappings
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can flag missing trace fields and boundary statuses; it cannot judge historical salience
      automatically.
  appendix_migration:
    retain_in_chapter:
    - local boundary rules
    - purchase and trace tests
    - stop/non-capture conditions
    migrate:
    - expanded boundary tests to Appendix G
    - invalid patterns to Appendix H
    - confusion cases to Appendix I
  completion_test:
  - Both PATH boundaries are explicit and non-compensatory.
  - Teleology and excessive compression are separately testable.
  - PATH is separated from SUB and RETYPE.
  - Stop and Non-Capture have distinct triggers.
  - A level change cannot rescue a failed path claim.
```

---

## Chapter 17 — PATH Cases, Countercases, and Local Audit

```yaml
chapter:
  number: '17'
  title: PATH Cases, Countercases, and Local Audit
  role_in_work:
    primary_function: Demonstrate and audit the full PATH discipline through positive, negative, and confusion cases.
    canonical_status: Primary PATH site for case architecture, local audit, PATH-specific outputs, and lock decision.
    handoff: Closes PATH and produces tested path/trajectory objects and failure records for SUB, RETYPE, LIMITS,
      and the integrated case pass.
  governing_question: Can PATH distinguish valid temporal composition from chronology, teleology, overcompression,
    false non-events, and premature projection?
  required_claim:
    core: PATH is locally complete only when its rules produce discriminating positive, counter, and confusion cases
      and map their results to canonical output classes.
    artifact_rule: Lock-critical cases require Markdown reconstruction, YAML record, admissibility result, and output-class
      mapping.
    closure_rule: PATH closes without assigning later contextual functions.
  required_distinctions:
  - case versus countercase versus confusion case
  - local result versus canonical output class
  - admissible path versus admissible trajectory versus path-dependence claim
  - failed composition versus mandatory stop versus non-capture
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapters 9–16
    case_requirements:
    - admissible trajectory composition
    - macro-label without traceable path
    - path versus projection confusion
    handoff:
    - PATH Lock to SUB and RETYPE.
  must_not_claim:
  - One successful case validates PATH globally.
  - Cases may omit loss or alternative records.
  - A trajectory case may silently claim a frame-function.
  - Countercases are merely illustrations rather than tests.
  - Non-capture is a disguised failure class.
  required_example:
    minimal_case: Include at least the three lock-critical cases and one weak-path-dependence counterpressure.
    artifact_set:
    - Markdown case
    - YAML record
    - local audit result
    - canonical output mapping
  required_counterpressure:
  - Chronology presented as path.
  - Teleological composition.
  - Composition through omitted asymmetry.
  - False central non-event.
  - Path versus resolution drift.
  - Trajectory versus attractor-function.
  redundancy_guard:
    defines_here:
    - PATH case architecture
    - PATH local audit
    - PATH result taxonomy and canonical mapping
    - PATH lock decision
    references_only:
    - definitions from Chapters 9–16
    - system-wide audit from Chapter 53
    - full case index Appendix M
    must_not_duplicate:
    - re-deriving operation or boundary theory
    - integrated multi-operation audit
  model_relation:
    supplies:
    - PATH audit checklist fields
    - case validation expectations
    - output mapping
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can validate record completeness and declared output class; it cannot replace expert case
      interpretation.
  appendix_migration:
    retain_in_chapter:
    - minimum lock cases
    - local audit
    - output mapping
    - closing statement
    migrate:
    - full case narratives to 03_cases/markdown
    - YAML records to 03_cases/yaml
    - index to Appendix M
    - audit form to Appendix N
  completion_test:
  - All required case classes are assigned.
  - At least three lock-critical cases are fully instantiated.
  - Every case includes loss, alternatives, admissibility, and claim scope.
  - PATH-specific outputs map to canonical outputs.
  - PATH closes without target-function claims.
  - The PATH local audit passes.
```

---

## Chapter 18 — The Provisionally Compressed Object

```yaml
chapter:
  number: '18'
  title: The Provisionally Compressed Object
  role_in_work:
    primary_function: Define the source object and justification required before any SUB operation begins.
    canonical_status: Primary SUB definition site for provisional elementarity, compressed object, reasons to decompose
      or not decompose, and source-function preservation.
    handoff: Supplies Chapter 19 and Chapter 20 with a bounded source reference rather than an assumed hidden microstructure.
  governing_question: What may legitimately be treated as a compressed object, and what warrants opening it?
  required_claim:
    core: An object is only provisionally elementary relative to frame, granularity, claim, and source access; it
      is never declared ontologically indivisible.
    source_rule: SUB opens operator-typed occurrences and composites, not Δ–Ψ operator types.
    preservation_rule: The source object and its coarser function remain the reconstruction target unless explicitly
      revised or rejected.
  required_distinctions:
  - provisional elementarity versus ontological indivisibility
  - compression versus error
  - operator type versus decomposable occurrence
  - reason to decompose versus curiosity or detail appetite
  - source preservation versus source immunization
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    conditional:
    - PATH Lock for path and trajectory source objects
    handoff:
    - Chapter 19 granularity relation
    - Chapter 20 DECOMPOSE procedure
  must_not_claim:
  - Every object has a final true decomposition.
  - Compression is inherently defective.
  - Operator types can be decomposed as empirical aggregates.
  - More detail is automatically preferable.
  - A counterexample always warrants finer resolution.
  required_example:
    minimal_case: Take a stable frame-typed occurrence and state what is known, compressed, unresolved, and why decomposition
      may alter the claim.
    restriction: Do not yet enumerate components as if already discovered.
  required_counterpressure:
  - The correct decision may be not to decompose.
  - Sources may not support an internal reconstruction.
  - A coarse source function can remain analytically preferable.
  redundancy_guard:
    defines_here:
    - provisional elementarity
    - compressed source object
    - reasons to decompose/not decompose
    - preservation requirement
    - minimal source declaration
    references_only:
    - general object model from Chapter 1
    - granularity mechanics Chapter 19
    - DECOMPOSE procedure Chapter 20
    must_not_duplicate:
    - Chapter 1 object categories
    - Chapter 20 operational fields
    - Chapter 25 resolution outcomes
  model_relation:
    supplies:
    - compressed-object input schema
    - decomposition-reason field
    - source-function preservation requirement
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can require a source declaration and decomposition reason; it cannot infer hidden components.
  appendix_migration:
    retain_in_chapter:
    - source-object criteria
    - provisional elementarity
    - preservation requirement
    - minimal source declaration
    migrate:
    - expanded source-object types to Appendix A
    - record details to Appendix E
    - non-operator remainder issues to Appendix L
  completion_test:
  - Operator types remain non-decomposable.
  - The source object, frame, granularity, level, function, and uncertainty are declared.
  - Reasons not to decompose remain legitimate.
  - Coarse function is preserved as a test target, not immunized.
```

---

## Chapter 19 — Granularity Change and the Logic of Decomposition

```yaml
chapter:
  number: '19'
  title: Granularity Change and the Logic of Decomposition
  role_in_work:
    primary_function: Define the coordinate change that makes DECOMPOSE a granularity operation rather than a frame
      change, metaphor, or truth descent.
    canonical_status: Primary SUB definition site for finer granularity, relative downward movement, functional components,
      comparability, mismatch, and minimal granularity relation.
    handoff: Supplies Chapter 20 with a declared source-to-target granularity relation.
  governing_question: What exactly changes when a source object is reconstructed at finer resolution?
  required_claim:
    core: Granularity change alters the distinction set and resolution while preserving a declared relation to the
      same source reference; it is not a descent toward deeper truth.
    frame_rule: A frame change may accompany decomposition but must be separately declared and is not itself DECOMPOSE.
    component_rule: Relevant components are relationally or functionally tied to the source object; fragments alone
      do not count.
  required_distinctions:
  - granularity versus frame
  - finer resolution versus deeper truth
  - relative downward movement versus ontological lower layer
  - functional component versus fragment
  - local versus distributed part
  - granularity mismatch versus substantive contradiction
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 18 source object
    handoff:
    - Chapter 20 DECOMPOSE signature
    - Chapter 25 resolution classification
    coordinate_basis:
    - Chapter 2 frame/granularity/relative level
  must_not_claim:
  - Finer granularity reveals ultimate constituents.
  - Every frame change is decomposition.
  - Parts must be spatially contained.
  - Micro evidence automatically entails macro conclusions.
  - A level mismatch automatically resolves disagreement.
  required_example:
    minimal_case: Open the same source object at a finer distinction set while keeping frame stable, then contrast
      a separate frame-change case.
    restriction: State expected praxis difference before analysis.
  required_counterpressure:
  - A finer reconstruction may be neutral or worse for the current claim.
  - Two decompositions may be incomparable because their frames or temporal scopes differ.
  - A detailed fragment may have no source-function relevance.
  redundancy_guard:
    defines_here:
    - granularity-change logic
    - relative downward movement
    - functional component criteria
    - comparability and mismatch
    - minimal granularity relation
    references_only:
    - Chapter 2 coordinate definitions
    - Chapter 20 DECOMPOSE procedure
    - Chapter 25 outcome classes
    - Chapter 43 no resolution privilege
    must_not_duplicate:
    - redefining frame, level, or granularity
    - full resolution boundary theory
  model_relation:
    supplies:
    - granularity relation fields
    - comparability status
    - frame-preservation flag
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may validate declared coordinates and comparability fields; it cannot rank granularities
      by truth.
  appendix_migration:
    retain_in_chapter:
    - granularity relation
    - component criteria
    - comparability conditions
    migrate:
    - formal notation to Appendix B
    - comparative examples to Appendix I
    - boundary tests to Appendix G
  completion_test:
  - Source and target granularities are explicit.
  - Frame preservation or change is marked.
  - Functional components are distinguished from fragments.
  - No epistemic privilege is assigned to finer resolution.
  - Comparability limits are explicit.
```

---

## Chapter 20 — DECOMPOSE: Conditions, Procedure, and Preservation Requirements

```yaml
chapter:
  number: '20'
  title: 'DECOMPOSE: Conditions, Procedure, and Preservation Requirements'
  role_in_work:
    primary_function: Provide the complete SUB-specific operationalization of DECOMPOSE.
    canonical_status: Primary procedure site for decomposition question, expected difference, component and relation
      identification, source support, source-function testing, loss, and outputs.
    handoff: Produces finer reconstructions for Chapters 21–28 and possible source traces for RETYPE.
  governing_question: Under what conditions may a compressed occurrence or composite be reconstructed through finer
    relational structures?
  required_claim:
    core: DECOMPOSE is the controlled reconstruction of a provisionally compressed source object as a relational organization
      of finer structures under declared granularity.
    preservation_rule: The source function may be confirmed, refined, differentiated, partially preserved, rejected,
      or left underdetermined; preservation is not immunity.
    non_invertibility: DECOMPOSE(COMPOSE(X)) does not restore X.
  required_distinctions:
  - component identification versus relation reconstruction
  - source support versus plausible internal model
  - preserved versus revised versus rejected source function
  - decomposition versus description
  - decomposition versus new PATH
  - decomposition versus PROJECT_AS
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapters 18–19
    kernel:
    - PMS_STRATA_Operation_Signatures_Minified.md
    later_use:
    - Chapters 21–28
    - RETYPE source trace
  must_not_claim:
  - DECOMPOSE acts on operator types.
  - A list of parts is sufficient.
  - Source function must always survive.
  - New details can be inferred from the coarse label.
  - The operation is lossless or inverse to COMPOSE.
  - Finer output inherits more authority.
  required_example:
    minimal_case: Decompose a trajectory or occurrence into supported components and relations, then classify the
      coarser source function.
    restriction: Include a no-gain or unsupported alternative.
  required_counterpressure:
  - The source function may fail under finer evidence.
  - Components may be replaceable rather than constitutive.
  - The operation may end as resolution-neutral, mandatory stop, or non-capture.
  redundancy_guard:
    defines_here:
    - complete DECOMPOSE procedure
    - source support
    - component and relation reconstruction
    - source-function outcomes
    - non-invertibility
    - DECOMPOSE record
    references_only:
    - generic identity from Chapter 4
    - source object Chapter 18
    - granularity relation Chapter 19
    - resolution outcomes Chapter 25
    - system-wide loss Chapter 48
    must_not_duplicate:
    - general object and coordinate definitions
    - full boundary conditions Chapter 27
  model_relation:
    supplies:
    - DECOMPOSE registry fields
    - component relation checks
    - source-function outcome mapping
    - source-support status
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may validate that components, relations, granularity, and source-function status were declared;
      it cannot discover actual constituents.
  appendix_migration:
    retain_in_chapter:
    - preconditions and procedure
    - source-function outcome classes
    - failure conditions
    - record
    migrate:
    - full record template to Appendix E
    - valid/invalid patterns to Appendix H
    - case files to Appendix M
  completion_test:
  - The source object and decomposition question are explicit.
  - Components and relations are both reconstructed.
  - Source support and uncertainty are disclosed.
  - Source function can be confirmed or rejected.
  - Non-invertibility is preserved.
  - Outputs map to canonical classes.
```

---

## Chapter 21 — Decomposing Operator-Typed Occurrences

```yaml
chapter:
  number: '21'
  title: Decomposing Operator-Typed Occurrences
  role_in_work:
    primary_function: Apply DECOMPOSE to concrete occurrences typed through PMS operators while protecting the operator
      grammar itself.
    canonical_status: Primary SUB site for frame-, attractor-, asymmetry-, impulse-, and binding-typed occurrence
      decomposition.
    handoff: Provides Chapter 22 with occurrence-level patterns and Chapter 28 with lock-critical cases.
  governing_question: How can a concrete operator-typed occurrence be opened without treating the operator type as
    a material aggregate?
  required_claim:
    core: SUB reconstructs the practices, relations, temporalities, and conditions that produce or maintain an occurrence
      typed through an operator; the operator type remains unchanged.
    variation_rule: Stable coarse function may coexist with internal variation, conflict, unequal reproduction work,
      or component substitution.
    failure_rule: Finer evidence may revise or reject the occurrence typing.
  required_distinctions:
  - operator type versus occurrence
  - function versus production conditions
  - stable function versus internal homogeneity
  - dynamic attractor occurrence versus later attractor-function
  - distributed asymmetry versus macroprojection
  - binding occurrence versus person property
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 20
    operator_basis:
    - □
    - Α
    - Ω
    - ∇
    - Ψ and other occurrence types as needed
    handoff:
    - Chapter 22 composites
    - Chapter 26 SUB/RETYPE boundary
  must_not_claim:
  - The operator itself is composed of the observed parts.
  - Every internal feature must match the coarse type.
  - Dynamic attractor occurrence is already a higher-level attractor-function.
  - Occurrence decomposition licenses person typing.
  - Stable function proves homogeneous internal structure.
  required_example:
    minimal_case: Decompose one frame-typed or attractor-typed occurrence into reproduction practices, roles, non-events,
      temporal thresholds, and source-function effects.
    restriction: Preserve the distinction between occurrence and operator type.
  required_counterpressure:
  - A coarse typing may be undermined by finer evidence.
  - Different internal configurations may sustain the same coarse function.
  - Local asymmetries may fail to form a coordinated macro-asymmetry.
  redundancy_guard:
    defines_here:
    - occurrence-specific decomposition logic
    - representative operator-typed families
    - stable function with internal variation
    - operator-decomposition error
    references_only:
    - operator definitions from PMS.yaml
    - generic DECOMPOSE procedure Chapter 20
    - higher-level functions RETYPE Chapter 34
    must_not_duplicate:
    - redefining any Δ–Ψ operator
    - full composite decomposition Chapter 22
    - projection claims
  model_relation:
    supplies:
    - occurrence subtype fields
    - operator-type protection rule
    - source-function revision flags
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may record occurrence typing and component evidence; it cannot validate the substantive
      PMS typing automatically.
  appendix_migration:
    retain_in_chapter:
    - general rule
    - representative occurrence families
    - failure pattern
    migrate:
    - expanded operator-family stress tests to Appendix J
    - case details to Appendix M
    - operator index links to 04_reference
  completion_test:
  - Operator type and occurrence remain distinct in every example.
  - At least three occurrence families are operationalized.
  - Internal variation does not imply automatic failure or success.
  - Finer evidence can revise the source type.
  - No person property or new operator is created.
```

---

## Chapter 22 — Decomposing Composite Structures

```yaml
chapter:
  number: '22'
  title: Decomposing Composite Structures
  role_in_work:
    primary_function: Specify relational decomposition of already-composite objects without atomistic fragmentation.
    canonical_status: Primary SUB site for component hierarchy, distributed function, redundancy, substitution, internal
      conflict, operator weighting, modulation profiles, and composite stability.
    handoff: Supplies Chapters 24–25 and RETYPE Chapter 34 with traceable component relations.
  governing_question: How can a composite be opened while retaining the relations that make it a composite?
  required_claim:
    core: A valid composite decomposition reconstructs constitutive, modulating, replaceable, compensatory, and incidental
      components together with their dependencies and temporal relations.
    stability_rule: Macro-stability may result from dynamic compensation, repair, redundancy, or unequal load rather
      than stable parts.
    profile_rule: Operator weighting and modulating profiles remain descriptions of existing operator relations, not
      new operators or person types.
  required_distinctions:
  - component versus fragment
  - constitutive versus modulating versus replaceable component
  - distributed function versus aggregation
  - macro-stability versus internal homogeneity
  - operator weighting versus operator replacement
  - modulating profile versus type
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 20
    - Chapter 21
    later_use:
    - Chapter 24 path/trajectory decomposition
    - Chapter 34 higher-level functions
    - Chapter 35 profiles
  must_not_claim:
  - A parts list is a decomposition.
  - Every component is equally constitutive.
  - Stable macrofunction requires stable local parts.
  - Operator weighting changes PMS dependencies.
  - A profile is a new primitive or person type.
  - Internal conflict automatically destroys the composite.
  required_example:
    minimal_case: Open a distributed composite with one constitutive, one replaceable, one compensatory, and one incidental
      component, including an internal conflict.
    restriction: Explain how the coarse function persists or changes.
  required_counterpressure:
  - Removing one component may not alter the function because of redundancy.
  - Internal conflict may be integrated, suppressed, destabilizing, or residual.
  - A coarse function may disappear if relations, not parts, are lost.
  redundancy_guard:
    defines_here:
    - component hierarchy
    - distributed and redundant function
    - internal conflict and stability
    - operator weighting and profiles
    - fragmentation failure
    references_only:
    - generic component procedure Chapter 20
    - occurrence families Chapter 21
    - higher-level projection RETYPE Chapters 34–35
    must_not_duplicate:
    - RETYPE projection of composites
    - full source/traceability ceiling theory
  model_relation:
    supplies:
    - component-role classes
    - relation map fields
    - redundancy/substitution status
    - profile anti-type flag
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can record component roles and relations; it cannot determine emergent function from enumeration
      alone.
  appendix_migration:
    retain_in_chapter:
    - relational composite logic
    - component roles
    - stability and conflict
    - profile boundary
    migrate:
    - detailed composition maps to Appendix E
    - profile stress tests to Appendix J
    - remainder cases to Appendix L
  completion_test:
  - Parts and relations are jointly represented.
  - Component roles are distinguishable.
  - Redundancy and substitution are testable.
  - Internal conflict has multiple possible outcomes.
  - Operator weighting creates no new operator.
  - The source composite remains reconstructible.
```

---

## Chapter 23 — Decomposing Events, Non-Events, and Internal Temporal Structures

```yaml
chapter:
  number: '23'
  title: Decomposing Events, Non-Events, and Internal Temporal Structures
  role_in_work:
    primary_function: Apply DECOMPOSE to event-like and non-event structures while preserving their temporal and categorical
      character.
    canonical_status: Primary SUB site for extended events, event clusters, event inflation, non-event decomposition,
      delay structures, repeated non-decision, and temporal granularity drift.
    handoff: Supplies Chapter 24 with temporal component methods and Chapter 28 with event/non-event cases.
  governing_question: How can temporally extended or apparently punctual structures be opened without inflating events
    or dissolving non-events?
  required_claim:
    core: Events and non-events may contain internal phases, decisions, delays, roles, and blockages, but decomposition
      must preserve what makes the source an event or non-event.
    lambda_rule: Positive sub-events do not erase the higher-level non-realization if the expected structure still
      failed to occur.
    floor_rule: Increasing temporal resolution without new transition or praxis difference is temporal granularity
      drift.
  required_distinctions:
  - punctual versus extended event
  - event cluster versus event inflation
  - non-event versus positive sub-events
  - delay structure versus intentional obstruction
  - internal temporal order versus timestamp multiplication
  - source absence versus Λ
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 14 non-event logic
    - Chapter 20 DECOMPOSE
    later_use:
    - Chapter 24 trajectory decomposition
    - Chapter 25 resolution drift
  must_not_claim:
  - Every micro-change is an event.
  - A non-event disappears once positive sub-events are identified.
  - Delay implies intention.
  - Missing records are non-events.
  - Finer timestamps necessarily improve explanation.
  required_example:
    minimal_case: Decompose an apparently single non-decision into deferrals, role shifts, information bottlenecks,
      and positive sub-events while preserving the expected non-occurrence.
    restriction: State where temporal detail ceases to add purchase.
  required_counterpressure:
  - The event boundary may remain contested.
  - A source may be better treated as an event cluster than one event.
  - The non-event claim may fail if expectation support is absent.
  redundancy_guard:
    defines_here:
    - event and non-event decomposition
    - event inflation
    - internal temporal order
    - temporal drift
    - categorical preservation
    references_only:
    - Chapter 14 PATH non-event role
    - Chapter 20 generic procedure
    - Chapter 25 general resolution outcomes
    - Chapter 49 source limits
    must_not_duplicate:
    - redefining event/non-event generally
    - PATH composition claims
  model_relation:
    supplies:
    - event phase fields
    - non-event preservation flag
    - temporal drift status
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may validate declared phases and expectation fields; it cannot determine the true event
      boundary or intention.
  appendix_migration:
    retain_in_chapter:
    - extended event logic
    - non-event preservation
    - drift and inflation failures
    migrate:
    - temporal notation to Appendix B
    - record details to Appendix E
    - confusion cases to Appendix I
  completion_test:
  - Event and non-event character remain explicit.
  - Positive sub-events do not automatically dissolve Λ.
  - Event inflation has a clear stop rule.
  - Internal temporal order is relationally represented.
  - Missing information remains distinct from non-occurrence.
```

---

## Chapter 24 — Decomposing Paths and Trajectories

```yaml
chapter:
  number: '24'
  title: Decomposing Paths and Trajectories
  role_in_work:
    primary_function: Apply SUB to PATH-produced objects while distinguishing opening the same object from constructing
      a rival path.
    canonical_status: Primary SUB site for subpaths, transition clusters, turning points, branch reconstruction, internal
      frame changes, irrecoverable PATH compression, and decomposition of path-dependence load.
    handoff: Connects PATH outputs to SUB and prepares traceable source structures for RETYPE.
  governing_question: When is a finer temporal reconstruction a decomposition of the same path or trajectory, and
    when is it a new PATH construction?
  required_claim:
    core: A PATH object may be decomposed into subpaths, transition clusters, branches, and operator-combination loads
      only while its source reference and coarser function remain explicit.
    non_inverse: SUB(PATH(X)) is not recovery of an original complete history.
    classification_rule: A new periodization or differently selected path may constitute a rival COMPOSE result rather
      than DECOMPOSE of the same object.
  required_distinctions:
  - same path opened versus new path composed
  - subpath versus fragment
  - turning point versus retrospective label
  - internal frame change versus source replacement
  - decomposition of path dependence versus path dependence as substance
  - irrecoverable compression versus recoverable detail
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - PATH Lock
    - Chapter 20
    path_sources:
    - path
    - trajectory
    - phase
    - turning point
    - branch cluster
    - path-dependence claim
    later_use:
    - Chapter 26 SUB/RETYPE
    - RETYPE Chapters 31–33
  must_not_claim:
  - More chronology is automatically SUB.
  - Every new periodization is decomposition of the same path.
  - The original path can be perfectly recovered.
  - A turning point can be named without source transitions.
  - Path dependence is a hidden substance.
  required_example:
    minimal_case: Open a trajectory into subpaths and transition clusters, then compare a rival periodization that
      should be classified as new PATH.
    restriction: Record irrecoverable compression explicitly.
  required_counterpressure:
  - Finer reconstruction may invalidate the alleged turning point.
  - Competing continuations may prevent a single coherent decomposition.
  - The coarse trajectory function may remain useful despite unrecoverable detail.
  redundancy_guard:
    defines_here:
    - PATH objects as SUB sources
    - subpaths and transition clusters
    - turning-point and branch reconstruction
    - decomposition versus rival PATH
    - non-invertibility
    references_only:
    - PATH definitions Chapters 10–12
    - COMPOSE Chapter 15
    - generic DECOMPOSE Chapter 20
    - RETYPE target functions
    must_not_duplicate:
    - redefining path or trajectory
    - performing PROJECT_AS
    - assuming original data recovery
  model_relation:
    supplies:
    - PATH-source subtype fields
    - same-reference versus rival-path decision branch
    - compression-debt fields
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model may require a source path reference and classification choice; it cannot determine whether
      two periodizations represent the same analytical object.
  appendix_migration:
    retain_in_chapter:
    - classification logic
    - temporal component forms
    - compression debt
    - failed trajectory decomposition
    migrate:
    - complex trajectory cases to Appendix J
    - confusion patterns to Appendix I
    - case records to Appendix M
  completion_test:
  - The same-object versus new-PATH distinction is explicit.
  - Turning points require component transitions.
  - Irrecoverable compression is declared.
  - Path-dependence load can be decomposed without reification.
  - RETYPE claims remain separate.
```

---

## Chapter 25 — Resolution Gain, Neutrality, Drift, and Escape

```yaml
chapter:
  number: '25'
  title: Resolution Gain, Neutrality, Drift, and Escape
  role_in_work:
    primary_function: Classify the outcomes of finer resolution and establish SUB-specific stop markers.
    canonical_status: Primary SUB definition site for resolution gain, neutrality, drift, escape, source overreach,
      calibration loss, decomposition fatigue, and mandatory stop.
    handoff: Supplies Chapters 26–28 and LIMITS with resolution outcome classes.
  governing_question: What result has finer resolution actually produced, and when must decomposition stop?
  required_claim:
    core: Finer resolution counts as gain only when it changes a warranted praxis reconstruction; correct additional
      detail may remain resolution-neutral.
    drift_rule: Complexity without relational or discriminative gain is resolution drift.
    escape_rule: Changing granularity to avoid a counterexample without answering it is resolution escape and preserves
      the original failure.
  required_distinctions:
  - gain versus detail
  - neutrality versus failure
  - drift versus source limitation
  - escape versus warranted revision
  - decomposition fatigue versus analyst psychology
  - source overreach versus bounded inference
  - calibration loss versus open threshold
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapters 18–24
    admissibility:
    - Praxeological Relevance Floor
    - Source Ceiling
    - Anti-Immunization
    handoff:
    - Chapter 27 local boundaries
    - Chapter 28 outputs
  must_not_claim:
  - Any correct detail is resolution gain.
  - Resolution-neutral findings are useless.
  - A finer level can rescue a failed claim automatically.
  - Uncertainty may be represented as precise structure.
  - Analysis should continue while any distinction remains possible.
  required_example:
    minimal_case: Classify four attempts on one source object as gain, neutral, drift, and escape, stating the changed
      or unchanged claim.
    restriction: At least one result must trigger mandatory stop.
  required_counterpressure:
  - A null gain can confirm the adequacy of the coarse claim.
  - New sources may later justify re-entry after stop.
  - A plausible internal model may remain unsupported rather than false.
  redundancy_guard:
    defines_here:
    - resolution outcome classes
    - source overreach
    - calibration loss
    - decomposition fatigue
    - mandatory stop
    references_only:
    - general Admissibility Band Chapter 6
    - source limits Chapter 49
    - anti-immunization Chapter 50
    - stop system Chapter 51
    must_not_duplicate:
    - full system-wide limits
    - redefining relevance floor
  model_relation:
    supplies:
    - resolution result enum
    - stop trigger fields
    - claim-effect mapping
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can require an outcome classification and reason; it cannot decide whether a distinction
      has substantive praxis purchase.
  appendix_migration:
    retain_in_chapter:
    - outcome definitions
    - escape and drift criteria
    - mandatory stop
    migrate:
    - test matrix to Appendix G
    - invalid patterns to Appendix H
    - source/remainder cases to Appendix L
  completion_test:
  - Gain requires a changed warranted reconstruction.
  - Neutrality is distinct from failure.
  - Drift and escape are independently identifiable.
  - Source overreach and calibration loss are explicit.
  - Mandatory stop follows when additional resolution lacks purchase or support.
```

---

## Chapter 26 — The Boundary between SUB and RETYPE

```yaml
chapter:
  number: '26'
  title: The Boundary between SUB and RETYPE
  role_in_work:
    primary_function: Provide the operation-classification rule separating internal reconstruction from external contextual
      function.
    canonical_status: Primary SUB site for DECOMPOSE versus PROJECT_AS, SUB versus recontextualization, dual-operation
      cases, and invalid collapse.
    handoff: Prevents Chapter 28 cases and later RETYPE from inheriting mixed or ambiguous operations.
  governing_question: Is the analysis opening the internal constitution of a source object or assigning that object
    a bounded function in another context?
  required_claim:
    core: DECOMPOSE changes granularity to reconstruct internal source structure; PROJECT_AS preserves the source
      object and assigns a target function in a declared context.
    dual_rule: A case may require both operations, but each requires a separate record, justification, loss account,
      and failure possibility.
    frame_rule: A changed frame without a target function may be recontextualization rather than either operation.
  required_distinctions:
  - internal constitution versus external function
  - granularity change versus target-context change
  - source function as explanation target versus target function as new claim
  - DECOMPOSE versus PROJECT_AS
  - SUB versus recontextualization
  - dual operation versus collapsed operation
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 20
    - Chapter 24
    projection_basis:
    - Chapter 5 origin type and target function
    - Chapter 4 operation distinction
    handoff:
    - Chapter 28 confusion cases
    - RETYPE Chapters 29–30
  must_not_claim:
  - Any new description is DECOMPOSE.
  - Any new frame is PROJECT_AS.
  - A decomposition automatically establishes a target function.
  - One record may silently combine both operations.
  - A new label proves a new function.
  required_example:
    minimal_case: Use one trajectory first as a DECOMPOSE source and then as a PROJECT_AS source, with separate questions
      and outputs.
    restriction: Include a mere recontextualization comparison.
  required_counterpressure:
  - An analysis that looks like SUB may actually assign a target function.
  - An analysis that looks like RETYPE may only summarize internal components.
  - Both operations may independently fail.
  redundancy_guard:
    defines_here:
    - SUB/RETYPE decision test
    - recontextualization boundary
    - dual-operation rule
    - invalid collapse
    references_only:
    - generic operation definitions Chapter 4
    - origin type/target function Chapter 5
    - full RETYPE theory Chapters 29–40
    must_not_duplicate:
    - redefining PROJECT_AS in full
    - performing RETYPE case families
  model_relation:
    supplies:
    - decision-tree branches
    - separate-record requirement
    - operation-confusion flags
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can classify declared operation features and flag mixed records; it cannot always resolve
      ambiguous prose without analyst judgment.
  appendix_migration:
    retain_in_chapter:
    - decision criteria
    - dual operation
    - invalid collapse
    migrate:
    - decision tree examples to Appendix I
    - pattern catalogue to Appendix H
    - record templates to Appendices E–F
  completion_test:
  - Internal structure and external function remain separate claims.
  - Changed granularity and changed target context are distinguishable.
  - Dual operations require separate records.
  - Recontextualization without target function remains possible.
  - Invalid collapse is formally flaggable.
```

---

## Chapter 27 — SUB Boundary Conditions

```yaml
chapter:
  number: '27'
  title: SUB Boundary Conditions
  role_in_work:
    primary_function: Apply the Admissibility Band, source ceiling, type preservation, and anti-immunization locally
      to DECOMPOSE.
    canonical_status: Primary SUB site for lower and upper decomposition boundaries, fragmentation, source ceiling,
      component counterfactual test, coarser-function traceability, stop, and non-capture.
    handoff: Defines the local gate enforced by Chapter 28 cases and later LIMITS.
  governing_question: Where does finer reconstruction fall below praxeological relevance or lose reconstructive anchoring
    to its source object?
  required_claim:
    core: DECOMPOSE is admissible only where added distinctions produce praxis purchase, sources support the finer
      structure, source reference remains identifiable, and the coarser function remains traceable or explicitly revised.
    lower_boundary: Resolution without purchase falls below the Relevance Floor.
    upper_boundary: Fragmentation without source-function reconstruction exceeds the admissible range.
  required_distinctions:
  - lower versus upper SUB boundary
  - detail without purchase versus fragmentation without reconstruction
  - component role versus incidental detail
  - source ceiling versus non-capture
  - type preservation versus source-function confirmation
  - stop versus claim reduction
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapters 18–26
    limits:
    - Chapter 6 Admissibility Band
    handoff:
    - Chapter 28 audit
    - LIMITS consolidation
  must_not_claim:
  - Finer resolution has automatic priority.
  - Component enumeration is sufficient traceability.
  - The source type must survive regardless of evidence.
  - Source limits may be filled by model inference.
  - A finer level erases the original counterexample.
  required_example:
    minimal_case: Compare an admissible decomposition, an overfine neutral/drift case, and a fragmentation case using
      explicit component counterfactual tests.
    restriction: Show one source-function rejection or claim reduction.
  required_counterpressure:
  - The coarser reconstruction may remain preferable.
  - Competing decompositions may be equally supported.
  - Non-capture may follow where no granularity preserves both source function and relevant difference.
  redundancy_guard:
    defines_here:
    - SUB lower and upper boundaries
    - source ceiling
    - counterfactual component test
    - coarser-function traceability
    - type preservation
    - SUB stop and non-capture
    references_only:
    - general gates Chapter 6
    - resolution outcomes Chapter 25
    - system-wide source and stop chapters 49–52
    must_not_duplicate:
    - full LIMITS theory
    - redefining DECOMPOSE
  model_relation:
    supplies:
    - SUB admissibility rule
    - component sensitivity classes
    - source ceiling status
    - stop/non-capture outputs
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can check presence of required gates and statuses; it cannot decide component constitutiveness
      from form alone.
  appendix_migration:
    retain_in_chapter:
    - local admissibility test
    - component sensitivity
    - stop/non-capture
    migrate:
    - test matrices to Appendix G
    - invalid patterns to Appendix H
    - remainder cases to Appendix L
  completion_test:
  - Both SUB boundaries are explicit.
  - Source support and source reference are independent gates.
  - The coarser function can be confirmed or rejected.
  - No fine-resolution privilege is implied.
  - Stop and Non-Capture remain distinct.
  - Granularity escape preserves the original failure.
```

---

## Chapter 28 — SUB Cases, Countercases, and Local Audit

```yaml
chapter:
  number: '28'
  title: SUB Cases, Countercases, and Local Audit
  role_in_work:
    primary_function: Demonstrate and audit the full SUB discipline through positive, negative, and confusion cases.
    canonical_status: Primary SUB site for case architecture, local audit, SUB-specific outputs, and lock decision.
    handoff: Closes SUB and supplies tested finer source traces and failure records to RETYPE, LIMITS, and integrated
      cases.
  governing_question: Can SUB distinguish warranted relational opening from overfine analysis, unsupported microstructure,
    operator decomposition, fragmentation, and operation confusion?
  required_claim:
    core: SUB is locally complete only when its rules generate discriminating positive, counter, and confusion cases
      and map all source-function and resolution outcomes to canonical output classes.
    artifact_rule: Lock-critical cases require Markdown reconstruction, YAML DECOMPOSE record, admissibility result,
      and output-class mapping.
    closure_rule: SUB closes with source coherence preserved or explicitly revised, never with hidden operator decomposition.
  required_distinctions:
  - admissible decomposition versus resolution-neutral result
  - source function refined versus rejected
  - unsupported decomposition versus non-capture
  - SUB versus new PATH
  - SUB versus RETYPE
  - modulator versus new operator
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapters 18–27
    - PATH Lock where path sources are used
    case_requirements:
    - admissible occurrence or trajectory decomposition
    - overfine analysis below Relevance Floor
    - SUB versus RETYPE confusion
    handoff:
    - SUB Lock to RETYPE and LIMITS
  must_not_claim:
  - One positive case validates DECOMPOSE generally.
  - Cases may omit component relations.
  - Operator types may appear as source objects.
  - A failed coarse type must be rescued at finer resolution.
  - Resolution-neutral and non-capture are interchangeable.
  required_example:
    minimal_case: Include at least the three lock-critical cases plus operator-decomposition error and fragmentation
      without source function.
    artifact_set:
    - Markdown case
    - YAML record
    - local audit result
    - canonical output mapping
  required_counterpressure:
  - Unsupported internal structure.
  - Resolution escape.
  - False macro-asymmetry.
  - SUB versus new PATH.
  - Decomposition versus analogy.
  - Modulator versus new operator.
  redundancy_guard:
    defines_here:
    - SUB case architecture
    - SUB local audit
    - SUB result taxonomy and canonical mapping
    - SUB lock decision
    references_only:
    - definitions from Chapters 18–27
    - system-wide audit Chapter 53
    - full case index Appendix M
    must_not_duplicate:
    - re-deriving DECOMPOSE or admissibility theory
    - performing RETYPE in the same record
  model_relation:
    supplies:
    - SUB audit checklist fields
    - case completeness expectations
    - source-function and resolution output mapping
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can validate record completeness and output mapping; it cannot substitute for substantive
      component analysis.
  appendix_migration:
    retain_in_chapter:
    - minimum lock cases
    - local audit
    - output mapping
    - closing statement
    migrate:
    - full narratives to 03_cases/markdown
    - records to 03_cases/yaml
    - index to Appendix M
    - audit form to Appendix N
  completion_test:
  - All required positive, counter, and confusion classes are assigned.
  - At least three lock-critical cases are fully instantiated.
  - Components and relations are present in every valid decomposition.
  - Source function outcomes and resolution outcomes map canonically.
  - Operator types remain untouched.
  - The SUB local audit passes.
```

---

## 37. PATH Cross-Chapter Dependency Chain

```text
Chapter 9   → establishes warranted transitions
Chapter 10  → forms path objects from transitions
Chapter 11  → specifies trajectory formation and sedimentation
Chapter 12  → tests degrees of path dependence
Chapter 13  → preserves branches and unavailable alternatives
Chapter 14  → preserves non-events within temporal objects
Chapter 15  → operationalizes COMPOSE
Chapter 16  → applies local PATH boundaries and Stop
Chapter 17  → tests, audits, and provisionally locks PATH
```

## 38. SUB Cross-Chapter Dependency Chain

```text
Chapter 18  → defines the provisionally compressed source object
Chapter 19  → defines the source-to-target granularity relation
Chapter 20  → operationalizes DECOMPOSE
Chapter 21  → applies it to operator-typed occurrences
Chapter 22  → applies it to composites and distributed functions
Chapter 23  → applies it to events, non-events, and internal time
Chapter 24  → applies it to PATH objects
Chapter 25  → classifies gain, neutrality, drift, and escape
Chapter 26  → separates SUB from RETYPE
Chapter 27  → applies local SUB boundaries and Stop
Chapter 28  → tests, audits, and provisionally locks SUB
```

## 39. Round 2 Primary Definition Matrix

| Concept family | Primary chapter | Later use without redefinition |
|---|---:|---|
| Temporal position and transition validity | 9 | 10–17, 23–24 |
| Path and path variants | 10 | 11–17, 24 |
| Trajectory and sedimentation | 11 | 12–17, 24, RETYPE |
| Path dependence as property | 12 | 13–17, 24, LIMITS |
| Branch and alternative status | 13 | 15–17, integrated cases |
| PATH-specific non-event logic | 14 | 15–17, 23 |
| COMPOSE procedure | 15 | cases, model registry, operation chains |
| PATH local boundaries | 16 | 17, LIMITS |
| PATH audit and outputs | 17 | integrated audit |
| Provisionally compressed source object | 18 | 19–28 |
| Granularity-change logic | 19 | 20–28 |
| DECOMPOSE procedure | 20 | 21–28, model registry |
| Operator-typed occurrence decomposition | 21 | 28, stress tests |
| Composite decomposition | 22 | 24, 28, RETYPE |
| Event/non-event decomposition | 23 | 24–28 |
| PATH-object decomposition | 24 | 26–28, RETYPE |
| Resolution outcome classes | 25 | 27–28, LIMITS |
| SUB/RETYPE boundary | 26 | 28, RETYPE |
| SUB local boundaries | 27 | 28, LIMITS |
| SUB audit and outputs | 28 | integrated audit |

## 40. Round 2 Critical Redundancy Guards

```text
9 / 10    → transition validity versus path formation
10 / 11   → path versus trajectory
11 / 12   → trajectory object versus path-dependence property
13 / 14   → unavailable alternatives versus expectation-bound non-events
14 / 23   → non-events in PATH versus decomposition of non-events
15 / 17   → COMPOSE procedure versus case/audit application
16 / 41–53 → local PATH limits versus integrated LIMITS
18 / 20   → source-object eligibility versus DECOMPOSE procedure
19 / 25   → granularity relation versus resolution outcome
20 / 21–24 → generic procedure versus object-family applications
24 / PATH → opening the same path versus composing a rival path
25 / 27   → resolution classification versus local admissibility gate
26 / RETYPE → operation boundary versus full projection theory
27 / 41–53 → local SUB limits versus integrated LIMITS
```

## 41. Round 2 Completion Gate

Round 2 is provisionally complete only when:

- exactly twenty new contracts exist for Chapters 9–28;
- the accumulated file contains exactly Chapters 0–28 without gaps or duplicates;
- PATH preserves chronology/sequence/path/trajectory/path-dependence distinctions;
- Θ alone is explicitly insufficient for trajectory and path dependence;
- COMPOSE preserves non-events, alternatives, asymmetries, bindings, selection, and loss;
- COMPOSE does not assign target functions;
- SUB acts only on occurrences and composites, never operator types;
- every DECOMPOSE contract preserves source reference and tests the coarser function;
- components and relations remain jointly required;
- gain, neutrality, drift, and escape are distinct;
- SUB versus new PATH and SUB versus RETYPE are explicitly decidable;
- PATH and SUB each include local boundaries, Stop, Non-Capture, cases, audits, and output mapping;
- no chapter imports additional authority from higher composition or finer resolution;
- all embedded YAML contracts are syntactically valid;
- Chapters 29–40 may begin without unresolved PATH or SUB operation-classification questions.

**Round status after generation:** `provisionally_complete`  
**Next contract round:** Chapters 29–40 — RETYPE, output 3/4


---

## 42. Round 3 Scope and Handoff

Round 3 governs Chapters 29–40, the complete RETYPE block.

```text
29–30  → functional-projection logic and PROJECT_AS
31–35  → principal projection families
36     → competing projections
37–38  → analogy, substitution, type jumps, and level mixing
39     → local RETYPE limits
40     → cases, audit, output mapping, and RETYPE Lock
```

The round receives typed source objects from Foundations, PATH, and SUB. It does not rewrite those source objects. Every RETYPE claim adds a bounded functional relation in a declared target context.

## 43. Round 3 Global Rules

1. `PROJECT_AS` remains the only RETYPE operation and one of exactly three STRATA core operations.
2. Origin type and target function remain separate in every sentence, record, model field, and case.
3. A target context, relative target level, validity scope, and claim ceiling are mandatory.
4. Recontextualization alone is not PROJECT_AS.
5. COMPOSE forms source objects; DECOMPOSE opens them; PROJECT_AS assigns bounded contextual functions.
6. Constitutive Source Trace, Counterfactual Sensitivity, loss disclosure, and alternatives are mandatory.
7. Each projection family operationalizes Chapter 30 and may not redefine PROJECT_AS.
8. Where PMS operator-typed occurrences materially carry a RETYPE claim, their already warranted occurrence Records, relevant dependency context, material variation, and exact Loss remain reconstructible through existing record positions. Operator names alone do not supply Source Trace.
9. Operator-occurrence anchoring does not require a full Δ–Ψ inventory, a new field, a new audit stage, or source typing inferred from target fit.
10. Functional similarity does not establish operator identity, semantic preservation, or a new primitive.
11. Higher-level functions remain source-traceable and do not inherit truth, rank, normative force, or application authority.
12. Operator weightings, modulators, and profiles do not alter Δ–Ψ dependencies and do not become person types.
13. Analogy-only, claim reduction, mandatory stop, failed transformation, and non-capture remain legitimate outputs.
14. No later projection erases the failure of an earlier source claim.
15. Add-on lenses remain optional later stress vectors and do not define RETYPE.
16. Formal validation checks declarations and consistency, not actual semantic adequacy, causality, or empirical truth.

---

## Chapter 29 — Functional Projection without Origin-Type Replacement

```yaml
chapter:
  number: '29'
  title: Functional Projection without Origin-Type Replacement
  role_in_work:
    primary_function: Establish the governing logic of RETYPE as bounded functional projection without source replacement.
    canonical_status: Primary RETYPE definition site for functional projection, source-object integrity, origin-type
      preservation, target function, and contextual boundedness.
    handoff: Supplies Chapter 30 with the conceptual conditions that PROJECT_AS must operationalize.
  governing_question: Under what conditions may an already typed PMS or STRATA object perform a new function in
    a declared target context without becoming a different origin type?
  required_claim:
    core: RETYPE adds a bounded source-to-context functional relation; it does not rewrite what the source object
      was or is in its origin reconstruction.
    typed_claim: Within target context C, source object X, while retaining origin type T, performs bounded function
      F.
    continuity_rule: Reference identity, origin type, historical load, and constitutive source relations remain
      visible through projection.
    occurrence_anchor_rule: Where a PMS-derived source claim materially depends on operator occurrences, the linked
      source Record preserves an inspectable occurrence-level route and material carrier variation without a new field.
    context_rule: No target function exists for RETYPE purposes without a declared target context, target object
      or scene, validity scope, and claim ceiling.
  required_distinctions:
  - origin type versus target function
  - functional projection versus origin-type replacement
  - source object versus target context
  - source-object integrity versus complete source reproduction
  - functional continuity versus semantic resemblance
  - PROJECT_AS versus Φ recontextualization
  - RETYPE versus COMPOSE
  - RETYPE versus DECOMPOSE
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    conditional:
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    handoff:
    - Chapter 30 formalizes the operation.
    - Chapters 31–35 instantiate projection families.
    - Chapters 36–39 test alternatives and limits.
  must_not_claim:
  - A projected function changes the source object into a new operator type.
  - A new frame alone constitutes RETYPE.
  - A trajectory that functions as a frame is thereby □ as an origin type.
  - A projected function applies beyond its declared context.
  - A successful projection replaces PATH or SUB.
  - Functional similarity supplies semantic identity or higher authority.
  required_example:
    minimal_case: A documented trajectory is projected as a bounded frame-function in one later configuration while
      remaining a trajectory in its source record.
    required_contrast: Show the same trajectory in a second context where no additional target function is warranted.
  required_counterpressure:
  - A source object may be relevant in the target context without performing a distinct target function.
  - A later scene may be fully reconstructible without the proposed historical projection.
  - Several present frames may outweigh the projected source function.
  - A target function that survives opposite source structures signals label elasticity.
  redundancy_guard:
    defines_here:
    - functional projection
    - typed RETYPE claim
    - projection without replacement
    - source-object integrity in projection
    - contextual boundedness of target function
    references_only:
    - Chapter 5 definitions of origin type, target function, and continuity
    - Chapter 26 operation boundary
    - Chapter 30 operation signature
    - specific projection families in Chapters 31–35
    must_not_duplicate:
    - redefining origin type or target function
    - restating the generic operation signature in every family chapter
    - treating recontextualization as projection
  model_relation:
    supplies:
    - RETYPE conceptual constraints
    - source and context identity requirements
    - origin-type preservation flag
    - bounded target-function relation
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can verify declared source type, context, target function, and preservation flags; it
      cannot determine whether the function is substantively warranted.
  appendix_migration:
    retain_in_chapter:
    - governing RETYPE claim
    - projection-versus-replacement distinction
    - minimal typed claim form
    migrate:
    - extended definitions to Appendix A
    - notation to Appendix B
    - valid/invalid patterns to Appendix H
    - confusion cases to Appendix I
  completion_test:
  - Origin type and target function remain syntactically and conceptually separate.
  - A target context and validity scope are mandatory.
  - PROJECT_AS is distinguished from recontextualization, COMPOSE, and DECOMPOSE.
  - Source integrity does not imply losslessness.
  - No new primitive or authority is produced.
```

---

## Chapter 30 — PROJECT_AS: Signature, Context, and Validity Scope

```yaml
chapter:
  number: '30'
  title: 'PROJECT_AS: Signature, Context, and Validity Scope'
  role_in_work:
    primary_function: Operationalize RETYPE through the complete PROJECT_AS signature, declarations, tests, losses,
      alternatives, and outputs.
    canonical_status: Primary and only full RETYPE operation-specification chapter.
    handoff: Provides a reusable operation record to Chapters 31–40 and the formal model.
  governing_question: What declarations and tests make a proposed target function a valid PROJECT_AS operation rather
    than renaming, analogy, or type jump?
  required_claim:
    core: PROJECT_AS maps an origin-typed source object and declared target context to a bounded target function,
      justification, loss profile, and validity scope.
    preconditions:
    - identifiable source object
    - declared origin type
    - source and target coordinates
    - specific target context
    - named target function
    - expected praxis difference
    - constitutive source trace
    - bounded claim
    test_rule: Constitutive Source Trace and Counterfactual Sensitivity are mandatory; relevant source change must
      be capable of changing the target-function claim.
    alternative_rule: At least one alternative projection and the no-projection option must remain available.
    result_rule: The operation-specific result and canonical output class are both recorded.
  required_distinctions:
  - source declaration versus target declaration
  - target function versus target object
  - load-bearing versus modulating source features
  - foregrounding versus compression versus exclusion
  - validity scope versus generalized transfer
  - projection result versus canonical output class
  - provisional projection versus failed projection
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    - Chapter 29 functional projection logic
    conditional:
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    model_handoff:
    - Operation Registry
    - Transformation Record schema
    - Boundary Decision Tree
    - Output Classes
  must_not_claim:
  - The target label itself justifies the projection.
  - Source Trace can be replaced by citation alone.
  - Counterfactual Sensitivity proves causality.
  - A valid PROJECT_AS is lossless.
  - A single admissible projection transfers validity to later operations.
  - The model can automatically establish semantic adequacy or empirical truth.
  required_example:
    minimal_case: One complete PROJECT_AS record with source, origin type, target context, target function, justification,
      constitutive trace, counterfactual test, loss, alternatives, scope, and result mapping.
    required_failure: A projection with an attractive target label but no source-dependent functional difference.
  required_counterpressure:
  - Missing target context.
  - Insufficient source trace.
  - Counterfactual insensitivity.
  - A no-projection account is more parsimonious.
  - The target function changes only rhetorically.
  - Source and target levels are mixed.
  redundancy_guard:
    defines_here:
    - PROJECT_AS signature
    - operation preconditions
    - source/target declarations
    - constitutive source trace
    - projection loss fields
    - validity-scope fields
    - projection-result set
    references_only:
    - Chapter 7 shared envelope
    - Chapter 6 general admissibility gates
    - Chapter 29 conceptual claim
    - family-specific tests in Chapters 31–35
    must_not_duplicate:
    - creating a second generic transformation record
    - defining a new operation for each projection family
    - claiming automated truth validation
  model_relation:
    supplies:
    - PROJECT_AS registry entry
    - required field groups
    - operation-specific failure codes
    - RETYPE output mappings
    - decision-tree branches for recontextualization, analogy, substitution, and type jump
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The formal model may validate structure, permitted values, and declared dependencies; human or
      domain-grounded analysis remains required for actual function, source load, and semantic continuity.
  appendix_migration:
    retain_in_chapter:
    - minimal signature
    - mandatory declarations
    - source-trace and counterfactual rules
    - loss and alternative requirements
    - result classes
    migrate:
    - full record schema to Appendix F
    - formal notation to Appendix B
    - test catalogue to Appendix G
    - invalid patterns to Appendix H
  completion_test:
  - Every mandatory PROJECT_AS field is assigned a clear role.
  - Source Trace and Counterfactual Sensitivity are non-optional.
  - Where PMS occurrence structure is material, source reference, source basis, Constitutive Source Trace, sensitivity, and Loss jointly preserve an inspectable occurrence-level route without adding a schema field.
  - Loss and alternatives are explicit.
  - The no-projection option is representable.
  - Operation-specific and canonical outputs are mapped.
  - Formal validation is not presented as truth determination.
```

---

## Chapter 31 — Trajectory as Frame-Function

```yaml
chapter:
  number: '31'
  title: Trajectory as Frame-Function
  role_in_work:
    primary_function: Specify the bounded conditions under which a prior trajectory structures later legibility,
      expectation, and action as a frame-function.
    canonical_status: Primary RETYPE family chapter for trajectory-to-frame-function projection.
    handoff: Provides the historical-frame stress case for PROJECT_AS and later competing-projection analysis.
  governing_question: When does a reconstructed trajectory carry enough historical load to function as a frame in
    a later configuration?
  required_claim:
    core: A trajectory may perform a bounded frame-function when sedimented expectations, roles, costs, exclusions,
      bindings, or residues materially structure a declared later context.
    non_determinism: Historical framing constrains or conditions later praxis but does not determine every later
      interpretation or action.
    plurality: The projected trajectory may be one frame source among several and its relative load must be stated.
    failure_rule: Rhetorical invocation of “history” without a reconstructible source trace is not an admissible
      frame projection.
    operator_carrier_rule: Bounded Frame-like work remains traceable to already warranted source occurrences and
      never creates a `□` occurrence or inherits complete Frame semantics.
  required_distinctions:
  - trajectory as source object versus frame-function as target function
  - historical load versus historical determinism
  - frame-function versus background relevance
  - single frame source versus multiple frame sources
  - source trajectory versus later target configuration
  - rhetorical history versus source-dependent framing
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    - Chapter 29
    - Chapter 30
    later_use:
    - Chapter 36 competing projections
    - Chapter 39 boundaries
    - Chapter 40 cases
  must_not_claim:
  - The past determines the later scene.
  - Every later interpretation is produced by the trajectory.
  - The trajectory becomes □.
  - “History matters” is a sufficient Source Trace.
  - A frame-function is permanent or universally transferable.
  - Present conditions need not be considered.
  required_example:
    minimal_case: A trajectory with sedimented expectations and asymmetric costs changes the set of credible interpretations
      in one later configuration.
    contrast_case: The same source history is present but does not change the target reconstruction because current
      conditions carry the full explanatory load.
  required_counterpressure:
  - Multiple present frames may weaken the historical function.
  - A contrary later event may recontextualize without erasing the trajectory.
  - Different source trajectories may produce indistinguishable later scenes.
  - The frame-function may be limited to one role or time window.
  redundancy_guard:
    defines_here:
    - trajectory-to-frame-function conditions
    - historical-load carriers
    - multiple-frame-source rule
    - rhetorical-history failure
    references_only:
    - trajectory definition and sedimentation from Chapters 11–12
    - generic PROJECT_AS fields from Chapter 30
    - general frame definition from Chapter 2
    must_not_duplicate:
    - redefining trajectory, frame, or PROJECT_AS
    - equating frame-function with □ identity
    - repeating general context and continuity theory
  model_relation:
    supplies:
    - frame-function family constraints
    - historical-load trace fields
    - counterfactual frame test
    - family-specific failure reasons
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can require historical-load fields and contextual limits; it cannot infer that a past
      trajectory actually frames a present scene.
  appendix_migration:
    retain_in_chapter:
    - family claim
    - historical-load criteria
    - counterfactual frame test
    - failure pattern
    migrate:
    - extended cases to 03_cases
    - family record examples to Appendix F
    - confusion patterns to Appendix I
  completion_test:
  - A valid source trajectory is already established by PATH.
  - The target configuration and framed praxis dimension are explicit.
  - Historical load is traced to source features.
  - Multiple frame sources remain possible.
  - Determinism and operator identity are denied.
  - A failed frame projection is representable.
```

---

## Chapter 32 — Trajectory as Macro-Event

```yaml
chapter:
  number: '32'
  title: Trajectory as Macro-Event
  role_in_work:
    primary_function: Specify when a temporally extended trajectory can function as an event-like unit within a
      wider path while preserving internal duration and heterogeneity.
    canonical_status: Primary RETYPE family chapter for trajectory-to-macro-event projection.
    handoff: Supplies a canonical test of temporal compression, punctualization risk, and COMPOSE/PROJECT_AS separation.
  governing_question: When may an extended trajectory serve as a bounded transition element in a wider temporal
    frame without being falsely punctualized?
  required_claim:
    core: A trajectory may function as a macro-event when, within a wider declared frame, it marks a source-traceable
      transition that changes later possibilities.
    duration_rule: Internal duration, constitutive phases, relevant reversals, and heterogeneity remain acknowledged
      even when compressed.
    operation_rule: COMPOSE forms the trajectory; PROJECT_AS assigns the macro-event function in the wider path.
    failure_rule: A historical headline or period label without internal trace and target transition gain is not
      a macro-event projection.
  required_distinctions:
  - trajectory source object versus macro-event target function
  - extended event versus punctual event
  - boundary selection versus retrospective label
  - internal duration versus target-level compression
  - COMPOSE versus PROJECT_AS
  - macro-event function versus complete historical period
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    - Chapter 29
    - Chapter 30
    later_use:
    - Chapter 36
    - Chapter 39
    - Chapter 40
  must_not_claim:
  - A macro-event occurred at one point merely because it is represented as one target element.
  - Internal phases and costs may be erased.
  - A period name establishes an event function.
  - COMPOSE itself assigns the macro-event function.
  - The wider target frame is optional.
  - The projection proves a causal turning point.
  required_example:
    minimal_case: A multi-year trajectory is projected as one transition-bearing macro-event within a longer institutional
      path, with internal phases retained in the trace.
    failure_case: A broad era label with no specified start, end, transition effect, or source-dependent boundary.
  required_counterpressure:
  - Different periodizations may produce different macro-event boundaries.
  - Internal reversals may defeat the unitary event function.
  - Removing one phase may leave the target transition unchanged.
  - A narrower path object may be a better source.
  redundancy_guard:
    defines_here:
    - macro-event family conditions
    - boundary-selection obligations
    - internal-duration preservation
    - punctualization error
    - counterfactual macro-event test
    references_only:
    - trajectory and COMPOSE theory
    - event definitions from Chapters 1 and 3
    - generic PROJECT_AS signature
    - general loss accounting
    must_not_duplicate:
    - redefining event or trajectory
    - treating macro-event as a new primitive
    - collapsing composition and projection
  model_relation:
    supplies:
    - macro-event target-function type
    - boundary and duration fields
    - punctualization failure code
    - family counterfactual test
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can verify that wider frame, boundaries, internal-duration trace, and target transition
      effect are declared; it cannot decide the historically correct periodization.
  appendix_migration:
    retain_in_chapter:
    - family claim
    - boundary and duration conditions
    - operation separation
    - failure rule
    migrate:
    - extended periodization examples to Appendix I
    - record details to Appendix F
    - notation to Appendix B
  completion_test:
  - The source trajectory and wider target frame are distinct.
  - Start, end, constitutive phases, and transition function are explicit.
  - Internal duration and heterogeneity remain visible.
  - COMPOSE and PROJECT_AS use separate records.
  - Source phases retain claim-relevant operator occurrence and `Θ` temporal relations; Macro-Event remains a non-operator target function.
  - Punctualization can cause failure or claim reduction.
```

---

## Chapter 33 — Recurrent Trajectory Form as Attractor-Function

```yaml
chapter:
  number: '33'
  title: Recurrent Trajectory Form as Attractor-Function
  role_in_work:
    primary_function: Specify when a recurrent temporal form, rather than one trajectory, performs a dynamic attractor-function.
    canonical_status: Primary RETYPE family chapter for recurrent-form-to-attractor-function projection.
    handoff: Provides the principal threshold and elasticity stress test for recurrent functional projection.
  governing_question: When does repeated similarity across trajectories become a source-traceable dynamic attractor-function
    rather than retrospective pattern narration?
  required_claim:
    core: A recurrent trajectory form may perform an attractor-function when multiple sufficiently comparable paths
      share constitutive transitions and the form lowers friction or raises alternative costs for later recurrence.
    source_rule: The source is the recurrent form reconstructed across trajectories, not a single trajectory treated
      as a universal pattern.
    threshold_rule: Repetition count alone is insufficient; common mechanisms, frames, operator weightings, and
      effects on later path accessibility are required.
    dynamic_rule: An attractor-function may stabilize a transition form rather than a static configuration.
  required_distinctions:
  - single trajectory versus recurrent trajectory form
  - repeated similarity versus constitutive recurrence
  - static attractor-function versus dynamic attractor-function
  - pattern threshold versus arbitrary count
  - recurrence source trace versus narrative motif
  - later path influence versus descriptive resemblance
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    - Chapter 29
    - Chapter 30
    conditional:
    - Chapter 35 operator-weighting analysis where invoked
    later_use:
    - Chapter 36
    - Chapter 39
    - Chapter 40
  must_not_claim:
  - One repeated-looking sequence establishes an attractor.
  - Any number of similar paths supplies a universal threshold.
  - The recurrent form becomes Α as a new primitive.
  - Narrative resemblance proves a reproduction mechanism.
  - The same pattern label may absorb opposite sequences.
  - Attractor-function implies determinism.
  required_example:
    minimal_case: Three comparable trajectories share a constitutive transition pattern and measurable changes in
      friction or alternative cost; vary one load-bearing phase and show the function weaken.
    countercase: Several superficially similar sequences lack common mechanism and do not affect later continuation
      probabilities.
  required_counterpressure:
  - Small samples may support only a provisional projection.
  - Different frames may make the trajectories non-comparable.
  - A repeated form may be produced anew each time without attracting later paths.
  - Elastic pattern definitions can absorb all deviations.
  redundancy_guard:
    defines_here:
    - recurrent-form source object
    - dynamic attractor-function
    - pattern threshold criteria
    - counterfactual attractor test
    - retrospective-similarity failure
    references_only:
    - trajectory and attractor definitions
    - generic PROJECT_AS procedure
    - general calibration limits from later LIMITS
    must_not_duplicate:
    - redefining Α
    - setting a universal recurrence threshold
    - turning a family label into a person or group type
  model_relation:
    supplies:
    - recurrent-form source schema
    - pattern-threshold declarations
    - dynamic/static target-function flag
    - elasticity and similarity failure codes
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can require multiple source trajectories and declared constitutive recurrence; it cannot
      establish whether the trajectories are genuinely comparable or causally linked.
  appendix_migration:
    retain_in_chapter:
    - family claim
    - source-object rule
    - threshold conditions
    - dynamic/static distinction
    - failure pattern
    migrate:
    - extended recurrence tests to Appendix J
    - calibration tests to Appendix G
    - cases to 03_cases
  completion_test:
  - The source is a recurrent form, not one path.
  - Constitutive recurrence is separated from resemblance.
  - A path-influence mechanism is declared.
  - Thresholds remain context-sensitive.
  - Dynamic and static attractor-functions are distinct.
  - Counterexamples can break the pattern claim.
  - Recurrent-form comparison preserves claim-relevant occurrence relations across linked source Trajectories and separates bounded Attractor-like work from `Α` identity.
```

---

<a id="chapter-34-composite-structures-as-higher-level-functions"></a>

## Chapter 34 — Composite Structures as Higher-Level Functions

```yaml
chapter:
  number: '34'
  title: Composite Structures as Higher-Level Functions
  role_in_work:
    primary_function: Specify how relationally organized composites may perform bounded higher-level functions without
      source-free emergence or authority increase.
    canonical_status: Primary RETYPE family chapter for composite-to-higher-level functional projection.
    handoff: Supplies generic criteria for boundary-, asymmetry-, binding-, integration-, and related composite
      functions.
  governing_question: When do multiple local occurrences form a relationally carried higher-level function rather
    than a mere aggregate or macro-label?
  required_claim:
    core: A composite may perform a higher-level function only when relations among its components generate a target-context
      praxis difference that remains traceable to local and distributed source load.
    emergence_rule: Emergent means visible only at composite level while remaining source-traceable; it does not
      mean source-free novelty.
    threshold_rule: Number, duration, or repetition alone is insufficient; functional formation requires coordination,
      reinforcement, or shared effect.
    authority_rule: Higher-level function adds analytical legibility, not truth, rank, or application authority.
  required_distinctions:
  - aggregation versus functional formation
  - component accumulation versus relational coordination
  - emergent function versus source-free novelty
  - local occurrence type versus higher-level target function
  - distributed function versus internal homogeneity
  - macrofunction versus person property
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    - Chapter 29
    - Chapter 30
    conditional:
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    later_use:
    - Chapter 35 profiles
    - Chapter 36 competing projections
    - Chapter 39 boundaries
  must_not_claim:
  - Many local occurrences automatically entail a macrofunction.
  - All components must be homogeneous.
  - A higher-level Ω-, Ψ-, Σ-, or boundary-function becomes a new operator.
  - Emergence licenses missing Source Trace.
  - Macrofunction can be assigned directly to a person or group essence.
  - Higher level means greater explanatory authority.
  required_example:
    minimal_case: Distributed local asymmetries jointly create a bounded higher-level access function through coordination
      and repeated load distribution.
    countercase: Numerous local differences coexist but do not coordinate, reinforce, or alter target-level praxis.
  required_counterpressure:
  - Component substitution may leave the function intact.
  - Local contradictions may weaken or redirect the target function.
  - A smaller subset may carry all relevant load.
  - Observed aggregation may be an artifact of frame selection.
  redundancy_guard:
    defines_here:
    - composite higher-level function conditions
    - functional formation
    - source-traceable emergence
    - threshold obligations
    - authority ceiling for macrofunctions
    references_only:
    - composite object and decomposition theory
    - generic PROJECT_AS procedure
    - operator definitions from PMS Base
    must_not_duplicate:
    - redefining specific operators
    - claiming macro entailment from micro support
    - assuming micro homogeneity
  model_relation:
    supplies:
    - higher-level function family registry
    - component-relation trace fields
    - formation versus aggregation decision branch
    - emergence boundary
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can require components, relations, target effect, and traceability; it cannot infer that
      a distributed macrofunction actually exists.
  appendix_migration:
    retain_in_chapter:
    - generic family conditions
    - aggregation/formation distinction
    - emergence boundary
    - authority rule
    migrate:
    - extended operator-family examples to Appendix J
    - valid/invalid patterns to Appendix H
    - records to Appendix F
  completion_test:
  - Components and their relations are both required.
  - A target-level praxis difference is explicit.
  - Emergence remains source-traceable.
  - No macrofunction becomes a primitive or person type.
  - Mere aggregation is a failed or reduced result.
  - Where components are operator-typed occurrences, relation topology and occurrence-level emergence remain reconstructible without dependency inheritance or new operator formation.
```

---

## Chapter 35 — Operator Weighting, Modulation, and Emergent Functional Profiles

```yaml
chapter:
  number: '35'
  title: Operator Weighting, Modulation, and Emergent Functional Profiles
  role_in_work:
    primary_function: Specify how existing operator weightings and modulating conditions may form bounded profiles
      without reordering PMS or creating hidden types.
    canonical_status: Primary RETYPE chapter for weighting, modulation, profile formation, and optional profile
      projection.
    handoff: Supplies profile-specific candidates and failure patterns to Chapters 36–40 and stress-test appendices.
  governing_question: How may different load distributions and access conditions among existing operators shape
    trajectories or target functions without altering the Δ–Ψ grammar?
  required_claim:
    core: Operator weighting and modulation describe configuration-bound differences in relative load, accessibility,
      threshold, or temporal effect; they do not create new operators or dependency orders.
    profile_rule: A functional profile summarizes a stable relation among existing operator occurrences and may
      be projected only when it changes later praxis and remains source-traceable.
    person_rule: Profiles belong to declared configurations or composites, not global person or group types.
    stress_vector_rule: Add-on lenses may later test profiles but do not define STRATA architecture or rules.
  required_distinctions:
  - operator weighting versus operator replacement
  - weighting versus dependency reordering
  - modulator versus operator
  - modulating profile versus formal type
  - configuration-bound profile versus person trait
  - profile description versus projected function
  - dominance versus exclusivity
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    - Chapter 29
    - Chapter 30
    conditional:
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    later_use:
    - Chapter 36 profile alternatives
    - Chapter 39 profile inflation limits
    - Appendix J stress tests
  must_not_claim:
  - High relevance of an operator removes its PMS dependencies.
  - A modulator is a fourth STRATA operation or new PMS primitive.
  - Every configuration requires a named profile.
  - A profile is a stable person essence.
  - Attractive profile labels establish predictive power.
  - Add-on lenses can authorize STRATA rules.
  required_example:
    minimal_case: A configuration-bound Ω/Θ-dominant profile alters which continuation becomes costly, while all
      PMS dependencies and source occurrences remain explicit.
    countercase: A rhetorically named profile has no stable weighting criteria and produces no discriminable path
      difference.
  required_counterpressure:
  - Weightings may change over time or by role.
  - Several profiles may explain the same trajectory.
  - A profile may be descriptively compact but functionally inert.
  - Thresholds may remain calibration-sensitive.
  - The source packet is claim-invoked rather than a complete Δ–Ψ census, and profile/function claims remain reconstructible after label removal.
  redundancy_guard:
    defines_here:
    - operator weighting
    - modulator
    - modulating profile
    - emergent functional profile
    - profile projection conditions
    - profile inflation failure
    references_only:
    - PMS operator definitions and dependencies
    - SUB analysis of internal composite weighting
    - generic PROJECT_AS rules
    - later source/calibration limits
    must_not_duplicate:
    - reordering Δ–Ψ
    - creating new operator or person types
    - making add-on lenses architectural dependencies
  model_relation:
    supplies:
    - weighting and profile data fields
    - profile-to-function projection branch
    - profile-inflation and person-typing errors
    - configuration-scope requirement
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can store declared weights, profiles, scopes, and effects; it cannot derive psychologically
      or empirically valid weights from persons or data by itself.
  appendix_migration:
    retain_in_chapter:
    - definitions and boundaries
    - configuration-scope rule
    - optional projection requirements
    - failure patterns
    migrate:
    - extended stress tests to Appendix J
    - person-typing countercases to Appendix I
    - formal profile examples to model examples
  completion_test:
  - Weighting does not change operator dependencies.
  - Modulators and profiles are not operators.
  - Profiles are configuration-bound.
  - A projected profile requires functional gain and traceability.
  - Add-on lenses remain optional stress vectors.
  - Profile inflation and person typing remain explicit failures.
```

---

<a id="chapter-36-competing-projections"></a>

## Chapter 36 — Competing Projections

```yaml
chapter:
  number: '36'
  title: Competing Projections
  role_in_work:
    primary_function: Provide the comparative discipline for multiple candidate target functions from the same source.
    canonical_status: Primary RETYPE chapter for compatibility, competition, comparison criteria, indeterminacy,
      and non-translation among projections.
    handoff: Supplies comparison records and unresolved outcomes to Chapters 39–40 and the integrated audit.
  governing_question: How should RETYPE compare several plausible projections without forcing integration or treating
    selection as tribunal judgment?
  required_claim:
    core: Multiple projections may be compatible, competing, context-dependent, non-comparable, or unresolved; comparison
      depends on shared source, target context, claim scope, source trace, discrimination, loss, and counterfactual
      sensitivity.
    alternative_rule: Every strong projection preserves at least one serious alternative and the no-projection option.
    indeterminacy_rule: Equal support or non-comparability may legitimately yield partially_admissible or non_capture.
    non_translation_rule: One projection need not translate losslessly into another.
  required_distinctions:
  - compatible projections versus competing projections
  - shared source versus shared target context
  - co-validity versus forced integration
  - comparative preference versus absolute truth
  - indeterminacy versus failure
  - non-translation versus contradiction
  - projection comparison versus person or theory tribunal
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapters 29–35
    conditional:
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    later_use:
    - Chapter 39 alternative test
    - Chapter 40 cases
    - Chapter 53 integrated audit
  must_not_claim:
  - One source object may have only one valid target function.
  - The most comprehensive projection is automatically superior.
  - Competing projections must be collapsed into one label.
  - A preferred projection becomes the true type of the source.
  - Indeterminacy is a defect to be hidden.
  - Projection comparison authorizes moral, political, or person judgment.
  required_example:
    minimal_case: The same trajectory supports a frame-function in context A and a macro-event function in context
      B; show compatibility.
    competition_case: In one target context, frame-function and attractor-function compete and require comparison
      or unresolved status.
  required_counterpressure:
  - Different validity scopes can dissolve apparent competition.
  - The no-projection account may outperform all candidates.
  - Different loss profiles can make candidates non-comparable.
  - A weaker but more sensitive projection may be preferable.
  redundancy_guard:
    defines_here:
    - projection compatibility and competition
    - comparative criteria
    - projection indeterminacy
    - non-translation
    - projection comparison record
    references_only:
    - family definitions from Chapters 31–35
    - generic operation rules from Chapter 30
    - canonical output meanings
    must_not_duplicate:
    - redefining target functions
    - creating a universal ranking metric
    - turning comparison into theory or person adjudication
  model_relation:
    supplies:
    - projection-comparison record
    - compatibility statuses
    - comparison criteria fields
    - mapping for competing projections
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can compare declared fields and compatibility statuses; it cannot automatically choose
      the semantically or empirically best projection.
  appendix_migration:
    retain_in_chapter:
    - comparison logic
    - minimal comparison record
    - indeterminacy and non-translation outcomes
    migrate:
    - full comparison examples to Appendix I
    - records to Appendix F
    - case index to Appendix M
  completion_test:
  - Compatibility and competition use explicit criteria.
  - The no-projection option remains present.
  - Indeterminacy and non-comparability are legitimate outputs.
  - No projection is promoted to source identity.
  - No tribunal or authority claim is introduced.
```

---

## Chapter 37 — Projection, Structural Analogy, and Label Substitution

```yaml
chapter:
  number: '37'
  title: Projection, Structural Analogy, and Label Substitution
  role_in_work:
    primary_function: Separate admissible functional projection from useful analogy and empty label substitution.
    canonical_status: Primary RETYPE definition site for the projection/analogy/substitution triad and cross-domain
      semantic-preservation discipline.
    handoff: Supplies error classification to Chapter 38, boundary tests to Chapter 39, and analogy-only outputs
      to Chapter 40.
  governing_question: What distinguishes a source-dependent target function from a merely useful resemblance or
    rhetorical PMS label?
  required_claim:
    core: A valid projection requires typed source, target context, functional gain, constitutive source trace,
      counterfactual sensitivity, loss, and bounded scope; analogy asserts only structured similarity; label substitution
      supplies neither.
    analogy_rule: Analogy may be a legitimate terminal output when semantic preservation or target function is unestablished.
    cross_domain_rule: Formal or executable correspondence across domains does not by itself establish praxeological
      semantic preservation.
    substitution_rule: A PMS label that remains unchanged across relevant source variations is presumptively non-functional.
  required_distinctions:
  - functional projection versus structural analogy
  - analogy versus label substitution
  - formal correspondence versus semantic preservation
  - symbolic mapping versus praxeological function
  - translation success versus model superiority
  - useful resemblance versus typed target claim
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapter 29
    - Chapter 30
    conditional:
    - Chapters 31–36
    - cross-domain cases only where sources support them
    later_use:
    - Chapter 38 error taxonomy
    - Chapter 39 analogy boundary
    - Chapter 40 cases
  must_not_claim:
  - Formal similarity establishes semantic identity.
  - Executable mapping proves a valid projection.
  - A useful analogy must be upgraded to PROJECT_AS.
  - Translation breadth proves PMS completeness or superiority.
  - Label familiarity creates PraxisPurchase.
  - Cross-domain residuals may be ignored.
  required_example:
    minimal_case: A cross-domain mapping is useful for comparing transition form but lacks semantic preservation
      and therefore ends as analogy_only.
    failure_case: A target receives an operator-derived label with no context, source trace, counterfactual test,
      or new discrimination.
  required_counterpressure:
  - The analogy may reveal differences rather than preserve function.
  - Target-domain features may have no source equivalent.
  - A projection may collapse to analogy after counterpressure.
  - A label may be rhetorically strong while empirically inert.
  redundancy_guard:
    defines_here:
    - valid projection/analogy/substitution triad
    - analogy status
    - cross-domain semantic-preservation test
    - label-substitution markers
    - analogy-only terminal result
    references_only:
    - generic PROJECT_AS requirements
    - Chapter 36 projection comparison
    - PMS Base non-capture and rival openness
    must_not_duplicate:
    - redefining semantic validity for every domain
    - treating analogy as failure by default
    - claiming translation success as proof
  model_relation:
    supplies:
    - mapping-status values
    - analogy-only output mapping
    - label-substitution error code
    - semantic-preservation declaration
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can distinguish declared mapping statuses and missing projection fields; it cannot automatically
      judge semantic preservation between domains.
  appendix_migration:
    retain_in_chapter:
    - triad definitions
    - cross-domain boundary
    - analogy-only outcome
    - substitution markers
    migrate:
    - cross-domain stress tests to Appendix K
    - valid/invalid mappings to Appendix H
    - cases to Appendix I
  completion_test:
  - Projection, analogy, and substitution have non-overlapping minimum requirements.
  - Analogy-only is explicitly legitimate.
  - Formal and executable mappings are not truth proofs.
  - Label substitution can fail even when rhetorically coherent.
  - Cross-domain non-capture remains available.
```

---

## Chapter 38 — Invalid Type Jumps and Unmarked Level Mixing

```yaml
chapter:
  number: '38'
  title: Invalid Type Jumps and Unmarked Level Mixing
  role_in_work:
    primary_function: Classify hard RETYPE category errors involving type replacement, context omission, level mixing,
      scope inflation, person typing, and claim rescue.
    canonical_status: Primary RETYPE error-taxonomy chapter for invalid projection structures.
    handoff: Supplies explicit failure codes to Chapter 39 boundaries, Chapter 40 audits, and the formal decision
      tree.
  governing_question: Which formal and claim-level errors make a proposed projection invalid before substantive
    preference is considered?
  required_claim:
    core: A projection is invalid when it replaces origin type, omits target context, mixes levels or granularities
      without relation, creates a new primitive, transfers a macrofunction to a person property, inflates scope,
      or rescues a failed claim by relocation.
    new_claim_rule: A projection after failure is a new independently testable claim and does not erase the original
      failure.
    loss_rule: Projection without declared foregrounding, backgrounding, and compression is incomplete.
    person_rule: Configuration or composite functions may not be rewritten as global person or group traits.
  required_distinctions:
  - origin-type replacement versus bounded function
  - level relation versus level mixing
  - granularity relation versus granularity mixing
  - local target function versus scope inflation
  - macrofunction versus person property
  - new projection claim versus rescue of failed source claim
  - metaphorical expression versus formal PROJECT_AS
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapter 29
    - Chapter 30
    - Chapter 37
    conditional:
    - Chapter 36 where competing claims are involved
    later_use:
    - Chapter 39
    - Chapter 40
    - Chapter 50 anti-immunization
  must_not_claim:
  - A target function may overwrite origin type.
  - An unspecified “higher level” is sufficient context.
  - Micro evidence automatically entails a macrofunction.
  - A configuration-level function characterizes a person.
  - Moving the claim to another context defeats the original objection.
  - Local projection may be generalized to all scenes or group members.
  required_example:
    minimal_case: A trajectory functions as a frame in context C and is then incorrectly declared to be a Frame
      operator or a stable property of an actor; classify each error separately.
    rescue_case: A failed source typing is relocated to another level without preserving the failure record.
  required_counterpressure:
  - A metaphor may be useful but formally insufficient.
  - A genuine dual operation may look like level mixing unless records are separated.
  - Some partial continuity failures require claim reduction rather than total rejection.
  redundancy_guard:
    defines_here:
    - invalid type jump
    - missing-context error
    - unmarked level and granularity mixing
    - scope inflation
    - person-level type jump
    - projection rescue
    - invalid projection record
    references_only:
    - generic projection requirements
    - Chapter 37 analogy/substitution
    - later general anti-immunization
    must_not_duplicate:
    - redefining continuity theory
    - turning every ambiguous phrase into automatic failure without analysis
    - performing the integrated audit
  model_relation:
    supplies:
    - RETYPE error codes
    - invalid-projection record
    - decision-tree failure branches
    - claim-rescue flag
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can detect missing declarations and prohibited type assignments; it cannot resolve every
      ambiguous natural-language metaphor without interpretive review.
  appendix_migration:
    retain_in_chapter:
    - error taxonomy
    - minimal invalid record
    - failure-preservation rule
    migrate:
    - extended invalid patterns to Appendix H
    - confusion cases to Appendix I
    - person-typing cases to Appendix K or L as appropriate
  completion_test:
  - Every invalidity class has a distinct trigger.
  - Origin-type replacement and scope inflation are separately testable.
  - Person typing is explicitly prohibited.
  - Projection rescue preserves the original failure.
  - Ambiguous metaphor may be reduced rather than overclassified.
```

---

<a id="chapter-39-retype-boundary-conditions"></a>

## Chapter 39 — RETYPE Boundary Conditions

```yaml
chapter:
  number: '39'
  title: RETYPE Boundary Conditions
  role_in_work:
    primary_function: Apply the Admissibility Band and RETYPE-specific type, context, analogy, elasticity, Stop,
      and Non-Capture conditions.
    canonical_status: Primary RETYPE local-limits chapter.
    handoff: Supplies the complete local gate to Chapter 40 and later integrated LIMITS without replacing Chapter
      6 or Chapters 41–53.
  governing_question: Where must PROJECT_AS be narrowed, reduced, stopped, failed, or recorded as Non-Capture?
  required_claim:
    core: RETYPE is admissible only where the target function adds praxeological discrimination, carries constitutive
      source load, preserves origin type and reference, remains context-bounded, declares loss, and is counterfactually
      sensitive.
    lower_boundary: Renaming without functional gain falls below the Relevance Floor.
    upper_boundary: Function without Source Trace or source dependency exceeds the Traceability Ceiling.
    elasticity_rule: A projection that survives opposite source structures or proliferates functions to absorb objections
      is overelastic.
    terminal_rule: Claim reduction, analogy_only, mandatory_stop, failed_transformation, and non_capture remain
      positive classified outcomes.
  required_distinctions:
  - lower RETYPE boundary versus upper RETYPE boundary
  - functional gain versus renaming
  - Source Trace versus citation
  - type-integrity failure versus context-boundary failure
  - analogy-only versus failed projection
  - claim reduction versus Stop
  - Stop versus Non-Capture
  - local RETYPE limit versus integrated LIMITS
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapters 29–38
    later_handoff:
    - Chapter 40 RETYPE Lock
    - Chapters 41–53 integrated system limits
  must_not_claim:
  - A clever label supplies functional gain.
  - Source Trace can be inferred from target fit.
  - A projection may be made indefinitely narrower to survive.
  - Every ambiguous case must be forced into one function.
  - Stop and Non-Capture are equivalent.
  - Local success adds authority or validates other operations.
  required_example:
    minimal_case: A proposed frame-function has clear context but no source-dependent change and is reduced to background
      relevance or stopped.
    boundary_case: A cross-domain mapping passes formal tests but remains analogy_only because semantic preservation
      is unestablished.
  required_counterpressure:
  - Counterfactuals may be unavailable, requiring provisional reduction.
  - Several equally strong functions may lead to non_capture.
  - A narrow projection may remain admissible despite substantial loss.
  - No projection may be the most accurate result.
  redundancy_guard:
    defines_here:
    - RETYPE-specific lower and upper boundaries
    - type and context boundary application
    - projection elasticity
    - RETYPE Stop conditions
    - RETYPE Non-Capture
    - local admissibility formula
    references_only:
    - Chapter 6 band definitions
    - Chapters 44–52 later system-wide elaboration
    - Chapter 30 operation fields
    - Chapter 37 analogy definition
    must_not_duplicate:
    - redefining the Admissibility Band
    - pre-empting integrated LIMITS
    - turning local audit into truth tribunal
  model_relation:
    supplies:
    - RETYPE admissibility rules
    - local Stop triggers
    - claim-reduction branches
    - analogy and non-capture mappings
    - elasticity failure
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can evaluate declared gates and output routing; it cannot establish actual praxis gain,
      semantic preservation, or the best target function automatically.
  appendix_migration:
    retain_in_chapter:
    - local boundary criteria
    - terminal outputs
    - elasticity rule
    - local formula
    migrate:
    - full tests to Appendix G
    - invalid patterns to Appendix H
    - audit form to Appendix N
  completion_test:
  - Lower and upper boundaries are independently testable.
  - Type, reference, context, loss, and counterfactual gates remain non-compensatory.
  - Analogy-only is not confused with projection failure.
  - Stop and Non-Capture remain distinct.
  - Overelastic claim rescue is blocked.
  - No local result increases authority.
```

---

## Chapter 40 — RETYPE Cases, Countercases, and Local Audit

```yaml
chapter:
  number: '40'
  title: RETYPE Cases, Countercases, and Local Audit
  role_in_work:
    primary_function: Demonstrate, audit, map, and provisionally lock the RETYPE discipline through positive, negative,
      and confusion cases.
    canonical_status: Primary RETYPE site for case architecture, local audit, operation-specific results, canonical
      mapping, and lock decision.
    handoff: Closes RETYPE and supplies tested projection records and failures to LIMITS and integrated cases.
  governing_question: Can RETYPE reliably distinguish bounded projection from recontextualization, composition,
    decomposition, analogy, label substitution, type jump, and person typing?
  required_claim:
    core: RETYPE is locally complete only when all principal projection families and failure modes produce explicit
      records, survive counterpressure, and map to the canonical output system.
    artifact_rule: Lock-critical cases require Markdown case, YAML PROJECT_AS record, local audit result, loss and
      alternative account, and output-class mapping.
    mapping_rule:
      admissible functional projection: admissible
      admissible narrow projection: admissible_with_bounded_claim
      provisional projection: admissible_but_provisional
      compatible multiple projections with fully separated contexts and no further material narrowing: admissible
      compatible multiple projections with material reach or scope narrowing as the decisive retained result: admissible_with_bounded_claim
      competing projections: admissible_but_provisional or partially_admissible or non_capture
      useful structural analogy: analogy_only
      label substitution: failed_transformation
      invalid type jump: failed_transformation
      unmarked level mixing: failed_transformation
      mandatory claim reduction: claim_reduction_required
      mandatory stop: mandatory_stop
      non-capture: non_capture
    closure_rule: RETYPE closes only when no result creates a new primitive, overwrites origin type, or inherits
      application authority.
  required_distinctions:
  - admissible versus narrow versus provisional projection
  - compatible versus competing projections
  - projection versus analogy-only
  - label substitution versus type jump
  - recontextualization versus PROJECT_AS
  - RETYPE versus COMPOSE or DECOMPOSE
  - claim reduction versus mandatory stop versus non-capture
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 origin type, target function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock
    - Chapters 9–17 where trajectory, recurrence, or macro-event source objects are used
    - SUB Lock
    - Chapter 26 SUB/RETYPE boundary
    - Chapters 29–39
    case_requirements:
    - trajectory as bounded frame-function
    - PROJECT_AS label substitution failure
    - projection versus structural analogy confusion case
    handoff:
    - RETYPE Lock to LIMITS and integrated case/model pass
  must_not_claim:
  - One positive family case validates RETYPE generally.
  - Cases may omit source trace, counterfactual test, loss, or alternatives.
  - Compatible projections must be merged.
  - Analogy-only is a disguised failure.
  - Projection results can alter PMS Base or classify persons.
  - A later projection erases a failed earlier claim.
  required_example:
    minimal_case: Include the three lock-critical cases plus a macro-event case, recurrent-form attractor case,
      competing-projection case, and person-level type-jump countercase.
    artifact_set:
    - Markdown case
    - YAML PROJECT_AS record
    - local audit result
    - canonical output mapping
  required_counterpressure:
  - Projection without context.
  - Rhetorical history.
  - Punctualization.
  - Repeated similarity without attractor load.
  - Macrofunction from aggregation.
  - Profile inflation.
  - Competing equal projections.
  - Analogy presented as projection.
  - Claim rescue and person typing.
  redundancy_guard:
    defines_here:
    - RETYPE case architecture
    - RETYPE local audit
    - operation-specific result taxonomy and canonical mapping
    - RETYPE lock decision
    references_only:
    - definitions from Chapters 29–39
    - integrated audit Chapter 53
    - full case index Appendix M
    must_not_duplicate:
    - re-deriving PROJECT_AS or admissibility theory
    - combining multiple operations in one undeclared record
    - using cases as person or theory tribunals
  model_relation:
    supplies:
    - RETYPE audit checklist fields
    - case completeness expectations
    - projection output mapping
    - lock status
    model_artifacts:
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can validate complete records, prohibited assignments, and output mappings; it cannot
      replace substantive contextual and semantic analysis.
  appendix_migration:
    retain_in_chapter:
    - minimum lock cases
    - local audit
    - canonical output mapping
    - closing statement
    migrate:
    - full narratives to 03_cases/markdown
    - records to 03_cases/yaml
    - index to Appendix M
    - audit form to Appendix N
  completion_test:
  - All required positive, negative, and confusion classes are assigned.
  - At least three lock-critical cases are fully instantiated.
  - Every valid projection includes context, source trace, counterfactual test, loss, alternatives, and scope.
  - Origin type is preserved in every admissible case.
  - Analogy-only, claim reduction, Stop, Failure, and Non-Capture are all reachable.
  - Person typing and authority inheritance are prohibited.
  - The RETYPE local audit passes.
```


---

## 44. RETYPE Cross-Chapter Dependency Chain

```text
Chapter 29  → establishes functional projection without source replacement
Chapter 30  → operationalizes PROJECT_AS
Chapter 31  → applies it to trajectory as frame-function
Chapter 32  → applies it to trajectory as macro-event
Chapter 33  → applies it to recurrent form as attractor-function
Chapter 34  → applies it to composites as higher-level functions
Chapter 35  → applies it to weighting, modulation, and profiles
Chapter 36  → compares compatible and competing projections
Chapter 37  → separates projection, analogy, and label substitution
Chapter 38  → classifies invalid type jumps and level mixing
Chapter 39  → applies local RETYPE boundaries and Stop
Chapter 40  → tests, audits, and provisionally locks RETYPE
```

## 45. Round 3 Primary Definition Matrix

| Concept family | Primary chapter | Later use without redefinition |
|---|---:|---|
| Functional projection and typed RETYPE claim | 29 | 30–40 |
| PROJECT_AS signature and record | 30 | 31–40, formal model |
| Trajectory as frame-function | 31 | 36, 39–40 |
| Trajectory as macro-event | 32 | 36, 39–40 |
| Recurrent form as attractor-function | 33 | 36, 39–40 |
| Composite higher-level functions | 34 | 35–36, 39–40 |
| Weighting, modulation, and profiles | 35 | 36, 39–40 |
| Compatible and competing projections | 36 | 39–40, integrated audit |
| Projection / analogy / label substitution | 37 | 38–40 |
| Type jump and level-mixing errors | 38 | 39–40, anti-immunization |
| RETYPE local limits | 39 | 40, integrated LIMITS |
| RETYPE audit and outputs | 40 | integrated cases and audit |

## 46. Round 3 Critical Redundancy Guards

```text
5 / 29     → foundational type/function definitions versus RETYPE governing claim
26 / 29    → SUB/RETYPE decision boundary versus full projection theory
29 / 30    → conceptual projection logic versus operation signature
30 / 31–35 → generic PROJECT_AS procedure versus family-specific conditions
31 / 32    → later frame-function versus wider-path macro-event function
33 / 35    → recurrent trajectory form versus operator-weighting profile
34 / 35    → composite functional formation versus profile description
36 / 37    → comparison among projections versus projection/analogy classification
37 / 38    → semantic-status boundary versus formal error taxonomy
38 / 50    → RETYPE-specific claim rescue versus system-wide anti-immunization
39 / 41–53 → local RETYPE limits versus integrated LIMITS
40 / 53    → local RETYPE audit versus integrated STRATA audit
```

## 47. Round 3 Completion Gate

Round 3 is provisionally complete only when:

- exactly twelve new contracts exist for Chapters 29–40;
- the accumulated file contains exactly Chapters 0–40 without gaps or duplicates;
- origin type and target function remain separate throughout;
- every PROJECT_AS candidate requires target context, target level, validity scope, source trace, counterfactual test, loss, and alternatives;
- PROJECT_AS is distinguished from COMPOSE, DECOMPOSE, and Φ recontextualization;
- trajectory-as-frame and trajectory-as-macro-event remain different target functions;
- recurrent trajectory form is distinguished from single trajectory and superficial similarity;
- composite higher-level functions require relational formation rather than aggregation;
- weighting, modulation, and profiles do not create operators, dependency changes, or person types;
- compatible, competing, non-comparable, and unresolved projections remain distinct;
- projection, analogy, and label substitution have separate minimum conditions;
- type jump, level mixing, scope inflation, person typing, and projection rescue are explicit failures;
- local RETYPE boundaries preserve claim reduction, analogy-only, Stop, Failure, and Non-Capture;
- all operation-specific results map to canonical output classes;
- no result increases authority or changes PMS Base;
- all embedded YAML contracts are syntactically valid;
- Chapters 41–57 and Front Matter may be contracted without unresolved RETYPE classification questions.

**Round status after generation:** `provisionally_complete`  
**Next contract round:** Chapters 41–57 and Front Matter — LIMITS, Conclusion, and orientation layer, output 4/4

---

## 48. Round 4 Scope and Handoff

Round 4 closes all remaining chapter and orientation contracts in three internal passes:

```text
Pass A — LIMITS: Chapters 41–53
Pass B — Conclusion: Chapters 54–57
Pass C — Front Matter: Preface, Status and Scope, Terminology and Notation, How to Read
```

The delivery is compressed into one output, but the dependency order remains LIMITS → Conclusion → Front Matter. Front Matter is oriented by the completed corpus and never supplies independent theory.

## 49. Round 4 Global Rules

1. LIMITS is constitutive across PATH, SUB, RETYPE, and operation chains; it is not a fourth operation or meta-PMS.
2. Chapters 44–45 elaborate the Admissibility Band defined in Chapter 6 without creating a rival definition.
3. Chapter 47 systematizes continuity checks defined in Chapter 5; Chapter 48 systematizes loss fields introduced in Chapter 7.
4. Chapter 53 integrates local audits without replacing their operation-specific results.
5. Conclusion synthesizes established content and introduces no new operation, theory, case evidence, threshold, or authority.
6. Chapter 57 must remain semantically aligned with Chapter 0, Chapter 6, Chapter 41, Chapter 53, README, and the minified kernel.
7. Front Matter contains orientation, notation guidance, status, and navigation only; removing it must not change the theory.
8. Formal completeness, schema validity, and release completion do not establish empirical truth, causality, semantic adequacy, normative validity, or complete capture.
9. Stop, Failure, Claim Reduction, Analogy-Only, Partial Admissibility, and Non-Capture remain reachable at corpus closure.
10. No chapter or front-matter artifact may create person typing, application authority, or authority inheritance.

## 50. Chapter 41 — Why STRATA Must Bound Itself

```yaml
chapter:
  number: '41'
  title: Why STRATA Must Bound Itself
  role_in_work:
    primary_function: Establish LIMITS as constitutive of every STRATA operation rather than as a late cautionary supplement.
    canonical_status: Primary rationale site for recursive risk, vertical authority drift, and the principle that availability
      does not imply admissibility.
    handoff: Hands the general risk architecture to Chapters 42–53 for explicit boundary, continuity, loss, stop, and audit
      rules.
  governing_question: Why must a transformation discipline that increases analytical mobility also make its own stopping and
    failure conditions constitutive?
  required_claim:
    core: An available STRATA operation is not thereby an admissible STRATA operation.
    risk_claim: Recursive composition, decomposition, and projection can create infinite detail, untraceable abstraction,
      arbitrary functionalization, and self-immunization unless bounded locally and system-wide.
    authority_claim: Movement to a finer, broader, or functionally different analytical position does not increase truth,
      validity, or application authority.
    integration_claim: LIMITS already governs PATH, SUB, RETYPE, and every operation chain; Part IV systematizes rather than
      newly imposes these controls.
  required_distinctions:
  - recursive availability versus recursive necessity
  - analytical mobility versus admissibility
  - local limit versus integrated LIMITS
  - vertical movement versus authority gain
  - new transformation versus answer to an objection
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - PMS_STRATA_Claim_Boundary_Minified.md
    - PMS_STRATA_Operation_Signatures_Minified.md
    - PMS_STRATA_Admissibility_Band_Minified.md
    - PMS_STRATA_Minified_Canonical.md
    - Block_Contracts.md
    status_and_navigation_alignment:
    - README.md
    conditional:
    - Chapters 42–53 elaborate the risk classes introduced here.
  must_not_claim:
  - LIMITS is a fourth STRATA operation.
  - Recursion is methodologically preferable whenever technically possible.
  - A higher or finer result inherits more authority.
  - Part IV can override valid local failures.
  - Boundary rules are optional ethical cautions rather than formal constraints.
  required_example:
    minimal_case: A failed projection is followed by a finer decomposition and a broader composition; show that each move
      creates a new claim and cannot erase the initial failure.
    restriction: The case demonstrates the need for LIMITS without pre-empting the detailed tests of Chapters 44–53.
  required_counterpressure:
  - A transformation may be possible but unnecessary.
  - A locally successful operation may render a later chain inadmissible.
  - Further analysis can reduce rather than increase discriminative performance.
  - The correct output may be Stop or Non-Capture.
  redundancy_guard:
    defines_here:
    - constitutive status of LIMITS
    - recursive-risk taxonomy
    - governing LIMITS principle
    - vertical authority drift
    references_only:
    - specific lower and upper boundary definitions from Chapters 44–45
    - anti-immunization procedure from Chapter 50
    - Stop and Non-Capture records from Chapters 51–52
    must_not_duplicate:
    - redefining the three operations
    - presenting LIMITS as meta-PMS
    - duplicating every local PATH, SUB, and RETYPE boundary
  model_relation:
    supplies:
    - global requirement that every operation and chain remains independently admissible
    - recursive-risk flags
    - authority-inheritance prohibition
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    model_limit: The model can require limit checks and preserve prior failures; it cannot decide substantive admissibility
      without source- and context-bound judgment.
  appendix_migration:
    retain_in_chapter:
    - governing LIMITS principle
    - risk rationale
    - relation between local and integrated limits
    migrate:
    - expanded valid/invalid patterns to Appendix H
    - confusion cases to Appendix I
    - integrated audit detail to Appendix N
  completion_test:
  - LIMITS is shown to be constitutive, not supplementary.
  - No fourth operation is created.
  - Recursive availability is separated from necessity.
  - Authority drift and self-immunization are explicit risks.
  - Chapters 42–53 receive non-overlapping assignments.
```

## 51. Chapter 42 — No Ontology of Strata

```yaml
chapter:
  number: '42'
  title: No Ontology of Strata
  role_in_work:
    primary_function: Systematize the anti-ontological status of levels, granularities, parts, composites, and projections.
    canonical_status: Primary LIMITS site for rejecting discrete reality layers, final constituents, ultimate composites,
      and ontological promotion.
    handoff: Constrains every later boundary test and the final claim language of Chapters 54–57.
  governing_question: How can STRATA use vertical, part-whole, and level language without converting its reconstruction grammar
    into an ontology of reality?
  required_claim:
    core: STRATA levels are locally declared analytical relations, not independently existing layers.
    decomposition_claim: DECOMPOSE reconstructs finer structures under a chosen frame and source basis; it does not discover
      final constituents.
    composition_claim: COMPOSE forms selective analytical objects; it does not reveal an ultimate whole.
    projection_claim: PROJECT_AS adds a bounded function; it does not ontologically promote or transform the source object.
    corrective_form: Within frame C and granularity g, X can be reconstructed through Y for claim Q.
  required_distinctions:
  - analytical level versus ontological layer
  - reconstructive part versus fundamental constituent
  - composite object versus totality
  - operator grammar versus world structure
  - functional projection versus ontological promotion
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapter 41 LIMITS rationale
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    conditional:
    - PMS Base may use layered organizational language that STRATA must not ontologize.
  must_not_claim:
  - Reality is composed of Δ–Ψ layers.
  - Finer parts are more fundamental.
  - A composed macro-object is the real whole.
  - A projected function creates a new real stratum.
  - Micro, meso, and macro are universal classes.
  required_example:
    minimal_case: Rewrite an ontological statement about a macrostructure into a frame-, granularity-, and claim-bounded reconstruction.
    required_contrast: Show that two different granularities can both be legitimate without identifying one as the real layer.
  required_counterpressure:
  - An analytical relation can be stable without being ontological.
  - A decomposition may fail to preserve the source object.
  - A coarse reconstruction may outperform a fine one.
  - Some relevant structure may remain outside the grammar.
  redundancy_guard:
    defines_here:
    - anti-ontology rule for strata
    - no-final-constituents rule
    - no-ultimate-composite rule
    - corrective bounded formulation
    references_only:
    - Chapter 0 initial No Ontology boundary
    - Chapter 2 definitions of granularity and relative level
    - Chapter 43 comparative performance
    must_not_duplicate:
    - redefining frame, granularity, or level
    - turning a negative boundary into a metaphysical counter-ontology
  model_relation:
    supplies:
    - ontology-drift markers
    - required local coordinate declarations
    - prohibited ontological interpretations
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    model_limit: Formal validation can detect missing coordinates and prohibited phrases; it cannot prove that a reconstruction
      is ontologically neutral in every substantive use.
  appendix_migration:
    retain_in_chapter:
    - anti-ontology principle
    - corrective formulation
    - key drift markers
    migrate:
    - extended non-equivalences to Appendix H
    - borderline formulations to Appendix I
    - notation detail to Appendix B
  completion_test:
  - Levels remain relational and local.
  - No final part or total composite is claimed.
  - Projection does not change ontology.
  - Operator grammar is not world structure.
  - The chapter adds no rival ontology.
```

## 52. Chapter 43 — No Privilege of Finer Resolution or Higher Composition

```yaml
chapter:
  number: '43'
  title: No Privilege of Finer Resolution or Higher Composition
  role_in_work:
    primary_function: Establish symmetrical non-privilege across finer decomposition and broader composition.
    canonical_status: Primary LIMITS site for scale-relative performance, coarse/fine co-validity, and rejection of automatic
      reduction or macro superiority.
    handoff: Prepares the operational lower and upper boundaries in Chapters 44–45.
  governing_question: How should competing granularities and compositional scopes be compared when neither detail nor scale
    carries automatic epistemic priority?
  required_claim:
    core: Neither finer resolution nor higher composition is presumptively better, truer, deeper, or more authoritative.
    comparative_rule: Performance is judged relative to question, frame, source basis, praxis difference, traceability, loss,
      and claim scope.
    co_validity: Coarse and fine reconstructions may be simultaneously valid for different claims if their relations and limits
      remain explicit.
    non_reduction: Micro-support does not entail a macroclaim, and macrofunction does not require micro-homogeneity.
  required_distinctions:
  - finer detail versus greater truth
  - coarse economy versus analytical deficiency
  - micro-support versus macro-entailment
  - macrofunction versus micro-homogeneity
  - co-validity versus forced integration
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapter 41 LIMITS rationale
    - Chapter 42 anti-ontology
    conditional:
    - Chapters 44–45 operationalize the two boundary directions.
  must_not_claim:
  - Finer analysis is always preferred.
  - Broader composition explains more by definition.
  - A local finding automatically scales upward.
  - A stable macrofunction proves homogeneous components.
  - All granularities must be merged into one representation.
  required_example:
    minimal_case: Compare a coarse reconstruction that preserves a stable function with a finer reconstruction that reveals
      heterogeneous production conditions; retain both claims without collapse.
    required_failure: Show a finer reconstruction whose extra detail falls below the Relevance Floor.
  required_counterpressure:
  - Fine detail may obscure relations.
  - A coarse claim may be more source-supported.
  - Two granularities may be incomparable.
  - A macro-object may lose traceable load.
  redundancy_guard:
    defines_here:
    - symmetrical non-privilege rule
    - scale-relative comparative criteria
    - coarse/fine co-validity
    - no automatic reduction
    references_only:
    - Chapter 2 multiple granularities
    - Chapters 25 and 27 SUB results
    - Chapter 39 RETYPE boundaries
    must_not_duplicate:
    - defining the Relevance Floor or Traceability Ceiling in full
    - equating plural validity with universal compatibility
  model_relation:
    supplies:
    - granularity-comparison fields
    - non-privilege constraints
    - co-valid and non-comparable result options
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    model_limit: The model can record comparison criteria and output status; it cannot rank granularities independently of
      the substantive claim and source basis.
  appendix_migration:
    retain_in_chapter:
    - comparative rule
    - micro/macro non-equivalences
    - co-validity statement
    migrate:
    - extended comparison tests to Appendix G
    - granularity conflicts to Appendix I
  completion_test:
  - Both analytical directions are limited symmetrically.
  - Coarse and fine claims can coexist without hierarchy.
  - No automatic reduction or entailment is allowed.
  - Comparison criteria are explicit and claim-relative.
  - The chapter hands distinct tasks to Chapters 44 and 45.
```

## 53. Chapter 44 — Praxeological Relevance Floor

```yaml
chapter:
  number: '44'
  title: Praxeological Relevance Floor
  role_in_work:
    primary_function: Operationalize the system-wide lower admissibility boundary for added distinctions and finer reconstruction.
    canonical_status: Primary LIMITS elaboration and test site for PraxisPurchase, the Changed-Reconstruction Test, resolution
      neutrality, and lower mandatory Stop.
    handoff: Feeds the integrated admissibility rules and audit stages in Chapters 51 and 53.
  governing_question: When does an added distinction change a warranted praxis reconstruction rather than merely increase
    descriptive resolution?
  required_claim:
    core: Below the Praxeological Relevance Floor, additional resolution is distinction without praxeological purchase.
    purchase_rule: An added distinction must alter at least one warranted claim concerning action corridors, costs, exposure,
      roles, asymmetries, expectations, non-events, bindings, temporality, irreversibility, integration, or stop.
    changed_reconstruction_test: The analyst must identify which defensible statement would be formulated differently because
      of the distinction.
    negative_result: A correct but non-changing distinction may yield resolution_neutral; it does not count as resolution
      gain.
    stop_rule: If no claim or praxis reconstruction changes and no hidden loss becomes visible, further differentiation stops.
  required_distinctions:
  - detail versus difference
  - PraxisPurchase versus action advice
  - resolution gain versus resolution neutrality
  - lower failure versus source failure
  - claim-relative relevance versus universal threshold
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapter 43 non-privilege
    conditional:
    - PATH, SUB, and RETYPE local lower boundaries provide operation-specific applications.
  must_not_claim:
  - More detail is inherently more relevant.
  - Relevance requires practical intervention or controllability.
  - A neutral result is a failed analysis.
  - One universal smallest relevant unit exists.
  - A numerical score can compensate for absent PraxisPurchase.
  required_example:
    minimal_case: Add a plausible component distinction to a decomposition and show exactly which claim, cost distribution,
      or alternative changes.
    required_negative: Add further detail that changes nothing and classify it as resolution_neutral or mandatory_stop.
  required_counterpressure:
  - The expected gain may not materialize.
  - A distinction may be relevant for one claim and irrelevant for another.
  - Source precision may end before relevance can be tested.
  - The coarser reconstruction may remain preferable.
  redundancy_guard:
    defines_here:
    - system-wide Relevance Floor
    - PraxisPurchase dimensions
    - Changed-Reconstruction Test
    - lower Stop condition
    - resolution-neutral interpretation
    references_only:
    - Chapter 6 compact definition
    - Chapter 25 SUB resolution classes
    - local operation boundaries
    must_not_duplicate:
    - inventing universal thresholds
    - reducing relevance to usefulness or intervention
    - redefining all local tests
  model_relation:
    supplies:
    - relevance-floor record fields
    - affected praxis dimensions
    - changed-claim requirement
    - lower-bound result mapping
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - PMS-STRATA.yaml
    model_limit: The model can require an asserted changed reconstruction and map outputs; it cannot determine whether the
      asserted praxis difference is substantively warranted.
  appendix_migration:
    retain_in_chapter:
    - canonical formulation
    - Changed-Reconstruction Test
    - negative-result rule
    - mandatory lower Stop
    migrate:
    - extended tests to Appendix G
    - lower-bound patterns to Appendix H
    - case variants to Appendix I
  completion_test:
  - PraxisPurchase is defined without numerical scoring.
  - At least one changed warranted reconstruction is required.
  - Resolution neutrality remains a legitimate output.
  - Source limitation is distinguished from absent relevance.
  - The lower Stop rule is explicit.
```

## 54. Chapter 45 — Praxeological Traceability Ceiling

```yaml
chapter:
  number: '45'
  title: Praxeological Traceability Ceiling
  role_in_work:
    primary_function: Operationalize the system-wide upper admissibility boundary for composition and functional projection.
    canonical_status: Primary LIMITS elaboration and test site for TraceableLoad, Constitutive Source Trace, source-target
      dependency, macro-label elasticity, and upper Stop.
    handoff: Supplies the upper-bound logic used by Chapters 46–53 and the formal model.
  governing_question: When does a broader composition or projected function cease to carry reconstructible praxis load from
    its source structures?
  required_claim:
    core: Above the Praxeological Traceability Ceiling, abstraction becomes a label without traceable source structure.
    load_rule: TraceableLoad requires identifiable load-bearing source features, preserved relations and temporality, visible
      cost and asymmetry structure, and target sensitivity to relevant source change.
    trace_rule: Citation alone is insufficient; the target claim must depend structurally and functionally on the declared
      source.
    non_exhaustive_rule: Traceability requires preservation of the load-bearing path, not complete or lossless reproduction.
    stop_rule: Claim reduction or mandatory Stop is required when the target becomes source-indifferent, purely metaphorical,
      or historically untraceable.
  required_distinctions:
  - traceability versus citation
  - load-bearing trace versus exhaustive reproduction
  - abstraction versus macro-label elasticity
  - source-target dependency versus association
  - upper Stop versus claim reduction
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapter 43 non-privilege
    - Chapter 44 Relevance Floor
    conditional:
    - COMPOSE and PROJECT_AS provide principal operation-specific applications; DECOMPOSE uses source-function traceability.
  must_not_claim:
  - A source list proves traceability.
  - Every source detail must be retained.
  - A broad label is valid if rhetorically coherent.
  - Target stability under opposite sources strengthens the claim.
  - Traceability establishes causality or truth.
  required_example:
    minimal_case: Construct a macro-event claim with explicit load-bearing phases, preserved duration, and a source change
      that would alter the target claim.
    required_failure: Show an elastic macro-label that survives contradictory source structures and must be reduced or stopped.
  required_counterpressure:
  - Compression may remain admissible despite major detail loss.
  - A plausible target may lack enough source dependency.
  - Several source traces may support competing targets.
  - Available sources may leave the ceiling underdetermined.
  redundancy_guard:
    defines_here:
    - system-wide Traceability Ceiling
    - TraceableLoad
    - Constitutive Source Trace minimum
    - macro-label elasticity test
    - mandatory upper response
    references_only:
    - Chapter 6 compact definition
    - Chapter 30 PROJECT_AS trace fields
    - Chapter 15 COMPOSE loss
    - Chapter 27 coarser-function traceability
    must_not_duplicate:
    - requiring exhaustive source reproduction
    - conflating source trace with causal proof
    - redefining operation-specific records
  model_relation:
    supplies:
    - traceability-ceiling fields
    - constitutive source trace classes
    - source-target dependency check
    - upper-bound output mapping
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can require source-trace structure and counterfactual dependency declarations; it cannot establish
      that the selected features truly carry the target function.
  appendix_migration:
    retain_in_chapter:
    - canonical formulation
    - TraceableLoad conditions
    - non-exhaustive rule
    - upper Stop and reduction conditions
    migrate:
    - extended upper-bound tests to Appendix G
    - valid/invalid traces to Appendix H
    - macro-label cases to Appendix I
  completion_test:
  - TraceableLoad is more than citation.
  - Constitutive features and preserved relations are required.
  - Exhaustiveness is explicitly rejected.
  - Source-target dependency is testable in principle.
  - Claim reduction and Stop remain distinct.
```

## 55. Chapter 46 — Counterfactual Sensitivity

```yaml
chapter:
  number: '46'
  title: Counterfactual Sensitivity
  role_in_work:
    primary_function: Define the common load test for whether a transformation result depends on the source features declared
      as constitutive.
    canonical_status: Primary system-wide definition site for relevant source modification, sensitivity classes, operation-specific
      variants, and source-bounded counterfactuals.
    handoff: Provides a shared test to continuity, anti-immunization, local audits, and the integrated audit.
  governing_question: Would a relevant change to a declared load-bearing source feature alter the transformation result, and
    what follows when that test is weak or unavailable?
  required_claim:
    core: Counterfactual Sensitivity tests source dependence; it does not prove causality, empirical law, or full validation.
    relevance_rule: The modified feature must have been declared constitutive, strongly modulating, temporally load-bearing,
      or functionally necessary.
    classes:
    - strongly_sensitive
    - partially_sensitive
    - weakly_sensitive
    - insensitive
    - underdetermined
    - untestable
    operation_variants:
      COMPOSE: change order, branch, event, or non-event
      DECOMPOSE: change or remove a component or relation
      PROJECT_AS: change the source feature claimed to carry the target function
    claim_effect: Weak, underdetermined, or untestable results require bounded status, claim reduction, Stop, or Non-Capture
      as appropriate.
  required_distinctions:
  - source-grounded counterfactual versus speculative scenario
  - sensitivity versus causality
  - constitutive versus incidental variation
  - insensitive result versus robust result
  - untestable versus false
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapters 44–45
    conditional:
    - Operation-specific tests from Chapters 15, 20, and 30.
  must_not_claim:
  - Counterfactual Sensitivity proves causal necessity.
  - Any imaginable source change is admissible.
  - An untestable claim is automatically true or false.
  - Insensitivity always means robustness.
  - The test can exceed available source knowledge.
  required_example:
    minimal_case: For one operation of each kind, alter a declared load-bearing feature and state the expected target change
      and claim effect.
    required_failure: Show a target label that remains unchanged under opposite constitutive sources.
  required_counterpressure:
  - The relevant counterfactual may be unavailable.
  - Partial sensitivity may support only a bounded claim.
  - A feature thought constitutive may prove replaceable.
  - Multiple target responses may remain plausible.
  redundancy_guard:
    defines_here:
    - system-wide Counterfactual Sensitivity test
    - sensitivity classes
    - source-bounded variation rule
    - operation-specific test forms
    references_only:
    - local counterfactual tests in PATH, SUB, RETYPE
    - Chapter 45 source-target dependency
    - Chapter 50 anti-immunization
    must_not_duplicate:
    - turning the test into causal inference
    - inventing unsupported alternate histories
    - duplicating family-specific examples
  model_relation:
    supplies:
    - counterfactual-test fields
    - sensitivity enum
    - claim-effect mapping
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can validate declared features, changes, expected responses, and classes; it cannot infer real
      counterfactual outcomes or causality.
  appendix_migration:
    retain_in_chapter:
    - core question
    - sensitivity taxonomy
    - source-discipline rule
    - claim effects
    migrate:
    - extended counterfactual tests to Appendix G
    - stress patterns to Appendix H
    - case records to Appendix I
  completion_test:
  - Relevant modifications are tied to declared load-bearing features.
  - All six sensitivity classes are reachable.
  - Untestability produces bounded outputs rather than immunity.
  - Operation-specific forms remain distinct.
  - No causal proof is claimed.
```

## 56. Chapter 47 — Reference, Type, and Function Continuity

```yaml
chapter:
  number: '47'
  title: Reference, Type, and Function Continuity
  role_in_work:
    primary_function: Systematize continuity checks across transformations and operation chains.
    canonical_status: Primary LIMITS audit site for Reference Continuity, Functional Continuity, Temporal Continuity,
      and the type-continuity view under canonical TypeIntegrity, plus discontinuity effects.
    handoff: Hands explicit continuity matrices and claim-reduction rules to Chapters 50–53.
  governing_question: What must remain continuous for a transformation to refer to the same object, preserve its type, and
    sustain its claimed function without pretending to be lossless?
  required_claim:
    core: Reference, functional, and where relevant temporal continuity are distinct and must be separately declared;
      type continuity is a continuity view under canonical TypeIntegrity, not a new Rule.
    reference: The same historical or structural referent remains identifiable through preserved constitutive relations.
    type: Origin type remains visible; components and target functions do not automatically rewrite it.
    function: The claimed function remains dependent on concrete source features within a bounded context.
    temporal: For PATH-derived objects, order, duration, sedimentation, and historical load remain reconstructible enough
      for the claim.
    failure_effect: Partial discontinuity may require narrower scope, provisional status, analogy-only, claim reduction, Stop,
      or failure.
  required_distinctions:
  - reference continuity versus nominal sameness
  - type-continuity view under TypeIntegrity versus functional continuity
  - functional continuity versus semantic analogy
  - temporal continuity versus complete chronology
  - partial continuity versus total validity
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapters 45–46
    conditional:
    - Chapters 15, 20, and 30 specify operation-specific preservation duties.
  must_not_claim:
  - All continuity types rise or fall together.
  - Nominal identity proves reference continuity.
  - Target function can overwrite origin type.
  - Temporal continuity requires preserving every detail.
  - Any discontinuity forces identical outcomes.
  required_example:
    minimal_case: Audit a COMPOSE → PROJECT_AS chain with separate reference, type, function, and temporal continuity results.
    required_failure: Show a projection where the source name persists but the historical referent and load-bearing relations
      have changed.
  required_counterpressure:
  - Reference may remain while function fails.
  - Type may remain while target scope narrows.
  - Temporal evidence may be partial.
  - A later operation may preserve some continuity dimensions and break others.
  redundancy_guard:
    defines_here:
    - continuity matrix with TypeIntegrity view
    - continuity failure classes
    - claim effects of partial continuity
    references_only:
    - Chapter 5 foundational definitions
    - operation-specific preservation requirements
    - Chapter 53 integrated audit
    must_not_duplicate:
    - redefining origin type or target function
    - equating continuity with losslessness
    - forcing one binary continuity result
  model_relation:
    supplies:
    - continuity matrix fields
    - dimension-specific limits
    - continuity-to-output mapping
    model_artifacts:
    - Admissibility_Rules.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    model_limit: The model can require separate continuity declarations and detect forbidden type replacement; it cannot determine
      historical identity from labels alone.
  appendix_migration:
    retain_in_chapter:
    - continuity matrix
    - dimension definitions
    - partial-failure effects
    migrate:
    - formal matrix to Appendix C
    - valid/invalid patterns to Appendix H
    - chain cases to Appendix I
  completion_test:
  - All continuity dimensions are separated and type continuity remains a view under TypeIntegrity rather than a new Rule.
  - Nominal sameness is insufficient.
  - Origin type is protected.
  - Temporal continuity is non-exhaustive.
  - Partial failure maps to bounded outcomes rather than automatic immunity.
```

## 57. Chapter 48 — Compression Loss and Reconstruction Selection

```yaml
chapter:
  number: '48'
  title: Compression Loss and Reconstruction Selection
  role_in_work:
    primary_function: Systematize the selection and loss that occur in every STRATA transformation.
    canonical_status: Primary LIMITS site for preserved, compressed, excluded, uncertain, irrecoverable, selection effects,
      compression debt, and hidden loss.
    handoff: Supplies common loss semantics to source limits, Stop, Non-Capture, and the integrated audit.
  governing_question: How must STRATA disclose what each operation selects, foregrounds, compresses, excludes, leaves uncertain,
    or makes irrecoverable?
  required_claim:
    core: No STRATA transformation is selection-free or lossless.
    loss_classes:
    - preserved
    - compressed
    - excluded
    - uncertain
    - irrecoverable
    selection_rule: Frame, granularity, source, relevance, periodization, and target-function choices shape the result and
      its possible biases.
    compression_debt: Earlier compression can later require SUB reopening, PATH revision, RETYPE reduction, or Non-Capture.
    admissibility_rule: Loss is admissible when disclosed, load-bearing structure remains, and the claim is calibrated to
      what survives.
  required_distinctions:
  - compression versus exclusion
  - uncertainty versus irrecoverability
  - selection versus discovery
  - admissible loss versus hidden loss
  - compression debt versus automatic failure
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - Chapter 47 continuity
    conditional:
    - PROJECT_AS may additionally distinguish foregrounded and backgrounded features.
  must_not_claim:
  - A valid transformation is lossless.
  - Excluded structure is irrelevant by definition.
  - Uncertainty may be translated into precise structure.
  - A loss record is optional when the target is clear.
  - Compression debt proves the original operation invalid.
  required_example:
    minimal_case: Compare loss profiles for one COMPOSE, DECOMPOSE, and PROJECT_AS record.
    required_failure: Show a target claim whose apparent coherence depends on hidden exclusion of a counterpath or asymmetry.
  required_counterpressure:
  - A large loss can still be admissible if load-bearing structure survives.
  - A small exclusion can overturn a claim.
  - Irrecoverability may predate the operation.
  - Different selections can yield competing admissible reconstructions.
  redundancy_guard:
    defines_here:
    - system-wide loss classes
    - selection-effect rule
    - compression debt
    - hidden-loss criterion
    references_only:
    - Chapter 7 Shared Transformation Record
    - operation-specific loss fields
    - Chapter 49 source limits
    must_not_duplicate:
    - creating a second transformation record
    - equating all omission with failure
    - redefining source support
  model_relation:
    supplies:
    - loss object semantics
    - selection declarations
    - compression-debt flag
    - hidden-loss failure conditions
    model_artifacts:
    - Transformation_Record.schema.json
    - Admissibility_Rules.yaml
    - Boundary_Decision_Tree.yaml
    - PMS-STRATA.yaml
    model_limit: The model can require loss categories and exclusions; it cannot know whether an omission is substantively
      load-bearing unless the record and sources establish it.
  appendix_migration:
    retain_in_chapter:
    - five common loss classes
    - selection effects
    - compression debt
    - admissible-loss rule
    migrate:
    - full schema to Appendix C
    - operation templates to Appendices D–F
    - loss patterns to Appendix H
  completion_test:
  - All operations are explicitly selective.
  - Loss classes are mutually intelligible and non-exhaustive where needed.
  - Hidden loss is distinguishable from disclosed compression.
  - Compression debt allows later revision without pretending invertibility.
  - No second record grammar is introduced.
```

## 58. Chapter 49 — Source Limits and Calibration Limits

```yaml
chapter:
  number: '49'
  title: Source Limits and Calibration Limits
  role_in_work:
    primary_function: Bound formal precision, inferential distance, and threshold claims by the actual source basis and calibration
      capacity.
    canonical_status: Primary LIMITS site for Source Ceiling, no-record/non-event separation, inferential distance, calibration
      loss, and technical formalization boundaries.
    handoff: Supplies source and calibration checks to Anti-Immunization, Stop, Non-Capture, and the integrated audit.
  governing_question: How far may STRATA reconstruct or formalize when the source basis, threshold calibration, or semantic
    comparability is incomplete?
  required_claim:
    core: Formal precision may not exceed the epistemic precision of the sources.
    missing_source_rule: No record is not a recorded non-occurrence, and an unknown event is not a non-event.
    distance_rule: Greater inferential distance requires stronger justification, loss disclosure, alternatives, and claim
      reduction.
    calibration_rule: Thresholds must remain comparable and falsifiable enough to distinguish cases; STRATA does not supply
      universal thresholds.
    source_ceiling: When further structure would be model assumption rather than source-supported reconstruction, the Source
      Ceiling is reached.
    formalization_boundary: Machine readability and schema validity establish consistency, not empirical truth, causality,
      semantic adequacy, or normative validity.
  required_distinctions:
  - source absence versus non-event
  - direct support versus inferred structure
  - source ceiling versus relevance floor
  - calibration openness versus conceptual vagueness
  - formal validity versus substantive validity
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapter 48 loss and selection
    conditional:
    - PMS.yaml computational and claim boundaries.
  must_not_claim:
  - Missing data is Λ.
  - Schema-valid output is empirically valid.
  - Universal numeric thresholds are required.
  - Greater formal detail compensates for weak sources.
  - Calibration uncertainty may be hidden by provisional terminology.
  required_example:
    minimal_case: A structurally plausible decomposition reaches the Source Ceiling before the expected component relation
      can be established and receives a source-limited output.
    required_contrast: A calibration-open result identifies form while leaving the threshold explicitly unresolved.
  required_counterpressure:
  - The best available reconstruction may remain underdetermined.
  - Different source types support different claims.
  - A threshold may be useful yet calibration-sensitive.
  - Technical formalization can expose inconsistency without resolving substance.
  redundancy_guard:
    defines_here:
    - Source Ceiling
    - source/non-event distinction
    - inferential-distance rule
    - calibration-loss criteria
    - technical formalization boundary
    references_only:
    - Chapter 2 Source Scope
    - Chapter 14 non-event expectations
    - Chapter 25 source overreach
    - PMS Base model boundary
    must_not_duplicate:
    - redefining Λ
    - treating source limits as Non-Capture automatically
    - specifying universal empirical thresholds
  model_relation:
    supplies:
    - source-and-calibration record fields
    - support-status enums
    - source-ceiling trigger
    - formalization limit flags
    model_artifacts:
    - Admissibility_Rules.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.schema.json
    model_limit: The model can validate source-status declarations and prevent unsupported certainty labels; it cannot evaluate
      the real adequacy of evidence or thresholds automatically.
  appendix_migration:
    retain_in_chapter:
    - source-bounded principle
    - no-record distinction
    - Source Ceiling
    - calibration-open result
    - technical boundary
    migrate:
    - source/calibration records to Appendix C
    - stress cases to Appendices G and I
    - technical notes to Appendix B
  completion_test:
  - Missing source and non-event remain distinct.
  - Inferential distance has explicit claim effects.
  - Source Ceiling and calibration loss are operationalized.
  - Universal thresholds are rejected.
  - Formalization does not become self-validation.
```

## 59. Chapter 50 — Anti-Immunization

```yaml
chapter:
  number: '50'
  title: Anti-Immunization
  role_in_work:
    primary_function: Prevent shifts of granularity, level, frame, composition, or target function from erasing prior failure
      or absorbing rivals.
    canonical_status: Primary system-wide rule and procedure for failure preservation, granularity escape, higher-level escape,
      projection rescue, rival sensitivity, and the translation success trap.
    handoff: Constrains Stop, Non-Capture, integrated audit, conclusion, and all later corpus production.
  governing_question: How can STRATA remain transformatively flexible without making every objection disappear through a new
    analytical position?
  required_claim:
    core: A change of granularity, level, composition, or target function creates a new testable reconstruction; it does not
      erase the failure of the claim from which the transformation began.
    failure_preservation: The original claim, objection, result, and transformed successor claim remain separately recorded.
    escape_rule: A move is admissible only when it supplies a declared operation, additional praxis difference, independent
      tests, and a direct disposition of the original objection.
    rival_rule: STRATA must preserve the possibility that a different granularity, composition, projection, or external model
      performs better.
    success_trap: Translatability into PMS language is not evidence of superiority, completeness, or semantic identity.
  required_distinctions:
  - answering versus moving an objection
  - new claim versus repaired old claim
  - granularity escape versus warranted decomposition
  - projection rescue versus independent projection
  - translation success versus validation
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - Chapters 41 and 49
    conditional:
    - Chapter 38 RETYPE-specific rescue errors.
  must_not_claim:
  - A higher level dissolves a local counterexample.
  - A finer analysis automatically repairs a coarse failure.
  - A successful PROJECT_AS validates the source typing.
  - Everything translatable into PMS confirms PMS.
  - Rival superiority is excluded after an admissible STRATA result.
  required_example:
    minimal_case: Preserve a failed trajectory claim, then separately test a narrower path claim and a new target-function
      projection without rewriting the initial result.
    required_failure: Show a granularity shift used only to postpone an objection.
  required_counterpressure:
  - The transformed claim may also fail.
  - The rival may be more parsimonious or empirically adequate.
  - No transformation may be the best option.
  - A successful translation may still be analogy-only.
  redundancy_guard:
    defines_here:
    - system-wide Anti-Immunization Rule
    - failure-preservation record logic
    - escape test
    - rival-sensitivity requirement
    - success-trap warning
    references_only:
    - local operation failures
    - Chapter 38 projection rescue
    - Chapter 53 audit stage
    must_not_duplicate:
    - reopening the merits of every earlier claim
    - treating all revision as immunization
    - creating a tribunal over rival theories
  model_relation:
    supplies:
    - prior-claim preservation fields
    - new-operation linkage
    - objection-disposition status
    - rival option requirement
    model_artifacts:
    - Admissibility_Rules.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    model_limit: The model can preserve records and flag undeclared shifts; it cannot determine whether an objection has been
      substantively answered without analysis.
  appendix_migration:
    retain_in_chapter:
    - canonical rule
    - failure-preservation sequence
    - six-question test
    - rival and success-trap clauses
    migrate:
    - invalid patterns to Appendix H
    - escape and rescue cases to Appendix I
    - audit fields to Appendix N
  completion_test:
  - Prior failure remains visible after transformation.
  - Every shift creates an independently testable claim.
  - Rival and no-transformation options remain open.
  - Translation success is not validation.
  - The rule applies across all three operations and chains.
```

## 60. Chapter 51 — Stop Conditions

```yaml
chapter:
  number: '51'
  title: Stop Conditions
  role_in_work:
    primary_function: Define Stop as a positive methodological output and specify general, operation-specific, mandatory,
      optional, reduction, and re-entry rules.
    canonical_status: Primary system-wide Stop definition and record site.
    handoff: Hands bounded termination logic to Non-Capture, the integrated audit, and all chapter completion gates.
  governing_question: When should a STRATA operation end because its claim is sufficient, its sources or relevance are exhausted,
    or continuation would become methodologically harmful?
  required_claim:
    core: Stop is a positive result that marks the admissible end of a transformation, not a shameful failure to continue.
    general_triggers:
    - no new praxis difference
    - lost traceability
    - Source Ceiling reached
    - calibration decline
    - type-integrity failure
    - objection displacement
    stop_types:
      mandatory: continuation would be inadmissible
      optional: continuation may be possible but is unnecessary for the current claim
    reduction_rule: Before full Stop, claims may reduce from stronger to weaker typed outputs when supported.
    reentry_rule: Later re-entry requires new sources, a new claim, relevant counterstructure, or justified recalibration
      and must be recorded as a new test.
  required_distinctions:
  - Stop versus failure
  - mandatory versus optional Stop
  - claim reduction versus Stop
  - Stop versus Non-Capture
  - re-entry versus silent continuation
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - Chapters 44–50
    conditional:
    - Local Stop conditions from Chapters 16, 27, and 39.
  must_not_claim:
  - Analysis should continue whenever another operation is possible.
  - Stop means the claim is false.
  - Optional and mandatory Stop are interchangeable.
  - Re-entry may resume without a new record.
  - Claim reduction is cosmetic relabeling.
  required_example:
    minimal_case: Show one mandatory Stop below the Relevance Floor, one optional Stop after a sufficient bounded claim, and
      one later re-entry triggered by new sources.
    required_mapping: Map each result to canonical output classes.
  required_counterpressure:
  - Stopping may preserve a valid partial result.
  - A failed strong claim may reduce to a supported weaker claim.
  - New sources may reopen a stopped question.
  - Non-Capture may be more appropriate than Stop when the object remains structurally resistant.
  redundancy_guard:
    defines_here:
    - positive Stop concept
    - general Stop triggers
    - mandatory/optional distinction
    - claim-reduction sequence
    - re-entry record
    references_only:
    - operation-specific local Stops
    - Chapter 52 Non-Capture
    - Chapter 53 integrated audit
    must_not_duplicate:
    - turning Stop into a universal end state
    - erasing preserved results
    - allowing unrecorded re-entry
  model_relation:
    supplies:
    - Stop record fields
    - trigger taxonomy
    - mandatory flag
    - claim-before/after mapping
    - re-entry conditions
    model_artifacts:
    - Output_Classes.yaml
    - Admissibility_Rules.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can detect declared triggers and output mappings; it cannot decide whether the substantive claim
      is sufficient or continuation harmful without context.
  appendix_migration:
    retain_in_chapter:
    - positive Stop definition
    - general and part-specific triggers
    - mandatory/optional distinction
    - claim reduction
    - re-entry rule
    migrate:
    - full Stop schema to Appendix C
    - Stop patterns to Appendix G/H
    - cases to Appendix I
  completion_test:
  - Stop remains a positive output.
  - Mandatory and optional Stop are distinct.
  - Claim reduction preserves supported content.
  - Re-entry is a new recorded test.
  - Stop does not erase failure or become Non-Capture by default.
```

## 61. Chapter 52 — Non-Capture

```yaml
chapter:
  number: '52'
  title: Non-Capture
  role_in_work:
    primary_function: Define and classify the legitimate result that present PMS-STRATA cannot adequately reconstruct, compose,
      decompose, or project the object.
    canonical_status: Primary system-wide definition and record site for source, granularity, compositional, projection, calibration,
      semantic, and partial Non-Capture.
    handoff: Preserves openness to rivals and supplies the terminal non-capture logic used by the integrated audit and final
      claim boundary.
  governing_question: How should STRATA record structures that remain only partially reconstructible, non-projectable, or
    better captured outside the present grammar?
  required_claim:
    core: Non-Capture is a reasoned result about the limits of the present reconstruction, not a refuge from a weak claim.
    forms:
    - source_non_capture
    - granularity_non_capture
    - compositional_non_capture
    - projection_non_capture
    - calibration_non_capture
    - semantic_non_capture
    - partial_capture
    justification_rule: The record identifies what was attempted, what was captured, what remains uncaptured, the limiting
      condition, alternatives or rivals, claim effect, and re-entry condition.
    remainder_rule: Uncaptured or non-operator remainders do not automatically become new PMS operators.
    rival_rule: A rival model may be more accurate, parsimonious, empirical, or semantically adequate.
  required_distinctions:
  - Non-Capture versus failure avoidance
  - partial capture versus total failure
  - source limitation versus semantic resistance
  - non-operator remainder versus new primitive
  - rival superiority versus PMS invalidity
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - Chapters 49–51
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    conditional:
    - Appendix L handles extended remainder cases.
  must_not_claim:
  - Non-Capture immunizes the analyst from criticism.
  - Anything not captured becomes a new operator.
  - Partial capture proves full adequacy.
  - Rival superiority is impossible within PMS.
  - Non-Capture and Stop are identical.
  required_example:
    minimal_case: A set of competing decompositions captures different load-bearing relations but cannot be integrated without
      destroying the source function; record partial capture and the unresolved remainder.
    required_contrast: Show a simple failed transformation that should not be mislabeled Non-Capture.
  required_counterpressure:
  - The object may be better captured elsewhere.
  - No available granularity may satisfy relevance, source support, and traceability together.
  - Competing reconstructions may remain equally strong.
  - Later evidence may permit re-entry.
  redundancy_guard:
    defines_here:
    - Non-Capture definition
    - Non-Capture forms
    - partial-capture record
    - non-operator remainder rule
    - rival-superiority clause
    references_only:
    - Chapter 51 Stop
    - local Non-Capture outputs
    - Chapter 50 rival sensitivity
    must_not_duplicate:
    - using Non-Capture to hide an avoidable failure
    - inventing new operators from remainders
    - claiming total semantic exteriority without evidence
  model_relation:
    supplies:
    - Non-Capture record fields
    - capture-status categories
    - limiting-condition taxonomy
    - rival/re-entry fields
    model_artifacts:
    - Output_Classes.yaml
    - Admissibility_Rules.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    model_limit: The model can require a reasoned Non-Capture record and distinguish it from missing fields; it cannot determine
      that an external model is substantively superior.
  appendix_migration:
    retain_in_chapter:
    - definition
    - forms
    - partial-capture logic
    - remainder and rival rules
    migrate:
    - extended remainders to Appendix L
    - cases to Appendix I
    - record schema to Appendix C
  completion_test:
  - Non-Capture is justified rather than asserted.
  - Partial capture is representable.
  - Remainders do not create primitives.
  - Rivals remain possible.
  - Stop, failure, and Non-Capture remain distinct outputs.
```

## 62. Chapter 53 — Integrated STRATA Admissibility Audit

```yaml
chapter:
  number: '53'
  title: Integrated STRATA Admissibility Audit
  role_in_work:
    primary_function: Integrate the local operation and boundary checks into one audit for individual transformations and
      complete chains.
    canonical_status: Primary and only integrated STRATA audit definition, result mapping, and LIMITS lock site.
    handoff: Closes LIMITS and hands an auditable transformation system to Conclusion, cases, model v0, and later corpus production.
  governing_question: Can a complete transformation or operation chain demonstrate source entry, correct classification, relevance,
    traceability, continuity, sensitivity, loss, alternatives, limits, failure preservation, Stop, Non-Capture, and authority
    restraint?
  required_claim:
    core: The integrated audit coordinates but does not replace PATH, SUB, and RETYPE local audits.
    stages:
    - source_and_claim_entry
    - operation_classification
    - relevance_floor
    - traceability_ceiling
    - continuity_and_type_integrity
    - counterfactual_sensitivity
    - loss_and_selection
    - alternatives
    - source_and_calibration_limits
    - anti_immunization
    - stop_and_non_capture
    - claim_and_authority_ceiling
    result_classes:
    - admissible
    - admissible_with_bounded_claim
    - admissible_but_provisional
    - resolution_neutral
    - analogy_only
    - partially_admissible
    - claim_reduction_required
    - mandatory_stop
    - failed_transformation
    - non_capture
    chain_rule: Every operation in a chain retains its own record, loss, validity scope, and possibility of failure.
    authority_rule: The audit evaluates reconstruction discipline, not persons, morality, legality, policy, diagnosis, or
      practical entitlement.
  required_distinctions:
  - local audit versus integrated audit
  - single operation versus operation chain
  - audit completeness versus substantive truth
  - partially admissible versus provisional
  - claim ceiling versus application authority
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - Chapters 41–52
    conditional:
    - Formal Model v0 will operationalize but not replace the audit.
  must_not_claim:
  - Passing the audit proves truth or causality.
  - The audit is a tribunal over persons or institutions.
  - One chain-level result overwrites operation-level failures.
  - Formal completeness compensates for missing source load.
  - Audit success grants application authority.
  required_example:
    minimal_case: Audit a COMPOSE → PROJECT_AS → DECOMPOSE chain with one bounded success, one claim reduction, preserved
      loss records, and explicit authority ceiling.
    required_failure: Show a syntactically complete chain that fails because its target remains source-insensitive.
  required_counterpressure:
  - A formally complete record may be substantively underdetermined.
  - Different operations in one chain may receive different results.
  - The best integrated result may be partial admissibility or Non-Capture.
  - No-transformation may be the preferred alternative.
  redundancy_guard:
    defines_here:
    - twelve-stage integrated audit
    - integrated result taxonomy
    - chain-record rule
    - LIMITS closing criterion
    references_only:
    - local audits in Chapters 17, 28, and 40
    - Chapter 7 shared record
    - all boundary chapters 41–52
    must_not_duplicate:
    - redefining operation semantics
    - collapsing local results into one score
    - turning audit into empirical or normative adjudication
  model_relation:
    supplies:
    - integrated audit fields
    - chain validation requirements
    - canonical final-result enum
    - authority-ceiling check
    model_artifacts:
    - Admissibility_Rules.yaml
    - Output_Classes.yaml
    - Boundary_Decision_Tree.yaml
    - Transformation_Record.schema.json
    - PMS-STRATA.yaml
    model_limit: The model can validate stages, records, enums, and prohibited inheritance; it cannot decide empirical truth,
      causality, semantic adequacy, or normative validity.
  appendix_migration:
    retain_in_chapter:
    - audit purpose
    - twelve stages
    - result classes
    - final audit questions
    - LIMITS closing statement
    migrate:
    - full audit template to Appendix N
    - extended tests to Appendix G
    - case index to Appendix M
  completion_test:
  - All twelve stages are explicit.
  - Local audit results remain visible.
  - All canonical outputs are reachable without scoring.
  - Operation chains preserve separate records and failures.
  - The audit grants no additional authority.
  - LIMITS is ready for lock.
```

## 63. Chapter 54 — The Integrated STRATA Model

```yaml
chapter:
  number: '54'
  title: The Integrated STRATA Model
  role_in_work:
    primary_function: Synthesize the complete architecture, operations, admissibility logic, and non-invertible chain structure
      without adding theory.
    canonical_status: Primary Conclusion integration site; summary, not a new definition site.
    handoff: Hands the integrated model to Chapters 55–57 for positive provision, negative scope, and final claim closure.
  governing_question: What coherent model results when PMS Base, PATH, SUB, RETYPE, and LIMITS are read as one bounded transformation
    discipline?
  required_claim:
    core: PMS Base supplies the operator grammar; PATH forms temporal objects; SUB opens compressed objects; RETYPE assigns
      bounded contextual functions; LIMITS controls admissibility, loss, failure, Stop, and Non-Capture.
    chain_claim: Operations may form chains only with separate declarations, justifications, loss records, validity scopes,
      and failure possibilities.
    non_invertibility:
    - DECOMPOSE(COMPOSE(X)) != X
    - COMPOSE(DECOMPOSE(X)) != X
    - PROJECT_AS(X) != X as a new origin type
    admissibility_summary: A transformation remains valid only where it is discriminating and reconstructively anchored.
    authority_summary: Integration increases internal control, not ontology or authority.
  required_distinctions:
  - PMS Base versus STRATA method
  - four Parts versus three operations
  - integration versus new meta-layer
  - chain coherence versus reversibility
  - summary versus new claim
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - LIMITS Lock Chapters 41–53
    conditional:
    - Minified Canonical provides the compact control version.
  must_not_claim:
  - Conclusion may repair unresolved theory.
  - The integrated model adds a fourth operation.
  - A complete chain is lossless.
  - Integration proves completeness.
  - The conclusion can strengthen the claim boundary.
  required_example:
    minimal_case: One compact chain diagram showing formation, optional reopening, and bounded projection with independent
      records.
    restriction: No new case evidence or operation family is introduced.
  required_counterpressure:
  - A coherent model may still yield Non-Capture.
  - Some operation sequences may be unavailable or inadmissible.
  - Formal integration does not establish empirical adequacy.
  - Local failures remain preserved.
  redundancy_guard:
    defines_here:
    - integrated architecture summary
    - operation-chain synthesis
    - non-invertibility summary
    references_only:
    - all primary definitions from Chapters 0–53
    - detailed operation and boundary records
    must_not_duplicate:
    - introducing new terminology or tests
    - re-deriving every Part
    - converting synthesis into meta-authority
  model_relation:
    supplies:
    - top-level architecture references
    - operation-chain relations
    - non-invertibility invariants
    model_artifacts:
    - PMS-STRATA.yaml
    - Operation_Registry.yaml
    - Admissibility_Rules.yaml
    model_limit: The model artifact may mirror this synthesis but does not acquire authority over the canonical prose or PMS
      Base.
  appendix_migration:
    retain_in_chapter:
    - integrated architecture
    - non-invertibility
    - shared admissibility summary
    migrate:
    - detailed notation to Appendix B
    - audit detail to Appendix N
  completion_test:
  - All four Parts and three operations appear with correct roles.
  - No new theory or operation is introduced.
  - Non-invertibility and separate chain records remain explicit.
  - Failure and Non-Capture survive integration.
  - Authority remains bounded.
```

## 64. Chapter 55 — What PMS-STRATA Provides

```yaml
chapter:
  number: '55'
  title: What PMS-STRATA Provides
  role_in_work:
    primary_function: State the positive methodological capabilities delivered by the completed work.
    canonical_status: Primary positive-scope inventory in the Conclusion; descriptive of established outputs only.
    handoff: Prepares the symmetrical negative inventory in Chapter 56.
  governing_question: What does the completed STRATA discipline make more explicit, testable, and auditable within PMS?
  required_claim:
    core: STRATA provides explicit vertical transformation discipline and increased internal legibility, not broader authority.
    capabilities:
    - controlled temporal composition
    - granularity-controlled decomposition
    - cross-level functional projection
    - operator-occurrence discipline
    - explicit loss accounting
    - competing reconstruction support
    - counterfactual load testing
    - bounded weighting and profile analysis
    - analogy discipline
    - anti-immunization
    - Stop and Non-Capture
    qualification: Every capability remains source-, frame-, granularity-, context-, claim-, and authority-bounded.
  required_distinctions:
  - capability versus authority
  - legibility versus truth
  - methodological output versus domain finding
  - support for rivals versus forced integration
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - Chapter 54 integration
    conditional:
    - README and Front Matter later present a shorter orientation version.
  must_not_claim:
  - STRATA provides diagnosis, prediction, intervention, ranking, policy, or moral judgment.
  - STRATA guarantees full capture.
  - Counterfactual tests prove causation.
  - Loss accounting makes transformations complete.
  - More legibility creates practical entitlement.
  required_example:
    minimal_case: For each major capability family, point to its established primary chapter and one bounded output.
    restriction: The inventory contains no new examples or promises.
  required_counterpressure:
  - A provided method may legitimately return Stop or Non-Capture.
  - Competing reconstructions may remain unresolved.
  - Technical representation may remain provisional.
  - Another model may perform better.
  redundancy_guard:
    defines_here:
    - positive capability inventory
    - increased-legibility formulation
    references_only:
    - primary methods defined in Chapters 0–53
    - negative scope Chapter 56
    must_not_duplicate:
    - turning summaries into new commitments
    - omitting the claim and authority qualifiers
  model_relation:
    supplies:
    - capability-to-chapter references
    - positive scope tags
    model_artifacts:
    - PMS-STRATA.yaml
    - Cross_Reference_Map.md
    - Reader_Pathways.md
    model_limit: Model and reference artifacts can index provided capabilities but cannot enlarge them.
  appendix_migration:
    retain_in_chapter:
    - capability inventory
    - bounded qualification
    - legibility-not-authority statement
    migrate:
    - full cross-reference detail to 04_reference
    - reader pathways to Reader_Pathways.md
  completion_test:
  - Every listed capability has an established source chapter.
  - No application authority is implied.
  - Stop, Non-Capture, rivals, and competing reconstructions remain included.
  - No capability exceeds PMS Base boundaries.
```

## 65. Chapter 56 — What PMS-STRATA Does Not Provide

```yaml
chapter:
  number: '56'
  title: What PMS-STRATA Does Not Provide
  role_in_work:
    primary_function: State the complete negative scope of the finished system in direct symmetry with its positive capabilities.
    canonical_status: Primary final negative inventory before the closing claim boundary.
    handoff: Hands a stable exclusion set to Chapter 57, README, Front Matter, model metadata, and release audits.
  governing_question: Which interpretations, promises, authorities, ontologies, and guarantees remain outside PMS-STRATA even
    after successful development?
  required_claim:
    core: STRATA does not provide a new PMS Base, superior layer, ontology, final constituents, totality, privileged scale,
      automatic retyping, lossless transformation, unlimited recursion, universal thresholds, causal proof, person typing,
      cross-domain validity, counterexample immunity, application authority, or full-capture guarantee.
    symmetry_rule: Every positive capability in Chapter 55 has an explicit negative ceiling.
    failure_rule: A successful transformation cannot be generalized into claims excluded here.
  required_distinctions:
  - negative boundary versus disclaimer
  - method limit versus model defect
  - no guarantee versus impossibility claim
  - structural result versus person-level attribute
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - Chapters 41–55
    conditional:
    - PMS.yaml prohibited-use and computational boundaries.
  must_not_claim:
  - The negative list is optional framing.
  - Absence of guarantee means failure of the method.
  - A strong case may override a listed exclusion.
  - Technical execution proves cross-domain validity.
  - A configuration-level function can become a person property.
  required_example:
    minimal_case: Pair each principal positive provision with the corresponding prohibited inference.
    required_focus: Include no causal proof, no person typing, no authority inheritance, and no full-capture guarantee.
  required_counterpressure:
  - Some excluded claims may be studied by other methods.
  - A bounded STRATA finding may still be useful.
  - Negative scope does not establish the opposite metaphysical claim.
  - Rival models remain admissible.
  redundancy_guard:
    defines_here:
    - final negative capability inventory
    - positive/negative symmetry rule
    references_only:
    - Chapter 0 initial boundary
    - Chapter 42 anti-ontology
    - PMS Base exclusions
    - Chapter 57 final wording
    must_not_duplicate:
    - inventing new exclusions unrelated to the corpus
    - turning limitations into claims of impossibility
  model_relation:
    supplies:
    - prohibited-claim registry
    - authority and use exclusions
    model_artifacts:
    - PMS-STRATA.yaml
    - Admissibility_Rules.yaml
    - Claim_Type_Table.md
    model_limit: The model can expose prohibited claim categories; it cannot police every future rhetorical misuse automatically.
  appendix_migration:
    retain_in_chapter:
    - complete negative inventory
    - symmetry with Chapter 55
    - non-override rule
    migrate:
    - full prohibited-use index to Claim_Type_Table.md
    - valid/invalid formulations to Appendix H
  completion_test:
  - All major exclusions from Chapter 0 and PMS Base reappear consistently.
  - No new metaphysical counterclaim is created.
  - Person typing and application authority are expressly excluded.
  - No successful case can override the inventory.
  - Chapter 57 can close without adding a missing boundary.
```

## 66. Chapter 57 — Final Claim Boundary

```yaml
chapter:
  number: '57'
  title: Final Claim Boundary
  role_in_work:
    primary_function: Close the canonical corpus with the exact bounded transformation, failure, Non-Capture, and authority
      rules established throughout the work.
    canonical_status: Final claim-boundary site; must align with Chapter 0, Chapter 6, Chapter 41, Chapter 53, README, and
      all minified kernel files.
    handoff: Provides the release-level governing formulation without creating a further meta-layer.
  governing_question: What is the strongest final claim PMS-STRATA may make after the full architecture and all limits have
    been demonstrated?
  required_claim:
    bounded_extension: STRATA extends explicit method across temporal structures, granular reconstructions, composites, and
      contextual functions; it does not extend PMS ontology or authority.
    central_limit: A transformation is admissible only above distinction without praxeological purchase and below abstraction
      without traceable load.
    governing_distinction: More structure is not more authority.
    transformation_rule:
    - identify source object
    - declare frame, granularity, and relative level
    - specify one of the three operations
    - state expected praxis difference
    - retain constitutive source trace
    - preserve reference and type integrity
    - disclose selection and loss
    - permit counterfactual failure
    - bound validity scope
    - preserve Stop and Non-Capture
    failure_rule: A claim must reduce, stop, fail, or become Non-Capture when its required conditions cannot be sustained.
    authority_rule: No transformation grants normative, diagnostic, person-level, institutional, policy, or intervention authority.
    closure_rule: No further STRATA meta-layer is required or authorized.
  required_distinctions:
  - bounded vertical extension versus meta-PMS
  - transformation legitimacy versus success
  - failure versus Non-Capture
  - method closure versus recursive completeness
  - final claim versus new theory
  dependencies:
    hard:
    - Foundations Lock
    - Chapter 0 claim boundary
    - Chapter 1 object model
    - Chapter 2 analytical coordinates
    - Chapter 3 temporal object chain
    - Chapter 4 operation grammar
    - Chapter 5 type, function, context, and continuity
    - Chapter 6 Admissibility Band
    - Chapter 7 Shared Transformation Record
    - Chapter 8 foundational non-equivalences
    - PATH Lock (Chapters 9–17)
    - SUB Lock (Chapters 18–28)
    - RETYPE Lock (Chapters 29–40)
    - Chapters 41–56
    - PMS_STRATA_Claim_Boundary_Minified.md
    - PMS_STRATA_Operation_Signatures_Minified.md
    - PMS_STRATA_Admissibility_Band_Minified.md
    - PMS_STRATA_Minified_Canonical.md
    - Block_Contracts.md
    status_and_navigation_alignment:
    - README.md
    conditional:
    - Front Matter must orient to this boundary without redefining it.
  must_not_claim:
  - The final chapter may strengthen the Governing Claim.
  - Completion proves universal capture.
  - A further meta-STRATA is required.
  - Successful transformations inherit application authority.
  - Failure can be removed by recursion.
  required_example:
    minimal_case: No new substantive case; include only the canonical transformation rule and final bounded formulation.
    consistency_check: Compare wording against all designated claim-boundary sites.
  required_counterpressure:
  - The final valid result may be partial, stopped, failed, or non-captured.
  - Completion of the corpus does not complete reality.
  - The method remains revisable without a superior layer.
  - External accountability and rival models remain possible.
  redundancy_guard:
    defines_here:
    - final governing formulation
    - ten-part transformation rule
    - failure, Non-Capture, and authority rules
    - no-meta-layer closure
    references_only:
    - all prior definitions and arguments
    - Chapter 0 initial boundary
    - minified kernel wording
    must_not_duplicate:
    - introducing new examples, distinctions, or operations
    - quietly broadening the claim
    - claiming release completeness as theoretical completeness
  model_relation:
    supplies:
    - final claim metadata
    - release boundary invariants
    - authority prohibition
    model_artifacts:
    - PMS-STRATA.yaml
    - Admissibility_Rules.yaml
    - Claim_Type_Table.md
    model_limit: Formal artifacts must mirror this boundary but cannot substitute for or exceed it.
  appendix_migration:
    retain_in_chapter:
    - final claim
    - transformation rule
    - failure and authority rules
    - closing statement
    migrate:
    - none required beyond cross-reference synchronization
  completion_test:
  - Wording aligns with Chapter 0, 6, 41, 53, README, and minified kernel.
  - All ten transformation conditions appear.
  - Failure, Stop, Non-Capture, and rivals remain possible.
  - No authority or ontology is added.
  - No further meta-layer is proposed.
```

## 67. FM-PREFACE — Preface

```yaml
chapter:
  number: FM-PREFACE
  title: Preface
  role_in_work:
    primary_function: Explain the development context, motivating gap, and provisional internal-specification status of PMS-STRATA.
    canonical_status: Orientation artifact only; not a primary theory, definition, evidence, or authority site.
    handoff: Introduces readers to why the work exists before the formal Status and Scope Note.
  governing_question: What historical and methodological problem motivated STRATA, and what expectations should the reader
    bring to the work?
  required_claim:
    core: STRATA arose to make previously implicit vertical PMS operations explicit and bounded.
    orientation: It is a precision of method rather than an extension of the Δ–Ψ grammar.
    status: The text is presented according to its actual development and release status, without implying completeness or
      empirical validation.
  required_distinctions:
  - development history versus theoretical proof
  - motivation versus governing claim
  - precision versus extension
  - internal specification versus finished universal theory
  dependencies:
    hard:
    - Completed Chapters 0–57
    status_and_navigation_alignment:
    - README.md
    conditional:
    - May reference project history and development sequence without importing add-on lenses as authorities.
  must_not_claim:
  - The preface defines canonical concepts.
  - Development effort proves validity.
  - STRATA was inevitable or universally required.
  - The preface may promise capabilities absent from the corpus.
  required_example:
    minimal_case: A brief motivating example of unmarked vertical movement, without performing a full analysis.
    restriction: No new operator, claim, or evidence enters through narrative framing.
  required_counterpressure:
  - The motivating problem may be narrower than the eventual architecture.
  - Some readers may not need STRATA for simple single-frame reconstructions.
  - Historical narrative must not imply teleology.
  redundancy_guard:
    defines_here:
    - development context
    - motivation
    - actual publication status
    references_only:
    - all canonical definitions from Chapters 0–57
    must_not_duplicate:
    - restating the full introduction
    - using narrative to smuggle stronger claims
  model_relation:
    supplies:
    - front-matter metadata only
    model_artifacts:
    - Reader_Pathways.md
    model_limit: No model artifact derives theoretical rules from the Preface.
  appendix_migration:
    retain_in_chapter:
    - motivation
    - status
    - relationship to PMS Base
    migrate:
    - development chronology may remain in project documentation rather than appendices
  completion_test:
  - No primary definition appears.
  - No capability exceeds Chapter 55.
  - No limitation is weaker than Chapter 56.
  - The narrative is non-teleological.
  - The text can be removed without changing the theory.
```

## 68. FM-STATUS-SCOPE — Status and Scope Note

```yaml
chapter:
  number: FM-STATUS-SCOPE
  title: Status and Scope Note
  role_in_work:
    primary_function: State the authoritative dependency, scope, exclusions, maturity, and use boundaries readers must know
      before entering the corpus.
    canonical_status: Primary front-matter orientation site for project status and scope, but subordinate to Chapter 0, Chapter
      57, README, and PMS Base.
    handoff: Prepares the terminology note and reading guide.
  governing_question: What is the status of this artifact, what does it depend on, and which claims and uses are excluded
    at entry?
  required_claim:
    core: PMS Base is the sole theoretical basis; STRATA uses the existing Δ–Ψ grammar without adding operators or authority.
    scope:
    - no ontology of strata
    - no universal micro-meso-macro hierarchy
    - no claim-type increase
    - no person typing
    - no automatic application authority
    - formal implementation is not truth proof
    add_on_rule: Add-on lenses may appear only as optional later stress vectors and do not ground STRATA rules.
    status_rule: Maturity and release status must match the repository at publication time.
  required_distinctions:
  - theoretical basis versus optional test vector
  - scope note versus final claim boundary
  - formal model versus source of truth
  - development status versus validity
  dependencies:
    hard:
    - PMS.yaml
    - Chapters 0, 56, and 57
    status_and_navigation_alignment:
    - README.md
    conditional:
    - Repository release metadata.
  must_not_claim:
  - Add-on lenses are co-foundational.
  - STRATA changes PMS dependencies.
  - Technical execution validates truth.
  - The scope note can supersede the final claim boundary.
  - Status labels imply empirical validation.
  required_example:
    minimal_case: A concise allowed/not-allowed scope table tied to canonical chapter references.
    restriction: Do not reproduce the entire negative inventory.
  required_counterpressure:
  - Repository status may change while the theory remains bounded.
  - Optional stress vectors may fail to translate.
  - Formal models may be incomplete or provisional.
  redundancy_guard:
    defines_here:
    - front-entry status metadata
    - scope orientation
    - add-on-lens restriction
    references_only:
    - full claim boundaries and exclusions from Chapters 0, 56, and 57
    must_not_duplicate:
    - creating a second source-authority order
    - silently updating theoretical status without repository evidence
  model_relation:
    supplies:
    - release metadata references
    - scope flags
    model_artifacts:
    - PMS-STRATA.yaml
    - Claim_Type_Table.md
    model_limit: The model may expose status metadata but does not derive validity from it.
  appendix_migration:
    retain_in_chapter:
    - status
    - dependency on PMS Base
    - major scope exclusions
    migrate:
    - detailed use constraints to reference tables
  completion_test:
  - Status matches the repository.
  - PMS Base remains sole foundation.
  - No claim or authority inflation appears.
  - Add-on lenses remain optional stress vectors.
  - The note is shorter and weaker than the final boundary.
```

## 69. FM-TERMINOLOGY-NOTATION — Terminology and Notation Note

```yaml
chapter:
  number: FM-TERMINOLOGY-NOTATION
  title: Terminology and Notation Note
  role_in_work:
    primary_function: Orient readers to language, symbols, object labels, coordinates, and the non-law status of formulas
      and schemas.
    canonical_status: Front-matter notation guide only; canonical meanings remain in PMS Base, Foundations, and Appendix B.
    handoff: Prepares readers to interpret English operation names, Δ–Ψ symbols, YAML fields, and relative-level notation
      consistently.
  governing_question: How should the mixed natural-language, symbolic, and machine-readable vocabulary of STRATA be read without
    mistaking notation for ontology or proof?
  required_claim:
    core: English operation names and technical keys coexist with prose, while Δ–Ψ retains PMS Base meanings.
    distinction_rule: Operator sign, operator name, operator type, and concrete occurrence remain separate.
    coordinate_rule: source, target, frame, granularity, relative level, and transformation context have distinct declared
      roles.
    formula_rule: Formulas are specifications and tests, not empirical laws.
    schema_rule: YAML and JSON structures are machine-readable operationalizations, not independent theoretical authority.
  required_distinctions:
  - operator sign versus name versus type versus occurrence
  - frame versus context
  - granularity versus level
  - source versus target
  - specification formula versus empirical law
  - schema validity versus truth
  dependencies:
    hard:
    - PMS.yaml
    - Chapters 1–7
    - Appendix B
    conditional:
    - Glossary and reference kernel.
  must_not_claim:
  - Notation creates new semantics.
  - Symbols are ontological entities.
  - Formula syntax implies quantitative law.
  - YAML keys may silently redefine prose.
  - Relative-level notation is a universal scale.
  required_example:
    minimal_case: Show one compact operation notation and the corresponding prose reading.
    restriction: No new formalism beyond what the corpus and Appendix B support.
  required_counterpressure:
  - The same word may have a narrower technical meaning than ordinary language.
  - A machine-readable field can be syntactically valid but semantically wrong.
  - Some thresholds remain qualitative and context-sensitive.
  redundancy_guard:
    defines_here:
    - front-entry notation conventions
    - status of formulas and schemas
    references_only:
    - canonical definitions
    - full notation catalogue Appendix B
    - Glossary entries
    must_not_duplicate:
    - introducing new symbols or aliases
    - resolving substantive ambiguities by notation alone
  model_relation:
    supplies:
    - notation references only
    model_artifacts:
    - PMS-STRATA.schema.json
    - Glossary.md
    - Operator_Index.md
    - Transformation_Operation_Index.md
    model_limit: Formal schemas may enforce field types but cannot establish semantic correctness.
  appendix_migration:
    retain_in_chapter:
    - language convention
    - symbol distinctions
    - coordinate distinctions
    - formula and schema status
    migrate:
    - full notation to Appendix B and Glossary
  completion_test:
  - No new symbol or meaning is introduced.
  - All coordinate terms match Foundations.
  - Formulas are explicitly non-empirical specifications.
  - Machine readability has no independent authority.
  - The note can be updated only with canonical changes.
```

## 70. FM-HOW-TO-READ — How to Read PMS-STRATA

```yaml
chapter:
  number: FM-HOW-TO-READ
  title: How to Read PMS-STRATA
  role_in_work:
    primary_function: Provide a navigation route through Foundations, PATH, SUB, RETYPE, LIMITS, cases, appendices, reference
      files, and formal model.
    canonical_status: Orientation and reading-path site only; it must not imply a hierarchy of truth or authority among Parts.
    handoff: Completes Front Matter and routes readers into Chapter 0.
  governing_question: In what order and for what purposes should different readers use the corpus, model, cases, appendices,
    and reference layer?
  required_claim:
    core: Foundations precedes operation-specific Parts; PATH, SUB, and RETYPE are locally audited; LIMITS applies throughout
      and is later systematized.
    artifact_rule: Canonical prose, minified controls, formal model, cases, appendices, references, derivatives, and Reader
      have distinct authority and navigation roles.
    reading_paths:
    - full canonical route
    - operation-specific route
    - boundary and audit route
    - formal-model route with prose back-reference
    non_authority_rule: Reading order does not create theoretical rank, and the Reader or derivative artifacts never become
      independent sources of truth.
  required_distinctions:
  - prerequisite order versus authority hierarchy
  - local audit versus integrated audit
  - canonical prose versus formal model
  - source artifact versus derivative or Reader
  dependencies:
    hard:
    - Block_Contracts.md
    - Completed Chapters 0–57
    status_and_navigation_alignment:
    - README.md
    conditional:
    - Reference Kernel and Reader Pathways later provide detailed navigation.
  must_not_claim:
  - Readers may begin with derivatives as sources of truth.
  - LIMITS is relevant only after RETYPE.
  - The model replaces prose.
  - A reading pathway changes claim authority.
  - Front Matter may define shortcuts that skip required dependencies.
  required_example:
    minimal_case: Provide three bounded reader routes and state what each route cannot substitute for.
    restriction: No chapter content is summarized beyond navigational necessity.
  required_counterpressure:
  - Specialist readers may enter through an operation chapter but must follow its dependencies.
  - The model route may reveal formal gaps without deciding substance.
  - Cases illustrate and test rather than define theory.
  redundancy_guard:
    defines_here:
    - front-entry reading routes
    - artifact-role navigation
    - dependency warnings
    references_only:
    - canonical chapter definitions
    - full cross-reference map
    - Reader implementation
    must_not_duplicate:
    - turning navigation into a second architecture
    - assigning authority by reading order
  model_relation:
    supplies:
    - reader pathway references
    - artifact-role metadata
    model_artifacts:
    - Reader_Pathways.md
    - Cross_Reference_Map.md
    - PMS-STRATA.yaml
    model_limit: Navigation tools can surface dependencies and files but cannot perform or validate analysis independently.
  appendix_migration:
    retain_in_chapter:
    - full route
    - specialist routes
    - artifact authority reminders
    migrate:
    - detailed pathways to Reader_Pathways.md and the Reader
  completion_test:
  - Foundations dependencies are visible.
  - LIMITS is described as cross-cutting.
  - Cases, model, appendices, derivatives, and Reader have correct roles.
  - No shortcut creates new authority.
  - The guide routes into Chapter 0 without redefining content.
```

## 71. Round 4 Dependency Chain

```text
41 → establishes why limits are constitutive
42 → blocks ontology of layers
43 → removes privilege from fine and coarse directions
44 → operationalizes the lower relevance boundary
45 → operationalizes the upper traceability boundary
46 → tests source dependence counterfactually
47 → separates reference, type, function, and temporal continuity
48 → discloses selection and loss
49 → bounds sources, calibration, and formalization
50 → preserves failure and blocks analytical escape
51 → defines positive Stop and re-entry
52 → defines reasoned Non-Capture and rival openness
53 → integrates the full admissibility audit
54 → synthesizes the completed model
55 → states positive provisions
56 → states negative provisions
57 → closes the final claim boundary
FM-PREFACE → motivates without defining
FM-STATUS-SCOPE → states status and entry boundaries
FM-TERMINOLOGY-NOTATION → explains language and notation without new semantics
FM-HOW-TO-READ → routes readers without creating authority hierarchy
```

## 72. Round 4 Primary Definition Matrix

| Concept family | Primary contract | Later use without redefinition |
|---|---:|---|
| Constitutive need for LIMITS | 41 | 42–53, Conclusion |
| Anti-ontology of strata | 42 | 43–57, Front Matter |
| Scale non-privilege | 43 | 44–53 |
| Praxeological Relevance Floor | 44 | 51, 53 |
| Praxeological Traceability Ceiling | 45 | 46–53 |
| Counterfactual Sensitivity | 46 | 47, 50, 53 |
| Continuity audit | 47 | 50–53 |
| Loss and selection | 48 | 49–53 |
| Source and calibration limits | 49 | 50–53 |
| Anti-Immunization | 50 | 51–57 |
| Stop | 51 | 52–57 |
| Non-Capture | 52 | 53–57 |
| Integrated audit | 53 | Conclusion, model, cases |
| Integrated model synthesis | 54 | 55–57, Front Matter |
| Positive provision inventory | 55 | README, Front Matter |
| Negative provision inventory | 56 | 57, README, Front Matter |
| Final claim boundary | 57 | release and orientation artifacts |
| Development motivation | FM-PREFACE | nowhere as theory |
| Entry status and scope | FM-STATUS-SCOPE | release metadata |
| Notation orientation | FM-TERMINOLOGY-NOTATION | reference layer |
| Reading pathways | FM-HOW-TO-READ | Reader and reference layer |

## 73. Round 4 Critical Redundancy Guards

```text
0 / 57      → initial versus final claim boundary; semantic alignment required
5 / 47      → continuity definitions versus integrated continuity audit
6 / 44–45   → compact Admissibility Band versus expanded lower/upper boundary tests
7 / 48      → shared record versus loss and selection semantics
16,27,39 / 51 → local Stop conditions versus system-wide Stop
17,28,40 / 53 → local audits versus integrated audit
38 / 50     → RETYPE-specific projection rescue versus system-wide anti-immunization
41 / 42–53  → LIMITS rationale versus individual boundary mechanisms
44 / 49     → absent PraxisPurchase versus insufficient source support
45 / 48     → lost traceability versus disclosed admissible loss
51 / 52     → Stop versus Non-Capture
54 / 55–57  → synthesis versus positive, negative, and final claim inventories
0,56 / FM-STATUS-SCOPE → canonical boundaries versus orientation summary
1–8 / FM-TERMINOLOGY-NOTATION → definitions versus notation guidance
README / FM-HOW-TO-READ → repository authority map versus reading navigation
```

## 74. Gate 2 Final Completion Gate

Gate 2 is complete only when:

- exactly 58 numeric chapter contracts exist for Chapters 0–57 with no gaps or duplicates;
- exactly four nonnumeric Front Matter contracts exist: `FM-PREFACE`, `FM-STATUS-SCOPE`, `FM-TERMINOLOGY-NOTATION`, and `FM-HOW-TO-READ`;
- every contract contains all prescribed fields and a syntactically valid YAML object;
- every concept has one primary definition site and explicit later reference-only sites;
- COMPOSE, DECOMPOSE, and PROJECT_AS remain the only core operations;
- frame, granularity, relative level, and transformation context remain distinct;
- origin type and target function remain distinct;
- Operator Type is never decomposed;
- Relevance Floor and Traceability Ceiling remain non-compensatory and non-numeric;
- local and integrated audits remain distinct;
- Claim Reduction, Analogy-Only, Partial Admissibility, Stop, Failure, and Non-Capture remain reachable;
- no operation, audit, model, conclusion, or orientation artifact creates ontology, person typing, normative authority, application authority, or immunity from failure;
- Conclusion introduces no new theory;
- Front Matter is removable without changing the canonical theory;
- all model relations remain operationalizations rather than sources of substantive truth;
- the repository copy and delivered artifact are byte-identical.

**Gate 2 status after generation:** `complete`  
**Next phase:** Phase 3 — Reference Kernel, followed by Formal Model v0.

---

## 75. Current Downstream Status Note

The historical Gate 2 handoff to the Reference Kernel and Formal Model v0 has been completed. The canonical chapter corpus, final bounded RETYPE/LIMITS/Conclusion locks, corpus-wide integration, substantive Front Matter, repository hygiene, and 59/59 case Record pairing now exist.

```text
current controlled phase:
Appendices A–N

next appendix:
Appendix A — Core Definitions
```

The 62 contract objects and their `appendix_migration` fields remain unchanged in meaning. This note updates production status only and creates no new contract burden.

