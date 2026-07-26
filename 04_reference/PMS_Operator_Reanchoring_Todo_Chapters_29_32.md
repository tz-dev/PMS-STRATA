# PMS-STRATA — PMS Operator Re-Anchoring To-do

## Chapters 29–32 — Review 1/2

**Status:** review completed; canonical re-anchoring patch executed in formal-model version `0.1.203`  
**Source of Truth:** `PMS-STRATA_Source_of_Truth_ZIP_251.zip`  
**Reviewed canonical block:** `01_blocks/04_part_iii_retype.md`  
**Primary controls:** `PMS.yaml`, `00_source/PMS-STRATA_Structure.md`, `05_minified/Chapter_Contracts.md`, `05_minified/Block_Contracts.md`, and the existing Reference Kernel  
**Next review:** Chapters 33–35

---

## 1. Review question

The review asks where Chapters 29–32 should make their PMS basis more visible without turning the prose into symbol display, repeating PATH or SUB, or changing the Δ–Ψ grammar.

The criterion is not operator-name frequency. A chapter does not become more PMS-specific merely by mentioning `Λ`, `Ω`, or `Θ` more often. The relevant question is:

> Where a RETYPE claim depends on a PMS-derived source object or on operator-like target work, does the prose show which concrete operator occurrences or operator relations carry the claim, how they enter the source object, and how their material variation would affect the proposed target function?

The current chapters already protect the negative boundary well:

```text
projected function
≠ PMS operator identity
≠ new primitive
≠ changed Δ–Ψ dependency
```

The principal gap is positive anchoring:

```text
which PMS occurrence-level structure
actually carries the source-to-target relation?
```

---

## 2. Conservative patch principle

The later patch should add **operator-occurrence anchoring**, not an operator quota.

### Add only where the operator relation is claim-bearing

A passage should name an operator or dependency only when at least one of the following is true:

- the source object was formed from operator-typed occurrences whose relation is constitutive for the present claim;
- the proposed target function explicitly invokes a bounded aspect of a PMS operator function;
- a counterfactual test changes or removes a concrete operator occurrence or relation;
- projection Loss compresses, excludes, leaves uncertain, or makes irrecoverable a claim-relevant operator relation;
- an operation chain must show how PMS occurrences become a derived source object before `PROJECT_AS`.

### Do not add

- decorative Δ–Ψ lists;
- universal formulas for every Trajectory, Frame-function, or Macro-Event;
- claims that every source object must instantiate all relevant operators;
- new operator dependencies or changed ordering;
- a new `operator_trace` schema field;
- new target-function enums, rules, audit stages, or Output Classes;
- repetition of PATH formation theory or SUB occurrence theory inside RETYPE;
- operator typing inferred from a desired target function.

### Use existing record positions

Operator anchoring should be carried through already existing fields and prose obligations:

```text
source_reference
source_basis
origin_type
constitutive_source_trace
counterfactual_sensitivity
loss.preserved / compressed / excluded / uncertain / irrecoverable
```

No schema expansion is required.

---

# 3. Chapter 29 — Functional Projection without Origin-Type Replacement

## Overall assessment

Chapter 29 is structurally strong and already protects PMS Base, operator identity, Δ–Ψ dependencies, and the distinction between target function and operator type. Sections 29.3 and 29.5 are especially clear.

The missing element is a positive source-side bridge. Sections 29.1, 29.6, and 29.7 describe source identity, load-bearing features, and Functional Continuity in general terms but do not yet require the analyst to show which concrete PMS occurrence relations carry a PMS-derived source object where that information is material.

## Necessary additions

### 29.1 — Purpose of RETYPE / source entry

Add one bounded question to the existing RETYPE question set:

> Where the source object is PMS-typed or PMS-derived, which concrete operator occurrences and relations are already warranted in the source record, and which of them are candidates for carrying the proposed target function?

Purpose:

- makes PMS anchoring part of operation entry;
- prevents the source object from becoming an abstract noun such as “history,” “trajectory,” or “structure” detached from its PMS formation;
- does not require re-derivation of the source object.

The wording must remain conditional: not every target claim requires every source operator to be repeated.

### 29.6 — Source Object Integrity

Add a short subsection or paragraph on **occurrence-level source integrity**:

- Source Object Integrity includes access to the operator-typed occurrences and relations that are constitutive for the source object where they matter to the projection.
- A derived object such as a Trajectory may reference its locked PATH Record rather than re-proving its operator composition.
- Operator symbols alone are insufficient; the occurrence, Frame, temporal relation, and source support must remain reconstructible.
- Operators not material to the present function claim need not be foregrounded.

Suggested compact distinction:

```text
PMS operator label retained
≠ occurrence-level source relation preserved
```

### 29.7 — Functional Continuity

Extend Functional Continuity with one explicit PMS test:

> If the proposed function is said to depend on a PMS-derived source structure, would material alteration of a load-bearing operator occurrence or relation require the target-function claim to change?

This should remain an occurrence-level sensitivity requirement, not a mutation of the abstract operator type.

Suggested distinction:

```text
change in concrete Λ-, Α-, Ω-, Θ-, Φ-, Χ-, Σ-, or Ψ-related source load
→ possible change in bounded target-function claim

change in abstract PMS operator definition
→ not a STRATA test
```

The list should be illustrative and limited to the operators actually warranted by the source record.

## Useful but non-essential addition

### 29.12–29.13 — one compact PMS-grounded operation-chain illustration

Add one short illustration, not a second theory derivation:

```text
warranted operator-typed occurrences and relations
→ COMPOSE
→ source Trajectory X

Trajectory X with retained source reference
→ PROJECT_AS
→ bounded target function in C
```

Where finer carrier inspection is required:

```text
Trajectory X
→ DECOMPOSE
→ finer occurrence-level carrier reconstruction

same retained source object or newly declared source claim
→ separate PROJECT_AS occurrence
```

The example should not prescribe one universal Δ–Ψ formula for Trajectory formation.

## Do not change

- 29.3 Origin-Type Preservation;
- 29.5 Target Function versus Operator Type;
- 29.11 `Φ` Recontextualization boundary;
- the existing result-axis, Stop, Non-Capture, and re-entry architecture.

These areas already perform their PMS-boundary function adequately.

---

# 4. Chapter 30 — PROJECT_AS: Signature, Context, and Validity Scope

## Overall assessment

Chapter 30 correctly functions as a generic operation chapter. It should not become a catalogue of Δ–Ψ examples. Its abstraction level is therefore not itself a defect.

The necessary repair is procedural: the complete `PROJECT_AS` procedure should make occurrence-level PMS anchoring an explicit conditional burden inside existing source, trace, sensitivity, Loss, and completion positions.

## Necessary additions

### 30.4 — Source Declaration

Add a prose requirement under `source_reference` and `source_basis`:

- where the source object is an operator-typed occurrence, identify the occurrence and its source Frame;
- where it is a composite or derived object, point to the source Record that preserves its operator-typed constituents or relations;
- where operator-level detail is unavailable or immaterial, state that limit rather than inventing a trace;
- a generic source label such as `documented_trajectory_X` is insufficient unless its linked source Record remains inspectable.

Do **not** add a new schema field. The requirement is satisfied through the existing source reference and basis.

Suggested completion question:

> Can the claim-relevant PMS occurrence structure be reconstructed from the declared source reference and source basis without inferring it from the proposed target function?

### 30.7 — Constitutive Source Trace

This is the most important Chapter-30 patch.

Add a conditional operator-anchoring clause:

- if the source claim rests on PMS operator-typed occurrences or relations, at least one load-bearing trace must identify the concrete occurrence-level relation that carries the proposed target difference;
- generic terms such as expectation, cost, recurrence, binding, or reframing should be connected to their warranted PMS occurrence typing where that typing is already established;
- the trace must preserve the difference between operator type, occurrence, composite, and derived object;
- an operator label without occurrence identity, relation, temporal placement, and source support remains label substitution at the source-trace level.

A conservative example may annotate the existing pressure candidates:

```text
repeated supported non-repair
→ Λ-occurrence trace within a declared expectation Frame

accumulated unequal exit cost
→ Ω-occurrence relation retained across the source Trajectory

persistent commitment continuity
→ Ψ-related occurrence trace retained within its source dependency context
```

These are examples of possible source typing, not automatic typings from ordinary-language words.

### 30.8 — Counterfactual Sensitivity

Add one explicit instruction:

> Where an operator occurrence or occurrence relation is declared load-bearing, the sensitivity test should vary that occurrence or relation rather than only changing the target label or narrative description.

The existing removal, reversal, order, threshold, substitution, and context tests remain sufficient. They only need operator-level interpretation where applicable.

Examples:

- replace a supported `Λ` non-repair sequence with supported timely repair;
- remove or equalize an `Ω` cost/exposure gradient;
- interrupt a retained `Ψ` commitment relation;
- alter the `Θ` ordering or persistence relation where temporal structure is claimed as load-bearing.

The abstract operator is never altered. Only the concrete source occurrence or relation is varied.

### 30.10 — Projection Visibility and Loss

Add a compact Loss instruction:

- if a claim-relevant operator occurrence or relation is foregrounded, compressed, excluded, uncertain, or irrecoverable under projection, record that condition inside the existing visibility declaration and five canonical Loss fields;
- projection may compress operator-level heterogeneity but may not imply that the remaining target function preserves the complete operator semantics or source dependency structure.

Suggested distinction:

```text
operator-occurrence relation compressed in projection
≠ operator type simplified or changed
```

### 30.13 — PROJECT_AS Record completion check

Add one prose-only completion question to the existing Record audit:

> Where PMS occurrence structure is material, do `source_reference`, `source_basis`, `constitutive_source_trace`, `counterfactual_sensitivity`, and `loss` together preserve an inspectable operator-occurrence route?

Again: no new field, Rule, or audit stage.

## Useful but non-essential addition

### 30.6 — Projection Justification

Add one sentence that analytical need is not established merely because a target function can be described in PMS vocabulary. The justification should show why the occurrence-level source structure produces a target difference that ordinary target description, `Φ`, or no-projection does not already capture.

## Do not change

- the minimal signature;
- the result vocabulary and mapping;
- sensitivity descriptors;
- the Shared Record schema;
- the ten canonical Output Classes;
- the distinction between visibility and canonical Loss.

---

# 5. Chapter 31 — Trajectory as Frame-Function

## Overall assessment

Chapter 31 is conceptually strong but needs the clearest positive PMS re-anchoring among Chapters 29–32. It already denies that a Trajectory becomes `□`; however, the positive relation between the source Trajectory’s operator load and the bounded target-side frame work remains mostly described through ordinary terms such as expectations, costs, Bindings, Non-Repair, roles, and residues.

The chapter should show why this is specifically a PMS-STRATA frame-function claim rather than a general historical-framing claim.

## Necessary additions

### 31.2 — Source Object

Require the source entry to retain a link to the PATH operator-load reconstruction where material.

The source declaration should not enumerate all Δ–Ψ operators. It should state which operator-typed occurrence relations are already established as candidate carriers, for example:

- supported `Λ` occurrences within declared expectation Frames;
- recurrent `Α` relations and their temporal persistence;
- `Ω` cost, exposure, capacity, or obligation gradients carried through the Trajectory;
- `Ψ` commitment or binding relations retained across time;
- relevant `Φ`, `Χ`, or `Σ` changes that interrupt, reinterpret, distance, or integrate the historical load.

These remain source-side candidates. Their presence does not establish the frame-function.

### 31.4 — Frame-Function

Add the positive semantic anchor currently missing from the otherwise strong `Trajectory ≠ □` boundary:

> A bounded frame-function should identify which limited aspect of the canonical PMS Frame function is being performed in the target context—such as relevance structuring, boundary conditioning, contextual constraint, or role-space organization—without importing the complete semantics, dependencies, or operator identity of `□`.

This is the central PMS-specific target-side clarification.

Suggested distinction:

```text
bounded performance of declared frame work
≠ complete □ semantics
≠ □ operator occurrence created by projection
```

The chapter’s existing target dimensions—legibility, credible interpretation, expectation, role reading, action corridors, cost, binding, and alternative visibility—should be related selectively to this bounded Frame work rather than treated as a free list.

### 31.5 — Historical Load

Add a small **PMS carrier anchoring** passage after the existing carrier table.

The passage should map only already warranted carrier families:

| Existing carrier language | Conservative PMS anchoring |
|---|---|
| sedimented expectations / repeated Non-Repair | source-supported `Λ` occurrences within declared Frames, retained through the Trajectory’s temporal structure |
| recurrent continuation pressure | source-supported `Α` occurrence relations whose persistence is part of the PATH record |
| accumulated asymmetric costs | source-supported `Ω` gradients retained across the Trajectory |
| persistent Bindings or Commitments | source-supported `Ψ` relations with their temporal and dependency context preserved |
| later reopening, reframing, distancing, or integration | target- or source-period `Φ`, `Χ`, or `Σ` occurrences that may weaken, redirect, or terminate the historical function |

The table must explicitly state:

- no carrier is universally required;
- ordinary-language resemblance does not establish operator typing;
- the source PATH Record owns the occurrence warrant;
- Chapter 31 only traces how the warranted load may perform target work.

### 31.7 — Multiple Frame Sources

Add one brief clarification:

- the projected historical frame-function may coexist or compete with actual target-side Frame occurrences, institutional Frames, present rules, and `Φ` recontextualizations;
- it does not compete with the abstract `□` operator type;
- comparison concerns concrete source contributions inside the target configuration.

This prevents “multiple frames” from becoming a comparison of labels rather than occurrences.

### 31.9 — Counterfactual Frame Test

Annotate the already well-designed carrier variations at occurrence level:

- timely repair versus repeated non-repair pressures the claimed `Λ` carrier;
- equalized exit cost pressures the claimed `Ω` carrier;
- interrupted commitment continuity pressures the claimed `Ψ` carrier;
- a material `Φ` recontextualization may change whether earlier load continues to frame the target scene;
- change in duration, order, or persistence pressures the relevant `Θ` relation.

Add the explicit protection:

```text
occurrence-level variation
≠ abstract operator revision
```

No new counterfactual route is needed.

## Useful but non-essential addition

### 31.3 — Target Context

The current present-condition list is already strong. It may be tightened by identifying current target-side `□` occurrences and `Φ` changes as rival or co-active frame sources where the evidence warrants them. A larger Δ–Ψ inventory should not be added.

## Do not change

- the independent PATH source-selection rule;
- the same-source `Y/Z` contrast;
- non-determinism and causal limits;
- the qualitative, non-scored relative-load rule;
- rhetorical-history failure;
- background relevance and no-projection as positive possibilities.

---

# 6. Chapter 32 — Trajectory as Macro-Event

## Overall assessment

Chapter 32 correctly treats Macro-Event as a contextual target function rather than a PMS operator. Therefore the patch must **not** attempt to invent an operator equivalent for Macro-Event.

PMS re-anchoring belongs instead in three places:

1. the operator-typed structure of the source Trajectory and its phases;
2. the PMS-reconstructible difference between target configurations before and after the projected unit;
3. the operator relations that would be lost by punctualization or arbitrary periodization.

## Necessary additions

### 32.1 — Basic Claim and source entry

Add one source-side requirement:

> The linked PATH Record must preserve, where material, which operator-typed occurrences and relations constitute the Trajectory’s phase structure and historical load; Chapter 32 references that warrant but does not reconstruct it from the desired Macro-Event function.

The target function remains Macro-Event. No PMS operator identity is assigned to it.

### 32.4 — Boundary Selection

Add a criterion that start, end, phases, and turning points should be supported by changes in the reconstructed praxis structure rather than by calendar convenience or later naming alone.

Possible occurrence-level boundary evidence may include:

- changed `□` relevance or role-space organization;
- emergence, accumulation, interruption, or disappearance of supported `Λ`, `Α`, `Ω`, or `Ψ` load;
- a material `Φ` recontextualization;
- changed `Θ` ordering, persistence, or trajectory relation.

No fixed operator checklist is required. The relevant operators depend on the source record.

Suggested distinction:

```text
operator-relevant configuration change may support a phase boundary
≠ operator symbol automatically fixes a historical boundary
```

### 32.5 — Internal Duration

Add a short positive anchor to `Θ`:

- internal duration, order, delay, persistence, and phase relation are PMS-temporal structures carried through `Θ`-typed occurrence relations in the source reconstruction where warranted;
- treating the Trajectory as one target-level unit must preserve access to those relations;
- the Trajectory does not become `Θ`, and Macro-Event is not a temporal operator.

This should be one compact paragraph, not a new Temporality theory section.

### 32.6 — Internal Heterogeneity and phase load

Make explicit that heterogeneity can consist of different operator-typed occurrence loads across phases, roles, and subpaths.

Examples may include:

- one phase dominated by structured `Λ` non-occurrence;
- another phase carrying stronger `Ω` exposure or obligation gradients;
- later `Ψ` binding or release;
- recurrent `Α` stabilization interrupted by `Φ`, `Χ`, or `Σ` changes.

The exact combination remains source-specific. The chapter must not assign operator dominance by impression or turn a phase profile into a new type.

Add a Loss instruction: if target-level compression obscures a claim-relevant occurrence relation, place it under the existing five-part Loss ledger.

### 32.7 — Event Function

Require the proposed wider-path transition difference to be stated through PMS-reconstructible praxis changes rather than generic historical importance.

A Macro-Event candidate should identify which target relation differs across `B_pre` and `B_post`, for example:

- Frame or role-space organization;
- expectation and structured Non-Event conditions;
- action-corridor availability;
- `Ω` exposure, capacity, cost, or obligation gradients;
- `Ψ` commitments or exit conditions;
- temporal reachability and persistence.

This remains a target-side functional difference, not proof that the Trajectory caused every change.

### 32.8 — Punctualization Error

Extend the current error description so that punctualization explicitly includes:

- erasure of source `Θ` ordering and duration;
- conversion of repeated or distributed `Λ`, `Ω`, `Α`, or `Ψ` occurrence load into one undifferentiated event marker;
- loss of operator-relevant phase variation that is material to the target claim.

The patch should not say that Event is a PMS operator.

### 32.10 — Counterfactual Macro-Event Test

Add occurrence-level examples to the existing phase-variation route:

- remove or reverse a phase whose `Λ`, `Ω`, `Α`, or `Ψ` load is claimed to carry the transition;
- alter `Θ` order, delay, persistence, or phase duration where those relations are constitutive;
- test whether a major `Φ` recontextualization changes the defensible source boundary or target transition function.

The operator typing must come from the source record, not from the counterfactual design.

## Useful but non-essential addition

### 32.9 — Macro-Event versus COMPOSE

Add one compact chain illustration:

```text
operator-typed configurations, events, Non-Events, and relations
→ COMPOSE
→ origin-typed Trajectory M

Trajectory M
→ PROJECT_AS
→ bounded Macro-Event function in wider Path B
```

This is useful for visibility but should remain shorter than the existing operation-separation discussion.

## Do not change

- Macro-Event as an open contextual target function;
- the anti-punctualization architecture;
- rival periodization and alternative-source tests;
- the separate `COMPOSE` and `PROJECT_AS` Records;
- descriptive compression and no-projection as legitimate outcomes;
- causal, person, legitimacy, recommendation, sanction, and authority prohibitions.

---

# 7. Consolidated patch order after Review 2/2

No chapter should be patched before Chapters 33–35 have been reviewed, because Chapter 33 and Chapter 35 will determine how recurrence, `Α`, weighting, and modulation should be anchored consistently across the whole RETYPE family set.

After Review 2/2, use this order:

1. **Shared contract/minified clause** — add one concise conditional PMS occurrence-anchoring requirement once.
2. **Chapter 30** — establish the generic procedure using existing fields.
3. **Chapter 29** — align conceptual source integrity and Functional Continuity with that procedure.
4. **Chapter 31** — add the positive `□`-function subset and operator-carrier trace.
5. **Chapter 32** — add source-phase, temporal, transition, and punctualization anchors.
6. **Chapters 33–35** — apply the same rule to recurrent form, higher-level composites, weighting, and modulation.
7. **Reference synchronization** — Glossary, Operator Index, Transformation Operation Index, Non-Equivalence Index, Claim Type Table, Admissibility Band Reference, Cross-Reference Map, Evidence Map, Audit Checklist, Reader Pathways.
8. **Formal-model synchronization only where already mirrored** — no new fields or routing logic unless an existing declaration must be clarified.
9. **Full repository audit** — YAML/JSON, schemas, records, smoke suite, inventories, links, anchors, fingerprints, ZIP CRC, and byte roundtrip.

---

# 8. Acceptance criteria for the later patch

The re-anchoring patch passes only if all of the following are true:

- every added operator reference is occurrence-level, source-supported, and claim-relevant;
- no chapter implies that all Trajectories instantiate one fixed operator combination;
- no projected target function becomes an operator type or occurrence automatically;
- no Δ–Ψ identity, order, or dependency changes;
- no fourth STRATA operation appears;
- no new schema field, Output Class, Rule, audit stage, score, or automatic selector appears;
- Chapters 29–30 remain generic and reusable;
- Chapters 31–32 become more specifically PMS-grounded without repeating PATH or SUB;
- operator-level counterfactual variation changes concrete occurrences or relations, never abstract operators;
- operator-related Loss is recorded through the existing five canonical fields;
- the prose remains readable without requiring constant symbol decoding;
- the resulting claims would no longer remain nearly unchanged if PMS were replaced by an arbitrary structural vocabulary.

---

# 9. Review result

The Chapters 29–32 prose does **not** require reconstruction from scratch.

```text
conceptual and operational derivation retained
+ targeted occurrence-level PMS anchoring required
→ conservative patch feasible
```

Relative patch need:

```text
Chapter 29: moderate, mainly source-integrity and continuity bridge
Chapter 30: moderate, procedural anchoring through existing fields
Chapter 31: substantial but local, positive Frame-function and carrier trace
Chapter 32: substantial but local, source phases, Θ, transition difference, and punctualization
```

No canonical prose, Contract, Minified Kernel, YAML, JSON, schema, Record, Smoke fixture, or Output Class is changed by this review artifact.

The next controlled step is:

```text
PMS Operator Re-Anchoring Review 2/2
→ Chapters 33–35
→ consolidated patch plan
→ only then canonical patch execution
```

## Execution record

The conservative re-anchoring patch has been applied to Chapters 29–35, the RETYPE Block and Chapter Contracts, the relevant Minified controls, the Reference Kernel, and the non-routing formal-model mirror.

The execution preserved:

- exactly three STRATA operations;
- the unchanged Δ–Ψ operator grammar and dependencies;
- the existing Shared Transformation Record fields;
- exactly five canonical Loss fields;
- exactly ten canonical Output Classes;
- exactly sixteen Rules and twelve integrated audit stages;
- all prior Chapter-40 and Part-III bounded-lock dispositions;
- the absence of new case, test, or smoke YAML production.

The patch adds occurrence-level source anchoring only where concrete PMS relations materially carry a RETYPE claim. It does not impose a full operator inventory or reopen the substantive case-adjudication gap.

**Next controlled production step:** Chapter 41 WP1 under the existing artifact-complete RETYPE `mandatory_stop`.
