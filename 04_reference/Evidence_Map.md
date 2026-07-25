# PMS-STRATA — Evidence Map

**Status:** Reference Kernel v0 scaffold v0.3.50; Chapter-20-WP4-lock-synchronized  
**Repository role:** `04_reference/*` — source, support, gap, rival, and external-warrant routing; not an independent theory source  
**Current control provenance:** `00_source/PMS-STRATA_Structure.md`, `05_minified/*`, the seven substantive Reference Kernel files, the post-smoke-synchronized `04_reference/Cross_Reference_Map.md`, the current peer scaffolds `04_reference/Audit_Checklist.md` and `04_reference/Reader_Pathways.md`, repository `README.md`, the seven populated Core artifacts in `07_model/`, the eight populated records and suite control in `07_model/examples/`, and `PMS.yaml` for PMS Base  
**Substantive evidence status:** Formal Model Core and Smoke Suite are internally validated as formal artifacts; Foundations Chapters 0–8, PATH Chapters 9–17, and SUB Chapters 18–20 are provisionally locked methodological prose; Chapter 21 WP1–WP2 §§21.1–21.9 are canonical and locally `admissible_but_provisional`; Chapter 21 WP3–WP4, later blocks, substantive cases, calibration sets, and external evidence remain pending.

---

## 1. Role, Status, and Authority

This map records what kind of source relation would be needed to support, limit, contradict, rival, or leave open a tested STRATA claim. It routes current control provenance, realized formal-model and smoke-test handoffs, and future case, calibration, and external-warrant evidence without treating navigation, citation, formal consistency, or repository volume as substantive proof.

```text
authority source
≠
current control source
≠
transformation source basis
≠
individual evidence item
≠
Constitutive Source Trace
≠
support status
≠
canonical output class
```

This map shall:
- distinguish project authority from claim evidence;
- register source types and claim-relative evidence roles;
- record supporting, limiting, contradictory, rival, missing, inaccessible, and external-warrant conditions;
- route operation- and claim-family evidence burdens;
- preserve Source Ceiling, Counterfactual Sensitivity, calibration, loss, Stop, and Non-Capture handoffs;
- distinguish realized Core and smoke-suite conformance from pending substantive case, calibration, and external evidence explicitly.

This map shall not:
- decide whether a source is truthful or a reconstruction is empirically correct;
- create an evidence score, universal hierarchy, confidence metric, or eleventh output class;
- turn citation count into TraceableLoad;
- treat missing documentation as a PMS Non-Event;
- infer causality, semantic validity, normative validity, person type, diagnosis, legitimacy, sanction, or application authority;
- redefine, extend, or semantically close formal field names independently of their realized Formal Model v0 owners.

```text
Evidence Map
≠
evidence of truth
≠
bibliography
≠
citation index
≠
source ranking
```

---

## 2. Evidence Semantics and Non-Goals

Evidence is claim-relative. A source may directly support one relation, indirectly support another, limit a stronger claim, or remain irrelevant to a third. No source type possesses automatic priority across all claims.

```text
same source
≠
same evidential force for every claim
```

The map distinguishes:

- **authority provenance:** why an artifact controls PMS or STRATA production;
- **source basis:** the declared material set on which a tested claim relies;
- **evidence item:** one document, record, observation, reconstructed relation, or other item inside that basis;
- **evidence role:** how an item bears on the tested claim;
- **support mode:** whether support is direct, indirect, reconstructed, or mixed;
- **support status:** the present condition of support for the claim;
- **evidence availability:** whether relevant material is available, partial, missing, unavailable, or inaccessible;
- **warrant routing:** whether STRATA-internal support is assessable or external warrant is required;
- **record-level status declaration:** the architecture that preserves support, resolution, disposition, and capture information without flattening them;
- **source trace:** the explicit mapping from source features to the transformation result;
- **external warrant:** evidence or method needed beyond STRATA's self-sufficient authority.

These are conceptual routing dimensions. Reference prose controls their semantic distinctions and permitted meanings. The realized Formal Model v0 Core mirrors selected dimensions through machine spellings, nesting, validation, and schema constraints; it does not create, revise, or close their semantics independently.

---

## 3. Authority Provenance versus Claim Evidence

| Source layer | Project role | Evidence boundary |
| --- | --- | --- |
| `PMS.yaml` | external governing authority for PMS Base and Δ–Ψ | not empirical evidence for a concrete STRATA transformation |
| `00_source/PMS-STRATA_Structure.md` | architecture and chapter blueprint | not evidence that future chapter claims are true |
| locked `01_blocks/*` | future canonical corpus prose | canonical prose still requires case, source, and claim discipline |
| `05_minified/*` | binding control artifacts | control consistency is not substantive evidence |
| `04_reference/*` | terminology, registry, routing, and audit preparation | reference density is not truth support |
| seven populated Core artifacts in `07_model/` | realized formal operationalization, integration, and schema control | formal consistency and machine-valid structure do not prove semantic or empirical validity |
| `07_model/examples/*` | current smoke-record and suite-documentation layer | eight populated schema-valid records plus suite README provide internal record-level and cross-record conformance evidence only |
| `03_cases/*` | future positive, negative, confusion, stop, and non-capture tests | cases test rules; they do not define theory |
| external domain sources | possible empirical, causal, semantic, normative, predictive, or policy warrant | do not inherit STRATA admissibility automatically |


```text
authority source
≠
empirical evidence
```

```text
current control source
≠
claim support
```

An artifact can be authoritative for terminology or production sequencing while providing no direct support for a concrete historical, functional, or causal claim.

`04_reference/Cross_Reference_Map.md` routes to this Evidence Map, and this Evidence Map routes back to established definition and control sites. That mutual navigation does not create a circular definition or authority inheritance.

```text
mutual routing
≠
circular definition
≠
authority inheritance
```

---

## 4. Evidence Assessment Object

Evidence is assessed for a delimited record, not globally for an object or source collection.

```text
operation occurrence T
+
reference or source object X
+
transformation context C
+
tested claim Q
+
source basis S
+
evidence role R
```

A compact evidence question is:

```text
Which declared sources support, limit, contradict,
or rival which constitutive part of Q,
within C, and with what Source Ceiling?
```

The same source basis may support an admissible sequence claim, leave a trajectory claim provisional, and fail to support path dependence. Evidence assessment must therefore remain claim-, scope-, and operation-specific.

```text
source collection
≠
globally evidential object
```

---

## 5. Source Basis and Evidence Roles

### 5.1 Source basis

The source basis is the declared set of documents, records, observations, reconstructed relations, existing PMS objects, or other materials on which a tested claim relies. It must be bounded by time, frame, access, selection, and known gaps where applicable.

```text
source basis
≠
Constitutive Source Trace
```

```text
source basis
≠
Source Ceiling
```

### 5.2 Evidence role matrix

The roles below are controlled pre-Block routing categories, not a closed formal enum. Cases may reveal a needed local wording, but any genuinely new system-wide role requires Reference Kernel revision before formalization.

| Evidence role | Claim relation | Minimum declaration | Primary limitation |
| --- | --- | --- | --- |
| direct support | explicitly records the asserted occurrence, order, relation, or feature | identify item, reference, time, and supported claim component | does not automatically support stronger formation or causal claims |
| indirect support | supports an inference through a declared relation | state inference rule and alternatives | must not be presented as direct documentation |
| reconstructive support | supports a bounded reconstruction from multiple traces | state assembly logic, uncertainty, and loss | plausibility alone is insufficient |
| temporal-order support | supports sequence, duration, transition, or timing | state time basis and conflicts | order does not establish path or trajectory |
| relation support | supports a constitutive or modulating relation | state relation and counterstructure | co-occurrence is not automatically constitutive |
| counterfactual-load support | supports sensitivity to a source-feature change | name changed feature, expected result change, and basis | does not prove actual causality |
| calibration comparator | discriminates thresholds or neighboring cases | state comparison class and decision boundary | formal exactness is not calibration |
| limiting evidence | bounds scope, detail, time, function, or generality | state affected claim dimension | limitation is not automatic failure |
| contradictory evidence | conflicts with the tested claim or a constitutive subclaim | preserve conflict and response | must not be hidden by re-description |
| rival evidence | supports an alternative COMPOSE, DECOMPOSE, PROJECT_AS, or No Transformation | state rival claim and comparable burden | rival existence is not rival superiority |
| gap indicator | records missing, inaccessible, or unresolvable material | state what is missing and why it matters | gap is not a Non-Event or falsehood |
| external-warrant evidence | belongs to a method beyond STRATA authority | state external method and governance | does not inherit validation from STRATA |
---

## 6. Source Classification Axes

Source form, reconstruction mode, case role, evidence availability, and external-warrant location are separate routing axes. None is a universal quality rank or source ontology.

```text
source type
≠
evidence role
≠
evidence availability
```

### 6.1 Source form and provenance

| Source form or provenance | Can directly support | Usually still requires reconstruction for | Common misuse |
| --- | --- | --- | --- |
| direct documentation | recorded occurrence, statement, rule, or decision within declared provenance | latent mechanism, unrecorded alternative, or broader function | document presence treated as complete structural proof |
| temporally ordered records | sequence, duration, interval, and transition timing | constitutive path relation or sedimentation without further support | chronology treated as path |
| institutional materials | formal roles, procedures, commitments, expectations, and recorded non-occurrences | actual practice or causal effect without external evidence | formal rule treated as enacted behavior |
| observable configurations | co-present roles, constraints, asymmetries, and action corridors | historical formation or hidden internal process | snapshot treated as trajectory |
| existing PMS objects | typed structural source objects within PMS | empirical truth about a domain | formal object treated as external evidence |
| documented non-occurrence | bounded absence relative to a declared expectation and frame | any unknown or undocumented event | missing information treated as Λ |

### 6.2 Reconstruction mode

| Reconstruction mode | Controlled use | Minimum disclosure | Boundary |
| --- | --- | --- | --- |
| reconstructed transition | bounded inferred transition assembled from distributed traces | source mapping, inference rule, alternatives, uncertainty, and loss | not direct occurrence evidence |
| analyst reconstruction | explicit interpretive model with a declared source trace | analyst contribution, source dependence, rival model, and uncertainty | analyst fluency is not evidence |

### 6.3 Case evidence role

| Case role | Controlled contribution | Boundary |
| --- | --- | --- |
| comparison case | discriminates similarity, difference, or threshold across records | one example is not calibration |
| countercase | pressures a rule, threshold, or claim | does not automatically refute the whole method |

### 6.4 Evidence availability is not a source type

Inaccessible, withheld, missing, or unavailable material describes the condition of access to relevant evidence. It does not name a source form and does not supply positive support.

### 6.5 External-warrant location is not a source type

External domain evidence names the location of an additional empirical, causal, semantic, normative, predictive, policy, clinical, or other domain-specific warrant. It does not become STRATA-internal evidence merely because a transformation record routes to it.

```text
external domain evidence
≠
STRATA-internal support automatically
```

---

## 7. Support Status, Evidence Availability, and Warrant Routing

Support mode, support status, evidence availability, and warrant routing must be declared separately. The tables below control their pre-Block meanings. Current machine spellings and constraints are realized in `07_model/Transformation_Record.schema.json`; those spellings do not replace the semantic owners in Reference prose.

```text
support mode
≠
support status
≠
evidence availability
≠
external-warrant requirement
```

### 7.1 Support status

| Support status | Meaning | Governance boundary |
| --- | --- | --- |
| supported | current sources and tests adequately carry the delimited claim | not empirical truth or automatic `admissible` |
| provisional | the claim remains usable while material source, calibration, rival, or counterfactual limits remain | may interact with `admissible_but_provisional` but does not force it mechanically |
| contested | material contradictory evidence, objection, or rival remains active | conflict must be preserved; not automatic failure |
| underdetermined | available grounds do not discriminate among materially different claims | does not automatically establish Non-Capture |
| unsupported | current source basis does not carry the declared relation, reach, precision, generality, functional load, or dependence strength | may require reduction, failure, stop, or external warrant after a separate governance audit |

```text
unsupported claim
≠
failed claim automatically
```

### 7.2 Evidence availability

| Availability condition | Meaning | Does not imply automatically |
| --- | --- | --- |
| available | relevant material is accessible and assessable for the declared record | support sufficiency |
| partially available | only part of the relevant material is accessible or located | one fixed support status |
| missing | relevant material is absent from the located source basis | falsehood or supported Non-Event |
| unavailable | relevant material is known or expected but cannot presently be obtained or tested | confirmation or refutation |
| inaccessible | access is withheld, prohibited, technically blocked, or otherwise unavailable to the assessment | positive support |

### 7.3 Warrant routing

| Warrant route | Meaning | Boundary |
| --- | --- | --- |
| STRATA-internal support assessable | the structural claim can be evaluated within declared STRATA sources and methods | does not establish external empirical, causal, semantic, or normative validity |
| external warrant required | STRATA can structure the claim but cannot establish it within its own authority | not a support status and no authority inheritance |

### 7.4 Support downgrade is not claim reduction

```text
supported
→ provisional
```

This is an illustrative support change, not a universal hierarchy. Claim reduction changes the asserted relation, reach, precision, generality, functional scope, or dependence strength.

```text
support downgrade
≠
claim reduction
```

### 7.5 Current formal evidence handoff

The current record schema exposes the following machine locations. These pointers register implementation ownership; they do not transfer semantic authority away from the Reference Kernel.

| Evidence axis | Current record location | Formal boundary |
| --- | --- | --- |
| source basis | `/source/source_basis` | bounded source-item array; not proof of sufficiency |
| support mode | `/source/source_basis/*/support_mode` | closed machine spelling for `direct`, `indirect`, `reconstructed`, or `mixed` |
| evidence role | `/source/source_basis/*/evidence_role` | open controlled term; no new closed evidence ontology |
| item-level evidence availability | `/source/source_basis/*/evidence_availability` | closed availability spelling; not support status |
| warrant route | `/source/source_basis/*/warrant_route` | STRATA-internal assessability or external-warrant requirement |
| external-warrant declaration | `/governance/external_warrant` | domain warrant routing without authority inheritance |
| support status | `/result/status_declaration/support_status` | separate from output class and claim disposition |
| evidence-availability summary | `/result/status_declaration/evidence_availability_summary` | record-level summary; not item-level replacement |
| resolution result | `/result/status_declaration/resolution_test_result` | separate from support and capture axes |
| capture statement | `/result/status_declaration/capture_statement` | preserves capture, failure, and Non-Capture distinctions |
| current claim disposition | `/result/routing/current_claim_disposition` | authoritative location; referenced by the fixed pointer in status declaration |

```text
machine location
≠
semantic ownership
≠
substantive warrant
```

---

## 8. Direct, Indirect, and Reconstructed Support

Support mode states how source material bears on a claim. It does not determine support status and does not form a universal hierarchy of epistemic worth.

| Support mode | Core relation | Minimum disclosure | No-authority rule |
| --- | --- | --- | --- |
| direct | source explicitly records the claimed occurrence or relation | provenance, scope, and reference identity | broader structural implications still require argument |
| indirect | source supports a claim through one declared inference | inference path and possible counterinference | must remain marked as indirect |
| reconstructed | multiple sources are assembled into a bounded structural model | selection, formation rule, uncertainty, alternatives, and loss | model fit is not direct observation |
| mixed | different claim components have different support modes | component-level mapping | cannot be summarized as uniformly direct |

```text
support mode
≠
support status
```

```text
direct evidence
≠
stronger claim automatically
```

```text
indirect evidence
≠
weak evidence automatically
```

Relevance depends on the tested relation. A directly recorded statement may be weak evidence for actual practice, while a well-traced distributed record may strongly support a bounded transition reconstruction.

---

## 9. Supporting, Limiting, Contradictory, and Rival Evidence

| Evidence direction | Primary effect | Required handling |
| --- | --- | --- |
| supporting | carries the tested claim or a constitutive subclaim | retain source-result mapping |
| limiting | narrows claim scope, precision, period, function, or generality | revise ceiling or claim without hiding support |
| contradictory | conflicts with the claim or declared relation | record contradiction and its effect |
| rival | supports a competing reconstruction or no-transformation alternative | compare burdens symmetrically |


A single item may play more than one role for different claims. Role assignment must therefore include the affected claim component.

```text
contradictory evidence
≠
automatic whole-record failure
```

```text
rival evidence
≠
proof of rival superiority
```

---

## 10. Missing Information and Non-Event

Missing information, inaccessible records, unknown events, and PMS Λ Non-Events must remain distinct.

```text
no record
≠
recorded non-occurrence
```

```text
missing information
≠
Λ Non-Event
```

A supported non-event claim requires at least:

- a declared frame within which the occurrence was expected;
- a specified expected occurrence or class of occurrence;
- a relevant temporal window;
- a source-grounded basis for the expectation;
- evidence that the non-occurrence is meaningful rather than merely undocumented;
- loss, uncertainty, and alternative explanations disclosed.


### 10.1 Gap matrix

| Gap type | Primary claim effect | Possible next test | Does not imply automatically |
| --- | --- | --- | --- |
| missing document | claim detail or chronology may be limited | search, alternative record, or bounded claim | falsehood or Non-Event |
| inaccessible source | support may remain provisional or underdetermined | access change, independent source, or stop | confirmation |
| temporal gap | sequence, transition, or trajectory may be underdetermined | narrow interval or compare alternatives | path continuity |
| relation gap | constitutive or functional link unsupported | counterfactual or component test | mere correlation becomes function |
| rival gap | no adequate competing construction tested | construct relevant rival or bound claim | preferred model superiority |
| calibration gap | threshold does not discriminate neighboring cases | comparison set or explicit open threshold | universal distinction |
| source-provenance gap | item origin or integrity unclear | provenance repair or exclusion | usable support |
| capture gap | adequate retained claim may be unavailable | Non-Capture test and re-entry condition | automatic `non_capture` |
---

## 11. Source Trace and Traceable Load

A source basis lists what material is available. A Constitutive Source Trace states how load-bearing and limiting source features enter the result.

```text
many sources
≠
traceable source-result dependency
```

A source trace should disclose, where applicable:

- load-bearing features;
- modulating features;
- compressed features;
- excluded features;
- uncertain features;
- irrecoverable features;
- temporal and relational dependencies;
- expected result change if a constitutive feature changes;
- resulting claim limitation.

```text
citation
≠
TraceableLoad
```

For PROJECT_AS, a source-target dependency is one operation-specific form of the broader source-result dependency. COMPOSE and DECOMPOSE require their own trace forms rather than being forced into target-function language.

---

## 12. Inferential Distance

Inferential distance describes how much declared reconstruction separates source material from the tested claim. It is not a numeric evidence score.

```text
inferential distance
≠
numeric evidence score
```

| Local description | Typical source-claim relation | Required control |
| --- | --- | --- |
| minimal | source explicitly records the bounded claim relation | provenance and scope |
| moderate | one or more declared relations connect source and claim | inference path, alternatives, and limits |
| extended | multi-step composition, decomposition, or projection carries the claim | formation rule, trace, counterfactual load, calibration, and loss |
| ceiling risk | result becomes insensitive to load-bearing source change or more precise than available sources | claim reduction, failure, stop, or Non-Capture test |


Higher inferential distance can be admissible if trace, alternatives, and claim limits remain adequate. Lower distance does not guarantee relevance, truth, or authority.

---

## 13. COMPOSE and PATH Evidence

COMPOSE requires evidence not only for selected items but for the formation rule, ordering, constitutive relations, alternatives, and loss that make the result a new composite analytical object.

| Evidence duty | Minimum burden | Failure signal |
| --- | --- | --- |
| source selection | identified source structures and exclusion rationale | unmarked cherry-picking |
| ordering | temporal or structural ordering basis | unordered aggregation presented as sequence |
| transition | support for movement or relation between configurations | chronology presented as path |
| formation rule | why these sources constitute one composite | parts list presented as COMPOSE |
| constitutive relation | which relations carry the composite | co-presence treated as constitution |
| alternative construction | relevant rival sequence, path, or composite | retrospective inevitability |
| non-event support | frame-bound meaningful non-occurrence where claimed | missing record treated as Λ |
| selection and loss | preserved, compressed, excluded, uncertain, irrecoverable | lossless-addition assumption |


### 13.1 PATH claim burden

| Claim type | Minimum evidence burden | No-inflation rule |
| --- | --- | --- |
| sequence claim | supported temporal ordering | does not establish transition structure |
| path claim | sequence plus supported transitions, alternatives, and path frame | does not follow from chronology alone |
| trajectory claim | path plus repetition, sedimentation, persistence, or historical load | does not follow from duration alone |
| path-dependence claim | historical load on current possibilities plus relevant rival or counterfactual burden | trajectory does not establish dependence automatically |
| branch-closure claim | evidence that an alternative was materially available and later closed | retrospective non-selection is insufficient |
| sedimentation claim | repeated structure and retained historical load | recurrence alone is insufficient |


These are local warrant relations, not a universal evidence ladder or authority hierarchy.

---

## 14. DECOMPOSE and SUB Evidence

DECOMPOSE requires finer support while preserving the same reference object. Additional detail must be source-supported and must not silently open an operator type, change the object, or exceed the Source Ceiling.

| Evidence duty | Minimum burden | Failure signal |
| --- | --- | --- |
| same-reference support | evidence that finer components belong to the same occurrence or composite | new object presented as decomposition |
| component identification | source-grounded components and uncertainty | analyst-invented constituents |
| component relation | relations among components and to the whole | parts list without reconstruction |
| temporal relation | order or duration where constitutive | static anatomy replacing process |
| source-function comparison | how finer evidence confirms, refines, differentiates, partially preserves, rejects, or leaves underdetermined the prior function claim | source-function effect treated as DECOMPOSE class |
| alternative internal model | relevant rival decomposition | single plausible model presented as final constituents |
| inaccessible area | declared gaps and Source Ceiling | hidden certainty |
| resolution test | which warranted reconstruction changes | detail count treated as gain |
| upper traceability | components remain tied to source object and coarser functional load | fragmentation without source-object load |


```text
plausible internal model
≠
source-supported decomposition
```

An admissible DECOMPOSE can reject a prior source-function claim. Evidence effects on the prior claim, the operation result, and the canonical output class remain separate.

---

## 15. PROJECT_AS and RETYPE Evidence

PROJECT_AS requires evidence for a bounded target function while preserving source reference and origin type. Structural resemblance alone is insufficient.

| Evidence duty | Minimum burden | Failure signal |
| --- | --- | --- |
| origin-object support | identified source object and provenance | untyped label source |
| origin-type support | declared and revisable occurrence typing | target function replacing origin type |
| target context | bounded context, level, period, and affected praxis dimensions | universalized transfer |
| target-function support | evidence that the source structure performs the declared function in context | analogy presented as function |
| Constitutive Source Trace | load-bearing, modulating, compressed, excluded, and uncertain source features | bibliography substituted for trace |
| Functional Continuity | function remains dependent on identified source features | source-indifferent target function |
| Counterfactual Sensitivity | relevant source change would alter the projected function | causal proof inferred |
| validity scope | record-bound reach and limitations | one context treated as all contexts |
| alternative projection | relevant rival function or analogy-only option | preferred projection treated as unique |
| loss disclosure | what origin structure is hidden, compressed, excluded, uncertain, or irrecoverable | projection treated as lossless retyping |


```text
structural resemblance
≠
evidence for a target function
```

```text
formal correspondence
≠
semantic preservation
```

An analogy may be evidentially supported even when PROJECT_AS is not. The result may therefore be `analogy_only` rather than a valid projection.

---

## 16. Claim-Family Evidence Burden Matrix

| Claim family | Minimum source burden | Counterfactual or revision burden | Rival burden | External warrant boundary |
| --- | --- | --- | --- | --- |
| occurrence typing | identifiable reference object and occurrence-level support | changed evidence can revise typing | neighboring typing criteria | none unless external empirical assertion is added |
| sequence | temporal ordering support | order change | alternative ordering where material | none |
| path | transitions, alternatives, branch structure, path frame | transition or option removal | rival path | historical truth beyond sources |
| trajectory | path plus repetition, sedimentation, persistence | interruption or desedimentation | rival trajectory | broad historical generalization |
| path dependence | historical load on present possibilities | counterpath or altered prior condition | weak versus strong dependence rival | actual causality if claimed |
| composite formation | source selection, formation rule, constitutive relations | source removal or relation change | alternative COMPOSE | macro empirical totality |
| decomposition | finer source support at same reference | component change/removal | rival internal model | final constituents |
| component role | role-specific evidence | change/removal/replacement test | alternative role assignment | biological or psychological diagnosis |
| source function | coarse function claim plus finer reconstruction | component and relation change | alternative function | actual causal mechanism |
| functional projection | origin support, target context, source trace, functional continuity | source-feature change | rival projection or analogy | semantic, normative, or application authority |
| structural analogy | documented bounded similarity | difference that breaks analogy | alternative comparison | target function |
| continuity | specific reference, type, functional, or temporal trace | appropriate discontinuity test | rival identity or relation | metaphysical identity |
| admissibility | recorded results of all applicable checks | gate failure | alternative bounded claim | truth, causality, or authorization |
| non-capture | documented capture limit and adequate alternatives attempted | new source or representation | rival framework or re-entry | rival superiority |
| external warrant | STRATA-internal structured question and limits | domain-specific test | domain rival | requires external method and governance |
---

## 17. Continuity and Type-Integrity Evidence

| Check | Evidence burden | Important allowance | Failure boundary |
| --- | --- | --- | --- |
| Reference Continuity | stable historical or structural reference across the operation | same label is insufficient | object change requires a new record or claim |
| Type Integrity | source, occurrence, composite, origin type, and target function remain distinguished | type evidence may revise an occurrence typing | silent replacement is operation failure |
| Functional Continuity | claimed function depends on identified source features | semantic similarity is insufficient | source-independent function exceeds traceability |
| Temporal Continuity | relevant order, duration, transition, sedimentation, and historical load are preserved where constitutive | complete chronology is not required | punctualization cannot erase process load |


A rejected prior source-function claim can be a valid bounded result of finer evidence. Functional Continuity requires honest source-result dependency, not forced confirmation of the earlier claim.

---

## 18. Counterfactual Evidence

Counterfactual Sensitivity tests source load. It does not establish actual causality.

| Counterfactual form | Changed element | Minimum basis | Evidence status |
| --- | --- | --- | --- |
| source-grounded | changes a documented source feature | feature is present and declared load-bearing | strongest STRATA-internal form |
| frame-grounded | changes a frame condition with documented relevance | frame relation is explicit | bounded to declared frame |
| operation-specific | changes selection, component, or target feature according to the operation | operation identity and source trace preserved | cannot substitute for empirical experiment |
| unavailable | relevant change cannot be tested under current sources | unavailability and claim effect declared | may support provisional, reduction, stop, or non-capture testing |
| unconstrained fiction | changes unspecified or unsupported conditions | no source-grounded relation | inadmissible as evidence |


A counterfactual record should state:
- the source feature changed;
- why it is treated as constitutive, strongly modulating, or otherwise relevant;
- the expected result change;
- the source or reconstruction supporting that expectation;
- uncertainty, rival expectations, and test limits.

```text
counterfactual plausibility
≠
causal proof
```

---

## 19. Calibration and Comparison Evidence

Calibration asks whether distinctions and thresholds discriminate relevant neighboring cases and preserve counterexamples.

| Calibration source | Function | Limit |
| --- | --- | --- |
| positive comparison case | shows the distinction under expected conditions | cannot set a universal threshold alone |
| negative case | shows absence or failure of the distinction | must be comparable |
| confusion case | tests neighboring categories or label substitution | requires explicit competing classification |
| boundary case | tests threshold or transition zone | may remain open rather than forced |
| rival case | tests alternative operation or claim | burdens must be comparable |
| analyst replication | checks whether another analyst can apply the distinction | agreement is not truth proof |
| open calibration status | records unavailable or insufficient discriminator | may justify bounded or provisional output |


```text
formal precision
≠
calibration evidence
```

```text
more exact fields
≠
better calibrated distinction
```

---

## 20. Source Ceiling and Evidence Gaps

The Source Ceiling is claim-relative. It marks where available material no longer supports additional detail, internal process, precision, or inference.

```text
source basis size
≠
Source Ceiling
```

```text
source quantity
≠
support sufficiency
```

| Ceiling or gap form | Evidence limitation | Typical bounded response |
| --- | --- | --- |
| detail ceiling | finer elements cannot be supported | reduce granularity or stop |
| process ceiling | internal mechanism or transition remains inaccessible | retain bounded structural description |
| temporal ceiling | order, duration, or interval cannot be resolved | narrow temporal claim |
| relation ceiling | constitutive or functional link cannot be supported | reduce to co-occurrence or analogy where warranted |
| comparison ceiling | rivals cannot be discriminated | provisional, partial, or non-capture test |
| generalization ceiling | source does not support broader frames or contexts | retain local claim |
| authority boundary | claim requires external empirical, causal, normative, diagnostic, legal, political, or policy warrant | mandatory stop under STRATA authority and external handoff |


The authority boundary is independent of the Claim Ceiling's structural and source-supported reach. A well-supported structural claim does not inherit external authority.

---

## 21. Selection, Loss, and Uncertainty

Evidence selection and transformation loss must be disclosed separately.

```text
selection
≠
loss
```

Selection records what enters the analysis and why. Loss records what the transformation preserves, compresses, excludes, leaves uncertain, or makes irrecoverable.

| Loss class | Evidence meaning | Disclosure duty |
| --- | --- | --- |
| preserved | source structure remains available and materially represented | not proof of complete reproduction |
| compressed | source structure remains acknowledged in reduced form | must state what distinction disappears |
| excluded | source material or relation is deliberately outside the result | exclusion rationale required |
| uncertain | support or recoverability remains open | not equivalent to irrecoverable |
| irrecoverable | reliable reconstruction is no longer possible | must not be hidden by formal completion |


Uncertainty may concern source provenance, reference identity, order, relation, function, counterfactual load, calibration, or capture. The affected claim dimension must be named rather than summarized as generic uncertainty.

---

## 22. External-Warrant Evidence

STRATA may structure questions that require other methods. It does not establish those claims by transformation alone.

| External claim | Possible STRATA contribution | Additional evidence and authority required |
| --- | --- | --- |
| empirical truth | bounded structural hypothesis and source trace | appropriate empirical data and domain method |
| actual causality | candidate mechanism and counterfactual sensitivity | causal design or domain-appropriate causal evidence |
| semantic validity | explicit structural correspondence and loss | language-, culture-, or domain-specific semantic assessment |
| normative validity | clarified stakes, alternatives, and asymmetries | independent normative argument and legitimate process |
| predictive validity | bounded projection and stated conditions | out-of-sample or prospective prediction evidence |
| rival superiority | comparable reconstructions and failure conditions | adequate comparative evidence and criteria |
| policy effectiveness | bounded scenario, costs, and risks | policy evidence, governance, and accountability |
| clinical or diagnostic claim | non-diagnostic structural observation only | qualified clinical method, evidence, consent, and safeguards |


```text
successful STRATA transformation
≠
external warrant
```

Person typing, diagnosis, moral ranking, legitimacy judgment, sanction entitlement, irreversible labeling, automatic intervention recommendation, and authority inheritance remain prohibited under STRATA authority.

---

## 23. Case and Countercase Evidence Handoffs

Before case production, all entries in this section are routing obligations rather than substantive evidence claims.

| Case evidence type | Required contribution | No-authority rule |
| --- | --- | --- |
| positive case | demonstrates a rule under bounded conditions | does not prove universality |
| negative case | demonstrates an operation or claim failure | does not invalidate unrelated rules |
| confusion case | tests neighboring categories and non-equivalences | must preserve both candidate classifications |
| boundary case | tests Floor, Ceiling, calibration, or claim limit | may produce bounded or open result |
| stop case | shows why continuation becomes inadmissible or unnecessary | must distinguish mandatory and optional stop |
| non-capture case | shows an adequate retained claim is unavailable without distortion | must state re-entry and rival conditions |
| chain case | tests separated operation occurrences and loss records | later success cannot erase earlier failure |
| countercase | pressures a central rule or recurrent pattern | must remain available through Part lock |


```text
case evidence
≠
theory authority
```

Every central rule requires positive, negative, confusion or boundary, and Stop or Non-Capture coverage before relevant Part lock.

---

## 24. Formal Model and Smoke-Test Evidence Boundary

The formal model may validate declarations and consistency. It cannot establish substantive source truth or semantic adequacy.

| Machine-checkable declaration | Formal validation scope | Human or domain judgment retained |
| --- | --- | --- |
| source basis declared | presence and syntactic form | whether sources are truthful or sufficient |
| evidence roles represented | presence and open-controlled-term structure | whether role assignment is substantively correct |
| support mode, support status, availability, and warrant route present | requiredness, closed machine spellings where specified, and valid nesting | whether the substantive judgment is warranted |
| gaps and uncertainty present | required disclosure structure | whether all material gaps were found |
| counterfactual test recorded | required parts and valid branch form | whether the counterfactual is empirically plausible |
| rival considered | declared rival or explicit not-applicable reason | whether the best rival was selected |
| Source Ceiling assessment present | required declaration and claim-effect structure | where the substantive ceiling actually lies |
| canonical output valid | one of ten controlled values | whether that class is materially correct |


The populated Core Model provides architecture, integration, schema, and package-conformance evidence only. The completed smoke suite adds record-instance and cross-record conformance evidence; neither form establishes theoretical truth.

```text
formal conformance evidence
≠
theoretical truth evidence
```

The ten canonical output classes are realized in `07_model/Output_Classes.yaml`, the decision tree, the record schema, and the Root assembly. The eight named smoke records and `07_model/examples/README.md` are populated and internally audited. The committed suite directly instantiates five of the ten classes; the remaining five retain formal owner, route, and boundary coverage but no committed instance-level smoke evidence.

### 24.1 Canonical output inventory boundary

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

Evidence roles, support modes, support statuses, availability conditions, warrant routes, gap descriptions, and formal validation results do not become additional output classes.

---

## 25. Current Repository Provenance Map

| Evidence or control object | Current source | Status | Boundary |
| --- | --- | --- | --- |
| PMS Base inventory and dependencies | `PMS.yaml` | current external governing reference | authoritative for PMS grammar, not empirical domain claims |
| STRATA architecture | `00_source/PMS-STRATA_Structure.md` | current architecture control | chapter design, not completed canonical prose |
| production obligations | `05_minified/Block_Contracts.md`; `05_minified/Chapter_Contracts.md` | current binding controls | obligation evidence, not substantive truth |
| operation controls | Operation Signatures, Transformation Operation Index | current control | classification and handoff evidence |
| claim and output controls | Claim Type Table; Output Class Index | current control | vocabulary and governance evidence |
| admissibility controls | Admissibility Band Minified; Admissibility Band Reference | current control | boundary architecture evidence |
| terminology and distinctions | Glossary; Non-Equivalence Index | current control | terminological consistency evidence |
| cross-reference routing | Cross Reference Map | Chapter-3-WP3-synchronized scaffold v0.3.18 | navigation and verified handoff evidence |
| evidence routing | Evidence Map | Chapter-3-WP3-synchronized scaffold v0.3.19 | not substantive source evidence |
| Formal Model v0 Core assembly | seven populated Core artifacts in `07_model/` | complete and package-validated | architecture and formal consistency evidence only |
| Root and Companion validation | `07_model/PMS-STRATA.yaml`; `07_model/PMS-STRATA.schema.json` | current Root validates against current Companion | assembly consistency is not substantive warrant |
| transformation-record validation contract | `07_model/Transformation_Record.schema.json` | populated and valid Draft 2020-12 schema | schema validity alone does not establish material correctness of present or future record instances |
| canonical Block prose | `01_blocks/01_foundations.md` canonical anchors for Chapters 0–3 | Chapters 0–3 provisionally locked; Chapters 4–57 pending | canonical methodological prose; not empirical domain evidence |
| cases and countercases | `03_cases/*` | pending | no current case evidence |
| smoke-test record instances | eight YAML files in `07_model/examples/` | populated and schema-valid | current internal record-level conformance evidence; not substantive or external evidence |
| smoke-suite documentation | `07_model/examples/README.md` | populated and synchronized | current suite inventory, coverage boundary, and cross-record interpretation contract |
| external domain evidence | outside repository unless later declared | pending per application | no inherited authority |
---

## 26. Open Evidence Registry

| Open evidence family | Planned target | Reason open | Unlock stage |
| --- | --- | --- | --- |
| canonical chapter support | Chapters 4–57 and Front Matter | Chapters 0, 1, 2, and 3 are provisionally locked; later prose remains pending | chapter lock |
| positive and negative case evidence | all central rules | case corpus not yet produced | Part locks and integrated audit |
| confusion and boundary evidence | non-equivalences and thresholds | case IDs pending | Part locks |
| calibration sets | Chapters 44–49 and operation boundaries | comparison cases pending | LIMITS and case production |
| rival reconstructions | PATH, SUB, RETYPE, integrated audit | case-specific rivals pending | case records |
| expanded formal record-instance coverage | possible additional committed records for the five currently uninstantiated Output Classes | current suite directly covers five of ten classes; expansion is not required for the passed internal gate but remains open to later stress | later model/case stress or Model Finalization |
| cross-record suite evidence | eight smoke records plus `07_model/examples/README.md` | suite-level semantic, graph, handoff, negative-mutation, and package audits passed | rerun whenever a record or controlling model owner changes |
| external empirical or causal evidence | application-specific | outside STRATA core | external application method |
| reader and derivative evidence routes | Reader and publications | deferred | release stages |


Pending evidence must not be cited as if already produced. Absence of pending evidence must constrain the present claim rather than being silently filled by confident prose.

---

## 27. Definition-Site and Cross-Reference Map

| Evidence concept | Designated primary site | Application or elaboration | Reference handoff |
| --- | --- | --- | --- |
| source basis | Chapter 49 | Chapter 7 and operation records | Glossary; Evidence Map; Claim Type Table |
| support mode | Chapter 7 | Chapter 49 and operation records | Glossary; Evidence Map; Claim Type Table |
| support status | Chapter 7 | Chapters 49 and 53 | Glossary; Evidence Map; Claim Type Table; Output Class Index |
| evidence availability | Chapter 49 | Chapter 7 and operation records | Glossary; Evidence Map; Claim Type Table |
| record-level status declaration | Chapter 7 | operation, case, chain, and integrated-audit records | Glossary; Claim Type Table; Output Class Index |
| Constitutive Source Trace | Chapter 45 | Chapter 30 and all operations where applicable | Glossary; Admissibility Band Reference |
| TraceableLoad | Chapter 6 | Chapter 45 | Glossary; Admissibility Band Reference |
| Source Ceiling | Chapter 49 | Chapters 20, 27, 30, 39, 53 | Glossary; Claim Type Table; Admissibility Band Reference |
| Counterfactual Sensitivity | Chapter 6 | Chapter 46 and operation-specific tests | Admissibility Band Reference |
| calibration | Chapter 49 | local operation boundaries and cases | Glossary; Admissibility Band Reference |
| non-event structure eligibility / missing-information boundary | Chapter 1 object category; Chapters 3 and 8 temporal and audit tests | PATH and Evidence Map | Glossary; Operator Index; Non-Equivalence Index; Chapter 1 Preparation Record |
| external warrant | Chapter 56 | application-specific | Claim Type Table; Evidence Map |
| formal evidence boundary | Chapter 49 | populated Formal Model v0 Core and passed internal smoke-test gate | Admissibility Band Reference; Cross Reference Map; `07_model/Transformation_Record.schema.json` |


This map does not become a second definition site. It routes controlled meanings to their existing owners.

---

## 28. Post-Smoke Evidence Gate

This gate distinguishes internal formal evidence from substantive and external warrant.

- [x] Seven Core artifacts are populated and package-validated.
- [x] Eight canonical smoke records and the suite README are populated.
- [x] Record-level schema, route, class, loss, rule, and audit-stage conformance is evidenced.
- [x] Cross-record IDs, claims, handoffs, operation order, loss preservation, and acyclicity are evidenced.
- [x] Structural rejection and schema-valid/materially-invalid mutation layers remain distinct.
- [x] Direct committed Output-Class coverage is stated as five of ten, not as a complete class census.
- [x] Reference/status and Root provenance synchronization are complete.
- [x] Chapter 1 preparation evidence remains limited to production readiness, while provisionally locked Chapter 1 canonical prose evidences the internally controlled object architecture, derived-object boundary, and minimum identity burdens only.
- [x] Neither the preparation record nor the WP1–WP4 audits are treated as empirical confirmation, calibration, causal proof, or proof of object identity in a domain.
- [x] Substantive cases, calibration, inter-annotator agreement, rival comparison, empirical truth, causality, normative validity, and external warrant remain pending.
- [x] Formal smoke success is not used as scientific confirmation.

```text
pass
→ internal Core and smoke-suite conformance evidence current
→ substantive and external evidence ceilings preserved
→ Chapter 1 internal evidence route is current and Chapter 1 is provisionally locked; Chapter 2 WP1 internal evidence route is current and WP2 may begin

fail
→ repair evidence-role, support, route, pointer, status, provenance, or authority handling before the next Foundations chapter
```

These gate terms are workflow-only and are not canonical Output Classes.

## 29. Revision and Freeze Policy

### 29.1 Revision during Block production

During Block production, this map may add only verified prose anchors, controlled source roles, evidence burdens, gap categories, and explicit handoffs supported by Structure, contracts, minified controls, canonical prose, and substantive Reference artifacts.

### 29.2 Update triggers

Update this map when:
- a chapter establishes a real source or evidence anchor;
- a case, countercase, confusion case, calibration set, stop case, or non-capture case is produced;
- a formal smoke test is executed and validated;
- an external-warrant source or method is explicitly declared;
- a Source Ceiling, source-form, support-mode, support-status, availability, warrant-route, or record-level status distinction changes through authorized corpus revision;
- the Cross Reference Map or Audit Checklist gains a new verified handoff.

### 29.3 Freeze requirements

Final Reference Freeze requires:
1. every core claim family to have explicit evidence and counterevidence duties;
2. all central rules to have positive, negative, confusion or boundary, and Stop or Non-Capture coverage;
3. all executed formal tests to be distinguished from substantive evidence;
4. unresolved evidence gaps and external-warrant dependencies to remain visible;
5. no citation, source count, formal consistency, model success, or case volume to be represented as truth proof;
6. no later source, frame, granularity, operation, or target function to erase a prior failed claim;
7. derivatives and Reader routes to remain without back-propagating authority.

The Evidence Map remains revisable until cases, conclusion, front matter, appendices, corpus audit, and model finalization are complete.

---

## Chapter 2 WP1 Evidence Boundary

The Chapter 2 preparation record supplies production provenance and ownership control only. Canonical [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) supplies methodological definitions and internally auditable examples for frame, granularity, relative level, and micro–meso–macro shorthand; it does not establish empirical truth for any external frame, granularity, or relative-level declaration. Temporal, source, and claim scope are canonical in WP2; coordinate comparison and the Minimal Level Declaration are canonical in WP3.

Current WP1 examples and future Chapter 2 cases must distinguish:

| Claim pressure | Minimum support relation | Unsupported inflation to prevent |
| --- | --- | --- |
| frame declaration | source-supported relevance and inside/outside boundary | analyst-selected frame treated as natural fact |
| finer granularity | additional source-supported distinctions with praxeological purchase | more detail treated as higher truth |
| relative-level claim | explicit comparison or composition relation | `higher` or `lower` used without reference object |
| source scope | declared accessible materials, supported distinctions, and known gaps | source quantity treated as scope sufficiency |
| claim scope | explicit object, frame, time, level, and generalization boundary | local reconstruction generalized by default |

The three WP1 running assignments are completed as canonical methodological examples, not substantive case files or empirical evidence. The remaining WP3 assignments are now executed as methodological chapter examples; substantive case-file production remains future work.

## Chapter 2 WP2 Evidence and Warrant Status

The WP2 running examples are methodological constructions built from a declared illustrative agenda–transcript–minutes bundle. They demonstrate scope discipline but do not establish empirical findings about any actual organization, meeting, person, recurrence, motive, or later event.

| WP2 object | Support status | What it demonstrates | What it does not warrant |
| --- | --- | --- | --- |
| open temporal edge | methodological example | temporal scope can end while later relations remain unresolved | actual later non-occurrence |
| source gap | methodological example | missing follow-up material must remain missing | positive non-event, motive, or institutional pattern |
| bounded local claim | chapter-level illustration | claim scope can support `admissible_with_bounded_claim` under explicit exclusions | empirical truth certification or external warrant |
| institution-wide overreach | counterpressure | reduction or Stop when local material is promoted beyond scope | a substantive finding about an institution |

No external warrant is added. The next evidence-producing duty remains later substantive cases and external testing; WP3 comparison cases will still be chapter illustrations unless separately sourced and registered.

## Chapter 2 WP3 Evidence and Comparison Status

WP3 uses the same declared illustrative project-review conversation to test coordinate movement, plurality, comparability, contradiction, Stop, and Non-Capture. These examples show methodological burdens only.

| WP3 pressure | Minimum support relation | Evidence limit |
| --- | --- | --- |
| finer granularity | additional source-supported distinctions plus preserved reference relation | more distinctions do not certify truth or completeness |
| changed frame | stable resolution plus a new relevance rule and new claim | frame selection does not prove a PMS operator occurrence or target function |
| changed relative level | named comparator, relation, and bounded purpose | vertical language without relation has no support |
| multiple valid granularities | local purchase, traceability, loss disclosure, and rival availability | plurality does not establish equal usefulness or total capture |
| apparent contradiction | claims shown to answer different or compatible predicates | scale wording alone does not establish coexistence |
| substantive contradiction | incompatible answers to the same bounded predicate | different resolution cannot neutralize the conflict |
| Minimal Level Declaration | conceptual completeness plus mapping to existing record paths | declaration is not evidence, schema validity, or operation proof |

`C2-POS-02`, `C2-CONF-01`, `C2-POS-03`, `C2-PLUR-01`, `C2-CONF-02`, `C2-NEG-01`, and `C2-NC-01` are now fulfilled as chapter-level methodological examples. They are not populated `03_cases` artifacts and do not provide external warrant.

---

## Chapter 2 Provisional-Lock Evidence and Warrant Status

Chapter 2 is now canonical and provisionally locked. Its local project-conversation constructions are structural examples under declared illustrative source assumptions. They establish conceptual burdens and counterpressure; they do not establish external empirical findings.

| Chapter 2 item | Current evidence status | Warrant limit |
| --- | --- | --- |
| baseline coordinate declaration | canonical construction | no institution-wide finding |
| stable frame / changed granularity | canonical comparison construction | no automatic `DECOMPOSE` or truth gain |
| changed frame / stable granularity | canonical confusion construction | no automatic `PROJECT_AS`, `Φ`, or target function |
| changed relative level | canonical relational construction | no ontological rank or authority inheritance |
| multiple valid granularities | canonical plurality rule | no universal resolution hierarchy |
| granularity conflict | canonical comparability rule | no automatic contradiction or automatic neutralization |
| Minimal Level Declaration | canonical conceptual template | not a Shared Transformation Record or schema |
| ten `C2-*` assignments | future substantive Case duties | not yet evidence and not Case Index completion |

The Formal Model mirrors declaration and boundary structure. Schema validity, path completeness, registry consistency, or a green audit does not establish source truth, empirical comparability, substantive contradiction, or the best analytical coordinates.

---

## Chapter 3 Preparation — Temporal Support Requirements

| Proposed claim | Required support | Insufficient support |
| --- | --- | --- |
| event | source-supported realized relevant change and temporal placement | date or mention alone |
| non-event | expectation source, bounded condition, non-realization, praxeological load | missing record or analyst surprise |
| transition | two bounded configurations, supported order, intervening structure, changed conditions | endpoint comparison alone |
| sequence | source or analytical ordering basis and selected units | arbitrary narrative order |
| path | actual traversal plus constitutive relation, selection, and loss disclosure | chronological list |
| trajectory | path plus sedimented load changing later meaning/cost/possibility | long duration or repeated label |
| path dependence | evidence that prior order/path materially conditions the present claim | `Θ`, history rhetoric, or correlation alone |
| sedimentation | accumulated source-traceable load | elapsed time alone |
| irreversibility | bounded restoration or cost-equivalence test | absolute assertion or rhetorical permanence |
| unrealized alternative | evidence of historical/structural availability, blockage, delay, or rejection | imaginable possibility |

The Chapter 3 Preparation Record is evidence of production readiness only. It is not evidence that any concrete path, trajectory, path-dependence, or irreversibility claim is true.



## Chapter 3 WP1 — Temporal Object Support Requirements

Canonical source: [`Chapter 3 Sections 3.1–3.5`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Claim | Required support | Insufficient substitute |
| --- | --- | --- |
| configuration | temporal location, relevant relation set, praxis conditions, bounded sources and claim | exhaustive-world rhetoric or unordered co-presence |
| state adequacy | narrow variable, temporal location, support, and immateriality of omitted relations | convenience of compression alone |
| event | positive realization, temporal placement, frame relevance, source support | expectation, endpoint difference, or causal story |
| non-event | expected occurrence, warranted expectation, realization bound, supported non-realization, praxeological load | absent record, unknown occurrence, analyst surprise |
| transition | identifiable configurations, temporal order, intervening structure, changed conditions, bounded relation | two different snapshots or one event label |

Chapter prose and illustrative cases establish methodological burdens only. They are not evidence that any external event, non-event, or transition claim is true.

## Chapter 3 WP2 — Ordered Historical Object Support Requirements

Canonical source: [`Chapter 3 Sections 3.6–3.8`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Claim | Required support | Insufficient support | Permitted reduction |
| --- | --- | --- | --- |
| sequence | declared analytical units, ordering basis, supported order, bounded scope | dates or presentation order alone | chronology, partial order, unresolved internal order |
| path | sequence plus actual traversal, connected configurations/transitions, selection rule, source trace, branch/omission/loss disclosure | chronology, plausible narrative, endpoint identity, or labels alone | sequence or chronology |
| trajectory | path plus source-supported historical carry-over with traceable later praxis effect | duration, archive survival, operator pairing, memory, or directionality alone | path or localized persistence claim |
| directionality | supported bounded continuation pressure | retrospective purpose, destiny, inevitability, or final goal | bounded directional claim |

The WP2 examples are methodological constructions. They are not empirical case evidence, external calibration, or proof that the same trajectory exists beyond the declared source and claim scopes.

## Chapter 3 WP3 — Historical-Property Support Requirements

Canonical source: [`Chapter 3 Sections 3.9–3.13`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory).

| Claim | Required support | Insufficient substitute | Permitted reduction |
| --- | --- | --- | --- |
| path dependence | warranted historical object, current-conditions insufficiency, prior-order/branch relevance, supported alternative-order sensitivity, traceable carry-over, bounded scope | `Θ`, duration, trajectory label, historical rhetoric, or imagined comparator | trajectory or bounded historical relevance |
| sedimentation | identified historical contributions, accumulation/persistence relation, source-supported carrier, later praxis relevance, declared scope | elapsed time, archival survival, remembrance, or operator co-presence | historical persistence or trajectory without stronger property detail |
| bounded irreversibility | declared frame, claim, object relation, restoration criterion, residual difference/cost, uncertainty | permanence rhetoric, any past occurrence, formal non-reversal alone | bounded residual-load or loss statement |
| unrealized alternative | bounded branch point, identifiable alternative, source-supported availability, relevant conditions, non-traversal status | analyst imagination, wish, absent record, retrospective preference | provisional possibility or omission |
| Minimal Temporal Object Chain | each stage's additional burden, source trace, loss, downgrade route, failed chronology-to-path variant | labels, timestamps, wider scope, or higher level | strongest warranted lower-burden object |

The WP3 chapter examples are methodological constructions. They are not empirical proof of path dependence, irreversibility, or alternative availability in an external case.

---

## Chapter 3 Case and Evidence Duties

The Chapter 3 provisional lock assigns fifteen later case duties: `C3-CONF-01`, `C3-EVT-01`, `C3-NON-01`, `C3-NON-02`, `C3-TRN-01`, `C3-TRN-02`, `C3-SEQ-01`, `C3-PATH-01`, `C3-PATH-02`, `C3-TRAJ-01`, `C3-PD-01`, `C3-TELE-01`, `C3-IRR-01`, `C3-ALT-01`, `C3-NC-01`. These assignments require positive, negative, confusion, reduction, Stop, irreversibility, alternative, and Non-Capture pressure. They are not completed empirical cases, evidence claims, or Shared Transformation Records. The Case Index remains unchanged until the case-production stage.

---

## Chapter 4 Preparation Evidence and Case Duties

The preparation gate assigns sixteen future operation-grammar pressures: `C4-COUNT-01`, `C4-CMP-01`, `C4-CMP-02`, `C4-DEC-01`, `C4-DEC-02`, `C4-PROJ-01`, `C4-PROJ-02`, `C4-CHAIN-01`, `C4-CHAIN-02`, `C4-CHAIN-03`, `C4-NINV-01`, `C4-NINV-02`, `C4-NINV-03`, `C4-CONF-01`, `C4-STOP-01`, and `C4-NC-01`.

These assignments require evidence sufficient to distinguish:

- new composite formation from chronology or aggregation;
- same-reference finer reconstruction from added detail or competing-object formation;
- source-dependent bounded function from analogy, renaming, recontextualization, or type replacement;
- separate chain links from one collapsed operation claim;
- bounded non-invertibility from metaphysical irreversibility;
- unresolved operation identity from protection of either strong candidate claim.

```text
case assignment
≠ completed case
≠ empirical evidence
≠ schema-valid record
≠ admissible transformation
```

The Case Index remains unchanged until the case-production stage. The common review-process source family is a methodological construction inherited from Chapters 1–3, not an external empirical dataset.

---

## Chapter 4 WP1 Support and Evidence Boundary

The Chapter 4 examples are methodological constructions using the established review-process source family. They demonstrate operation-signature burdens; they are not external evidence that a concrete organization exhibits the reconstructed path or function.

| Example | What it demonstrates | What it does not prove |
| --- | --- | --- |
| `C4-COUNT-01` | bounded closure test for a proposed fourth operation | universal ontological completeness |
| `C4-CMP-01/02` | supported composite formation versus chronology-only failure | empirical truth of an external review history |
| `C4-DEC-01/02` | same-object finer reconstruction versus competing-object substitution | lossless recovery of original sources |
| `C4-PROJ-01/02` | bounded source-dependent function versus analogy or label substitution | permanent type, authority, or universal validity |

Canonical prose supplies methodological warrants. Concrete case admissibility still requires actual sources, declared context, local loss, and independent testing.

---

## Chapter 4 WP2 Chain-Warrant Boundary

The WP2 chain examples demonstrate methodological separation, not empirical occurrence of a real organizational chain.

| Claim | Required warrant | Unsupported shortcut |
| --- | --- | --- |
| direction claim | source–target signature plus separate coordinate declaration | “upward,” “downward,” or “reframed” wording |
| level-relation claim | focal unit, comparator, relation, purpose, and declared coordinate change/stability | wider or finer target treated as higher truth or authority |
| chain handoff | prior target availability, identity, and successor source declaration | textual adjacency or reused label |
| later-link success | independent function or reconstruction warrant | validity inherited from earlier link |
| integrated chain result | retained local Output Classes and explicit relation among them | one flattened verdict that erases link failure |

`C4-CHAIN-01`, `C4-CHAIN-02`, and `C4-CHAIN-03` are methodological constructions. Substantive case records remain future work.

---

## Chapter 4 WP3 Support and Evidence Boundary

The non-invertibility and confusion cases are methodological constructions using the established review-path source family. They demonstrate declaration and reduction burdens; they do not establish empirical irreversibility, actual institutional memory, or the existence of an external operation chain.

| Claim | Minimum support needed | Insufficient support |
| --- | --- | --- |
| decomposed composite is not untouched source | documented selection, compression, later reconstruction question, loss comparison | mere use of a reverse verb |
| recomposition is a new occurrence | new selection, formation relation, context, and target claim | repeated label for the composite |
| projection preserves origin type | declared origin type, target function, bounded context, source trace | evocative target label |
| collapsed chain requires stop | two distinct target relations and hidden local failure conditions | stylistic complexity alone |
| unresolved operation identity warrants non-capture | positive support for rival signatures plus unresolved constitutive identity | generic missing information |
| minimal declaration is complete | all conceptual slots and existing record-path mapping | field presence as substantive validity |

Canonical return: [`Chapter 4 §4.8–4.10`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

---

## Chapter 4 Case and Evidence Duties

The Chapter 4 provisional lock assigns sixteen later case duties: `C4-COUNT-01`, `C4-CMP-01`, `C4-CMP-02`, `C4-DEC-01`, `C4-DEC-02`, `C4-PROJ-01`, `C4-PROJ-02`, `C4-CHAIN-01`, `C4-CHAIN-02`, `C4-CHAIN-03`, `C4-NINV-01`, `C4-NINV-02`, `C4-NINV-03`, `C4-CONF-01`, `C4-STOP-01`, `C4-NC-01`. These assignments require positive, negative, chain, later-link-failure, non-invertibility, confusion, Stop, and Non-Capture pressure. They are not completed empirical cases, evidence claims, or Shared Transformation Records.

---

## Chapter 5 Preparation Evidence Boundary

The preparation record supports only these workflow claims:

- the Chapter 5 Contract has been converted into a drafting and audit architecture;
- origin type, target function, transformation context, continuity dimensions, contextual boundedness, record mapping, cases, and work packages have assigned production burdens;
- existing Formal Model fields can receive later declarations without a new schema;
- canonical Chapter 5 prose and substantive case evidence do not yet exist.

It does not support:

- actual reference continuity in a domain case;
- actual semantic adequacy of a target function;
- actual source sensitivity or constitutive trace;
- empirical persistence, causality, or historical identity;
- validity outside the bounded synthetic running case;
- scientific, normative, legal, political, diagnostic, or application authority.

```text
preparation completeness
≠ continuity evidence
≠ projection validity
```

The running `P_review` example is a controlled drafting test vector. It is not empirical evidence and is not yet a Shared Transformation Record or substantive case file.

---

## Chapter 5 WP1 Support and Evidence Boundary

A target-function claim requires more than context fit or metaphorical resemblance. Its support must identify:

- the source object and origin type;
- the target context and analytical purpose;
- the load-bearing source features;
- the validity scope and exclusions;
- the material source changes that would alter, weaken, or defeat the function;
- uncertainty inherited from provisional source components.

```text
usefulness
≠ constitutive source trace

formal declaration
≠ semantic warrant
```

Canonical return: [`Chapter 5 §§5.1–5.3`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP2 Continuity Evidence Burdens

| Tested finding | Required source support | Insufficient support | Re-entry pressure |
| --- | --- | --- | --- |
| reference continuity | bounded referent, constitutive relations, source and target boundary, operation-specific bridge | same label, topic, actor, or document alone | identify the bridge or declare a new object |
| type continuity | prior typing, new evidence or finer reconstruction, reason and scope of revision | usefulness, resemblance, or later function alone | retest downstream claims under the revised type |
| functional continuity | precise function, load-bearing source features, relation to operation, material source-change test | context fit, metaphor, repeated wording, analyst preference | specify source carriage or reduce to analogy |
| provisional continuity | identifiable supported core plus named unresolved material relation | unbounded uncertainty | state the withheld stronger claim and evidence needed |
| mixed continuity result | separate evidence and result per dimension | one aggregate “continuity passed” label | disaggregate reference, type, function, and later temporal findings |

Evidence completeness does not decide semantic continuity automatically. Canonical return: [`Chapter 5 §§5.4–5.6`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP3 Temporal and Contextual Evidence Burdens

| Tested claim | Required trace | Insufficient substitute |
| --- | --- | --- |
| temporal continuity | relevant order, interval or carry-over, source-to-target bridge, bounded target-time scope | later relevance or stable wording |
| non-erasure | retained prior uncertainty, failure, Stop, or Non-Capture history | later utility or a new context |
| contextual boundedness | target context, purpose, scope, temporal reach, exclusion, revision condition | contextual similarity |
| context transfer | material relation between contexts and renewed source-feature relevance | prior admissibility |
| rival function resolution | target-purpose or discriminating functional evidence | analyst preference |
| Minimal Projection Form | complete mapped declarations across existing record families | field completion as semantic proof |

The running cases remain constructed chapter pressure tests, not empirical case files. Canonical return: [`Chapter 5 §§5.7–5.9`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

---

## Chapter 5 Continuity Evidence Handoff

Chapter 5 provides internally audited methodological prose and constructed pressure cases, not external empirical validation. Its fifteen `C5-*` assignments identify later evidence duties for referent continuity, type preservation, source-sensitive function, temporal carry-over, contextual transfer, Stop, and Non-Capture.

```text
constructed chapter case
≠ empirical case completion
≠ external validation
```

A positive continuity claim requires source-specific support for the referent, type, load-bearing features, temporal relation, target context, and validity scope. Formal fields, stable labels, or successful machine validation do not supply that evidence.

## Chapter 6 Evidence and Load-Test Handoff

Chapter 6 distinguishes source presence from source load.

```text
source named
≠ source mapped
≠ source constitutive
≠ result source-sensitive
```

A Chapter 6 test must identify the source basis, load-bearing features, relevant relations and temporality, declared loss, and the claim effect of material source change. Counterfactual Sensitivity may be `sensitive`, `partially sensitive`, `insensitive`, `underdetermined`, or `not testable with available sources`; none of these labels proves causality.

Evidence insufficiency may yield provisionality, Claim Reduction, Failure, Stop, or Non-Capture depending on the delimited claim. Missing information alone does not mechanically determine any one class.

Production control: [`Chapter 6 Preparation Record`](Chapter_6_Preparation_Record.md).

---

## Chapter 6 WP1 Relevance Evidence Boundary

A PraxisPurchase claim requires evidence for a **difference in warranted reconstruction**, not merely evidence that a finer detail exists.

Required support identifies:

- the delimited claim under review;
- the proposed added distinction;
- the affected praxis-relevant dimension;
- the prior and revised reconstruction;
- the source basis supporting the difference;
- the resulting change in scope, comparison, loss, countercase, or Stop condition.

```text
evidence for detail
≠ evidence for changed reconstruction
```

`C6-FLOOR-02` is supported as a valid comparison even though it yields no added PraxisPurchase. `C6-FLOOR-03` lacks a new delimited comparison and cannot convert repeated detail into additional support. Constructed chapter cases are methodological tests, not external empirical validation.

Canonical return: [`Chapter 6 §§6.1–6.4`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP2 Source-Dependency Evidence Handoff

Traceability evidence must establish more than source presence.

```text
source identification
+ constitutive feature mapping
+ reconstructible relations and temporality
+ disclosed selection and loss
+ target response to material source change
→ TraceableLoad candidate
```

Evidence for Counterfactual Sensitivity is evidence of analytical dependency, not evidence of actual causal history. Missing source intervals must remain missing-information conditions unless an expectation frame and bounded interval independently support a Non-Event claim.

Canonical return: [`Chapter 6 §§6.5–6.8`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP3 Integrity and Routing Evidence Handoff

Evidence for band passage must support separate burdens rather than one aggregate impression.

```text
changed warranted reconstruction
+ reconstructible source dependency
+ visible type commitments
+ bounded context and scope
→ integrated admissibility candidate
```

Source citation cannot substitute for Reference Continuity. Semantic usefulness cannot establish Type Integrity. A material source gap may support provisionality only where one coherent delimited claim remains and the limiting interval, rivals, and re-entry condition are explicit. No numeric score or formal completeness check can supply missing semantic evidence.

Canonical return: [`Chapter 6 §§6.9–6.13`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 Provisional-Lock Evidence Boundary

Chapter 6 supplies methodological criteria, not empirical evidence. Its sixteen case constructions test distinctions and routing pressure but do not establish domain facts, actual causal relations, or completed `03_cases/*` coverage.

Evidence sufficient for citation may still be insufficient for structural mapping or source-result dependency. Missing sources may support `underdetermined` or `not testable with available sources` without licensing an invented Non-Event, causal story, or automatic `non_capture` route.

Canonical return: [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 7 Preparation — Record Evidence and Incompleteness Boundary

A Shared Transformation Record must distinguish the following source relations:

```text
record provenance
≠ transformation source basis
≠ individual evidence item
≠ Constitutive Source Trace
≠ source-result dependency
≠ proof
```

The record may be declaration-complete while sources remain epistemically incomplete. In that case it must preserve known gaps, underdetermination, rival transformations, limiting conditions, and the next permitted handoff rather than inventing precision.

The sixteen Chapter 7 case assignments are production duties only: `C7-REC-01`, `C7-REC-02`, `C7-SRC-01`, `C7-OP-01`, `C7-OP-02`, `C7-LOSS-01`, `C7-ALT-01`, `C7-ALT-02`, `C7-GOV-01`, `C7-STAT-01`, `C7-STAT-02`, `C7-DIAG-01`, `C7-CHAIN-01`, `C7-EXT-01`, `C7-EXT-02`, and `C7-NC-01`. They are not empirical evidence, populated case files, or completed Shared Transformation Records.

The eight existing smoke records remain synthetic formal fixtures. Their schema validity and routing coherence do not establish empirical or semantic adequacy.

---

## Chapter 7 WP1 Evidence and Support Map

The five WP1 cases are canonical methodological constructions, not empirical evidence or committed `03_cases/*` artifacts.

| Case | Tested burden | Support status at WP1 |
| --- | --- | --- |
| `C7-REC-01` | inspectable compact shared-record candidate | positive declaration example; substantive result remains source- and rule-dependent |
| `C7-REC-02` | syntactic completeness with generic trace | negative pressure; syntax cannot rescue load failure |
| `C7-SRC-01` | underdetermined source interval | explicit gap required; no invented `N1` |
| `C7-OP-01` | one occurrence and one operation kind | valid identity candidate; formation still substantively testable |
| `C7-OP-02` | collapsed `DECOMPOSE + PROJECT_AS` | `mandatory_stop` until occurrence separation |

Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record). Formal smoke records remain conformance fixtures rather than evidence of empirical adequacy.

---

## Chapter 7 WP2 Evidence and Record-Burden Route

| Record family | Evidence burden | Insufficient substitute |
| --- | --- | --- |
| Admissibility | claim-specific rule application, source relation, local finding, limitation, and audit-to-routing basis | completed fields or generic assertions |
| Loss | identified preserved/compressed/excluded/uncertain/irrecoverable items within declared scope | omitted categories or universal no-loss language |
| Alternatives | testable rival, no-transformation, non-translation, unresolved, or reasoned negative finding | empty lists treated as exhaustive search |
| Governance | explicit limits, prohibited inferences, authority ceiling, and separate external-warrant pointers | schema validity, routing permission, or analyst confidence |

Chapter 7 records evidence and limitation claims; it does not turn record syntax into substantive evidence.

---

## Chapter 7 WP3 Evidence and Routing-Burden Route

| Record question | Required support | Missing-support handling |
| --- | --- | --- |
| support status | claim-relative source basis and known gaps | provisional, contested, underdetermined, or unsupported status |
| resolution-test result | same-object comparison and declared resolution change | null if inapplicable; diagnostic finding if drift or escape |
| claim disposition | record lineage and split/revision relation | preserve prior claim without erasure |
| capture statement | captured structure, uncaptured structure, limiting condition, and re-entry | no automatic `non_capture` |
| routed result | substantive candidate assessment and boundary adjudication | exactly one canonical class per delimited claim |
| formal diagnostic | identified unresolved formal prerequisite and preserved available material | no canonical Output Class |
| chain | occurrence records, order, handoffs, local results, and losses | no inherited admissibility |
| extension | named control source and non-replacement assertion | Stop if used as shared-field bypass |

These are methodological support duties. They are not empirical evidence that any future domain claim is true.

---

## Chapter 7 WP4 Provisional-Lock Synchronization

Chapter 7 is provisionally locked after integrated ownership, redundancy, status, case-duty, prose-to-schema, link, schema, fingerprint, package, and roundtrip audit. The Shared Transformation Record records transformation claims without becoming the transformation, a truth proof, or an authority source. The existing record schema supplies lower-authority structural carriers; its Chapter-7 handoff annotation does not redefine canonical prose. The sixteen Chapter-7 case identifiers remain later production duties rather than completed evidence. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 8 Preparation Evidence and Counterclaim Boundary

A non-equivalence finding identifies a category or authority boundary. It does not by itself establish an empirical alternative.

```text
category-collapse flag
≠ evidence that the rival empirical claim is true
```

For Chapter 8 cases, the evidence map must distinguish:

- sources supporting each paired term’s actual use;
- sources supporting a declared relation across the pair;
- sources required for operation, continuity, or property testing;
- missing sources that leave analogy/projection or path/trajectory classification unresolved;
- formal conformance evidence that cannot supply semantic or application authority.

The Chapter 8 Preparation Record and its eighteen case assignments are production-control artifacts, not substantive evidence. No missing source may be converted into a non-event or a proof of identity collapse.

---

## Chapter 8 WP1 Evidence Boundary

WP1 distinguishes evidence for a relation from evidence for an identity claim.

```text
more observations
≠ evidence of higher truth

source presence
≠ evidence of lossless composition

finer components
≠ evidence of final constituents
```

A bounded comparative claim requires sources for the added distinction and its claim-specific effect. A relative-level claim requires a declared comparison axis and reference set. A composition requires source, selection, formation, and loss evidence. A decomposition requires same-reference continuity, source support, and a declared resolution. None of these source relations establishes ontology or authority.

---

## Chapter 8 WP2 Evidence Boundary

WP2 distinguishes evidence for ordered, traversed, sedimented, functional, and weighted relations.

```text
supported order
≠ evidence of actual traversal

actual traversal
≠ evidence of sedimentation

sedimentation
≠ evidence of path dependence automatically

functional resemblance
≠ evidence of operator identity

relative prominence
≠ evidence of grammar replacement
```

Every stronger claim requires its own source relation. Machine validity, repeated terminology, rhetorical importance, or recurrence of a label cannot replace the missing burden.

---

## Chapter 8 WP3 Evidence Boundary

WP3 distinguishes evidence of resemblance, dependency, recursive availability, formal consistency, and authority.

```text
source-supported resemblance
≠ source-result dependency

available next transformation
≠ evidence of complete capture

schema-valid record
≠ evidence of semantic truth

external warrant pointer
≠ inherited authority
```

A later projection, completeness, or application claim requires its own evidence and warrant. Repeated labels, technical success, auditability, or further operational availability cannot compensate for missing constitutive support.

---

## Chapter 8 WP4 Evidence and Case-Duty Boundary

Chapter 8 supplies internally audited methodological prose and later case assignments. It does not supply empirical evidence, calibration data, domain confirmation, or application warrants.

The eighteen `C8-*` identifiers are registered production duties. Their appearance in prose and Reference routing does not mean that `03_cases/*`, appendix stress tests, or external evidence have been produced.

The Decision-Tree handoff records explicit structural constraints only. Machine detection of a declared contradiction is not evidence that a natural-language identity collapse has been semantically established.

---

## Chapter 9 Preparation — Temporal Evidence Burdens

| Claim | Required source relation | Insufficient substitute | Explicit gap behavior |
| --- | --- | --- | --- |
| temporal position | timestamp, relative-order evidence, interval boundary, or warranted periodization basis | retrospective label alone | preserve precision and dispute status |
| order dependence | supported order plus claim-relevant consequence of order | document order or narrative sequence | retain chronology; reduce stronger claim |
| duration relevance | interval evidence plus changed praxis relation | duration count alone | mark open edges and uncertain thresholds |
| delay as transition structure | deferred relation and changed cost/expectation/alternative | elapsed time alone | preserve unresolved interval |
| delay as framed non-event | expected occurrence, expectation warrant, realization condition, non-realization | silence, absence of record, missing information | do not invent `Λ` |
| persistence | source-supported continuity across an interval | one stable snapshot | mark continuity as untested |
| bounded irreversibility | restoration criterion and residual difference/cost evidence | rhetorical “cannot go back” | bound claim or remain diagnostic |
| temporal recontextualization | later event/frame and changed legibility with earlier trace retained | later interpretation alone | preserve rival readings |
| transition | two configurations, temporal relation, change object, events/non-events, changed praxis conditions, residue | before/after pair or causal narrative | route to reduction, failure, diagnostic, or non-capture |

```text
source order
≠ historical order

missing information
≠ non-event

recorded endpoints
≠ transition trace
```

The `C9-*` assignments are future test obligations and not evidence items. Production control: [`Chapter 9 Preparation Record`](Chapter_9_Preparation_Record.md).

---

## Chapter 9 WP1 — Evidence and Uncertainty Burdens

| Finding | Evidence burden | Preserved uncertainty |
| --- | --- | --- |
| PATH scope | source-grounded temporal object or relation | no target function or operation inferred |
| `Θ` contribution | explicit temporal dimension and object occurrence relation | no automatic transition, trajectory, dependence, or cause |
| temporal position | contemporaneous or reconstructive source relation; frame and precision | disputed date, open interval, partial order, retrospective boundary |
| order dependence | supported actual order plus source-traceable change under material reorder | unrealized reorder is analytical sensitivity, not prediction |
| source/document order | source layout or record-production trace | historical order remains separately testable |

The five `C9-*` examples in WP1 are methodological pressure constructions, not empirical evidence or produced Case files. Canonical route: [`Chapter 9 §§9.1–9.4`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

---

## Chapter 9 WP2 — Evidence and Uncertainty Burdens

| Finding | Required source relation | Preserved uncertainty |
| --- | --- | --- |
| duration relevance | bounded interval plus traceable change in praxis load | internal variation and open endpoints |
| delay structure | supported deferred relation and altered alternatives/cost/binding | no invented expected occurrence |
| delayed non-event | warranted expectation and bounded non-realization condition | positive sub-events remain visible |
| persistence | source trace connecting the continuing relation across change | gaps prevent uninterrupted certainty |
| bounded irreversibility | criterion-specific residual difference or additional cost | other restoration criteria may differ |
| temporal recontextualization | later evidence/frame changes support of earlier claim | earlier occurrence and t1 reading retained |

The six `C9-*` examples are methodological pressure constructions, not empirical evidence or produced Case files.

---

## Chapter 9 WP3 — Evidence and Uncertainty Burdens

| Transition burden | Required evidence form | Controlled uncertainty behavior |
| --- | --- | --- |
| endpoint configurations | source-specific configuration reconstruction | endpoints may remain valid if relation fails |
| comparison basis | declared common dimension or explicit handoff | same label cannot substitute |
| temporal relation | exact, relative, partial, interval, or disputed order | preserve strongest supported order only |
| constitutive relation | source trace connecting events/non-events and changed/retained fields | diagnostic, reduction, failure, or non-capture where unresolved |
| intermediate structures | disclosure proportional to possible claim effect | known load-bearing gaps cannot be treated as empty |
| frame handoff | source/target frame, invariant, loss, scope | direct comparison withheld where absent |
| rival transitions | candidate-specific support and loss | `non_capture` only where rivalry remains responsibly undecidable |


## Chapter 9 Provisional-Lock Evidence Boundary

Chapter 9 pressure cases and audit results are methodological tests, not empirical evidence. A transition claim must keep four evidence relations distinct:

- endpoint support;
- temporal-order or interval support;
- constitutive relation support;
- praxis-relevance support.

```text
strong endpoints
≠ strong transition relation automatically

case representation
≠ external validation
```

The seventeen `C9-*` duties remain assigned for later case production. Canonical return: [`Chapter 9`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).

---

## Chapter 10 Preparation — Path Evidence Burdens

| Claim | Required source relation | Insufficient substitute | Explicit gap behavior |
| --- | --- | --- | --- |
| path | reconstructible components, actual traversal, constitutive connectedness, selection rule, frame, evidence, loss | chronology, endpoint, plausibility, or narrative coherence | retain chronology/sequence; reduce, diagnose, fail, or non-capture path claim |
| actual traversal | direct or traceable indirect evidence that the selected chain was realized | conceivable or institutionally typical route | expose inferential steps and rivals |
| path selection | source-linked relevance criterion plus inclusion/compression/exclusion record | analyst preference or endpoint hindsight | retain rival selections and loss |
| path frame | supported reference object, periodization, environments, scopes, coordinate compatibility | naturalized start/end boundary | mark bounded/provisional frame or diagnostic |
| blocked continuation | prior availability or preparation plus identifiable blocking condition | imagined possibility or missing record | refuse blocked status |
| aborted path | initiation/authorization/partial traversal plus cessation | never-started option | route to blocked/non-selected/unresolved status |
| deferred continuation | continued availability plus postponement and changed temporal load | indefinite silence or permanent non-realization | preserve delay and uncertainty separately |
| path comparison | comparable frame, span, granularity, selection, alternatives, evidence | endpoint label or universal distance | partial comparison or diagnostic |
| same endpoint/different path | endpoint similarity plus different costs, bindings, residue, or continuations | endpoint identity alone | preserve path-specific differences |
| weak dependence | valid path plus present-condition evidence and limited additional historical load | absence of historical records | retain path; separately test dependence |

```text
source abundance
≠ traversal proof

endpoint evidence
≠ path evidence

imagined possibility
≠ blocked continuation
```

The `C10-*` assignments are future test obligations and not evidence items. Production control: [`Chapter 10 Preparation Record`](Chapter_10_Preparation_Record.md).

---

## Chapter 10 WP1 — Path Evidence Relations

| Relation | Evidence burden | Preserved uncertainty |
| --- | --- | --- |
| component support | reconstructible configurations, transitions, events, non-events, branch notes | role may remain contextual rather than constitutive |
| traversal support | direct trace or explicit bounded inferential chain for actual passage | indirect bridge and gaps remain visible |
| constitutive support | claim-specific reason units form one path | complete causal mechanism not inferred |
| selection support | reasons for inclusion, compression, exclusion, and retained uncertainty | rival responsible selections remain possible |
| branch support | source-supported availability or preparation of non-realized continuation | blocked/aborted/deferred status remains deferred to §§10.8–10.10 |
| praxis support | warranted change in action corridor, expectation, cost, binding, asymmetry, alternative, or residue reconstruction | no authority inheritance |

```text
evidence quantity
≠ path admissibility
```

The six `C10-*` examples in WP1 are methodological pressure constructions, not empirical evidence or produced Case files. Canonical route: [`Chapter 10 §§10.1–10.6`](../01_blocks/02_part_i_path.md#chapter-10-path).

---

## Chapter 10 WP2 — Path-Status Evidence Burdens

| Status claim | Required evidence relation | Insufficient substitute | Preserved uncertainty |
| --- | --- | --- | --- |
| realized | traversal through the declared segment and cut | endpoint presence, narrative coherence, or later outcome | open continuation and mechanism uncertainty |
| blocked continuation | prior availability/preparation, blocking condition, temporal precedence, and prevention relation | imagined option, non-selection, missing record, or beneficiary | rival blocking roles and later repair |
| aborted path | initiation/authorization/partial traversal, cessation, and residue | never-started proposal or mere silence | exact cause, restart identity, and later effects |
| deferred continuation | postponement plus continued bounded availability/commitment | delay alone, missed date alone, or indefinite non-realization | future availability and later identity |
| status lineage | time-indexed records and continuity test across status change | final status used to rewrite earlier interval | earlier status, loss, and re-entry condition |

```text
strong realized-prefix evidence
≠ continuation-status proof
```

The five `C10-*` WP2 examples are methodological pressure constructions, not external evidence or produced Case files. Canonical route: [`Chapter 10 §§10.7–10.10`](../01_blocks/02_part_i_path.md#10-7-realized-path).

---

## Chapter 10 WP3 Evidence Duties

| Claim | Constitutive evidence | Insufficient substitute |
| --- | --- | --- |
| path comparison | aligned frame/reference/time/selection/source relation and dimension-specific support | endpoint similarity or source quantity alone |
| incomparability | documented material mismatch or undecidable rival alignment | analyst preference not to compare |
| same endpoint, different path | endpoint similarity plus source-supported differences in cost, binding, residue, or continuation | different narrative alone |
| path without strong dependence | warranted path plus present-condition and counterfactual assessment | mere existence of history |
| minimal record | resolvable path fields, evidence status, loss, lineage, and claim scope | field presence without substantive support |
| Stop | known failed load-bearing path plus continued stronger derivation | mere uncertainty in a non-load-bearing detail |
| Non-Capture | at least two source-responsible materially different path constructions and no adjudicating evidence | one strong and one speculative path |

Canonical route: [`Chapter 10 §§10.11–10.14`](../01_blocks/02_part_i_path.md#10-11-path-comparison).


## Chapter 10 Provisional-Lock Evidence Handoff

A warranted Path requires non-compensatory support across component, traversal, constitutive, selection, branch, and praxis relations. Qualified statuses add status-specific burdens: realized requires traversal through the cut; blocked requires prior availability plus prevention; aborted requires initiation or partial traversal plus cessation; deferred requires postponement plus continuing bounded availability.

Comparison requires explicit alignment or translation of reference, frame, temporal scope, granularity, selection, source basis, dimensions, and uncertainty. Missing information is not zero value, absence, open alternative, or non-event automatically.

```text
rich chronology ≠ traversal evidence
endpoint support ≠ Path support
strong realized-prefix evidence ≠ continuation-status proof
record completeness ≠ evidence sufficiency
```

Canonical return: [`Chapter 10`](../01_blocks/02_part_i_path.md#chapter-10-path).

---

## Chapter 11 Preparation — Trajectory Evidence Burdens

| Evidence relation | Control question |
| --- | --- |
| Path-substrate support | Is the referenced Path warranted under Chapter 10 and is its lineage intact? |
| sedimentation support | What repeated, cumulative, irreversible, or retained relation exceeds duration and recurrence? |
| continuity/carrier support | How does the historical load persist, transfer, or remain as residue? |
| present-load support | Which current configuration or continuation possibilities differ because of the Path history? |
| operator-profile support | Which bounded `Α`, `Ω`, `Ψ`, or `Λ` occurrences with `Θ` are constitutive? |
| directionality support | What dimension changes directionally without necessity, destiny, or original-plan inference? |
| boundary/compression support | Why are start, endpoint, periodization, inclusion, compression, and exclusion warranted? |
| competing-construction support | Which rival boundaries or constitutive selections remain plausible or undecidable? |

```text
evidence volume
≠ trajectory admissibility
```

Production control: [`Chapter 11 Preparation Record`](Chapter_11_Preparation_Record.md).

## Chapter 11 WP1 Evidence and Warrant Map

| Claim | Minimum evidence relation | Insufficient substitute | Bounded fallback |
| --- | --- | --- | --- |
| Trajectory candidate | warranted Path, declared present cut, historical carrier, cumulative/sedimented contribution, present praxis effect, source-result sensitivity | long duration, repeated label, event count, coherent narrative | warranted Path plus local temporal findings |
| warranted Trajectory | candidate plus applicable continuity, admissibility, loss, governance, Stop, and Non-Capture controls | complete record fields | `admissible_but_provisional`, reduction, Failure, Stop, or Non-Capture as applicable |
| Historical Sedimentation | source-supported carrier, retained/transformed load, persistent residue or cumulative change, present effect | archive survival, remembrance, age, repetition | duration, recurrence, persistence, or local residue claim |
| historical co-determination | material change in present reconstruction under relevant source variation | chronological priority or correlation alone | bounded historical relevance |
| directionality | dimension-specific ordered change with alternatives, repairs, reversals, and endpoint-bias control | progress/decline label, inferred plan, current endpoint | segment-specific or provisional directional claim |
| teleology rejection | preserved alternatives, contingencies, external conditions, and uncertainty about foresight | absence of explicit plan alone | claim reduction to source-supported directional relations |

WP1 cases `C11-DEF-01`, `C11-PATH-01`, `C11-DUR-01`, `C11-SED-01`, `C11-DIR-01`, and `C11-TEL-01` are canonical methodological pressure cases, not empirical evidence or completed case artifacts.

## Chapter 11 WP2 Evidence and Warrant Map

| Claim | Minimum evidence relation | Insufficient substitute | Bounded fallback |
| --- | --- | --- | --- |
| Attractor Sedimentation | bounded `Α` occurrence, recurrent/translated configurations, carrier, changed friction/default access, alternatives, repair/erosion, current-condition pressure | repetition count, popularity, current rule alone | recurrence, routine, current default, or provisional historical relevance |
| Asymmetry Accumulation | declared distribution dimensions, temporal carrier, repeated/cumulative differential load, present effect, exit conditions, repair/redistribution | one unequal outcome, role label, moral judgment | local Asymmetry occurrence or bounded current distribution claim |
| Binding Accumulation | commitment/reliance records, carrier, layered or transformed relation, present breach/reopening effect, weakening/transfer/release | number of promises, archival agreement, assumed consent | discrete Binding occurrence, reliance, or current switching-cost claim |
| Residual Accumulation | warranted expectations and windows, documented non-occurrences, residual carrier, present effect, repair/closure/dormancy, uncertainty | silence, source gap, later disappointment, count of absences | missing-information declaration, single bounded Non-Event, or unresolved expectation |
| Changed Action Corridor | declared corridor dimensions, distinct profile/current-condition contributions, source-result variation, remaining agency, repair/reopening | current constraint plus historical story, formal permission alone | bounded present accessibility/cost statement without historical attribution |
| multi-profile corridor | separately supported carriers and effects; absent/uncertain profiles declared | descriptive density or operator-symbol co-presence | narrower profile-specific claim or `claim_reduction_required` |

WP2 cases `C11-ATTR-01`, `C11-ASYM-01`, `C11-BIND-01`, `C11-RES-01`, and `C11-CORR-01` are canonical methodological pressure cases, not empirical evidence or completed case artifacts.

## Chapter 11 WP3 Evidence and Warrant Map

| Claim | Evidence / warrant required | Insufficient substitute | Preserved reduced finding |
| --- | --- | --- | --- |
| Trajectory Boundary | constitutive carrier, entry rationale, prehistory relation, segment lineage, analytical cut, terminal/open status, boundary sensitivity | oldest event, neat period, endpoint-selected beginning | bounded Path segment, prehistory, disputed periodization |
| Trajectory Compression | source-linked transitions, Non-Events, profiles, alternatives, reversals, repairs, current conditions, Loss and source-variation test | elegant macro-label, dense chronology, unchanged label under source change | reduced direction, Path, local profile, unresolved loss |
| competing construction | independent source basis, boundary, carrier, compression, claim scope, common comparison basis, source asymmetry | difference in wording, detail count, formal elegance | compatible bounded claims, incomparability, or unresolved rivalry |
| False Trajectory | identified failed burden and explicit preservation of weaker findings | label rejection alone or absence of complete history | chronology, duration, Path, recurrence, local profile, current constraint |
| Minimal Record sufficiency | complete Shared Record mapping plus substantive source support and admissibility judgment | valid YAML, filled fields, schema conformance | structurally complete but provisional or reduced claim |
| Non-Capture | materially different source-responsible constructions and insufficient adjudicative sources | analyst indecision, missing effort, or weak rivals | explicit unresolved construction set without validation |
| Mandatory Stop | known failed Trajectory used as premise for stronger dependence, function, causality, legitimacy, ranking, or authority | mere uncertainty with responsible re-entry still open | stop of stronger chain; earlier warranted weaker findings retained |

Canonical route: [`Chapter 11 §§11.10–11.14`](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary).

## Chapter 11 Provisional-Lock Evidence Handoff

| Evidence burden | Minimum support | Unsupported substitution |
| --- | --- | --- |
| Path substrate | individually warranted traversal lineage | chronology or retrospective plausibility |
| sedimentation carrier | identifiable occurrence, relation, record, practice, role, resource, rule, expectation, or residue carrier | operator symbol or historical importance label |
| cumulative relation | trace across time with disclosed gaps, repairs, reversals, and current conditions | duration, frequency, or monotonic narrative alone |
| present effect | changed praxis condition or continuation corridor at the analytical cut | remembrance or archival survival alone |
| profile claim | profile-specific historical and present evidence | cross-profile compensation |
| Boundary/periodization | entry rationale, prehistory, included segments, cut, terminal/open status | oldest event or source-window endpoint automatically |
| Compression | preserved constitutive trace plus canonical Loss | macro-label or source-insensitive summary |
| competing construction | independent source basis and common comparison dimensions | detail, formality, or breadth as superiority proof |

Chapter 12 may use this evidence package for a separate dependence test. It may not treat Chapter 11 lock as empirical confirmation.


---

## Chapter 12 Preparation Evidence Handoff

| Evidence burden | Minimum declaration | Unsupported substitution to reject |
| --- | --- | --- |
| input integrity | warranted Path/Trajectory reference, boundary, analytical cut, source status | macro-label or failed upstream object |
| current-state baseline | current rules, resources, roles, frame, constraints, alternatives, and explanatory reach | weak baseline constructed to make history look necessary |
| historical carrier | source-traceable retained relation and temporal linkage | historical story without present-bearing mechanism |
| present effect | changed meaning, cost, role, credibility, accessibility, reachability, or continuation | salience, drama, age, or repetition alone |
| omission test | material reconstruction loss when the relevant Path is removed | merely shorter or less vivid narrative |
| actual comparator | declared similarities, retained differences, source compatibility | treating two present objects as identical experiments |
| bounded alternative history | source-supported available or structurally comparable variation | free counterfactual storytelling or prediction |
| `Α + Θ` | repeated pattern plus changed current friction/default accessibility | current habit without historical trace |
| `Ω + Θ` | temporally accumulated differential distribution and current effect | present inequality alone |
| `Ψ + Θ` | concrete commitments/reliance plus retained breach/reopening load | inferred intention, morality, or permanent obligation |
| `Λ + Θ` | warranted expectation, bounded window, non-occurrence, residue, current effect | missing records or ordinary absence |
| modifier/reset | separate later occurrence and tested residual difference | new label, policy, frame, exit, or repair as automatic reset |
| non-determinism | retained alternatives and bounded cost/access changes | fate, inevitability, prediction, or impossibility claim |

The model may validate that these declarations exist. It cannot establish substantive historical indispensability, causal necessity, or real counterfactual possibility.

Production control: [`Chapter 12 Preparation Record`](Chapter_12_Preparation_Record.md).

## Chapter 12 WP1 Evidence Burdens

A Path-Dependence claim should identify:

- warranted Path/Trajectory input and lineage;
- present analytical cut;
- tested dependence dimension;
- relevant prior Path segment;
- source-supported historical carrier;
- current-state baseline and current-condition contribution;
- present effect with praxeological purchase;
- Source–Result Dependency under relevant source variation;
- omission, actual-comparator, or source-bounded comparison pressure;
- retained differences, uncertainty, canonical Loss, claim ceiling, Stop, and Non-Capture status.

Duration, repetition, institutional age, archive volume, narrative coherence, operator-symbol co-presence, or Record completeness are not sufficient evidence of historical indispensability.

## Chapter 12 WP2 Evidence Burdens

| Profile | Required evidence pressure | Common insufficiency |
| --- | --- | --- |
| `Α + Θ` | repeated configurations, retention/translation carrier, present friction/default difference, strongest current-only rival | recurrence count, current habit, broad attractor label, inferred inevitability |
| `Ω + Θ` | temporal distribution of cost/access/exposure/capacity, retained carrier, present differential, source-bounded redistribution pressure | one unequal outcome, current-only difference, person inference, severity without lineage |
| `Ψ + Θ` | concrete commitments, reliance or investment, retention/transfer/release trace, present reopening or coordination effect | atmosphere of expectation, current enforceability alone, moral-duty inference |
| `Λ + Θ` | expectation frame, realization window, warranted non-occurrence, retained residue, present effect, closure/repair test | missing record, mere absence, retrospective expectation, every delay treated as `Λ` |
| cross-profile | separate source traces, current effects, uncertainty, Loss, and local results | profile count, narrative richness, additive score, compensation for failed gate |

Formal completeness, symbol co-presence, and visualization do not prove substantive support.

## Chapter 12 WP3 Evidence and Comparison Burdens

| Test element | Required support | Common insufficiency |
| --- | --- | --- |
| recontextualization | source/target frames, occurrence, carrier before/after, current conditions | new label treated as reset or continuity proof |
| later modifier | distinct temporal occurrence, mechanism, pre/post effect, retained residue | operator symbol treated as automatic repair |
| Current-State Baseline | strongest current-only explanation using rules, resources, roles, infrastructure, frame, and alternatives | deliberately weak rival |
| Historical Omission | specific present reconstruction changed by omission | richer story only |
| Alternative History | actual comparator or source-supported bounded variation, declared similarities and differences | invented, unavailable, or non-comparable scenario |
| Non-Capture | materially rival explanations and explicit missing discriminator | preference disguised as uncertainty |

Visual richness, graph connectivity, schema completeness, and symbol density do not satisfy these burdens.

## Chapter 12 Provisional-Lock Evidence Handoff

A warranted dependence claim requires source support for the Path/Trajectory input, present analytical cut, tested dimension, current-state baseline, historical carrier, present effect, Source–Result Dependency, omission or comparison pressure, modifier status, uncertainty, and Claim Ceiling. Duration, repetition, operator symbols, profile richness, complete Records, model validity, or graphs are not evidence substitutes.

Chapter 13 must independently source historical availability and temporal windows for alternatives. Chapter 12 does not hand forward pre-validated branches or counterfactual outcomes.

Canonical return: [`Chapter 12 completion boundary`](../01_blocks/02_part_i_path.md#chapter-12-completion-boundary).

---

## Chapter 13 Preparation Evidence Handoff

| Alternative claim element | Required support | Insufficient substitute |
| --- | --- | --- |
| historical availability | contemporaneous records, plans, permissions, resources, actor statements, or reconstructible action corridors | later plausibility |
| temporal window | dated opportunity, deadline, phase, or condition interval | vague period narrative |
| rejection | explicit refusal or source-supported non-selection while available | mere non-realization |
| blockage | identifiable preventing structure | later failure or difficulty |
| initiation/abortion | action, commitment, resource use, role change, or implementation trace followed by interruption | intention alone |
| deferral | original window plus delayed status and changed conditions | later occurrence alone |
| loss | support for earlier reachability and later unavailability | current unattractiveness |
| counterfactual Path | documented branch point and bounded source variation | free storytelling |
| non-selection | active decision context, expectation, window, and consequence | missing information |

Evidence status must remain distinct from Output Class, claim disposition, and capture status.

## Chapter 13 WP1 Evidence Burdens

| Finding | Required source pressure |
| --- | --- |
| alternative space | contemporaneous practical reachability, not later imagination |
| Branch Point | plural distinct continuations within a bounded window |
| Realized Branch | actual entry/traversal trace, not announcement alone |
| Rejected Branch | refusal or non-selection while availability remained open |
| unsupported rival | explicit source ceiling; absence is not proof of impossibility |

Later outcomes may guide inquiry but do not automatically establish earlier availability.

## Chapter 13 WP2 Evidence Burdens

| Claim element | Required support | Insufficient substitute |
| --- | --- | --- |
| Blocked | prior availability/preparation plus an identifiable prevention relation in the declared window | mere non-realization or later statement that the option was impossible |
| Aborted | initiation, partial traversal, interruption, and bounded residual effect | plan, announcement, or unexecuted contract alone |
| Deferred | original availability, deferral trace, old/new window, intervening changes, and later candidacy/reachability | same label at a later date |
| Lost | earlier availability, later unavailability/material unreachability, and source-supported loss transition | present dislike, higher cost, or current unavailability alone |
| Continuity after gap | preserved reference, frame, resources, roles, bindings, and transition lineage to the claimed degree | retrospective narrative or brand/name continuity |
| Rejected versus blocked distinction | contemporaneous decision/refusal trace or prevention relation | conflicting uncorroborated recollection |

Where the sources support a candidate continuation but not its precise status, the claim must remain uncertain, reduce, or receive `non_capture` where the distinction is material.

## Chapter 13 WP3 Evidence Burdens

| WP3 object or claim | Required support | What remains unwarranted |
| --- | --- | --- |
| Counterfactual Path | contemporaneous branch availability, declared divergence, known constraints, bounded continuation support, source ceiling | unrealized success, full alternative future, prediction, causal necessity |
| Non-Selection | active decision architecture, bounded window, available continuations, non-selection trace, material consequence | hidden motive, guilt, automatic `Λ`, rejection or blockage without support |
| Alternative-Space Compression | source-supported branch field, materiality selection, five-part Loss, uncertainty | exhaustive historical openness, equal status of all visible branches |
| Alternative Status Record | source pointers per field, cut-specific status, later reachability, uncertainty | status truth from syntax or completeness |

The eight `C13-*` WP3 cases are methodological pressure constructions. They are not external evidence, produced Case files, calibration data, training data, graph specifications, or Reader implementations.

## Chapter 13 Provisional-Lock Evidence Boundary

Alternative claims require evidence at the historical cut: availability window, contemporary frame, actors or roles, resources, permissions, costs, constraints, selection or prevention trace, initiation where claimed, later-reachability or loss transition, and uncertainty. Later plausibility, current technical possibility, same naming, narrative coherence, record completeness, or graph rendering cannot substitute for contemporaneous support.

Counterfactual continuations stop at the source ceiling. Chapter 14 must independently establish expectation-grounded Non-Event status; Chapter 15 must independently establish `COMPOSE` warrant.

Canonical return: [`Chapter 13 completion boundary`](../01_blocks/02_part_i_path.md#chapter-13-completion-boundary).

## Chapter 14 Preparation Evidence Handoff

| Claim element | Required source support | Insufficient substitute |
| --- | --- | --- |
| expected occurrence | explicit identification of what was due or conditionally due | “something should have happened” |
| expectation relation | commitment, rule, schedule, role, recurrent procedure, adopted plan, trigger, or comparable source relation | analyst preference, hindsight, moral intuition |
| expectation frame | contemporaneous context in which the relation operated | later relabelling or unmarked frame shift |
| expected window | deadline, interval, recurrence window, trigger condition, or bounded sequence position | open-ended possibility |
| non-realization | source structure capable of establishing bounded non-occurrence | no record found, incomplete archive, silence in one channel |
| praxeological load | changed or preserved transitions, costs, roles, alternatives, bindings, residues, or corridors | mere nameability or narrative interest |
| Delay as `Λ` | missed warranted window plus material temporal load | postponement messages alone |
| repeated Non-Decision | renewed active decision windows plus repeated supported non-realization | long silence or repeated missing minutes |
| Blocked Responsibility | role architecture and positive blocking relation | person motive or inferred fault |
| Missing Repair | independently supported repair expectation and failed window | observed defect or desired remedy alone |
| Missing Exit | independently supported exit/release expectation and failed condition/window | formal exit availability or non-exit alone |
| sedimentation | warranted occurrence(s), persistence into later praxis, occurrence-boundary and alternative-construction support | repetition or duration alone |

Complete forms, graphs, or records do not substitute for these source burdens. Missing source must remain visible and may require reduction, Stop, or Non-Capture.

## Chapter 14 WP1 Evidence Burdens

| Finding | Required source pressure |
| --- | --- |
| expectation relation | commitment, rule, procedure, schedule, role relation, recurrent practice, plan, or triggered condition |
| expected window | historically valid bounded date, interval, recurring window, condition, sequence position, or phase threshold |
| non-realization | source bundle capable of establishing bounded non-occurrence at the claimed granularity |
| positive sub-events | event-level sources preserving activity inside the governing Non-Event interval |
| path-forming load | trace from missed occurrence to transition, configuration, alternatives, costs, roles, bindings, residue, or later meaning |
| Delay | original window, window status, positive postponement events, non-realization support, and accumulated load |

An incomplete archive may support an expectation claim while leaving occurrence status unresolved.

## Chapter 14 WP2 Evidence Burdens

| Finding | Required source pressure |
| --- | --- |
| repeated Non-Decision | recurring or renewed active decision contexts, expected disposition, window-level non-realization, continuity/change across contexts |
| blocked responsibility | role and authority map, dependency or referral relations, positive attempts, bounded failure to terminate |
| Missing Repair | independent repair commitment or trigger, completion condition, missed window, positive repair sub-events, residual carryover |
| Missing Exit | triggered or warranted release process, bounded condition, non-realization, practical continuation load |
| Non-Event Sedimentation | valid source `Λ`, occurrence boundaries, later carrier, changed costs/roles/alternatives/corridors, current-condition rival and uncertainty |
| profile interaction | separate occurrence support for each `Α`, `Ω`, `Ψ`, or `Λ` interaction; no fused or score-based inference |

Later residue does not retroactively establish an earlier expectation or non-realization.

## Chapter 14 WP3 Evidence Burdens

| Finding | Required source pressure |
| --- | --- |
| preservation through composition | expectation/frame/window/non-realization source chain, positive sub-events, occurrence boundaries, affected roles/alternatives, residue, uncertainty, Loss |
| False Non-Event | explicit identification of the missing or failed constitutive burden |
| open-window status | current window or realization condition, pending checkpoints, absence of premature failure claim |
| complete Non-Event extension | owner pointer, source support, uncertainty, claim scope, output mapping, non-replacement of top-level fields |
| reduction | distinction between supported expectation, unresolved occurrence status, supported later occurrences, and sedimentation carrier |
| Stop | evidence that unsupported `Λ` is being reused for blame, sanction, authority, prediction, operation, or function |
| Non-Capture | source-supported materiality plus unresolved alternatives that cannot be responsibly separated |

Missing records, graph gaps, or complete syntax never substitute for non-realization evidence.

## Chapter 14 Provisional-Lock Evidence Boundary

A Non-Event claim requires independent support for the expected occurrence, expectation relation, expectation frame, expected window or condition, relevant granularity, and non-realization. Positive sub-events, source coverage, alternative forums, later realization, changed roles, costs, residue, and uncertainty must be recorded where material.

Missing records, ordinary silence, retrospective desirability, same-label continuity, later residue, graph gaps, and machine-readable completeness cannot substitute for non-realization support. Person motive, blame, duty, coercion, and legitimacy require independent sources and remain outside Chapter 14's authority.

Canonical return: [`Chapter 14 completion boundary`](../01_blocks/02_part_i_path.md#chapter-14-completion-boundary).

## Chapter 15 Preparation Evidence Handoff

A composition claim requires source support at several distinct layers:

1. source-object identity and typing;
2. source-frame and temporal/structural scope;
3. ordering relation;
4. selection and omission rationale;
5. formation and constitutive relations;
6. preservation and all five Loss fields;
7. target-object class and claim scope;
8. counterfactual-sensitivity result;
9. rival composition or no-composition pressure;
10. uncertainty and Claim Ceiling.

Later sources may support retrospective periodization but may not be used silently to invent earlier order, availability, or constitutive relation. Missing material remains uncertainty or source limitation, not convenient exclusion.

## Chapter 15 WP1 Evidence Handoff

A WP1 COMPOSE candidate requires evidence routing for:

- source identity and origin typing;
- source lineage and inherited uncertainty/Loss;
- source-domain search and inaccessible material;
- inclusion and omission reasons;
- temporal or structural ordering;
- frame, scope, granularity, and relative level;
- expected praxis difference;
- rival selection, rival frame, or no-composition option.

Source abundance does not establish a common relation. Later sources may assist bounded periodization but may not be back-projected to manufacture earlier order, availability, or source identity.

Graph edges and layout are representations of supported relations, not independent evidence.

## Chapter 15 WP2 Evidence Handoff

A formation-and-Loss claim should expose:

- source identifiers, origin types, frames, levels, granularity, lineage, and inherited uncertainty;
- the Formation Rule and each claimed constitutive relation;
- target-object class, boundary, and new praxeological discrimination;
- preserved load and the carrier through which it remains reconstructible;
- compression rule and external recoverability;
- excluded material, source-domain status, reason, contestability, and rival-frame relevance;
- uncertain material and its effect on order, relation, boundary, or claim;
- irrecoverable material, its source-inherited or composition-induced origin, and target materiality;
- the complete five-part Loss structure;
- rival formation or no-composition pressure.

A complete source bundle, record, or graph does not decide formation, Loss adequacy, or target truth.

## Chapter 15 WP3 Evidence Handoff

Evidence duties include target and claim identity, source-to-claim trace, class-specific threshold support, bounded sensitivity variations, material effects of removal or exchange, failure-burden localization, rival and no-composition support, complete Loss, and explicit ceilings.

No source volume, graph density, record completeness, or sensitivity result can establish causal necessity, target function, person judgment, sanction, prediction, or higher authority.

## Chapter 15 Provisional-Lock Evidence Boundary

A `COMPOSE` claim requires source-specific support for typing, selection, ordering, frame, Formation Rule, constitutive relations, target boundary, preservation, compression, exclusion, uncertainty, irrecoverability, sensitivity, alternatives, and Claim Ceiling. The weakest load-bearing source or relation limits the claim.

No archive size, graph density, visual continuity, macro-label, target stability, schema validity, or package success establishes substantive formation, causal necessity, target function, person judgment, sanction, legitimacy, prediction, or authority.

Canonical return: [`Chapter 15 completion boundary`](../01_blocks/02_part_i_path.md#chapter-15-completion-boundary).

## Chapter 16 Preparation Evidence Handoff

A PATH boundary claim should expose evidence for:

- the tested temporal claim and target class;
- source configurations, transitions, order, frame, and periodization;
- material effects of added or removed temporal differentiation;
- turning points, reversals, alternatives, `Λ`, `Ω`, bindings, and residuals where constitutive;
- Selection Rule, Formation Rule, compression rule, and complete Loss where `COMPOSE` is used;
- Counterfactual Sensitivity to removal, reorder, substitution, recompression, and reframing;
- uncertainty, inaccessible sources, and Claim Ceiling.

Dates, citations, visual continuity, archive size, long duration, a complete record, or a stable macro-label do not independently establish Purchase or Trace. Missing source support must remain missing information or uncertainty rather than be converted into a boundary pass or teleological narrative.

## Chapter 16 WP1 Evidence Handoff

A lower-bound finding requires evidence that temporal differentiation changes a claim-relevant reconstruction, not merely that more dates or intervals exist.

An upper-bound finding requires source-to-result dependency for the target boundary and strength claim, including where material:

- configurations and transitions;
- order and turning points;
- `Λ`, `Ω`, bindings, alternatives, reversals, repair, and residuals;
- present-bearing historical load;
- Selection Rule, Formation Rule, compression, exclusion, uncertainty, and irrecoverability;
- bounded removal, reorder, and rival-periodization pressure.

Citations, graph edges, animation, macro-nodes, or stable labels are representational aids. They are not independent evidence of purchase, traceability, Trajectory, or boundary passage.

## Chapter 16 WP2 Evidence Handoff

Directionality requires source support for the claimed dimension, ordering relations, turning points, reversals, alternatives, parallel subpaths, periodization, and later load. Teleology testing requires endpoint-independent Selection Rule pressure and preservation of source-supported alternatives.

Omission testing requires:

- for `Λ`: expected occurrence, expectation relation/frame/window, non-realization support, positive sub-events, later carrier, uncertainty;
- for `Ω`: unequal access, exposure, cost, reversibility, fallback, repair, evidence, coordination, or binding load.

A later `PROJECT_AS` or `DECOMPOSE` requires a new operation record. Reader layout, graph expansion, narrative utility, repeated labels, or data volume are not independent evidence of operation success or historical warrant.

## Chapter 16 WP3 Evidence Handoff

| WP3 duty | Required evidence form | Insufficient substitute |
| --- | --- | --- |
| Purchase | baseline plus source-to-difference account for the tested praxis dimension | dates, duration, visual density, narrative interest |
| Trace | typed source lineage, order, constitutive relation, Loss, and sensitivity | citation count or schema completion |
| Provisionality | localized uncertainty and retained rival orders with bounded target stability | softened wording around an unreduced failed claim |
| Reduction | explicit failed claim and surviving source/target route | silent relabeling |
| Mandatory Stop | documented failure plus prohibited continued use | generic caution language |
| Non-Capture | bounded tests showing irreducible traces or periodizations | missing data alone |

The Chapter-16 cases remain methodological pressure tests and are not standalone evidence artifacts.

## Chapter 16 Provisional-Lock Evidence Boundary

A PATH boundary claim requires evidence pointers for the temporal input, target claim, praxis baseline, changed dimension, typed sources, lineage, order or Partial Order, constitutive relations, preserved `Λ`/`Ω`/branch/binding/repair/residual load, Selection and Formation Rules where relevant, complete Loss, sensitivity results, and uncertainty.

Evidence density does not replace source-to-result dependency. A clean graph, many citations, formal completeness, or stable label cannot establish purchase, trace, directionality, teleology, omission, target class, or Output Class.

Chapter-16 Pressure Cases remain methodological tests rather than empirical evidence or produced `03_cases/*` records.

## Chapter 17 Preparation Evidence Handoff

Chapter 17 separates four evidentiary layers:

1. source materials and lineage used inside a case;
2. chapter-level Pressure Cases as methodological seeds;
3. instantiated Markdown/YAML case artifacts;
4. local audit and canonical output mapping.

A Pressure Case ID is not evidence that a standalone case exists. A schema-valid case record is not evidence that its substantive interpretation is correct. The Chapter-17 local audit must cite actual artifact paths and source pointers.

## Chapter 17 WP1 Case Evidence Status

The three WP1 case packets are synthetic declarations used to test STRATA discrimination, record completeness, Loss, alternatives, audit, and mapping.

```text
synthetic case packet
= internal method support
≠ external empirical evidence
≠ domain calibration
```

Every source item declares provenance, affected claim component, support mode, evidence availability, temporal and reference scope, uncertainty/provenance limit, and warrant route. All broader empirical, causal, functional, normative, person, and authority claims remain outside the case ceiling.

## Chapter 17 WP2-A Case Evidence Status

Both WP2-A cases use synthetic declarations solely to test STRATA discrimination and record architecture. Their schema validity and local audit do not constitute empirical calibration. Historical indispensability and current-state sufficiency remain substantive, reasoned case findings rather than automatic model outputs.

## Chapter 17 WP2-B Case Evidence Status

The WP2-B records use synthetic declarations solely for method discrimination. Schema validity confirms record conformance, not the substantive correctness of a chronology reduction, source-indifference finding, or teleology finding. Those remain reasoned case judgments under the declared packet.


## Chapter 17 WP2-C Evidence Routing

- `C17-OMEGA-01` requires direct synthetic support for unequal access, exposure, exit, and repair load; shared milestone labels alone are insufficient.
- `C17-FALSEL-01` records absence of a review record as a source gap. Without an expectation frame and expected window, the gap does not route as `Λ` evidence.
- Both records remain internal method tests and supply no external warrant.


## Chapter 17 WP3-A Evidence Boundary

The three confusion cases use synthetic declarations to test operation and type discrimination. Their schema validity and source trace establish artifact consistency only. They do not establish an actual Frame-function, Attractor-function, universal resolution neutrality, causal mechanism, empirical truth, person judgment, or application authority.


## Chapter 17 WP3-B Evidence and Artifact Coverage

Evidence coverage consists of thirteen Markdown reconstructions, thirteen schema-valid YAML records, complete five-part Loss, alternatives, twelve record-audit stages each, synchronized indices, and the twenty-control chapter audit. Artifact completeness supports lock readiness; it does not establish empirical truth, causal sufficiency, or universal PATH validity.

## Part I — PATH Provisional-Lock Evidence Boundary

Lock evidence consists of canonical prose, Chapter Contracts, thirteen Markdown reconstructions, thirteen schema-valid records, complete record audits, the twenty-control chapter audit, synchronized indices/references/model mirrors, and package integrity. This evidence supports internal methodological closure only; it does not establish empirical truth, causal necessity, universal PATH validity, or application authority.

## Chapter 18 Preparation — Compressed-Object Source Burden

A Chapter-18 source declaration must distinguish evidence for the coarse object from evidence for its internal reconstruction.

| Support object | Minimum burden |
|---|---|
| source reference | stable identity and lineage |
| origin/source type | explicit typing without operator-type decomposition |
| known internal structure | directly supported distinctions only |
| unresolved internal structure | bounded unknowns, not populated hypotheses |
| decomposition reason | expected claim-relevant difference and source route |
| current/coarser function | source-supported claim under test |

```text
coarse-object evidence
≠ evidence for hidden components

warrant to test decomposition
≠ warrant for a particular internal result
```

Where sources cannot support relations among finer candidates, the correct route may be no decomposition, Claim Reduction, Stop, or Non-Capture rather than speculative completion.

## Chapter 18 WP1 — Source-Candidate Evidence Boundary

WP1 separates evidence for the current source object from evidence for a later internal reconstruction.

| WP1 claim | Minimum support | Not established |
|---|---|---|
| identifiable compressed source candidate | stable reference, lineage, source-side category and typing, bounded coordinates | target granularity or component set |
| provisional elementarity | current claim sufficiency or bounded source/relevance stop | absolute indivisibility |
| known internal structure | directly supported current distinctions | complete internal constitution |
| unresolved internal structure | bounded question tied to a possible claim difference | a populated hidden model |
| operator-typed occurrence eligibility | concrete reference and source-supported occurrence typing | admissible `DECOMPOSE` |
| Path/Trajectory/Non-Event/composite eligibility | retained identity, prior Loss, scope, and current function | inherited operation success or finer truth |

```text
evidence for the coarse source object
≠ evidence for a particular finer reconstruction

source-side question
≠ source-supported answer
```

The WP1 chapter cases are methodological pressure tests, not empirical evidence or produced standalone case artifacts.



## Chapter 18 WP2 — Evidence Duties for Compression Decisions

| Decision pressure | Minimum evidence duty | Evidence does not authorize |
|---|---|---|
| necessary compression | source-bounded coarse relation and claim sufficiency | absolute simplicity or final closure |
| compression insufficiency | identifiable source-supported internal distinction with material claim effect | hidden components by inference from complexity |
| reason to decompose | plausible source route for distinctions and their relation to the source object | target granularity or successful operation |
| counterexample pressure | direct support for the counterexample and its scope | a complete finer model without additional sources |
| no praxeological purchase | absence of a specified material change under the proposed distinction | universal irrelevance of the detail |
| source insufficiency | documented source gap for the proposed components or relations | conversion of missing information into positive content or `Λ` |

WP2 preserves the rule that component evidence without relation evidence is insufficient for a complete later decomposition. Canonical source: [Chapter 18 §§18.5–18.8](../01_blocks/03_part_ii_sub.md#18-5-why-compression-is-necessary).


## Chapter 18 WP3 Evidence Handoff

A Chapter-18 source declaration must retain evidence for:

- occurrence or composite identity;
- source Frame, granularity, relative level, and current function;
- already warranted internal distinctions;
- bounded unresolved relations and inaccessible areas;
- the source route supporting a proposed finer test;
- inherited uncertainty, exclusions, and irrecoverability;
- rival source-supported internal models where present.

The evidence layer must not populate hidden components from an operator label, treat missing records as positive Event or Non-Event content, or infer source-function survival. Chapter 19 and Chapter 20 receive the declared evidence burden without inheriting success.

Canonical site: [Minimal Source Declaration](../01_blocks/03_part_ii_sub.md#18-10-minimal-source-declaration).


## Chapter 18 Provisional-Lock Evidence Boundary

Chapter 18 requires a traceable route from the declared source object to the reason for testing finer resolution. Evidence may support source identity, current/coarser function, known distinctions, unresolved relations, and bounded rival internal models. It may not be converted automatically into components, target granularity, operation success, or a source-function result.

The Chapter-19 handoff carries evidence obligations forward without inheriting passage. Primary site: [Minimal Source Declaration](../01_blocks/03_part_ii_sub.md#18-10-minimal-source-declaration).

## Chapter 19 Preparation — Granularity and Comparability Source Burden

A target granularity requires more than a plausible finer vocabulary. The source burden includes:

- traceable source and target reference relation;
- source-supported candidate distinction family;
- declared source and target Frames;
- aligned temporal and source scopes;
- expected praxeological difference stated before analysis;
- translation or alignment rationale for comparison;
- explicit gaps, exclusions, and irrecoverable detail;
- competing finer models where sources permit more than one partition.

The source map must not infer components from the coarse type, infer reference preservation from matching labels, or treat data volume as support. Incomparability is a bounded source-and-coordinate finding, not evidence that incompatible local claims are equally warranted.

## Chapter 19 WP1 Canonical Evidence Burden

A WP1 granularity proposal must keep traceable:

- the bounded source reference;
- the source distinction set;
- the proposed target distinction family without treating it as discovered;
- the comparison dimension along which the target is finer;
- the source and target Frame status;
- the relative-level status;
- the bounded temporal and source scope;
- the expected praxeological difference declared before finer reconstruction;
- prior uncertainty, Loss, Stop, failure, and Non-Capture.

Matching labels do not prove reference or Frame continuity. More quotations or timestamps do not prove a changed distinction set. WP1 evidence can support a coherent proposal and source route; it cannot by itself establish actual components, target relations, operation success, source-function effect, or truth gain.

Primary sites: [§19.1–§19.4](../01_blocks/03_part_ii_sub.md#19-1-granularity-change).

## Chapter 19 WP2 Canonical Evidence Burden

For each proposed distinction or component candidate, the evidence map must preserve:

- relation to the bounded source reference;
- direct source support or a bounded source route;
- the coarse function or claim under pressure;
- the praxeological dimension that could change;
- relation to other proposed candidates;
- whether the candidate is local, temporal, relational, role-distributed, institutionally distributed, or recurrent;
- uncertainty, rival partitions, exclusions, and inaccessible relations;
- whether the candidate is proposed as carrying, disturbing, or replaceable.

Source authenticity alone does not establish component status. Evidence for participation does not establish necessity, sufficiency, causal priority, or final constituent status. WP2 evidence supports candidate eligibility only; actual component reconstruction and source-function effect remain Chapter-20 burdens.

Primary sites: [§19.5–§19.7](../01_blocks/03_part_ii_sub.md#19-5-change-of-distinction-set).

## Chapter 19 WP3 Evidence Return

WP3 uses the continuing bounded review-arrangement illustration to test:

- aligned interactional and procedural reconstructions under declared translation (`C19-COMPARE-01`);
- positive incomparability between a single-meeting decision claim and a year-level delivery-performance aggregate (`C19-INCOMP-01`);
- documented procedural closure versus unresolved interactional repair as compatible predicates (`C19-MISMATCH-01`);
- final decision authority affirmed and denied under aligned predicate and sources as substantive contradiction (`C19-CONFLICT-01`);
- source-supported but claim-neutral utterance details without premature resolution classification (`C19-LOWER-01`);
- an exact populated Minimal Granularity Relation without component or operation-result claims (`C19-MINREL-01`).

These are methodological pressure illustrations, not empirical findings or completed `03_cases/*` artifacts. Primary sites: [§19.8–§19.11](../01_blocks/03_part_ii_sub.md#19-8-granularity-comparability).


## Chapter 19 Provisional-Lock Evidence Boundary

Chapter 19 requires traceable support for the source reference, proposed distinction-set change, Frame and temporal relation, expected praxeological difference, and comparison basis. Evidence may support coordinate plausibility and bounded candidate relations. It may not be converted automatically into actual components, component relations, semantic comparability, source-function survival, operation success, or a resolution outcome.

The Chapter-20 handoff carries these obligations forward without inheriting passage. Primary site: [Minimal Granularity Relation](../01_blocks/03_part_ii_sub.md#19-11-minimal-granularity-relation).

## Chapter 20 Preparation Evidence Roles

The finer reconstruction must distinguish:

| Evidence role | Permitted use | Prohibited inference |
| --- | --- | --- |
| direct support | support a component, relation, timing, or source-function effect | completeness or causality automatically |
| indirect reconstruction | bounded inference with explicit bridge | direct observation |
| uncertain attribution | retain a candidate with uncertainty | established component status |
| missing intermediate structure | mark a gap and limit claim | fill the gap from the coarse type |
| rival internal model | preserve a supported alternative | forced single-model adjudication |
| inaccessible area | justify bounded underdetermination, Stop, or Non-Capture | weak-claim protection |
| unsupported inference | route to failure, reduction, or Stop | retain as finding because it is plausible |

Preparation control: [`Chapter_20_Preparation_Record.md`](Chapter_20_Preparation_Record.md). This record is production evidence only, not empirical support for a decomposition.

## Chapter 20 WP1 Evidence Return

WP1 uses the continuing review-arrangement illustration to pressure:

- relational reconstruction rather than generic detail (`C20-DEF-01`);
- a failed source-route precondition for a proposed Trajectory opening (`C20-PRE-01`);
- independently identifiable source identity and current function under test (`C20-SRC-01`);
- a question with explicit source route, no-gain, and Stop (`C20-Q-01`);
- additional quotations and narrative without changed distinctions (`C20-DESC-01`);
- invalid decomposition of `□` corrected to a Frame-typed occurrence question (`C20-TYPE-01`).

These are methodological pressure illustrations, not empirical findings or completed `03_cases/*` artifacts. Actual source-support classification begins in WP2.

## Chapter 20 WP2 Evidence Return

WP2 adds a role-sensitive source map for finer reconstruction:

```text
direct support
indirect reconstruction
uncertain attribution
missing intermediate structure
rival internal model
inaccessible area
unsupported inference
```

These roles do not form a score or truth rank. The same source may directly support one claim and be insufficient for another. Rival models remain open until source changes distinguish them or a bounded unresolved result is required.

Primary site: [§20.6](../01_blocks/03_part_ii_sub.md#20-6-source-support).

## Chapter 20 WP3 Evidence and Result Return

Evidence must support not only components and relations but also any selected source-function effect. Rejection requires source-supported contradiction or insufficiency relative to the tested function; underdetermination preserves missing intermediates and rival models; confirmation does not increase authority.

Failure preserves weaker supported observations. Mandatory Stop preserves the valid earlier segment. Non-Capture preserves known endpoints, inaccessible intervals, and rivals without asserting that all rivals are true.

Primary sites: [§20.9](../01_blocks/03_part_ii_sub.md#20-9-preservation-of-source-function) and [§20.12](../01_blocks/03_part_ii_sub.md#20-12-decomposition-failure).

## Chapter 20 WP4 Evidence-Lock Return

The provisionally locked procedure requires claim-specific evidence for source identity, component existence, relation claims, temporal order, uncertainty, source-function effect, and Loss. Evidence for one layer does not transfer automatically to another. Missing support may yield claim reduction, Mandatory Stop, failed transformation, or Non-Capture; record completeness does not repair the evidence gap.

Primary site: [Chapter-20 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-20-completion-boundary).

## Chapter 21 Preparation Evidence Route

Occurrence-family evidence must support the concrete source typing and its production/maintenance conditions separately. Evidence that a review boundary exists does not automatically support every proposed maintenance mechanism; repeated behavior does not automatically support Attractor load; local gradients do not automatically support coordinated macro-asymmetry; commitment language does not automatically support person-level Binding.

Rival typings and disturbing components remain visible. Finer evidence may confirm, differentiate, partially preserve, reject, or leave the occurrence typing underdetermined.

Preparation control: [Chapter 21 Preparation Record](Chapter_21_Preparation_Record.md).

## Chapter 21 WP1 Evidence Return

The R-17 continuity example uses agenda, transcript, minutes, closure notice, and follow-up material to support a bounded occurrence-level reconstruction of admission, qualification, closure, routing, revisit-window, and Non-Reopening relations. The evidence does not establish motives, person properties, universal institutional practice, legitimacy, or constituents of `□`.

WP1 preserves direct support, uncertainty about informal access and notice uptake, inaccessible participant interpretation, and counterevidence capable of pressuring the Frame typing.

Primary sites: [§21.2–§21.4](../01_blocks/03_part_ii_sub.md#21-2-frame-typed-occurrence).

## Chapter 21 WP2 Evidence Return

The Attractor-family example is explicitly bounded to a declared review-series source route of dated agendas, routing logs, closure notices, follow-up requests, and reopening records. It supports only those recurrence, friction, expectation, alternative, threshold, and exit relations traceable to the declared material.

The R-17 Asymmetry return uses agenda, transcript, minutes, notice, closure, and follow-up records to distinguish role authority, approval capacity, notice access, time-window knowledge, follow-up activation capacity, burden, and exit gradients. It does not establish total person rank, motive, legitimacy, universal institutional structure, or macro-Asymmetry beyond the reference object.

Primary sites: [§21.5–§21.9](../01_blocks/03_part_ii_sub.md#21-5-attractor-typed-occurrence).

## Chapter 21 WP3 Evidence Return

Impulse-occurrence evidence may support activating differences, directing Frames, Non-Events, thresholds, attenuation, and changed continuation corridors; it does not establish motive automatically. Binding-occurrence evidence may support commitments, rules, records, continuity, revision conditions, dependencies, and breach/exit costs; it does not establish equal endorsement, legitimacy, or person identity. Missing support remains visible through Failure, Stop, or Non-Capture rather than inferred completion.

## Chapter 21 WP4 Evidence Lock

The five family applications are provisionally locked as methodological evidence architectures, not as external empirical findings. Frame evidence must support selection and boundary practices; Attractor evidence differential continuation; Asymmetry evidence declared gradients and coordination; Impulse evidence structural activation without motive inference; Binding evidence commitments and load distribution without person conversion. Rival typings, missing support, counterevidence, and underdetermination remain effective.

## Chapter 22 Preparation Evidence Routing

Composite decomposition requires evidence for:

- source composite identity and boundary;
- constituents and constitutive relations;
- prior composition trace and inherited Loss where available;
- component role and counterpressure;
- distributed coordination rather than aggregation;
- redundancy and substitution conditions;
- internal conflict and possible outcome;
- stability mechanism and temporal scope;
- operator-weighting or modulation carrier;
- source-function effect and unresolved structure.

Source volume cannot substitute for relation evidence. A coherent map may guide search but remains a rival model until the sources support the component roles and relations claimed.

Preparation control: [Chapter 22 Preparation Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP1 Evidence Return

The bounded R-17C review-governance anchor uses documented admission, approval, closure, routing, reconsideration, and Non-Reopening structures to prepare a source-supported composite-entry and internal-map claim. The evidence supports neither a complete formation history nor universal institutional causality, legitimacy, person properties, numerical operator strength, or a target function.

WP1 preserves uncertainty about informal pre-agenda coordination, notice uptake, excluded alternatives, and the exact boundary of the reconsideration route. These uncertainties remain effective against stronger role, map, and weighting claims.

Primary sites: [§§22.1–22.4](../01_blocks/03_part_ii_sub.md#chapter-22-decomposing-composite-structures).

## Chapter 22 WP2 Evidence Return

The bounded R-17C anchor routes profile claims through notice timing, revisit-window dates, record availability, follow-up correspondence, and procedural access records. Distributed-function claims require the documented chain among notice, record access, request routing, independent reconsideration, and status return. Redundancy and substitution remain function-specific and retain changed delay, access, auditability, burden, and Loss. Conflict claims preserve rival readings of closure finality, reconsideration access, residual objection, and asymmetric control.

The current evidence does not establish numerical burden, universal resilience, complete informal-route coverage, carrier equivalence, causal necessity, legitimacy, person properties, or a contextual target function.

Primary sites: [§§22.5–22.8](../01_blocks/03_part_ii_sub.md#22-5-modulating-profiles).

## Chapter 22 WP3 Evidence Return

The bounded R-17C anchor uses continuity of admission, approval, routing, reconsideration, status-return, replacement carriers, temporal windows, and repeated Non-Reopening to test composite stability. Evidence remains differentiated among stable output, stable relations, accessible repair, unequal burden, residual objection, and label persistence.

The current evidence supports a bounded relational decomposition and an internally differentiated Source-Function Effect. It does not establish homogeneous access, equal load, universal resilience, legitimacy, complete formation history, person properties, or a contextual target function.

Primary sites: [§§22.9–22.11](../01_blocks/03_part_ii_sub.md#22-9-composite-stability).

## Chapter 22 WP4 Evidence Lock

Chapter 22 is provisionally locked as a methodological evidence architecture, not as an empirical finding that any named system is composite, stable, distributed, redundant, or causally organized. Constituent, relation, role, weighting, profile, coordination, substitution, conflict, stability, and Loss claims each retain their own Source Route, counterpressure, uncertainty, and Claim Ceiling. Co-presence, labels, repeated function, and formal maps remain insufficient by themselves.

## Chapter 23 Preparation Evidence Routing

Temporal decomposition requires evidence for:

- source Event-like or Non-Event identity;
- Event beginning, completion, contextual margins, and rival boundaries;
- internal phases, positive sub-events, thresholds, and role shifts;
- relation among sequence, overlap, interruption, delay, and closure;
- expectation Frame and expected window for Non-Event claims;
- documented non-realization distinct from missing records;
- delay mechanism distinct from intention;
- repeated non-decision and absent binding occurrence;
- categorical preservation or revision;
- temporal drift, unresolved structure, and canonical Loss.

Timestamp volume cannot substitute for event-unit relevance or relation evidence. Record absence cannot substitute for expectation and non-realization evidence.

Preparation control: [Chapter 23 Preparation Record](Chapter_23_Preparation_Record.md).

## Chapter 23 WP1 Event Evidence Routing

Event-side temporal decomposition requires separately traceable support for:

- source Event-like occurrence and praxis-relevant change;
- governing Frame and coarse boundary;
- beginning and completion criteria;
- contextual predecessors and aftermath;
- phases, thresholds, role shifts, interruptions, resumptions, and completion relations;
- local Event identities and cluster relation where claimed;
- rival boundaries and category counterpressure;
- duplicated records versus distinct Events;
- Event-unit relevance and the Event-Inflation stop point.

Timestamp quantity, recording-system multiplicity, document versions, or fine sensor resolution cannot substitute for Event relevance or relation evidence. Primary sites: [§§23.1–23.4](../01_blocks/03_part_ii_sub.md#23-1-event-decomposition).

## Chapter 23 WP2 Non-Event Evidence Routing

Non-Event decomposition requires separately traceable support for:

- the expected structure and its governing Frame;
- the expected window, deadline, trigger, or completion condition;
- non-realization within that boundary;
- the praxis difference produced by non-realization;
- positive sub-events and their relation to production, stabilization, deferral, fragmentation, or failure to overcome `Λ`;
- delay mechanisms, role and authority conditions, thresholds, and dependencies;
- later realization and its non-erasure relation to the earlier window;
- repeated decision opportunities and candidate temporal categories;
- the occurrence capable of creating binding closure;
- source gaps and rival explanations.

Archive silence, record gaps, elapsed duration, structural benefit, or repeated role transfer cannot substitute for expectation, non-realization, intention, causal, person, or binding evidence. Primary sites: [§§23.5–23.8](../01_blocks/03_part_ii_sub.md#23-5-non-event-decomposition).



## Chapter 23 WP3 Evidence Burdens

Internal temporal order requires evidence for relations, not only dates. Partial order and overlap require supported dependency or concurrency; multiple clocks require separately supported timing claims; interruption/resumption requires reference continuity; temporal drift requires a no-difference finding against the declared praxis claim. Event/Non-Event category revision requires expectation, realization, boundary, and Source-Function evidence. Missing relation evidence routes to uncertainty, claim reduction, Stop, or Non-Capture—not invented chronology. Primary sites: [§§23.9–23.11](../01_blocks/03_part_ii_sub.md#23-9-internal-temporal-order).


## Chapter 23 Provisional-Lock Evidence Profile

Event claims require occurrence, boundary, completion, and praxis-change support. Non-Event claims additionally require independent expectation and bounded non-realization support. Delay, repeated non-decision, internal order, overlap, interruption, thresholds, and each clock relation require their own source trace. Missing evidence routes to uncertainty, claim reduction, Stop, Failure, or Non-Capture—not invented chronology, `Λ`, intention, or person responsibility. Primary site: [Chapter 23](../01_blocks/03_part_ii_sub.md#23-decomposing-events-non-events-and-internal-temporal-structures).

## Chapter 24 Preparation Evidence Routing

Path/Trajectory decomposition requires evidence for:

- independently warranted PATH-produced source identity;
- original source boundary, selection rule, formation rule, and coarser function;
- inherited `COMPOSE` Loss and unresolved compression debt;
- subpaths and their relations to the coarse object;
- transition clusters and intermediate configurations;
- turning-point transitions and historically traceable effects;
- realized and unrealized branch status within the relevant window;
- internal Frame changes and continuity carriers;
- competing continuations without prediction;
- operator-profile carriers of bounded Path-Dependence load;
- Same-Path versus rival PATH classification;
- new `DECOMPOSE` Loss, unresolved structure, Stop, and Non-Capture.

Chronology volume, endpoint similarity, narrative salience, or graph coherence cannot substitute for formation-lineage and relation evidence.

Preparation control: [Chapter 24 Preparation Record](Chapter_24_Preparation_Record.md).

## Chapter 24 WP1 Evidence Return

WP1 claims require evidence for:

- independently warranted PATH-produced source identity;
- source boundary, category, coarse function, and historical reference;
- original selected configurations, ordering, formation relations, and inherited Loss;
- the bounded insufficiency of the coarse reconstruction;
- local subpath sources, endpoints, transitions, and relation to the coarse Path;
- sequential, parallel, partial, competing, interrupted, resumed, and differently paced relations where claimed;
- transition-cluster source/target configurations, intermediates, dependencies, thresholds, and rival maps;
- every new selection introduced during decomposition;
- classification pressure between `DECOMPOSE`, `COMPOSE`, and `PROJECT_AS`.

Chronology volume, shared labels, graph coherence, or later narrative importance cannot substitute for source and formation-lineage evidence. Primary site: [Chapter 24 WP1](../01_blocks/03_part_ii_sub.md#chapter-24-decomposing-paths-and-trajectories).

## Chapter 24 WP2 Evidence Return

WP2 claims require evidence for:

- component transitions and later historically traceable effects of turning-point candidates;
- changed alternatives, costs, asymmetries, bindings, or action corridors;
- branch availability within a bounded historical window;
- roles, conditions, and mechanisms supporting branch status;
- counterfactual constraints using then-available information and capacities;
- earlier/later Frames and the relation connecting them;
- persisted records, roles, obligations, residues, and practical consequences supporting continuity;
- continuation entry conditions, accessibility, unequal load, horizon, and uncertainty;
- reversals, interruptions, repair, parallelism, and counter-trends.

Later narrative importance, current imaginability, shared institutional labels, graph coherence, or current accessibility cannot substitute for historical source support. Primary site: [Chapter 24 WP2](../01_blocks/03_part_ii_sub.md#24-5-turning-points).

## Chapter 24 WP3 Evidence Return

WP3 requires distinct evidence for:

- original PATH selection, formation, and inherited Loss;
- recovered detail versus later or newly accessed sources;
- any assertion that a historical distinction remains irrecoverable;
- the present analytical cut and each tested Path-Dependence dimension;
- historical carriers, intervals, present effects, counterevidence, and current-condition sufficiency pressure;
- Same-Path reference, boundary, formation lineage, and coarse function;
- materially new source selections, periodizations, macro-objects, or referents requiring rival `COMPOSE`;
- local result, source-function effect, prior claim disposition, and Output Class separately;
- Failure, Stop, and Non-Capture triggers.

Detail volume, archive completeness, profile count, narrative coherence, shared endpoint, or machine-readable consistency cannot substitute for these burdens. Primary site: [Chapter 24 WP3](../01_blocks/03_part_ii_sub.md#24-9-irrecoverable-compression).

## Chapter 24 Provisional-Lock Evidence Return

Required evidence is claim-specific: original PATH selection and formation records; source boundaries; transition relations; subpath carriers; historical branch availability; turning-point effects; Frame-change continuity; continuation entry conditions; inherited and current Loss; present carriers of dependence; and rival maps. Missing or irrecoverable evidence remains declared and cannot be repaired by formal completeness, graph density, interactivity, or later narrative coherence.

## Chapter 25 Preparation Evidence Routing

Resolution classification requires evidence for:

- the coarse source claim and finer reconstruction;
- the same tested claim and comparison basis;
- source-supported component and relation differences;
- changed or unchanged praxis-relevant dimensions;
- the coarser source function after refinement;
- source precision relative to semantic precision;
- calibration thresholds, rival maps, and revision conditions;
- the counterexample or failed condition in an Escape test;
- the original claim disposition before any new finer claim;
- Stop, Non-Capture, Loss, and re-entry conditions.

Detail volume, graph coherence, formal validation, or model plausibility cannot independently establish purchase, relation support, calibration, or claim repair.

Preparation control: [Chapter 25 Preparation Record](Chapter_25_Preparation_Record.md).

## Chapter 25 WP1 Evidence Routing

WP1 claims require evidence for:

- the bounded source object or source Transformation Record;
- the exact coarse claim and finer claim;
- continuity of the tested burden and comparison basis;
- source support for added distinctions;
- relation support for claimed connections;
- the changed or unchanged praxis dimensions;
- the precise claim effect;
- the counterexample or failed condition in an Escape test;
- the prior claim disposition before a new finer claim is tested;
- source coherence where Drift is alleged.

Detail volume, graph dimensionality, interaction, visual coherence, formal validation, or analytical effort cannot independently establish Gain, relations, claim repair, or admissibility.

Primary site: [Chapter 25 WP1](../01_blocks/03_part_ii_sub.md#chapter-25-resolution-gain-neutrality-drift-and-escape).

## Chapter 25 WP2 Evidence Routing

WP2 claims require evidence for:

- the tested claim and relevant praxis dimensions;
- the finer distinction whose purchase is assessed;
- the component, relation, and claim support states separately;
- the coarser source function and its relation to finer components;
- the source-supported precision ceiling;
- the exact semantic or structural excess where Source Overreach is alleged;
- the comparison threshold, its basis, uncertainty, revision condition, and version;
- prior claim dispositions before threshold or claim revision;
- declared monitoring signals, invariants, Stop triggers, and re-entry conditions where runtime treatment is discussed.

Visual coherence, graph topology, formal validity, computational effort, repeated derived agreement, or complete fields do not independently establish historical relations, purchase, calibration, semantic truth, or universal termination.

Primary site: [Chapter 25 WP2](../01_blocks/03_part_ii_sub.md#25-5-detail-without-purchase).

## Chapter 25 WP3 Evidence Routing

WP3 requires evidence for the last resolution-bearing distinction, subsequent no-gain or drift attempts, source and relation support, preserved coarser function, prior claim disposition, Stop trigger, and materially new re-entry basis. Unsupported refinement lacks the support needed for Neutrality. Non-Capture requires evidence that the discrimination problem is genuine rather than merely unexamined. Runtime monitoring may record declared signals and invariants; it does not prove semantic truth or universal termination.

## Chapter 25 Provisional-Lock Evidence Return

Required evidence is comparison- and claim-specific: source support for coarse and finer reconstructions; relation support; changed or unchanged praxis dimensions; coarser-function continuity; threshold versions; counterpressure; prior claim dispositions; Stop and re-entry bases; and Loss. Missing evidence cannot be repaired by graph density, dimensionality, formal completeness, additional compute, runtime monitoring, or a finer vocabulary.

## Chapter 26 Preparation Evidence Routing

| Boundary question | Evidence required | Insufficient substitute |
|---|---|---|
| internal constitution | same-reference source materials, finer components and relations, granularity change, coarser-function trace | more detail or a new heading |
| contextual target function | preserved origin type, declared target context, source-traceable functional relation, boundedness and rivals | analogy, usefulness, interface role, or label |
| recontextualization | changed Frame, perspective, question, or presentation setting | automatic operation assignment |
| dual operation | link-specific source, claim, Record, Loss, result, and failure evidence | one mixed narrative or shared success claim |
| invalid collapse | evidence that claims, types, contexts, or records were merged | mere stylistic ambiguity |

Graph geometry, proximity, clustering, colour, interaction, centrality, formal completeness, or model flags do not establish semantic operation identity or target function.

Preparation control: [Chapter 26 Preparation Record](Chapter_26_Preparation_Record.md).

## Chapter 26 WP1 Evidence Routing

WP1 operation-boundary claims require evidence for:

- the bounded source object and origin type;
- the source function or explanatory target;
- the source Frame and declared granularity relation;
- the internal structures and relations claimed by SUB;
- the declared target context and proposed target function claimed by RETYPE pressure;
- the source features on which the target function would depend;
- origin-type preservation and prior source-claim disposition;
- rival operation readings, uncertainty, and Loss.

Shared sources, semantic similarity, new labels, analogies, graph geometry, visual centrality, interface use, interaction, or formal validation cannot independently establish operation identity or target-function warrant.

Primary site: [Chapter 26 WP1](../01_blocks/03_part_ii_sub.md#chapter-26-the-boundary-between-sub-and-retype).

## Chapter 26 WP2 Evidence Routing

WP2 boundary claims require evidence for:

- the same origin-typed source object across separately declared operation candidates;
- the internal structures and source-function effect used by the Trajectory or Attractor decomposition;
- the bounded target context, task, conditions, exclusions, and failure boundary;
- the source features on which the target function depends;
- the context-specific functional difference produced by those features;
- the distinction among Attractor operator type, occurrence typing, recurrence structure, and contextual function;
- the operative claim hidden by SUB-looking or RETYPE-looking language;
- the changed Frame or presentation condition where recontextualization is alleged;
- prior claim dispositions and operation-specific Loss.

Shared evidence, source-feature presence, usefulness, later use, labels, headings, Reader panels, graph layers, spatial proximity, centrality, or interaction cannot independently establish operation identity or target-function warrant.

Primary site: [Chapter 26 WP2](../01_blocks/03_part_ii_sub.md#26-5-trajectory-decomposition-and-projection).

## Chapter 26 WP3 Evidence Routing

The decision test requires evidence for source object and origin type, internal distinction and relation support, source-object unit continuity, bounded target context, source-traceable target function, operation order, record handoff, and occurrence-specific Loss. A target function cannot inherit support from a component map, and a decomposition cannot inherit validity from contextual usefulness. Non-Capture requires evidence that the classification ambiguity is genuine rather than merely untested.

## Chapter 26 Provisional-Lock Evidence Return

Operation-boundary evidence is claim-specific: source-object and origin-type support; source-function and Frame declarations; granularity change; internal component and relation support; bounded target-context conditions; source-traceable target-function relations; recontextualization evidence; operation order; separate Records, Loss, and results; prior claim dispositions; and rival classifications. Shared evidence, usefulness, later use, labels, headings, Graph geometry, centrality, interaction, formal validation, or interface roles do not independently establish operation identity or target-function warrant.

## Chapter 27 Preparation Evidence Route

Chapter 27 requires separate evidence burdens for:

- the source object and source claim;
- each component candidate;
- each asserted component relation;
- source and target granularity;
- the expected additional praxis difference;
- actual changed praxis dimensions;
- source-reference continuity;
- coarser-function confirmation, revision, rejection, or underdetermination;
- type-integrity preservation or revision;
- component counterfactual variants;
- Source-Ceiling, Stop, Claim Reduction, and Non-Capture findings.

Source presence does not prove relation support. Relation support does not prove component constitutiveness. A counterfactual component test does not prove universal causality. Missing information cannot be converted into a component, relation, Non-Event, or negative result merely to complete the map.

Preparation control: [Chapter 27 Preparation Record](Chapter_27_Preparation_Record.md).

## Chapter 27 WP1 Evidence Routing

WP1 boundary claims require evidence for:

- the bounded source object and tested source claim;
- source and target granularity;
- the expected and actual changed praxis dimensions;
- component existence and relation support as separate burdens;
- source-reference continuity or explicit revision;
- the coarser function and its possible confirmation, differentiation, reduction, rejection, or underdetermination;
- uncertainty and Loss.

Additional timestamps, node density, interface distinctions, graph layout, common labels, temporal adjacency, or formal completeness cannot independently establish PraxisPurchase, source continuity, relation support, or reconstruction.

Primary site: [Chapter 27 WP1](../01_blocks/03_part_ii_sub.md#chapter-27-sub-boundary-conditions).

## Chapter 27 WP2 Evidence Routing

WP2 claims route evidence separately for:

- component existence and boundary;
- temporal, dependency, enabling, blocking, substitution, maintenance, or conflict relations;
- event and Non-Event claims;
- source-function effects;
- bounded component counterfactual variations;
- source-type confirmation, restriction, rejection, or underdetermination.

Model coherence, simulation output, graph centrality, node density, schema completion, shared labels, or narrative plausibility cannot supply missing source support. Counterfactual findings must expose assumptions and remain local to the declared source object, relation map, Frame, and claim.

Primary site: [Chapter 27 WP2](../01_blocks/03_part_ii_sub.md#27-5-source-ceiling).

## Chapter 27 WP3 Evidence Routing

A WP3 result must preserve evidence separately for:

- the coarse/fine comparison basis and materially changed claim dimensions;
- every failed or satisfied conjunctive SUB gate;
- the surviving weaker claim under Claim Reduction;
- unresolved rival component or relation maps under Non-Capture;
- the basis and threshold for Optional or Mandatory Stop;
- the materially new source, relation map, claim, object, threshold, or invariant enabling re-entry;
- prior Record disposition and canonical Loss.

More compute, denser graphs, generated components, simulation coherence, or interface changes are not new evidence. Primary site: [Chapter 27 WP3](../01_blocks/03_part_ii_sub.md#27-9-no-privilege-of-fine-resolution).

## Chapter 27 Provisional-Lock Evidence Routing

A locked Chapter-27 assessment keeps evidence distinct for Component presence, Relation Support, Source Reference, Coarser-Function effect, Type Integrity, counterfactual assumptions, Source Ceiling, unresolved structure, Stop/re-entry basis, and canonical Loss. Evidence in one field cannot silently compensate for another.

Primary site: [Chapter 27 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-27-completion-boundary).

## Chapter 28 Preparation Evidence and Artifact Route

Every Chapter-28 case requires separate support for source identity, origin type, Frame, granularity, components, relations, temporal order where relevant, source-function effect, type effect, resolution result, alternatives, Counterfactual Sensitivity, Loss, and final mapping.

Artifact completeness requires:

```text
Markdown reconstruction
+ schema-valid YAML Record
+ case-local audit
+ canonical Output-Class mapping
+ Case Index registration and hashes
```

This is a completeness burden, not proof of substantive truth. Shared evidence does not merge operations; graph geometry does not prove relations; a coherent narrative does not fill source gaps; a valid schema does not select the correct semantic result.

Preparation control: [Chapter 28 Preparation Record](Chapter_28_Preparation_Record.md).

## Chapter 28 WP1 — Positive Case Evidence Discipline

All six WP1 records use synthetic declarations with explicit provenance and no external empirical warrant. Component presence, relation support, counterfactual sensitivity, source-function effect, uncertainty, and Claim Ceiling are recorded separately. Missing relations are not filled through narrative coherence, graph layout, or simulation.

## Chapter 28 WP2 — Countercase Evidence Discipline

WP2 separates supported detail from relevant detail, component support from relation support, local difference from macrostructure, occurrence source from operator type, and internal reconstruction from target-function or new-PATH claims. Missing support is preserved as unavailable or underdetermined, never completed by graph or narrative coherence.

## Chapter 28 WP3 — Analogy and Modulation Evidence Discipline

Foreign-domain resemblance is not source-bound component or relation evidence. Recurrent occurrence effects do not establish a new operator type. The integrated Local Audit preserves unavailable and underdetermined structure rather than completing it through models, graphs, or type inflation.

## Chapter 28 and Part II Provisional-Lock Evidence Status

The lock is supported by sixteen Chapter-28 Markdown reconstructions, sixteen schema-valid Chapter-28 YAML Records, twelve-stage local audits, canonical mappings, complete Loss, alternatives, Case Index registration and hashes, the twenty-four-question integrated SUB Local Audit, and the retained Chapters-18–27 canonical method.

All case sources are synthetic declarations unless separately stated. Artifact completeness and schema validity establish controlled record integrity, not empirical truth, causal sufficiency, semantic validity, person judgment, or application authority.

Primary artifact registry: [Case Index](../03_cases/Case_Index.md).  
Primary lock site: [Part-II SUB lock boundary](../01_blocks/03_part_ii_sub.md#part-ii-sub-provisional-lock-boundary).

## Chapter 29 Preparation Evidence Route

A functional-projection claim requires separate support for:

- source-object identity and origin type;
- historical and constitutive source load;
- target-context identity, roles, level, and duration;
- the proposed target-function difference;
- the source-to-context functional relation;
- bounded Counterfactual Sensitivity;
- competing present structures and no-projection alternatives;
- validity scope, Claim Ceiling, Loss, Stop, and Non-Capture.

```text
source cited
≠ source functionally constitutive

target label useful
≠ target function warranted
```

A model or Reader may expose recorded evidence but may not infer target-function truth from graph position, frequency, similarity, or interface use.

Preparation control: [Chapter 29 Preparation Record](Chapter_29_Preparation_Record.md).


## Chapter 29 WP1 Evidence Routing

WP1 keeps evidence and declarations separate for:

- source-object identity and source Record;
- origin type and source reference;
- prior source disposition, uncertainty, and inherited Loss;
- target-context identity, target scene or object, relative level, and analytical purpose;
- the proposed target-side praxis difference;
- the same-source no-additional-function contrast.

```text
source evidence available
≠ target function carried

target context declared
≠ functional continuity established
```

WP1 identifies candidate source load but does not yet decide which features are constitutive. Graph position, narrative usefulness, similarity, frequency, repeated citation, interface prominence, or model completeness cannot establish the target function.

Primary site: [Chapter 29 WP1](../01_blocks/04_part_iii_retype.md#chapter-29-functional-projection-without-origin-type-replacement).

## Chapter 29 WP2 Evidence Routing

WP2 distinguishes evidence roles without deciding empirical truth:

- source identity and formation records support Source Object Integrity;
- source-supported historical relations identify load-bearing candidates;
- target-context records support scene, role, duration, and current-structure declarations;
- bounded source variants test claim sensitivity rather than counterfactual truth;
- same-source context contrast tests function necessity in the target scene;
- canonical Loss records preserve unavailable, compressed, excluded, uncertain, and irrecoverable source information.

The formal model may validate that these evidence roles are declared. It may not decide which feature is actually load-bearing, whether a counterfactual is true, whether causality is established, or whether the final projection succeeds.

Primary site: [Chapter 29 WP2](../01_blocks/04_part_iii_retype.md#29-6-source-object-integrity).

## Chapter 29 WP3 Evidence Burden

A projection-without-replacement packet must preserve evidence routes for the source object's formation, any separate decomposition, source heterogeneity, prior Loss and dispositions, the declared target context, and the claimed target-side difference. Evidence that only changes interpretation or presentation supports Recontextualization or display use, not `PROJECT_AS` by itself.

Separate evidence routes are required for:

- formation of a source composite under `COMPOSE`;
- internal source trace under `DECOMPOSE`;
- bounded target-function effect under `PROJECT_AS`;
- any re-entry under changed context, function, source typing, or scope.

Primary site: [Chapter 29 WP3](../01_blocks/04_part_iii_retype.md#29-9-projection-without-replacement).

## Chapter 29 Lock and Chapter 30 Evidence Burden

Chapter 29’s lock is supported by Contract coverage, twenty-four exact Pressure Duties, Reference/Formal-Model synchronization, and package checks. Those controls support the method lock only; they do not support a concrete target function.

A Chapter-30 `PROJECT_AS` occurrence requires distinct evidence roles:

- source-basis evidence for the source object and origin type;
- source pointers for load-bearing and modulating features;
- target-context evidence for the claimed praxis difference;
- counterfactual support for bounded source dependence;
- evidence for validity scope, alternatives, and no-projection pressure;
- Loss and uncertainty disclosure.

```text
file/hash/schema/package evidence
≠ semantic target-function warrant
```

## Chapter 30 WP1 Evidence Burden

WP1 requires a source route before projection testing:

| Evidence position | Required visibility | Boundary |
|---|---|---|
| source object | independent reconstruction | may not be defined by the target label |
| source reference | record, case, historical, or documentary identity | repeated label is insufficient |
| source coordinates | Frame, granularity, level, temporal scope | relative, not ontological |
| source basis | materials and prior records | citation volume is not Constitutive Source Trace |
| prior status | disposition and uncertainty | may not be upgraded by RETYPE entry |
| inherited Loss | exact five canonical fields | may not be reset or recovered rhetorically |

Constitutive Source Trace and Counterfactual Sensitivity remain WP2 burdens. WP1 establishes only that a credible test route must exist.

Primary site: [§30.4 Source Declaration](../01_blocks/04_part_iii_retype.md#30-4-source-declaration).

## Chapter 30 WP2 Evidence Route

WP2 distinguishes evidence location from functional trace:

```text
source pointer
→ where material can be inspected

Constitutive Source Trace
→ how a specific source relation is proposed to change a named target-side praxis dimension
```

The evidence packet must retain source identity, feature role, target-side difference, rival pressure, uncertainty, and a route by which material source change could weaken or defeat the claim. Counterfactual variants may be documented, observed, or boundedly hypothetical; unavailable variation remains underdetermined or not testable rather than being converted into support.

No evidence route alone selects a sensitivity descriptor or canonical Output Class.

## Chapter 30 WP3 Evidence and Warrant Routing

Validity Scope requires evidence for the declared target interval, roles, relations, and affected praxis dimensions. Transfer requires new evidence and a new operation occurrence. Visibility choices do not upgrade evidence. Loss declarations must preserve unavailable, uncertain, excluded, compressed, and irrecoverable source conditions.

Alternatives require enough source and target support to compare rival functions and no-projection without inventing complete counterfactual histories. Formal Record completion may prove declaration presence, not substantive source load, target-function truth, causality, or parsimony.

Primary sites: [Validity Scope](../01_blocks/04_part_iii_retype.md#30-9-validity-scope), [Alternatives](../01_blocks/04_part_iii_retype.md#30-11-alternative-projections-and-no-projection), and [Record](../01_blocks/04_part_iii_retype.md#30-13-project-as-record).

\n## Chapter 31 Historical-Load Evidence Route\n\nA trajectory-to-frame-function claim requires an already warranted source Trajectory, source pointers to sedimented expectations/roles/costs/exclusions/bindings/residues, present-target evidence, and a bounded counterfactual frame test. “History matters,” chronology, citation density, or retrospective narrative do not substitute for Constitutive Source Trace.\n\nNo test, case, or smoke YAML is produced during the Block phase. Family case records remain deferred.\n\nPrimary site: [Chapter 31 Preparation Record](Chapter_31_Preparation_Record.md).\n


## Chapter 31 WP1 Evidence Separation

| Evidence layer | Primary burden | Prohibited substitution |
|---|---|---|
| source-period evidence | warrant the Trajectory, sequence, and candidate load carriers | target fit cannot manufacture the source object |
| target-period evidence | warrant the later configuration, present conditions, and framed dimensions | source validity does not establish target function |
| later retrospective evidence | support later interpretation or bounded reconstruction with explicit marking | later narrative does not silently replace either period |

Evidence may overlap in source material but must remain claim-typed by use. Historical Load and Constitutive Source Trace remain WP2 burdens.

Primary site: [§31.2 Source Object](../01_blocks/04_part_iii_retype.md#31-2-source-object).


## Chapter 31 WP2 Evidence Route

Historical-Load evidence must connect four separately inspectable positions:

1. a source feature already warranted inside Trajectory `X`;
2. a supported persistence, transmission, institutionalization, or reactivation route;
3. a named target-period difference in `Y` or `Z`;
4. present and rival-source evidence capable of weakening, replacing, or leaving the relation unresolved.

Evidence for the source object does not automatically support the target function. Later retrospective evidence must remain marked and may corroborate or reconstruct a relation, but it cannot silently substitute for source-period or target-period evidence.

Load-bearing and modulating carrier assignments require source pointers and defeat conditions. Qualitative relative-load statements require comparative evidence; they do not authorize causal shares or scores.

Primary site: [Chapter 31 §§31.5–31.7](../01_blocks/04_part_iii_retype.md#31-5-historical-load).


## Chapter 31 WP3 Evidence Route

A frame-function claim requires separately inspectable evidence for:

1. the PATH-established source Trajectory;
2. the proposed historical carrier;
3. persistence, transmission, institutionalization, or reactivation;
4. the bounded target difference;
5. present and rival frame sources;
6. carrier, source, context, and rival-source variation;
7. temporal status of source-period, target-period, and later retrospective evidence.

Archive size, citation density, salience, continuity of names, target fit, and retrospective coherence are insufficient substitutes. Different histories producing indistinguishable later scenes may require Claim Reduction, provisionality, or Non-Capture rather than a forced source-specific function.

Primary site: [Chapter 31 WP3](../01_blocks/04_part_iii_retype.md#31-8-rhetorical-history-versus-frame-function).

## Chapter 31 Lock and Chapter 32 Preparation — Evidence Burden

The Macro-Event family requires separate evidence roles:

| Evidence role | Burden |
|---|---|
| source-Trajectory support | independently warranted internal duration, sequence, phases, reversals, heterogeneity, prior disposition, and Loss |
| boundary support | start, end, constitutive phases, turning points, and adjacent-development relation not derived solely from a later label |
| target-Frame support | wider Path, target time scope, granularity, level, roles, and before/after relation |
| transition-function support | concrete change in possibilities, path segmentation, or bounded transition structure |
| compression support | source details remain traceable despite target-level unit treatment |
| counterfactual support | phase, boundary, source, target, and alternative-source variation can pressure the claim |

A large archive or familiar period name may support historical relevance while leaving boundary or target-function warrant absent. Later retrospective periodization must be marked and cannot silently replace source- or target-period support.

Primary site: [Chapter 32 Preparation Record](Chapter_32_Preparation_Record.md).


## Chapter 32 WP1 Evidence Routing

| Evidence layer | Supports | Must not silently substitute for |
|---|---|---|
| source-Trajectory evidence | phases, transitions, branches, internal turning points, PATH boundary | Macro-Event function |
| projection-boundary evidence | relevance of the tested start/end scope to the target claim | source-object validity or target gain |
| target-Path evidence | wider before/after configurations and adjacent developments | causal monopoly |
| later retrospective evidence | candidate names, rival periodizations, later interpretations | source-period or target-period support |
| formal declaration | field presence and inventory consistency | historical correctness or transition truth |

Primary sites: [§32.3](../01_blocks/04_part_iii_retype.md#32-3-target-frame) and [§32.4](../01_blocks/04_part_iii_retype.md#32-4-boundary-selection).

## Chapter 32 WP2 Evidence Routing

| Evidence layer | Supports | Cannot by itself establish |
|---|---|---|
| source-period sequence evidence | duration, phase relations, turning points, delays | Macro-Event function |
| role/cost/asymmetry evidence | internal heterogeneity and bounded effects | homogeneous transition |
| target before/after evidence | candidate event-function difference | causal sufficiency |
| later retrospective evidence | rival naming and periodization | original phase order or boundary truth |
| formal Loss declaration | disclosure completeness | substantive trace preservation |

Primary site: [§§32.5–32.7](../01_blocks/04_part_iii_retype.md#32-5-internal-duration).


## Chapter 32 WP3 Evidence Return

| Evidence burden | Required support | Insufficient substitute |
|---|---|---|
| punctualization pressure | constitutive source structure shown lost or falsely collapsed | one target node or date alone |
| operation-chain separation | prior `COMPOSE` record plus independent `PROJECT_AS` record | one merged narrative |
| phase variation | source-supported removal, reversal, delay, or replacement pressure | invented alternative history |
| boundary variation | serious rival start/end candidates and changed trace/Loss/function | preferred period label |
| alternative source | separately warranted narrower or different object | silent relabeling of `M` |
| same-source target contrast | fixed `M` tested in `B` and `C` | different source intervals per target |
| failed projection | missing or contradicted indispensable function warrant | source prominence or low readability |

Primary site: [Counterfactual Macro-Event Test](../01_blocks/04_part_iii_retype.md#32-10-counterfactual-macro-event-test).

## Chapter 33 Evidence Separation

Evidence must remain separated across:

1. each source Trajectory and its prior PATH warrant;
2. trajectory selection and comparison coordinates;
3. constitutive versus variable recurrence;
4. source-traceable reproduction or later-path influence;
5. target-context difference in `D` or `E`;
6. sampling, survivorship, missing, failed, truncated, and divergent trajectories;
7. later retrospective pattern narratives.

```text
source-Trajectory evidence
≠ comparability evidence
≠ recurrent-form evidence
≠ mechanism evidence
≠ target attractor-function evidence
```

Later recurrence may test the candidate form but may not retroactively select the source trajectories or constitutive phases.

Primary site: [Chapter 33 Preparation Record](Chapter_33_Preparation_Record.md).


## Chapter 33 WP1 Evidence Route

| Evidence burden | WP1 requirement | Still open |
|---|---|---|
| source-Trajectory evidence | independent PATH references for each source object | substantive source-record quality remains case-bound |
| source-selection evidence | trajectories selected before target-result adjudication | sampling and survivorship audit remains WP3 |
| comparability evidence | Frame, granularity, role, time, evidence, transition, and operator-weighting relations declared | substantive comparability/incomparability result remains open |
| recurrent-form evidence | candidate discriminating cross-trajectory relation declared | constitutive phases and allowable variation remain WP2 |
| target evidence | `D/E` contexts and eligible continuation dimensions declared | later-path work and mechanism remain WP2 |
| threshold evidence | non-count threshold architecture declared | threshold not substantively crossed |

Citation density, shared vocabulary, visual alignment, recurrence count, and later target fit do not substitute for the relevant evidence layer.

Primary site: [§33.2 Single Trajectory versus Recurrent Form](../01_blocks/04_part_iii_retype.md#33-2-single-trajectory-versus-recurrent-form).

## Chapter 33 WP2 Evidence Route

| Evidence burden | Required material | Insufficient substitute |
|---|---|---|
| constitutive repetition | source records supporting relation, order, roles, Non-Events, costs, variation, and break conditions | shared label or repeated vocabulary |
| reproduction/path influence | temporally directed persistence, transmission, institutionalization, or reactivation trace | simultaneous resemblance or later narrative |
| Attractor Load | target-period evidence of changed friction, expectation, accessibility, role, repair/exit, alternative cost, continuation, or visibility | recurrence count or source salience |
| dynamic/static distinction | separate transition-form and state-stabilization traces | generic “attractor” label |
| scope | target context, roles, level, time, granularity, praxis dimensions, rivals, uncertainty | universalized pattern statement |

Primary site: [Chapter 33 WP2](../01_blocks/04_part_iii_retype.md#33-5-constitutive-repetition).

## Chapter 33 WP3 Evidence Route

| Evidence burden | Required material | Insufficient substitute |
|---|---|---|
| target-blind source formation | independently warranted Trajectories, predeclared inclusion/exclusion, comparison coordinates, known source revisions | later target fit or narrative motif |
| selection and missingness | accessible source field, dependence, duplication, survivorship, interrupted/opposite/missing Trajectories, directional uncertainty | large documented count |
| pattern elasticity | explicit incompatible cases, opposite sequences, break conditions, narrowing/splitting consequences | label expansion after counterexamples |
| counterfactual pressure | source-constrained phase/frame/role/cost/source/comparison/mechanism/target variation | imagined unconstrained alternatives or causal assertion |
| rival comparison | common Frame, present condition, independent regeneration, multiple forms, static-only, descriptive motif, no stable source | attractor label treated as default |
| failure routing | located source, mechanism, target-work, type, scope, Loss, or source-ceiling failure | global rejection of all source histories |

Primary site: [Chapter 33 WP3](../01_blocks/04_part_iii_retype.md#33-8-recurrent-form-versus-retrospective-similarity).

## Chapter 33 Lock and Chapter 34 Evidence Burden

Chapter 34 requires distinct evidence for:

1. each local occurrence;
2. component boundaries and relation topology;
3. source-composite identity;
4. target context and target praxis difference;
5. substitution, smaller-subset, contradiction, rival-Frame, and present-condition pressure;
6. exact Loss, uncertainty, Stop, and Non-Capture.

Evidence for component presence is not evidence for relational functional formation.

## Chapter 34 WP1 Evidence Routing

| Evidence layer | Supports | Must not silently substitute for |
|---|---|---|
| component evidence | local occurrence identity and source typing | relation or composite warrant |
| relation evidence | coordination, reinforcement, dependency, sequence, countervailing structure | target function |
| target-period evidence | access, exclusion, expectation, cost, role, corridor, binding, or alternative difference | source-composite validity |
| expectation evidence | Non-Event Frame and expected window | missing information or retrospective disappointment |
| present-condition and rival-Frame evidence | competing explanation of target field | automatic source invalidation |
| formal declaration | field presence and inventory integrity | substantive functional formation or emergence |

Primary sites: [§34.1](../01_blocks/04_part_iii_retype.md#34-1-basic-claim) and [§§34.2–34.4](../01_blocks/04_part_iii_retype.md#34-2-local-differences-as-higher-level-boundary-function).

## Chapter 34 WP2 Evidence Routing

| Evidence burden | Supports | Does not establish alone |
|---|---|---|
| commitment records and practice | local commitment occurrence | higher-level binding-function |
| continuity, succession, repair, breach, and exit evidence | binding relation and target consequences | legitimacy or enforceability |
| local integration and residual-conflict evidence | integration occurrences and partiality | global coherence |
| coordination, dependency, sequence, translation, and shared-effect evidence | relation topology | emergent function truth |
| removal, replacement, redundancy, and subset evidence | component-role pressure | causal percentage or permanent role |
| countervailing and incompatible evidence | weakening, redirection, split, Stop, Failure, or Non-Capture | automatic destruction of source composite |

Primary sites: [§34.5](../01_blocks/04_part_iii_retype.md#34-5-repeated-commitments-as-higher-level-psi-function) through [§34.7](../01_blocks/04_part_iii_retype.md#34-7-emergent-function).

## Chapter 34 WP3 Evidence Return

| Evidence position | Supports | Does not alone support |
|---|---|---|
| component inventory | descriptive aggregation | functional formation |
| relation trace | candidate coordination or distributed load | target function truth |
| target praxis difference | target-function burden | causality or authority |
| subset and boundary comparison | source-scope calibration | unique correct composite |
| rival-Frame analysis | frame sensitivity | final Frame selection automatically |
| counterfactual variation | sensitivity classification | causal necessity or sufficiency |
| schema and smoke results | formal consistency | empirical emergence or macrofunction truth |

Primary sites: [§§34.8–34.11](../01_blocks/04_part_iii_retype.md#34-8-aggregation-versus-functional-formation).

## Chapter 34 Lock and Chapter 35 Evidence Burden

Chapter 35 requires distinct evidence for:

1. each operator occurrence and its canonical dependencies;
2. qualitative weighting criteria, role scope, time window, and relation map;
3. each declared modulator and its contextual effect;
4. profile stability and variation;
5. target-context praxis difference for any projection;
6. rival profile, no-profile, present-condition, and no-projection alternatives;
7. exact Loss, uncertainty, Stop, Non-Capture, and Claim Ceiling.

Symbol frequency, label recurrence, visual prominence, model centrality, or add-on vocabulary are not weighting evidence by themselves.

## Chapter 35 WP1 Evidence Routing

| Evidence layer | Supports | Must not silently substitute for |
|---|---|---|
| operator-occurrence evidence | source occurrence identity and typing | weighting or profile |
| relation evidence | support, opposition, sequence, access, persistence, threshold relation | causality or dependency change |
| role/phase evidence | bounded variation in relative load | aggregate person/group type |
| contextual-condition evidence | modulator candidate and relation path | operator identity or effect by label |
| target-period evidence | later access, cost, exit, revision, or continuation difference | source weighting validity |
| rival and missingness evidence | calibration and Non-Capture pressure | automatic source invalidation |
| formal declaration and smoke results | artifact consistency | substantive weighting, modulation, or prediction truth |

Primary sites: [§35.1](../01_blocks/04_part_iii_retype.md#35-1-purpose) through [§35.4](../01_blocks/04_part_iii_retype.md#35-4-modulator).

## Chapter 35 WP2 Evidence Routing

| Evidence layer | Supports | Must not silently substitute for |
|---|---|---|
| occurrence and relation evidence | profile topology | target function or causal mechanism |
| role/phase evidence | bounded stability and variation | aggregate person/group type |
| temporal evidence | transition accessibility, Λ-centrality, persistence, sedimentation, continuation differences | probability or teleology |
| modulator variation evidence | removal, substitution, reversal, redundancy, changed access | causality by label |
| rival-profile evidence | calibration, narrower relations, inert profile, no stable profile | automatic failure of source occurrences |
| target evidence | later-praxis difference in `K/L` | source-profile selection |
| smoke/schema evidence | artifact consistency | substantive profile or projection truth |

Primary sites: [§35.6](../01_blocks/04_part_iii_retype.md#35-6-from-weighting-to-trajectory-form) and [§35.7](../01_blocks/04_part_iii_retype.md#35-7-emergent-functional-profile).

## Chapter 35 WP3 Evidence Routing

Profile projection requires separate evidence for source occurrences, relation topology, qualitative weighting, modulators, bounded stability, target placement, concrete target difference, target-condition isolation, Counterfactual Sensitivity, and exact Loss.

Evidence for a compact label, symbol frequency, clustering output, add-on vocabulary, or later outcome cannot substitute for these warrants. Missing or inseparable evidence must remain uncertain, reduced, stopped, failed, or non-captured rather than typed onto persons or groups.

## Chapter 35 Lock and Chapter 36 Evidence Routing

Projection comparison requires candidate-specific evidence for source load, target context, target difference, Counterfactual Sensitivity, and exact Loss. A shared source label is insufficient where candidates use different periods, subsets, Frames, or evidential bases.

Evidence for breadth, elegance, model completeness, label familiarity, or institutional use cannot establish comparative superiority. Missing common comparison bases must remain uncertain, non-comparable, stopped, or non-captured.

## Chapter 36 WP1 Evidence Routing

Projection comparison requires:

- one stable source reference with retained disposition, uncertainty, and inherited Loss;
- candidate-specific declarations of load-bearing source subsets;
- target context, level, object, function, Claim Scope, validity scope, temporal scope, and affected praxis dimensions;
- evidence capable of distinguishing non-exclusive from overlapping target work;
- live alternative functions, contexts, narrower claims, source-only accounts, no-projection, and Non-Capture.

Evidence for breadth, elegance, label familiarity, schema completeness, or joint readability does not establish compatibility, competition, preference, or integration.

## Chapter 36 WP2 Evidence Routing

Comparative preference requires candidate-specific evidence for:

- positive target-level praxis difference;
- relevant countercase rejection;
- response to material source/subset changes;
- present-target-condition isolation;
- exact five-part Loss;
- added assumptions and exclusions;
- justified common comparison basis.

Evidence for breadth, elegance, popularity, formal completeness, label familiarity, or corpus coverage cannot establish comparative superiority. Missing common bases route to uncertainty, underdetermination, non-comparability, Stop, or Non-Capture rather than invented scoring.

## Chapter 36 WP3 Evidence Routing

Non-translation requires evidence that transfer between candidates would materially change target coordinates, Claim Scope, Constitutive Source Trace, affected praxis dimensions, countercase boundaries, or exact Loss. Contradiction requires same-claim affirmation and denial under compatible scope and evidence; semantic distance is insufficient.

The Projection Comparison Record must reference separate candidate evidence, candidate-specific Loss, source/target variation, target-condition isolation, serious alternatives, no-projection, Stop, and Non-Capture. Evidence for formal completeness, vocabulary familiarity, institutional uptake, political desirability, or theory prestige cannot establish comparative superiority or tribunal authority.

## Chapter 36 Lock and Chapter 37 Evidence Routing

Cross-domain projection and analogy must keep separate evidence for source identity, mapping subset, target context, formal correspondence, semantic role, residuals, target-only features, Counterfactual Sensitivity, exact Loss, and alternative/no-projection accounts. Compilation, simulation, execution, or translation success is implementation evidence only and cannot substitute for semantic warrant.

## Chapter 37 WP1 Evidence Routing

A functional projection requires separate evidence for source identity, candidate mapping subset, target context, target function, PraxisPurchase, Constitutive Source Trace, material source/target sensitivity, exact Loss, alternatives, and Claim Ceiling.

A structural analogy requires evidence only for its declared correspondence and bounded usefulness, together with source-only residuals, target-only features, incompatibilities, uncertainty, and counterexamples. Formal isomorphism, compilation, execution, simulation, visual fit, or vocabulary familiarity cannot substitute for semantic-preservation evidence.

Evidence routing for the stable packets remains unresolved:

```text
S source evidence
→ retained independently

M formal mapping evidence
→ does not yet establish semantic preservation or target function

L recurrence and label familiarity
→ does not yet establish analogy or projection
```

Primary site: [Chapter 37 WP1](../01_blocks/04_part_iii_retype.md#37-1-why-the-distinction-matters).

## Chapter 37 WP2 Evidence Routing

Symbolic evidence supports notation correspondence. Formal evidence supports declared relation preservation. Executable evidence supports target-side implementation consistency. None substitutes for domain-grounded evidence of comparable praxeological role or bounded target function.

A terminal or partial analogy requires evidence for the exact preserved relation plus source-only residuals, target-only structure, incompatibilities, uncertainty, countercases, and Claim Ceiling. Label-substitution analysis requires comparison against ordinary domain descriptions, label removal, material source/target variation, exact Loss, and serious rivals.

```text
compile or simulation evidence
→ executable-status support only

relation-preservation evidence
→ analogy support possible

semantic-role and target-function evidence
→ separately required
```

Primary site: [Chapter 37 WP2](../01_blocks/04_part_iii_retype.md#37-5-symbolic-formal-and-executable-mapping).

## Chapter 37 WP3 Evidence Routing

Analogy-drift analysis requires the earliest bounded claim, every later scope or semantic increase, retained residuals, and new warrant for each transition. Translation-breadth evidence must distinguish symbol, relation, execution, compression, and bidirectional-rendering coverage from semantic-role evidence.

The integrated stress test routes evidence separately for source identity, mapping subset, target coordinates, correspondence level, comparable praxeological role, source-only and target-only residuals, countercases, reverse mapping, label sensitivity, no-projection, and Non-Capture. Implementation evidence cannot substitute for semantic evidence; passed formal validation cannot establish substantive mapping truth.

Primary site: [Chapter 37 WP3](../01_blocks/04_part_iii_retype.md#37-9-analogy-drift).

## Chapter 37 Lock and Chapter 38 Evidence Routing

Invalidity evidence must identify the exact original claim, source type, target function, context, Frame, level, granularity, temporal scope, evidence-transfer path, exact Loss, and prior disposition. A changed context or level requires a new evidence packet; it cannot inherit the failed claim's warrant.

Metaphor classification requires evidence of intended claim form. Person-level error analysis requires only the prohibited attribution structure, not diagnosis or motive evidence. Primitive-inflation analysis compares the local target-function claim against the unchanged operation and Δ–Ψ inventories.

Preparation site: [Chapter 38 Preparation Record](Chapter_38_Preparation_Record.md#6-scientific-pressure-and-counterfactual-architecture).

## Chapter 38 WP1 Evidence Routing

Invalid-type-jump analysis requires the warranted source type, source reference, dependencies, prior disposition, and the exact statement that allegedly replaces them. Missing-context analysis requires explicit absence or instability of target context, object, level, Frame, granularity, temporal scope, function, and Claim Scope.

Metaphor/formal-claim analysis requires evidence of intended claim form. Where intention or operational use remains genuinely ambiguous, the evidence supports interpretive review or Non-Capture rather than invented formalization. Completing coordinates supplies a new claim packet; it does not validate the earlier incomplete claim.

Primary site: [Chapter 38 WP1](../01_blocks/04_part_iii_retype.md#38-1-invalid-type-jump).

## Chapter 38 WP2 Evidence Routing

Cross-level claims require evidence at each relevant level plus evidence for the declared relation. Multi-granular claims require resolution-specific evidence and a traceable reconstruction, aggregation, decomposition, or projection bridge. Fine evidence does not self-promote into macrofunction evidence.

Post-failure projections require the preserved earlier disposition and a new evidence packet for the new target claim. Person-related statements require separate person-level evidence and may not inherit configuration-level function. Primitive claims cannot inherit authority from local empirical success, model validity, or repeated use.

```text
local evidence + undeclared bridge
≠ configuration-function evidence

new target evidence
≠ original failure erased

configuration evidence
≠ person essence evidence
```

Primary site: [Chapter 38 WP2](../01_blocks/04_part_iii_retype.md#38-5-unmarked-level-mixing).

## Chapter 38 WP3 Evidence Routing

Scope extension requires evidence for each added coordinate and the relation carrying the target function into it. Temporal claims require formation-, phase-, interruption-, persistence-, dissolution-, and observation-window evidence rather than duration alone. Projection Loss requires evidence for what is preserved, compressed, excluded, uncertain, and irrecoverable plus explicit visibility change.

```text
one bounded case + similarity
≠ class-wide evidence

current persistence
≠ pre-formation or future evidence

complete target representation
≠ complete source preservation evidence
```

The Invalid Projection Record preserves original claim evidence, separately valid source material, prior failed dispositions, and the evidential burden of any reduced or new claim.

Primary site: [Chapter 38 WP3](../01_blocks/04_part_iii_retype.md#38-10-scope-inflation).



<a id="chapter-38-lock-and-chapter-39-preparation-evidence-sync"></a>

## Chapter 39 Prepared Evidence Burdens

| Evidence burden | Required support | Insufficient substitute |
|---|---|---|
| Functional Gain | target-side change in corridors, expectations, costs, interpretation, coordination, or continuation | new label or clearer prose |
| Constitutive Source Trace | source features, dependencies, relation path, and material source sensitivity | citation, historical mention, or target fit |
| Context Boundary | explicit target coordinates and bounded validity | generic domain resemblance |
| Counterfactual Sensitivity | material and irrelevant source variation, target conditions, rivals, and countercases | narrative plausibility |
| Analogy Boundary | preserved relation plus semantic and functional residuals | formal or executable mapping alone |
| Elasticity | stable failure conditions under opposite source and objection pressure | repeated relabeling or narrowing |
| Stop / Non-Capture | exact trigger, retained valid material, and route distinction | uncertainty alone |

<a id="chapter-39-wp1-evidence-sync"></a>

## Chapter 39 WP1 Evidence and Warrant Route

Lower-boundary warrant requires evidence of a concrete target-side difference relative to source-only and ordinary-domain rivals. Upper-boundary warrant requires constitutive source load rather than citation, historical mention, thematic resemblance, or retrospective target fit.

The `W/A–D` packets remain unadjudicated; WP1 records burdens and evidence locations only.

Primary site: [§§39.1–39.4](../01_blocks/04_part_iii_retype.md#39-1-lower-retype-boundary).

<a id="chapter-39-wp2-evidence-sync"></a>

## Chapter 39 WP2 Evidence and Warrant Route

A retained projection requires evidence for constitutive source features and relations, a reconstructible dependency path, complete target coordinates, and differentiated counterfactual response. Citation, narrative coherence, thematic similarity, or target fit may support context but cannot substitute for constitutive source load.

Opposite-source and source-removal pressure must use source-supported contrasts or explicitly bounded hypothetical variation; unsupported imaginary histories cannot be treated as evidence.

Primary site: [§39.8](../01_blocks/04_part_iii_retype.md#39-8-counterfactual-projection-test).

<a id="chapter-39-wp3-evidence-sync"></a>

## Chapter 39 WP3 Evidence Route

Alternatives require candidate-specific evidence and Loss. Elasticity requires a documented sequence of claim changes. Stop requires evidence that continuation depends on a prohibited move. Non-Capture must identify the unavailable discriminant and retained valid material.

<a id="chapter-39-lock-and-chapter-40-preparation-evidence-sync"></a>

## Chapter 39 Lock / Chapter 40 Evidence Burden

Chapter 40 case evidence must separate:

- source evidence and source reference;
- constitutive versus modulating source features;
- target-context evidence;
- Counterfactual Sensitivity and countercases;
- exact Loss and alternatives;
- local audit result and canonical output mapping;
- actual artifact existence from planned artifact obligations.

Existing smoke tests show formal routing behavior only. They do not establish the substantive warrant of Chapter-40 cases.

## Chapter 40 WP1 Evidence and Artifact Status

`P1–P7` currently possess canonical family prose only. Their synthetic source/target packets are method-demonstration structures, not empirical evidence records. No standalone Markdown case, YAML `PROJECT_AS` Record, Local Audit result, or canonical mapping record was produced. Existing smoke examples validate formal routing behavior only and do not discharge Chapter-40 evidence obligations.

<a id="chapter-40-wp2-evidence-sync"></a>

## Chapter 40 WP2 Evidence and Artifact Status

`N1–N7` possess canonical Layer-1 family prose only. The packets expose the evidence burdens for source identity, target coordinates, Source Trace, semantic preservation, relation topology, failure continuity, and person/configuration separation.

No countercase has an executed Local Audit, standalone Markdown case, YAML `PROJECT_AS` record, canonical mapping record, or selected Output Class. Existing smoke fixtures demonstrate formal route behavior only; they do not prove the substantive countercase claims.

<a id="chapter-40-wp3-evidence-sync"></a>

## Chapter 40 WP3 Evidence and Artifact Status

`X1–X6` possess canonical Layer-1 family prose only. Their packets identify the evidence required to distinguish source reconstruction, composite formation, Frame change, recurrent stabilizing load, contextual modulation, semantic preservation, and target function.

No confusion case has an instantiated standalone Markdown case, operation YAML record, Local Audit record, canonical mapping record, or selected Output Class. Existing smoke fixtures validate formal routing behavior only and do not prove a confusion-case result.


## Chapter 40 Lock Evidence and Chapter 41 Input Status

Evidence actually present for Chapter 40:

- complete canonical Layer-1 packets for 20 families;
- 24/24 Pressure Duties;
- all 32 Local Audit questions represented;
- canonical mapping matrix and closing boundaries;
- unchanged existing schemas, 37 Records, and eight Smoke fixtures;
- exact artifact-gap declaration.

Evidence not present:

- three lock-critical standalone Markdown cases;
- corresponding YAML `PROJECT_AS` Records;
- case-specific Local Audit results;
- case-specific canonical mappings.

The first set supports `admissible_with_bounded_claim` for method architecture. The second absence supports `mandatory_stop` for the artifact-complete lock claim. Chapter 41 inherits both dispositions without inferring missing evidence.
