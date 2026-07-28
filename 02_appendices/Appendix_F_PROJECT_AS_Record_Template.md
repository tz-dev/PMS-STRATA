# Appendix F — PROJECT_AS Record Template

**Status:** substantive bounded provisional completion  
**Primary prose owners:** Chapters 5, 29, 30, 31, 32, 34, and 36  
**Shared record owner:** Chapter 7 and `07_model/Transformation_Record.schema.json`  
**Operation registry owner:** `07_model/Operation_Registry.yaml#/operation_types/PROJECT_AS`  
**Reusable YAML fixture:** `03_cases/templates/project_as_case_template.yaml`

---

## F.1 Purpose and Boundary

Appendix F specifies the operation-specific record duties for exactly one `PROJECT_AS` occurrence.

The canonical movement is:

```text
origin-typed source object
→
bounded contextual target function
```

PROJECT_AS preserves source reference and origin type while testing whether the source performs an additional function within a declared target context.

```text
PROJECT_AS
≠ analogy
≠ label substitution
≠ recontextualization alone
≠ origin-type replacement
≠ COMPOSE
≠ DECOMPOSE
```

The YAML fixture is schema-valid and contains a worked positive projection. It is not a reusable finding. Every source feature, target context, function claim, comparison, Loss entry, and route must be replaced or affirmatively re-established.

---

## F.2 Entry Test: Is PROJECT_AS the Correct Operation?

Use PROJECT_AS only where the tested claim is that an independently identified and origin-typed source object performs a distinct, source-dependent function in a bounded target context.

The entry question is:

> Given source object X of origin type T_o, does X perform target function F_t in context C_t, and does that function disappear, weaken, or change when load-bearing source features or the target context are varied?

Appropriate source objects include:

- a warranted Path or Trajectory;
- a composite structure;
- an event-like or non-event structure;
- a configuration;
- a reconstructed source object from a prior DECOMPOSE occurrence;
- another independently typed analytical object.

Do not use PROJECT_AS where:

- the target is merely a new composite object — use COMPOSE;
- the source is being opened under finer granularity — use DECOMPOSE;
- the source is merely relevant background;
- a metaphor or analogy is being proposed;
- the target label replaces the origin type;
- the target context is vague;
- present target structures explain the alleged function without source dependence.

---

## F.3 Source Object and Origin Type

The Source Declaration must identify the source independently of the target function.

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

The origin type must remain visible before, during, and after projection.

```text
X : T_o
PROJECT_AS
F_t @ C_t
```

means:

```text
X functions as F_t in C_t
```

not:

```text
X becomes F_t as origin type
```

If the origin typing itself is under revision, resolve that source claim separately. PROJECT_AS cannot be used to smuggle in a retyping of the source.

---

## F.4 Claim Declaration

A useful claim form is:

```text
Origin-typed source object X performs bounded target function F_t
within target context C_t and validity scope V,
while source reference and origin type remain preserved.
```

The Claim Scope must specify:

- source reference object;
- this PROJECT_AS occurrence;
- source and target frames;
- source and target granularities;
- relative-level relation;
- temporal scope;
- target context and scene;
- role or relation boundaries where relevant;
- generalization boundary;
- excluded reach.

The Claim Ceiling should exclude:

- function outside the target context;
- permanent or universal function;
- origin-type replacement;
- causal monopoly;
- prediction;
- moral, legal, clinical, political, or application authority;
- function for persons or roles not included in the target relation.

---

## F.5 Target Context

The operation payload requires:

```yaml
operation:
  details:
    target_context:
```

The target context must identify enough structure to make the function distinguishable:

- target scene, object, or configuration;
- target frame;
- relative target level;
- relevant roles and relations;
- temporal cut or duration;
- analytical purpose;
- current structures and alternatives;
- comparison context or no-projection condition.

Vague phrases are insufficient:

```text
at the macro level
in the system
for the organization
later on
```

A valid context tells the reader where the source is claimed to make a practical difference.

---

## F.6 Proposed Target Function

The target function should name the work performed in the target context, not a new identity of the source.

Examples include bounded:

- frame-function;
- macro-event function;
- attractor-function;
- threshold function;
- access function;
- coordination function;
- repair-cost function;
- another context-specific function.

The function label does not establish functional load.

```text
function label
≠ function demonstrated
```

The target declaration requires a non-null controlled term:

```yaml
target:
  contextual_function:
    value:
    control_source:
    inventory_status:
```

Only PROJECT_AS may populate this field with a contextual function.

---

## F.7 Constitutive Source Trace

The PROJECT_AS payload duplicates the constitutive trace by pointer-preserving structure because the projection claim depends directly on source features:

```yaml
operation:
  details:
    constitutive_source_trace:
```

For every load-bearing source feature, declare:

- source feature;
- affected target-function component;
- trace role;
- result dependency;
- expected result change under variation;
- temporal or relational dependency;
- claim limitation;
- source pointer where available.

The trace must support the **function**, not merely historical relevance.

```text
source matters historically
≠ source performs an additional target function
```

---

## F.8 Preservation Declarations

The payload requires:

```yaml
source_reference_preserved: true | false
origin_type_preserved: true | false
target_function_bounded: true | false
```

A routed positive projection normally requires all three to be true. If source reference or origin type is replaced, the operation fails Type Integrity. If the target function is unbounded, Claim Reduction, Stop, or Failure pressure arises.

The record should explain preservation, not merely set booleans.

---

## F.9 Alternative Projection or No Projection

The payload requires explicit comparison:

```yaml
alternative_projection_or_no_projection:
```

At minimum test:

- another plausible bounded function;
- background relevance only;
- present target structures as sufficient explanation;
- no additional function;
- analogy or metaphor only;
- a different target context;
- a narrower role or temporal scope.

The same source may warrant a function in one context and no additional function in another.

```text
function in C1
≠ function in C2 automatically
```

No-projection is a valid result. It does not invalidate the source object.

---

## F.10 Target Declaration

The target record should represent the function while preserving source identity:

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
  contextual_function_origin_occurrence_ref: null
```

The target `reference_object` may name the function-bearing relation or target-side analytical object, but the source object must remain traceable. The target typing must not state that the source has become the function type.

The target validity scope should specify:

- target context;
- role relation;
- temporal interval;
- function boundary;
- exclusion of transfer;
- authority boundary.

---

## F.11 Counterfactual Sensitivity

PROJECT_AS requires a particularly strong source-variation test.

Ask:

1. If a load-bearing source feature is removed or materially changed, does the target-function claim weaken or disappear?
2. If the target context is replaced by a comparison context, does the function remain?
3. If present target structures alone are retained, is the source-dependent function still necessary?
4. If only the label is removed, does the target reconstruction change?
5. If origin type is preserved but the proposed function is withdrawn, does the source object remain valid?

Controlled local sensitivity results remain:

```text
strongly_sensitive
partially_sensitive
weakly_sensitive
insensitive
underdetermined
untestable
```

A projection that is insensitive to both source variation and context variation is likely label substitution, background relevance, analogy, or failed transformation.

---

## F.12 Contextual Boundedness

A target function must be bounded by:

- declared context;
- target frame;
- role or relation;
- temporal scope;
- analytical purpose;
- source carriers;
- comparison condition;
- Claim Ceiling.

The record must make defeat conditions visible. A function that cannot be weakened or withdrawn by any source or context variation is immunized rather than bounded.

```text
contextual boundedness
≠ arbitrary local wording
```

The context must be source-supported and substantively relevant.

---

## F.13 Type Integrity

PROJECT_AS has the strongest explicit Type Integrity burden.

The record must show:

```text
origin type preserved
+ target function grammatically and structurally marked as function
+ source record remains available
+ no target label overwrites source typing
```

Frequent failures include:

- “Trajectory X is now a Frame”;
- “Composite Q becomes an Attractor”;
- “the person is a PROJECT_AS function”;
- “the source belongs to a higher ontological level”;
- “the contextual function proves the source’s true identity.”

These are not bounded projections.

---

## F.14 Functional Continuity

Functional Continuity asks whether the source-to-target relation actually carries the proposed function.

A target function is supported only where:

- the source feature remains identifiable;
- the target-side difference is explicit;
- the relation survives relevant counterfactual pressure;
- present target structures do not fully replace source dependence;
- the function is not generated solely by analogy or label;
- any competing function is considered.

Historical continuity alone is insufficient.

```text
same history retained
≠ same target function warranted
```

---

## F.15 Projection versus Recontextualization

Recontextualization changes how the source is described or viewed. PROJECT_AS claims that the source performs additional work in the target context.

A practical test:

```text
remove the proposed source-to-context functional relation
→ does the target reconstruction change?
```

If access, cost, relevance, expectation, alternatives, or action corridors remain unchanged, the result may be recontextualization without projection.

---

## F.16 Projection versus Analogy

Analogy states similarity. Projection states bounded function.

```text
X resembles F
≠ X performs F in C
```

An analogy may be useful and route to `analogy_only`. It cannot be upgraded to PROJECT_AS merely because the target label is illuminating.

The record should preserve analogy as a non-selected finding where relevant rather than erasing it.

---

## F.17 Loss Record

Typical PROJECT_AS Loss includes:

- source complexity compressed into selected functional carriers;
- source features excluded because they do not bear on the target function;
- exact magnitude or mechanism left uncertain;
- target-side alternatives omitted from the bounded claim;
- some source-to-function relation irrecoverable from available evidence.

All five canonical fields remain required. A projection is never presumed lossless simply because origin type is preserved.

---

## F.18 Alternatives and Competing Projections

PROJECT_AS may yield several rival target functions. Each must remain a separate claim and, where executed, a separate operation record.

```text
same source object
+ same target context
+ different candidate functions
→ competing PROJECT_AS claims
```

Do not merge them into one vague “multi-function” claim unless a new claim explicitly tests that combination.

Assess:

- source trace for each candidate;
- target-side difference;
- context dependence;
- collision on the same claim;
- whether one function subsumes or contradicts another;
- no-projection and analogy alternatives;
- Claim Ceiling for each candidate.

---

## F.19 Stop, Failure, Claim Reduction, and Non-Capture

Mandatory Stop applies where continuation would require:

- origin-type replacement;
- vague or unsupported target context;
- source-independent function;
- person typing or diagnosis;
- authority inheritance;
- unbounded generalization;
- automatic action recommendation;
- conversion of analogy into function;
- concealment of a prior failed claim.

Claim Reduction applies where a narrower context, role, interval, or functional component remains supported.

Failure applies where the operation does not establish a distinct function or violates Type Integrity.

Non-Capture remains possible only after adequate bounded attempts and a persistent capture limit; it is not a rescue label for a weak projection.

---

## F.20 Output Routing

The schema-valid fixture selects a positive bounded route. For a new record, this selection must be discarded and rebuilt from the actual findings.

Check consistency among:

- target contextual function;
- source and origin-type preservation;
- contextual boundedness;
- counterfactual sensitivity;
- source and Claim Ceilings;
- alternatives;
- Stop and Non-Capture;
- selected class and class payload.

A source-dependent function may still route to:

- `admissible_but_provisional` where calibration remains open;
- `partially_admissible` where only some function components carry;
- `claim_reduction_required` where scope is too broad;
- `analogy_only` where similarity survives but functional load does not;
- `failed_transformation` where projection fails;
- `mandatory_stop` or `non_capture` under their distinct conditions.

---

## F.21 Chain Participation

PROJECT_AS frequently participates in:

```text
COMPOSE → PROJECT_AS
DECOMPOSE → PROJECT_AS
PROJECT_AS → DECOMPOSE
COMPOSE → PROJECT_AS → DECOMPOSE
```

A prior COMPOSE or DECOMPOSE result supplies an origin-typed source object; it does not pre-authorize projection. A later DECOMPOSE occurrence must identify whether it reopens the origin source or tests a source-side structure relevant to the function.

Each occurrence preserves its own Loss, result, and claim history.

---

## F.22 Worked-Fixture Use Protocol

To use `project_as_case_template.yaml`:

1. copy it to the case YAML directory;
2. replace IDs, metadata, and pointers;
3. identify the source object and independent origin type;
4. declare the target context precisely;
5. name one bounded target function;
6. rebuild Constitutive Source Trace around functional load;
7. declare source-reference, origin-type, and bounded-function preservation;
8. add a comparison or no-projection context;
9. test source and context counterfactuals;
10. repopulate Loss and Alternatives;
11. assess Type Integrity, Functional Continuity, Stop, and Non-Capture;
12. rebuild all ten class candidates and select the actual route;
13. create the same-basename Markdown companion.

Never retain the fixture’s target function or route merely to preserve schema validity.

---

## F.23 Completion Checklist

A PROJECT_AS record is ready only where:

- exactly one PROJECT_AS occurrence is declared;
- source reference and origin type are independently stated;
- target context is specific and source-supported;
- target function is distinct from a label or analogy;
- target `contextual_function` is non-null and bounded;
- origin type remains preserved;
- Constitutive Source Trace supports functional load;
- a no-projection or competing projection is assessed;
- source and context variation affect the claim where expected;
- Type Integrity and Functional Continuity are explicit;
- all five Loss fields are populated;
- Stop, Failure, Claim Reduction, and Non-Capture remain distinct;
- exactly one Output Class is selected after collision assessment;
- no person typing, diagnosis, authority inheritance, or automatic action recommendation is introduced.

The bounded Appendix-F result is:

```text
admissible_with_bounded_claim
```

---

## F.24 Handoff

Appendix F hands forward to:

```text
Appendix G
→ detailed Admissibility Band tests

Appendix H
→ valid and invalid transformation patterns

Appendix I
→ boundary and confusion cases

Appendix K
→ cross-domain projection and analogy stress tests

Appendix N
→ integrated audit and chain template
```
