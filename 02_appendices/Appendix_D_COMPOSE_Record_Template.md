# Appendix D — COMPOSE Record Template

**Status:** substantive bounded provisional completion  
**Primary prose owners:** Chapters 9, 10, 14, and 15  
**Shared record owner:** Chapter 7 and `07_model/Transformation_Record.schema.json`  
**Operation registry owner:** `07_model/Operation_Registry.yaml#/operation_types/COMPOSE`  
**Reusable YAML fixture:** `03_cases/templates/compose_case_template.yaml`

---

## D.1 Purpose and Boundary

Appendix D provides the operation-specific completion guide for one `COMPOSE` occurrence. It does not define a second record grammar. The Shared Transformation Record described in Appendix C remains the common envelope; this Appendix specifies how that envelope is populated when the declared operation is exactly:

```text
COMPOSE
```

The canonical movement is:

```text
many or sequential source structures
→
new composite analytical object
```

A valid record must make source selection, ordering, formation, constitutive relations, compression, exclusion, uncertainty, and irrecoverable loss inspectable. It must also keep the new composite distinct from every source object and from any later contextual function.

```text
COMPOSE
≠ aggregation
≠ chronology
≠ automatic Path
≠ automatic Trajectory
≠ PROJECT_AS
≠ new PMS primitive
```

The YAML fixture is intentionally schema-valid as written. Its retained synthetic content is a worked structural example, not a pre-authorized result. Every source, claim, finding, Loss entry, alternative, route, and pointer must be replaced or affirmatively retained for the new occurrence and then re-audited.

---

## D.2 Entry Test: Is COMPOSE the Correct Operation?

Use `COMPOSE` only when the tested claim is that several source structures form one new analytical object through declared relations. The entry question is not whether several things can be listed together. It is:

> Which source structures, under which selection, order, and formation rule, constitute one bounded composite object whose identity depends on those relations?

A `COMPOSE` record is appropriate where the proposed target is, for example:

- a Sequence;
- a Path;
- a Trajectory;
- a branch structure;
- an event cluster;
- a phase;
- a bounded relational composite;
- another explicitly typed composite object.

Do not use `COMPOSE` where the actual claim is:

- that one compressed object should be opened under finer granularity — use `DECOMPOSE`;
- that an origin-typed object performs a contextual function — use `PROJECT_AS`;
- that several items are merely associated, co-present, or rhetorically grouped;
- that a composite has greater truth or authority because it is larger or more structured.

If operation identity remains unresolved, preserve the packet as `formal_diagnostic` rather than forcing a routed COMPOSE occurrence.

---

## D.3 Minimum Source Packet

A COMPOSE occurrence requires at least two identifiable source objects or source-bearing structures. Each must be separately referable even where they share a source file or temporal episode.

The record must declare:

```yaml
source:
  reference_object:
  object_typing:
  frame:
  granularity:
  relative_level:
  temporal_scope:
  source_scope:
  source_basis:
  constitutive_source_trace:
  known_gaps:
  source_ceiling:
```

### D.3.1 Source multiplicity

The source declaration must not hide multiplicity inside one undifferentiated label. The operation-specific payload therefore includes:

```yaml
operation:
  details:
    source_objects:
    source_typings:
```

Each source object should have:

- a stable local identifier;
- a description that distinguishes it from the other source objects;
- an origin-side typing;
- a source pointer or provenance route where available.

A source set may be represented by one top-level `source.reference_object`, but the operation payload must still expose the members that carry the composition claim.

### D.3.2 Source Basis versus Constitutive Source Trace

`source_basis` records what material is available. `constitutive_source_trace` records which source features actually carry the result.

```text
source available
≠ source constitutive
```

For every load-bearing trace, state:

- the relevant source feature;
- the affected claim component;
- why the result depends on that feature;
- what would change if it were removed or materially altered;
- its temporal or relational dependency;
- the limitation imposed on the claim.

---

## D.4 Claim Declaration

The claim statement should name the composite, the selected source set, and the relation through which the result becomes more than a list.

A useful pattern is:

```text
The declared source structures S,
under ordering rule R_o and formation rule R_f,
form bounded composite X_c of type K_c
within validity scope V.
```

The claim scope must bound:

- the reference object boundary;
- this occurrence only;
- source and target frame;
- source and target granularity;
- relative-level relation;
- temporal scope;
- source scope;
- context scope;
- generalization boundary;
- excluded reach.

The Claim Ceiling should say explicitly what the composition does **not** establish. Typical exclusions include:

```text
composite formation
≠ causal explanation
≠ strong Path Dependence
≠ contextual target function
≠ person or institution evaluation
≠ application authority
```

---

## D.5 Selection Rule

Selection is constitutive, not clerical. The record must state why each included structure belongs to the composite and why omitted structures do not.

The template field is:

```yaml
operation:
  selection_rule:
```

The rule should identify:

1. included source objects;
2. excluded source objects;
3. load-bearing versus illustrative elements;
4. disputed or uncertain inclusions;
5. the relation between selection and the target claim;
6. what information becomes unavailable because of selection.

A selection rule fails where it is circular:

```text
included because part of the Path
and
Path exists because included
```

A valid rule is source- and claim-relative. It permits a counterfactual question: would removing this element change the composite identity or only make the narrative less complete?

---

## D.6 Ordering Rule

`COMPOSE` may preserve linear order, partial order, overlap, parallelism, branch structure, uncertain order, or retrospective periodization. The record must not silently convert one form into another.

```yaml
operation:
  details:
    ordering_rule:
```

Permitted declarations include:

```text
X1 before X2 before X3
X1 and X2 both precede X3, while their mutual order is unresolved
X1 overlaps X2
branch B1 and branch B2 remain parallel until transition T3
periodization is retrospective and bounded to claim Q
```

The ordering rule must preserve uncertainty where the source does not warrant total order.

```text
partial order
≠ incomplete total order waiting to be guessed
```

For non-temporal composites, state the structural relation that replaces temporal sequence.

---

## D.7 Formation Rule

The formation rule explains why the selected and ordered sources become the declared composite.

```yaml
operation:
  details:
    formation_rule:
```

The rule must identify the relation that distinguishes:

```text
list → Sequence
chronology → Path
a Path → Trajectory
co-presence → relational composite
```

Examples of formation conditions include:

- continuation sensitivity;
- transition dependence;
- retained asymmetry;
- repeated reinforcement;
- branch closure;
- binding relation;
- sedimented cost or expectation;
- constitutive cross-component dependency.

The formation rule must be independently criticizable. A target label is not a formation rule.

```text
“these events form a Trajectory”
≠ explanation of trajectory formation
```

---

## D.8 Constitutive Relations

The operation payload requires explicit relations:

```yaml
operation:
  details:
    constitutive_relations:
      - relation_id:
        relation_type:
        from_object_id:
        to_object_id:
        description:
        constitutive: true
```

A relation may be temporal, structural, dependency-bearing, or another controlled local relation. It must not be invented merely to satisfy the schema.

For each relation, test:

- whether both endpoints are declared source objects;
- whether the relation is source-supported;
- whether it is constitutive or illustrative;
- whether removing it defeats, narrows, or leaves the composite unchanged;
- whether its direction is warranted;
- whether the relation remains bounded to the stated frame and temporal scope.

A mere adjacency relation normally cannot support a stronger dependency claim without additional evidence.

---

## D.9 Target Composite Declaration

The target is a new analytical object. It must receive its own reference and typing:

```yaml
target:
  reference_object:
  object_typing:
  contextual_function: null
  frame:
  granularity:
  relative_level:
  temporal_scope:
  validity_scope:
  contextual_function_origin_occurrence_ref: null
```

For COMPOSE, `contextual_function` must remain `null`. A function claim requires a separate `PROJECT_AS` occurrence.

The target declaration should make visible:

- the composite identifier;
- its object class;
- its difference from the source set;
- the coordinate change, if any;
- the validity scope;
- the non-primitive boundary.

```text
new composite object
≠ replacement of source objects
≠ automatic higher-level authority
```

---

## D.10 Preservation Duties

Assess preservation where constitutive to the claim. Typical COMPOSE preservation duties include:

- source reference and provenance;
- relevant order and transition structure;
- central events and non-events;
- branch points and blocked alternatives;
- asymmetry and binding structures;
- internal heterogeneity needed by the composite claim;
- distinction between source object types and target composite type;
- prior failures, Stops, or Non-Capture findings inherited through a chain.

Preservation does not require total reproduction. It requires reconstructible dependence.

---

## D.11 Loss Record

Populate all five categories:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

Typical COMPOSE Loss:

- local detail compressed into phase or composite identity;
- minor parallel branches excluded;
- exact micro-order left uncertain;
- separability of local costs reduced;
- omitted alternatives irrecoverable from the target alone.

Do not use a scalar score, and do not allow an aesthetically coherent composite to hide source loss.

```text
formal elegance
≠ compensation for missing traceable load
```

---

## D.12 Admissibility and Counterfactual Tests

The shared twelve-stage audit remains mandatory. COMPOSE-specific emphasis falls on:

- Praxis Purchase: does the composite change a warranted reconstruction rather than merely summarize?
- Traceable Load: can each load-bearing relation be traced to source material?
- Type Integrity: is the target a composite rather than a disguised function or primitive?
- Reference Continuity: are source identities retained?
- Temporal Continuity: is order preserved without false totalization?
- Counterfactual Sensitivity: would removing or changing a load-bearing source or relation alter the result?
- Selection and Loss: are inclusion, exclusion, and compression explicit?
- Alternatives: were rival compositions and no transformation assessed?
- Source and Claim Ceilings: does the record avoid trajectory, dependence, causal, or function overreach?

The central counterfactual form is:

```text
remove or alter source element X_i
or relation R_j
→ does composite identity or claim materially change?
```

If only the story becomes shorter while the target object remains unchanged, the element may be illustrative rather than constitutive.

---

## D.13 Alternatives

At minimum consider:

```yaml
alternatives:
  rival_compositions:
  rival_decompositions:
  rival_projections:
  no_transformation:
  non_translation:
  unresolved:
  no_additional_alternatives_asserted:
```

COMPOSE-relevant alternatives include:

- different selection boundaries;
- rival ordering or periodization;
- a smaller or larger composite;
- retention as chronology or list;
- direct use of source objects without composition;
- later projection of an already warranted composite rather than hidden function assignment now.

Alternative assessment is not a requirement to manufacture arbitrary rivals. It is a requirement to make plausible source-supported competitors visible.

---

## D.14 Stop, Failure, Claim Reduction, and Non-Capture

Possible COMPOSE routes include all ten canonical Output Classes. Frequent boundaries are:

- `claim_reduction_required` where a smaller composite is supported but the broader Path or Trajectory claim is not;
- `mandatory_stop` where continuation would require unsupported order, relation, or source closure;
- `failed_transformation` where the target remains a list, chronology, label, or disguised function;
- `non_capture` only after adequate bounded composition attempts cannot retain the capture object without distortion.

```text
missing relation evidence
≠ automatically non_capture
```

Stop conditions should preserve any bounded result already warranted. A later recomposition is a new occurrence and does not erase an earlier failure.

---

## D.15 Output Routing

The template contains a schema-valid worked route. It must never be copied as an adjudication shortcut.

For a new record:

1. complete all twelve audit stages;
2. complete all sixteen Rule assessments;
3. generate all ten class candidates;
4. assess same-claim collision;
5. split claims where required;
6. select exactly one class for the tested claim;
7. populate only the matching class payload;
8. preserve non-selected findings;
9. keep local operation result separate from selected class.

```text
template default route
≠ result of the new case
```

---

## D.16 Chain Participation

A COMPOSE occurrence may precede or follow another occurrence, but it remains one record:

```text
COMPOSE → PROJECT_AS
COMPOSE → DECOMPOSE
DECOMPOSE → COMPOSE
```

The next record must declare the handoff explicitly. It may not inherit authority or treat the target composite as lossless.

```text
DECOMPOSE(COMPOSE(X)) ≠ X
```

A reverse movement is a new claim with a new Loss profile.

---

## D.17 Worked-Fixture Use Protocol

To use `compose_case_template.yaml`:

1. copy the file to `03_cases/yaml/<case-id>.yaml`;
2. replace record, claim, source, occurrence, and object identifiers;
3. replace every retained synthetic source and relation;
4. update metadata and artifact pointers;
5. declare at least two source objects;
6. rewrite selection, ordering, and formation rules;
7. rebuild Constitutive Source Trace;
8. declare target composite identity and keep `contextual_function: null`;
9. repopulate all five Loss fields;
10. rerun alternatives, Stop, Non-Capture, and all class candidates;
11. select and justify the actual route;
12. create the same-basename Markdown companion;
13. add the record to the Case Index only after structural and substantive review.

Do not retain a synthetic value merely because it is schema-valid.

---

## D.18 Completion Checklist

A COMPOSE record is ready for routing only where:

- exactly one COMPOSE occurrence is declared;
- at least two source objects are separately identifiable;
- source Basis and Constitutive Source Trace are populated;
- selection, ordering, and formation rules are explicit;
- constitutive relations are declared and source-supported;
- the target is a new bounded composite object;
- no automatic target function is assigned;
- preservation and all five Loss categories are assessed;
- rival compositions and no transformation are considered;
- the twelve-stage audit and sixteen Rules are complete;
- Stop and Non-Capture are assessed without conflation;
- exactly one Output Class is selected after collision assessment;
- no new PMS primitive or authority relation is introduced.

The bounded Appendix-D result is:

```text
admissible_with_bounded_claim
```

This result applies to the template architecture, not to any record produced from it.

---

## D.19 Handoff

Appendix D hands forward to:

```text
Appendix G
→ detailed Admissibility Band tests

Appendix H
→ valid and invalid transformation patterns

Appendix J
→ weighting and trajectory stress tests

Appendix M
→ case and countercase indexing

Appendix N
→ integrated audit and chain handoff
```
