# Appendix B — Formal Notation

**Status:** substantive bounded provisional completion; cross-artifact lock conditioned on Reference Freeze and the Integrated Corpus Audit  
**Repository role:** formal notation and cross-artifact translation supplement; not an independent semantic, mathematical, or theory source  
**Authority basis:** `PMS.yaml` → `00_source/PMS-STRATA_Structure.md` → canonical prose in `01_blocks/*` → binding controls in `05_minified/*` → formal operationalization in `07_model/*`  
**Primary inputs:** Chapters 2, 3, 5, 9, 11, 19, 23, 29, 30, 32, 42, 49, and 54; `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`; `04_reference/Transformation_Operation_Index.md`; `07_model/Operation_Registry.yaml`; `07_model/Transformation_Record.schema.json`

---

## B.1 Purpose, Status, and Formal Boundary

Appendix B provides a controlled notation for the analytical objects, coordinates, operation occurrences, chains, losses, claims, and adjudication states used throughout PMS-STRATA. It gathers notation that the Chapter Contracts explicitly migrate out of the main prose and aligns that notation with the current Minified Kernel and Formal Model.

Its function is translational:

```text
canonical prose
→ substantive meaning and governing distinctions

Appendix B
→ compact notation for inspection, comparison, records, and diagrams

Formal Model
→ machine-readable structural constraints
```

The appendix does not grant formulas greater authority than prose. It does not establish that PMS-STRATA is a complete mathematical theory, a category, a metric space, a scoring system, or a theorem-proving environment. A well-formed expression may still be empirically unsupported, semantically mistaken, normatively invalid, inadmissible, or non-capturing.

```text
well-formed notation
≠ valid transformation
≠ empirical truth
≠ causal proof
≠ semantic adequacy
≠ application authority
```

All notation in this appendix is therefore **relational, claim-bound, and defeasible**. It abbreviates declarations already required elsewhere. It does not create new objects, fields, operations, Output Classes, or admissibility gates.

### B.1.1 Controlling source pointers

- [Chapter 2 — Frame, Granularity, and Relative Level](../01_blocks/01_foundations.md#2-frame-granularity-and-relative-level) owns the analytical-coordinate distinctions.
- [Chapter 3 — Configuration, Event, Non-Event, Transition, Path, and Trajectory](../01_blocks/01_foundations.md#3-configuration-event-non-event-transition-path-and-trajectory) owns the foundational temporal-object chain.
- [Chapter 5 — Origin Type, Target Function, and Transformation Context](../01_blocks/01_foundations.md#5-origin-type-target-function-and-transformation-context) owns origin-type and target-function notation.
- [Chapter 9 — Temporal Order and Transition](../01_blocks/02_part_i_path.md#9-temporal-order-and-transition) owns extended temporal-order notation.
- [Chapter 11 — Trajectory](../01_blocks/02_part_i_path.md#11-trajectory) owns trajectory notation and historical-load burdens.
- [Chapter 19 — Granularity Change and the Logic of Decomposition](../01_blocks/03_part_ii_sub.md#19-granularity-change-and-the-logic-of-decomposition) owns decomposition-coordinate relations.
- [Chapter 23 — Decomposing Events, Non-Events, and Internal Temporal Structures](../01_blocks/03_part_ii_sub.md#23-decomposing-events-non-events-and-internal-temporal-structures) owns finer temporal reconstruction notation.
- [Chapter 29](../01_blocks/04_part_iii_retype.md#29-functional-projection-without-origin-type-replacement) and [Chapter 30](../01_blocks/04_part_iii_retype.md#30-project_as-signature-context-and-validity-scope) own functional-projection notation.
- [Chapter 42 — No Ontology of Strata](../01_blocks/05_part_iv_limits.md#42-no-ontology-of-strata) owns the prohibition on reading coordinates as ontological layers.
- [Chapter 49 — Source Limits and Calibration Limits](../01_blocks/05_part_iv_limits.md#chapter-49-source-limits-and-calibration-limits) owns source-precision and calibration limits on formal expression.
- [Chapter 54 — The Integrated STRATA Model](../01_blocks/05_part_iv_limits.md#chapter-54-the-integrated-strata-model) owns integrated chain notation.
- [Operation Signatures Minified](../05_minified/PMS_STRATA_Operation_Signatures_Minified.md) controls the compact signatures.
- [Operation Registry](../07_model/Operation_Registry.yaml) controls operation identity and chain constraints.
- [Transformation Record Schema](../07_model/Transformation_Record.schema.json) controls record structure.

---

## B.2 Notation Principles

### B.2.1 Semantic precedence

Where notation and prose appear to diverge, the controlling prose and Minified Kernel govern. The expression must be revised; the prose must not be silently reinterpreted to preserve a convenient formula.

```text
notation follows meaning
meaning does not follow notation automatically
```

### B.2.2 One symbol does not establish one ontology

A symbol identifies a role within a declared expression. It does not imply that the represented object has a permanent essence, universal identity, or context-free location.

```text
X in one record
≠ universal type X

ℓ in one declared relation
≠ fixed ontological layer
```

### B.2.3 Δ–Ψ are reserved

The Greek symbols `Δ` through `Ψ` used by PMS Base remain reserved for the canonical PMS operator grammar and its fixed dependencies. Appendix B does not reuse them as free variables, path labels, loss values, or generic mathematical operators.

```text
Δ–Ψ
→ PMS Base operator signs only

STRATA shorthand
→ Latin symbols, indexed variables, predicates, and record paths
```

This prevents formal convenience from renaming, reordering, decomposing, or extending the PMS operator grammar.

### B.2.4 Subscripts are relational, not hierarchical

The most common subscripts are:

| Subscript | Meaning |
| --- | --- |
| `s` | source-side declaration |
| `t` | target-side declaration |
| `c` | composite result or composite class |
| `o` | origin type |
| `i, j, k` | indexed objects, stages, or occurrences |
| `K` | reconstructed component set or finer structure |
| `local` | operation-local finding |

A source/target subscript indicates the role in one transformation occurrence. It does not indicate lower and higher truth, inferior and superior levels, or weaker and stronger authority.

### B.2.5 Equality signs are restricted

Use `=` only for declared identity within a notation, assignment, or exact field equivalence. Use `≠` for protected non-equivalence. Use arrows for transformation or relation direction. Do not use equality to assert empirical identity merely because two labels are the same.

```text
same label
≠ same reference object

same reference object
≠ unchanged function

same function label
≠ same constitutive source trace
```

Where reference continuity is warranted, this appendix uses the predicate:

```text
ReferenceContinuityPreserved(T)
```

rather than a universal identity equation.

### B.2.6 ASCII and Unicode forms

Unicode notation improves readability but must have a plain-text equivalent for YAML, JSON, terminals, and readers without full symbol support.

| Unicode form | Plain-text form |
| --- | --- |
| `ℓ_s` | `level_s` |
| `τ` | `temporal_scope` |
| `→` | `->` |
| `≠` | `!=` |
| `⟨X_1,…,X_n⟩` | `[X_1, ..., X_n]` with `ordered: true` |
| `∈` | `in` |
| `∅` | `none` or empty collection, where schema-valid |

The plain-text version must preserve the same declaration burden. ASCII transliteration is not permission to collapse relations or omit fields.

---

## B.3 Core Symbol Table

| Symbol | Controlled meaning | Boundary |
| --- | --- | --- |
| `X` | one identified analytical object | not a universal object type |
| `X_i` | indexed analytical object | index does not establish order unless declared |
| `S` | declared source collection or source sequence | collection ≠ ordered sequence |
| `T_o` | origin type of a source object | origin type ≠ target function |
| `K_c` | declared analytical class of a composite | class ≠ PMS primitive |
| `F_s` | source or coarser function under examination | source function may be revised or rejected |
| `F_t` | bounded contextual target function | target function ≠ new origin type |
| `Fr_s`, `Fr_t` | source and target analytical frames | frame ≠ PMS Frame operator type |
| `C_t` | declared target context | target context ≠ target frame |
| `C_x` | transformation context for one occurrence | context ≠ operation kind |
| `g_s`, `g_t` | source and target granularities | finer ≠ truer |
| `ℓ_s`, `ℓ_t` | source and target relative levels | relative level ≠ ontology |
| `τ`, `τ_s`, `τ_t` | temporal scope or bounded temporal relation | time scope ≠ path |
| `R` | declared ordering or constitutive relation structure | relation declaration ≠ causal proof |
| `R_K` | reconstructed relation structure among finer components | finer relation ≠ final constituent structure |
| `Q_d` | decomposition question | question ≠ result |
| `J` | operation justification | justification text ≠ passage of the operation |
| `L` | canonical five-field loss profile | loss ≠ automatic failure |
| `V` | validity scope | validity scope ≠ general truth domain |
| `T_i` | one transformation occurrence record | occurrence ≠ operation type |
| `O_i` | operation kind used in `T_i` | one of exactly three values |
| `H_{i,i+1}` | declared handoff between two occurrences | handoff ≠ fourth operation |
| `r_local(T_i)` | operation-local result | local result ≠ Output Class |
| `class(T_i)` | exactly one canonical Output Class for the tested claim | class ≠ rank |

### B.3.1 Source collection versus source sequence

A source collection without declared order may be written:

```text
S = {X_1, X_2, …, X_n}
```

An ordered source sequence may be written:

```text
S_ord = ⟨X_1, X_2, …, X_n⟩
```

The angle brackets mean that order is part of the declaration. They do not establish that the order is historically correct, causal, traversed, or sufficient for a path.

```text
ordered source sequence
≠ warranted path automatically
```

A partial order should be represented by an explicit relation set rather than by forcing a total sequence:

```text
R_τ = {X_1 ≺ X_3, X_2 ≺ X_3}
```

Here `≺` means only the declared supported precedence relation within the stated temporal scope. It does not mean causal determination.

---

## B.4 Object and Type Notation

### B.4.1 Typed analytical object

The compact source-side typing form is:

```text
X : T_o
```

Read:

> Object `X` is reconstructed under origin type `T_o` for the present claim.

This is a bounded analytical typing, not an assertion of permanent essence. Where `T_o` is a PMS operator-typed occurrence, the object remains an occurrence, not the abstract PMS operator type.

```text
X : Ω-occurrence
≠ X = Ω operator type
```

The exact operator sign must follow `PMS.yaml`; Appendix B does not define or alter operator meanings.

### B.4.2 Composite object

A composite produced by `COMPOSE` may be written:

```text
X_c : K_c
```

with formation relation:

```text
X_c = Form(S, R, J)
```

`Form` is shorthand for the declared selection, ordering, and constitutive-relation account in the record. It is not a new STRATA operation. The actual operation remains `COMPOSE`.

A safer expanded reading is:

```text
COMPOSE(S, R, J) → X_c : K_c
```

The symbol `=` in `X_c = Form(...)` is a record-level assignment, not a claim that the composite is a lossless sum of its constituents.

### B.4.3 Derived analytical object or function

A derived object or function may be marked:

```text
derived(X_c)
non_primitive(X_c)
```

or in prose/YAML through explicit `derived` and `non_primitive` declarations where the schema permits. The notation is a reminder of the authority boundary:

```text
derived analytical object
≠ new PMS primitive
```

### B.4.4 Reference identity and continuity

Reference identity is always claim-relative and source-bound. Use predicates rather than unqualified equality:

```text
ReferenceContinuityPreserved(T_i)
ReferenceContinuityFailed(T_i)
ReferenceContinuityUnderdetermined(T_i)
```

For a DECOMPOSE occurrence, the intended relation is:

```text
Ref(X_s) retained as reconstruction target
```

not:

```text
X_t = untouched X_s
```

A later finer reconstruction may distinguish structures not previously represented while still concern the same reference object. Conversely, nominal sameness may fail to preserve the reference.

---

## B.5 Coordinate Notation

### B.5.1 Coordinate bundle

For compact display, the declared analytical coordinates of an object may be grouped as:

```text
κ_s(X) = (Fr_s, g_s, ℓ_s, τ_s)
κ_t(Y) = (Fr_t, g_t, ℓ_t, τ_t)
```

`κ` is only a display shorthand for fields already required in prose and records. It is not a new schema field and does not turn the coordinates into a metric space.

Where source scope and claim scope are needed, use an expanded bundle:

```text
κ_s^+(X) = (Fr_s, g_s, ℓ_s, τ_s, source_scope_s, claim_scope_s)
```

The expansion does not imply that all coordinates can be numerically measured.

### B.5.2 Frame

Use `Fr_s` and `Fr_t` for declared analytical frames. A frame change may be displayed:

```text
Fr_s → Fr_t
```

This arrow alone does not classify an operation.

```text
changed frame
≠ PROJECT_AS automatically
≠ Φ occurrence automatically
```

The PMS Frame operator type must be referenced by its canonical PMS symbol/name, not by `Fr`.

### B.5.3 Granularity

Use `g_s` and `g_t` for source and target granularity. Because STRATA rejects a universal resolution hierarchy, do not use an unqualified global order such as `g_1 < g_2`.

A claim that `g_t` is finer than `g_s` must be relationally qualified:

```text
Finer(g_t, g_s | X, Q, C_x)
```

Read:

> `g_t` distinguishes more claim-relevant internal structure than `g_s` for source object `X`, question `Q`, and transformation context `C_x`.

This predicate does not mean:

```text
g_t more true than g_s
or
g_t more authoritative than g_s
```

A resolution-neutral relation may be represented:

```text
NoAdditionalPraxeologicalDifference(g_t, g_s | X, Q, C_x)
```

The canonical Output Class still requires the full audit and route selection.

### B.5.4 Relative level

Use `ℓ_s` and `ℓ_t` only with an explicit comparator and relation. The preferred expanded notation is:

```text
ℓ(X | Y, R_rel, C_x)
```

Read:

> the relative analytical position of `X` with respect to `Y` under declared relation `R_rel` in context `C_x`.

Examples of admissible relation declarations include part/whole, source/target, local/composite, occurrence/trajectory, or trajectory/wider-frame relation. No universal micro–meso–macro ordering follows.

```text
ℓ_t higher relative to one comparator
≠ ontologically higher
≠ greater authority
```

### B.5.5 Temporal scope

Use `τ` for a declared temporal scope:

```text
τ = [t_a, t_b]
```

when bounded dates or positions are supported. Open boundaries may be represented descriptively:

```text
τ = (open_before, t_b]
τ = [t_a, open_after)
```

These forms declare the scope boundary only. They do not establish complete chronology, event identity, path, trajectory, or dependence.

### B.5.6 Transformation and target context

Use `C_x` for transformation context and `C_t` for target context:

```text
C_x = context governing source–operation–target test
C_t = scene or relation within which F_t is claimed
```

They may overlap, but are not interchangeable:

```text
C_x ≠ C_t automatically
Fr_t ≠ C_t
```

---

## B.6 Temporal-Structure Notation

### B.6.1 Temporal position and precedence

Use `t_i` for a temporal position and `I_i` for an interval where exact dating is not required. Supported precedence may be written:

```text
t_1 ≺ t_2
X_1 ≺_τ X_2
```

`≺_τ` denotes supported temporal precedence within scope `τ`. It does not establish causality, necessity, or teleology.

For partial order:

```text
X_1 ≺_τ X_3
X_2 ≺_τ X_3
order(X_1, X_2) = underdetermined
```

The notation preserves uncertainty rather than inventing a total sequence.

### B.6.2 Configuration

A configuration at a bounded temporal position may be written:

```text
C_i = Config(X_1, …, X_n | Fr, g, ℓ, t_i)
```

`Config` is a descriptive constructor, not a STRATA operation. It abbreviates a source-supported configuration declaration. The selected elements do not form a complete world description.

### B.6.3 Event and non-event

Use:

```text
E_i = event-like object
NE_i = non-event structure
```

A non-event must retain its expectation relation:

```text
NE_i = NonRealization(E_expected | expectation_basis, realization_window, Fr)
```

This is shorthand for the prose burden. It does not infer a non-event from missing information.

```text
missing source
≠ NE_i
```

### B.6.4 Transition

A transition is not merely an arrow between states. The compact form is:

```text
Tn_i : C_i → C_j | R_i, τ_i, source_basis_i
```

where `Tn_i` is a transition object and `R_i` identifies the supported relation connecting the configurations. To avoid confusion with transformation occurrences `T_i`, this appendix uses `Tn_i` for temporal transitions and `T_i` for STRATA transformation records.

```text
C_i ≠ C_j
≠ sufficient transition claim
```

### B.6.5 Chronology, sequence, path, and trajectory

A chronology may be written:

```text
Chr = ⟨d_1, d_2, …, d_n⟩
```

A sequence:

```text
Seq = ⟨X_1, X_2, …, X_n⟩
```

A path requires actual traversal and warranted transitions:

```text
P = ⟨C_0, Tn_1, C_1, …, Tn_n, C_n⟩
```

with explicit selection and loss:

```text
P = Path(Seq, R_τ, selection, L, V)
```

A trajectory may be represented:

```text
Tr = Trajectory(P | historical_load, present_or_later_effect, V)
```

This is not a numerical trajectory equation. It marks the additional burden that historical carry-over matters to a present or later configuration.

Path dependence remains a separate property claim:

```text
PathDependent(Tr | alternatives, counterfactual_order_sensitivity, V)
```

Therefore:

```text
Chr ≠ Seq ≠ P ≠ Tr
Tr ≠ PathDependent(Tr) automatically
```

### B.6.6 Branches and historical alternatives

A branch structure may be written:

```text
B = (N, E, status, τ, source_basis)
```

where `N` are nodes and `E` are declared edges. Every alternative edge requires a status such as realized, blocked, aborted, deferred, rejected, unavailable, or open. The graph structure alone does not establish historical availability.

```text
edge rendered
≠ alternative historically available
```

---

## B.7 Shared Transformation-Occurrence Notation

### B.7.1 One occurrence

One STRATA transformation occurrence is represented:

```text
T_i = ⟨X_s, O_i, Y_t, C_x, J_i, L_i, V_i⟩
```

with:

```text
O_i ∈ {COMPOSE, DECOMPOSE, PROJECT_AS}
```

This tuple is a readable summary, not a replacement for the Shared Transformation Record. The full record additionally contains claim, admissibility, alternatives, Stop, governance, relations, and result fields.

The occurrence may also be written in directed form:

```text
T_i : X_s --O_i--> Y_t
```

The arrow means that a declared operation occurrence relates source and target. It does not mean the operation is admissible.

```text
T_i syntactically declared
≠ T_i substantively passed
```

### B.7.2 Operation kind

Use:

```text
kind(T_i) = COMPOSE
kind(T_i) = DECOMPOSE
kind(T_i) = PROJECT_AS
```

Exactly one kind must be selected per occurrence. A label such as `COMPOSE_PROJECT_AS` is prohibited as an operation kind. A chain must contain separate records.

### B.7.3 Claim notation

A tested claim may be summarized:

```text
Q_i = Claim(object, predicate, scope, ceiling)
```

The claim ceiling may be represented:

```text
Ceiling(Q_i) = bounded range of warranted assertion
```

This notation does not calculate the ceiling. It displays the declared limit. A narrower successor claim is a new claim:

```text
Q_{i+1} ⊂ Q_i
```

where `⊂` means narrower in declared scope, not logically proven set inclusion. The relation must be explained in prose or record fields.

### B.7.4 Justification

`J_i` records why the operation is proposed and what praxeological difference it is expected to make:

```text
J_i = (operation_reason, expected_praxeological_difference)
```

A justification is inspectable input, not a pass result.

### B.7.5 Validity scope

`V_i` bounds the result by object, context, time, relation, and transfer limits:

```text
V_i = ValidFor(object, context, τ, relation, exclusions)
```

No universal validity is implied by leaving a field broad. Overbroad scope triggers claim-ceiling pressure.

---

## B.8 Canonical Operation Signatures

The following signatures reproduce and explain the compact forms controlled by `PMS_STRATA_Operation_Signatures_Minified.md`. They are specifications of declaration burdens, not equations that mechanically produce a substantive result.

### B.8.1 COMPOSE

Canonical minimal signature:

```text
COMPOSE:
(S, Fr_s, g_s, ℓ_s, τ, R, J)
→
(X_c, K_c, Fr_t, g_t, ℓ_t, L, V)
```

Interpretation:

- `S` is a declared source set or ordered sequence;
- `R` contains ordering and constitutive relations;
- `J` states selection and formation justification;
- `X_c` is the new composite analytical object;
- `K_c` is its declared analytical class;
- `L` is the canonical loss profile;
- `V` bounds the result.

Occurrence form:

```text
T_i : S --COMPOSE[R, J]--> X_c : K_c
```

Compact burden form:

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

The plus signs denote conjunction of burdens, not arithmetic addition.

```text
COMPOSE(S)
≠ ΣX_i
≠ lossless union
≠ automatic target function
```

### B.8.2 DECOMPOSE

Canonical minimal signature:

```text
DECOMPOSE:
(X, T_o, F_s, Fr_s, g_s, ℓ_s, Q_d, J)
→
(K, R_K, F_s', Fr_t, g_t, ℓ_t, L, V)
```

Interpretation:

- `X` remains the identifiable source object under test;
- `T_o` is its source-side origin type;
- `F_s` is its current or coarser function under examination;
- `Q_d` is the decomposition question;
- `K` is the reconstructed finer component set;
- `R_K` contains relations and internal temporal structure;
- `F_s'` records the post-decomposition status of the source function;
- `g_t` must be declared finer relative to `g_s` for the stated question and context;
- `L` records preservation and unavailable structure.

Occurrence form:

```text
T_i : X --DECOMPOSE[Q_d, g_s→g_t]--> (K, R_K, F_s')
```

Compact burden form:

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
source-bounded Stop
```

The source-function status may be declared:

```text
F_s' ∈ {
  confirmed,
  refined,
  internally_differentiated,
  partially_preserved,
  rejected,
  underdetermined
}
```

This set is a controlled descriptive vocabulary from the Minified signature, not a new Output-Class enum.

```text
F_s' = rejected
≠ source object erased

finer reconstruction
≠ final constituent discovery
```

### B.8.3 PROJECT_AS

Canonical minimal signature:

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

Occurrence form:

```text
T_i : (X : T_o) --PROJECT_AS[C_t]--> F_t @ C_t [V]
```

Read:

> Object `X`, retaining origin type `T_o`, is tested as performing target function `F_t` within target context `C_t` and validity scope `V`.

Compact burden form:

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

Canonical non-equivalence:

```text
(X : T_o) PROJECT_AS F_t @ C_t
≠ X becomes F_t as origin type
```

### B.8.4 Operation-classification guard

A coordinate change is not by itself an operation signature:

```text
g_s → g_t
≠ DECOMPOSE automatically

Fr_s → Fr_t
≠ PROJECT_AS automatically

ℓ_s → ℓ_t
≠ operation identity
```

The operation kind follows the analytical movement and reference logic, not the visual direction of a coordinate arrow.

---

## B.9 Loss Notation

### B.9.1 Canonical loss profile

Every occurrence uses exactly five canonical loss fields:

```text
L_i = (
  preserved_i,
  compressed_i,
  excluded_i,
  uncertain_i,
  irrecoverable_i
)
```

Equivalent YAML form:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

No sixth canonical loss field may be added. Operation-specific language such as foregrounding, backgrounding, calibration pressure, or resolution drift must be mapped into the five canonical fields or retained as local diagnostic detail.

### B.9.2 Loss is not a scalar

Do not write:

```text
L_i = 0.7
```

unless a future separately authorized empirical calibration model exists. Current STRATA does not assign a universal numerical magnitude, weight, or rank to loss.

```text
more declared loss entries
≠ greater total loss automatically

less visible loss
≠ lossless transformation
```

### B.9.3 Loss inheritance in chains

For a chain, each occurrence retains its own loss profile:

```text
L_chain = ⟨L_1, L_2, …, L_n⟩
```

This sequence is not a sum. Inherited burdens may be referenced:

```text
Inherited(L_i → T_{i+1})
```

but the next record must state what is inherited, newly introduced, reclassified, or irrecoverable. Later operations do not overwrite earlier loss.

```text
L_{i+1}
≠ replacement for L_i
```

---

## B.10 Admissibility and Continuity Notation

### B.10.1 Core predicates

The following predicates name existing tests:

```text
PraxisPurchase(T_i, X, C_x)
TraceableLoad(T_i, X, C_x)
TypeIntegrity(T_i, X, C_x)
ReferenceContinuityPreserved(T_i)
FunctionalContinuityWarranted(T_i)
TemporalContinuityWarranted(T_i)
ContextualBoundedness(T_i, X, C_x)
CounterfactualSensitivity(T_i)
SourceCeilingRespected(T_i)
ClaimCeilingRespected(T_i)
```

These are qualitative audit predicates. They are not automatically evaluated by the existence of fields or by schema validation.

### B.10.2 Admissibility-band shorthand

A compact candidate statement may be written:

```text
BandCandidate(T_i)
iff
PraxisPurchase(T_i, X, C_x)
and
TraceableLoad(T_i, X, C_x)
```

The full admissibility decision requires all applicable tests, not only the two band edges. Therefore use:

```text
AdmissibleCandidate(T_i)
```

for a pre-audit notation and reserve the canonical Output Class for the completed adjudication.

The familiar compact form:

```text
Admissible(T, X, C)
iff
PraxisPurchase
and TraceableLoad
and TypeIntegrity
and ContextualBoundedness
```

is a governing minimum, not a four-variable scoring formula and not an exhaustive substitute for continuity, counterfactual, source, calibration, loss, alternatives, Stop, Non-Capture, and authority checks.

### B.10.3 Applicability states

For a conditional test `A_j`, use:

```text
applicability(A_j, T_i) ∈ {required, conditional, not_applicable}
```

`not_applicable` requires a condition and rationale. It does not mean passed.

```text
not_applicable
≠ true
≠ passed
```

### B.10.4 Counterfactual sensitivity

A projection or dependence claim may record:

```text
Sensitivity(T_i) ∈ {
  strongly_sensitive,
  partially_sensitive,
  weakly_sensitive,
  insensitive,
  underdetermined,
  untestable
}
```

These values describe the result of the declared test. They are not a numerical scale and do not establish an ordinal class ranking.

### B.10.5 Source precision and calibration

Formal precision must not exceed source precision. A compact guard is:

```text
Precision(claim_i) ≤ Precision(source_basis_i)
```

The `≤` sign is conceptual, not a calibrated numerical comparison. It means that the claim may not assert finer certainty or exactness than the source supports.

Where calibration remains open:

```text
Calibration(T_i) = underdetermined within declared range R_c
```

A bounded provisional result may still be available if the threshold uncertainty is explicit and claim scope is reduced accordingly.

---

## B.11 Result, Output Class, Stop, Failure, and Non-Capture

### B.11.1 Local result and canonical class

Use:

```text
r_local(T_i) = operation-specific finding
class(T_i) = one canonical Output Class
```

Examples:

```text
r_local(T_i) = bounded_path_reconstruction
class(T_i) = admissible_with_bounded_claim
```

or:

```text
r_local(T_i) = origin_type_replacement_detected
class(T_i) = failed_transformation
```

The class inventory remains:

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

No mathematical ordering is implied.

```text
class_a ≠ class_b
but not:
class_a > class_b
```

### B.11.2 Mandatory and optional Stop

Mandatory Stop may be written:

```text
Stop_mandatory(T_i | condition_j) = reached
```

Optional Stop:

```text
Stop_optional(T_i | sufficiency_condition) = reached
```

Only `mandatory_stop` is a canonical Output Class. Optional Stop is a governance result indicating that further analysis is unnecessary, not inadmissible.

### B.11.3 Failure preservation

A failed occurrence remains failed even if a later claim succeeds:

```text
class(T_i) = failed_transformation
and
class(T_{i+1}) = admissible_with_bounded_claim
```

does not entail:

```text
class(T_i) revised to admissible
```

The later operation is a new testable claim.

### B.11.4 Non-Capture

Non-Capture may be summarized:

```text
AdequateBoundedAttempts(Q_capture) = exhausted
and
NoAdequateRetainedForm(Q_capture)
and
NoUnsupportedIntegrationPermitted
→ class(T_i) = non_capture
```

This is a structured conclusion, not an inference from missing information or one failed attempt.

```text
missing information
≠ non_capture

failed transformation
≠ non_capture automatically
```

---

## B.12 Operation-Chain Notation

### B.12.1 Declared chain

A chain is an ordered sequence of separate transformation occurrences:

```text
χ = ⟨T_1, T_2, …, T_n⟩
```

or visually:

```text
T_1 → T_2 → … → T_n
```

Every `T_i` retains its own operation kind, source, target, claim, loss, admissibility, Stop condition, local result, and Output Class.

```text
χ
≠ compound operation type
≠ merged record
≠ averaged result
```

### B.12.2 Handoff

The handoff from `T_i` to `T_{i+1}` is written:

```text
H_{i,i+1} : target(T_i) → source(T_{i+1})
```

The handoff is a continuity claim, not an operation. Its burden may include reference, type, function, temporal, loss, and authority continuity.

```text
H_{i,i+1} passed
≠ T_{i+1} admissible automatically

T_i admissible
≠ H_{i,i+1} passed automatically
```

### B.12.3 Minimum chain families

The controlled minimum families may be displayed:

```text
COMPOSE → PROJECT_AS
COMPOSE → DECOMPOSE
DECOMPOSE → COMPOSE
DECOMPOSE → PROJECT_AS
PROJECT_AS → DECOMPOSE
COMPOSE → PROJECT_AS → DECOMPOSE
```

These are tested families, not an exhaustive list of all finite chains. Repetition remains possible, but each new occurrence requires a new record and new handoff.

### B.12.4 Chain-level summary

A chain summary may contain:

```text
chain_id(χ)
occurrences(χ)
handoffs(χ)
inherited_losses(χ)
preserved_failures(χ)
chain_claim(χ)
chain_result(χ)
```

`chain_result(χ)` must not erase or average the local classes. It is a bounded statement about the integrated chain claim only.

### B.12.5 Non-invertibility

Canonical non-invertibility statements remain:

```text
DECOMPOSE(COMPOSE(X)) ≠ X
COMPOSE(DECOMPOSE(X)) ≠ X
PROJECT_AS(X) ≠ X as a new origin type
```

These formulas deny presumed lossless reversal. They do not claim that reverse-direction operations are always prohibited. A reverse movement is a new occurrence:

```text
T_reverse = new transformation record
```

with new loss, evidence, and admissibility burdens.

---

## B.13 Record-Path Crosswalk

Appendix B notation maps to existing record paths. The notation does not add fields.

| Notation | Shared Transformation Record location |
| --- | --- |
| `T_i` | `/record_id` plus the full record object |
| `O_i` | `/operation/kind` or operation-specific discriminated payload |
| `X_s` | `/source/*` |
| `T_o` | source typing and operation-specific origin-type field |
| `Fr_s`, `g_s`, `ℓ_s`, `τ_s` | `/source/frame`, `/source/granularity`, `/source/relative_level`, `/source/temporal_scope` |
| `C_x` | `/operation/shared_occurrence/transformation_context` or current schema-equivalent path |
| `Y_t` | `/target/*` |
| `Fr_t`, `g_t`, `ℓ_t`, `τ_t` | target coordinate paths |
| `Q_i` | `/claim/*` |
| `L_i` | `/loss/preserved`, `/compressed`, `/excluded`, `/uncertain`, `/irrecoverable` |
| `H_{i,i+1}` | `/chain/*` and `/relations/*` as represented by the current schema |
| `r_local(T_i)` | `/result/local_result` or current schema-equivalent field |
| `class(T_i)` | `/result/selected_output_class` or current schema-equivalent field |
| Stop notation | `/governance/*`, `/result/*`, and applicable admissibility findings |

Where the schema uses a more specific field name than this table, the schema governs. Appendix C explains the current field groups in detail.

### B.13.1 JSON Pointer notation

Paths beginning with `/` are JSON Pointer-style references to record locations. They identify structure only.

```text
field path exists
≠ field substantively satisfied
```

A valid YAML or JSON document may still contain weak, false, or inadmissible content.

---

## B.14 Formula and Diagram Status

### B.14.1 Formula classes

STRATA uses at least four types of compact expression:

| Formula class | Function | Example |
| --- | --- | --- |
| signature | declares operation inputs and outputs | `COMPOSE: (...) → (...)` |
| non-equivalence | prevents category collapse | `origin type ≠ target function` |
| audit predicate | names a qualitative test | `TraceableLoad(T,X,C)` |
| compact burden form | lists conjunctive requirements | `PROJECT_AS = preserved source + context + function + trace` |

None is an empirical law. None proves completeness.

### B.14.2 Plus signs

In compact burden forms, `+` means that multiple duties must be jointly represented. It is not arithmetic, weighting, or compensation.

```text
TypeIntegrity + TraceableLoad
```

means both duties matter. It does not allow a high value on one to compensate for failure of the other.

### B.14.3 Arrows

An arrow may mean temporal precedence, operation direction, handoff, navigation, or a declared dependency. The surrounding label must disambiguate it.

```text
X_1 → X_2
```

alone is insufficient. Prefer:

```text
X_1 ≺_τ X_2                 temporal precedence
T_i : X --COMPOSE--> Y      operation occurrence
H_{i,i+1}: Y → Z            chain handoff
Appendix B → Appendix C     navigation or declared dependency
```

### B.14.4 Graph notation

For Reader diagrams:

```text
node
→ declared object, record, claim, context, or status

edge
→ declared relation, operation occurrence, handoff, or navigation link
```

The graph must type its edge. An untyped line does not establish a path, causal relation, historical alternative, dependency, or admissible transformation.

```text
graph edge
≠ evidence
≠ operation automatically
≠ historical availability automatically
```

### B.14.5 No category-theoretic claim

The presence of typed objects, arrows, and composition-like chains does not establish that PMS-STRATA has been defined as a mathematical category, operad, rewriting system, or complete transition algebra. Such formal research may be pursued later, but Appendix B does not supply identities, associativity laws, equivalence relations, closure theorems, or representation proofs.

---

## B.15 Worked Notation Examples

### B.15.1 COMPOSE path example

Source declaration:

```text
S_ord = ⟨C_0, Tn_1, C_1, Tn_2, C_2⟩
κ_s = (Fr_review, g_occurrence, ℓ_local, τ_0–2)
R = supported temporal and constitutive relations
```

Operation:

```text
T_1 : S_ord --COMPOSE[R, J_1]--> P_1 : path
```

Loss:

```text
L_1 = (
  preserved = order and review-relevant transitions,
  compressed = internal variation within C_1,
  excluded = non-constitutive side material,
  uncertain = mechanism of Tn_2,
  irrecoverable = unavailable contemporaneous detail
)
```

This notation does not yet establish that `P_1` is a trajectory or performs a higher-level frame-function.

### B.15.2 DECOMPOSE example

Source:

```text
X = H_0 : compressed handoff occurrence
F_s = bounded handoff function
```

Operation:

```text
T_2 : X --DECOMPOSE[Q_d, g_s→g_t]--> (K, R_K, F_s')
```

with:

```text
K = {access-blockage reconstruction, responsibility-transition reconstruction}
F_s' = internally_differentiated
```

If no single integrated reconstruction preserves both load-bearing relations without invention, the capture claim may route to `non_capture`; the partial reconstructions remain documented.

### B.15.3 PROJECT_AS example

Source:

```text
Q_47 : distributed access composite
T_o = relational composite
```

Projection:

```text
T_3 : (Q_47 : T_o)
      --PROJECT_AS[H_47]-->
      higher-level access function @ H_47 [V_47]
```

Counterfactual source variation:

```text
remove review-initiation asymmetry
→ target access function weakens or fails
```

Therefore the notation preserves constitutive source trace. The result still does not convert `Q_47` into a new operator type.

### B.15.4 Chain example

```text
χ_1 = ⟨T_1, T_3, T_4⟩
```

where:

```text
kind(T_1) = COMPOSE
kind(T_3) = PROJECT_AS
kind(T_4) = DECOMPOSE
```

Handoffs:

```text
H_{1,3}: X_c(T_1) → source(T_3)
H_{3,4}: origin_source(T_3) → source(T_4)
```

The second handoff must return to the origin-typed source object if the target function itself is not a decomposable source object. The chain does not imply:

```text
DECOMPOSE(PROJECT_AS(COMPOSE(S))) = S
```

### B.15.5 Calibration-open example

```text
threshold q* ∈ [q_2, q_4]
exact q* = underdetermined
```

The interval records a source-supported range. It does not license invented precision. A bounded claim may be provisionally admissible if it does not depend on choosing an exact point within the unresolved range.

---

## B.16 Prohibited Formalizations

The following forms are prohibited under the current corpus:

### B.16.1 Universal level ranking

```text
ℓ_1 < ℓ_2 < ℓ_3
```

when used as a context-free ontology or authority hierarchy.

### B.16.2 Numerical admissibility score

```text
score(T) = 0.82
```

when used to replace qualitative gate passage, collision adjudication, or Output-Class mapping.

### B.16.3 Compensatory weighting

```text
high PraxisPurchase
compensates for failed TypeIntegrity
```

No such compensation is permitted.

### B.16.4 Merged chain operator

```text
COMPOSE_DECOMPOSE_PROJECT_AS
```

as a fourth or compound operation kind.

### B.16.5 Lossless inverse notation

```text
COMPOSE^{-1} = DECOMPOSE
DECOMPOSE^{-1} = COMPOSE
```

No inverse relation is defined.

### B.16.6 Type replacement by projection

```text
X : T_o
PROJECT_AS F_t
therefore
X : F_t
```

This is exactly the origin-type replacement prohibited by RETYPE.

### B.16.7 Formal validity as substantive truth

```text
schema_valid(record) → claim_true
```

This implication is prohibited.

### B.16.8 Output-Class ranking

```text
admissible > partially_admissible > failed_transformation
```

The classes are routing outcomes, not a single quality ladder.

### B.16.9 Non-Capture from silence

```text
missing_information → non_capture
```

Non-Capture requires adequate bounded attempts and a persistent claim-relative capture limit.

---

## B.17 Notation Ownership and Downstream Handoffs

| Notation family | Primary owner | Appendix B role | Downstream handoff |
| --- | --- | --- | --- |
| object and type notation | Chapters 1 and 5 | compact typed-object syntax | Appendices C–F, H, I |
| coordinate notation | Chapter 2 | frame/granularity/level/scope shorthand | Appendices C–G, N |
| temporal order | Chapters 3 and 9 | precedence, interval, partial-order notation | Appendices H–J, M |
| path and trajectory | Chapters 10–12 | compact path/trajectory burden syntax | Appendices D, H, J |
| decomposition | Chapters 19, 20, 23 | finer-reconstruction signature | Appendices C and E, L |
| functional projection | Chapters 29–32 | origin/function/context notation | Appendices C and F, K |
| admissibility predicates | Chapters 41–53; Minified Band | named qualitative tests | Appendices G and N |
| loss notation | Chapters 6 and 48; Minified Kernel | canonical five-field tuple/map | Appendices C–G, N |
| chain notation | Chapters 47 and 54 | occurrence/handoff/loss-preservation syntax | Appendices C and N |
| record paths | Transformation Record Schema | human-readable crosswalk | Appendix C |
| case examples | `03_cases/*` | notation illustration only | Appendices H–M |
| graph notation | Reader boundary and Chapter 13 branch rules | typed-edge guard | Reader |

---

## B.18 Completion Boundary

Appendix B is complete for its assigned migration burden when:

- object, origin-type, and target-function symbols are controlled;
- frame, granularity, relative level, temporal scope, transformation context, and validity scope remain distinct;
- temporal order, partial order, sequence, path, trajectory, branch, and alternative notation preserve their burdens;
- the three operation signatures reproduce the Minified Kernel without modification;
- one operation occurrence remains distinct from its operation type, result, and chain;
- chains preserve separate records, handoffs, local results, losses, failures, Stops, and Non-Capture states;
- the loss profile contains exactly the five canonical fields and is not treated as a scalar;
- admissibility predicates remain qualitative and non-compensatory;
- formulas are clearly marked as specifications rather than empirical laws or completeness proofs;
- Δ–Ψ remain reserved for PMS Base;
- no category-theoretic, metric, numerical-scoring, inverse-operation, or representational-completeness claim is introduced;
- notation maps to existing record fields without creating new schema requirements;
- authority inheritance remains prohibited.

Appendix B satisfies those conditions at a substantive bounded provisional level.

```text
Appendix B complete
→ formal notation available for schemas, templates, audits, and Reader views

Appendix B complete
≠ mathematical completeness theorem
≠ numerical calibration model
≠ Reference Freeze
≠ Integrated Corpus Audit
≠ Model Finalization
≠ final release lock
```

