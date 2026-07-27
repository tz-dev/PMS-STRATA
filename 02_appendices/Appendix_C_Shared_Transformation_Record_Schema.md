# Appendix C — Shared Transformation Record Schema

## C.0 Status, Authority, and Use

This Appendix expands the Shared Transformation Record defined in Chapter 7 into a human-readable schema guide. It explains the purpose, requiredness, conditional structure, field semantics, and cross-field invariants of the current machine-readable record carrier:

```text
07_model/Transformation_Record.schema.json
```

The governing order remains:

```text
Chapter 7 canonical record contract
→ Appendix C explanatory schema guide
→ Transformation_Record.schema.json structural validator
→ operation-specific templates in Appendices D–F
→ integrated audit template in Appendix N
```

Appendix C does not replace Chapter 7 and does not become the owner of operation semantics, Admissibility Rules, Output Classes, or substantive judgment. The JSON Schema remains the owner of concrete syntax and structural requiredness. Chapter 7 remains the owner of why the Shared Transformation Record exists and what epistemic duties its field families carry.

```text
record structure
≠ transformation

schema-valid record
≠ admissible transformation

field presence
≠ adequate source support

machine-readable consistency
≠ truth, causality, semantic validity,
  normative validity, diagnosis, legitimacy,
  application authority, or complete capture
```

The current formal artifact is JSON Schema Draft 2020-12 with:

```text
schema id:
https://pms-strata.local/schema/Transformation_Record.schema.json

root component version:
0.1.3

instance field schema_version:
0.1.2
```

The distinction between artifact version and instance `schema_version` is deliberate. The root component version tracks the current schema artifact as a repository component. The instance field is the record-declared syntax contract currently required by the schema. Neither number is a measure of theoretical rank or claim authority.

The Appendix status is:

```text
substantive bounded provisional completion
```

Its final lock remains dependent on the completion of Appendices D–N, Reference Freeze, the Integrated Corpus Audit, and Model Finalization.

---

## C.1 What the Shared Record Represents

A Shared Transformation Record represents one of two record scopes:

```text
operation_occurrence
integrated_chain
```

and one of two routing states:

```text
routed
formal_diagnostic
```

These are independent axes.

### C.1.1 Operation-occurrence record

An `operation_occurrence` record declares one and only one occurrence of:

```text
COMPOSE
DECOMPOSE
PROJECT_AS
```

It must not merge several operations into one compound kind. A sequence such as:

```text
COMPOSE → PROJECT_AS → DECOMPOSE
```

requires three occurrence records. A separate chain record may then declare their order and handoffs.

### C.1.2 Integrated-chain record

An `integrated_chain` record does not itself perform an operation. It declares:

- the ordered occurrence-record identifiers;
- the declared operation sequence;
- the chain claim;
- continuity handoffs;
- preserved local results;
- preserved local Loss profiles;
- preserved Stops and Non-Capture findings;
- the rationale for sequence alignment.

```text
chain declaration
≠ fourth operation
≠ merged operation occurrence
≠ averaged local result
```

### C.1.3 Routed record

A `routed` record contains a delimited claim that has passed through the complete audit and routing process. It must contain the full substantive carrier required by the schema, including Claim, Source, Target, Admissibility, Loss, Alternatives, Governance, Result, and Relations. An occurrence record additionally requires `operation`; a chain record requires `chain`.

A routed record selects exactly one canonical Output Class for the current delimited claim.

### C.1.4 Formal diagnostic

A `formal_diagnostic` record preserves a packet that cannot yet be routed because a prerequisite remains unresolved, such as:

- incomplete packet;
- unresolved claim segmentation;
- no supported candidate;
- unresolved collision;
- unresolved selection.

It does not receive a canonical Output Class. Its `result` may contain non-routing status material, but `/result/routing` and `/result/class_payload` are prohibited.

```text
formal diagnostic
≠ failed_transformation
≠ mandatory_stop
≠ non_capture
```

A formal diagnostic identifies a process-state limitation before a substantive route has been completed. The three canonical outputs above are substantive results for delimited claims.

---

## C.2 The Common Semantic Envelope and the Serialization Companions

Chapter 7 defines the common semantic envelope:

```yaml
source:
operation:
target:
admissibility:
loss:
alternatives:
governance:
status_and_result:
```

The machine schema exposes this envelope through explicit top-level fields and adds serialization companions needed for identity, provenance, lineage, chain declaration, local extensions, and formal diagnostics.

### C.2.1 Top-level field inventory

| Top-level field | Structural role | Required for all records | Required for routed records | Prohibited or conditional |
|---|---|---:|---:|---|
| `schema_version` | declares the record syntax version | yes | yes | fixed to `0.1.2` |
| `record_id` | unique record identity | yes | yes | controlled identifier syntax |
| `record_scope` | occurrence or integrated chain | yes | yes | exactly one of two values |
| `routing_state` | routed or formal diagnostic | yes | yes | exactly one of two values |
| `record_metadata` | provenance and model-version declaration | yes | yes | may not confer authority |
| `claim` | current tested claim | no at base | yes | may be absent in a formal diagnostic |
| `source` | source object, basis, trace, gaps, ceiling | no at base | yes | routed records require non-empty basis and trace |
| `operation` | one occurrence declaration | conditional | occurrence only | prohibited in integrated-chain records |
| `chain` | integrated-chain declaration | conditional | chain only | prohibited in occurrence records |
| `target` | target object/function and coordinates | no at base | yes | operation-specific function constraints apply |
| `admissibility` | twelve-stage audit and sixteen Rule assessments | yes | yes | routed records require complete assessments |
| `loss` | five-field Loss declaration | no at base | yes | no sixth field and no scalar score |
| `alternatives` | rival and no-transformation routes | no at base | yes | must not be bypassed by an extension |
| `governance` | claim and authority limits | yes | yes | `authority_inheritance` fixed to prohibited |
| `result` | local result, status axes, route, class payload | yes | yes | formal diagnostics cannot contain route/class payload |
| `relations` | claim and record lineage | yes | yes | empty relation object is structurally permitted |
| `extensions` | bounded owner-controlled local views | optional | optional | cannot replace any required field |
| `formal_diagnostic` | unresolved formal-routing packet | conditional | no | required when `routing_state: formal_diagnostic` |

The schema uses `additionalProperties: false` at the root and throughout controlled structures. New top-level fields cannot be inserted informally. A genuinely necessary new field requires an explicit owner-level model revision rather than a local record workaround.

### C.2.2 Base requiredness versus routed requiredness

At the root, every record must contain:

```yaml
schema_version:
record_id:
record_scope:
routing_state:
record_metadata:
admissibility:
governance:
result:
relations:
```

A routed record additionally requires:

```yaml
claim:
source:
target:
loss:
alternatives:
```

and, depending on scope:

```yaml
operation:  # operation_occurrence
```

or:

```yaml
chain:      # integrated_chain
```

This two-level requiredness is not a permission to omit substantive fields from a routed record. It permits formal diagnostics to preserve incomplete or unresolved material without fabricating a complete transformation claim.

---

## C.3 Record Identity and Metadata

### C.3.1 `schema_version`

The current record instance value is fixed:

```yaml
schema_version: 0.1.2
```

A record with another value does not conform to the current schema. Conformance does not imply substantive passage.

### C.3.2 `record_id`

`record_id` identifies one record artifact. It is not automatically identical to:

- the claim identifier;
- the operation occurrence identifier;
- the source object identifier;
- the chain identifier;
- a case label;
- a filename.

The values may be coordinated for traceability, but their identities remain distinct.

### C.3.3 `record_metadata`

Required metadata fields are:

| Field | Purpose |
|---|---|
| `created_at` | creation timestamp |
| `updated_at` | last record update timestamp |
| `revision_id` | explicit record revision identity |
| `record_provenance` | non-empty provenance statements |
| `model_versions` | component-version declarations used for the record |
| `formal_validation_not_substantive_validation_acknowledged` | must be `true` |

Optional metadata fields include:

- `producer_id`;
- `repository_or_case_pointer`;
- `record_status_note`.

Metadata documents artifact history. It does not increase the transformation claim's evidence or authority.

```text
more provenance detail
≠ stronger substantive claim
```

---

## C.4 Claim Declaration

A routed record contains one current tested claim under `/claim`.

Required fields:

```yaml
claim:
  claim_id:
  statement:
  claim_type:
  claim_role:
  claim_scope:
  validity_scope:
  claim_ceiling:
  authority_boundary:
```

### C.4.1 Claim identity and statement

`claim_id` identifies the current tested proposition. `statement` states the proposition in bounded language. The claim statement must be specific enough to test and narrow enough to retain the declared Source Ceiling and Claim Ceiling.

### C.4.2 Controlled claim type and role

`claim_type` and `claim_role` use the open controlled-term structure:

```yaml
value:
control_source:
inventory_status:
extension_rationale:  # required only for extensions
```

An open controlled term permits locally necessary language while preserving its owner and inventory status. It does not allow a local term to become a new canonical class, operation, or primitive.

### C.4.3 Claim scope

`claim_scope` requires all of the following:

```yaml
reference_object_boundary:
operation_occurrence_boundary:
frame:
granularity:
relative_level:
temporal_scope:
source_scope:
context_scope:
generalization_boundary:
excluded_reach:
```

The scope fields prevent a valid local claim from silently acquiring wider temporal, contextual, level, functional, or generalization reach.

### C.4.4 Claim ceiling

`claim_ceiling` requires:

```yaml
asserted_relation:
reach:
precision:
generality:
functional_scope:
dependence_strength:
inferential_distance:
limiting_sources:
rationale:
```

The Claim Ceiling is not reducible to one scalar. A claim may be bounded in reach but excessive in precision, acceptable in functional scope but excessive in causal distance, or materially provisional because one limiting source remains unresolved.

### C.4.5 Authority boundary

`authority_boundary` states what the record does not authorize. It must remain compatible with Governance and may not be used to conceal an otherwise overreaching claim.

```text
stated authority boundary
≠ automatic compliance with authority boundary
```

---

## C.5 Source Declaration

The Source Declaration is the main carrier of traceability and Source Ceiling control.

Required fields:

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

### C.5.1 Reference object

`reference_object` contains:

```yaml
object_id:
description:
typing:         # optional local pointer/typing term
source_pointer: # optional
```

The reference object is the claim-relative object whose continuity or transformation is being tested. A matching label is not sufficient to establish identity.

### C.5.2 Object typing and analytical coordinates

`object_typing`, `frame`, `granularity`, and `relative_level` use controlled-term structures. `temporal_scope` and `source_scope` declare the bounded source reach.

```text
frame
≠ granularity
≠ relative level
≠ temporal scope
```

### C.5.3 Source basis

Each `source_basis` item must declare:

| Field | Duty |
|---|---|
| `source_item_id` | local item identity |
| `source_pointer` | address or bounded source reference |
| `provenance_description` | what the item is and where it comes from |
| `affected_claim_component` | which part of the claim it supports or limits |
| `support_mode` | direct, indirect, synthetic, comparative, or controlled local mode |
| `evidence_role` | controlled description of the item's role |
| `evidence_availability` | availability state |
| `temporal_scope` | time range supported by the item |
| `reference_scope` | object or relation range supported |
| `uncertainty_or_provenance_limit` | explicit limitation |
| `warrant_route` | how the item may enter the STRATA assessment |
| `external_warrant_pointer` | optional pointer where external warrant is relevant |

A routed record requires at least one source-basis item. Generic references such as “several documents” may be syntactically non-empty while remaining substantively insufficient.

### C.5.4 Constitutive Source Trace

Each `constitutive_source_trace` entry requires:

```yaml
trace_id:
source_feature:
affected_claim_component:
trace_role:
result_dependency:
expected_result_change:
temporal_or_relational_dependency:
claim_limitation:
source_pointer:  # optional
```

The Source Trace states why a source feature is load-bearing for the result. It must support counterfactual inspection: if the feature were removed or materially changed, what aspect of the result would weaken, disappear, or require reclassification?

```text
source list
≠ Constitutive Source Trace
```

A routed record requires at least one trace entry.

### C.5.5 Known gaps and Source Ceiling

`known_gaps` preserves unresolved source limits. `source_ceiling` uses the same nine-dimensional ceiling structure as the Claim Ceiling and states what the source basis can and cannot support.

Missing information must not be converted into an empty event, an exact relation, or a claim of Non-Capture without the required additional burden.

---

## C.6 Operation Declaration

An occurrence record uses:

```yaml
operation:
  occurrence_id:
  kind:
  justification:
  expected_praxeological_difference:
  selection_rule:
  transformation_context:
  details:
```

### C.6.1 Exactly one operation kind

`kind` is exactly one of:

```text
COMPOSE
DECOMPOSE
PROJECT_AS
```

The `details` payload is conditionally tied to that kind.

```text
kind: COMPOSE
→ composeDetails only

kind: DECOMPOSE
→ decomposeDetails only

kind: PROJECT_AS
→ projectAsDetails only
```

### C.6.2 Shared operation fields

- `justification` explains why this operation, rather than another or no transformation, is claimed.
- `expected_praxeological_difference` states the practical analytical purchase expected from the move.
- `selection_rule` declares inclusion, ordering, reconstruction, or function-selection criteria.
- `transformation_context` distinguishes the operation context from source and target frames.

These fields record reasons. They do not automatically establish warrant.

### C.6.3 COMPOSE details

The COMPOSE payload requires:

```yaml
source_objects:
source_typings:
ordering_rule:
formation_rule:
constitutive_relations:
source_trace:
selection_rule_pointer:
target_reference_object_pointer:
target_object_typing_pointer:
```

Appendix D will provide the usable occurrence template. Appendix C fixes only the shared schema relation.

### C.6.4 DECOMPOSE details

The DECOMPOSE payload requires:

```yaml
source_function:
decomposition_question:
insufficiency_of_current_compression:
components:
component_relations:
internal_temporality:
source_support:
source_reference_preserved:
prior_source_claim_id:
unresolved_structure:
counterfactual_component_test:
source_function_effect_pointer:
resolution_test_result_pointer:
source_reference_object_pointer:
origin_type_pointer:
target_granularity_pointer:
```

The pointers keep the operation-specific payload aligned with the authoritative result and source axes rather than duplicating them.

### C.6.5 PROJECT_AS details

The PROJECT_AS payload requires:

```yaml
target_context:
constitutive_source_trace:
source_reference_preserved:
origin_type_preserved:
target_function_bounded:
alternative_projection_or_no_projection:
target_contextual_function_pointer:
source_reference_object_pointer:
origin_type_pointer:
target_reference_object_pointer:
target_frame_pointer:
validity_scope_pointer:
```

Appendix F will provide the complete reusable template.

---

## C.7 Target Declaration

A routed record declares:

```yaml
target:
  reference_object:
  object_typing:
  contextual_function:
  frame:
  granularity:
  relative_level:
  temporal_scope:
  validity_scope:
  contextual_function_origin_occurrence_ref:
```

### C.7.1 Target object and target function

`reference_object` and `object_typing` identify the target-side analytical object state. `contextual_function` is operation-sensitive:

```text
PROJECT_AS
→ contextual_function must be a controlled term

COMPOSE or DECOMPOSE
→ contextual_function must be null
```

This prevents hidden RETYPE inside COMPOSE or DECOMPOSE.

For a PROJECT_AS occurrence, `contextual_function_origin_occurrence_ref` is null because the current operation is the origin of the function assignment. For a target that inherits a previously declared function in a later, different operation, the record must preserve the appropriate prior occurrence through relations rather than pretend the later operation created it.

### C.7.2 Target coordinates and validity scope

Target frame, granularity, relative level, temporal scope, and validity scope remain separate. A change in one coordinate does not imply a change in the others or increased authority.

---

## C.8 Admissibility Declaration

The Admissibility Declaration is the largest shared field family. It records the completed audit; it does not replace substantive reasoning.

A routed record requires:

```yaml
admissibility:
  audit_stages:
  rule_assessments:
  non_compensation_confirmation: true
  audit_to_routing_basis:
  anti_immunization_assessment:
  stop_assessment:
  non_capture_assessment:
```

### C.8.1 Twelve audit stages

All twelve stages must be present and complete for a routed record:

1. `source_and_claim_entry`
2. `operation_classification`
3. `relevance_floor`
4. `traceability_ceiling`
5. `continuity_and_type_integrity`
6. `counterfactual_sensitivity`
7. `loss_and_selection`
8. `alternatives`
9. `source_and_calibration_limits`
10. `anti_immunization`
11. `stop_and_non_capture`
12. `claim_and_authority_ceiling`

Each stage declares:

```yaml
stage_id:
assessment_mode:
completion_state:
summary_finding:
rationale:
rule_assessment_pointers:
evidence_or_artifact_pointers:
unresolved_items:
```

Repeated Rule identifiers across stages represent distinct assessment modes, not duplicate independent tests.

### C.8.2 Sixteen Rule assessments

Every routed record declares all sixteen Rule assessment carriers:

```text
praxis_purchase
traceable_load
type_integrity
reference_continuity
functional_continuity
temporal_continuity
contextual_boundedness
counterfactual_sensitivity
source_ceiling
calibration
selection_and_loss
alternatives
claim_ceiling
authority_ceiling
stop
non_capture
```

Operation-specific schema conditions determine which may be `not_applicable`. Applicability is not a method for avoiding a difficult finding. It must be justified against the operation contract.

Every assessment records at least:

- applicability;
- applicability rationale where needed;
- assessment state;
- control-source pointer;
- evidence or artifact pointers;
- reasoned finding;
- claim or artifact effect;
- required action;
- controlled local result.

Specialized Rule carriers add fields for relevance, traceability, counterfactual sensitivity, calibration, Stop, and Non-Capture.

### C.8.3 Non-compensation

A routed record must state:

```yaml
non_compensation_confirmation: true
```

No strong finding compensates for a failed load-bearing Rule. Formal detail, extensive sources, or elegant notation cannot compensate for absent PraxisPurchase, TraceableLoad, Type Integrity, or a breached ceiling.

### C.8.4 Stop assessment

`stop_assessment` requires:

```yaml
reached:
condition_assessed:
rationale:
reentry_contemplated:
```

If Stop is reached, the record must also declare:

```yaml
mode: mandatory | optional
stop_condition:
preserved_result:
reentry_conditions:
```

If re-entry is contemplated even without a current Stop, `reentry_conditions` are required.

```text
Stop reached
≠ prior result erased
```

### C.8.5 Non-Capture assessment

`non_capture_assessment` requires:

```yaml
adequate_capture_assessed:
material_capture_limit_asserted:
adequate_retained_claim_remains:
partial_capture_asserted:
non_capture_form_asserted:
rationale:
```

Where any capture limit is asserted, `capture_boundary` is required:

```yaml
captured_structure:
uncaptured_structure:
limiting_condition:
distortion_if_forced:
attempted_operations:
rivals_or_external_method:
reentry_condition:
non_capture_form:
```

A capture boundary may support partial capture or bounded provisionality without selecting `non_capture`. Canonical Non-Capture additionally requires that no adequate retained claim remains for the delimited whole claim after adequate bounded attempts.

---

## C.9 Loss Declaration

Every routed record declares exactly five Loss arrays:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

Every Loss entry contains:

```yaml
item_id:
affected_element:
description:
reason:
claim_effect:
source_or_evidence_pointer:       # optional
recoverability_or_reentry_note:   # optional
```

The arrays may be empty only where an explicit substantive finding supports emptiness. They may not be omitted.

```text
empty declared category
≠ undeclared category
```

The five categories are non-interchangeable. `uncertain` is not a polite synonym for `excluded`; `compressed` does not mean recoverable in every later operation; `irrecoverable` does not establish that the source never contained the information.

A chain preserves the ordered set of local Loss profiles. It does not sum, average, or overwrite them.

---

## C.10 Alternatives Declaration

A routed record declares all alternative families:

```yaml
alternatives:
  rival_compositions:
  rival_decompositions:
  rival_projections:
  no_transformation:
  non_translation:
  unresolved:
  no_additional_alternatives_asserted:
  negative_finding_rationale:  # conditional
```

Each alternative entry contains:

```yaml
alternative_id:
claim_relation:
source_basis_or_evidence_pointer:  # optional
comparative_burden:
current_handling:
rationale:
```

The field distinguishes:

- rival transformation;
- no transformation;
- non-translation;
- unresolved alternative.

These are not equivalent. A record may select one transformation while preserving a serious rival. Two rival occurrences may require separate records rather than forced integration.

If `no_additional_alternatives_asserted` is true, the negative-finding rationale must explain the bounded search basis. It cannot claim metaphysical exhaustiveness.

---

## C.11 Governance Declaration

Governance requires:

```yaml
governance:
  authority_inheritance: prohibited
  formal_validation_not_substantive_validation_acknowledged: true
  application_authority_not_granted: true
  claim_ceiling_pointer:
```

Optional but often necessary fields include:

```yaml
authority_ceiling:
external_warrant:
prohibited_inferences_acknowledged:
```

### C.11.1 Authority inheritance

The value is fixed:

```yaml
authority_inheritance: prohibited
```

No upstream authority, formal precision, source prestige, model validation, or visual prominence transfers application authority to a transformation result.

### C.11.2 External warrant

Where a downstream use requires empirical, legal, clinical, political, technical, or domain-specific warrant, that warrant must be declared separately. The record may point to it but cannot generate it.

### C.11.3 Prohibited inferences

The record may list prohibited inferences such as person typing, diagnosis, sanction, legitimacy judgment, universal causal law, or action recommendation. This list preserves the boundary but does not substitute for bounded claim construction.

---

## C.12 Result and Status Axes

The `result` object separates four families:

```yaml
result:
  operation_specific_result:
  status_declaration:
  routing:
  class_payload:
```

These are not interchangeable.

### C.12.1 Operation-specific result

Required fields are:

```yaml
summary:
result_family:
source_function_effect:
prior_source_claim_disposition:
current_claim_pointer:
additional_affected_claim_ids:
```

For DECOMPOSE records, source-function effect and resolution result receive operation-specific restrictions. A DECOMPOSE result may refine or reject a source-function claim without changing the origin type or reference object.

### C.12.2 Status declaration

The status axis requires:

```yaml
support_status:
resolution_test_result:
capture_statement:
evidence_availability_summary:
claim_disposition_pointer:
```

The capture statement includes:

```yaml
statement:
claim_relative:
capture_limit_present:
```

```text
support status
≠ resolution result
≠ Claim Disposition
≠ capture statement
≠ canonical Output Class
```

### C.12.3 Routing

A routed result declares:

```yaml
selected_class:
route_id:
matched_constitutive_conditions:
preserved_non_selected_findings:
split_decision:
class_selection_rationale:
current_claim_disposition:
substantive_judgment_acknowledged: true
candidate_assessments:
same_claim_collision_assessed: true
same_claim_collision_present:
collision_resolution_state:
boundary_adjudication_source_pointer: /result/routing/candidate_assessments
```

All ten candidates are assessed. Exactly one receives status `selected` for the current delimited claim. A first-match-wins shortcut is prohibited.

Candidate assessment includes:

- candidate class;
- status;
- rationale;
- constitutive-condition pointers;
- preserved finding;
- optional rejection reason;
- separated claim or record identifiers;
- candidate-local boundary adjudication.

### C.12.4 Class-specific payload

The selected class determines the required class payload.

| Selected class | Required payload burden |
|---|---|
| `admissible` | ordinary boundedness confirmation and rationale |
| `admissible_with_bounded_claim` | original broader claim, retained narrower claim, material narrowing, excluded reach |
| `admissible_but_provisional` | material provisionality, claim effect, review or re-entry conditions |
| `resolution_neutral` | prior warranted reconstruction, unchanged result, rejected resolution-gain claim |
| `analogy_only` | resemblance, scope, breaking points, rejected stronger identity/projection claim |
| `partially_admissible` | separable parts, retained segments, non-retained or differently classified segments |
| `claim_reduction_required` | excessive dimensions, proposed weaker form, grounding and retest requirement |
| `mandatory_stop` | load-bearing trigger, continuation claim, preserved earlier result, re-entry condition |
| `failed_transformation` | failed operation claim, failed constitutive conditions, preserved source and alternatives |
| `non_capture` | delimited whole claim, captured portions, attempted operations, preserved limits and rivals |

The schema binds each route identifier to its selected class and each selected class to its matching payload. A record cannot select one class while supplying another class's payload.

---

## C.13 Relations and Claim Lineage

`relations` preserves historical and analytical lineage through optional fields:

```yaml
parent_record_id:
parent_claim_id:
prior_record_ids:
prior_claim_ids:
revised_from_claim_id:
reduced_from_claim_id:
successor_to_claim_id:
split_from_claim_id:
sibling_claim_or_record_ids:
chain_id:
previous_occurrence_id:
next_occurrence_id:
rival_record_ids:
countercase_refs:
```

The relation carrier permits a new claim to acknowledge its predecessors without inheriting their result.

```text
successor claim
≠ repaired predecessor

revised record
≠ erased failure history

split claim
≠ whole claim validated
```

An empty `relations: {}` is structurally permitted where no lineage applies. Known lineage must not be omitted to make a later result appear independent.

---

## C.14 Extensions

Extensions are arrays of owner-controlled entries:

```yaml
extensions:
  - extension_id:
    owner_or_source:
    control_source_pointer:
    purpose:
    payload:
    does_not_replace_required_field: true
```

Extensions support bounded local views such as a Minimal Path Record, Alternative Status Record, Minimal Non-Event Record, or chapter-specific diagnostic carrier.

They may not:

- add a fourth operation;
- add an eleventh Output Class;
- replace Source, Loss, Alternatives, Governance, or Result duties;
- hide a chain inside one occurrence;
- invent precise source structure;
- establish admissibility from local syntax;
- create authority inheritance.

```text
local extension
≠ local schema sovereignty
```

---

## C.15 Formal-Diagnostic Structure

A formal diagnostic requires:

```yaml
formal_diagnostic:
  diagnostic_id:
  diagnostic_node_id:
  diagnostic_inventory_status:
  extension_control_source:  # conditional
  extension_rationale:       # conditional
  missing_or_unresolved_requirements:
  preserved_available_material:
  next_permitted_process_handoff:
  rationale:
```

It preserves what is already available and identifies the next permitted process step. It must not use a diagnostic identifier to conceal a substantive failure that is already testable.

A formal diagnostic may later lead to:

- a revised packet;
- a split claim;
- a new occurrence record;
- a routed result;
- an explicit architecture-revision request.

The later result is a new inspectable state. It does not retroactively assign an Output Class to the earlier diagnostic packet.

---

## C.16 Cross-Field Invariants

The schema enforces structural invariants that implement the record contract.

### C.16.1 Scope invariants

```text
operation_occurrence
→ operation allowed and required when routed
→ chain prohibited

integrated_chain
→ chain allowed and required when routed
→ operation prohibited
```

### C.16.2 Routing invariants

```text
routed
→ claim, source, target, loss, alternatives required
→ full twelve-stage audit complete
→ all sixteen Rule assessments complete
→ one route and one class payload required
→ formal_diagnostic prohibited

formal_diagnostic
→ formal_diagnostic required
→ route and class payload prohibited
```

### C.16.3 Operation-function invariants

```text
PROJECT_AS
→ target.contextual_function populated
→ current function-origin occurrence ref null

COMPOSE or DECOMPOSE
→ target.contextual_function null
```

### C.16.4 Stop invariant

```text
selected_class: mandatory_stop
→ stop_assessment.reached: true
→ stop_assessment.mode: mandatory
```

Optional Stop remains a local stop finding and does not map to an additional Output Class.

### C.16.5 Non-Capture invariant

```text
selected_class: non_capture
→ capture limit present
→ material capture limit asserted
→ no adequate retained claim remains
→ capture boundary required
```

### C.16.6 Route-payload invariant

```text
selected_class
↔ exact route_id
↔ exact class_payload family
```

### C.16.7 Candidate-collision invariant

Every routed record assesses all class candidates, checks whether several candidates apply to the same claim, and either resolves the collision or records completed claim splits before selecting one class.

### C.16.8 Non-compensation invariant

```text
non_compensation_confirmation: true
```

is required. The schema can ensure that the acknowledgment is present. It cannot determine whether the analyst's substantive reasoning actually avoided compensation.

---

## C.17 Declaration Completeness, Schema Validity, and Substantive Adequacy

Three levels must remain separate.

### C.17.1 Declaration completeness

Every applicable duty is explicitly addressed, including known gaps, empty categories, no-transformation alternatives, and bounded negative findings.

### C.17.2 Schema validity

The serialized record matches field types, requiredness, enumerations, constants, and conditional relations in `Transformation_Record.schema.json`.

### C.17.3 Substantive adequacy

The record's claims are supported by adequate sources, proper operation identity, traceable load, preserved type and reference integrity, justified loss, serious alternatives, bounded ceilings, and correct route selection.

```text
declaration completeness
≠ schema validity
≠ substantive adequacy
```

A record can be declaration-complete and schema-valid while failing TraceableLoad. A record can be substantively cautious but formally diagnostic because claim segmentation is unresolved. A genuine Non-Capture record can be declaration-complete while explicitly stating that complete capture is not available.

---

## C.18 Compact Routed Record Skeleton

The following skeleton shows the common placement of fields. It is intentionally abbreviated and is not a schema-valid substitute for the operation-specific templates in Appendices D–F.

```yaml
schema_version: 0.1.2
record_id: <record-id>
record_scope: operation_occurrence
routing_state: routed

record_metadata:
  created_at: <timestamp>
  updated_at: <timestamp>
  revision_id: <revision>
  record_provenance:
    - <provenance statement>
  model_versions:
    operation_registry: <version>
    output_classes: <version>
    admissibility_rules: <version>
    boundary_decision_tree: <version>
  formal_validation_not_substantive_validation_acknowledged: true

claim:
  claim_id: <claim-id>
  statement: <bounded tested claim>
  claim_type: <controlled term>
  claim_role: <controlled term>
  claim_scope: <complete claim scope>
  validity_scope: <bounded validity scope>
  claim_ceiling: <complete claim ceiling>
  authority_boundary: <explicit boundary>

source:
  reference_object: <object reference>
  object_typing: <controlled term>
  frame: <controlled term>
  granularity: <controlled term>
  relative_level: <controlled term>
  temporal_scope: <scope>
  source_scope: <scope>
  source_basis:
    - <at least one complete source-basis item>
  constitutive_source_trace:
    - <at least one complete trace entry>
  known_gaps: []
  source_ceiling: <complete source ceiling>

operation:
  occurrence_id: <occurrence-id>
  kind: COMPOSE | DECOMPOSE | PROJECT_AS
  justification: <reasoned operation identity>
  expected_praxeological_difference: <purchase>
  selection_rule: <selection rule>
  transformation_context: <context>
  details: <operation-specific payload>

target:
  reference_object: <object reference>
  object_typing: <controlled term>
  contextual_function: <controlled term or null>
  frame: <controlled term>
  granularity: <controlled term>
  relative_level: <controlled term>
  temporal_scope: <scope>
  validity_scope: <scope>
  contextual_function_origin_occurrence_ref: <pointer or null>

admissibility:
  audit_stages: <all twelve stages>
  rule_assessments: <all sixteen Rules>
  non_compensation_confirmation: true
  audit_to_routing_basis: <reasoned mapping>
  anti_immunization_assessment: <assessment>
  stop_assessment: <assessment>
  non_capture_assessment: <assessment>

loss:
  preserved: []
  compressed: []
  excluded: []
  uncertain: []
  irrecoverable: []

alternatives:
  rival_compositions: []
  rival_decompositions: []
  rival_projections: []
  no_transformation: []
  non_translation: []
  unresolved: []
  no_additional_alternatives_asserted: false

governance:
  authority_inheritance: prohibited
  formal_validation_not_substantive_validation_acknowledged: true
  application_authority_not_granted: true
  claim_ceiling_pointer: /claim/claim_ceiling

result:
  operation_specific_result: <local result>
  status_declaration: <separate status axes>
  routing: <candidate assessments and selected route>
  class_payload: <payload matching selected class>

relations: {}
extensions: []
```

A directly usable YAML occurrence template belongs to Appendix D, E, or F because the operation-specific payload and applicability constraints differ materially.

---

## C.19 Compact Formal-Diagnostic Skeleton

```yaml
schema_version: 0.1.2
record_id: <diagnostic-record-id>
record_scope: operation_occurrence
routing_state: formal_diagnostic

record_metadata: <complete metadata>
admissibility: <available formal assessment state>
governance:
  authority_inheritance: prohibited
  formal_validation_not_substantive_validation_acknowledged: true
  application_authority_not_granted: true
  claim_ceiling_pointer: /claim/claim_ceiling
result:
  operation_specific_result: <optional preserved local material>
  status_declaration: <optional status material>
relations: {}
formal_diagnostic:
  diagnostic_id: <diagnostic-id>
  diagnostic_node_id: incomplete_packet
  diagnostic_inventory_status: current_controlled
  missing_or_unresolved_requirements:
    - <unresolved prerequisite>
  preserved_available_material:
    - <material that must not be discarded>
  next_permitted_process_handoff: <next bounded process step>
  rationale: <why routing is not yet permitted>
```

The exact allowed diagnostic identifiers remain owned by the current Boundary Decision Tree and record schema. This skeleton does not create a new diagnostic inventory.

---

## C.20 Positive and Negative Schema Readings

### C.20.1 Positive reading

A routed record is structurally and substantively inspectable when:

- the claim is delimited;
- the source object and Source Ceiling are explicit;
- source-basis items identify what supports which claim component;
- Constitutive Source Trace states how the result depends on source features;
- one operation occurrence is identified;
- target identity or target function is bounded;
- all applicable Rules are assessed without compensation;
- Loss and serious alternatives are declared;
- Stop and Non-Capture are assessed;
- one Output Class is selected after candidate collision adjudication;
- prior failures and claim lineage remain preserved;
- authority inheritance is prohibited.

### C.20.2 Syntactically complete but substantively insufficient

A record can fill every required text field with generic language:

```yaml
source_basis:
  - provenance_description: several relevant documents

constitutive_source_trace:
  - source_feature: the documents support the result
```

The record may still fail because it does not identify:

- which source feature supports which claim component;
- what material source change would alter the result;
- what the Source Ceiling excludes;
- why the selected operation is constitutive;
- how a rival or no-transformation route compares.

Depending on the delimited claim, the correct route may be:

```text
claim_reduction_required
failed_transformation
mandatory_stop
```

If the claim or operation cannot yet be delimited, the packet remains `formal_diagnostic` instead.

### C.20.3 Genuine epistemic incompleteness

A record may honestly state:

- source relation underdetermined;
- rival decompositions unresolved;
- exact calibration unavailable;
- one capture remainder persists.

That does not make the record analytically defective. The route depends on what adequate bounded claim remains. Invented precision is a defect; explicit bounded incompleteness is inspectable.

---

## C.21 Human-Readable Markdown Companion

Every operation-record YAML in the current Case corpus has a same-basename Markdown companion. The companion exists to make the record reviewable without reading the entire serialization.

The reusable template is maintained at:

```text
03_cases/templates/case_template.md
```

The companion must summarize, not duplicate or override, the YAML record. It should expose:

- record and claim identity;
- source and target;
- operation occurrence;
- local result and selected Output Class;
- five-part Loss;
- alternatives;
- Stop and Non-Capture boundary;
- claim and authority limits;
- record/package links.

```text
Markdown companion
≠ second operation occurrence
≠ second adjudication
≠ theory source
```

---

## C.22 Validation Layers

The Shared Transformation Record participates in several distinct checks.

### Layer 1 — parseability

The YAML or JSON instance can be read as structured data.

### Layer 2 — schema conformance

The instance validates against `Transformation_Record.schema.json`.

### Layer 3 — package consistency

Pointers, identifiers, case pairing, lineage, chain order, and referenced artifacts are consistent.

### Layer 4 — substantive audit

The sources, operation identity, continuity, Loss, alternatives, ceilings, Stop, Non-Capture, and route are reasoned and supportable.

### Layer 5 — external warrant

Any empirical, legal, clinical, political, technical, or application use obtains the required external warrant.

```text
Layer 1 or 2
≠ Layer 4

Layer 4
≠ Layer 5
```

Appendix N will integrate the full twelve-stage substantive audit and chain handoff. Model Finalization will revisit schema synchronization after the corpus and references are frozen.

---

## C.23 Schema Revision Boundary

A schema revision is justified only where a documented corpus-level need cannot be carried by existing fields or bounded extensions without distortion.

Examples of legitimate pressure include:

- a canonical duty has no structural carrier;
- a conditional invariant permits a prohibited state;
- an existing field collapses two load-bearing axes;
- a required chain handoff cannot be represented;
- the schema contradicts an authoritative prose owner.

Examples that do not justify revision include:

- preference for shorter records;
- desire to automate substantive judgment;
- desire for a new local label;
- pressure to merge several occurrences;
- desire for numeric scoring or class ranking;
- desire to encode a person diagnosis or application decision.

The present Appendix-C comparison finds no need for a new top-level field, operation, Output Class, Loss category, routing state, record scope, or authority carrier. The existing schema supplies structural carriers for the current canonical record duties.

---

## C.24 Completion Test

Appendix C is substantively complete when all of the following hold:

1. the Shared Transformation Record is clearly distinguished from the transformation;
2. Chapter 7 remains the semantic owner and the JSON Schema remains the syntax owner;
3. both record scopes and both routing states are explained;
4. routed and formal-diagnostic requiredness are separated;
5. every top-level field family has a declared purpose;
6. Source Basis and Constitutive Source Trace remain distinct;
7. operation-specific detail payloads do not flatten operation identity;
8. target function is restricted to PROJECT_AS;
9. all twelve audit stages and sixteen Rule assessments remain visible;
10. all five Loss fields remain exact and non-scalar;
11. Alternatives, Governance, Stop, Non-Capture, and Claim Ceiling cannot be bypassed;
12. route, status axes, local result, and class payload remain separate;
13. each routed claim selects exactly one canonical Output Class after collision assessment;
14. formal diagnostics receive no canonical Output Class;
15. claim lineage preserves prior failures and reductions;
16. extensions cannot replace shared duties;
17. chains preserve one record per occurrence and separate local Loss/results;
18. a negative example shows that schema validity is not substantive validity;
19. the human-readable companion template is populated;
20. no new operation, class, primitive, field family, or authority is introduced.

The current result is:

```text
admissible_with_bounded_claim
```

This result applies to Appendix C as a bounded explanatory and template-owning artifact. It does not certify every existing or future record's substantive adequacy.

---

## C.25 Handoff

Appendix C hands forward to:

```text
Appendix D
→ COMPOSE occurrence template

Appendix E
→ DECOMPOSE occurrence template

Appendix F
→ PROJECT_AS occurrence template

Appendix G
→ detailed Admissibility Band tests

Appendix N
→ integrated twelve-stage audit and chain template
```

The downstream templates must instantiate this shared schema without redefining it.

```text
shared schema
+ operation-specific template
→ usable occurrence record

not:
operation-specific template
→ independent record grammar
```
