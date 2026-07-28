# Appendix N — Integrated STRATA Audit Template

**Status:** substantive bounded provisional completion  
**Authority:** reusable audit and chain-record supplement only; no independent theory, truth, or application authority  
**Primary owners:** Chapter 53, `04_reference/Audit_Checklist.md`, `07_model/Admissibility_Rules.yaml`, `07_model/Boundary_Decision_Tree.yaml`, and `07_model/Transformation_Record.schema.json`  
**Template output:** `03_cases/templates/integrated_audit_case_template.yaml`

## N.1 Purpose

Appendix N provides the complete reusable audit route for one routed operation occurrence or one declared integrated chain. It joins the existing Shared Transformation Record, the twelve audit stages, the sixteen Rule assessments, candidate generation, claim segmentation, Same-Claim collision adjudication, unique Output-Class selection, five-part Loss, Stop, Failure, Non-Capture, re-entry, and authority limits in one navigable workflow.

It does not create a thirteenth audit stage. Candidate generation and Output mapping occur **after** the twelve-stage audit and remain a separate routing phase.

```text
audit completion ≠ substantive passage
candidate generation ≠ final selection
integrated chain ≠ fourth operation
schema validity ≠ truth proof
more structure ≠ more authority
```

## N.2 Audit artifact boundary

The integrated audit uses three distinct artifact levels:

| Level | Unit | Function | Prohibited collapse |
|---|---|---|---|
| Occurrence Record | one `COMPOSE`, `DECOMPOSE`, or `PROJECT_AS` occurrence | stores local source, claim, target, audit, Loss, alternatives, and route | several operations in one Record |
| Chain Record | ordered references to several occurrence Records | tests handoffs and a separately delimited chain claim | merged local results or a fourth operation |
| Package narrative | human-readable shared context | explains source relations, sequence, contrast, and preservation | replacement of occurrence or chain Records |

Every operation occurrence remains independently adjudicated. A chain Record may preserve and compare those local results, but it may not rewrite them.

## N.3 Entry contract

Before Stage 1 begins, prepare a complete semantic packet. This preparation is not an audit stage.

### Required identity declarations

- one `record_id` and `record_scope`;
- `routing_state: routed` or a noncanonical `formal_diagnostic` state;
- one delimited tested claim;
- one registered operation for an occurrence Record, or one ordered sequence of registered occurrence Records for a chain;
- source object, origin typing, frame, granularity, relative level, temporal scope, and source scope;
- target object and, for `PROJECT_AS`, a bounded contextual function;
- claim ceiling, source ceiling, validity scope, excluded reach, and authority boundary.

### Required audit carriers

- all twelve stage objects;
- all sixteen Rule assessments;
- all five Loss fields;
- alternatives and rivals;
- Stop and Non-Capture assessments;
- candidate assessments for all ten Output Classes;
- final class selection or an explicit formal routing diagnostic.

If required material is missing, do not route the absence to `failed_transformation`, `mandatory_stop`, or `non_capture`.

```text
incomplete packet
→ formal diagnostic
→ preserve available material
→ no canonical Output Class
```

## N.4 Twelve-stage integrated audit

The order is fixed. A stage may refer back to earlier declarations, but it must not be silently skipped or replaced by a later routing decision.

### Stage 1 — `source_and_claim_entry`

**Purpose:** delimit the tested claim and its source basis before evaluating it.

Record:

- claim statement and claim role;
- reference-object boundary;
- operation-occurrence or chain boundary;
- frame, granularity, relative level, temporal scope, source scope, and context scope;
- claim ceiling and excluded reach;
- Source Basis and Constitutive Source Trace;
- known gaps and Source Ceiling;
- authority boundary.

**Failure guard:** a broad narrative, topic, or label is not a delimited transformation claim.

### Stage 2 — `operation_classification`

**Purpose:** establish whether the packet is one `COMPOSE`, `DECOMPOSE`, `PROJECT_AS`, or an `integrated_chain` Record referring to several already separate occurrences.

Questions:

- Is the source a valid source type for the proposed operation?
- Does the target correspond to the registered signature?
- Is a supposed chain merely a merged operation?
- Has a fourth operation name been introduced?

```text
operation type ≠ operation occurrence ≠ chain
```

### Stage 3 — `relevance_floor`

**Purpose:** test `PraxisPurchase`.

Ask:

> Which warranted reconstruction changes because of this transformation or additional distinction?

Local findings may include `gain`, `neutral`, `below_floor`, or `underdetermined`. Detail quantity is never a substitute for praxeological purchase.

### Stage 4 — `traceability_ceiling`

**Purpose:** test whether the result still carries reconstructible load from the declared sources.

Require:

- source identification;
- structural mapping;
- result dependence;
- expected effect of source variation;
- temporal or relational dependence;
- explicit claim limitation.

A citation list alone is not a Constitutive Source Trace.

### Stage 5 — `continuity_and_type_integrity`

**Purpose:** test the full continuity matrix without converting continuity into identity.

Assess separately:

- Type Integrity;
- Reference Continuity;
- Functional Continuity;
- Temporal Continuity;
- Loss Continuity;
- Authority Continuity.

For chains, perform the same checks at each handoff. A valid target of `T_i` is not automatically a valid source of `T_i+1`.

### Stage 6 — `counterfactual_sensitivity`

**Purpose:** test whether changing a load-bearing source relation changes the result in the expected direction.

Use source-supported variation only. Record one of the controlled local findings:

```text
strongly_sensitive
partially_sensitive
weakly_sensitive
insensitive
underdetermined
untestable
```

Counterfactual sensitivity is not causal proof.

### Stage 7 — `loss_and_selection`

**Purpose:** expose what the transformation retains and changes.

Every occurrence must declare:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

For `COMPOSE`, also test source selection, ordering, formation, and constitutive relations. For `DECOMPOSE`, test component selection, residual binding, unresolved structure, and source-function return. For `PROJECT_AS`, test what is retained from the origin object and what is excluded from the target function.

For chains, preserve the ordered sequence `⟨L_1, L_2, …, L_n⟩`. Do not sum or average Loss.

### Stage 8 — `alternatives`

**Purpose:** prevent one transformation route from becoming self-confirming.

Consider where applicable:

- rival compositions;
- rival decompositions;
- rival projections;
- no transformation;
- non-translation or an external method;
- unresolved alternatives.

A rival must be described strongly enough to pressure the preferred claim. Listing a caricature is not an alternative test.

### Stage 9 — `source_and_calibration_limits`

**Purpose:** test Source Ceiling and Calibration independently.

A source may support the existence of a structure while leaving its threshold, strength, temporal range, or contextual generality provisional. Calibration uncertainty does not mechanically imply Non-Capture.

### Stage 10 — `anti_immunization`

**Purpose:** prevent route switching from rescuing a failed claim.

Ask:

- Has a failed claim been moved to another frame, granularity, level, composite, or target function without becoming a new claim?
- Are counterexamples answered, or merely displaced?
- Are earlier Failure, Stop, Claim Reduction, or Non-Capture results still preserved?

```text
new transformation = new testable claim
later success ≠ repair of earlier failure
```

### Stage 11 — `stop_and_non_capture`

**Purpose:** decide whether continuation is required, optional, prohibited, or unable to retain an adequate capture claim.

Distinguish:

- Mandatory Stop;
- Optional Stop;
- failed transformation;
- genuine Non-Capture;
- missing information;
- a still-usable provisional claim.

Genuine Non-Capture requires adequate bounded attempts, preserved partial capture, a persistent material remainder, no adequate retained whole-claim form, distortion if forced, rivals or external methods, and an explicit re-entry condition.

### Stage 12 — `claim_and_authority_ceiling`

**Purpose:** state exactly what may and may not be claimed after the audit.

Confirm:

- retained claim and validity scope;
- excluded reach;
- current claim disposition;
- required external warrant;
- prohibited inferences;
- `authority_inheritance: prohibited`;
- no person typing, diagnosis, legitimacy judgment, sanction, or automatic recommendation.

Stage 12 closes the audit. Output mapping follows; it is not Stage 13.

## N.5 Sixteen Rule assessments

The twelve stages coordinate exactly sixteen canonical Rule carriers. `anti_immunization` is a governing Stage-10 contract that evaluates patterns across several Rule findings; it is not a seventeenth Rule.

| Rule | Main question | Typical decisive stage |
|---|---|---|
| `praxis_purchase` | does the distinction change a warranted reconstruction? | 3 |
| `traceable_load` | does the result depend on reconstructible source structure? | 4 |
| `type_integrity` | are source type, occurrence, composite, and target function kept distinct? | 5 |
| `reference_continuity` | is the same declared reference preserved where required? | 5 |
| `functional_continuity` | is the relevant function retained, revised, or rejected with warrant? | 5 |
| `temporal_continuity` | is load-bearing temporal structure preserved? | 5 |
| `contextual_boundedness` | is the target context and validity scope explicit? | 5 / 12 |
| `counterfactual_sensitivity` | does source variation pressure the result? | 6 |
| `selection_and_loss` | are selection and all five Loss fields explicit? | 7 |
| `alternatives` | were credible rivals and no-transformation routes considered? | 8 |
| `source_ceiling` | does the claim exceed available source support? | 9 |
| `calibration` | are unresolved thresholds or magnitudes exposed? | 9 |
| `stop` | has a mandatory or optional stop condition been reached? | 11 |
| `non_capture` | is there a genuine claim-relative capture limit? | 11 |
| `claim_ceiling` | is the retained claim bounded to supported reach? | 12 |
| `authority_ceiling` | are unsupported authority transfers and application inferences prohibited? | 12 |

Stage 10 uses the `anti_immunization_contract` to compare present and prior claims, frames, granularities, levels, composites, functions, failures, and stop conditions. It therefore remains mandatory without altering the exact sixteen-Rule inventory.

## N.6 Post-audit routing phase

### N.6.1 Candidate generation

After all applicable stages and Rules are complete, assess every canonical class candidate:

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

Candidate generation may return several plausible candidates. This does not create a class stack.

### N.6.2 Claim segmentation

Before resolving a collision, ask whether the candidates answer the same delimited claim.

If the apparent collision reflects different claims, split them into separate claims and, where operations differ, separate Records. Do not force one class to govern heterogeneous claims.

### N.6.3 Same-Claim collision adjudication

For a real Same-Claim collision:

1. identify the load-bearing boundary family;
2. compare the constitutive conditions of the candidate classes;
3. preserve non-selected findings;
4. state why one governance question is primary;
5. select exactly one class for the delimited tested claim.

No default precedence, score, weighted sum, majority vote, or first-match rule is permitted.

### N.6.4 Output mapping

The selected route must include:

- selected class;
- route ID;
- matched constitutive-condition pointers;
- collision state;
- preserved non-selected findings;
- split decision;
- class-selection rationale;
- current claim disposition;
- class-specific payload.

```text
Output Class ≠ Claim Disposition
```

A class may constrain continuation while the claim disposition states retained, revised, withdrawn, superseded, or another controlled state with its own rationale.

## N.7 Integrated-chain audit

A chain Record contains no `operation` object. It references the local occurrence Records in order.

Required chain fields:

```yaml
chain:
  chain_id:
  ordered_occurrence_record_ids:
  declared_operation_sequence:
  chain_claim_id:
  continuity_handoffs:
  preserved_occurrence_results:
  preserved_occurrence_losses:
  preserved_stops_and_non_capture:
  sequence_alignment_rationale:
```

### Handoff audit

For each `H_i,i+1`, verify:

- the target reference of `T_i` matches the declared source reference of `T_i+1`;
- origin type and contextual function are not collapsed;
- frame, granularity, relative level, and temporal scope changes are declared;
- prior Loss travels forward as a burden rather than disappearing;
- prior Failure, Stop, Claim Reduction, or Non-Capture remains preserved;
- the successor claim is independently delimited and tested.

### Chain result

The chain claim may receive its own routed class, but local occurrence classes remain unchanged.

```text
class(chain claim)
≠ average(class(T_1), …, class(T_n))
```

The chain Record may conclude that the handoff is admissible, bounded, partial, stopped, failed, or uncaptured only after testing a separately stated chain-level claim.

## N.8 Worked YAML fixture

`03_cases/templates/integrated_audit_case_template.yaml` is a schema-valid worked `integrated_chain` fixture. It uses the existing synthetic COMPOSE and PROJECT_AS smoke Records and deliberately retains a `non_capture` chain result because that route exercises the most demanding preservation duties:

- locally admissible component results remain unchanged;
- the handoff is preserved;
- component Loss remains separate;
- a global whole claim is not retained;
- bounded alternatives and re-entry stay open;
- no fourth operation or authority transfer is introduced.

The fixture is not a default Non-Capture template and not a substantive finding about any real authorization system. Reuse requires replacing or revalidating every claim, source, trace, chain member, handoff, target, audit finding, Loss item, alternative, route, and authority statement.

## N.9 Reuse procedure

1. Copy the YAML fixture and assign new Record, Claim, and Chain IDs.
2. Replace all synthetic source pointers and provenance notes.
3. Link only existing, independently valid occurrence Records.
4. Declare a new chain-level claim rather than inheriting local claims.
5. Re-run all twelve stages and all sixteen Rules.
6. Reconstruct the ordered Loss sequence.
7. Test alternatives, Stop, Failure preservation, and Non-Capture independently.
8. Generate all ten class candidates.
9. Segment claims and adjudicate any Same-Claim collision.
10. Select exactly one class or emit a formal diagnostic.
11. Validate against `Transformation_Record.schema.json`.
12. Report schema validity separately from substantive judgment.

## N.10 Compact human audit worksheet

```text
IDENTITY
[ ] one Record scope
[ ] one occurrence or one declared chain
[ ] one delimited tested claim

ENTRY
[ ] source and claim complete
[ ] source and claim ceilings explicit
[ ] authority boundary explicit

STAGES 1–12
[ ] source_and_claim_entry
[ ] operation_classification
[ ] relevance_floor
[ ] traceability_ceiling
[ ] continuity_and_type_integrity
[ ] counterfactual_sensitivity
[ ] loss_and_selection
[ ] alternatives
[ ] source_and_calibration_limits
[ ] anti_immunization
[ ] stop_and_non_capture
[ ] claim_and_authority_ceiling

ROUTING
[ ] ten candidates assessed
[ ] claims segmented
[ ] Same-Claim collision assessed
[ ] one class selected or formal diagnostic emitted
[ ] current claim disposition separately stated

CHAIN
[ ] each occurrence remains a separate Record
[ ] every handoff tested
[ ] local results preserved
[ ] local Loss preserved
[ ] prior Stop / Failure / Non-Capture preserved

GOVERNANCE
[ ] no scoring or compensation
[ ] no fourth operation
[ ] no eleventh class
[ ] no authority inheritance
[ ] formal validity not reported as truth
```

## N.11 Completion boundary

Appendix N completes the Appendix A–N operational set and provides the integrated audit template. It does not finalize the Reference Kernel, perform the Integrated Corpus Audit, finalize the Formal Model, or authorize release.

```text
Appendix set status: complete at a bounded provisional level
Reference Kernel status: subject to Reference Freeze
Canonical corpus status: subject to the Integrated Corpus Audit
Formal Model status: subject to Model Finalization
```

The Appendix-set lock remains bounded provisional until Reference Freeze and the Integrated Corpus Audit confirm cross-artifact alignment with canonical `01_blocks/*`.
