# Appendix E — DECOMPOSE Record Template

**Status:** substantive bounded provisional completion  
**Primary prose owners:** Chapters 18, 20, 22, and 23  
**Shared record owner:** Chapter 7 and `07_model/Transformation_Record.schema.json`  
**Operation registry owner:** `07_model/Operation_Registry.yaml#/operation_types/DECOMPOSE`  
**Reusable YAML fixture:** `03_cases/templates/decompose_case_template.yaml`

---

## E.1 Purpose and Boundary

Appendix E specifies how the Shared Transformation Record is populated for exactly one `DECOMPOSE` occurrence.

The canonical movement is:

```text
provisionally compressed occurrence or composite
→
finer reconstruction of the same reference object
```

DECOMPOSE opens internal structure under a declared question and granularity. It does not atomize operator types, descend toward a truer reality, create a new Path by stealth, or assign a contextual target function.

```text
DECOMPOSE
≠ operator-type decomposition
≠ exhaustive description
≠ truth descent
≠ reverse COMPOSE
≠ hidden PROJECT_AS
```

The reusable YAML is a schema-valid worked fixture. Its synthetic reconstruction, findings, and route are examples only. Every substantive field must be replaced or expressly re-established for the new source object.

---

## E.2 Entry Test: Is DECOMPOSE the Correct Operation?

Use DECOMPOSE when the current analytical object is provisionally compressed and a finer reconstruction may change a claim-relevant distinction while preserving the same reference object.

The entry question is:

> What finer internal components, relations, or temporality can be reconstructed for this same source object, under this question and granularity, and what happens to its current function claim?

Appropriate source objects include:

- compressed operator occurrences;
- compressed events or non-events;
- compressed composite structures;
- Paths or Trajectories treated as source objects;
- phase, event-cluster, or branch composites;
- prior projection-derived objects, provided the source of decomposition is explicitly identified and not confused with the target function.

Do not use DECOMPOSE to:

- open a PMS operator type;
- create a different reference object and call it a finer version;
- assert that more detail is inherently more true;
- replace a source function without recording its disposition;
- produce a contextual function;
- escape a failed claim by changing granularity without a new record.

If the source reference or decomposition question is unresolved, preserve a formal diagnostic rather than forcing a routed occurrence.

---

## E.3 Source Object Declaration

The top-level Source Declaration must identify one compressed reference object and its current analytical status.

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

The operation payload adds the source-function question and decomposition-specific reasons:

```yaml
operation:
  details:
    source_function:
    decomposition_question:
    insufficiency_of_current_compression:
```

### E.3.1 Provisional compression

Compression must be declared rather than presumed. State:

- which distinctions are currently compressed;
- why those distinctions may matter to the tested claim;
- what the current representation can and cannot support;
- whether the source function is already claimed, merely suspected, or under dispute;
- what finer granularity is being requested.

```text
compressed
≠ erroneous
≠ incomplete in every respect
```

A compressed form may remain sufficient. DECOMPOSE is warranted only where finer resolution has possible praxeological purchase.

### E.3.2 Same-reference requirement

The reconstruction must remain of the same reference object. Nominal continuity is insufficient, but a newly created object is not a decomposition merely because it reuses the source label.

Assess:

- source reference before and after the operation;
- preserved origin typing;
- coordinate change;
- constitutive carriers of identity;
- any shift from reconstruction to replacement.

---

## E.4 Claim Declaration

A DECOMPOSE claim should state the source object, the finer question, the target granularity, and the expected source-function effect.

A useful form is:

```text
Source object X can be reconstructed at finer granularity g_t
as components K with relations R_K and internal temporality τ_K,
while preserving reference X and reassessing source function F_s.
```

The claim scope must exclude:

- operator-type decomposition;
- claims beyond the same reference object;
- universal truth advantage of finer granularity;
- hidden function projection;
- lossless recovery of an untouched original;
- automatic causal or psychological interpretation.

The Claim Ceiling should specify what resolution gain can and cannot establish.

---

## E.5 Decomposition Question

The decomposition question is the governing local reason for opening the source.

```yaml
operation:
  details:
    decomposition_question:
```

A useful question identifies:

- the compressed distinction at issue;
- the claim it may change;
- the target granularity;
- the relevant temporal or relational scope;
- the required source support;
- a Stop condition.

Bad questions are unlimited:

```text
“What is really inside X?”
“Can X be made more detailed?”
```

Better questions are bounded:

```text
“Does the compressed handoff contain distinct access-blockage and responsibility-transition structures, and how does each affect the source-function claim?”
```

The operation may end in resolution gain, neutrality, drift, escape, Stop, failure, or Non-Capture. The question must permit those outcomes.

---

## E.6 Insufficiency of Current Compression

The field:

```yaml
operation:
  details:
    insufficiency_of_current_compression:
```

must state why the present resolution cannot adequately test the claim. It should not merely repeat that finer detail is desired.

Possible insufficiencies include:

- two load-bearing phases collapsed into one occurrence;
- a central non-event hidden inside an event label;
- relation topology compressed into a list;
- temporal order or overlap unavailable at the current resolution;
- source-function effects that cannot be distinguished;
- rival decompositions that remain conflated.

If no claim-relevant insufficiency is shown, the result may be below the Relevance Floor or an Optional Stop after sufficiency.

---

## E.7 Components and Typing

The operation payload requires components:

```yaml
operation:
  details:
    components:
      - component_id:
        description:
        component_typing:
        source_pointer:
```

Components are reconstruction products, not newly discovered primitives. For each component, state:

- its local identity;
- its analytical typing;
- the source feature supporting it;
- its temporal or relational position;
- its uncertainty;
- whether it is constitutive, secondary, or unresolved.

```text
component
≠ PMS operator type
≠ atom
≠ independent truth unit
```

The number of components is not a quality measure. More components may push the reconstruction above the Traceability Ceiling.

---

## E.8 Component Relations and Internal Temporality

A decomposition is not adequate if it produces isolated pieces but loses the source object's internal binding.

```yaml
operation:
  details:
    component_relations:
    internal_temporality:
```

Relations may include:

- sequence;
- overlap;
- dependency;
- conditional activation;
- asymmetry;
- role transfer;
- binding or residual load;
- partial ordering;
- unresolved relation.

Internal temporality should distinguish:

- component duration;
- order and overlap;
- event and non-event relation;
- phase transition;
- temporal uncertainty;
- retrospective reconstruction from directly observed sequence.

A finer timeline must not be invented merely because the template has a field for it.

---

## E.9 Source Support

The DECOMPOSE payload carries operation-specific support:

```yaml
operation:
  details:
    source_support:
```

This support should connect each component and relation to the Source Basis and Constitutive Source Trace. State where:

- a component is directly supported;
- it is reconstructed from several sources;
- its boundary is uncertain;
- the relation is inferred rather than directly recorded;
- an alternative decomposition remains plausible;
- source limits require claim reduction or Stop.

Formal presence of a source pointer does not establish that the component is warranted.

---

## E.10 Reference and Origin-Type Preservation

The payload must affirm or deny:

```yaml
operation:
  details:
    source_reference_preserved:
```

and point to:

```yaml
source_reference_object_pointer:
origin_type_pointer:
target_granularity_pointer:
```

If source reference is not preserved, the claim is not an admissible decomposition of that object. It may be a new composition, a replacement, a comparison, or a failed transformation.

Origin type may later be revised through source-supported analysis, but it cannot be silently changed because finer components resemble another type.

---

## E.11 Source Function and Effect

DECOMPOSE must not assume that the prior source-function claim survives unchanged.

The record should declare:

```yaml
operation:
  details:
    source_function:
    prior_source_claim_id:
```

and route the result through:

```yaml
result:
  operation_specific_result:
    source_function_effect:
    prior_source_claim_disposition:
```

Possible effects include confirmation, refinement, internal differentiation, partial preservation, rejection, or underdetermination, using the actual controlled vocabulary in the schema.

```text
finer reconstruction
≠ automatic confirmation of the coarser function
```

A failed prior source claim remains failed even if a new narrower claim later succeeds.

---

## E.12 Resolution Test

DECOMPOSE uniquely requires an explicit resolution result. The target record must distinguish:

```text
resolution_gain
resolution_neutral
resolution_drift
resolution_escape
```

### Resolution gain

The finer reconstruction changes a claim-relevant distinction while preserving reference and type integrity.

### Resolution neutral

Additional detail does not change the warranted claim. This is a canonical Output Class only where the route is `resolution_neutral` and all schema conditions are satisfied.

### Resolution drift

The reconstruction accumulates detail but moves away from the tested distinction or source function.

### Resolution escape

The operation changes granularity, frame, level, reference, or claim so that the original burden is evaded rather than resolved.

```text
new granularity
≠ repaired failed claim
```

---

## E.13 Target Reconstruction

For DECOMPOSE, the target remains a reconstruction of the same reference object:

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
```

`contextual_function` must remain `null`. If the finer reconstruction is later tested for a contextual function, that requires a separate `PROJECT_AS` record.

The target granularity should be relationally finer for the declared question, not universally higher or truer.

---

## E.14 Residual Binding and Unresolved Structure

A valid decomposition may leave structure unresolved. The payload therefore includes:

```yaml
operation:
  details:
    unresolved_structure:
```

Unresolved structure should state:

- what remains compressed;
- why it cannot be responsibly opened;
- whether the limit is source-based, calibration-based, or capture-based;
- what distortion would follow from forcing closure;
- what new evidence or method could permit re-entry.

Residual binding matters where the source object remains a whole whose components cannot be treated as independent.

```text
components identified
≠ whole exhausted
```

---

## E.15 Counterfactual Component Test

The operation-specific counterfactual test asks:

> If component K_i or relation R_j is removed, altered, or merged back into the compressed source, what changes in the source-function claim or target reconstruction?

The payload field is:

```yaml
operation:
  details:
    counterfactual_component_test:
```

Use the test to distinguish:

- load-bearing components;
- explanatory but non-constitutive detail;
- arbitrary segmentation;
- rival decompositions;
- components whose removal changes only narrative richness;
- components whose removal collapses the claim.

---

## E.16 Loss Record

All five fields remain mandatory. Typical DECOMPOSE Loss includes:

- source compression partly preserved because not all structure can be opened;
- local relations compressed into component labels;
- unsupported micro-detail excluded;
- component boundaries uncertain;
- original undifferentiated experience irrecoverable after analytical segmentation.

DECOMPOSE does not reverse prior COMPOSE Loss automatically.

```text
DECOMPOSE(COMPOSE(X)) ≠ X
```

The new record must inherit and reassess prior Loss rather than overwrite it.

---

## E.17 Alternatives

DECOMPOSE-relevant alternatives include:

- rival component boundaries;
- temporal versus relational decomposition;
- phase versus role decomposition;
- no decomposition because current resolution is sufficient;
- claim reduction without further opening;
- external methods where STRATA cannot capture the object;
- later projection of the source or reconstruction as a separate operation.

Competing decompositions may each capture different load-bearing relations. Their coexistence does not automatically require integration; forced integration may produce genuine Non-Capture pressure.

---

## E.18 Stop and Non-Capture

Mandatory Stop applies where continuation would:

- decompose an operator type;
- cross the Source Ceiling;
- lose source reference;
- create unsupported component boundaries;
- perform hidden RETYPE;
- escape the tested claim;
- imply person diagnosis or authority.

Optional Stop applies where the current reconstruction is sufficient and further opening adds no praxeological purchase.

Genuine Non-Capture requires adequate bounded attempts and a persistent capture limit. It is not a label for missing information or one failed decomposition.

---

## E.19 Output Routing

The worked YAML fixture contains a valid positive route, but new records must independently assess all ten candidates. DECOMPOSE additionally requires consistency among:

- `status_declaration.resolution_test_result`;
- local source-function effect;
- prior source-claim disposition;
- selected Output Class;
- class payload;
- Stop and Non-Capture assessments.

A `resolution_gain` does not automatically imply `admissible`; the wider claim may still require narrowing, remain provisional, or fail another rule.

---

## E.20 Chain Participation

Common chains include:

```text
COMPOSE → DECOMPOSE
DECOMPOSE → COMPOSE
DECOMPOSE → PROJECT_AS
PROJECT_AS → DECOMPOSE
COMPOSE → PROJECT_AS → DECOMPOSE
```

Where PROJECT_AS precedes DECOMPOSE, the record must identify whether it is decomposing the origin-typed source object or merely analyzing the target-function claim. A target function is not itself automatically a decomposable source object.

Each occurrence has a separate record, Loss profile, route, and claim.

---

## E.21 Worked-Fixture Use Protocol

To use `decompose_case_template.yaml`:

1. copy it to the case YAML directory;
2. replace all IDs and metadata;
3. declare the compressed source object and current source function;
4. state the bounded decomposition question;
5. explain insufficiency of current compression;
6. replace components, relations, temporality, and source support;
7. test same-reference preservation;
8. declare unresolved structure and residual binding;
9. run the counterfactual component test;
10. determine source-function effect and resolution result;
11. repopulate all Loss and Alternative fields;
12. assess Stop, capture boundary, and Non-Capture;
13. route the actual claim after candidate collision assessment;
14. create the same-basename Markdown companion.

---

## E.22 Completion Checklist

A DECOMPOSE record is ready only where:

- exactly one DECOMPOSE occurrence is declared;
- the source is an occurrence or composite, never an operator type;
- provisional compression is explicit;
- the decomposition question is bounded;
- target granularity is declared;
- components, relations, and internal temporality are source-supported;
- source reference is preserved;
- the prior source-function claim is tracked;
- unresolved structure is retained;
- a counterfactual component test is documented;
- the resolution result is declared;
- `contextual_function` remains `null`;
- all five Loss fields and all Alternatives are assessed;
- Stop and Non-Capture remain distinct;
- exactly one canonical Output Class is selected;
- no finer-is-truer or authority claim is introduced.

The bounded Appendix-E result is:

```text
admissible_with_bounded_claim
```

---

## E.23 Handoff

Appendix E hands forward to:

```text
Appendix G
→ Admissibility Band tests

Appendix H
→ valid and invalid patterns

Appendix I
→ boundary and confusion cases

Appendix L
→ Non-Operator Remainders and decomposition limits

Appendix N
→ integrated audit and chain template
```
