# PMS-STRATA — Cross Reference Map

**Status:** active Reference Kernel artifact; corpus-audit synchronized 
**Repository role:** canonical ownership and cross-artifact routing; not an independent theory or authority source 
**Authority basis:** `PMS.yaml` → `00_source/PMS-STRATA_Structure.md` → `01_blocks/*` → `05_minified/*`; formal, case, appendix, and Reader artifacts remain subordinate to their canonical owners 
**Reference Freeze duty:** open bounded duty; this artifact may be corrected for ownership, routing, duplication, and carrier consistency without broadening any claim 

---

## 1. Role, Status, and Authority

This map routes controlled definitions, elaborations, applications, audits, formal carriers, cases, appendices, derivatives, and Reader paths. It does not define theory, repair missing prose by implication, or make a linked artifact more authoritative than its repository role permits.

```text
designated canonical site ≠ current control source
routing convenience ≠ authority inheritance
```

It shall:
- register one designated canonical definition site for each core term;
- distinguish definition, elaboration, application, audit, indexing, formalization, testing, templating, summarization, and routing;
- preserve repository authority order;
- route current corpus, case, Appendix, Formal Model, derivative, and Reader artifacts back to their governing owners;
- state open bounded duties without presenting them as completed claims.

It shall not introduce a fourth operation, a new Output Class, a new PMS primitive, a machine field, a case result, or an authority transfer.

## 2. Cross-Reference Semantics

| Relation | Navigation meaning | Authority limit |
| --- | --- | --- |
| defines | designated canonical primary definition site | one target only; canonical owner required |
| elaborates | expanded method, procedure, or boundary treatment | must not compete with the definition site |
| applies | local use of an established concept | no local redefinition |
| audits | tests an established rule, record, or transformation | audit cannot create theory |
| indexes | reference-layer navigation | no independent theory authority |
| formalizes | machine-readable operationalization | formal consistency is not truth or semantic validity |
| tests | case, countercase, confusion case, or smoke test | tests do not define theory |
| templates | record or appendix template handoff | template completeness is not substantive adequacy |
| summarizes | conclusion, front matter, or derivative presentation | summary cannot broaden the claim |
| routes | reader or repository navigation | routing is not authority ranking |

### 2.1 Local navigation statuses

| Status | Meaning |
| --- | --- |
| active canonical owner | existing canonical prose controls the concept or rule |
| active architecture control | Structure controls architecture and chapter placement |
| active binding control | a minified artifact or contract constrains the corpus under prose precedence |
| active Reference control | a Reference artifact controls terminology, ownership, evidence, audit, or navigation |
| active formal carrier | a model artifact operationalizes declared structure without deciding substantive truth |
| active case pressure | a case, countercase, confusion case, chain, Stop, or Non-Capture record tests a rule |
| active Appendix carrier | an Appendix operationalizes, templates, indexes, or stress-tests an existing owner |
| bounded partial duty | a declared comparison, source, calibration, or coverage duty remains incomplete |
| open bounded duty | a corpus-maintenance obligation has a stated completion condition |
| excluded provenance | archived workflow material has no active theory, evidence, model, case, or Reader role |

```text
navigation status ≠ record status ≠ canonical output class
```

Internal artifacts use full repository paths in registries and handoff tables. Short labels do not alter ownership.

## 3. Authority and Repository Map

### 3.1 External governing reference

| External reference | Authority and function | Packaging status | No-authority rule |
| --- | --- | --- | --- |
| `PMS.yaml` | unchanged PMS Base grammar and Δ–Ψ inventory | governing external reference; not packaged as an internal STRATA repository artifact | not rewritten, reordered, decomposed, extended, or made subordinate by STRATA references |

```text
external governing reference
≠
packaged repository artifact
```

### 3.2 Internal STRATA repository authority

| Internal layer | Authority and function | No-authority rule |
| --- | --- | --- |
| `00_source/PMS-STRATA_Structure.md` | architecture and chapter blueprint | not a substitute for canonical prose |
| `01_blocks/*` | canonical corpus prose, Front Matter through Conclusion | no authority beyond declared claim and source ceilings |
| `02_appendices/*` | operationalization, notation, templates, tests, and indices | no competing definitions or new primitives |
| `03_cases/*` | case and chain pressure | tests rules; does not define them |
| `04_reference/*` | terminology, ownership, routing, evidence, audit, and reader navigation | no independent theory authority |
| `05_minified/*` | binding compact controls | subordinate to canonical prose |
| `06_derivative_publications/*` | derivative presentation | no back-propagation |
| `07_model/*` | formal operationalization and structural validation | no truth, causality, normativity, diagnosis, or authority decision |
| `08_PMS-STRATA Reader/*` | browsing and visualization | presentation is not authority |

Linking an artifact to `PMS.yaml` records source authority; it does not transfer PMS-Base authority to the linked artifact.

## 4. Active Artifact Registry

| Layer | Active role | Canonical return | Authority boundary |
| --- | --- | --- | --- |
| `PMS.yaml` | unchanged PMS Base grammar and Δ–Ψ control | itself | external governing reference; not rewritten by STRATA |
| `00_source/PMS-STRATA_Structure.md` | architecture and chapter blueprint | PMS Base and canonical corpus | architecture is not completed prose |
| `01_blocks/*` | canonical corpus prose, Front Matter through Conclusion | designated chapter owners | no authority beyond declared claim boundaries |
| `02_appendices/*` | operationalization, notation, templates, tests, and indices | governing chapters and References | no competing definitions |
| `03_cases/*` | positive, negative, confusion, chain, Stop, and Non-Capture pressure | governing rules and chapters | cases test; they do not define theory |
| `04_reference/*` | terminology, ownership, routing, evidence, audit, and reader navigation | canonical definition sites | no independent theory authority |
| `05_minified/*` | binding control artifacts | canonical prose | control compression does not outrank prose |
| `06_derivative_publications/*` | derivative presentation | locked corpus | no back-propagation |
| `07_model/*` | formal operationalization and consistency validation | prose, controls, and Reference owners | machine consistency is not truth proof |
| `08_PMS-STRATA Reader/*` | non-authoritative browsing and visualization | active repository artifacts | presentation is not authority |

## 5. Corpus Block Map

| Corpus unit | Chapters | Primary file | Current function |
| --- | ---: | --- | --- |
| Front Matter | — | `01_blocks/00_front_matter.md` | entry, authority, claim, and reading boundary |
| Foundations | 0–8 | `01_blocks/01_foundations.md` | objects, coordinates, temporality, operations, admissibility, records, non-equivalences |
| PATH | 9–17 | `01_blocks/02_part_i_path.md` | temporal composition and COMPOSE |
| SUB | 18–28 | `01_blocks/03_part_ii_sub.md` | decomposition under finer resolution |
| RETYPE | 29–40 | `01_blocks/04_part_iii_retype.md` | bounded contextual PROJECT_AS functions |
| LIMITS | 41–53 | `01_blocks/05_part_iv_limits.md` | relevance, traceability, continuity, source, Stop, Failure, Non-Capture, audit |
| Conclusion | 54–57 | `01_blocks/06_conclusion.md` | integrated chains, positive capability, negative scope, final bounded claim |

## 6. Chapter Registry 0–57

| Ch. | Title | Part | Target Block | Primary concept family | Current contract source | Reference handoff | Model/case handoff | Anchor status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Position and Claim Boundary | Foundations | `01_blocks/01_foundations.md` | claim and authority boundary | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Claim_Type_Table.md`; `05_minified/PMS_STRATA_Claim_Boundary_Minified.md` | no semantic Formal Model revision required | active canonical owner |
| 1 | Object Model: Operator Type, Operator Occurrence, and Composite Structure | Foundations | `01_blocks/01_foundations.md` | object model | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Operator_Index.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Claim_Type_Table.md` | `07_model/Operation_Registry.yaml` object-model carrier; Record Schema unchanged | active canonical owner |
| 2 | Frame, Granularity, and Relative Level | Foundations | `01_blocks/01_foundations.md` | analytical coordinates and scopes | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Claim_Type_Table.md` | `07_model/Operation_Registry.yaml`; `07_model/Transformation_Record.schema.json` coordinate carriers | active canonical owner |
| 3 | Configuration, Event, Non-Event, Transition, Path, and Trajectory | Foundations | `01_blocks/01_foundations.md` | full temporal object and historical-property architecture | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Operator_Index.md`; `04_reference/Claim_Type_Table.md` | `07_model/Operation_Registry.yaml` temporal-object carrier; Record Schema unchanged | active canonical owner |
| 4 | The Three STRATA Operations: COMPOSE, DECOMPOSE, and PROJECT_AS | Foundations | `01_blocks/01_foundations.md` | operation grammar | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Claim_Type_Table.md` | `07_model/Operation_Registry.yaml`; exactly three operations | active canonical owner |
| 5 | Origin Type, Target Function, and Transformation Context | Foundations | `01_blocks/01_foundations.md` | type, function, context, and continuity | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` continuity carrier | active canonical owner |
| 6 | The STRATA Admissibility Band | Foundations | `01_blocks/01_foundations.md` | Admissibility Band and output architecture | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 7 | Shared Transformation Record | Foundations | `01_blocks/01_foundations.md` | shared transformation record | `05_minified/Chapter_Contracts.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md`; `04_reference/Evidence_Map.md` | `07_model/Transformation_Record.schema.json`; `07_model/PMS-STRATA.schema.json` | active canonical owner |
| 8 | Foundational Non-Equivalences | Foundations | `01_blocks/01_foundations.md` | foundational non-equivalences | `05_minified/Chapter_Contracts.md` | `04_reference/Non_Equivalence_Index.md` | `07_model/Boundary_Decision_Tree.yaml` bounded handoff | active canonical owner |
| 9 | Temporal Order and Transition | PATH | `01_blocks/02_part_i_path.md` | temporal order and transition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | active canonical owner |
| 10 | Path | PATH | `01_blocks/02_part_i_path.md` | path | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | active canonical owner |
| 11 | Trajectory | PATH | `01_blocks/02_part_i_path.md` | trajectory | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | active canonical owner |
| 12 | Path Dependence and Sedimentation | PATH | `01_blocks/02_part_i_path.md` | path dependence and sedimentation | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | active canonical owner |
| 13 | Branches, Aborts, Delays, and Unavailable Alternatives | PATH | `01_blocks/02_part_i_path.md` | alternatives and branch structure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | active canonical owner |
| 14 | Non-Events within Paths and Trajectories | PATH | `01_blocks/02_part_i_path.md` | non-events in temporal composites | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | active canonical owner |
| 15 | COMPOSE: Selection, Formation, and Compression | PATH | `01_blocks/02_part_i_path.md` | COMPOSE procedure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | `07_model/Operation_Registry.yaml` | active canonical owner |
| 16 | PATH Boundary Conditions | PATH | `01_blocks/02_part_i_path.md` | PATH limits | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | active canonical owner; bounded same-source case-comparison duty |
| 17 | PATH Cases, Countercases, and Local Audit | PATH | `01_blocks/02_part_i_path.md` | PATH cases and local audit | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | `03_cases/Case_Index.md`; paired PATH case records | active canonical owner |
| 18 | The Provisionally Compressed Object | SUB | `01_blocks/03_part_ii_sub.md` | provisional elementarity and compressed source-object entry | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Operator_Index.md`; `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Evidence_Map.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml` bounded compressed-object carrier; schema unchanged | active canonical owner |
| 19 | Granularity Change and the Logic of Decomposition | SUB | `01_blocks/03_part_ii_sub.md` | source-to-target granularity relation | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Evidence_Map.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml` granularity carrier; schema unchanged | active canonical owner |
| 20 | DECOMPOSE: Conditions, Procedure, and Preservation Requirements | SUB | `01_blocks/03_part_ii_sub.md` | complete generic DECOMPOSE procedure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | `07_model/Operation_Registry.yaml`; `07_model/Admissibility_Rules.yaml` | active canonical owner |
| 21 | Decomposing Operator-Typed Occurrences | SUB | `01_blocks/03_part_ii_sub.md` | operator-occurrence decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | active canonical owner |
| 22 | Decomposing Composite Structures | SUB | `01_blocks/03_part_ii_sub.md` | composite decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | active canonical owner |
| 23 | Decomposing Events, Non-Events, and Internal Temporal Structures | SUB | `01_blocks/03_part_ii_sub.md` | event and internal-temporal decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | active canonical owner |
| 24 | Decomposing Paths and Trajectories | SUB | `01_blocks/03_part_ii_sub.md` | path and trajectory decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | active canonical owner |
| 25 | Resolution Gain, Neutrality, Drift, and Escape | SUB | `01_blocks/03_part_ii_sub.md` | resolution results | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | active canonical owner; bounded same-source case-comparison duty |
| 26 | The Boundary between SUB and RETYPE | SUB | `01_blocks/03_part_ii_sub.md` | SUB–RETYPE boundary | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | active canonical owner |
| 27 | SUB Boundary Conditions | SUB | `01_blocks/03_part_ii_sub.md` | SUB limits | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | active canonical owner |
| 28 | SUB Cases, Countercases, and Local Audit | SUB | `01_blocks/03_part_ii_sub.md` | SUB cases and local audit | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | `03_cases/Case_Index.md`; paired SUB case records | active canonical owner |
| 29 | Functional Projection without Origin-Type Replacement | RETYPE | `01_blocks/04_part_iii_retype.md` | functional projection and type preservation | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | active canonical owner |
| 30 | PROJECT_AS: Signature, Context, and Validity Scope | RETYPE | `01_blocks/04_part_iii_retype.md` | PROJECT_AS procedure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Operation_Registry.yaml`; `07_model/Admissibility_Rules.yaml` | active canonical owner |
| 31 | Trajectory as Frame-Function | RETYPE | `01_blocks/04_part_iii_retype.md` | frame-function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` bounded functional carrier | active canonical owner |
| 32 | Trajectory as Macro-Event | RETYPE | `01_blocks/04_part_iii_retype.md` | macro-event function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` bounded functional carrier | active canonical owner |
| 33 | Recurrent Trajectory Form as Attractor-Function | RETYPE | `01_blocks/04_part_iii_retype.md` | attractor-function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` bounded functional carrier | active canonical owner |
| 34 | Composite Structures as Higher-Level Functions | RETYPE | `01_blocks/04_part_iii_retype.md` | higher-level function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` bounded functional carrier | active canonical owner |
| 35 | Operator Weighting, Modulation, and Emergent Functional Profiles | RETYPE | `01_blocks/04_part_iii_retype.md` | operator weighting and profiles | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` bounded functional carrier | active canonical owner |
| 36 | Competing Projections | RETYPE | `01_blocks/04_part_iii_retype.md` | competing projections | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` bounded functional carrier | active canonical owner |
| 37 | Projection, Structural Analogy, and Label Substitution | RETYPE | `01_blocks/04_part_iii_retype.md` | projection, analogy, and substitution | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | active canonical owner |
| 38 | Invalid Type Jumps and Unmarked Level Mixing | RETYPE | `01_blocks/04_part_iii_retype.md` | invalid type jumps and level mixing | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | active canonical owner |
| 39 | RETYPE Boundary Conditions | RETYPE | `01_blocks/04_part_iii_retype.md` | RETYPE limits | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | active canonical owner |
| 40 | RETYPE Cases, Countercases, and Local Audit | RETYPE | `01_blocks/04_part_iii_retype.md` | RETYPE cases and local audit | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `03_cases/Case_Index.md`; paired RETYPE case records | active canonical owner |
| 41 | Why STRATA Must Bound Itself | LIMITS | `01_blocks/05_part_iv_limits.md` | constitutive LIMITS rationale | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | formal handoff only where declared by chapter contract | active canonical owner |
| 42 | No Ontology of Strata | LIMITS | `01_blocks/05_part_iv_limits.md` | anti-ontology | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | formal handoff only where declared by chapter contract | active canonical owner |
| 43 | No Privilege of Finer Resolution or Higher Composition | LIMITS | `01_blocks/05_part_iv_limits.md` | no resolution or composition privilege | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | formal handoff only where declared by chapter contract | active canonical owner |
| 44 | Praxeological Relevance Floor | LIMITS | `01_blocks/05_part_iv_limits.md` | Praxeological Relevance Floor | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 45 | Praxeological Traceability Ceiling | LIMITS | `01_blocks/05_part_iv_limits.md` | Praxeological Traceability Ceiling | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 46 | Counterfactual Sensitivity | LIMITS | `01_blocks/05_part_iv_limits.md` | Counterfactual Sensitivity | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 47 | Reference, Type, and Function Continuity | LIMITS | `01_blocks/05_part_iv_limits.md` | continuity audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 48 | Compression Loss and Reconstruction Selection | LIMITS | `01_blocks/05_part_iv_limits.md` | loss audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 49 | Source Limits and Calibration Limits | LIMITS | `01_blocks/05_part_iv_limits.md` | Source Ceiling and calibration | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 50 | Anti-Immunization | LIMITS | `01_blocks/05_part_iv_limits.md` | anti-immunization | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 51 | Stop Conditions | LIMITS | `01_blocks/05_part_iv_limits.md` | Stop method | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 52 | Non-Capture | LIMITS | `01_blocks/05_part_iv_limits.md` | Non-Capture method | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 53 | Integrated STRATA Admissibility Audit | LIMITS | `01_blocks/05_part_iv_limits.md` | Integrated STRATA Admissibility Audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | active canonical owner |
| 54 | The Integrated STRATA Model | Conclusion | `01_blocks/06_conclusion.md` | integrated results | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | active canonical owner |
| 55 | What PMS-STRATA Provides | Conclusion | `01_blocks/06_conclusion.md` | relation to PMS Base | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | active canonical owner |
| 56 | What PMS-STRATA Does Not Provide | Conclusion | `01_blocks/06_conclusion.md` | negative provision registry | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | active canonical owner |
| 57 | Final Claim Boundary | Conclusion | `01_blocks/06_conclusion.md` | final claim and closure | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | active canonical owner |

### 6.1 Chapter relation rules

- The registry records primary concept ownership but does not copy hard and conditional dependency lists from `Chapter_Contracts.md`.
- Chapters 17, 28, and 40 are local audits; Chapter 53 is the integrated audit. Local results remain preserved.
- Chapters 44–52 elaborate limits already active in PATH, SUB, RETYPE, and operation chains.
- Chapters 54–57 synthesize and close; they do not introduce a new operation, output class, empirical result, or authority.

---

## 7. Front-Matter Registry

| Unit | Title | Function | Target Block | Reference handoff | Anchor status |
| --- | --- | --- | --- | --- | --- |
| FM-PREFACE | Preface | motivation without theory definition | `01_blocks/00_front_matter.md` | development history and orientation only | canonical anchor available |
| FM-STATUS-SCOPE | Status and Scope Note | status, scope, and entry boundaries without replacing Chapters 0 or 56 | `01_blocks/00_front_matter.md` | Chapters 0 and 56; README status | canonical anchor available |
| FM-TERMINOLOGY-NOTATION | Terminology and Notation Note | notation guidance without new semantics | `01_blocks/00_front_matter.md` | `04_reference/Glossary.md`; `04_reference/Operator_Index.md`; `04_reference/Non_Equivalence_Index.md` | canonical anchor available |
| FM-HOW-TO-READ | How to Read PMS-STRATA | reading navigation without authority ranking | `01_blocks/00_front_matter.md` | `04_reference/Reader_Pathways.md`; repository `README.md` | canonical anchor available |

```text
orientation site
≠
canonical theory definition site
```

---

## 8. Core Concept Definition Map

`04_reference/Glossary.md` is the term registry for all rows below. The table therefore records the principal specialist handoff rather than repeating the Glossary path 112 times. It registers spelling, destination, current control, and navigation status only; definitions and non-equivalences remain in the substantive Reference artifacts.

| Term | Glossary family | Designated canonical site | Current control sources | Principal specialist handoff | Anchor status |
| --- | --- | --- | --- | --- | --- |
| `PMS Base` | A. Project, Claim, and Authority | PMS.yaml | `PMS.yaml` | `04_reference/Operator_Index.md` | canonical anchor available |
| `PMS-STRATA` | A. Project, Claim, and Authority | Chapter 0 — Position and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `05_minified/PMS_STRATA_Minified_Canonical.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `bounded transformation discipline` | A. Project, Claim, and Authority | Chapter 0 — Position and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `governing claim` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `claim boundary` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `claim type` | A. Project, Claim, and Authority | Chapter 7 — Shared Transformation Record | `04_reference/Claim_Type_Table.md`; `05_minified/PMS_STRATA_Minified_Canonical.md`; `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `claim ceiling` | A. Project, Claim, and Authority | Chapter 5 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `No Meta-PMS` | A. Project, Claim, and Authority | Chapter 0 — Position and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Non_Equivalence_Index.md` | canonical anchor available |
| `No Ontology of Strata` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Non_Equivalence_Index.md` | canonical anchor available |
| `No Universal STRATA Scale` | A. Project, Claim, and Authority | Chapter 6 — The STRATA Admissibility Band | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Non_Equivalence_Index.md` | canonical anchor available |
| `authority inheritance` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `authority ceiling` | A. Project, Claim, and Authority | Chapter 0 — Governing Claim and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `04_reference/Admissibility_Band_Reference.md`; `01_blocks/01_foundations.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `more structure ≠ more authority` | A. Project, Claim, and Authority | Chapter 0 | `README.md`; `05_minified/PMS_STRATA_Minified_Canonical.md`; `01_blocks/01_foundations.md` | `04_reference/Non_Equivalence_Index.md` | canonical anchor available |
| `operator occurrence` | B. Object Model | Chapter 1 — Object Model | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Operator_Index.md` | canonical anchor available |
| `composite structure` | B. Object Model | Chapter 1 — Object Model | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `configuration` | B. Object Model | Chapter 1 as object category | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `state` | B. Object Model | Chapter 3 — Temporal Object Chain | `00_source/PMS-STRATA_Structure.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `event-like object` | B. Object Model | Chapter 1 — Object Model | `00_source/PMS-STRATA_Structure.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `event` | B. Object Model | Chapter 3 — Temporal Object Chain | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `non-event` | B. Object Model | Chapter 3 temporal category | `PMS.yaml`; `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `transition` | B. Object Model | Chapter 3 temporal category | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `derived analytical object` | B. Object Model | Chapter 1 — Object Model | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `reference identity` | B. Object Model | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `source object` | B. Object Model | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `target object` | B. Object Model | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `provisional elementarity` | B. Object Model | Chapter 18 — Provisionally Compressed Object | `00_source/PMS-STRATA_Structure.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `compressed object` | B. Object Model | Chapter 18 — Provisionally Compressed Object | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `transformation context` | C. Analytical Coordinates and Scopes | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `target context` | C. Analytical Coordinates and Scopes | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `validity scope` | C. Analytical Coordinates and Scopes | Chapter 5 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `sequence` | D. Temporal and Path Structures | Chapter 3 — Temporal Object Chain | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `path` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `trajectory` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `path dependence` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `sedimentation` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `irreversibility` | D. Temporal and Path Structures | Chapter 3 — Temporal Object Chain | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `unrealized alternative` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `historical load` | D. Temporal and Path Structures | Chapter 11 — Trajectory | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `STRATA operation` | E. Operations and Transformation Records | Chapter 4 — The Three STRATA Operations | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `COMPOSE` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `DECOMPOSE` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `PROJECT_AS` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `operation occurrence` | E. Operations and Transformation Records | Chapter 4 — The Three STRATA Operations | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `operation chain` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `non-invertibility` | E. Operations and Transformation Records | Chapter 4 — The Three STRATA Operations | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `shared transformation record` | E. Operations and Transformation Records | Chapter 7 — Shared Transformation Record | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `record status` | E. Operations and Transformation Records | Chapter 7 — Shared Transformation Record | `05_minified/PMS_STRATA_Minified_Canonical.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md`; `04_reference/Evidence_Map.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` | canonical anchor available |
| `operation-specific result` | E. Operations and Transformation Records | Chapter 6 — The STRATA Admissibility Band | `05_minified/PMS_STRATA_Minified_Canonical.md`; `04_reference/Transformation_Operation_Index.md`; `04_reference/Output_Class_Index.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `origin type` | F. Projection, Functions, and Profiles | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `target function` | F. Projection, Functions, and Profiles | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `source function` | F. Projection, Functions, and Profiles | Chapter 20 — DECOMPOSE | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `functional projection` | F. Projection, Functions, and Profiles | Chapter 29 — Functional Projection | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `frame-function` | F. Projection, Functions, and Profiles | Chapter 31 — Trajectory as Frame-Function | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `macro-event` | F. Projection, Functions, and Profiles | Chapter 32 — Trajectory as Macro-Event | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `attractor-function` | F. Projection, Functions, and Profiles | Chapter 33 — Recurrent Trajectory Form as Attractor-Function | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `higher-level function` | F. Projection, Functions, and Profiles | Chapter 34 — Composite Structures as Higher-Level Functions | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `operator weighting` | F. Projection, Functions, and Profiles | Chapter 35 — Operator Weighting and Modulation | `00_source/PMS-STRATA_Structure.md` | `04_reference/Operator_Index.md` | canonical anchor available |
| `modulator` | F. Projection, Functions, and Profiles | Chapter 35 — Operator Weighting and Modulation | `00_source/PMS-STRATA_Structure.md` | `04_reference/Operator_Index.md` | canonical anchor available |
| `modulating profile` | F. Projection, Functions, and Profiles | Chapter 35 — Operator Weighting and Modulation | `00_source/PMS-STRATA_Structure.md` | `04_reference/Operator_Index.md` | canonical anchor available |
| `structural analogy` | F. Projection, Functions, and Profiles | Chapter 37 — Projection, Structural Analogy, and Label Substitution | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `label substitution` | F. Projection, Functions, and Profiles | Chapter 37 — Projection, Structural Analogy, and Label Substitution | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `invalid type jump` | F. Projection, Functions, and Profiles | Chapter 38 — Invalid Type Jumps and Level Mixing | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `level mixing` | F. Projection, Functions, and Profiles | Chapter 38 — Invalid Type Jumps and Level Mixing | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `granularity mixing` | F. Projection, Functions, and Profiles | Chapter 38 — Invalid Type Jumps and Level Mixing | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `STRATA Admissibility Band` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 — STRATA Admissibility Band | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `admissible transformation` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `Praxeological Relevance Floor` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `PraxisPurchase` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `Changed-Reconstruction Test` | G. Admissibility, Continuity, Source, and Loss | Chapter 44 — Praxeological Relevance Floor | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `resolution gain` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `resolution neutrality` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `resolution drift` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 — Resolution Gain, Neutrality, Drift, and Escape | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `resolution escape` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `Praxeological Traceability Ceiling` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `TraceableLoad` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `Constitutive Source Trace` | G. Admissibility, Continuity, Source, and Loss | Chapter 45 — Praxeological Traceability Ceiling | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `Counterfactual Sensitivity` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `Type Integrity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `reference continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `type continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `functional continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `temporal continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `contextual boundedness` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `loss` | G. Admissibility, Continuity, Source, and Loss | Chapter 7 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `source basis` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md` | `04_reference/Evidence_Map.md` | canonical anchor available |
| `support mode` | G. Admissibility, Continuity, Source, and Loss | Chapter 7 — Shared Transformation Record | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md` | `04_reference/Evidence_Map.md` | canonical anchor available |
| `support status` | G. Admissibility, Continuity, Source, and Loss | Chapter 7 — Shared Transformation Record | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Evidence_Map.md` | canonical anchor available |
| `evidence availability` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md` | `04_reference/Evidence_Map.md` | canonical anchor available |
| `Source Ceiling` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `calibration` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `anti-immunization` | G. Admissibility, Continuity, Source, and Loss | Chapter 50 — Anti-Immunization | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `canonical output class` | H. Results, Stop, Non-Capture, and Audit | Chapter 6 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Output_Class_Index.md` | canonical anchor available |
| `claim reduction` | H. Results, Stop, Non-Capture, and Audit | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `stop` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `mandatory stop` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Output_Class_Index.md` | canonical anchor available |
| `optional stop` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `re-entry` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `failed transformation` | H. Results, Stop, Non-Capture, and Audit | Chapter 6 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Output_Class_Index.md` | canonical anchor available |
| `Non-Capture` | H. Results, Stop, Non-Capture, and Audit | Chapter 52 — Non-Capture | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `non-equivalence` | H. Results, Stop, Non-Capture, and Audit | Chapter 8 — Foundational Non-Equivalences | `05_minified/Chapter_Contracts.md`; `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Non_Equivalence_Index.md` | canonical anchor available |
| `local audit` | H. Results, Stop, Non-Capture, and Audit | Chapter 17 — PATH Cases, Countercases, and Local Audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | canonical anchor available |
| `Integrated STRATA Admissibility Audit` | H. Results, Stop, Non-Capture, and Audit | Chapter 53 — Integrated STRATA Admissibility Audit | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `formal model boundary` | H. Results, Stop, Non-Capture, and Audit | Chapter 49 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |

### 8.1 Definition-site rule

A term may have one designated canonical definition site and multiple elaboration, application, audit, or index sites. A later detailed chapter does not become a competing definition site merely because it carries the fuller procedure.

```text
canonical definition site
≠
primary elaboration and audit site
```

---

## 9. PMS Operator Map

| Order | Operator | Name | PMS dependencies | Canonical source | Reference handoff | Relevant application routes | Critical boundary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Δ | Difference | none | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 1, 3, 21 | difference ≠ asymmetry |
| 2 | ∇ | Impulse | Δ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 1, 3, 21 | impulse ≠ intention |
| 3 | □ | Frame | Δ, ∇ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 2, 3, 5, 14, 31 | Frame operator type ≠ analytical frame coordinate |
| 4 | Λ | Non-Event | □ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 3, 14, 23 | non-event ≠ missing information |
| 5 | Α | Attractor | Δ, ∇, □, Λ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 3, 11, 12, 33 | recurrence ≠ Attractor operator type |
| 6 | Ω | Asymmetry | Α | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 3, 12, 35 | asymmetry ≠ moral hierarchy |
| 7 | Θ | Temporality | Ω, Α | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 3, 9–12, 24, 31–32 | temporality ≠ trajectory |
| 8 | Φ | Recontextualization | Θ, Ω, □ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 5, 29–30, 37 | Recontextualization ≠ PROJECT_AS |
| 9 | Χ | Distance | Φ, Θ, □ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 5, 35, 47 | distance ≠ passivity |
| 10 | Σ | Integration | Χ, Φ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 1, 34–35, 47 | PMS Integration ≠ STRATA COMPOSE |
| 11 | Ψ | Self-Binding | Σ, Θ, Χ | `PMS.yaml` | `04_reference/Operator_Index.md` | Chapters 3, 11, 35, 55 | self-binding ≠ moral worth |

PMS operator layer, STRATA Part, relative level, granularity, and authority rank remain distinct. The map does not reorder, decompose, rename, or extend Δ–Ψ.

```text
application route
≠
operator dependency
≠
definition site
```

---

## 10. STRATA Operation Map

| Operation | Shared definition | Procedure | Local limits | Local audit | Reference control | Formal handoff |
| --- | --- | --- | --- | --- | --- | --- |
| `COMPOSE` | Chapter 4 | Chapter 15 | Chapter 16 | Chapter 17 | `04_reference/Transformation_Operation_Index.md` | `07_model/Operation_Registry.yaml` |
| `DECOMPOSE` | Chapter 4 | Chapter 20 | Chapter 27 | Chapter 28 | `04_reference/Transformation_Operation_Index.md` | `07_model/Operation_Registry.yaml` |
| `PROJECT_AS` | Chapter 4 | Chapter 30 | Chapter 39 | Chapter 40 | `04_reference/Transformation_Operation_Index.md` | `07_model/Operation_Registry.yaml` |

```text
operation chain
≠
fourth compound operation
```

All chain records route additionally to Chapter 7, Chapter 53, `04_reference/Transformation_Operation_Index.md`, active case records, and `07_model/*`. Each occurrence retains its own claim, loss, and output class.

---

## 11. Canonical Output-Class Map

| Canonical value | Primary output architecture | Method or application elaboration | Reference control | Formal handoff |
| --- | --- | --- | --- | --- |
| `admissible` | Chapter 6 | Chapter 53 integrated application | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/admissible` |
| `admissible_with_bounded_claim` | Chapter 6 | Chapters 5, 30, 49, 53 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/admissible_with_bounded_claim` |
| `admissible_but_provisional` | Chapter 6 | Chapters 17, 28, 40, 49, 53 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/admissible_but_provisional` |
| `resolution_neutral` | Chapter 6 | Chapters 25 and 44 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/resolution_neutral` |
| `analogy_only` | Chapter 6 | Chapter 37 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/analogy_only` |
| `partially_admissible` | Chapter 6 | local audits Chapters 17, 28, 40; Chapter 53 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/partially_admissible` |
| `claim_reduction_required` | Chapter 6 | Chapters 49–51 and local audits | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/claim_reduction_required` |
| `mandatory_stop` | Chapter 6 | Stop method Chapter 51 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/mandatory_stop` |
| `failed_transformation` | Chapter 6 | operation boundaries Chapters 16, 27, 39; Chapter 53 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/failed_transformation` |
| `non_capture` | Chapter 6 | Non-Capture method Chapter 52 | `04_reference/Output_Class_Index.md` | `07_model/Output_Classes.yaml` — current owner path `/output_classes/non_capture` |

```text
stop
≠
mandatory_stop
```

```text
Non-Capture
≠
non_capture
```

The method concepts are primary in Chapters 51 and 52. Their canonical output values remain part of the Chapter 6 output architecture.

---

## 12. Claim Architecture Map

| Claim family | Operation or method context | Primary chapter route | Reference and audit handoff |
| --- | --- | --- | --- |
| object and typing | shared / all operations | Chapters 1, 5, 7 | `04_reference/Claim_Type_Table.md`; `04_reference/Operator_Index.md` |
| temporal ordering | COMPOSE / PATH | Chapters 9–10 | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` |
| path formation and branch closure | COMPOSE / PATH | Chapters 10, 13, 15 | `04_reference/Claim_Type_Table.md` |
| trajectory and sedimentation | COMPOSE / PATH | Chapters 11–12, 15 | `04_reference/Claim_Type_Table.md` |
| path dependence | COMPOSE / PATH | Chapter 12 | `04_reference/Claim_Type_Table.md` |
| declared composite and formation rule | COMPOSE | Chapter 15 | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` |
| internal structure and decomposition | DECOMPOSE / SUB | Chapters 19–24 | `04_reference/Claim_Type_Table.md` |
| component load, substitutability, compensation, remainder | DECOMPOSE / SUB | Chapters 21–22 | `04_reference/Claim_Type_Table.md` |
| source function | DECOMPOSE / SUB | Chapters 20–25 | `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` |
| resolution gain | DECOMPOSE / SUB | Chapter 25 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` |
| functional projection and target function | PROJECT_AS / RETYPE | Chapters 29–36 | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` |
| structural analogy | RETYPE / comparison | Chapter 37 | `04_reference/Claim_Type_Table.md`; `04_reference/Non_Equivalence_Index.md` |
| continuity and integrity | shared admissibility | Chapters 5 and 47 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` |
| admissibility and governance | shared admissibility | Chapters 6 and 44–53 | `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` |
| capture, partial capture, and non-capture | LIMITS / audit | Chapters 52–53 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` |

Claim roles such as prior, successor, rival, revised, or withdrawn are record relations or dispositions, not new claim families. Claim type, scope, ceiling, support status, operation result, and output class remain separate.

---

## 13. Admissibility and LIMITS Map

| Common check | Canonical definition route | Primary elaboration or audit | Reference control | Formal handoff |
| --- | --- | --- | --- | --- |
| PraxisPurchase | Chapter 6 | Chapter 44 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| TraceableLoad | Chapter 6 | Chapter 45 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| TypeIntegrity | Chapter 5 | Chapters 38, 47 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| ReferenceContinuity | Chapter 5 | Chapter 47 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Transformation_Record.schema.json` |
| FunctionalContinuity | Chapter 5 | Chapter 47 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Transformation_Record.schema.json` |
| TemporalContinuity | Chapter 5 | Chapter 47 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Transformation_Record.schema.json` |
| ContextualBoundedness | Chapter 5 | Chapters 30, 47, 49 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| CounterfactualSensitivity | Chapter 6 | Chapter 46 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| SourceCeiling | Chapter 49 | Chapters 45, 53 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| Calibration | Chapter 49 | Chapter 53 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| SelectionAndLoss | Chapters 7 and 15 | Chapter 48 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Transformation_Record.schema.json` |
| Alternatives | Chapters 7 and 13 | Chapters 49, 53 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Transformation_Record.schema.json` |
| ClaimCeiling | Chapter 5 | Chapters 49, 53 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| AuthorityCeiling | Chapter 0 | Chapters 41, 53, 56 | `04_reference/Admissibility_Band_Reference.md` | `07_model/Admissibility_Rules.yaml` |
| Stop | Chapter 51 | Chapter 53 | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | `07_model/Boundary_Decision_Tree.yaml` |
| NonCapture | Chapter 52 | Chapter 53 | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | `07_model/Boundary_Decision_Tree.yaml` |

### 13.1 Band topology routing

| Boundary | Governing role | Primary route | Reference control |
| --- | --- | --- | --- |
| Praxeological Relevance Floor | excludes distinction without praxeological purchase | Chapter 6 → Chapter 44 | `04_reference/Admissibility_Band_Reference.md` |
| Source Ceiling | limits detail, precision, and inference by available support | Chapter 49 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` |
| Praxeological Traceability Ceiling | excludes abstraction or fragmentation without traceable load | Chapter 6 → Chapter 45 | `04_reference/Admissibility_Band_Reference.md` |
| Claim Ceiling | limits the maximum warranted structural assertion | Chapter 5 → Chapters 49 and 53 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` |
| authority ceiling | blocks authority inheritance and prohibited inference | Chapter 0 → Chapters 41, 53, 56 | `04_reference/Admissibility_Band_Reference.md` |

Passing the Floor and Ceiling does not by itself establish full admissibility. The checks are non-compensatory and route to the ten canonical output classes only through a record- and claim-bound judgment.

---

## 14. Non-Equivalence Routing

| Non-equivalence family | Primary collection or elaboration | Complete registry |
| --- | --- | --- |
| foundational object, coordinate, temporal, and authority pairs | Chapter 8 | `04_reference/Non_Equivalence_Index.md` |
| PMS operator boundaries | `04_reference/Operator_Index.md` | `04_reference/Non_Equivalence_Index.md` |
| operation identity, non-invertibility, and chain boundaries | `04_reference/Transformation_Operation_Index.md` | `04_reference/Non_Equivalence_Index.md` |
| claim type, reach, ceiling, status, reduction, and authority boundaries | `04_reference/Claim_Type_Table.md` | `04_reference/Non_Equivalence_Index.md` |
| output-class collision boundaries | `04_reference/Output_Class_Index.md` | `04_reference/Non_Equivalence_Index.md` |
| Floor, Ceiling, continuity, source, loss, stop, and capture boundaries | `04_reference/Admissibility_Band_Reference.md` | `04_reference/Non_Equivalence_Index.md` |
| cross-file routing and anchor roles | this map | `04_reference/Non_Equivalence_Index.md` only where a substantive collapse is blocked |

Critical cross-file pairs include:

```text
designated canonical site ≠ current control source
definition ≠ elaboration ≠ application ≠ audit
navigation status ≠ record status ≠ output class
formal handoff ≠ substantive validation
case test ≠ theory definition
Reader route ≠ authority hierarchy
```

The current Non-Equivalence registry is controlled in `04_reference/Non_Equivalence_Index.md` and is not duplicated here.

---

## 15. Shared Record and Schema Handoffs

| Record concern | Canonical prose route | Current controls | Current formal schema and later template handoff |
| --- | --- | --- | --- |
| shared transformation record | Chapter 7 | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` | current: `07_model/Transformation_Record.schema.json`; later: `02_appendices/Appendix_C_Shared_Transformation_Record_Schema.md` |
| COMPOSE record | Chapters 7 and 15 | `04_reference/Transformation_Operation_Index.md`; `07_model/Operation_Registry.yaml` | current operation-specific schema branch under `#/$defs/composeDetails`; later: `02_appendices/Appendix_D_COMPOSE_Record_Template.md` and compose case template |
| DECOMPOSE record | Chapters 7 and 20 | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `07_model/Operation_Registry.yaml` | current operation-specific schema branch under `#/$defs/decomposeDetails`; later: `02_appendices/Appendix_E_DECOMPOSE_Record_Template.md` and decompose case template |
| PROJECT_AS record | Chapters 7 and 30 | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `07_model/Operation_Registry.yaml` | current operation-specific schema branch under `#/$defs/projectAsDetails`; later: `02_appendices/Appendix_F_PROJECT_AS_Record_Template.md` and project-as case template |
| loss record | Chapters 7 and 48 | `04_reference/Admissibility_Band_Reference.md`; `07_model/Admissibility_Rules.yaml` | current: record pointer `/loss` and schema definition `#/$defs/lossDeclaration`; five canonical fields only |
| integrated chain audit | Chapter 53 | `04_reference/Output_Class_Index.md`; `04_reference/Admissibility_Band_Reference.md`; populated Core artifacts | current chain scope and result separation in `07_model/Transformation_Record.schema.json`; later: `02_appendices/Appendix_N_Integrated_STRATA_Audit_Template.md` and integrated audit case template |

### 15.1 Current Model-Field and Schema Handoffs

The following paths are current formal routes owned by the populated Core artifacts. They operationalize controlled distinctions; they do not create new prose definitions or establish substantive validity.

| Concern | Record-instance pointer | Schema or owner pointer | Cross-artifact owner |
| --- | --- | --- | --- |
| record scope | `/record_scope` | `#/properties/record_scope` | `07_model/Transformation_Record.schema.json`; root handoff under `/record_and_schema_handoff` |
| routing state | `/routing_state` | `#/properties/routing_state` | record schema and `07_model/Boundary_Decision_Tree.yaml` |
| claim declaration and ceiling | `/claim` | `#/$defs/claimDeclaration`; `#/$defs/claimCeiling` | `04_reference/Claim_Type_Table.md`; record schema |
| operation occurrence and type | `/operation` | `#/$defs/operationDeclaration`; owner inventory `/operation_types` | `07_model/Operation_Registry.yaml` |
| admissibility audit and rule findings | `/admissibility` | `#/$defs/admissibilityDeclaration`; owner paths `/ordered_audit_contract/stages` and `/rule_profiles` | `07_model/Admissibility_Rules.yaml` |
| canonical loss record | `/loss` | `#/$defs/lossDeclaration` | record schema; rule and operation controls |
| separated status axes | `/result/status_declaration` | `#/$defs/statusDeclaration` | record schema; root `/record_and_schema_handoff/status_and_result_axis_separation` |
| candidate assessments and one selected class | `/result/routing/candidate_assessments`; `/result/routing/selected_class` | `#/$defs/candidateAssessments`; `#/$defs/routedResult` | `07_model/Output_Classes.yaml` and `07_model/Boundary_Decision_Tree.yaml` |
| current claim disposition | `/result/routing/current_claim_disposition` | `#/$defs/claimDispositionResult` | decision tree final-selection contract and record schema |
| formal diagnostic without output class | `/formal_diagnostic` | `#/$defs/formalDiagnostic` | decision-tree diagnostic routes and record schema |
| integrated root and validation companion | not a record-instance field | root `/component_manifest`, `/dependency_graph`, `/ownership_matrix`, `/inventory_integrity_snapshots`; companion schema root | `07_model/PMS-STRATA.yaml`; `07_model/PMS-STRATA.schema.json` |

Field names and pointers above are active formal handoffs. Smoke records instantiate them without treating schema validity as substantive admissibility, truth, causality, semantic adequacy, normative validity, person judgment, or application authority.

---

## 16. Case and Countercase Handoffs

| Test requirement | Primary chapter route | Active carrier | Current status |
| --- | --- | --- | --- |
| positive operation case | Chapters 17, 28, 40 | operation-specific Markdown and YAML case records | active case pressure |
| negative operation case | Chapters 17, 28, 40 | countercase template and `03_cases/Case_Index.md` | active case pressure |
| boundary or confusion case | Chapters 8, 16, 27, 37–39 | confusion-case template; `02_appendices/Appendix_I_Boundary_and_Confusion_Cases.md` | active case pressure |
| Stop case | Chapters 51 and 53 | mandatory-stop smoke tests and active case records | Records 02 and 07 current; substantive active case pressure |
| Non-Capture case | Chapters 52 and 53 | non-capture smoke test and active case records | Record 08 current; substantive active case pressure |
| integrated chain case | Chapter 53 | integrated audit template; `02_appendices/Appendix_N_Integrated_STRATA_Audit_Template.md` | active case pressure |

Cases test and expose rules. They do not define operations, claim types, output classes, or admissibility boundaries.

---

## 17. Appendix Handoffs

| Appendix | Title | Primary chapter route | Reference or model handoff | Current status |
| --- | --- | --- | --- | --- |
| A | Core Definitions | Chapters 0–8 | `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md` | active Appendix carrier |
| B | Formal Notation | Chapters 4–7 | `07_model/*`; `04_reference/Operator_Index.md` | active Appendix carrier |
| C | Shared Transformation Record Schema | Chapter 7 | `07_model/Transformation_Record.schema.json`; `04_reference/Claim_Type_Table.md` | active Appendix carrier |
| D | COMPOSE Record Template | Chapter 15 | `04_reference/Transformation_Operation_Index.md` | active Appendix carrier |
| E | DECOMPOSE Record Template | Chapter 20 | `04_reference/Transformation_Operation_Index.md` | active Appendix carrier |
| F | PROJECT_AS Record Template | Chapter 30 | `04_reference/Transformation_Operation_Index.md` | active Appendix carrier |
| G | Admissibility Band Tests | Chapters 44–53 | `04_reference/Admissibility_Band_Reference.md` | active Appendix carrier |
| H | Valid and Invalid Transformation Patterns | Chapters 16, 27, 39, 41 | `04_reference/Non_Equivalence_Index.md`; `04_reference/Audit_Checklist.md` | active Appendix carrier |
| I | Boundary and Confusion Cases | Chapters 8, 16, 27, 39 | `04_reference/Non_Equivalence_Index.md`; `03_cases/Case_Index.md` | active Appendix carrier |
| J | Operator-Weighting and Trajectory Stress Tests | Chapters 11, 35 | `04_reference/Operator_Index.md`; `04_reference/Claim_Type_Table.md` | active Appendix carrier |
| K | Cross-Domain Projection and Analogy Stress Tests | Chapters 36–37 | `04_reference/Claim_Type_Table.md`; `04_reference/Non_Equivalence_Index.md` | active Appendix carrier |
| L | Non-Operator Remainders and Decomposition Limits | Chapters 22, 25, 27, 52 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | active Appendix carrier |
| M | Case and Countercase Index | Chapters 17, 28, 40, 53 | `03_cases/Case_Index.md` | active Appendix carrier |
| N | Integrated STRATA Audit Template | Chapter 53 | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Audit_Checklist.md` | active Appendix carrier |

---

## 18. Formal Model Handoffs

Repository artifacts are written with full internal paths. The seven Core artifacts and eight canonical smoke records are populated and audit-passed. The internal Formal Model v0 smoke-test gate has passed; this does not establish substantive truth, external warrant, or corpus completion.

The table records current Core roles and, for each committed smoke test, one expected canonical output per delimited tested claim.

| Artifact | Current status | Current or declared role | Tested claim or record focus | Expected canonical output | Controlled prose and reference sources | Prohibited automatic inference |
| --- | --- | --- | --- | --- | --- | --- |
| `07_model/Operation_Registry.yaml` | current formal model core; v0.2.0 | registers exactly COMPOSE, DECOMPOSE, and PROJECT_AS with structural requirements | registry artifact; no tested occurrence | not applicable | Chapters 4, 15, 20, 30; `04_reference/Transformation_Operation_Index.md` | empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/Output_Classes.yaml` | current formal model core; v0.2.0 | registers exactly ten canonical output values, constitutive profiles, and current load-bearing class boundaries | registry artifact; no tested occurrence | not applicable | Chapter 6; `04_reference/Output_Class_Index.md` | empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/Admissibility_Rules.yaml` | current formal model core; v0.2.0 | registers sixteen checks, twelve audit stages, local vocabularies, non-compensation, Stop, Non-Capture, anti-immunization, and ceilings | rule artifact; no tested occurrence | not applicable | Chapter 6 and Chapters 44–53; `04_reference/Admissibility_Band_Reference.md` | substantive admissibility, empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/Boundary_Decision_Tree.yaml` | current formal model core; v0.2.0 | routes complete semantic packets through candidate generation, claim separation, collision adjudication, diagnostics, and unique final selection without ranking or first-match logic | decision-routing artifact; no tested occurrence | not applicable | Chapter 6 and Chapters 44–53; `04_reference/Output_Class_Index.md`; `04_reference/Admissibility_Band_Reference.md`; `04_reference/Non_Equivalence_Index.md` | substantive truth, causal validity, semantic adequacy, normative validity, person judgment, or application authority |
| `07_model/Transformation_Record.schema.json` | current formal model core; artifact v0.2.0; record schema v0.1.2 | validates occurrence and integrated-chain record form, required axes, pointer contracts, loss, diagnostics, candidate assessments, and routed results | schema artifact; no tested occurrence | not applicable | Chapter 7; `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | adequacy of source interpretation or substantive claim validity |
| `07_model/PMS-STRATA.yaml` | current formal model core; v0.2.0 | integrates component manifest, dependency graph, ownership matrix, inventory snapshots, record handoff, and package integrity declarations without independent theory authority | integrated registry artifact; no tested occurrence | not applicable | all controlled prose and Reference artifacts | empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/PMS-STRATA.schema.json` | current formal model core; v0.2.0 | validates the integrated root structure and declared integrity-binding form without duplicating component semantics | schema artifact; no tested occurrence | not applicable | controlled prose and formal registries | truth, completeness of theory, or application authority |
| `07_model/examples/01_COMPOSE_Admissible.yaml` | current smoke-test evidence | positive COMPOSE smoke record | a declared composite satisfies operation identity and all applicable checks | `admissible` | Chapter 15; `04_reference/Transformation_Operation_Index.md`; `04_reference/Output_Class_Index.md` | empirical truth of the composite |
| `07_model/examples/02_DECOMPOSE_Relevance_Floor_Stop.yaml` | current smoke-test evidence | lower-bound stop smoke record | continued DECOMPOSE refinement below the Praxeological Relevance Floor | `mandatory_stop` | Chapters 25, 44, 51; `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | that every valid neutral resolution test must stop immediately |
| `07_model/examples/03_PROJECT_AS_Admissible.yaml` | current smoke-test evidence | positive PROJECT_AS smoke record | origin type is preserved and a source-traceable contextual target function passes without material additional claim narrowing | `admissible` | Chapter 30; `04_reference/Transformation_Operation_Index.md`; `04_reference/Output_Class_Index.md` | empirical or normative validity of the target function |
| `07_model/examples/04_PROJECT_AS_Label_Substitution.yaml` | current smoke-test evidence | invalid projection confusion record | label substitution is presented as PROJECT_AS without typed target function and source trace | `failed_transformation` | Chapters 37, 39; `04_reference/Non_Equivalence_Index.md`; `04_reference/Output_Class_Index.md` | general invalidity of analogy or comparison |
| `07_model/examples/05_Traceability_Ceiling_Failure.yaml` | current smoke-test evidence | upper-bound failure smoke record | transformation result no longer carries traceable load from declared source structures | `failed_transformation` | Chapter 45; `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | empirical falsity of the source object |
| `07_model/examples/06_Claim_Reduction.yaml` | current smoke-test evidence | claim-revision smoke record | current claim exceeds the warranted ceiling and a reduced successor claim still requires testing | `claim_reduction_required` | Chapters 49, 50, 53; `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` | admissibility of the untested reduced claim |
| `07_model/examples/07_Mandatory_Stop.yaml` | current smoke-test evidence | mandatory-stop smoke record | further continuation would violate a non-compensatory boundary | `mandatory_stop` | Chapter 51; `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | that all prior local results failed |
| `07_model/examples/08_Non_Capture.yaml` | current smoke-test evidence | non-capture smoke record | no adequate retained claim remains without distortion or false closure | `non_capture` | Chapter 52; `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | proof of rival superiority or immunity from criticism |
| `07_model/examples/README.md` | current smoke-test evidence | document smoke-record status, execution order, and interpretation limits | navigation artifact | not applicable | Formal Model v0 controls | substantive validation of examples |

The populated Core may validate inventory, completeness, operation identity declarations, field form, Type Integrity constraints, boundary routing, and canonical output values. Machine-readable consistency is not a truth proof. The formal vocabulary and record schema now exist; each forthcoming smoke-test record must preserve its tested claim, local result, status axes, loss, routing basis, and expected canonical output as distinct data.

---

## 19. Critical Redundancy Guards

| Site relation | Routing rule |
| --- | --- |
| Chapters 0 / 57 | Chapter 0 defines the governing claim and boundary; Chapter 57 restates and closes without expansion |
| Chapters 5 / 47 | Chapter 5 defines type, function, context, and continuity; Chapter 47 audits continuity |
| Chapters 6 / 44–45 | Chapter 6 defines the common band architecture; Chapters 44–45 elaborate lower and upper tests |
| Chapters 7 / 48 | Chapter 7 introduces the shared record and loss fields; Chapter 48 audits loss |
| Chapters 16, 27, 39 / 51 | local operation limits route to the system-wide Stop method without being replaced |
| Chapters 17, 28, 40 / 53 | local audits retain their results; Chapter 53 integrates without overwriting |
| Chapters 38 / 50 | invalid type jumps remain operation failures; anti-immunization prevents rescue by later transformations |
| Chapters 44 / 49 | Relevance Floor is distinct from source and calibration limits |
| Chapters 45 / 48 | Traceability Ceiling is distinct from loss disclosure |
| Chapters 51 / 52 | Stop is distinct from Non-Capture |
| Front Matter / numeric chapters | orientation and navigation must not define theory |
| Reference / Blocks | Reference artifacts index and stabilize; locked Blocks become canonical prose |

---

## 20. Open Bounded Duties

| Duty | Active carrier | Completion condition | Claim boundary |
| --- | --- | --- | --- |
| Reference Freeze | all active files in `04_reference/` | ownership, links, terminology, case pressure, appendices, formal carriers, and duplicate definitions are corpus-audited | freeze cannot create theory or authority |
| Chapters 16 and 25 same-source comparison pressure | `03_cases/Case_Obligation_Coverage_Matrix.csv` and governing chapter rules | exact same-source comparison sets are either added or retained as explicit bounded partial duties | missing comparison evidence cannot be narrated as complete |
| Formal Model finalization | `07_model/*` | model is synchronized to the audited corpus and validates structurally | model cannot decide truth, causality, normativity, diagnosis, or authority |
| Reader synchronization | `08_PMS-STRATA Reader/*` | navigation reflects final active paths and exclusions | Reader cannot become a theory source |
