# PMS-STRATA — Cross Reference Map

**Status:** Pre-LIMITS Maintenance WP5-synchronized; maintenance gate passed; Reference Freeze not performed  
**Historical local version marker:** Reference Kernel v0 scaffold v0.3.48 — Chapter-20-WP3-synchronized  
**Repository role:** `04_reference/*` — routing and cross-reference layer; not an independent theory source  
**Current control provenance:** `00_source/PMS-STRATA_Structure.md`, `05_minified/*`, the seven substantive Reference Kernel files, the three synchronized peer scaffolds `04_reference/Evidence_Map.md`, `04_reference/Audit_Checklist.md`, and `04_reference/Reader_Pathways.md`, repository `README.md`, and `PMS.yaml` for PMS Base  
**Current formal handoff inputs:** all seven populated `07_model/*` Core artifacts plus eight populated canonical smoke records and `07_model/examples/README.md`; internal smoke-test gate audit-passed and Root/Companion synchronized  
**Block-anchor status:** Foundations 0–8, PATH 9–17, and SUB 18–28 are provisionally locked; RETYPE 29–40 holds a bounded provisional method lock; LIMITS prose is unstarted; Chapter 41 Preparation and Pre-LIMITS Maintenance WP0–WP5 are complete; Chapter 41 WP1 is next.  

---

**Current synchronization:** Foundations Chapters 0–8, PATH Chapters 9–17, and SUB Chapters 18–28 are provisionally locked; RETYPE Chapters 29–40 hold a bounded provisional method lock; 29 PATH/SUB case packages are present and indexed; Chapter 41 Preparation and Pre-LIMITS Maintenance WP0–WP5 are complete while canonical Chapter 41 prose remains unstarted; Chapter 41 WP1 is the next controlled production step; the artifact-complete RETYPE lock remains `mandatory_stop`, and Part IV final lock remains unavailable.  
**Historical-layering rule:** Later `pending`, `next controlled step`, availability, or WP-stage statements preserve the local production state at the time of entry unless explicitly marked as current. They do not override this header and remain non-normative provenance until Reference Freeze.  

## 1. Role, Status, and Authority

This map routes already controlled definitions, elaborations, applications, audits, formal handoffs, cases, appendices, and later reader paths. It does not define theory, repair missing prose by implication, or make a linked artifact more authoritative than its repository role permits.

```text
designated canonical site
≠
current control source
```

Before the relevant chapter lock, a chapter may be the designated canonical destination while its current support is distributed among populated canonical sections, Structure, contracts, minified controls, and Reference Kernel artifacts. A pending or partial chapter anchor is never cited as if the entire chapter were already locked.

This map shall:
- register one designated canonical definition site for each core term;
- distinguish definition, elaboration, application, audit, indexing, formalization, testing, templating, summarization, and routing;
- preserve repository authority order;
- register current Core and smoke-suite paths while keeping pending Block anchors, case IDs, appendix anchors, derivative links, and Reader implementation routes explicitly open;
- prevent cross-reference convenience from becoming authority inheritance.

Mutual routing among Reference artifacts is navigational only. A Cross Reference handoff to the Evidence Map and an Evidence Map handoff back to established definition sites do not create circular definition or authority inheritance.

```text
mutual routing
≠
circular definition
≠
authority inheritance
```

This map shall not:
- introduce a fourth operation, a new output class, a new PMS primitive, a machine field, or a case result;
- replace `Chapter_Contracts.md`, the substantive Reference indices, or future canonical Block prose;
- assess evidence quality, decide substantive admissibility, or define a reading hierarchy of authority;
- describe placeholders as completed systems.

---

## 2. Cross-Reference Semantics

| Relation | Navigation meaning | Authority limit |
| --- | --- | --- |
| defines | designated canonical primary definition site | one target only; pending until prose exists |
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
| current architecture control | populated Structure artifact carrying architecture and chapter blueprint control |
| current binding control | populated minified artifact or contract carrying binding drafting control |
| current navigation/status control | populated README or navigation artifact carrying package and status guidance |
| provisionally controlled pre-Block | populated substantive Reference artifact controlled before Block prose |
| populated pre-Block scaffold | populated Reference navigation scaffold without independent theory authority |
| current control | other populated artifact presently carrying a control or registry function |
| current formal model core | populated Core artifact carrying formal operationalization; package validation does not establish substantive truth |
| contract-bound / prose pending | canonical target and obligations are specified, but Block prose is empty |
| placeholder | file exists at 0 bytes and carries no current content authority |
| current smoke-test evidence | populated schema-valid smoke record or suite-control artifact with passed internal conformance audit; not substantive or external evidence |
| case handoff pending | case or template target exists only as an empty target |
| appendix handoff pending | appendix target exists only as an empty target |
| deferred until Block lock | anchor or relation cannot be finalized before relevant chapter prose is locked; not an artifact state |
| deferred until Reference Freeze | navigation can be stabilized only after cases, Conclusion, Front Matter, and Appendices; not an artifact state |

```text
navigation status
≠
record status
≠
canonical output class
```

Internal repository artifacts are written with full paths in registries and handoff tables. Short labels may be used in prose only after the full path has been established in the same section.

---

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
| `00_source/PMS-STRATA_Structure.md` | architecture and chapter blueprint | not a substitute for locked corpus prose |
| `01_blocks/*` | canonical corpus prose after lock | currently empty; no present prose authority |
| `05_minified/*` | binding control artifacts | must remain subordinate to locked canonical prose |
| `07_model/*` | formal operationalization | never replaces prose or proves truth |
| `02_appendices/*` | schemas, templates, and supplements | not an independent theory source |
| `03_cases/*` | cases, countercases, confusion cases, and audits | tests rules; does not define them |
| `04_reference/*` | terminology, registries, and cross-reference | no independent theory authority |
| `06_derivative_publications/*` | later public derivatives | no back-propagation |
| `08_PMS-STRATA Reader/*` | later presentation and navigation | no back-propagation |

Linking an internal artifact to `PMS.yaml` records source authority. It does not make `PMS.yaml` an internal packaged path or grant the linked artifact PMS-Base authority.

---

## 4. Current Artifact Status Registry

| Path | Current status | Repository role | Primary upstream | Downstream handoff | Freeze stage |
| --- | --- | --- | --- | --- | --- |
| `00_source/PMS-STRATA_Structure.md` | current architecture control | architecture and chapter blueprint | PMS.yaml and project architecture | contracts, references, Blocks, model | Structure lock; later change only by explicit architecture revision |
| `01_blocks/00_front_matter.md` | placeholder | future canonical corpus prose | Structure, contracts, Reference Kernel, Formal Model v0 | appendices, cases, Reference freeze, model finalization | per-chapter and per-part lock |
| `01_blocks/01_foundations.md` | provisionally locked — Chapters 0–8 | canonical corpus prose | Structure, contracts, Reference Kernel, Formal Model v0 | appendices, cases, Reference freeze, model finalization | per-chapter and per-part lock |
| `01_blocks/02_part_i_path.md` | provisionally locked — Chapters 9–17 | canonical corpus prose | Structure, contracts, Reference Kernel, Formal Model v0 | appendices, cases, Reference freeze, model finalization | per-chapter and per-part lock |
| `01_blocks/03_part_ii_sub.md` | provisionally locked — Chapters 18–28 | canonical corpus prose | Structure, contracts, Reference Kernel, Formal Model v0 | appendices, cases, Reference freeze, model finalization | per-chapter and per-part lock |
| `01_blocks/04_part_iii_retype.md` | bounded provisional method lock — Chapters 29–40; artifact lock `mandatory_stop` | canonical corpus prose | Structure, contracts, Reference Kernel, Formal Model v0 | appendices, cases, Reference freeze, model finalization | per-chapter and per-part lock |
| `01_blocks/05_part_iv_limits.md` | placeholder | future canonical corpus prose | Structure, contracts, Reference Kernel, Formal Model v0 | appendices, cases, Reference freeze, model finalization | per-chapter and per-part lock |
| `01_blocks/06_conclusion.md` | placeholder | future canonical corpus prose | Structure, contracts, Reference Kernel, Formal Model v0 | appendices, cases, Reference freeze, model finalization | per-chapter and per-part lock |
| `02_appendices/Appendix_A_Core_Definitions.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_B_Formal_Notation.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_C_Shared_Transformation_Record_Schema.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_D_COMPOSE_Record_Template.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_E_DECOMPOSE_Record_Template.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_F_PROJECT_AS_Record_Template.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_G_Admissibility_Band_Tests.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_H_Valid_and_Invalid_Transformation_Patterns.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_I_Boundary_and_Confusion_Cases.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_J_Operator_Weighting_and_Trajectory_Stress_Tests.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_K_Cross_Domain_Projection_and_Analogy_Stress_Tests.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_L_Non_Operator_Remainders_and_Decomposition_Limits.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_M_Case_and_Countercase_Index.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `02_appendices/Appendix_N_Integrated_STRATA_Audit_Template.md` | placeholder | future schema, template, and supplement layer | locked Blocks and Reference Kernel | Reference freeze and release | after Conclusion and Front Matter |
| `03_cases/Case_Index.md` | populated — 29 indexed PATH/SUB packages; RETYPE lock packages absent | test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/Case_Index.yaml` | populated — 29 indexed PATH/SUB packages; RETYPE lock packages absent | test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/markdown/README.md` | populated directory guide; 29 PATH/SUB Markdown cases present | test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/case_template.md` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/compose_case_template.yaml` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/confusion_case_template.md` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/countercase_template.md` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/decompose_case_template.yaml` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/integrated_audit_case_template.yaml` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/non_capture_case_template.yaml` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/templates/project_as_case_template.yaml` | placeholder | future test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `03_cases/yaml/README.md` | populated directory guide; 29 PATH/SUB YAML records present | test and countercase layer | operation rules, output classes, and audits | integrated audit and corpus audit | local Part locks and integrated audit |
| `04_reference/Admissibility_Band_Reference.md` | provisionally controlled pre-Block | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Audit_Checklist.md` | populated pre-Block scaffold | executable audit navigation; no independent theory authority | Structure, contracts, minified controls, substantive Reference Kernel, Cross Reference Map, Evidence Map, and PMS.yaml where applicable | Blocks, Formal Model, cases, corpus audit, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Claim_Type_Table.md` | provisionally controlled pre-Block | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Cross_Reference_Map.md` | populated pre-Block scaffold | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, seven substantive Reference files, Evidence Map, Audit Checklist, Reader Pathways, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Evidence_Map.md` | populated pre-Block scaffold | source, support, gap, rival, and external-warrant routing; no independent theory authority | Structure, contracts, minified controls, substantive Reference files, and PMS.yaml where applicable | Blocks, Formal Model, cases, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Glossary.md` | provisionally controlled pre-Block | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Non_Equivalence_Index.md` | provisionally controlled pre-Block | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Operator_Index.md` | provisionally controlled pre-Block | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Output_Class_Index.md` | provisionally controlled pre-Block | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Reader_Pathways.md` | populated pre-Block scaffold | terminology and reader-route navigation; no independent theory authority | Structure, contracts, minified controls, seven substantive Reference files, Cross Reference Map, Evidence Map, Audit Checklist, and PMS.yaml where applicable | Front Matter, Blocks, Formal Model, cases, appendices, derivatives, Reader | final freeze after cases, conclusion, front matter, appendices |
| `04_reference/Transformation_Operation_Index.md` | provisionally controlled pre-Block | terminology and navigation; no independent theory authority | Structure, contracts, minified controls, and PMS.yaml where applicable | Blocks, Formal Model, audits, Reader | final freeze after cases, conclusion, front matter, appendices |
| `05_minified/Block_Contracts.md` | current binding control | binding control artifacts | Structure and canonical controls | all production stages | synchronized throughout; final control audit before release |
| `05_minified/Chapter_Contracts.md` | current binding control | binding control artifacts | Structure and canonical controls | all production stages | synchronized throughout; final control audit before release |
| `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | current binding control | binding control artifacts | Structure and canonical controls | all production stages | synchronized throughout; final control audit before release |
| `05_minified/PMS_STRATA_Claim_Boundary_Minified.md` | current binding control | binding control artifacts | Structure and canonical controls | all production stages | synchronized throughout; final control audit before release |
| `05_minified/PMS_STRATA_Minified_Canonical.md` | current binding control | binding control artifacts | Structure and canonical controls | all production stages | synchronized throughout; final control audit before release |
| `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | current binding control | binding control artifacts | Structure and canonical controls | all production stages | synchronized throughout; final control audit before release |
| `06_derivative_publications/PMS_STRATA_Compact_Overview.md` | placeholder | future derivative publication; no back-propagation | locked corpus and finalized model | Reader and public release only | after corpus audit and model finalization |
| `06_derivative_publications/PMS_STRATA_Derived_Publishable_Paper.md` | placeholder | future derivative publication; no back-propagation | locked corpus and finalized model | Reader and public release only | after corpus audit and model finalization |
| `06_derivative_publications/PMS_STRATA_Technical_Whitepaper.md` | placeholder | future derivative publication; no back-propagation | locked corpus and finalized model | Reader and public release only | after corpus audit and model finalization |
| `07_model/Admissibility_Rules.yaml` | current formal model core | populated rule registry and twelve-stage audit contract; no prose replacement | controlled prose, contracts, Reference Kernel, and prior Core artifacts | decision tree, record schema, root, smoke tests, cases, Reader | Formal Model v0 internal smoke gate passed; final after corpus audit |
| `07_model/Boundary_Decision_Tree.yaml` | current formal model core | populated non-ranking candidate, collision, diagnostic, and final-routing contract; no prose replacement | controlled prose, contracts, Reference Kernel, and prior Core artifacts | record schema, root, smoke tests, cases, Reader | Formal Model v0 internal smoke gate passed; final after corpus audit |
| `07_model/Operation_Registry.yaml` | current formal model core | populated closed registry of exactly COMPOSE, DECOMPOSE, and PROJECT_AS; no prose replacement | controlled prose, contracts, and Reference Kernel | remaining Core artifacts, smoke tests, cases, Reader | Formal Model v0 internal smoke gate passed; final after corpus audit |
| `07_model/Output_Classes.yaml` | current formal model core | populated closed registry of exactly ten canonical output classes; no prose replacement | controlled prose, contracts, Reference Kernel, and Operation Registry | remaining Core artifacts, smoke tests, cases, Reader | Formal Model v0 internal smoke gate passed; final after corpus audit |
| `07_model/PMS-STRATA.schema.json` | current formal model core | populated JSON Schema companion validating the integrated root form; no semantic ownership | populated root contract and Core assembly requirements | root validation, package audit, later model finalization | Formal Model v0 internal smoke gate passed; final after corpus audit |
| `07_model/PMS-STRATA.yaml` | current formal model core | populated integration manifest, ownership map, dependency graph, integrity declaration, and package-level handoff | five semantic Core components, controlled prose, contracts, and Reference inputs | companion validation, smoke tests, package audit, Reader | Formal Model v0 internal smoke gate passed; final after corpus audit |
| `07_model/Transformation_Record.schema.json` | current formal model core | populated record schema for operation occurrences and integrated chains; no substantive claim decision | four prior semantic Core components and controlled prose/reference inputs | smoke records, cases, appendices, Reader | Formal Model v0 internal smoke gate passed; final after corpus audit |
| `07_model/examples/01_COMPOSE_Admissible.yaml` | current smoke-test evidence | populated schema-valid positive COMPOSE smoke record; expected route `admissible` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/02_DECOMPOSE_Relevance_Floor_Stop.yaml` | current smoke-test evidence | populated schema-valid lower-bound DECOMPOSE stop smoke record; expected route `mandatory_stop` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/03_PROJECT_AS_Admissible.yaml` | current smoke-test evidence | populated schema-valid positive PROJECT_AS smoke record; expected route `admissible` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/04_PROJECT_AS_Label_Substitution.yaml` | current smoke-test evidence | populated schema-valid PROJECT_AS label-substitution failure smoke record; expected route `failed_transformation` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/05_Traceability_Ceiling_Failure.yaml` | current smoke-test evidence | populated schema-valid upper-bound COMPOSE traceability failure smoke record; expected route `failed_transformation` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/06_Claim_Reduction.yaml` | current smoke-test evidence | populated schema-valid DECOMPOSE claim-reduction smoke record; expected route `claim_reduction_required` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/07_Mandatory_Stop.yaml` | current smoke-test evidence | populated schema-valid DECOMPOSE continuity/traceability stop smoke record; expected route `mandatory_stop` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/08_Non_Capture.yaml` | current smoke-test evidence | populated schema-valid integrated COMPOSE → PROJECT_AS non-capture smoke record; expected route `non_capture` confirmed; no prose replacement or truth proof | populated Core artifacts and controlled prose/reference inputs | cases, Foundations drafting, Reader | internal smoke gate passed; final model only after corpus audit |
| `07_model/examples/README.md` | current smoke-test evidence | populated suite index, coverage boundary, execution contract, and interpretation limits; no substantive validation | eight records, populated Core artifacts, and controlled prose/reference inputs | Foundations drafting, later cases, Reader | internal smoke gate passed; update on suite change |
| `08_PMS-STRATA Reader/README.md` | placeholder | future presentation and navigation layer | release corpus, references, cases, and derivatives | release navigation only | release stage |
| `08_PMS-STRATA Reader/pms_strata_reader.py` | placeholder | future presentation and navigation layer | release corpus, references, cases, and derivatives | release navigation only | release stage |
| `README.md` | current navigation/status control | repository navigation and status | repository architecture | all repository users | release stage |

### 4.1 Current kernel summary

| Artifact group | Count | Current state |
| --- | --- | --- |
| substantive Reference Kernel files | 7 | populated and provisionally controlled pre-Block |
| Reference scaffolds including this map | 4 | all four Reference scaffolds populated; Reference Kernel v0 population complete and provisionally controlled |
| numeric chapters | 58 | Chapters 0–5 provisionally locked; Chapters 6–57 canonical prose pending |
| Front Matter units | 4 | contract-bound; Block prose pending |
| Formal Model core files | 7 | populated, integrated, schema-validated, and package-audited; full Model v0 gate still open |
| Formal Model smoke-test records | 8 | populated, schema-valid, suite- and cross-record-audited |
| Appendices | 14 | placeholders |

---

## 5. Corpus Block Map

| Block file | Chapter or unit range | Canonical role after lock | Current status |
| --- | --- | --- | --- |
| `01_blocks/00_front_matter.md` | four FM units | orientation, status, notation, and reading navigation only | contract-bound / prose pending |
| `01_blocks/01_foundations.md` | Chapters 0–8 | shared object model, operations, band, record, and non-equivalences | Chapters 0–4 provisionally locked; Chapters 5–8 prose pending |
| `01_blocks/02_part_i_path.md` | Chapters 9–17 | PATH and COMPOSE | contract-bound / prose pending |
| `01_blocks/03_part_ii_sub.md` | Chapters 18–28 | SUB and DECOMPOSE | contract-bound / prose pending |
| `01_blocks/04_part_iii_retype.md` | Chapters 29–40 | RETYPE and PROJECT_AS | contract-bound / prose pending |
| `01_blocks/05_part_iv_limits.md` | Chapters 41–53 | LIMITS and integrated audit | contract-bound / prose pending |
| `01_blocks/06_conclusion.md` | Chapters 54–57 | integration, PMS relation, negative provision, final claim | contract-bound / prose pending |

---

## 6. Chapter Registry 0–57

| Ch. | Title | Part | Target Block | Primary concept family | Current contract source | Reference handoff | Model/case handoff | Anchor status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Position and Claim Boundary | Foundations | `01_blocks/01_foundations.md` | claim and authority boundary | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Claim_Type_Table.md`; `05_minified/PMS_STRATA_Claim_Boundary_Minified.md` | no semantic Formal Model revision required | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional chapter lock |
| 1 | Object Model: Operator Type, Operator Occurrence, and Composite Structure | Foundations | `01_blocks/01_foundations.md` | object model | `05_minified/Chapter_Contracts.md` | `04_reference/Chapter_1_Preparation_Record.md`; `04_reference/Glossary.md`; `04_reference/Operator_Index.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Claim_Type_Table.md` | `07_model/Operation_Registry.yaml` open object-model handoff synchronized; Record Schema unchanged | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — provisionally locked |
| 2 | Frame, Granularity, and Relative Level | Foundations | `01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level` | analytical coordinates and scopes | `05_minified/Chapter_Contracts.md` | `04_reference/Chapter_2_Preparation_Record.md`; `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Claim_Type_Table.md` | existing nested record-coordinate paths verified; open Operation Registry handoff synchronized | provisionally locked after integrated WP4 audit |
| 3 | Configuration, Event, Non-Event, Transition, Path, and Trajectory | Foundations | [`01_blocks/01_foundations.md`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | full temporal object and historical-property architecture | `05_minified/Chapter_Contracts.md` | `04_reference/Chapter_3_Preparation_Record.md`; `04_reference/Glossary.md`; `04_reference/Operator_Index.md`; `04_reference/Claim_Type_Table.md` | open Chapter 3 handoff synchronized in `07_model/Operation_Registry.yaml`; Record Schema unchanged | provisionally locked after integrated WP4 audit |
| 4 | The Three STRATA Operations: COMPOSE, DECOMPOSE, and PROJECT_AS | Foundations | `01_blocks/01_foundations.md`; `04_reference/Chapter_4_Preparation_Record.md` | operation grammar | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Claim_Type_Table.md` | three-operation registry synchronized; no fourth operation | provisionally locked |
| 5 | Origin Type, Target Function, and Transformation Context | Foundations | `01_blocks/01_foundations.md`; `04_reference/Chapter_5_Preparation_Record.md` | type, function, context, and continuity | `05_minified/Chapter_Contracts.md` | `04_reference/Glossary.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | continuity duties synchronized; no origin-type replacement | provisionally locked |
| 6 | The STRATA Admissibility Band | Foundations | `01_blocks/01_foundations.md` | Admissibility Band and output architecture | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | provisionally locked |
| 7 | Shared Transformation Record | Foundations | `01_blocks/01_foundations.md`; `04_reference/Chapter_7_Preparation_Record.md` | shared transformation record | `05_minified/Chapter_Contracts.md`; Chapter 7 Preparation Record | `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md`; `04_reference/Evidence_Map.md` | `07_model/Transformation_Record.schema.json`; `07_model/PMS-STRATA.schema.json` | provisionally locked |
| 8 | Foundational Non-Equivalences | Foundations | `01_blocks/01_foundations.md` | foundational non-equivalences | `05_minified/Chapter_Contracts.md` | `04_reference/Non_Equivalence_Index.md` | bounded handoff in `07_model/Boundary_Decision_Tree.yaml` | provisionally locked; Foundations complete |
| 9 | Temporal Order and Transition | PATH | `01_blocks/02_part_i_path.md` | temporal order and transition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | anchor pending |
| 10 | Path | PATH | `01_blocks/02_part_i_path.md` | path | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | anchor pending |
| 11 | Trajectory | PATH | `01_blocks/02_part_i_path.md` | trajectory | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | anchor pending |
| 12 | Path Dependence and Sedimentation | PATH | `01_blocks/02_part_i_path.md` | path dependence and sedimentation | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | anchor pending |
| 13 | Branches, Aborts, Delays, and Unavailable Alternatives | PATH | `01_blocks/02_part_i_path.md`; `04_reference/Chapter_13_Preparation_Record.md` | alternatives and branch structure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | WP1–WP3 canonical prose; WP4 pending | WP3 complete |
| 14 | Non-Events within Paths and Trajectories | PATH | `01_blocks/02_part_i_path.md` | non-events in temporal composites | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | anchor pending |
| 15 | COMPOSE: Selection, Formation, and Compression | PATH | `01_blocks/02_part_i_path.md` | COMPOSE procedure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | `07_model/Operation_Registry.yaml` | anchor pending |
| 16 | PATH Boundary Conditions | PATH | `01_blocks/02_part_i_path.md` | PATH limits | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | formal handoff only where declared by chapter contract | anchor pending |
| 17 | PATH Cases, Countercases, and Local Audit | PATH | `01_blocks/02_part_i_path.md` | PATH cases and local audit | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local PATH audit | smoke tests and later case records | anchor pending |
| 18 | The Provisionally Compressed Object | SUB | [`01_blocks/03_part_ii_sub.md`](../01_blocks/03_part_ii_sub.md#chapter-18-the-provisionally-compressed-object) | provisional elementarity and compressed source-object entry | `05_minified/Chapter_Contracts.md`; `04_reference/Chapter_18_Preparation_Record.md` | `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Operator_Index.md`; `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Evidence_Map.md`; `04_reference/Audit_Checklist.md` | bounded Chapter-18 mirrors in `07_model/Admissibility_Rules.yaml`; no schema change | provisionally locked through §§18.1–18.10 after WP4 audit |
| 19 | Granularity Change and the Logic of Decomposition | SUB | `01_blocks/03_part_ii_sub.md`; `04_reference/Chapter_19_Preparation_Record.md` | source-to-target granularity relation | `05_minified/Chapter_Contracts.md`; Chapter-19 Preparation Gate | `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md`; `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Evidence_Map.md`; `04_reference/Audit_Checklist.md` | bounded non-routing preparation mirror in `07_model/Admissibility_Rules.yaml`; no schema change | Preparation Gate complete; canonical prose pending |
| 20 | DECOMPOSE: Conditions, Procedure, and Preservation Requirements | SUB | `01_blocks/03_part_ii_sub.md`; `04_reference/Chapter_20_Preparation_Record.md` | complete generic DECOMPOSE procedure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | `07_model/Operation_Registry.yaml`; `07_model/Admissibility_Rules.yaml` | Preparation Gate complete; canonical anchor pending |
| 21 | Decomposing Operator-Typed Occurrences | SUB | `01_blocks/03_part_ii_sub.md` | operator-occurrence decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | provisionally locked after integrated WP4 audit; formal handoff only where declared by chapter contract | [chapter anchor](../01_blocks/03_part_ii_sub.md#chapter-21-decomposing-operator-typed-occurrences) |
| 22 | Decomposing Composite Structures | SUB | `01_blocks/03_part_ii_sub.md` | composite decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | [chapter anchor](../01_blocks/03_part_ii_sub.md#chapter-22-decomposing-composite-structures) |
| 23 | Decomposing Events, Non-Events, and Internal Temporal Structures | SUB | `01_blocks/03_part_ii_sub.md` | event and internal-temporal decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | anchor pending |
| 24 | Decomposing Paths and Trajectories | SUB | `01_blocks/03_part_ii_sub.md` | path and trajectory decomposition | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | anchor pending |
| 25 | Resolution Gain, Neutrality, Drift, and Escape | SUB | `01_blocks/03_part_ii_sub.md` | resolution results | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | anchor pending |
| 26 | The Boundary between SUB and RETYPE | SUB | `01_blocks/03_part_ii_sub.md` | SUB–RETYPE boundary | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | anchor pending |
| 27 | SUB Boundary Conditions | SUB | `01_blocks/03_part_ii_sub.md` | SUB limits | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | formal handoff only where declared by chapter contract | anchor pending |
| 28 | SUB Cases, Countercases, and Local Audit | SUB | `01_blocks/03_part_ii_sub.md` | SUB cases and local audit | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local SUB audit | smoke tests and later case records | anchor pending |
| 29 | Functional Projection without Origin-Type Replacement | RETYPE | `01_blocks/04_part_iii_retype.md` | functional projection and type preservation | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | anchor pending |
| 30 | PROJECT_AS: Signature, Context, and Validity Scope | RETYPE | `01_blocks/04_part_iii_retype.md`; `04_reference/Chapter_30_Preparation_Record.md` | PROJECT_AS procedure | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Operation_Registry.yaml`; `07_model/Admissibility_Rules.yaml` | WP1 §§30.1–30.4 complete; chapter open |
| 31 | Trajectory as Frame-Function | RETYPE | `01_blocks/04_part_iii_retype.md`; `04_reference/Chapter_31_Preparation_Record.md` | frame-function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` non-routing mirror | WP1 §§31.1–31.4 complete; chapter open |
| 32 | Trajectory as Macro-Event | RETYPE | `01_blocks/04_part_iii_retype.md`; `04_reference/Chapter_32_Preparation_Record.md` | macro-event function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` non-routing mirror | WP1 §§32.1–32.4 complete; chapter open |
| 33 | Recurrent Trajectory Form as Attractor-Function | RETYPE | `01_blocks/04_part_iii_retype.md` | attractor-function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | anchor pending |
| 34 | Composite Structures as Higher-Level Functions | RETYPE | `01_blocks/04_part_iii_retype.md`; `04_reference/Chapter_34_Preparation_Record.md` | higher-level function | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` non-routing mirror | provisionally locked; Q/H/I unadjudicated |
| 35 | Operator Weighting, Modulation, and Emergent Functional Profiles | RETYPE | `01_blocks/04_part_iii_retype.md`; `04_reference/Chapter_35_Preparation_Record.md` | operator weighting and profiles | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` non-routing WP2 mirror | WP1–WP2 §§35.1–35.7 complete; chapter open |
| 36 | Competing Projections | RETYPE | `01_blocks/04_part_iii_retype.md`; `04_reference/Chapter_36_Preparation_Record.md` | competing projections | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | `07_model/Admissibility_Rules.yaml` non-routing WP3 mirror | WP1–WP3 §§36.1–36.10 complete; integrated lock audit pending |
| 37 | Projection, Structural Analogy, and Label Substitution | RETYPE | `01_blocks/04_part_iii_retype.md` | projection, analogy, and substitution | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | anchor pending |
| 38 | Invalid Type Jumps and Unmarked Level Mixing | RETYPE | `01_blocks/04_part_iii_retype.md` | invalid type jumps and level mixing | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | anchor pending |
| 39 | RETYPE Boundary Conditions | RETYPE | `01_blocks/04_part_iii_retype.md` | RETYPE limits | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | formal handoff only where declared by chapter contract | anchor pending |
| 40 | RETYPE Cases, Countercases, and Local Audit | RETYPE | `01_blocks/04_part_iii_retype.md` | RETYPE cases and local audit | `05_minified/Chapter_Contracts.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; local RETYPE audit | smoke tests and later case records | anchor pending |
| 41 | Why STRATA Must Bound Itself | LIMITS | `01_blocks/05_part_iv_limits.md` | constitutive LIMITS rationale | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | formal handoff only where declared by chapter contract | anchor pending |
| 42 | No Ontology of Strata | LIMITS | `01_blocks/05_part_iv_limits.md` | anti-ontology | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | formal handoff only where declared by chapter contract | anchor pending |
| 43 | No Privilege of Finer Resolution or Higher Composition | LIMITS | `01_blocks/05_part_iv_limits.md` | no resolution or composition privilege | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | formal handoff only where declared by chapter contract | anchor pending |
| 44 | Praxeological Relevance Floor | LIMITS | `01_blocks/05_part_iv_limits.md` | Praxeological Relevance Floor | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 45 | Praxeological Traceability Ceiling | LIMITS | `01_blocks/05_part_iv_limits.md` | Praxeological Traceability Ceiling | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 46 | Counterfactual Sensitivity | LIMITS | `01_blocks/05_part_iv_limits.md` | Counterfactual Sensitivity | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 47 | Reference, Type, and Function Continuity | LIMITS | `01_blocks/05_part_iv_limits.md` | continuity audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 48 | Compression Loss and Reconstruction Selection | LIMITS | `01_blocks/05_part_iv_limits.md` | loss audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 49 | Source Limits and Calibration Limits | LIMITS | `01_blocks/05_part_iv_limits.md` | Source Ceiling and calibration | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 50 | Anti-Immunization | LIMITS | `01_blocks/05_part_iv_limits.md` | anti-immunization | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 51 | Stop Conditions | LIMITS | `01_blocks/05_part_iv_limits.md` | Stop method | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 52 | Non-Capture | LIMITS | `01_blocks/05_part_iv_limits.md` | Non-Capture method | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 53 | Integrated STRATA Admissibility Audit | LIMITS | `01_blocks/05_part_iv_limits.md` | Integrated STRATA Admissibility Audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md`; `04_reference/Audit_Checklist.md` | `07_model/Admissibility_Rules.yaml`; `07_model/Boundary_Decision_Tree.yaml`; `07_model/Output_Classes.yaml` | anchor pending |
| 54 | The Integrated STRATA Model | Conclusion | `01_blocks/06_conclusion.md` | integrated results | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | anchor pending |
| 55 | What PMS-STRATA Provides | Conclusion | `01_blocks/06_conclusion.md` | relation to PMS Base | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | anchor pending |
| 56 | What PMS-STRATA Does Not Provide | Conclusion | `01_blocks/06_conclusion.md` | negative provision registry | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | anchor pending |
| 57 | Final Claim Boundary | Conclusion | `01_blocks/06_conclusion.md` | final claim and closure | `05_minified/Chapter_Contracts.md` | `04_reference/Cross_Reference_Map.md`; `04_reference/Reader_Pathways.md`; final Reference freeze | formal handoff only where declared by chapter contract | anchor pending |

### 6.1 Chapter relation rules

- The registry records primary concept ownership but does not copy hard and conditional dependency lists from `Chapter_Contracts.md`.
- Chapters 17, 28, and 40 are local audits; Chapter 53 is the integrated audit. Local results remain preserved.
- Chapters 44–52 elaborate limits already active in PATH, SUB, RETYPE, and operation chains.
- Chapters 54–57 synthesize and close; they do not introduce a new operation, output class, empirical result, or authority.

---

## 7. Front-Matter Registry

| Unit | Title | Function | Target Block | Reference handoff | Anchor status |
| --- | --- | --- | --- | --- | --- |
| FM-PREFACE | Preface | motivation without theory definition | `01_blocks/00_front_matter.md` | development history and orientation only | anchor pending |
| FM-STATUS-SCOPE | Status and Scope Note | status, scope, and entry boundaries without replacing Chapters 0 or 56 | `01_blocks/00_front_matter.md` | Chapters 0 and 56; README status | anchor pending |
| FM-TERMINOLOGY-NOTATION | Terminology and Notation Note | notation guidance without new semantics | `01_blocks/00_front_matter.md` | `04_reference/Glossary.md`; `04_reference/Operator_Index.md`; `04_reference/Non_Equivalence_Index.md` | anchor pending |
| FM-HOW-TO-READ | How to Read PMS-STRATA | reading navigation without authority ranking | `01_blocks/00_front_matter.md` | `04_reference/Reader_Pathways.md`; repository `README.md` | anchor pending |

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
| `PMS Base` | A. Project, Claim, and Authority | PMS.yaml | `PMS.yaml` | `04_reference/Operator_Index.md` | current external governing source; no internal Block definition anchor |
| `PMS-STRATA` | A. Project, Claim, and Authority | Chapter 0 — Position and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `05_minified/PMS_STRATA_Minified_Canonical.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `bounded transformation discipline` | A. Project, Claim, and Authority | Chapter 0 — Position and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `governing claim` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `claim boundary` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `claim type` | A. Project, Claim, and Authority | Chapter 7 — Shared Transformation Record | `04_reference/Claim_Type_Table.md`; `05_minified/PMS_STRATA_Minified_Canonical.md`; `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md` | anchor pending |
| `claim ceiling` | A. Project, Claim, and Authority | Chapter 5 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | `04_reference/Claim_Type_Table.md` | anchor pending |
| `No Meta-PMS` | A. Project, Claim, and Authority | Chapter 0 — Position and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Non_Equivalence_Index.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `No Ontology of Strata` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Non_Equivalence_Index.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `No Universal STRATA Scale` | A. Project, Claim, and Authority | Chapter 6 — The STRATA Admissibility Band | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Non_Equivalence_Index.md` | anchor pending |
| `authority inheritance` | A. Project, Claim, and Authority | Chapter 0 | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `01_blocks/01_foundations.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `authority ceiling` | A. Project, Claim, and Authority | Chapter 0 — Governing Claim and Claim Boundary | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md`; `04_reference/Admissibility_Band_Reference.md`; `01_blocks/01_foundations.md` | `04_reference/Admissibility_Band_Reference.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `more structure ≠ more authority` | A. Project, Claim, and Authority | Chapter 0 | `README.md`; `05_minified/PMS_STRATA_Minified_Canonical.md`; `01_blocks/01_foundations.md` | `04_reference/Non_Equivalence_Index.md` | [`chapter-0-position-and-claim-boundary`](../01_blocks/01_foundations.md#chapter-0-position-and-claim-boundary) — provisional |
| `operator sign` | B. Object Model | Chapter 1 distinction; actual inventory in `PMS.yaml` | `PMS.yaml`; `04_reference/Operator_Index.md` | `04_reference/Chapter_1_Preparation_Record.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP1 canonical |
| `operator name` | B. Object Model | Chapter 1 distinction; actual inventory in `PMS.yaml` | `PMS.yaml`; `04_reference/Operator_Index.md` | `04_reference/Chapter_1_Preparation_Record.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP1 canonical |
| `operator type` | B. Object Model | Chapter 1 — Object Model | `PMS.yaml`; `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Operator_Index.md`; `04_reference/Chapter_1_Preparation_Record.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP1 canonical |
| `operator occurrence` | B. Object Model | Chapter 1 — Object Model | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Operator_Index.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP1 canonical |
| `composite structure` | B. Object Model | Chapter 1 — Object Model | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP1 canonical |
| `configuration` | B. Object Model | Chapter 1 as object category | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP2 canonical |
| `state` | B. Object Model | Chapter 3 — Temporal Object Chain | `00_source/PMS-STRATA_Structure.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `event-like object` | B. Object Model | Chapter 1 — Object Model | `00_source/PMS-STRATA_Structure.md` | `04_reference/Transformation_Operation_Index.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP2 canonical |
| `event` | B. Object Model | Chapter 3 — Temporal Object Chain | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `non-event structure` | B. Object Model | Chapter 1 object category | `05_minified/Chapter_Contracts.md`; `PMS.yaml` | `04_reference/Operator_Index.md`; `04_reference/Chapter_1_Preparation_Record.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP2 canonical |
| `non-event` | B. Object Model | Chapter 3 temporal category | `PMS.yaml`; `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `transition as object` | B. Object Model | Chapter 1 object category | `05_minified/Chapter_Contracts.md` | `04_reference/Chapter_1_Preparation_Record.md` | [`chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure`](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) — WP2 canonical |
| `transition` | B. Object Model | Chapter 3 temporal category | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `derived analytical object` | B. Object Model | Chapter 1 — Object Model | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | [Chapter 1 WP3](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) |
| `object identity` | B. Object Model | Chapter 1 minimal identification dimensions | `05_minified/Chapter_Contracts.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_1_Preparation_Record.md` | [Chapter 1 WP3](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) |
| `reference object` | B. Object Model | Chapter 1 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Chapter_1_Preparation_Record.md` | [Chapter 1 WP3](../01_blocks/01_foundations.md#chapter-1-object-model-operator-type-operator-occurrence-and-composite-structure) |
| `reference identity` | B. Object Model | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `source object` | B. Object Model | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `target object` | B. Object Model | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `provisional elementarity` | B. Object Model | Chapter 18 — Provisionally Compressed Object | `00_source/PMS-STRATA_Structure.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `compressed object` | B. Object Model | Chapter 18 — Provisionally Compressed Object | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `frame` | C. Analytical Coordinates and Scopes | [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | `PMS.yaml`; `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_2_Preparation_Record.md` | Chapter 2 provisionally locked; WP1 definition route retained |
| `granularity` | C. Analytical Coordinates and Scopes | [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_2_Preparation_Record.md` | Chapter 2 provisionally locked; WP1 definition route retained |
| `relative level` | C. Analytical Coordinates and Scopes | [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_2_Preparation_Record.md` | Chapter 2 provisionally locked; WP1 definition route retained |
| `micro / meso / macro` | C. Analytical Coordinates and Scopes | [`Chapter 2 WP1`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | `05_minified/PMS_STRATA_Claim_Boundary_Minified.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_2_Preparation_Record.md` | Chapter 2 provisionally locked; WP1 definition route retained |
| `temporal scope` | C. Analytical Coordinates and Scopes | [`Chapter 2 WP2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_2_Preparation_Record.md` | Chapter 2 provisionally locked; WP2 definition route retained |
| `source scope` | C. Analytical Coordinates and Scopes | [`Chapter 2 WP2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_2_Preparation_Record.md` | Chapter 2 provisionally locked; WP2 definition route retained |
| `claim scope` | C. Analytical Coordinates and Scopes | [`Chapter 2 WP2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Chapter_2_Preparation_Record.md` | Chapter 2 provisionally locked; WP2 definition route retained |
| `transformation context` | C. Analytical Coordinates and Scopes | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `target context` | C. Analytical Coordinates and Scopes | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `validity scope` | C. Analytical Coordinates and Scopes | Chapter 5 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md`; `04_reference/Claim_Type_Table.md` | canonical anchor available |
| `sequence` | D. Temporal and Path Structures | Chapter 3 — Temporal Object Chain | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `path` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `trajectory` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `path dependence` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `sedimentation` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `irreversibility` | D. Temporal and Path Structures | Chapter 3 — Temporal Object Chain | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `unrealized alternative` | D. Temporal and Path Structures | Chapter 3 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `historical load` | D. Temporal and Path Structures | Chapter 11 — Trajectory | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `STRATA operation` | E. Operations and Transformation Records | Chapter 4 — The Three STRATA Operations | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `COMPOSE` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `DECOMPOSE` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `PROJECT_AS` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `operation occurrence` | E. Operations and Transformation Records | Chapter 4 — The Three STRATA Operations | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `operation chain` | E. Operations and Transformation Records | Chapter 4 | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `non-invertibility` | E. Operations and Transformation Records | Chapter 4 — The Three STRATA Operations | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Transformation_Operation_Index.md` | canonical Chapter 4 anchor available |
| `shared transformation record` | E. Operations and Transformation Records | Chapter 7 — Shared Transformation Record | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `record status` | E. Operations and Transformation Records | Chapter 7 — Shared Transformation Record | `05_minified/PMS_STRATA_Minified_Canonical.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md`; `04_reference/Evidence_Map.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` | anchor pending |
| `operation-specific result` | E. Operations and Transformation Records | Chapter 6 — The STRATA Admissibility Band | `05_minified/PMS_STRATA_Minified_Canonical.md`; `04_reference/Transformation_Operation_Index.md`; `04_reference/Output_Class_Index.md` | `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `origin type` | F. Projection, Functions, and Profiles | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `target function` | F. Projection, Functions, and Profiles | Chapter 5 — Origin Type, Target Function, and Transformation Context | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | canonical anchor available |
| `source function` | F. Projection, Functions, and Profiles | Chapter 20 — DECOMPOSE | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `functional projection` | F. Projection, Functions, and Profiles | Chapter 29 — Functional Projection | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `frame-function` | F. Projection, Functions, and Profiles | Chapter 31 — Trajectory as Frame-Function | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `macro-event` | F. Projection, Functions, and Profiles | Chapter 32 — Trajectory as Macro-Event | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `attractor-function` | F. Projection, Functions, and Profiles | Chapter 33 — Recurrent Trajectory Form as Attractor-Function | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `higher-level function` | F. Projection, Functions, and Profiles | Chapter 34 — Composite Structures as Higher-Level Functions | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `operator weighting` | F. Projection, Functions, and Profiles | Chapter 35 — Operator Weighting and Modulation | `00_source/PMS-STRATA_Structure.md` | `04_reference/Operator_Index.md` | anchor pending |
| `modulator` | F. Projection, Functions, and Profiles | Chapter 35 — Operator Weighting and Modulation | `00_source/PMS-STRATA_Structure.md` | `04_reference/Operator_Index.md` | anchor pending |
| `modulating profile` | F. Projection, Functions, and Profiles | Chapter 35 — Operator Weighting and Modulation | `00_source/PMS-STRATA_Structure.md` | `04_reference/Operator_Index.md` | anchor pending |
| `structural analogy` | F. Projection, Functions, and Profiles | Chapter 37 — Projection, Structural Analogy, and Label Substitution | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `label substitution` | F. Projection, Functions, and Profiles | Chapter 37 — Projection, Structural Analogy, and Label Substitution | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `invalid type jump` | F. Projection, Functions, and Profiles | Chapter 38 — Invalid Type Jumps and Level Mixing | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `level mixing` | F. Projection, Functions, and Profiles | Chapter 38 — Invalid Type Jumps and Level Mixing | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `granularity mixing` | F. Projection, Functions, and Profiles | Chapter 38 — Invalid Type Jumps and Level Mixing | `00_source/PMS-STRATA_Structure.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | anchor pending |
| `STRATA Admissibility Band` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 — STRATA Admissibility Band | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `admissible transformation` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `Praxeological Relevance Floor` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `PraxisPurchase` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `Changed-Reconstruction Test` | G. Admissibility, Continuity, Source, and Loss | Chapter 44 — Praxeological Relevance Floor | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `resolution gain` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `resolution neutrality` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `resolution drift` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 — Resolution Gain, Neutrality, Drift, and Escape | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `resolution escape` | G. Admissibility, Continuity, Source, and Loss | Chapter 25 | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `Praxeological Traceability Ceiling` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `TraceableLoad` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `Constitutive Source Trace` | G. Admissibility, Continuity, Source, and Loss | Chapter 45 — Praxeological Traceability Ceiling | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `Counterfactual Sensitivity` | G. Admissibility, Continuity, Source, and Loss | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `Type Integrity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `reference continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `type continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `functional continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `temporal continuity` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `contextual boundedness` | G. Admissibility, Continuity, Source, and Loss | Chapter 5 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | canonical anchor available |
| `loss` | G. Admissibility, Continuity, Source, and Loss | Chapter 7 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `source basis` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md` | `04_reference/Evidence_Map.md` | anchor pending |
| `support mode` | G. Admissibility, Continuity, Source, and Loss | Chapter 7 — Shared Transformation Record | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md` | `04_reference/Evidence_Map.md` | anchor pending |
| `support status` | G. Admissibility, Continuity, Source, and Loss | Chapter 7 — Shared Transformation Record | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md`; `04_reference/Output_Class_Index.md` | `04_reference/Claim_Type_Table.md`; `04_reference/Evidence_Map.md` | anchor pending |
| `evidence availability` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `04_reference/Evidence_Map.md`; `04_reference/Claim_Type_Table.md` | `04_reference/Evidence_Map.md` | anchor pending |
| `Source Ceiling` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `calibration` | G. Admissibility, Continuity, Source, and Loss | Chapter 49 — Source Limits and Calibration Limits | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `anti-immunization` | G. Admissibility, Continuity, Source, and Loss | Chapter 50 — Anti-Immunization | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `canonical output class` | H. Results, Stop, Non-Capture, and Audit | Chapter 6 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Output_Class_Index.md` | anchor pending |
| `claim reduction` | H. Results, Stop, Non-Capture, and Audit | Chapter 6 | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Claim_Type_Table.md` | anchor pending |
| `stop` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `mandatory stop` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Output_Class_Index.md` | anchor pending |
| `optional stop` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `re-entry` | H. Results, Stop, Non-Capture, and Audit | Chapter 51 — Stop Conditions | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `failed transformation` | H. Results, Stop, Non-Capture, and Audit | Chapter 6 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Output_Class_Index.md` | anchor pending |
| `Non-Capture` | H. Results, Stop, Non-Capture, and Audit | Chapter 52 — Non-Capture | `05_minified/PMS_STRATA_Admissibility_Band_Minified.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `non-equivalence` | H. Results, Stop, Non-Capture, and Audit | Chapter 8 — Foundational Non-Equivalences | `05_minified/Chapter_Contracts.md`; `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Non_Equivalence_Index.md` | anchor pending |
| `local audit` | H. Results, Stop, Non-Capture, and Audit | Chapter 17 — PATH Cases, Countercases, and Local Audit | `05_minified/Chapter_Contracts.md` | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Output_Class_Index.md` | anchor pending |
| `Integrated STRATA Admissibility Audit` | H. Results, Stop, Non-Capture, and Audit | Chapter 53 — Integrated STRATA Admissibility Audit | `00_source/PMS-STRATA_Structure.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |
| `formal model boundary` | H. Results, Stop, Non-Capture, and Audit | Chapter 49 | `05_minified/PMS_STRATA_Minified_Canonical.md` | `04_reference/Admissibility_Band_Reference.md` | anchor pending |

### 8.1 Definition-site rule

A term may have one designated canonical definition site and multiple elaboration, application, audit, or index sites. A later detailed chapter does not become a competing definition site merely because it carries the fuller procedure.

```text
canonical definition site
≠
primary elaboration and audit site
```

---

## 9. PMS Operator Map

| Order | Operator | Name | PMS dependencies | Canonical source | Reference handoff | Planned relevant application routes | Critical boundary |
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

All chain records route additionally to Chapter 7, Chapter 53, `04_reference/Transformation_Operation_Index.md`, later case records, and `07_model/*`. Each occurrence retains its own claim, loss, and output class.

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

Field names and pointers above are now real formal handoffs. Future smoke records must instantiate them without treating schema validity as substantive admissibility, truth, causality, semantic adequacy, normative validity, person judgment, or application authority.

---

## 16. Case and Countercase Handoffs

| Test requirement | Primary chapter route | Future target | Current status |
| --- | --- | --- | --- |
| positive operation case | Chapters 17, 28, 40 | operation-specific Markdown and YAML case records | case handoff pending |
| negative operation case | Chapters 17, 28, 40 | countercase template and `03_cases/Case_Index.md` | case handoff pending |
| boundary or confusion case | Chapters 8, 16, 27, 37–39 | confusion-case template; `02_appendices/Appendix_I_Boundary_and_Confusion_Cases.md` | case handoff pending |
| Stop case | Chapters 51 and 53 | mandatory-stop smoke tests and later case record | Records 02 and 07 current; substantive case handoff pending |
| Non-Capture case | Chapters 52 and 53 | non-capture smoke test and later case record | Record 08 current; substantive case handoff pending |
| integrated chain case | Chapter 53 | integrated audit template; `02_appendices/Appendix_N_Integrated_STRATA_Audit_Template.md` | case handoff pending |

Cases test and expose rules. They do not define operations, claim types, output classes, or admissibility boundaries.

---

## 17. Appendix Handoffs

| Appendix | Title | Primary chapter route | Reference or model handoff | Current status |
| --- | --- | --- | --- | --- |
| A | Core Definitions | Chapters 0–8 | `04_reference/Glossary.md`; `04_reference/Non_Equivalence_Index.md` | appendix handoff pending |
| B | Formal Notation | Chapters 4–7 | `07_model/*`; `04_reference/Operator_Index.md` | appendix handoff pending |
| C | Shared Transformation Record Schema | Chapter 7 | `07_model/Transformation_Record.schema.json`; `04_reference/Claim_Type_Table.md` | appendix handoff pending |
| D | COMPOSE Record Template | Chapter 15 | `04_reference/Transformation_Operation_Index.md` | appendix handoff pending |
| E | DECOMPOSE Record Template | Chapter 20 | `04_reference/Transformation_Operation_Index.md` | appendix handoff pending |
| F | PROJECT_AS Record Template | Chapter 30 | `04_reference/Transformation_Operation_Index.md` | appendix handoff pending |
| G | Admissibility Band Tests | Chapters 44–53 | `04_reference/Admissibility_Band_Reference.md` | appendix handoff pending |
| H | Valid and Invalid Transformation Patterns | Chapters 16, 27, 39, 41 | `04_reference/Non_Equivalence_Index.md`; `04_reference/Audit_Checklist.md` | appendix handoff pending |
| I | Boundary and Confusion Cases | Chapters 8, 16, 27, 39 | `04_reference/Non_Equivalence_Index.md`; `03_cases/Case_Index.md` pending | appendix handoff pending |
| J | Operator-Weighting and Trajectory Stress Tests | Chapters 11, 35 | `04_reference/Operator_Index.md`; `04_reference/Claim_Type_Table.md` | appendix handoff pending |
| K | Cross-Domain Projection and Analogy Stress Tests | Chapters 36–37 | `04_reference/Claim_Type_Table.md`; `04_reference/Non_Equivalence_Index.md` | appendix handoff pending |
| L | Non-Operator Remainders and Decomposition Limits | Chapters 22, 25, 27, 52 | `04_reference/Claim_Type_Table.md`; `04_reference/Admissibility_Band_Reference.md` | appendix handoff pending |
| M | Case and Countercase Index | Chapters 17, 28, 40, 53 | `03_cases/Case_Index.md` pending | appendix handoff pending |
| N | Integrated STRATA Audit Template | Chapter 53 | `04_reference/Admissibility_Band_Reference.md`; `04_reference/Audit_Checklist.md` | appendix handoff pending |

---

## 18. Formal Model Handoffs

Repository artifacts are written with full internal paths. The seven Core artifacts and eight canonical smoke records are populated and audit-passed. The internal Formal Model v0 smoke-test gate has passed; this does not establish substantive truth, external warrant, or corpus completion.

The table records current Core roles and, for each committed smoke test, one expected canonical output per delimited tested claim.

| Artifact | Current status | Current or planned role | Tested claim or record focus | Expected canonical output | Controlled prose and reference sources | Prohibited automatic inference |
| --- | --- | --- | --- | --- | --- | --- |
| `07_model/Operation_Registry.yaml` | current formal model core; v0.1.3 | registers exactly COMPOSE, DECOMPOSE, and PROJECT_AS with structural requirements | registry artifact; no tested occurrence | not applicable | Chapters 4, 15, 20, 30; `04_reference/Transformation_Operation_Index.md` | empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/Output_Classes.yaml` | current formal model core; v0.1.1 | registers exactly ten canonical output values, constitutive profiles, and current load-bearing class boundaries | registry artifact; no tested occurrence | not applicable | Chapter 6; `04_reference/Output_Class_Index.md` | empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/Admissibility_Rules.yaml` | current formal model core; v0.1.2 | registers sixteen checks, twelve audit stages, local vocabularies, non-compensation, Stop, Non-Capture, anti-immunization, and ceilings | rule artifact; no tested occurrence | not applicable | Chapter 6 and Chapters 44–53; `04_reference/Admissibility_Band_Reference.md` | substantive admissibility, empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/Boundary_Decision_Tree.yaml` | current formal model core; v0.1.1 | routes complete semantic packets through candidate generation, claim separation, collision adjudication, diagnostics, and unique final selection without ranking or first-match logic | decision-routing artifact; no tested occurrence | not applicable | Chapter 6 and Chapters 44–53; `04_reference/Output_Class_Index.md`; `04_reference/Admissibility_Band_Reference.md`; `04_reference/Non_Equivalence_Index.md` | substantive truth, causal validity, semantic adequacy, normative validity, person judgment, or application authority |
| `07_model/Transformation_Record.schema.json` | current formal model core; v0.1.2 | validates occurrence and integrated-chain record form, required axes, pointer contracts, loss, diagnostics, candidate assessments, and routed results | schema artifact; no tested occurrence | not applicable | Chapter 7; `04_reference/Claim_Type_Table.md`; `04_reference/Transformation_Operation_Index.md` | adequacy of source interpretation or substantive claim validity |
| `07_model/PMS-STRATA.yaml` | current formal model core; version declared by the Root artifact itself | integrates component manifest, dependency graph, ownership matrix, inventory snapshots, record handoff, and package integrity declarations without independent theory authority | integrated registry artifact; no tested occurrence | not applicable | all controlled prose and Reference artifacts | empirical truth, causality, semantic or normative validity, person judgment, or application authority |
| `07_model/PMS-STRATA.schema.json` | current formal model core; v0.1.0 | validates the integrated root structure and declared integrity-binding form without duplicating component semantics | schema artifact; no tested occurrence | not applicable | controlled prose and formal registries | truth, completeness of theory, or application authority |
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

## 20. Open-Link Registry

| Open link family | Planned target | Reason still open | Unlock condition | Freeze stage |
| --- | --- | --- | --- | --- |
| Block section anchors | Chapters 1–57 and Front Matter units | Chapter 0 is available and provisionally re-locked; remaining target sections are not yet drafted | relevant chapter drafted and provisionally locked | per-chapter lock |
| final Glossary anchors | 112 core terms | chapter heading and section IDs do not yet exist | primary chapter anchors stable | Reference freeze |
| case IDs | positive, negative, confusion, stop, non-capture, and chain cases | case corpus not yet written | case record created and audited | Part lock / integrated audit |
| appendix anchors | Appendices A–N | appendices are empty | appendix content drafted after corpus and front matter | Appendix stage |
| Reference pathway families | `04_reference/Reader_Pathways.md` | populated pre-Block scaffold; actual chapter, case, appendix, model, derivative, and Reader anchors remain pending | route targets populated at their production stages | Reference Freeze |
| Reader implementation routes | `08_PMS-STRATA Reader/*` | implementation deferred and files empty | corpus, cases, references, model, and derivatives finalized | Reader / Release |
| derivative anchors | overview, paper, whitepaper | derivatives deferred | corpus audit and model finalization complete | Derivatives |

Core model field paths and schema pointers are no longer open links; their current handoffs are registered in Sections 15 and 18. No remaining pending link may be represented as a current citation target. Broken or missing future anchors are recorded, not silently inferred.

---

## 21. Post-Smoke / Foundations Cross-Reference Gate

This gate records navigation and handoff conformance only. It is not an Output Class and does not establish substantive truth. The Chapter-0 repair pass additionally requires exact claim-owner equality, absence of ad-hoc machine fields, internally consistent status/version language, and reality-checked open registries.

- [x] All eight canonical smoke records and `07_model/examples/README.md` are populated.
- [x] All eight records validate against the current Transformation Record Schema.
- [x] The three operation identities remain exactly `COMPOSE`, `DECOMPOSE`, and `PROJECT_AS`.
- [x] The ten canonical Output Classes remain closed and unchanged.
- [x] Expected classes and routes are recorded for all eight examples.
- [x] `01 → 03 → 08` handoffs resolve without class or authority inheritance.
- [x] All file, JSON Pointer, YAML, and Markdown-anchor control references resolve.
- [x] Record-level conformance remains distinct from substantive case or external evidence.
- [x] Root/Companion provenance and all changed registered Reference fingerprints are synchronized.
- [x] The Formal Model v0 internal smoke-test gate has passed.
- [x] Chapter 1 definition ownership, Chapter 3/5 boundaries, example assignments, work packages, and model handoffs are preparation-locked.
- [x] The Chapter 1 preparation record is a Reference control only and is not cited as canonical Chapter 1 prose.
- [x] Foundations production is active; Chapter 0 is provisionally locked; the Chapter 1 preparation gate, WP1–WP3 local audits, and WP4 integrated audit have passed; the Chapter 1 anchor resolves; all later chapter anchors remain pending.

```text
pass
→ Core and canonical smoke-suite routes current
→ suite-level and package audits passed
→ internal formal smoke gate closed
→ Chapters 0–3 routes are current and provisionally locked; Chapter 4 WP1–WP3 are canonical; WP4 is the next production handoff

fail
→ repair pointer, route, status, provenance, fingerprint, or authority handling before the next Foundations chapter
```

These gate terms are workflow-only and are not canonical Output Classes.

## 22. Revision and Freeze Policy

### 22.1 Pre-Block revision

During Foundations, PATH, SUB, RETYPE, LIMITS, conclusion, front matter, cases, and appendices, this map grows by adding actual anchors and verified handoffs. It must not absorb chapter prose or become a competing definition source.

### 22.2 Required update triggers

Update this map when:
- a primary definition site changes through an explicit architecture revision;
- a chapter or Front Matter anchor is created or renamed;
- a new case ID, appendix section, formal field path, schema pointer, or reader route becomes real;
- a Reference artifact is revised in a way that changes its handoff role;
- an audit finds duplicate ownership, a broken path, a circular authority relation, or an undeclared pending target.

### 22.3 Freeze sequence

```text
pre-Block Cross Reference scaffold
→ all four Reference scaffolds populated
→ Reference Kernel v0 population complete and provisionally controlled
→ Formal Model v0 Core Assembly and package audit
→ post-Model status and reference synchronization
→ Examples and smoke-test validation
→ full Formal Model v0 gate decision
→ chapter-anchor synchronization during Blocks
→ case and appendix synchronization
→ Reference freeze after Conclusion, Front Matter, and Appendices
→ corpus audit
→ model finalization
→ derivative and Reader routes
→ release freeze
```

Embedded artifact revision is not the same as global Reference Kernel freeze status.

---

## Chapter 2 WP1–WP3 Route

| Artifact | Role | Authority boundary | Current status |
| --- | --- | --- | --- |
| `04_reference/Chapter_2_Preparation_Record.md` | definition-ownership, architecture, execution history, case-assignment, work-package, and audit planning | Reference production control only | preparation gate and WP1–WP2 execution recorded |
| `01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level` | canonical Chapter 2 coordinate, scope, comparison, and Minimal Declaration prose | provisionally locked canonical corpus authority | Sections 2.1–2.14 available after integrated WP4 audit |
| `07_model/Transformation_Record.schema.json` | existing nested coordinate encoding | structure validation only | no preparation-stage change required |

The preparation and WP1–WP2 route fixes the conceptual-slot mapping to `/source/frame`, `/target/frame`, `/source/granularity`, `/target/granularity`, `/source/relative_level`, `/target/relative_level`, `/source/temporal_scope`, `/target/temporal_scope`, `/source/source_scope`, and `/claim/claim_scope`. This route does not make the preparation record a formal-model support input or a theory source.

## Chapter 2 WP2 Scope Architecture Handoff

| Canonical term | Primary anchor | Current downstream handoff | Boundary |
| --- | --- | --- | --- |
| temporal scope | [`Chapter 2 §2.6`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | Chapter 3; PATH; Shared Transformation Record | does not establish sequence, path, trajectory, or path dependence |
| source scope | [`Chapter 2 §2.7`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | Chapters 6–7, 49, LIMITS | not source object, source basis, source ceiling, or positive structure from a gap |
| claim scope | [`Chapter 2 §2.8`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | Chapters 5–7, 49–53 | not claim boundary, claim ceiling, validity scope, or authority inheritance |

The Chapter 2 Preparation Record remains the production-history route. Canonical scope definitions now belong to `01_blocks/01_foundations.md`. WP3 owns Sections 2.9–2.14 and may not redefine these scopes through declaration fields.

## Chapter 2 WP3 Coordinate-Comparison Handoff

| Chapter 2 WP3 family | Canonical owner | Primary downstream handoff | Boundary |
| --- | --- | --- | --- |
| stable frame / changed granularity | Section 2.9 | Chapters 19, 20, and 25 | coordinate pattern is not automatic `DECOMPOSE` |
| changed frame / stable granularity | Section 2.10 | Chapters 4, 5, and 30 | frame change is not automatic `PROJECT_AS` or `Φ` |
| changed relative level | Section 2.11 | all operation families | relation position is not operation identity or authority |
| multiple valid granularities | Section 2.12 | Chapters 25, 43, and 44 | plurality has no truth hierarchy |
| granularity conflict | Section 2.13 | Chapters 6, 25, 49, and 53 | mismatch neither proves nor dissolves contradiction |
| Minimal Level Declaration | Section 2.14 | Chapters 7 and operation records | conceptual handoff is not a second schema |

Canonical Sections 2.1–2.14 are available at [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level). `04_reference/Chapter_2_Preparation_Record.md` records production history and audit only. WP4 remains responsible for integrated lock review.

---

## Chapter 2 Provisional-Lock Handoff

Canonical owner:

- [`Chapter 2 — Frame, Granularity, and Relative Level`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)

Production-control history:

- [`Chapter 2 Preparation and Execution Record`](Chapter_2_Preparation_Record.md)

Formal mirror:

- [`Operation Registry`](../07_model/Operation_Registry.yaml) — open Chapter 2 coordinate-and-scope handoff only;
- [`Transformation Record Schema`](../07_model/Transformation_Record.schema.json) — existing nested paths, unchanged;
- [`Formal Model Root`](../07_model/PMS-STRATA.yaml) — package registration and fingerprints only.

Downstream owner routes:

```text
Chapter 2 coordinates and scopes
→ Chapter 3 temporal grammar
→ Chapter 4 operation identity
→ Chapter 5 transformation context and continuity
→ Chapter 6 admissibility
→ Chapter 7 record fields
→ Chapters 19/25 resolution procedures and outcomes
→ Chapters 42–45 coordinate LIMITS
→ Chapter 49 source and claim ceilings
→ Chapter 52 Stop and Non-Capture
```

The ten `C2-*` duties recorded in the Preparation Record are future Case assignments. They are not existing Case files, evidence, or completed Case Index entries.

---

## Chapter 3 Preparation and WP1 Route

| Chapter 3 preparation object | Primary control | Upstream dependency | Downstream handoff |
| --- | --- | --- | --- |
| configuration/state boundary | [Chapter 3 WP1](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapter 1 object model | Chapter 5 continuity; PATH |
| event/non-event/transition boundary | [Chapter 3 WP1](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | PMS `Λ`, Chapter 1 object eligibility | Chapters 9, 13, 14 |
| sequence/path/trajectory burden chain | [Chapter 3 WP2](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapters 1–2 and WP1 temporal objects | PATH Chapters 9–12 |
| path dependence as property | [Chapter 3 §3.9](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | trajectory burden, supported counterfactual sensitivity, operator constraints | Chapter 12; LIMITS |
| sedimentation/irreversibility | [Chapter 3 §§3.10–3.11](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | source-supported carriers and bounded restoration criterion | PATH, Appendix J, LIMITS |
| unrealized alternatives | [Chapter 3 §3.12](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | source-supported availability and non-traversal | Chapter 13; cases |
| Minimal Temporal Object Chain | [Chapter 3 §3.13](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | all Chapter 3 definitions and downgrade route | Chapter 4 and PATH |
| production control | `04_reference/Chapter_3_Preparation_Record.md` | ZIP 68 preparation source; ZIP 69 WP1 source; ZIP 70 WP2 source; ZIP 71 WP3 source; ZIP 72 WP4 source | WP1–WP4 complete; provisional lock recorded |

Current route status:

```text
Chapters 0–2 provisionally locked
→ Chapter 3 Preparation Gate complete
→ Chapter 3 provisionally locked
→ Chapter 4 Preparation Gate complete
→ Chapter 4 provisional lock complete; Chapter 5 Preparation Gate and WP1–WP2 complete; Chapter 5 WP3 next
```

The Preparation Record is a route and audit artifact, not a substitute for future canonical prose.



## Chapter 3 WP1 Canonical Route

```text
Chapter 1 object-category eligibility
→ Chapter 2 coordinate architecture
→ Chapter 3 Sections 3.1–3.5
   configuration / state / event / non-event / transition
→ Chapter 3 WP2
   sequence / path / trajectory
→ Chapter 3 WP3
   historical properties and minimal chain — canonical and locally audited
```

Canonical return: [`01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory). The Preparation Record supplies production history only.

## Chapter 3 WP2 Canonical Route

```text
Chapter 3 WP1 temporal objects
→ Section 3.6 sequence
→ Section 3.7 path
→ Section 3.8 trajectory
→ Chapter 3 WP3 historical properties and Minimal Temporal Object Chain — canonical
→ Chapter 3 WP4 integrated audit and lock decision
→ PATH Chapters 9–12 operationalization
```

| WP2 object | Canonical return | Operational handoff | Boundary |
| --- | --- | --- | --- |
| sequence | [Chapter 3 §3.6](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapter 9 | order does not establish traversal or cause |
| path | [Chapter 3 §3.7](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapter 10 and Chapter 15 | object burden does not complete `COMPOSE` |
| trajectory | [Chapter 3 §3.8](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapters 11–12 and RETYPE Chapters 31–33 | no automatic path dependence, teleology, or target function |

The Preparation Record is execution history only and cannot replace these canonical definitions.

## Chapter 3 WP3 Canonical Route

```text
Chapter 3 WP2 warranted trajectory
→ Section 3.9 path dependence as separately tested property
→ Section 3.10 sedimentation
→ Section 3.11 bounded irreversibility
→ Section 3.12 source-supported unrealized alternatives
→ Section 3.13 Minimal Temporal Object Chain and downgrade ladder
→ Chapter 3 WP4 integrated audit and provisional-lock decision
→ PATH operational chapters
```

| WP3 object/property | Canonical return | Operational handoff | Boundary |
| --- | --- | --- | --- |
| path dependence | [Chapter 3 §3.9](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapter 12 | property, not object class; no `Θ` or duration shortcut |
| sedimentation | [Chapter 3 §3.10](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapters 11–12 and Appendix J | requires carrier and later praxis effect |
| bounded irreversibility | [Chapter 3 §3.11](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | PATH and LIMITS | restoration criterion required; no metaphysical absolute |
| unrealized alternative | [Chapter 3 §3.12](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapter 13 | availability must be source-supported |
| Minimal Temporal Object Chain | [Chapter 3 §3.13](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | Chapter 4 and PATH | no automatic derivation, operation identity, or record schema |

---

## Chapter 3 Provisional-Lock Route

Canonical temporal definitions now return to [`Chapter 3`](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory). `04_reference/Chapter_3_Preparation_Record.md` records the completed preparation and WP1–WP4 audit history. Chapter 4 is provisionally locked; the next production route is Chapter 5 preparation. PATH Chapters 9–13 may operationalize temporal objects and properties but must not create a competing definition layer.

---

## Chapter 4 Preparation Route

| Route element | Current target | Boundary |
| --- | --- | --- |
| architecture and chapter obligations | `00_source/PMS-STRATA_Structure.md`; `05_minified/Chapter_Contracts.md` | blueprint and contract do not equal delivered prose |
| production-control record | `04_reference/Chapter_4_Preparation_Record.md` | preparation record is not a theory source |
| operation inventory and compact signatures | `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`; `04_reference/Transformation_Operation_Index.md` | compact or reference control may not replace Chapter 4 prose |
| source objects and coordinates | provisionally locked Chapters 1–3 | object and coordinate labels do not establish operation identity |
| formal mirror | `07_model/Operation_Registry.yaml`; `07_model/Transformation_Record.schema.json` | registration and schema validity do not establish semantic adequacy |
| next canonical destination | Chapter 4 WP4 integrated synchronization and lock | Sections 4.1–4.10 are canonical; WP4 changes prose only for demonstrated integration defects |

```text
Chapter 4 Preparation Record
→ canonical Chapter 4 Sections 4.1–4.7
→ Chapters 15 / 20 / 30 procedures
→ Chapter 7 recording
→ Chapter 8 non-equivalence audit
→ LIMITS and integrated cases
```

Every downstream route must return to canonical Chapter 4 for operation identity and must not infer a fourth operation from a chain, coordinate movement, comparison, audit, or confusion case.

---

## Chapter 4 WP1 Canonical Routing

```text
Chapter 4 WP1 canonical prose
→ explicit operation identity
→ COMPOSE / DECOMPOSE / PROJECT_AS core signatures
→ common-source-family positive and negative examples
→ WP2 direction and chain architecture — canonical
→ WP3 non-invertibility, confusion, and declaration
```

Primary return: [`01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as).

The route now distinguishes canonical WP1–WP2 prose from the non-theory Preparation Record. Sections 4.8–4.10, Chapter 5 continuity, Chapter 7 recording, and Chapters 15/20/30 procedures remain downstream.

---

## Chapter 4 WP2 Direction and Chain Routing

```text
Chapter 4 WP1 signatures
→ Section 4.5 transformation direction
→ Section 4.6 operation / level relation
→ Section 4.7 operation chains
→ WP3 non-invertibility, confusion, and declaration
```

| WP2 concept | Canonical return | Required downstream handoff | Boundary |
| --- | --- | --- | --- |
| transformation direction | [Chapter 4 §4.5](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapter 8 non-equivalence audit | no ontological, temporal, claim, or authority ascent |
| operation / level relation | [Chapter 4 §4.6](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapter 2 coordinates; Chapter 5 continuity | level tendency never defines operation identity |
| operation chain | [Chapter 4 §4.7](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapter 7 records; Chapters 15/20/30 procedures | every link is a separate occurrence and claim |
| failure propagation | [Chapter 4 §4.7](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapter 6 outputs; LIMITS | no inherited validity and no later-link rescue |

The six required chain families are now canonically present. WP3 retains non-invertibility, integrated confusion, `C4-STOP-01`, `C4-NC-01`, and the Minimal Operation Declaration.

---

## Chapter 4 WP3 Non-Invertibility, Confusion, and Declaration Routing

```text
Chapter 4 core signatures and chains
→ Section 4.8 non-invertibility
→ Section 4.9 operation confusion
→ Section 4.10 Minimal Operation Declaration
→ WP4 integrated lock
```

| WP3 concept | Canonical return | Downstream handoff | Boundary |
| --- | --- | --- | --- |
| non-invertibility | [Chapter 4 §4.8](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapters 15/20/30 procedure; LIMITS loss | no total-loss or metaphysical claim |
| operation confusion | [Chapter 4 §4.9](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapter 8 audit; Appendix I | no fourth operation or forced identity |
| Minimal Operation Declaration | [Chapter 4 §4.10](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapter 7 record | conceptual mapping only; no second schema |
| collapsed chain stop | [Chapter 4 §4.9](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Chapter 6 / LIMITS | separate occurrences before continuation |
| unresolved identity non-capture | [Chapter 4 §4.9](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | Cases and re-entry evidence | protects neither rival strong claim |

---

## Chapter 4 Provisional-Lock Route

Canonical operation definitions now return to [`Chapter 4`](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as). `04_reference/Chapter_4_Preparation_Record.md` records preparation and WP1–WP4 audit history. The Chapter 5 Preparation Gate and WP1 are complete; the next production route is Chapter 5 WP2. Chapters 15, 20, and 30 may operationalize the three operations but may not add a fourth core operation or competing signature definition.

---

## Chapter 5 Preparation Routing

```text
Chapter 1 source-object identity
+ Chapter 2 coordinates and scopes
+ Chapter 3 historical load
+ Chapter 4 operation identity
→ Chapter 5 continuity and context preparation
```

Primary production-control file: `04_reference/Chapter_5_Preparation_Record.md`.

| Prepared concept | Future canonical owner | Current compact control | Downstream operational owner |
| --- | --- | --- | --- |
| origin type | Chapter 5 | Chapter Contract; Canonical Minified | Chapters 29–30 |
| target function | Chapter 5 | Operation Signatures Minified | Chapters 29–37 |
| transformation context | Chapter 5 | Chapter Contract; Shared Record fields | Chapters 7 and 30 |
| reference continuity | Chapter 5 | Canonical Minified | Chapter 47 |
| type integrity / type continuity | Chapter 5 | Admissibility Band Minified | Chapters 6, 38, and 47 |
| functional continuity | Chapter 5 | Canonical Minified | RETYPE and Chapter 47 |
| temporal continuity | Chapter 5 | Canonical Minified | PATH, RETYPE, and Chapter 47 |
| contextual boundedness | Chapter 5 | Admissibility Band Minified | Chapters 6, 30, 39, and 47 |

Until canonical drafting, all Chapter 5 terminology returns to the Structure, Chapter Contract, minified controls, and this non-theory preparation record. The preparation route cannot substitute for the missing canonical anchor.

---

## Chapter 5 WP1 Cross-Reference Route

```text
Chapter 1 object identity and typing
→ Chapter 2 coordinates and scopes
→ Chapter 4 PROJECT_AS signature
→ Chapter 5 §5.1 origin type
→ Chapter 5 §5.2 target function
→ Chapter 5 §5.3 target / transformation context
→ Chapter 5 WP2 continuity criteria
→ Chapter 6 admissibility
→ Chapter 7 Shared Transformation Record
```

Canonical return: [`Chapter 5 WP1`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP2 Continuity Cross-Reference Handoff

| Chapter 5 WP2 concept | Canonical site | Upstream dependency | Downstream consumer | Boundary |
| --- | --- | --- | --- | --- |
| reference identity and continuity | Chapter 5 §5.4 | Chapter 1 object identity; Chapter 4 operation relation | Chapters 6, 7, 47 | same label is not continuity proof |
| type integrity and continuity | Chapter 5 §5.5 | Chapter 1 typing; Chapter 4 `PROJECT_AS` signature | Chapters 6, 38, 47 | function does not replace origin type |
| functional continuity | Chapter 5 §5.6 | Chapter 5 §§5.1–5.3 source/function/context | Chapters 6, 30, 47 | function must be source-sensitive |
| mixed continuity findings | Chapter 5 §5.4–5.6 | canonical Output Classes | Chapters 6 and 47 | one passing dimension does not compensate for another failure |
| temporal continuity and contextual boundedness | Chapter 5 §§5.7–5.9 | Chapters 2–3 | Chapters 6, 30, 47 | canonical; Chapter 5 provisionally locked |

Canonical return: [`Chapter 5`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context).

## Chapter 5 WP3 Temporal and Contextual Cross-Reference Handoff

| Chapter 5 WP3 control | Upstream dependency | Downstream consumer | Boundary |
| --- | --- | --- | --- |
| Temporal Continuity | Chapters 2–3 temporal objects and scopes | Chapters 6, 31–35, 47 | not exhaustive chronology or timeless identity |
| Contextual Boundedness | Chapter 2 scopes; Chapter 5 target and transformation contexts | Chapters 6, 29–38, 49, 57 | no automatic context or authority transfer |
| four-dimension continuity matrix | Chapter 5 §§5.4–5.7 | Chapters 6–7 and 47 | dimensions remain non-compensatory |
| Minimal Projection Form | Chapters 2 and 4 minimal declarations; existing record paths | Chapter 7 and RETYPE | conceptual mapping, not second schema |
| Stop and Non-Capture pressure | Chapters 0 and 4 | Chapters 51–53 | weak claims remain unprotected |

Canonical return: [`Chapter 5`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context). WP4 owns integrated synchronization and provisional lock.

---

## Chapter 5 Canonical Route and Provisional Lock

Canonical Sections 5.1–5.9 are available at [`Chapter 5`](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context). `04_reference/Chapter_5_Preparation_Record.md` records preparation, WP1–WP4 execution, fifteen later case duties, Formal Model handoff, integrated audit, and provisional-lock rationale. It is not a second theory source.

```text
Chapter 1 object identity
→ Chapter 5 transformation continuity
→ Chapter 6 integrated admissibility
→ Chapter 7 record serialization
```

## Chapter 6 Preparation Cross-Reference Route

```text
Chapter 0
→ claim and authority ceiling

Chapters 1–5
→ object, coordinate, temporal, operation,
  context, and continuity burdens

Chapter 6
→ Relevance Floor / Traceability Ceiling
→ PraxisPurchase / TraceableLoad
→ Counterfactual Sensitivity
→ non-compensatory unified test
→ No Universal STRATA Scale

Chapter 7
→ records the test declarations and results

Chapter 8
→ indexes the governing non-equivalences

Chapters 44–53
→ expand and integrate the same band under LIMITS
```

Primary controls: [`Admissibility Band Reference`](Admissibility_Band_Reference.md) and [`Chapter 6 Preparation Record`](Chapter_6_Preparation_Record.md).

---

## Chapter 6 WP1 Cross-Reference Route

```text
Chapter 1 object identity
+ Chapter 2 coordinates and scopes
+ Chapter 3 temporal burdens
+ Chapter 4 operation occurrence
+ Chapter 5 continuity and context
→ Chapter 6 §6.1 operating range
→ §6.2 Relevance Floor / PraxisPurchase
→ §6.3 praxis-relevant dimensions
→ §6.4 gain / neutrality / below-floor Stop pressure
→ Chapter 6 WP2 upper-bound source-load tests
→ Chapter 7 record serialization
```

Canonical return: [`Chapter 6 WP1`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

---

## Chapter 6 WP2 Canonical Cross-Reference Route

```text
Chapter 6 §6.5
→ Praxeological Traceability Ceiling

Chapter 6 §6.6
→ TraceableLoad
→ source citation ≠ mapping ≠ dependency

Chapter 6 §6.7
→ abstraction / fragmentation / projection without load

Chapter 6 §6.8
→ Counterfactual Sensitivity
→ sensitive / partial / insensitive / underdetermined / not testable
```

Primary canonical return: [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band). Production history: [`Chapter 6 Preparation Record`](Chapter_6_Preparation_Record.md).

---

## Chapter 6 WP3 Canonical Cross-Reference Route

```text
Chapter 6 §6.9
→ Type Integrity handoff
→ semantic attraction ≠ operator identity

Chapter 6 §6.10
→ Reference Continuity handoff
→ citation or same name ≠ same referent

Chapter 6 §6.11
→ unified conjunctive test
→ non-compensation
→ claim segmentation and reduction

Chapter 6 §6.12
→ below / within / above band
→ ten-class routing boundary
→ Stop and Non-Capture

Chapter 6 §6.13
→ No Universal STRATA Scale
→ bounded local comparison remains possible
```

Primary canonical return: [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band). Production history: [`Chapter 6 Preparation Record`](Chapter_6_Preparation_Record.md).

---

## Chapter 6 Provisional-Lock Route

Primary canonical return: [`Chapter 6`](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band).

Production and audit history: [`Chapter 6 Preparation and Execution Record`](Chapter_6_Preparation_Record.md).

Formal mirror: [`Admissibility Rules`](../07_model/Admissibility_Rules.yaml), including the open `chapter_6_admissibility_band_handoff`.

Downstream ownership remains with Chapter 7 for record serialization, Chapter 8 for Foundational Non-Equivalences, Chapters 44–53 for expanded LIMITS procedure, `03_cases/*` for produced cases, and model finalization for any justified schema revision.

---

## Chapter 7 Preparation Cross-Reference Route

```text
PMS.yaml
→ Chapters 0–6 under provisional lock
→ Chapter 7 contract and Structure blueprint
→ Chapter 7 Preparation Record
→ future canonical Sections 7.1–7.10
→ Appendix C and operation-specific templates
→ Transformation Record schema as mirror
→ cases and Integrated STRATA Audit
```

Current route:

| Need | Current controlled source | Future canonical return |
| --- | --- | --- |
| shared record purpose and boundary | `05_minified/Chapter_Contracts.md`; `04_reference/Chapter_7_Preparation_Record.md` | Chapter 7 §7.1 |
| Source Declaration | Structure §7.2; Preparation Record | Chapter 7 §7.2 |
| Operation Declaration | Chapter 4; Structure §7.3; Preparation Record | Chapter 7 §7.3 |
| Target Declaration | Chapters 1, 2, and 5; Structure §7.4 | Chapter 7 §7.4 |
| Admissibility Declaration | Chapter 6; Structure §7.5 | Chapter 7 §7.5 |
| Loss Declaration | Structure §7.6; current schema mirror | Chapter 7 §7.6 |
| alternatives and non-translation | Structure §7.7; Preparation Record | Chapter 7 §7.7 |
| governance and authority boundary | Chapter 0; Structure §7.8 | Chapter 7 §7.8 |
| separated status/result axes | Structure §7.9; Claim and Output indexes | Chapter 7 §7.9 |
| chains, extensions, local/integrated use | Chapters 4 and 7 contract; current schema mirror | Chapter 7 §7.10 |

No canonical Chapter 7 anchor is claimed at the Preparation Gate. The existing schema is a comparison and implementation artifact, not the return authority.

---

## Chapter 7 WP1 Cross-Reference Synchronization

| Chapter 7 WP1 duty | Upstream owner | Current canonical route | Formal carrier candidate | Later handoff |
| --- | --- | --- | --- | --- |
| record boundary | Chapters 0 and 7 | [§7.1](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record) | root record identity and metadata | Appendix C |
| source reference and typing | Chapters 1–3 | §7.2 | `/source/reference_object`, `/source/object_typing` | cases and operation templates |
| source coordinates and scopes | Chapter 2 | §7.2 | `/source/frame`, `/source/granularity`, `/source/relative_level`, scopes | Parts and operation templates |
| Source Basis and Constitutive Source Trace | Chapters 5–6 | §7.2 | `/source/source_basis`, `/source/constitutive_source_trace` | admissibility audit |
| occurrence identity and operation kind | Chapter 4 | §7.3 | `/operation/occurrence_id`, `/operation/kind` | chain architecture in WP3 |
| selection and transformation context | Chapters 4–5 | §7.3 | `/operation/selection_rule`, `/operation/transformation_context` | operation chapters |
| target reference, typing, and function | Chapters 1, 4, 5 | §7.4 | `/target/*` | continuity and operation templates |

The schema paths are implementation carriers and do not replace the canonical prose.

---

## Chapter 7 WP2 Cross-Reference Synchronization

| Duty | Canonical owner | Consumed upstream source | Current formal carrier |
| --- | --- | --- | --- |
| Admissibility Declaration | Chapter 7 §7.5 | Chapters 5–6 | `/admissibility/*` plus Source, Target, and Claim pointers |
| five-part Loss Declaration | Chapter 7 §7.6 | Chapters 4–6 operation and continuity burdens | `/loss/preserved`, `/compressed`, `/excluded`, `/uncertain`, `/irrecoverable` |
| Alternatives Declaration | Chapter 7 §7.7 | Chapter 4 operation closure and Chapters 5–6 boundaries | `/alternatives/*` |
| Governance Declaration | Chapter 7 §7.8 | Chapter 0 Claim/Authority boundary and Chapters 5–6 Stop/Non-Capture | `/claim/claim_ceiling`, `/admissibility/*assessment`, `/governance/*` |

Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record). Sections 7.9–7.10 remain pending WP3.

---

## Chapter 7 WP3 Cross-Reference Synchronization

| WP3 concept | Canonical site | Upstream owner | Downstream handoff |
| --- | --- | --- | --- |
| separated status axes | Chapter 7 §7.9 | Chapters 0, 5, and 6 | Output Class Index, schema, cases |
| routed versus formal diagnostic | Chapter 7 §7.9 | Chapter 6 routing boundary | Decision Tree and record schema |
| claim-relative capture | Chapter 7 §7.9 | Chapter 0 Stop/Non-Capture boundary | cases and integrated audit |
| operation chains | Chapter 7 §7.10 | Chapter 4 chain semantics | operation-specific records and cases |
| local extensions | Chapter 7 §7.10 | Chapter Contracts and Part ownership | Appendices D–F and later Parts |
| integrated use | Chapter 7 §7.10 | Chapters 0–6 | Integrated STRATA Audit |

Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record). Chapter 7 is theoretically complete through §7.10; WP4 remains pending.

---

## Chapter 7 WP4 Provisional-Lock Synchronization

Chapter 7 is provisionally locked after integrated ownership, redundancy, status, case-duty, prose-to-schema, link, schema, fingerprint, package, and roundtrip audit. The Shared Transformation Record records transformation claims without becoming the transformation, a truth proof, or an authority source. The existing record schema supplies lower-authority structural carriers; its Chapter-7 handoff annotation does not redefine canonical prose. The sixteen Chapter-7 case identifiers remain later production duties rather than completed evidence. Canonical return: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record).

---

## Chapter 8 Preparation Cross-Reference Synchronization

| Chapter 8 cluster | Primary definition returns | Preparation route | Later specialist handoff |
| --- | --- | --- | --- |
| granularity, relative level, composition, decomposition | Chapters 0, 2, 4, and 6 | [`Chapter 8 Preparation Record`](Chapter_8_Preparation_Record.md) | SUB and LIMITS |
| sequence, path, trajectory, path dependence | Chapter 3 | Chapter 8 Preparation Record | PATH Chapters 9–14 |
| origin type, target function, projection, operator identity, weighting | PMS Base and Chapters 1, 4, and 5 | Chapter 8 Preparation Record | RETYPE Chapters 29–35 |
| analogy, recursion, legibility, authority | Chapters 0, 5, 6, and 7 | Chapter 8 Preparation Record | RETYPE, LIMITS, Cases, Appendices H–K |

The Non-Equivalence Index is the current reference catalogue. It remains subordinate to future canonical Chapter-8 prose and may not create parallel pair definitions. No Chapter-8 block anchor exists yet.

---

## Chapter 8 WP1 Canonical Return Map

| WP1 pair | Canonical Chapter-8 site | Primary definition returns |
| --- | --- | --- |
| finer granularity ≠ higher truth | [Section 8.1](../01_blocks/01_foundations.md#81-finer-granularity-is-not-higher-truth) | Chapters 0, 2, 6 |
| relative level ≠ ontological layer | [Section 8.2](../01_blocks/01_foundations.md#82-relative-level-is-not-ontological-layer) | Chapters 0, 1, 2, 4 |
| composition ≠ lossless addition | [Section 8.3](../01_blocks/01_foundations.md#83-composition-is-not-lossless-addition) | Chapters 1, 4, 6, 7 |
| decomposition ≠ discovery of final constituents | [Section 8.4](../01_blocks/01_foundations.md#84-decomposition-is-not-discovery-of-final-constituents) | Chapters 1, 2, 4, 6, 7 |

Chapter 8 owns the audit statement and contrast form. The returned chapters retain the definitions of the paired terms.

---

## Chapter 8 WP2 Canonical Return Map

| WP2 pair | Canonical Chapter-8 site | Primary definition returns |
| --- | --- | --- |
| path ≠ sequence | [Section 8.5](../01_blocks/01_foundations.md#85-path-is-not-sequence) | Chapters 1, 2, 3, 4, 6, 7 |
| path ≠ trajectory | [Section 8.6](../01_blocks/01_foundations.md#86-path-is-not-trajectory) | Chapters 3, 5, 6, 7 |
| trajectory ≠ path dependence | [Section 8.7](../01_blocks/01_foundations.md#87-trajectory-is-not-path-dependence) | Chapters 3, 5, 6, 7 |
| origin type ≠ target function | [Section 8.8](../01_blocks/01_foundations.md#88-origin-type-is-not-target-function) | Chapters 1, 4, 5, 6, 7 |
| projection ≠ operator identity | [Section 8.9](../01_blocks/01_foundations.md#89-projection-is-not-operator-identity) | PMS Base; Chapters 0, 1, 4, 5, 7 |
| operator weighting ≠ operator replacement | [Section 8.10](../01_blocks/01_foundations.md#810-operator-weighting-is-not-operator-replacement) | PMS Base; Chapters 0, 1, 2, 5, 6, 7; later Chapter 35 |

Chapter 8 owns the audit statement and contrast form. The returned sources retain definitions and procedures.

---

## Chapter 8 WP3 Canonical Return Map

| WP3 pair or integration duty | Canonical Chapter-8 site | Primary definition returns |
| --- | --- | --- |
| structural analogy ≠ valid projection | [Section 8.11](../01_blocks/01_foundations.md#811-structural-analogy-is-not-valid-projection) | Chapters 0, 1, 2, 4, 5, 6, 7; later RETYPE |
| recursion ≠ completeness | [Section 8.12](../01_blocks/01_foundations.md#812-recursion-is-not-completeness) | Chapters 0, 1, 2, 4, 5, 6, 7; later LIMITS |
| legibility ≠ authority | [Section 8.13](../01_blocks/01_foundations.md#813-legibility-is-not-authority) | PMS Base; Chapters 0, 2, 5, 6, 7; later Integrated Audit and LIMITS |
| integrated thirteen-pair matrix | [Section 8.13 matrix](../01_blocks/01_foundations.md#integrated-thirteen-pair-comparison-matrix) | PMS Base and Chapters 0–7 |
| integrated catalogue use | [Section 8.13 catalogue use](../01_blocks/01_foundations.md#integrated-catalogue-use) | Chapters 6–7 for routing, Stop, Non-Capture, and records |

Chapter 8 owns the compact audit contrasts. The returned sources retain definitions, operation procedures, admissibility, routing, and authority control.

---

## Chapter 8 WP4 Canonical Lock and PATH Handoff

Canonical Chapter 8 is [provisionally locked](../01_blocks/01_foundations.md#chapter-8-integrated-completion-and-foundations-provisional-lock). Its thirteen pairs return to Chapters 0–7 and PMS Base; its integrated matrix and catalogue use remain audit navigation rather than a replacement definition layer.

The bounded Formal-Model mirror is `07_model/Boundary_Decision_Tree.yaml#chapter_8_foundational_non_equivalence_handoff`. The handoff adds no route, Rule, operation, Output Class, or automatic semantic inference.

Foundations Chapters 0–8 are provisionally complete. The next production route is Chapter 9 Preparation in Part I — PATH.

---

## Chapter 9 Preparation Route

| Duty | Governing source | Chapter 9 destination | Boundary return |
| --- | --- | --- | --- |
| temporal object definitions | [Chapter 3](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory) | operational transition use | no redefinition |
| frame and temporal scope | [Chapter 2](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level) | temporal-position and comparison declarations | no unmarked frame change |
| `Θ`, `Λ`, `Φ` | `PMS.yaml` and [`Operator Index`](Operator_Index.md) | bounded operator-occurrence references | no operator retyping |
| transition versus operation | [Chapter 4](../01_blocks/01_foundations.md#chapter-4-the-three-strata-operations-compose-decompose-and-project_as) | transition record handoff | no fourth operation |
| continuity and recontextualization | [Chapter 5](../01_blocks/01_foundations.md#chapter-5-origin-type-target-function-and-transformation-context) | preservation of prior trace | no retroactive erasure |
| admissibility and routing | [Chapter 6](../01_blocks/01_foundations.md#chapter-6-the-strata-admissibility-band) | transition passage/failure pressure | no temporal score |
| record architecture | [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record) | minimal transition declaration | record completion ≠ transition truth |
| non-equivalence audit | [Chapter 8](../01_blocks/01_foundations.md#chapter-8-foundational-non-equivalences) | PATH-entry confusion control | no category laundering |
| path formation | Chapter 10, pending | receives warranted transitions | no path composition in Chapter 9 |

Production-control route: [`Chapter 9 Preparation Record`](Chapter_9_Preparation_Record.md). Canonical Chapter 9 remains pending.

---

## Chapter 9 WP1 Canonical Route

| WP1 concept | Primary return | Canonical route | Deferred handoff |
| --- | --- | --- | --- |
| PATH purpose | Chapter 0 boundary; Chapters 3–4 | [§9.1](../01_blocks/02_part_i_path.md#9-1-purpose-of-path) | path formation Chapter 10; `COMPOSE` Chapter 15; function RETYPE |
| `Θ` temporal structuring | `PMS.yaml`; Chapters 1 and 3 | [§9.2](../01_blocks/02_part_i_path.md#9-2-theta-as-temporal-structuring) | duration through transition in §§9.5–9.12 |
| temporal position | Chapters 2–3 | [§9.3](../01_blocks/02_part_i_path.md#9-3-temporal-position) | transition comparison in §§9.10–9.12 |
| order dependence | Chapters 3, 6, and 8 | [§9.4](../01_blocks/02_part_i_path.md#9-4-order-dependence) | later path-dependence test Chapter 12 |
| five WP1 pressure cases | Preparation Record assignments | §§9.1–9.4 | later `03_cases/*` production |

WP1 supplies bounded temporal-position and order-sensitive findings. It does not supply a path or operation result.

---

## Chapter 9 WP2 Canonical Route

| Concept | Primary return | Canonical route | Deferred handoff |
| --- | --- | --- | --- |
| duration | Chapters 2–3; Chapter 6 | [§9.5](../01_blocks/02_part_i_path.md#9-5-duration) | transition test §9.10 |
| delay | Chapter 3 non-event; `Λ` in PMS Base | [§9.6](../01_blocks/02_part_i_path.md#9-6-delay) | branches/delays Chapter 13 |
| persistence | Chapter 3 temporal objects | [§9.7](../01_blocks/02_part_i_path.md#9-7-persistence) | sedimentation Chapter 12 |
| bounded irreversibility | Chapter 3 §3.11 | [§9.8](../01_blocks/02_part_i_path.md#9-8-irreversibility) | PATH boundaries Chapter 16 |
| temporal recontextualization | Chapter 5 continuity; `Φ` boundary | [§9.9](../01_blocks/02_part_i_path.md#9-9-temporal-recontextualization) | RETYPE only through separate claim |

---

## Chapter 9 WP3 Canonical Route

- Transition preconditions: [`§9.10`](../01_blocks/02_part_i_path.md#9-10-transition-preconditions)
- Transition structure and Shared Record mapping: [`§9.11`](../01_blocks/02_part_i_path.md#9-11-transition-structure)
- Transition failure, routing, and Chapter 10 handoff: [`§9.12`](../01_blocks/02_part_i_path.md#9-12-transition-failure)
- Primary transition object definition: [Chapter 3](../01_blocks/01_foundations.md#chapter-3-configuration-event-non-event-transition-path-and-trajectory)
- Shared Record ownership: [Chapter 7](../01_blocks/01_foundations.md#chapter-7-shared-transformation-record)
- Non-equivalence returns: [Chapter 8](../01_blocks/01_foundations.md#chapter-8-foundational-non-equivalences)
- Production control: [`Chapter 9 Preparation Record`](Chapter_9_Preparation_Record.md)

Chapter 10 path formation and Chapter 15 `COMPOSE` remain pending.


## Chapter 9 Provisional-Lock Handoff

| From | To | Controlled handoff |
| --- | --- | --- |
| Chapter 3 | Chapter 9 | temporal-object definitions → operational transition tests |
| Chapters 5–7 | Chapter 9 | continuity, admissibility, and Shared Record carriers |
| Chapter 8 | Chapter 9 | non-equivalence guards for sequence, path, trajectory, function, and authority |
| Chapter 9 | Chapter 10 | individually warranted transition records without Path identity |
| Chapter 9 | Admissibility Rules | prose-owned non-routing transition-gate mirror |

Chapter 9 is provisionally locked. The next production route is [`Chapter 10 — Preparation`](../05_minified/Chapter_Contracts.md#chapter-10-path).

---

## Chapter 10 Preparation Route

| Duty | Governing source | Chapter 10 destination | Boundary return |
| --- | --- | --- | --- |
| core path object and actual traversal | [Chapter 3 §3.7](../01_blocks/01_foundations.md#37-path) | operational path threshold | no redefinition or automatic trajectory |
| analytical coordinates | [Chapter 2](../01_blocks/01_foundations.md#2-frame-granularity-and-relative-level) | path frame, periodization, comparison basis | no unmarked coordinate change |
| transition inputs | [Chapter 9](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition) | path components and traversal chain | transition set ≠ path automatically |
| continuity and boundedness | [Chapter 5](../01_blocks/01_foundations.md#5-origin-type-target-function-and-transformation-context) | reference/path identity and frame handoff | no endpoint or frame substitution |
| admissibility and routing | [Chapter 6](../01_blocks/01_foundations.md#6-the-strata-admissibility-band) | path passage, failure, Stop, Non-Capture | no narrative or evidence score |
| Shared Record | [Chapter 7](../01_blocks/01_foundations.md#7-shared-transformation-record) | minimal path carrier | record completeness ≠ path truth |
| non-equivalence control | [Chapter 8](../01_blocks/01_foundations.md#8-foundational-non-equivalences) | chronology/path, path/trajectory, legibility/authority guards | no category laundering |
| trajectory formation | Chapter 11, pending | receives warranted path object | no sedimentation claim in Chapter 10 |
| full `COMPOSE` procedure | Chapter 15, pending | later operation occurrence | path-object burden ≠ completed operation |

Production-control route: [`Chapter 10 Preparation Record`](Chapter_10_Preparation_Record.md). Canonical Chapter 10 remains pending.

---

## Chapter 10 WP1 Canonical Route

| WP1 concept | Primary return | Canonical route | Deferred handoff |
| --- | --- | --- | --- |
| path threshold | Chapters 3 and 9 | [§10.1](../01_blocks/02_part_i_path.md#10-1-definition-of-path) | status §§10.7–10.10; trajectory Chapter 11 |
| chronology/sequence/path | Chapters 3 and 9 | [§10.2](../01_blocks/02_part_i_path.md#10-2-path-versus-chronology) | comparison §§10.11–10.12 |
| components | Chapter 9 transition records | [§10.3](../01_blocks/02_part_i_path.md#10-3-path-components) | branch ontology Chapter 13 |
| selection and loss | Chapters 6–8 | [§10.4](../01_blocks/02_part_i_path.md#10-4-path-selection) | full `COMPOSE` procedure Chapter 15 |
| path frame | Chapter 2 coordinates | [§10.5](../01_blocks/02_part_i_path.md#10-5-path-frame) | boundary audit Chapter 16 |
| path evidence | Chapters 6–7 and Chapter 9 | [§10.6](../01_blocks/02_part_i_path.md#10-6-path-evidence) | full record §10.14 and Chapter 15 |
| six WP1 pressure cases | Chapter 10 Preparation assignments | §§10.1–10.6 | later `03_cases/*` production |

WP1 supplies bounded path-threshold and evidence findings. It does not supply a trajectory, dependence result, or operation occurrence.

---

## Chapter 10 WP2 Canonical Route

| WP2 concept | Dependency return | Canonical route | Protected later owner |
| --- | --- | --- | --- |
| realized path and open endpoint | Chapter 10 §§10.1–10.6 | [§10.7](../01_blocks/02_part_i_path.md#10-7-realized-path) | trajectory Chapter 11 |
| blocked continuation | Chapter 9 transition/non-event controls and Chapter 10 traversal | [§10.8](../01_blocks/02_part_i_path.md#10-8-blocked-path) | branch ontology/source discipline Chapter 13 |
| aborted path and residue | Chapter 9 transition/failure and Chapter 10 path components | [§10.9](../01_blocks/02_part_i_path.md#10-9-aborted-path) | sedimentation Chapter 11; dependence Chapter 12 |
| deferred continuation | Chapter 9 delay and Chapter 10 path frame | [§10.10](../01_blocks/02_part_i_path.md#10-10-deferred-path) | alternatives Chapter 13 |
| status lineage and Path Identity | Chapter 10 §10.5 | [WP2 completion boundary](../01_blocks/02_part_i_path.md#10-10-deferred-path) | full record §§10.14 and Chapter 7 |

Sections 10.11–10.14 remain pending.

---

## Chapter 10 WP3 Cross-References

| Chapter-10 site | Governing dependency | Forward handoff |
| --- | --- | --- |
| [§10.11 Path Comparison](../01_blocks/02_part_i_path.md#10-11-path-comparison) | Chapter 2 coordinates; Chapter 6 non-compensatory admissibility | Chapter 13 alternatives; Chapter 17 comparison cases |
| [§10.12 Similar End States](../01_blocks/02_part_i_path.md#10-12-similar-end-states-different-paths) | Chapter 9 residue and bounded irreversibility | Chapter 11 historical load; Chapter 12 dependence |
| [§10.13 Path without Strong Dependence](../01_blocks/02_part_i_path.md#10-13-path-without-strong-dependence) | Chapter 0 claim boundary; Chapter 6 counterfactual sensitivity | Chapter 12 full dependence test |
| [§10.14 Minimal Path Record](../01_blocks/02_part_i_path.md#10-14-minimal-path-record) | Chapter 7 Shared Transformation Record | Chapter 11 trajectory input; Chapter 15 `COMPOSE` occurrence test |


## Chapter 10 Provisional-Lock Cross-References

- Primary Path definition and integrated lock: [`Chapter 10`](../01_blocks/02_part_i_path.md#chapter-10-path).
- Actual traversal, components, selection, frame, and evidence: [§§10.1–10.6](../01_blocks/02_part_i_path.md#10-1-definition-of-path).
- Realized, blocked, aborted, and deferred status: [§§10.7–10.10](../01_blocks/02_part_i_path.md#10-7-realized-path).
- Comparison, endpoints, non-dependence, Minimal Record, Stop, and Non-Capture: [§§10.11–10.14](../01_blocks/02_part_i_path.md#10-11-path-comparison).
- Integrated Chapter 11 handoff and no-erasure boundary: [`Chapter 10 completion boundary`](../01_blocks/02_part_i_path.md#chapter-10-completion-boundary).
- Upstream transition burden: [`Chapter 9`](../01_blocks/02_part_i_path.md#chapter-9-temporal-order-and-transition).
- Later full formation procedure: [`Chapter 15 contract`](../05_minified/Chapter_Contracts.md#chapter-15-compose-selection-formation-and-compression).

Chapter 10 does not inherit Trajectory, Path Dependence, `COMPOSE`, target-function, causal, normative, or authority passage.

---

## Chapter 11 Preparation Route

| Chapter 11 duty | Primary upstream owner | Protected downstream owner |
| --- | --- | --- |
| Path substrate and anti-laundering | [Chapter 10 completion boundary](../01_blocks/02_part_i_path.md#chapter-10-completion-boundary) | Chapter 11 may formulate only a new, independently tested Trajectory claim |
| Trajectory object distinction | [Chapter 3 temporal object chain](../01_blocks/01_foundations.md#38-trajectory) and [Chapter 8 §8.6–8.7](../01_blocks/01_foundations.md#86-path-is-not-trajectory) | Chapter 12 dependence remains separate |
| operator profile material | `PMS.yaml` and [Operator Index](Operator_Index.md) | no operator fusion or new primitive |
| frame, level, scope, boundary | Chapter 2 | competing periodizations remain testable |
| continuity and historical load | Chapters 5–6 | no score or compensation |
| Shared Record, loss, alternatives, governance | Chapter 7 | Minimal Trajectory Record remains a view |
| complete `COMPOSE` mechanics | Chapter 15 | not duplicated in Chapter 11 |
| target functions | RETYPE Chapters 31–33 | not assigned in Chapter 11 |

Production control: [`Chapter 11 Preparation Record`](Chapter_11_Preparation_Record.md).

## Chapter 11 WP1 Canonical Cross-Reference Route

| WP1 object or duty | Canonical owner | Required return / protected owner |
| --- | --- | --- |
| Trajectory operational definition | [§11.1](../01_blocks/02_part_i_path.md#11-1-definition-of-trajectory) | Foundations §3.8 remains foundational source |
| Path-to-Trajectory threshold | [§11.2](../01_blocks/02_part_i_path.md#11-2-from-path-to-trajectory) | Chapter 10 supplies Path; Chapter 12 retains dependence test |
| Historical Sedimentation | [§11.3](../01_blocks/02_part_i_path.md#11-3-historical-sedimentation) | Chapter 3 supplies foundational property; WP2 supplies profile-specific elaboration |
| non-teleological directionality | [§11.4](../01_blocks/02_part_i_path.md#11-4-directionality-without-teleology) | Chapter 12 may later test dependence, not purpose |
| six WP1 pressure cases | [§§11.1–11.4](../01_blocks/02_part_i_path.md#11-trajectory) | `03_cases/*` production remains later |
| WP1 execution history | [`Chapter_11_Preparation_Record.md`](Chapter_11_Preparation_Record.md#20-wp1-execution-record) | Reference record has no independent theory authority |
| model mirror | `07_model/Admissibility_Rules.yaml#chapter_11_wp1_trajectory_handoff` | field validity does not decide substantive sufficiency |

WP2 is now canonical; the next route is Chapter 11 WP3, Sections 11.10–11.14.

## Chapter 11 WP2 Canonical Cross-Reference Route

| WP2 object or duty | Canonical owner | Required return / protected owner |
| --- | --- | --- |
| Attractor Sedimentation | [§11.5](../01_blocks/02_part_i_path.md#11-5-attractor-sedimentation) | PMS `Α` and `Θ` remain separate operator types; RETYPE retains attractor-function |
| Asymmetry Accumulation | [§11.6](../01_blocks/02_part_i_path.md#11-6-asymmetry-accumulation) | PMS `Ω` remains Base operator; no legitimacy or person claim |
| Binding Accumulation | [§11.7](../01_blocks/02_part_i_path.md#11-7-binding-accumulation) | PMS `Ψ` remains Base operator; no moral-duty or consent inference |
| Residual Accumulation | [§11.8](../01_blocks/02_part_i_path.md#11-8-residual-accumulation) | Chapter 14 retains complete Non-Event procedure; missing information remains distinct |
| Changed Action Corridors | [§11.9](../01_blocks/02_part_i_path.md#11-9-changed-action-corridors) | Chapter 12 retains dependence test; no prediction or recommendation |
| five WP2 pressure cases | [§§11.5–11.9](../01_blocks/02_part_i_path.md#11-5-attractor-sedimentation) | `03_cases/*` production remains later |
| WP2 execution history | [`Chapter_11_Preparation_Record.md`](Chapter_11_Preparation_Record.md#21-wp2-execution-record) | Reference record has no independent theory authority |
| model mirror | `07_model/Admissibility_Rules.yaml#chapter_11_wp2_profile_and_corridor_handoff` | field validity does not decide substantive accumulation or corridor truth |

Next canonical route: Chapter 11 WP3, Sections 11.10–11.14.

## Chapter 11 WP3 Canonical Cross-Reference Route

| WP3 object or duty | Canonical owner | Required return / protected owner |
| --- | --- | --- |
| Trajectory Boundary and periodization | [§11.10](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary) | Chapter 2 retains frame, granularity, level, temporal/source/claim scope; Chapter 10 retains Path identity |
| segment lineage and open continuation | [§11.10](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary) | Chapter 9 retains transition and bounded-irreversibility definitions; Chapter 12 retains dependence test |
| Trajectory Compression and Loss | [§11.11](../01_blocks/02_part_i_path.md#11-11-trajectory-compression) | Chapter 7 retains canonical Loss; Chapter 15 retains full `COMPOSE` mechanics |
| competing constructions | [§11.12](../01_blocks/02_part_i_path.md#11-12-competing-trajectory-constructions) | Chapter 6 retains admissibility; Chapter 51–52 retain Stop and Non-Capture general theory |
| False Trajectory | [§11.13](../01_blocks/02_part_i_path.md#11-13-false-trajectory) | Output Class inventory remains closed; weaker findings and no-erasure lineage remain preserved |
| Minimal Trajectory Record | [§11.14](../01_blocks/02_part_i_path.md#11-14-minimal-trajectory-record) | Chapter 7 remains Shared Record owner; no schema expansion authorized |
| Chapter-12 handoff | [§11.14](../01_blocks/02_part_i_path.md#chapter-12-handoff) | Chapter 12 tests Path Dependence separately; RETYPE retains target functions |

WP3 completes canonical Sections 11.1–11.14 but not Chapter-11 Provisional Lock. The next route is WP4 integrated synchronization and audit.

## Chapter 11 Provisional-Lock Cross-References

| Chapter 11 result | Canonical return | Protected later owner |
| --- | --- | --- |
| Trajectory threshold and Historical Sedimentation | [§§11.1–11.3](../01_blocks/02_part_i_path.md#11-1-definition-of-trajectory) | Chapter 12 tests dependence separately |
| directionality without teleology | [§11.4](../01_blocks/02_part_i_path.md#11-4-directionality-without-teleology) | no purpose, destiny, or prediction handoff |
| occurrence-level accumulation profiles | [§§11.5–11.8](../01_blocks/02_part_i_path.md#11-5-attractor-sedimentation) | Appendix J stress tests; Chapter 12 dependence |
| Changed Action Corridors | [§11.9](../01_blocks/02_part_i_path.md#11-9-changed-action-corridors) | no RETYPE target function or recommendation |
| Boundary, Compression, and competing constructions | [§§11.10–11.12](../01_blocks/02_part_i_path.md#11-10-trajectory-boundary) | Chapter 15 retains full `COMPOSE` mechanics |
| False Trajectory and Minimal Record | [§§11.13–11.14](../01_blocks/02_part_i_path.md#11-13-false-trajectory) | Shared Record remains owner; stronger failed use triggers Stop |
| Chapter completion and handoff | [Chapter 11 completion boundary](../01_blocks/02_part_i_path.md#chapter-11-completion-boundary) | Chapter 12 Preparation |

```text
Chapter 11 provisional lock
→ Chapter 12 Preparation

Trajectory object
≠ Path Dependence property
```


---

## Chapter 12 Preparation Cross-References

```text
Chapter 10 warranted Path
→ Chapter 11 warranted Trajectory
→ Chapter 12 graded Path-Dependence property test
```

| Route | Handoff | Non-inheritance boundary |
| --- | --- | --- |
| Chapter 3 → Chapter 12 | foundational property/object and weak/strong distinctions | no re-derivation of the temporal-object chain |
| Chapter 6 → Chapter 12 | Counterfactual Sensitivity, Source/Claim Ceiling, Stop, Non-Capture | no universal score or automatic semantic decision |
| Chapter 11 → Chapter 12 | Trajectory reference, sedimentation carriers, profiles, corridors, boundary, rivals, Loss | Trajectory does not pre-confirm dependence |
| Chapter 12 → Chapter 13 | bounded dependence result and only minimum alternative-history pressure | detailed branch taxonomy and availability remain Chapter 13-owned |
| Chapter 12 → Chapter 15 | dependence claim as possible composition claim content | full `COMPOSE` occurrence remains separately tested |
| Chapter 12 → Chapter 24 | dependence-bearing occurrences/composites eligible for later decomposition | fine resolution cannot retroactively prove the property |
| Chapter 12 → Chapter 46 | local counterfactual burden and unresolved questions | system-wide Counterfactual Sensitivity remains later-owned |
| Chapter 12 → RETYPE | source history and dependence may become trace material | target-function validity remains a separate `PROJECT_AS` claim |
| Chapter 12 → LIMITS | local Failure, Stop, Non-Capture, anti-laundering lineage | no authority inheritance or final global audit |

```text
later operation or projection success
≠ retroactive repair of a failed dependence claim
```

Production control: [`Chapter 12 Preparation Record`](Chapter_12_Preparation_Record.md).

## Chapter 12 WP1 Cross-Reference Handoff

```text
Chapter 10 warranted Path
→ Chapter 11 warranted Trajectory
→ Chapter 12 WP1 graded Path-Dependence property test
→ Chapter 12 WP2 dependence-bearing operator profiles
```

Protected later owners:

- Chapter 13: detailed branch and unavailable-alternative taxonomy;
- Chapter 15: complete `COMPOSE` procedure;
- Chapter 24: `DECOMPOSE` analysis of dependence-bearing occurrences/composites;
- Chapter 46: general Counterfactual-Sensitivity architecture;
- RETYPE: contextual target-function assignment.

A later successful operation or projection does not retroactively repair a failed Path, Trajectory, or dependence claim.

## Chapter 12 WP2 Cross-Reference Handoff

| Route | Ownership relation |
| --- | --- |
| Chapter 11 §§11.5–11.8 → Chapter 12 §§12.4–12.7 | sedimentation profile supplies possible historical carrier; Chapter 12 separately tests historical indispensability |
| Chapter 12 §12.3 → §§12.4–12.7 | strong property threshold governs every profile; no profile bypasses current-state sufficiency |
| Chapter 12 §§12.4–12.7 → WP3 | profile-specific support hands off to the complete Historical-Omission, Alternative-History, modifier, failure, Stop, and Non-Capture architecture |
| Chapter 13 | retains branch, lost-alternative, and counterfactual-path taxonomy |
| Chapter 15 | retains complete `COMPOSE` selection and formation procedure |
| Chapter 24 | retains later `DECOMPOSE` analysis of dependence-bearing occurrences and composites |
| Chapter 46 | retains general Counterfactual-Sensitivity architecture |
| RETYPE | retains every target-function assignment |

No downstream route retroactively repairs a failed profile or Path-Dependence claim.

## Chapter 12 WP3 Cross-Reference Handoff

| Route | Ownership relation |
| --- | --- |
| Chapter 11 → Chapter 12 | Trajectory and historical carriers are eligible inputs, not inherited dependence conclusions |
| Chapter 12 §§12.8–12.10 | tests recontextualization, later modifiers, and non-determinism without target-function assignment |
| Chapter 12 §12.11 | owns the local property test and minimum source-bounded comparison architecture |
| Chapter 12 §12.12 | owns failure, reduction, resolution neutrality, Stop, Non-Capture, and re-entry for the property claim |
| Chapter 13 | owns detailed branches, availability windows, and lost-alternative taxonomy |
| Chapter 15 | owns complete `COMPOSE` formation and compression mechanics |
| Chapter 24 | owns later `DECOMPOSE` analysis of dependence-bearing carriers |
| Chapter 46 | owns system-wide Counterfactual Sensitivity |
| RETYPE | owns every contextual target-function assignment |

No downstream success retroactively repairs an upstream failed dependence claim.

## Chapter 12 Provisional-Lock Cross-References

- Property/object distinction and graded findings: [`§§12.1–12.3`](../01_blocks/02_part_i_path.md#12-1-path-dependence-as-a-property)
- Dependence-bearing profiles: [`§§12.4–12.7`](../01_blocks/02_part_i_path.md#12-4-a-theta-attractor-dependence)
- Recontextualization, modifiers, non-determinism, test, Failure, Stop, and Non-Capture: [`§§12.8–12.12`](../01_blocks/02_part_i_path.md#12-8-phi-under-path-dependence)
- Integrated lock and Chapter-13 handoff: [`Chapter 12 completion boundary`](../01_blocks/02_part_i_path.md#chapter-12-completion-boundary)
- Production history: [`Chapter 12 Preparation Record — WP4`](Chapter_12_Preparation_Record.md#25-wp4-execution-and-provisional-lock-record)
- Chapter-13 contract: [`Chapter 13`](../05_minified/Chapter_Contracts.md#chapter-13--branches-aborts-delays-and-unavailable-alternatives)

---

## Chapter 13 Preparation Cross-References

| Route | Input | Chapter-13 duty | Protected handoff |
| --- | --- | --- | --- |
| Chapter 10 → 13 | Path and minimum branch markers | full branch/status and availability discipline | do not redefine Path |
| Chapter 11 → 13 | Trajectory, corridor, compression, competing constructions | inspect retained/lost alternatives | no automatic branch proof |
| Chapter 12 → 13 | bounded source-variation and dependence pressure | establish actual branch point, window, status, and later reachability | no inherited classification |
| Chapter 13 → 14 | non-selection and delay candidates | Chapter 14 supplies full Non-Event burden | do not exhaust `Λ` here |
| Chapter 13 → 15 | selected, rejected, blocked, aborted, deferred, and lost alternatives | Chapter 15 audits `COMPOSE` selection/compression/Loss | no completed operation inheritance |
| Chapter 13 → 46 | bounded counterfactual Path examples | Chapter 46 owns general Counterfactual Sensitivity | no duplicated theory |

Production control: [`Chapter 13 Preparation Record`](Chapter_13_Preparation_Record.md). Canonical prose anchor remains pending until WP1.

## Chapter 13 WP1 Cross-References

- Canonical prose: [`§§13.1–13.4`](../01_blocks/02_part_i_path.md#13-branches-aborts-delays-and-unavailable-alternatives)
- Production control: [`Chapter_13_Preparation_Record.md`](Chapter_13_Preparation_Record.md)
- Predecessors: Chapter 10 Path; Chapter 11 Trajectory; Chapter 12 Path Dependence
- Protected successors: Chapter 14 Non-Events; Chapter 15 `COMPOSE`; Chapter 46 Counterfactual Sensitivity; RETYPE
- Cases represented: `C13-ALT-01`, `C13-BRANCH-01`, `C13-REAL-01`, `C13-REJ-01`, `C13-SOURCE-01`.

## Chapter 13 WP2 Cross-References

| Route | Handoff | Boundary |
| --- | --- | --- |
| Chapter 10 → Chapter 13 WP2 | earlier blocked/aborted/deferred Path overview | Chapter 13 owns source-bounded status classification and later-reachability burden |
| Chapter 13 WP1 → WP2 | historical alternative field, Branch Point, Realized and Rejected status | WP2 adds Blocked, Aborted, Deferred, and Lost without retroactive reclassification |
| Chapter 13 WP2 → Chapter 14 | delay, non-decision, missed transition, or absent approval candidates | Chapter 14 owns full expectation-grounded `Λ` analysis |
| Chapter 13 WP2 → Chapter 15 | differentiated alternative statuses and five-part representation Loss | Chapter 15 owns completed `COMPOSE` selection/compression mechanics |
| Chapter 13 WP2 → WP3 | status-bearing alternatives and unresolved distinctions | WP3 owns counterfactual, non-selection, compression, record, failure, Stop, and Non-Capture architecture |

Canonical route: [Chapter 13 WP2](../01_blocks/02_part_i_path.md#13-5-blocked-branch).

## Chapter 13 WP3 Cross-References

| Route | What WP3 supplies | Protected owner / non-inheritance |
| --- | --- | --- |
| Chapter 13 WP1–WP2 → WP3 | source-supported alternative field and differentiated branch statuses | no unrealized outcome inherited |
| Chapter 13 WP3 → Chapter 14 | bounded Non-Selection candidates and decision-window structure | Chapter 14 owns expectation-grounded `Λ` determination |
| Chapter 13 WP3 → Chapter 15 | branch field, compression declaration, canonical Loss, Alternative Status Record entries | Chapter 15 owns completed `COMPOSE` procedure and result |
| Chapter 13 WP3 → Chapter 46 | source-bounded historical counterfactual examples | Chapter 46 owns general Counterfactual Sensitivity |
| Chapter 13 WP3 → RETYPE | possible later source material | no target function or `PROJECT_AS` authorization inherited |
| Chapter 13 WP3 → Reader | status-bearing, uncertainty-bearing graph inputs | visualization may not establish historical status or upgrade claims |

Schema route: the Alternative Status Record uses `Transformation_Record.schema.json`'s existing `extensions` carrier; the top-level rival-transformation `alternatives` field remains semantically separate.

## Chapter 13 Provisional-Lock Cross-References

| Handoff | Supplied | Not inherited |
| --- | --- | --- |
| Chapter 13 → Chapter 14 | active decision contexts, expected windows, Non-Selection candidates, delay and residual traces | automatic `Λ` typing |
| Chapter 13 → Chapter 15 | source-supported alternative field, status declarations, compression and five-part Loss | completed `COMPOSE` or target object |
| Chapter 13 → Chapter 16 | lower/upper alternative-space boundary pressure | final PATH boundary result |
| Chapter 13 → Chapter 17 | nineteen chapter-level Pressure Cases and audit duties | produced case artifacts or empirical findings |
| Chapter 13 → Chapter 46 | bounded historical counterfactual examples and horizon discipline | general Counterfactual-Sensitivity theory |
| Chapter 13 → RETYPE | possible later source material | `PROJECT_AS` authorization or target function |
| Chapter 13 → Reader | status-, source-, uncertainty-, and Loss-bearing graph inputs | historical status, counterfactual truth, or claim upgrade |

Canonical return: [`Chapter 13 completion boundary`](../01_blocks/02_part_i_path.md#chapter-13-completion-boundary).

## Chapter 14 Preparation Cross-References

| Chapter-14 preparation object | Upstream control | Later owner or use |
| --- | --- | --- |
| PATH-specific Non-Event | Chapter 3 foundational definition; Chapters 0/2/6 source, frame, and claim controls | Chapter 15 `COMPOSE`; Chapter 17 PATH audit |
| expectation relation/frame/window | Chapters 2 and 3 | Chapter 14 canonical §§14.1–14.3 |
| Delay / Non-Decision candidates | Chapters 9, 10, and 13 | Chapter 14 canonical §§14.3–14.4 |
| Blocked Responsibility | Chapter 0 authority boundary; Chapter 13 blocking distinction | Chapter 14 §14.5 |
| Missing Repair / Missing Exit | Chapters 3, 10, 11, 13 | Chapter 14 §§14.6–14.7 |
| Non-Event Sedimentation | Chapter 11 Trajectory; Chapter 12 `Λ + Θ` profile | Chapter 14 §14.8; Chapter 15 composition |
| preservation of `Λ` | Chapter 7 Shared Record and Loss | Chapter 15 `COMPOSE` |
| internal event/Non-Event structure | Chapter 14 preserves higher-level character | Chapter 23 `DECOMPOSE` |
| missing-source distinction | Chapter 3 minimum; Chapter 49 full source limits | Chapter 14 source gate |
| Minimal Non-Event Record | Chapter 7 record architecture | Chapter 14 WP3 model decision |
| contextual function | origin type remains `Λ` occurrence/composite | RETYPE `PROJECT_AS` only |

Preparation control: [`Chapter_14_Preparation_Record.md`](Chapter_14_Preparation_Record.md). Canonical Chapter-14 prose remains pending.

## Chapter 14 WP1 Cross-References

- Canonical prose: [`§§14.1–14.3`](../01_blocks/02_part_i_path.md#14-non-events-within-paths-and-trajectories)
- Production control: [`Chapter_14_Preparation_Record.md`](Chapter_14_Preparation_Record.md)
- Foundational owner: Chapter 3 Non-Event definition
- Immediate predecessor: Chapter 13 historical alternatives and Non-Selection candidates
- Protected successors: Chapter 14 WP2/WP3; Chapter 15 `COMPOSE`; Chapter 23 `DECOMPOSE`; Chapter 49 source limits; RETYPE
- Cases represented: `C14-CENT-01`, `C14-FRAME-01`, `C14-DELAY-01`, `C14-SOURCE-01`.

## Chapter 14 WP2 Cross-References

- Canonical prose: [`§§14.4–14.8`](../01_blocks/02_part_i_path.md#14-4-repeated-non-decision)
- Production control: [`Chapter_14_Preparation_Record.md`](Chapter_14_Preparation_Record.md)
- Foundational owner: Chapter 3 Non-Event object
- Immediate controls: Chapter 11 sedimentation/corridors; Chapter 12 Path Dependence; Chapter 13 branch and Non-Selection distinctions
- Protected successors: Chapter 14 WP3; Chapter 15 `COMPOSE`; Chapter 23 `DECOMPOSE`; Chapter 49 source limits; RETYPE
- Cases represented in WP2: `C14-NDEC-01`, `C14-BRESP-01`, `C14-REPAIR-01`, `C14-EXIT-01`, `C14-SED-01`, `C14-CONF-01`, `C14-CONF-02`.

Canonical Chapter-14 prose is now drafted through Section 14.8; WP3 and WP4 remain pending.

## Chapter 14 WP3 Cross-References

- Canonical prose: [`§§14.9–14.11`](../01_blocks/02_part_i_path.md#14-9-preserving-%CE%BB-in-composition)
- Production control: [`Chapter_14_Preparation_Record.md`](Chapter_14_Preparation_Record.md)
- Foundational owner: Chapter 3 Non-Event object
- Immediate controls: Chapter 7 Shared Record; Chapters 11–13 sedimentation, dependence, alternatives, and Non-Selection
- Protected successors: Chapter 15 `COMPOSE`; Chapter 23 `DECOMPOSE`; Chapter 49 source limits; RETYPE
- Cases represented in WP3: `C14-PRES-01`, `C14-SUBEV-01`, `C14-FALSE-01`, `C14-REC-01`, `C14-REDUCE-01`, `C14-STOP-01`, `C14-NC-01`, `C14-HANDOFF-01`.

Canonical Chapter-14 prose is complete through Section 14.11; WP4 integrated audit and Provisional Lock remain pending.

## Chapter 14 Provisional-Lock Cross-References

| Handoff | Supplied | Not inherited |
| --- | --- | --- |
| Chapter 14 → Chapter 15 | preservable `Λ` structures, positive sub-events, uncertainty, canonical Loss burdens | completed `COMPOSE` or target object |
| Chapter 14 → Chapter 16 | false-Non-Event, lower/upper boundary, compression, graph-gap, and anti-teleology pressure | final PATH boundary result |
| Chapter 14 → Chapter 17 | nineteen chapter-level Pressure Cases and audit duties | produced case artifacts or empirical findings |
| Chapter 14 → Chapter 23 | bounded Non-Event occurrences and higher/lower-level tension | completed `DECOMPOSE` |
| Chapter 14 → Chapter 49 | source-gap and non-realization boundary examples | general source-limit theory |
| Chapter 14 → RETYPE | possible later source material | `PROJECT_AS` authorization or target function |
| Chapter 14 → Reader | expectation-, window-, source-, uncertainty-, sub-event-, sedimentation-, and Loss-bearing graph inputs | `Λ` truth, blame, operation result, or claim upgrade |

Canonical return: [`Chapter 14 completion boundary`](../01_blocks/02_part_i_path.md#chapter-14-completion-boundary).

## Chapter 15 Preparation Cross-References

| Chapter-15 duty | Consumes | Protected downstream owner |
| --- | --- | --- |
| operation identity | Chapter 4; Operation Signatures | no redefinition |
| typed sources and composite | Chapters 1–3, 9–14 | Chapter 16 boundary tests |
| selection/order/frame/formation | Chapters 2, 7, 10–14 | Chapter 17 integrated cases |
| preservation and Loss | Chapter 7; Chapters 11, 13, 14 | Chapter 48 general Loss ontology |
| counterfactual sensitivity | Chapter 6; Chapters 12–13 | no causal or predictive authority |
| COMPOSE Record | Chapter 7; Operation Registry; Record schema | Appendix D template detail |
| later decomposition | composite and declared Loss | Chapter 24 `DECOMPOSE` |
| contextual target function | formed composite | RETYPE / `PROJECT_AS` |

Primary preparation control: [`Chapter_15_Preparation_Record.md`](Chapter_15_Preparation_Record.md).

## Chapter 15 WP1 Cross-References

| WP1 burden | Upstream owner | Canonical WP1 route | Downstream owner |
| --- | --- | --- | --- |
| operation identity | Chapter 4 | [§15 intro and §15.1](../01_blocks/02_part_i_path.md#15-compose-selection-formation-and-compression) | Chapter 15 WP2/WP3 |
| typed temporal sources | Chapters 9–14 | [§15.3](../01_blocks/02_part_i_path.md#15-3-source-objects) | Formation and preservation |
| selection and alternatives | Chapters 10 and 13 | [§15.4](../01_blocks/02_part_i_path.md#15-4-selection-rule) | Sensitivity and competing composition |
| temporal order | Chapters 9–11 | [§15.5](../01_blocks/02_part_i_path.md#15-5-temporal-ordering-rule) | Target formation |
| frame/granularity/level | Chapter 2 | [§15.6](../01_blocks/02_part_i_path.md#15-6-composition-frame) | Chapter 16 boundaries and RETYPE separation |
| Loss | Chapter 7; Chapter 48 | entry burden only | Chapter 15 WP2 |
| target function | RETYPE | prohibited in WP1 | `PROJECT_AS` only |

## Chapter 15 WP2 Cross-References

| Chapter-15 WP2 concern | Upstream owner | Downstream owner |
| --- | --- | --- |
| target-class threshold | Chapters 3 and 9–14 | Chapters 16–17 |
| Formation Rule and constitutive relations | Chapter 15 | Chapter 17 cases; SUB/RETYPE consumers |
| operator load preservation | PMS Base; Chapters 9–14 | Chapter 15 WP3 and Chapter 17 |
| canonical five-part Loss | Chapters 7 and 48 | Chapter 15 WP3; Chapter 16; Appendices |
| compression and external lineage | Chapter 15 consuming Chapter 7 | Chapter 24 `DECOMPOSE` |
| exclusion and rival frames | Chapters 2, 10, 13 | Chapter 16 boundary tests |
| uncertainty and irrecoverability | Chapters 0, 6, 7 | Chapter 15 WP3–WP4; Chapter 17 |
| target function | RETYPE / `PROJECT_AS` | not assigned by Chapter 15 |

Canonical route: [Chapter 15 WP2](../01_blocks/02_part_i_path.md#15-7-formation-rule).

## Chapter 15 WP3 Cross-References

| WP3 concern | Primary owner | Protected downstream owner |
| --- | --- | --- |
| composition claim and target strength | Chapter 15 §15.12 | Chapter 16 boundaries |
| origin-type preservation | Chapter 15 §15.13 | RETYPE / `PROJECT_AS` |
| sensitivity and overelasticity | Chapter 15 §15.14 | Chapter 17 cases |
| failure and reduction | Chapter 15 §15.15 | canonical Output Classes |
| complete COMPOSE record | Chapter 15 §15.16 | Appendix D template |
| non-invertibility | Chapter 24 | not Chapter 15 |
| general Loss ontology | Chapter 48 | not Chapter 15 |

## Chapter 15 Provisional-Lock Cross-References

| Handoff | Supplied | Not inherited |
| --- | --- | --- |
| Chapters 9–14 → Chapter 15 | typed temporal structures, Path/Trajectory/Dependence/branch/Non-Event burdens | automatic composition |
| Chapter 15 → Chapter 16 | complete PATH-specific `COMPOSE` procedure and failure routes | boundary adjudication |
| Chapter 15 → Chapter 17 | nineteen Pressure Cases and integrated audit duties | produced case corpus |
| Chapter 15 → Chapter 24 | compressed composites and Lineage/Loss burdens | automatic inversion or `DECOMPOSE` result |
| Chapter 15 → Chapter 48 | operation-specific five-part Loss use | general Loss-ontology redefinition |
| Chapter 15 → RETYPE | origin-typed composite objects | `PROJECT_AS` authorization or target function |
| Chapter 15 → Reader | source, order, formation, Loss, sensitivity, rival-composition, Stop/Non-Capture overlays | operation truth or authority |

Canonical return: [`Chapter 15 completion boundary`](../01_blocks/02_part_i_path.md#chapter-15-completion-boundary).

## Chapter 16 Preparation Cross-References

| Chapter-16 concern | Primary owner | Protected downstream owner |
| --- | --- | --- |
| general Relevance Floor and Traceability Ceiling | Chapter 6 | Chapters 41–53 integrated LIMITS |
| PATH-local lower and upper boundaries | Chapter 16 | Chapter 17 cases and audit |
| Path, Trajectory, dependence, branches, and Non-Events | Chapters 10–14 | no competitive redefinition here |
| complete `COMPOSE` procedure and Loss | Chapter 15 | Chapter 16 boundary application |
| excessive compression and punctualization | Chapter 16 | Chapter 24 later `DECOMPOSE` |
| PATH/SUB boundary | Chapter 16 | SUB operation chapters |
| PATH/RETYPE boundary | Chapter 16 | RETYPE and `PROJECT_AS` |
| Stop and Non-Capture route | Chapter 16 consuming Chapters 6–8 | Chapter 17 local audit |

Primary preparation control: [`Chapter_16_Preparation_Record.md`](Chapter_16_Preparation_Record.md).

## Chapter 16 WP1 Cross-References

| WP1 burden | Upstream owner | Canonical WP1 route | Downstream owner |
| --- | --- | --- | --- |
| common Admissibility Band | Chapter 6 | [Chapter 16 introduction](../01_blocks/02_part_i_path.md#16-path-boundary-conditions) | LIMITS consolidation |
| lower PATH boundary | Chapter 16 | [§16.1](../01_blocks/02_part_i_path.md#16-1-the-lower-path-boundary) | WP3 Purchase Test |
| chronology/Trajectory separation | Chapters 10–11 | [§16.2](../01_blocks/02_part_i_path.md#16-2-chronology-without-trajectory-gain) | Chapter 17 cases |
| upper PATH boundary | Chapter 16 | [§16.3](../01_blocks/02_part_i_path.md#16-3-the-upper-path-boundary) | WP3 Trace Test |
| Trajectory trace burden | Chapter 11 | [§16.4](../01_blocks/02_part_i_path.md#16-4-trajectory-without-path-trace) | Claim Reduction |
| compression and Loss | Chapters 15 and 48 | [§16.5](../01_blocks/02_part_i_path.md#16-5-excessive-temporal-compression) | WP2 omissions; SUB later |
| same-material Band contrast | Chapter 16 Contract | [`C16-BAND-01`](../01_blocks/02_part_i_path.md#c16-band-01-the-same-broad-materials-across-the-full-path-band) | Chapter 17 audit |
| target function | RETYPE | prohibited in WP1 | `PROJECT_AS` only |

## Chapter 16 WP2 Cross-References

| WP2 burden | Upstream owner | Canonical route | Downstream owner |
| --- | --- | --- | --- |
| bounded directionality | Chapter 11 | [§16.6](../01_blocks/02_part_i_path.md#16-6-artificial-directionality) | WP3 Trace Test; Chapter 17 |
| anti-teleology | Chapter 11 and Chapter 13 alternatives | [§16.7](../01_blocks/02_part_i_path.md#16-7-hidden-teleology) | Chapter 17; LIMITS |
| constitutive `Λ` preservation | Chapter 14 | [§16.8](../01_blocks/02_part_i_path.md#16-8-omitted-non-events) | Chapter 15 Loss; Chapter 17 |
| constitutive `Ω` preservation | Chapters 11–12 | [§16.9](../01_blocks/02_part_i_path.md#16-9-omitted-asymmetries) | Chapter 17; LIMITS |
| PATH/RETYPE boundary | Chapters 4 and 15 | [§16.10](../01_blocks/02_part_i_path.md#16-10-path-versus-retype) | RETYPE `PROJECT_AS` owner |
| PATH/SUB boundary | Chapters 4 and 15 | [§16.11](../01_blocks/02_part_i_path.md#16-11-path-versus-sub) | SUB `DECOMPOSE` owner |
| Stop and Non-Capture | Chapter 6 | deferred to WP3 | Chapter 17 local audit |

## Chapter 16 WP3 Cross-References

- [§16.12 Praxeological Purchase Test](../01_blocks/02_part_i_path.md#16-12-praxeological-purchase-test) consumes Chapter 6 Floor logic and Chapters 9–15 temporal-object controls.
- [§16.13 Traceable Path Test](../01_blocks/02_part_i_path.md#16-13-traceable-path-test) consumes Chapter 6 Ceiling logic, Chapter 7 Shared Record, Chapter 15 Formation/Loss, and Chapter 11 Trajectory thresholds.
- [§16.14 Claim Reduction and PATH Stop Conditions](../01_blocks/02_part_i_path.md#16-14-claim-reduction-and-path-stop-conditions) routes stronger failures without erasing weaker objects and preserves SUB/RETYPE ownership.
- [§16.15 PATH Non-Capture](../01_blocks/02_part_i_path.md#16-15-path-non-capture) supplies Chapter 17 with irreducible-periodization, Stop, and local-audit duties.
- [Chapter 16 Preparation Record — WP3](Chapter_16_Preparation_Record.md#31-wp3-execution-record) records production history only.

## Chapter 16 Provisional-Lock Cross-References

| Locked relation | Primary owner | Return | Next owner |
| --- | --- | --- | --- |
| common Admissibility Band | Chapter 6 | [`Chapter 16 completion boundary`](../01_blocks/02_part_i_path.md#chapter-16-completion-boundary) | LIMITS consolidation |
| PATH lower and upper boundaries | Chapter 16 | [`§§16.1–16.5`](../01_blocks/02_part_i_path.md#16-1-the-lower-path-boundary) | Chapter 17 cases and audit |
| directionality, teleology, omitted `Λ`/`Ω` | Chapter 16 | [`§§16.6–16.11`](../01_blocks/02_part_i_path.md#16-6-artificial-directionality) | Chapter 17 pressure cases |
| Purchase, Trace, reduction, Stop, Non-Capture | Chapter 16 | [`§§16.12–16.15`](../01_blocks/02_part_i_path.md#16-12-praxeological-purchase-test) | Chapter 17 local audit |
| `DECOMPOSE` | SUB | Chapter-16 anti-rescue boundary | Chapter 24 |
| `PROJECT_AS` | RETYPE | Chapter-16 anti-rescue boundary | RETYPE chapters |
| production history | Reference layer | [`Chapter 16 Preparation Record — WP4`](Chapter_16_Preparation_Record.md#32-wp4-execution-and-provisional-lock-record) | no theory ownership |

## Chapter 17 Preparation Cross-References

- Structure: [`Chapter 17`](../00_source/PMS-STRATA_Structure.md#17-path-cases-countercases-and-local-audit)
- Contract: [`Chapter 17`](../05_minified/Chapter_Contracts.md#chapter-17--path-cases-countercases-and-local-audit)
- PATH source block: [`Part I`](../01_blocks/02_part_i_path.md)
- Preparation control: [`Chapter_17_Preparation_Record.md`](Chapter_17_Preparation_Record.md)
- Case templates: [`03_cases/templates`](../03_cases/templates/)
- Case index: [`Case_Index.md`](../03_cases/Case_Index.md) and [`Case_Index.yaml`](../03_cases/Case_Index.yaml)
- Shared Record schema: [`Transformation_Record.schema.json`](../07_model/Transformation_Record.schema.json)
- Canonical outputs: [`Output_Classes.yaml`](../07_model/Output_Classes.yaml)

## Chapter 17 WP1 Cross-References

- Canonical sections: [`§§17.1–17.4`](../01_blocks/02_part_i_path.md#17-path-cases-countercases-and-local-audit)
- Case Index: [`Case_Index.md`](../03_cases/Case_Index.md) and [`Case_Index.yaml`](../03_cases/Case_Index.yaml)
- Simple Linear Path: [`MD`](../03_cases/markdown/C17-LINEAR-01_Simple_Linear_Path.md) · [`YAML`](../03_cases/yaml/C17-LINEAR-01_Simple_Linear_Path.yaml)
- Branching Path: [`MD`](../03_cases/markdown/C17-BRANCH-01_Branching_Path.md) · [`YAML`](../03_cases/yaml/C17-BRANCH-01_Branching_Path.yaml)
- Trajectory with central `Λ`: [`MD`](../03_cases/markdown/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.md) · [`YAML`](../03_cases/yaml/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.yaml)
- Record schema: [`Transformation_Record.schema.json`](../07_model/Transformation_Record.schema.json)
- Next: Chapter 17 WP2 counterpressure and the second lock-critical artifact.

## Chapter 17 WP2-A Cross-References

| Chapter site | Case artifact | Primary pressure |
|---|---|---|
| §17.5 | `C17-HISTORY-01` Markdown/YAML | similar endpoints, different histories, dimension-specific dependence |
| §17.6 | `C17-WEAKPD-01` Markdown/YAML | recurrence, weak dependence, current-state sufficiency |

Both feed the later Chapter-17 PATH Local Audit and remain open to Chapter 24, RETYPE, LIMITS, and corpus-wide audit.

## Chapter 17 WP2-B Cross-References

| Chapter site | Case artifact | Primary pressure |
|---|---|---|
| §17.7 | `C17-CHRON-01` Markdown/YAML | chronology versus Path; Claim Reduction |
| §17.8 | `C17-MACRO-01` Markdown/YAML | macro-label versus traceable load; failed COMPOSE |
| §17.9 | `C17-TEL-01` Markdown/YAML | directionality versus teleology; endpoint-conditioned formation |

All three feed the later PATH Local Audit and remain open to WP2-C, WP3, LIMITS, and corpus-wide audit.


## Chapter 17 WP2-C Cross-References

| Canonical section | Case artifacts | Primary control |
|---|---|---|
| §17.10 | `C17-OMEGA-01` Markdown/YAML | milestone equality versus practical-load equivalence |
| §17.11 | `C17-FALSEL-01` Markdown/YAML | missing information versus structured Non-Event |
| Full WP2 boundary | Case Index | seven WP2 result mappings and WP3 handoff |


## Chapter 17 WP3-A Cross-References

- §17.12 ↔ `C17-PROJ-01` ↔ PATH/RETYPE boundary ↔ Chapter 30 future `PROJECT_AS` owner.
- §17.13 ↔ `C17-RES-01` ↔ Relevance Floor ↔ Chapter 25/27 future SUB resolution controls.
- §17.14 ↔ `C17-ATTR-01` ↔ Trajectory/Attractor non-equivalence ↔ RETYPE Attractor-function owner.
- All three lock-critical artifacts now exist; WP3-B retains the Part-I lock decision.


## Chapter 17 WP3-B Cross-References

- §§17.1–17.14 → thirteen standalone artifacts registered in `03_cases/Case_Index.*`.
- §17.15 → Chapters 6, 7, 15, 16 and the twelve-stage record audits.
- §17.16 → `07_model/Output_Classes.yaml` and `04_reference/Output_Class_Index.md`.
- §17.17 → Chapter 17 Contract completion test and the WP4 Part-I lock gate.
- No Chapter-17 result pre-empts Chapter 18 SUB or later RETYPE target-function tests.

## Part I — PATH Provisional-Lock Cross-References

- Chapters 9–14 → temporal object, dependence, alternatives, and `Λ` source architecture.
- Chapter 15 → `COMPOSE` procedure and complete Loss.
- Chapter 16 → PATH-local Band, reduction, Stop, and Non-Capture.
- Chapter 17 → thirteen case records, Output mapping, Local Audit, and closing statement.
- Part-I lock boundary → Chapter 18 Preparation without pre-authorized `DECOMPOSE`.

## Chapter 18 Preparation Cross-References

- Structure: [`Chapter 18`](../00_source/PMS-STRATA_Structure.md#18-the-provisionally-compressed-object)
- Block Contract: [`Part II — SUB`](../05_minified/Block_Contracts.md#7-03--sub)
- Chapter Contract: [`Chapter 18`](../05_minified/Chapter_Contracts.md#chapter-18--the-provisionally-compressed-object)
- Preparation control: [`Chapter_18_Preparation_Record.md`](Chapter_18_Preparation_Record.md)
- Canonical target block: [`03_part_ii_sub.md`](../01_blocks/03_part_ii_sub.md)
- PATH handoff: [`Part I provisional-lock boundary`](../01_blocks/02_part_i_path.md#part-i--path-provisional-lock-boundary)
- Operation identity: [`DECOMPOSE`](Transformation_Operation_Index.md#7-decompose)
- Record carrier: [`Transformation_Record.schema.json`](../07_model/Transformation_Record.schema.json)

```text
Chapter 18 source declaration
→ Chapter 19 granularity relation
→ Chapter 20 DECOMPOSE procedure
```

Standalone case and test files are deferred until all canonical Blocks are complete and the dedicated Integrated Cases and Audit pass begins.

## Chapter 18 WP1 Cross-References

- Canonical chapter entry: [Chapter 18](../01_blocks/03_part_ii_sub.md#chapter-18-the-provisionally-compressed-object)
- Purpose and source-entry boundary: [§18.1](../01_blocks/03_part_ii_sub.md#18-1-purpose-of-sub)
- Provisional elementarity: [§18.2](../01_blocks/03_part_ii_sub.md#18-2-provisional-elementarity)
- Compressed source object: [§18.3](../01_blocks/03_part_ii_sub.md#18-3-the-compressed-object)
- Operator type / occurrence boundary: [§18.4](../01_blocks/03_part_ii_sub.md#18-4-operator-type-versus-decomposable-occurrence)
- Preparation and execution history: [`Chapter_18_Preparation_Record.md`](Chapter_18_Preparation_Record.md#26-wp1-execution-record)
- Formal non-routing mirror: [`Admissibility_Rules.yaml`](../07_model/Admissibility_Rules.yaml)

Protected handoffs:

```text
Chapter 18 WP1 source candidate
→ Chapter 18 WP2 compression warrant
→ Chapter 18 WP3 preservation and minimal declaration
→ Chapter 19 granularity relation
→ Chapter 20 DECOMPOSE procedure
```

No cross-reference in this route authorizes hidden-component inference, target-granularity selection, operation success, source-function outcome, target function, or authority.



## Chapter 18 WP2 Cross-References

| Canonical site | Consumes | Produces | Protects |
|---|---|---|---|
| [§18.5](../01_blocks/03_part_ii_sub.md#18-5-why-compression-is-necessary) | Chapter 6 Band; Chapter 7 Loss; WP1 compressed source object | necessary-compression baseline | compression ≠ error; compression ≠ `COMPOSE` automatically |
| [§18.6](../01_blocks/03_part_ii_sub.md#18-6-why-compression-can-become-insufficient) | source-candidate architecture; PraxisPurchase; source trace | source-supported insufficiency pressure | available detail ≠ insufficiency; carrier pressure ≠ hidden truth |
| [§18.7](../01_blocks/03_part_ii_sub.md#18-7-reasons-to-decompose) | Counterfactual Sensitivity; source and claim ceilings | six-part decomposition reason | reason ≠ target granularity, components, or result |
| [§18.8](../01_blocks/03_part_ii_sub.md#18-8-reasons-not-to-decompose) | Relevance Floor; source ceiling; operation boundaries | positive bounded no-decomposition decision | no-decomposition ≠ `resolution_neutral` or permanent closure |

Handoff remains:

```text
WP2 reason/no-reason decision
→ WP3 preservation, source declaration, Stop, Non-Capture
→ Chapter 19 granularity relation
→ Chapter 20 operation procedure
```


## Chapter 18 WP3 Handoff Map

```text
Chapter 18
source reference, typing, coordinates, current function,
known/unresolved structure, reason, Loss, Stop, Non-Capture

→ Chapter 19
target-granularity relation, added distinctions,
Frame preservation/change, component/fragment comparability

→ Chapter 20
DECOMPOSE question, components, relations, temporality,
source support, source-function effect, Loss, result
```

No arrow denotes inherited admissibility, truth, target function, or authority. Chapter 18 WP3 completes canonical source-entry prose; the separate WP4 audit owns provisional Chapter-18 lock and Chapter-19 preparation.


## Chapter 18 Provisional-Lock Cross-Reference

```text
Chapter 1 object model
+ Chapter 2 source coordinates
+ Chapter 4 DECOMPOSE identity
+ Chapter 6 Admissibility Band
+ Chapter 7 Shared Record
+ PATH source objects and Loss
→ Chapter 18 provisionally locked source-entry architecture
→ Chapter 19 Preparation Gate and granularity relation
→ Chapter 20 DECOMPOSE procedure
```

Protected later owners: Chapter 25 resolution outcomes, RETYPE target functions, LIMITS integrated boundaries, Integrated Cases and Audit, Appendices, Reference Freeze, Model Finalization, and Reader.

## Chapter 19 Preparation Cross-References

- Governing Contract: [`Chapter_Contracts.md`](../05_minified/Chapter_Contracts.md#chapter-19--granularity-change-and-the-logic-of-decomposition)
- Source-object handoff: [`Chapter 18 completion boundary`](../01_blocks/03_part_ii_sub.md#chapter-18-completion-boundary)
- Preparation control: [`Chapter_19_Preparation_Record.md`](Chapter_19_Preparation_Record.md)
- General coordinate owner: [`Chapter 2`](../01_blocks/01_foundations.md#chapter-2-frame-granularity-and-relative-level)
- Operation owner: Chapter 20, canonical prose pending
- Resolution owner: Chapter 25, canonical prose pending

```text
Chapter 18 provisional lock
→ Chapter 19 Preparation Gate complete
→ Chapter 19 WP1
→ Chapter 20 Preparation and procedure
```

## Chapter 19 WP1 Canonical Cross-References

- Chapter opening and granularity relation: [`Chapter 19`](../01_blocks/03_part_ii_sub.md#chapter-19-granularity-change-and-the-logic-of-decomposition)
- Granularity change and anti-truth descent: [`§19.1`](../01_blocks/03_part_ii_sub.md#19-1-granularity-change)
- Relative downward movement and level separation: [`§19.2`](../01_blocks/03_part_ii_sub.md#19-2-relative-downward-movement)
- Stable-Frame positive case: [`§19.3`](../01_blocks/03_part_ii_sub.md#19-3-stable-frame-finer-granularity)
- Changed-Frame contrast and operation boundary: [`§19.4`](../01_blocks/03_part_ii_sub.md#19-4-changed-frame-during-decomposition)
- Production history: [`Chapter 19 WP1 Execution Record`](Chapter_19_Preparation_Record.md#26-wp1-execution-record)

```text
Chapter 18 provisional lock
→ Chapter 19 Preparation Gate complete
→ Chapter 19 WP1 canonical
→ Chapter 19 WP2
→ Chapter 20 procedure later
```

Protected later owners remain WP2 component architecture, WP3 comparability and Minimal Granularity Relation, Chapter 20 operation procedure, Chapter 25 resolution classification, Chapter 26 complete SUB/RETYPE boundary, and LIMITS integration.

## Chapter 19 WP2 Canonical Cross-References

- Change of Distinction Set: [`§19.5`](../01_blocks/03_part_ii_sub.md#19-5-change-of-distinction-set)
- Local versus Distributed Structure: [`§19.6`](../01_blocks/03_part_ii_sub.md#19-6-local-versus-distributed-structure)
- Functional Parts versus Mere Fragments: [`§19.7`](../01_blocks/03_part_ii_sub.md#19-7-functional-parts-versus-mere-fragments)
- Production history: [`Chapter 19 WP2 Execution Record`](Chapter_19_Preparation_Record.md#27-wp2-execution-record)

```text
Chapter 19 WP1 canonical
→ Chapter 19 WP2 canonical
→ Chapter 19 WP3
→ Chapter 20 procedure later
```

Protected later owners remain WP3 comparability and Minimal Granularity Relation, Chapter 20 actual component/relation reconstruction, Chapter 23 Counterfactual Component Tests, Chapter 25 resolution classification, Chapter 26 complete SUB/RETYPE boundary, and LIMITS integration.

## Chapter 19 WP3 Cross-Reference Return

| Canonical site | Consumes | Supplies | Withholds |
| --- | --- | --- | --- |
| [§19.8](../01_blocks/03_part_ii_sub.md#19-8-granularity-comparability) | Chapter 2 coordinate comparison; Chapters 18–19 source/granularity declarations | local comparability basis, translation, partial comparison, positive incomparability | semantic ranking, identity, global enum |
| [§19.9](../01_blocks/03_part_ii_sub.md#19-9-granularity-mismatch) | predicate, Frame, reference, temporal, and source alignment | mismatch/compatible-predicate/substantive-contradiction separation | automatic contradiction resolution or Output Class |
| [§19.10](../01_blocks/03_part_ii_sub.md#19-10-the-lower-granularity-question) | Admissibility Band and component-candidate burden | pre-operation relevance question, Optional/Mandatory Stop, Non-Capture | Chapter-25 resolution classification |
| [§19.11](../01_blocks/03_part_ii_sub.md#19-11-minimal-granularity-relation) | Chapter-18 source declaration and Shared Record carriers | exact eight-field relation, record mapping, Chapter-20 handoff | component discovery, DECOMPOSE result, schema replacement |


## Chapter 19 Provisional-Lock Cross-Reference

```text
Chapter 2 analytical coordinates
+ Chapter 18 source-entry architecture
+ Chapter 4 DECOMPOSE identity
+ Chapter 6 Admissibility Band
+ Chapter 7 Shared Record
→ Chapter 19 provisionally locked granularity-relation architecture
→ Chapter 20 Preparation Gate and procedure
→ Chapter 25 resolution classification
→ Chapter 26 boundary adjudication
```

Protected later owners remain Chapter 20 operation procedure, Chapter 23 Counterfactual Component Tests, Chapter 25 resolution outcomes, Chapter 26 SUB/RETYPE and new-PATH boundary, LIMITS, Integrated Cases and Audit, Appendices, Reference Freeze, Model Finalization, and Reader.

## Chapter 20 Preparation Cross-Reference Route

```text
Chapter 18 — source entry
→ Chapter 19 — granularity relation
→ Chapter 20 — generic DECOMPOSE procedure
→ Chapters 21–24 — source-family applications
→ Chapter 25 — resolution outcomes
→ Chapter 26 — SUB/RETYPE/new-PATH boundaries
→ Chapter 27 — full SUB limits
→ Chapter 28 — cases and Local Audit
```

Primary production control: [`Chapter_20_Preparation_Record.md`](Chapter_20_Preparation_Record.md). Canonical procedure will reside in [`01_blocks/03_part_ii_sub.md`](../01_blocks/03_part_ii_sub.md#chapter-20-decompose-conditions-procedure-and-preservation-requirements) after drafting.

## Chapter 20 WP1 Cross-Reference Return

| Canonical site | Consumes | Supplies | Withholds |
| --- | --- | --- | --- |
| [§20.1](../01_blocks/03_part_ii_sub.md#20-1-definition) | Chapter 4 identity; Chapters 18–19 handoffs | complete relational operation definition and confusion boundaries | source support, components, relations, result |
| [§20.2](../01_blocks/03_part_ii_sub.md#20-2-preconditions) | Admissibility Band; source and granularity declarations | conjunctive entry screen and pre-operation Stop | operation success or class |
| [§20.3](../01_blocks/03_part_ii_sub.md#20-3-source-object) | Chapter-18 Minimal Source Declaration | independent source identity and function-under-test burden | source-function disposition |
| [§20.4](../01_blocks/03_part_ii_sub.md#20-4-decomposition-question) | Chapter-19 target proposal; source route | six-burden leading-question architecture | expected-difference, support, components, outputs |

## Chapter 20 WP2 Cross-Reference Return

| Canonical site | Upstream dependency | Downstream owner protected |
| --- | --- | --- |
| §20.5 Expected Additional Difference | Chapter 19 Lower Granularity Question; §20.4 question | Chapter 25 resolution taxonomy |
| §20.6 Source Support | Chapter 18 Source Scope; Claim/Source Ceiling | Chapters 21–24 family-specific evidence |
| §20.7 Component Identification | Chapter 19 candidate/fragment logic | Chapter 27 complete component test |
| §20.8 Relation Identification | PATH temporal distinctions; same-source identity | Chapter 26 operation-boundary adjudication |

WP2 supplies reconstruction burdens to WP3 without selecting source-function effect, operation result, or canonical Output Class.

## Chapter 20 WP3 Cross-Reference Return

| Chapter-20 site | Upstream dependency | Downstream handoff |
| --- | --- | --- |
| §20.9 Source-function effect | Chapters 18 and 5 preservation/function distinction | Chapters 21–24 family-specific tests |
| §20.10 Output mapping | Chapter 7 Shared Record; canonical Output Classes | Chapter 25 full resolution taxonomy; Chapter 28 Local Audit |
| §20.11 Non-invertibility | Chapter 4 operation grammar; PATH Loss | Chapter 26 operation-chain boundaries |
| §20.12 Failure/Stop/Non-Capture | Chapter 6 Admissibility Band | Chapter 27 complete SUB limits |
| §20.13 DECOMPOSE Record | Chapter 7 Shared Record; Chapters 18–19 handoff | Chapter 21 occurrence-family application |

WP3 completed canonical Chapter-20 prose; the integrated WP4 audit now provisionally locks the chapter and hands family-specific application to Chapter 21.

## Chapter 20 WP4 Provisional-Lock Route

| Locked Chapter-20 element | Upstream dependency | Downstream owner |
|---|---|---|
| source and decomposition question | Chapters 18–19; Chapter 4 | Chapters 21–24 family applications |
| component and relation reconstruction | Chapter 19 candidate criteria | Chapter 23/24 object-family stress |
| source-function and result axes | Chapters 6–7 | Chapter 25 full resolution taxonomy |
| non-invertibility and operation confusion | Chapter 4 and PATH Loss | Chapter 26 complete boundary adjudication |
| Failure, Stop, Non-Capture, Loss | Chapters 6–7 | Chapters 27–28 limits and Local Audit |
| operation-specific Record | Chapter 7 Shared Record | Appendix E and integrated cases later |

Next route: [Chapter-21 handoff](../01_blocks/03_part_ii_sub.md#chapter-20-completion-boundary).

## Chapter 21 Preparation Route

| Chapter-21 family | Upstream owner | Downstream boundary |
|---|---|---|
| general occurrence rule and Frame family | Chapters 1 and 20 | Chapter 22 composite hierarchy |
| Attractor occurrence and dynamic cycle | Chapters 3, 12, and 20 | RETYPE target-function ownership |
| distributed Asymmetry occurrence | Chapters 2, 19, and 20 | separate COMPOSE/PROJECT_AS where required |
| Impulse and Binding occurrences | PMS Base and Chapter 20 | no psychology or person property |
| failure/Stop/Non-Capture | Chapters 6 and 20 | Chapter 27 complete SUB limits |

Next route: [Chapter 21 Preparation Record](Chapter_21_Preparation_Record.md).

## Chapter 21 WP1 Canonical Route

```text
Chapter 20 generic DECOMPOSE lock
→ Chapter 21 Preparation Gate
→ §§21.1–21.4 operator-occurrence boundary and Frame family
→ WP2 §§21.5–21.9 Attractor and Asymmetry families
```

Primary anchor: [Chapter 21](../01_blocks/03_part_ii_sub.md#chapter-21-decomposing-operator-typed-occurrences).  
Execution control: [Chapter 21 Preparation/Execution Record](Chapter_21_Preparation_Record.md).

## Chapter 21 WP2 Canonical Route

```text
Chapter 21 WP1 — operator/type boundary and Frame family
→ WP2 §§21.5–21.9 — Attractor and Asymmetry families
→ WP3 §§21.10–21.12 — Impulse, Binding, Failure, Stop, Non-Capture
```

Primary anchors: [§21.5](../01_blocks/03_part_ii_sub.md#21-5-attractor-typed-occurrence), [§21.7](../01_blocks/03_part_ii_sub.md#21-7-dynamic-attractor-occurrence), and [§21.9](../01_blocks/03_part_ii_sub.md#21-9-distributed-asymmetry).  
Execution control: [Chapter 21 Preparation/Execution Record](Chapter_21_Preparation_Record.md).

## Chapter 21 WP3 Cross-Reference Return

- [§21.10](../01_blocks/03_part_ii_sub.md#21-10-impulse-typed-occurrence) applies Chapter-20 `DECOMPOSE` to Impulse-typed occurrences and protects PMS Base, motive, person, Path, and RETYPE boundaries.
- [§21.11](../01_blocks/03_part_ii_sub.md#21-11-binding-typed-occurrence) applies the procedure to Binding-typed occurrences and separates homogeneous coarse claims from unequal internal load.
- [§21.12](../01_blocks/03_part_ii_sub.md#21-12-failed-operator-occurrence-decomposition) owns family-specific Failure, Mandatory Stop, Non-Capture, completion, and Chapter-22 handoff.

## Chapter 21 WP4 Provisional-Lock Route

```text
Chapter 20 generic DECOMPOSE lock
→ Chapter 21 operator-occurrence family application lock
→ Chapter 22 Preparation Gate for composite structures
```

Primary anchor: [Chapter-21 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-21-completion-boundary).  
Execution control: [Chapter 21 Preparation/Execution Record](Chapter_21_Preparation_Record.md#27-wp4-execution-and-provisional-lock-record).

## Chapter 22 Preparation Cross-References

```text
Chapter 1 composite object model
+ Chapter 15 composition lineage and Loss where applicable
+ Chapters 18–20 source/granularity/DECOMPOSE procedure
+ Chapter 21 occurrence-family methods
→ Chapter 22 composite decomposition
```

Chapter 22 owns internal composition map, component hierarchy, distributed function, redundancy, substitution, internal conflict, composite stability, operator weighting, source-side profiles, and fragmentation failure. Chapter 23 retains event/non-event decomposition; Chapter 24 retains Path/Trajectory decomposition; Chapter 25 retains the complete resolution taxonomy; Chapter 27 retains complete SUB limits and the full Counterfactual Component Test; RETYPE Chapters 34–35 retain contextual higher-level functions and projected profiles.

Preparation control: [Chapter 22 Preparation Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP1 Canonical Route

```text
Chapter 21 provisional lock
→ Chapter 22 Preparation Gate
→ §§22.1–22.4 composite entry, internal map, component roles, operator weighting
→ WP2 §§22.5–22.8 profiles, distribution, redundancy/substitution, conflict
```

Primary anchor: [Chapter 22](../01_blocks/03_part_ii_sub.md#chapter-22-decomposing-composite-structures).  
Execution control: [Chapter 22 Preparation/Execution Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP2 Canonical Route

```text
Chapter 22 WP1 composite source and internal map
→ §22.5 source-side modulating profiles
→ §22.6 distributed function under coordination burden
→ §22.7 redundancy, substitution, and qualitative thresholds
→ §22.8 internal conflict and operation-boundary control
→ Chapter 22 WP3 stability, non-fragmentation, Failure/Stop/Non-Capture, Record, and Chapter-23 handoff
```

Primary anchors: [§22.5](../01_blocks/03_part_ii_sub.md#22-5-modulating-profiles), [§22.6](../01_blocks/03_part_ii_sub.md#22-6-distributed-function), [§22.7](../01_blocks/03_part_ii_sub.md#22-7-redundant-and-substitutable-components), and [§22.8](../01_blocks/03_part_ii_sub.md#22-8-internal-conflict).  
Execution control: [Chapter 22 Preparation/Execution Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP3 Canonical Route

```text
Chapter 22 WP1 source composite and internal map
→ WP2 profiles, distribution, redundancy/substitution, and conflict
→ §22.9 Composite Stability
→ §22.10 non-fragmenting composite decomposition and result axes
→ §22.11 Failure, Mandatory Stop, Non-Capture, Record view, and Chapter-23 handoff
→ Chapter 22 WP4 integrated lock pass
```

Primary anchors: [§22.9](../01_blocks/03_part_ii_sub.md#22-9-composite-stability), [§22.10](../01_blocks/03_part_ii_sub.md#22-10-decomposition-of-a-composite-without-fragmentation), and [§22.11](../01_blocks/03_part_ii_sub.md#22-11-failed-composite-decomposition).  
Execution control: [Chapter 22 Preparation/Execution Record](Chapter_22_Preparation_Record.md).

## Chapter 22 WP4 Provisional-Lock Route

```text
Chapter 20 generic DECOMPOSE lock
→ Chapter 21 operator-occurrence family lock
→ Chapter 22 relational composite-decomposition lock
→ Chapter 23 Preparation Gate for Event and Non-Event Decomposition
```

Primary anchor: [Chapter-22 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-22-completion-boundary).  
Execution control: [Chapter 22 Preparation/Execution Record](Chapter_22_Preparation_Record.md#27-wp4-execution-and-provisional-lock-record).

## Chapter 23 Preparation Cross-References

```text
Foundations Chapter 3 temporal object distinctions
+ PATH Chapter 14 Non-Event role
+ Chapters 18–20 source/granularity/DECOMPOSE procedure
+ Chapters 21–22 occurrence and composite methods
→ Chapter 23 Event, Non-Event, and internal-temporal decomposition
```

Chapter 23 owns Event decomposition, Extended Events, Event Clusters, Event Inflation, Non-Event preservation, delay structures, repeated non-decision, internal temporal order, temporal granularity drift, and Event/Non-Event confusion. Chapter 24 owns Path/Trajectory decomposition and same-path versus new-PATH classification. Chapter 25 owns the complete resolution taxonomy. Chapter 27 owns complete SUB limits. Chapter 28 owns cases and Local Audit. RETYPE retains contextual target functions.

Preparation control: [Chapter 23 Preparation Record](Chapter_23_Preparation_Record.md).

## Chapter 23 WP1 Cross-References

```text
Chapter 3 Event / Non-Event / Transition distinctions
+ Chapter 20 generic DECOMPOSE procedure
+ Chapter 21 occurrence integrity
+ Chapter 22 composite and operation-boundary discipline
→ Chapter 23 WP1 Event entry, boundary, extension, clustering, and inflation controls
```

WP2 owns full Non-Event, delay, repeated-non-decision, and absent-binding analysis. WP3 owns internal temporal order, temporal drift, confusion, result axes, Failure/Stop/Non-Capture, Record, and handoff. Chapter 24 owns Path and Trajectory decomposition. Chapter 25 owns the complete resolution taxonomy.

Primary sites: [§§23.1–23.4](../01_blocks/03_part_ii_sub.md#23-1-event-decomposition). Execution control: [Chapter 23 Preparation/Execution Record](Chapter_23_Preparation_Record.md#20-wp1-execution-record).

## Chapter 23 WP2 Cross-References

```text
Chapter 3 Event / Non-Event distinction
+ Chapter 14 PATH-side Non-Event role
+ Chapter 20 generic DECOMPOSE procedure
+ Chapter 21 occurrence/person boundary
+ Chapter 23 WP1 Event-side boundary discipline
→ Chapter 23 WP2 expectation, Λ-preservation, delay, repeated-non-decision, and absent-binding controls
```

WP3 owns internal temporal order, multiple clocks, drift, confusion, result axes, Failure/Stop/Non-Capture, Record, and Chapter-24 handoff. Chapter 24 owns broader Path/Trajectory objects; Chapter 25 owns the complete resolution taxonomy.

Primary sites: [§§23.5–23.8](../01_blocks/03_part_ii_sub.md#23-5-non-event-decomposition). Execution control: [Chapter 23 WP2 Execution Record](Chapter_23_Preparation_Record.md#21-wp2-execution-record).



## Chapter 23 WP3 Cross-Reference Closure

- [§23.9](../01_blocks/03_part_ii_sub.md#23-9-internal-temporal-order) applies Chapters 2–3 and 20 to internal order, partial order, overlap, interruption, thresholds, and multiple clocks.
- [§23.10](../01_blocks/03_part_ii_sub.md#23-10-temporal-granularity-drift) routes bounded no-gain toward Chapter 25 without pre-empting its complete taxonomy.
- [§23.11](../01_blocks/03_part_ii_sub.md#23-11-event--non-event-confusion-results-and-completion) completes category confusion, result axes, Failure/Stop/Non-Capture, Record mapping, and the Chapter-24 handoff.
- Chapter 24 retains Path/Trajectory decomposition; Chapter 27 retains full SUB limits; RETYPE retains contextual target functions.


## Chapter 23 Provisional-Lock Cross-Reference

- Chapters 3 and 14 retain primary Event/Non-Event and PATH-context definitions.
- Chapter 20 retains generic `DECOMPOSE` procedure ownership.
- Chapter 23 owns bounded Event/Non-Event and internal temporal decomposition.
- Chapter 24 owns Path/Trajectory decomposition and broader temporal reference continuity.
- Chapter 25 owns the complete resolution taxonomy; Chapters 26–28 own operation boundaries, SUB limits, cases, audit, and Part outputs.
- RETYPE retains contextual target functions.

Primary site: [Chapter 23 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-23-completion-boundary).

## Chapter 24 Preparation Cross-References

```text
PATH Chapters 10–16 formed Path/Trajectory objects
+ Chapters 18–20 source/granularity/DECOMPOSE procedure
+ Chapters 22–23 composite and internal-temporal decomposition
→ Chapter 24 Path/Trajectory decomposition
```

Chapter 24 owns Same-Path versus rival PATH classification, subpaths, transition clusters, turning-point decomposition, branch reconstruction, internal Frame changes, competing continuations, irrecoverable PATH compression, and Path-Dependence-load decomposition. Chapter 25 owns the complete resolution taxonomy. Chapter 26 owns complete operation-boundary adjudication. Chapter 27 owns complete SUB limits. Chapter 28 owns cases and Local Audit. RETYPE retains contextual target functions.

Preparation control: [Chapter 24 Preparation Record](Chapter_24_Preparation_Record.md).

## Chapter 24 WP1 Cross-References

```text
PATH Chapters 10–16
→ source Path/Trajectory definitions, selection, formation, branches, Non-Events, and COMPOSE

SUB Chapters 18–20
→ source entry, granularity change, and generic DECOMPOSE

Chapter 23
→ internal Event/Non-Event temporal objects that may occur inside Path transitions

Chapter 24 WP1
→ PATH-source entry, formation lineage, decomposition reason, subpaths, transition clusters, operation boundary
```

WP2 retains turning points, branches, internal Frame changes, continuations, and non-linearity. WP3 retains Loss integration, Path-Dependence load, rival PATH adjudication, result axes, Failure/Stop/Non-Capture, Record view, and Chapter-25 handoff. Primary site: [Chapter 24 WP1](../01_blocks/03_part_ii_sub.md#chapter-24-decomposing-paths-and-trajectories).

## Chapter 24 WP2 Cross-Reference Return

```text
PATH Chapter 13
→ branch statuses, source-bounded alternatives, and Alternative Status Record

PATH Chapters 10–12
→ Path, Trajectory, turning-point pressure, and Path-Dependence distinctions

Chapter 23
→ Event/Non-Event and internal temporal structures inside candidate transitions

Chapter 24 WP1
→ source entry, formation lineage, subpaths, transition clusters, operation boundary

Chapter 24 WP2
→ turning points, branches, internal Frame changes, competing continuations, non-linearity

Chapter 24 WP3
→ inherited/new Loss, Path-Dependence load, rival PATH, results, Failure/Stop/Non-Capture, Record, handoff
```

Primary site: [Chapter 24 WP2](../01_blocks/03_part_ii_sub.md#24-5-turning-points).

## Chapter 24 WP3 Cross-Reference Return

```text
PATH Chapters 10–16
→ Path/Trajectory objects, Path Dependence, branches, Loss, and original COMPOSE formation

Chapter 20
→ generic DECOMPOSE procedure and four result axes

Chapter 24 WP1–WP2
→ source lineage, subpaths, transitions, turning points, branches, Frames, continuations

Chapter 24 WP3
→ irrecoverable compression, Path-Dependence load, rival PATH, results, Failure/Stop/Non-Capture, Record

Chapter 25
→ complete Resolution Gain, Neutrality, Drift, and Escape taxonomy

Chapters 26–28 and RETYPE
→ operation adjudication, SUB Limits, cases/audit, and contextual target functions
```

Primary site: [Chapter 24 WP3](../01_blocks/03_part_ii_sub.md#24-9-irrecoverable-compression).

## Chapter 24 Provisional-Lock Cross-Reference Return

- PATH definitions and formation: Chapters 10–16.
- Generic `DECOMPOSE`: Chapter 20.
- Event/Non-Event internal temporal opening: Chapter 23.
- Path/Trajectory decomposition: Chapter 24 §§24.1–24.12.
- Integrated lock: [Chapter 24 WP4](Chapter_24_Preparation_Record.md#26-wp4-execution-and-provisional-lock-record).
- Resolution Gain/Neutrality/Drift/Escape: Chapter 25.
- Complete operation boundaries: Chapter 26.
- SUB Limits: Chapter 27.
- Cases and Part audit: Chapter 28.
- Contextual target functions: RETYPE.

## Chapter 25 Preparation Cross-References

```text
Chapters 18–24 source, granularity, DECOMPOSE, and object-family reconstructions
+ Chapter 6 Admissibility Band
+ Chapter 7 Shared Record and canonical classes
→ Chapter 25 resolution classification and SUB-specific Stop markers
```

Chapter 25 owns gain, neutrality, drift, escape, Detail without Purchase, Components without Coarser Function, Source Overreach, Calibration Loss, Decomposition Fatigue, local classification, and Mandatory Stop. Chapter 26 owns complete SUB/RETYPE operation-boundary adjudication. Chapter 27 owns complete SUB limits. Chapter 28 owns cases and Local Audit. LIMITS retains system-wide Source Ceiling, Anti-Immunization, Stop, Non-Capture, and authority consolidation.

Preparation control: [Chapter 25 Preparation Record](Chapter_25_Preparation_Record.md).

## Chapter 25 WP1 Cross-References

```text
Chapter 6 Admissibility Band
+ Chapter 7 Shared Transformation Record
+ Chapters 18–24 source and finer-reconstruction outputs
→ Chapter 25 WP1 comparison entry and Gain/Neutrality/Drift/Escape classification
```

- Gain/Neutrality/Drift/Escape primary site: [Chapter 25 WP1](../01_blocks/03_part_ii_sub.md#chapter-25-resolution-gain-neutrality-drift-and-escape).
- Purchase, coarser-function, Source Overreach, and Calibration Loss remain Chapter 25 WP2.
- Decomposition Fatigue, complete classification, Stop/Failure/Non-Capture/re-entry, Record view, and handoff remain Chapter 25 WP3.
- Complete SUB/RETYPE boundary remains Chapter 26; complete SUB limits remain Chapter 27; cases and Local Audit remain Chapter 28.
- System-wide anti-immunization, Stop, Non-Capture, Source Ceiling, and authority boundaries remain LIMITS-owned.

## Chapter 25 WP2 Cross-References

```text
Chapter 6 Relevance Floor and Traceability Ceiling
+ Chapter 20 source, component, relation, and source-function requirements
+ Chapter 25 WP1 local resolution results
→ Chapter 25 WP2 purchase, coarser-function, Source-Overreach, and calibration controls
```

- Detail without Purchase and unsupported refinement: [§25.5](../01_blocks/03_part_ii_sub.md#25-5-detail-without-purchase).
- Components without Coarser Function and relation support: [§25.6](../01_blocks/03_part_ii_sub.md#25-6-components-without-coarser-function).
- Source Overreach and non-compensation: [§25.7](../01_blocks/03_part_ii_sub.md#25-7-source-overreach).
- Calibration Loss and open-threshold discipline: [§25.8](../01_blocks/03_part_ii_sub.md#25-8-calibration-loss).
- Decomposition Fatigue, complete classification, result axes, Failure/Stop/Non-Capture/re-entry, Record view, and handoff remain Chapter 25 WP3.
- Complete operation-boundary adjudication remains Chapter 26; complete SUB limits remain Chapter 27; cases and Local Audit remain Chapter 28.

## Chapter 25 WP3 Cross-References

- Decomposition Fatigue: [§25.9](../01_blocks/03_part_ii_sub.md#25-9-decomposition-fatigue).
- Six-family classification and result axes: [§25.10](../01_blocks/03_part_ii_sub.md#25-10-resolution-classification).
- Mandatory Stop, Non-Capture, re-entry, Record view, and handoff: [§25.11](../01_blocks/03_part_ii_sub.md#25-11-stop-reentry-and-completion).
- Execution control: [Chapter 25 WP3 Execution Record](Chapter_25_Preparation_Record.md#25-wp3-execution-record).
- Next controlled step: Chapter 25 WP4 integrated audit and provisional lock.

## Chapter 25 Provisional-Lock Cross-Reference Return

- Admissibility Band and non-compensation: Chapter 6.
- Shared Transformation Record: Chapter 7.
- Generic `DECOMPOSE`: Chapter 20.
- Object-family decompositions: Chapters 21–24.
- Resolution Gain/Neutrality/Drift/Escape and bounded continuation: Chapter 25 §§25.1–25.11.
- Integrated lock: [Chapter 25 WP4](Chapter_25_Preparation_Record.md#26-wp4-execution-and-provisional-lock-record).
- SUB/RETYPE operation boundary: Chapter 26.
- SUB Limits: Chapter 27.
- Cases and Part audit: Chapter 28.
- Contextual target functions: RETYPE.

## Chapter 26 Preparation Cross-References

```text
Chapter 4 operation grammar
+ Chapter 5 origin type / target function
+ Chapter 20 generic DECOMPOSE
+ Chapter 24 same-source Path/Trajectory lineage
+ Chapter 25 resolution and bounded continuation
→ Chapter 26 SUB/RETYPE operation boundary
```

Chapter 26 prepares §§26.1–26.12, the trajectory and Attractor comparisons, recontextualization boundary, dual-operation rule, invalid collapse, nineteen-field assessment view, and Chapter-27 handoff. Full RETYPE theory remains Chapters 29–40; full SUB limits remain Chapter 27; integrated cases remain Chapter 28.

Preparation control: [Chapter 26 Preparation Record](Chapter_26_Preparation_Record.md).

## Chapter 26 WP1 Cross-References

```text
Chapter 4 operation grammar
+ Chapter 5 origin type / target function
+ Chapter 20 DECOMPOSE procedure
+ Chapters 24–25 source and resolution outputs
→ Chapter 26 WP1 operation-entry and DECOMPOSE / PROJECT_AS boundary
```

- Primary site: [Chapter 26 WP1](../01_blocks/03_part_ii_sub.md#chapter-26-the-boundary-between-sub-and-retype).
- Trajectory/Attractor comparisons, subtle misclassification, reverse misclassification, and recontextualization remain Chapter 26 WP2.
- Complete decision test, dual operation, invalid collapse, result axes, Failure/Stop/Non-Capture, Record view, and handoff remain Chapter 26 WP3.
- Complete SUB limits remain Chapter 27; cases and Local Audit remain Chapter 28.
- Full contextual target-function theory remains RETYPE Chapters 29–40; system-wide boundaries remain LIMITS-owned.

## Chapter 26 WP2 Cross-References

```text
Chapter 21 occurrence/operator protection
+ Chapter 24 Trajectory decomposition
+ Chapter 25 preserved claim dispositions
+ Chapter 26 WP1 primary boundary
→ Chapter 26 WP2 trajectory/Attractor comparisons,
  misclassification guards, and recontextualization boundary
```

- Primary site: [Chapter 26 WP2](../01_blocks/03_part_ii_sub.md#26-5-trajectory-decomposition-and-projection).
- Complete decision test, dual-operation Records and chain order, invalid collapse, result axes, Failure/Stop/Non-Capture, Record view, and Chapter-27 handoff remain WP3.
- Integrated lock remains WP4.
- Complete SUB boundaries remain Chapter 27; cases and Local Audit remain Chapter 28.
- Full target-function families remain RETYPE Chapters 29–40; system-wide limits remain LIMITS-owned.

## Chapter 26 WP3 Cross-References

- Decision test: [§26.10](../01_blocks/03_part_ii_sub.md#26-10-sub-retype-decision-test).
- Dual operation, Record separation, and chain order: [§26.11](../01_blocks/03_part_ii_sub.md#26-11-dual-operation).
- Invalid collapse, result axes, Failure/Stop/Non-Capture, Record view, and Chapter-27 handoff: [§26.12](../01_blocks/03_part_ii_sub.md#26-12-invalid-collapse).
- Execution control: [Chapter 26 WP3 Execution Record](Chapter_26_Preparation_Record.md#15-wp3-execution-record).
- Next controlled step: Chapter 26 WP4 integrated audit and provisional lock.

## Chapter 26 Provisional-Lock Cross-Reference Return

- Operation grammar: Chapter 4.
- Origin type and target function: Chapter 5.
- Generic `DECOMPOSE`: Chapter 20.
- Path/Trajectory source and resolution outputs: Chapters 24–25.
- SUB/RETYPE operation boundary: Chapter 26 §§26.1–26.12.
- Integrated lock: [Chapter 26 WP4](Chapter_26_Preparation_Record.md#chapter-26-wp4-execution-and-provisional-lock-record).
- Lower and upper SUB boundaries: Chapter 27.
- SUB cases, Local Audit, and Part lock: Chapter 28.
- Contextual target-function theory: RETYPE Chapters 29–40.
- System-wide Source, Stop, Non-Capture, anti-immunization, and authority controls: LIMITS.

## Chapter 27 Preparation Cross-Reference Route

```text
Chapter 6
→ general Admissibility Band, PraxisPurchase, TraceableLoad, Counterfactual Sensitivity

Chapters 18–20
→ eligible source object, lower granularity, and generic DECOMPOSE procedure

Chapters 21–24
→ family-specific source-reference and coarser-function burdens

Chapter 25
→ Gain, Neutrality, Drift, Escape, Source Overreach, Calibration Loss, Stop, and re-entry

Chapter 26
→ only claims already classified as DECOMPOSE

Chapter 27
→ local lower/upper SUB boundaries, Source Ceiling, component sensitivity,
   coarser-function traceability, type integrity, Stop, Claim Reduction, and Non-Capture

Chapter 28
→ cases, countercases, Local Audit, canonical mapping, and SUB lock

LIMITS Chapters 44–52
→ system-wide consolidation without retroactive redefinition
```

Preparation control: [Chapter 27 Preparation Record](Chapter_27_Preparation_Record.md).

## Chapter 27 WP1 Cross-References

```text
Chapter 6 Admissibility Band
+ Chapter 20 DECOMPOSE procedure
+ Chapter 25 resolution outcomes
+ Chapter 26 operation boundary
→ Chapter 27 WP1 lower/upper local SUB boundaries
```

- Primary site: [Chapter 27 WP1](../01_blocks/03_part_ii_sub.md#chapter-27-sub-boundary-conditions).
- Source Ceiling, Counterfactual Component Test, coarser-function traceability, and Type Preservation remain Chapter 27 WP2.
- No-privilege, Stop/Reduction/Non-Capture, complete admissibility test, result axes, Record view, and handoff remain Chapter 27 WP3.
- Cases, Local Audit, output mapping, and SUB lock remain Chapter 28.
- System-wide ceilings and Stop consolidation remain LIMITS-owned.

## Chapter 27 WP2 Cross-References

```text
Chapter 6 Admissibility Band and Source/Claim ceilings
+ Chapter 20 DECOMPOSE support and Loss procedure
+ Chapter 25 source overreach, calibration, Stop, and re-entry
+ Chapter 27 WP1 lower/upper boundaries
→ Chapter 27 WP2 Source Ceiling, component sensitivity, function traceability, and type integrity
```

- Primary site: [Chapter 27 WP2](../01_blocks/03_part_ii_sub.md#27-5-source-ceiling).
- No-privilege, final Stop/Reduction/Non-Capture, complete admissibility test, result axes, Record view, and handoff remain Chapter 27 WP3.
- Cases, Local Audit, Part output mapping, and SUB lock remain Chapter 28.
- System-wide ceiling and authority consolidation remains LIMITS-owned.

## Chapter 27 WP3 Cross-References

```text
Chapter 25 resolution, Stop, anti-escape, and re-entry
+ Chapter 26 operation-boundary separation
+ Chapter 27 WP1 lower/upper boundaries
+ Chapter 27 WP2 source, component, function, and type controls
→ Chapter 27 WP3 complete local SUB admissibility and routing
→ Chapter 28 cases, Local Audit, output mapping, and SUB lock
```

System-wide consolidation remains LIMITS-owned. Primary site: [Chapter 27 WP3](../01_blocks/03_part_ii_sub.md#27-9-no-privilege-of-fine-resolution).

## Chapter 27 Provisional-Lock Cross-Reference

```text
Chapters 18–26 source, granularity, DECOMPOSE, resolution, and operation-boundary controls
→ Chapter 27 complete local SUB boundary procedure
→ Chapter 28 cases, Local Audit, output mapping, and SUB lock
→ LIMITS later consolidates system-wide boundaries without retroactive redefinition
```

Primary site: [Chapter 27 completion boundary](../01_blocks/03_part_ii_sub.md#chapter-27-completion-boundary).

## Chapter 28 Preparation Cross-Reference Route

```text
Chapters 18–20
→ source object, granularity, and generic DECOMPOSE procedure

Chapters 21–24
→ occurrence, composite, temporal, Event/Non-Event, and PATH-source case burdens

Chapter 25
→ Gain, Neutrality, Drift, Escape, Stop, and re-entry

Chapter 26
→ SUB versus RETYPE, recontextualization, and dual-operation separation

Chapter 27
→ Lower/Upper SUB boundaries, Source Ceiling, component test, function/type traceability

Chapter 28
→ positive, counter, and confusion artifacts; Local Audit; output mapping; SUB lock

03_cases/*
→ case evidence and records below canonical prose

RETYPE / LIMITS / Chapter 53
→ later target-function theory, system-wide boundaries, and integrated audit
```

Preparation control: [Chapter 28 Preparation Record](Chapter_28_Preparation_Record.md).

## Chapter 28 WP1 Cross-Reference Route

```text
§28.1 case architecture
→ C28-FRAME-01
→ C28-ATTR-01
→ C28-ASYM-01
→ C28-NONEVENT-01
→ C28-TRAJECTORY-01
→ C28-GAIN-01
→ Case Index and schema-valid Records
→ WP2 countercases and first confusion pair
```

The cases remain below canonical prose and do not redefine Chapters 18–27.

## Chapter 28 WP2 Cross-Reference Route

```text
§§28.8–28.13 countercases
→ §§28.14–28.15 confusion pair
→ eight artifact sets
→ Case Index
→ WP3 remaining confusion cases and integrated Local Audit
```

## Chapter 28 WP3 Cross-Reference Route

```text
§§28.16–28.17 final confusion cases
→ §§28.18–28.19 Local Audit and output/loss/chain integration
→ §28.20 lock readiness
→ Chapter 28 WP4 integrated lock pass
```

## Chapter 28 and Part II — SUB Provisional-Lock Map

```text
Chapters 18–20
→ source eligibility, granularity relation, generic DECOMPOSE

Chapters 21–24
→ occurrence, composite, temporal, PATH/Trajectory applications

Chapters 25–27
→ resolution, SUB/RETYPE boundary, local SUB limits

Chapter 28
→ sixteen case targets, twenty-four-question Local Audit, canonical mapping
→ Chapter 28 provisional lock
→ Part II — SUB provisional lock

Part II lock
→ Chapter 29 Preparation Gate
→ Part III — RETYPE without inherited target function
```

Primary site: [Chapter 28 and Part II completion boundary](../01_blocks/03_part_ii_sub.md#part-ii-sub-provisional-lock-boundary).

## Chapter 29 Preparation Cross-Reference Route

```text
Foundations Chapters 1–8
→ source identity, coordinates, operation grammar, origin type, target function, continuity, Band, Record, non-equivalences

Part I — PATH
→ possible Trajectory or composite source histories

Part II — SUB and Chapter 26
→ source traces, operation-boundary findings, prior dispositions, and unexecuted PROJECT_AS pressure

Chapter 29
→ governing functional-projection and no-replacement logic

Chapter 30
→ complete PROJECT_AS signature, declarations, tests, Loss, scope, and results

Chapters 31–40
→ projection families, alternatives, limits, cases, and RETYPE Local Audit
```

Preparation control: [Chapter 29 Preparation Record](Chapter_29_Preparation_Record.md).


## Chapter 29 WP1 Canonical Cross-Reference Route

```text
Chapter 5 definitions
→ Chapter 29 WP1 typed functional-projection entry
→ Chapter 29 WP2 integrity/continuity/boundedness
→ Chapter 29 WP3 operation-boundary consolidation
→ Chapter 30 complete PROJECT_AS procedure
```

| WP1 concept | Canonical source | Protected successor |
|---|---|---|
| RETYPE purpose and typed `X/T/C/F` claim | [§29.1](../01_blocks/04_part_iii_retype.md#29-1-purpose-of-retype) | Chapter 30 operation procedure |
| target-context declaration and same-source contrast | [§29.2](../01_blocks/04_part_iii_retype.md#29-2-functional-projection) | WP2 Contextual Boundedness and counterfactual tests |
| Origin-Type Preservation and no-new-primitive rule | [§29.3](../01_blocks/04_part_iii_retype.md#29-3-origin-type-preservation) | §29.5 target function versus operator type |
| specific relational target-function candidate | [§29.4](../01_blocks/04_part_iii_retype.md#29-4-target-function) | WP2 Functional Continuity and Chapter 30 result discipline |

Protected boundaries: Chapter 5 remains the definition owner; Chapter 26 remains the SUB/RETYPE boundary owner; Chapter 30 retains full `PROJECT_AS`; Chapters 31–40 retain families, alternatives, limits, cases, and audit.

## Chapter 29 WP2 Canonical Cross-Reference Route

```text
§29.5 operator-type separation
→ §29.6 source-object integrity and load trace
→ §29.7 Functional Continuity and bounded source variation
→ §29.8 Contextual Boundedness and Loss
→ Chapter 29 WP3 integrated Part boundaries
→ Chapter 30 complete PROJECT_AS procedure
```

| WP2 burden | Primary canonical site | Later owner |
|---|---|---|
| target function versus operator type | [§29.5](../01_blocks/04_part_iii_retype.md#29-5-target-function-versus-operator-type) | Chapters 31–35 family-specific use |
| Source Object Integrity | [§29.6](../01_blocks/04_part_iii_retype.md#29-6-source-object-integrity) | Chapter 30 complete declaration |
| Functional Continuity and bounded source variation | [§29.7](../01_blocks/04_part_iii_retype.md#29-7-functional-continuity) | Chapter 30 test procedure; Chapter 39 limits |
| Contextual Boundedness and Loss | [§29.8](../01_blocks/04_part_iii_retype.md#29-8-contextual-boundedness) | Chapter 30 Record; LIMITS integrated audit |

## Chapter 29 WP3 Cross-References

| Chapter-29 site | Receives from | Hands to |
|---|---|---|
| [§29.9 Projection without Replacement](../01_blocks/04_part_iii_retype.md#29-9-projection-without-replacement) | PATH and SUB locks; Chapters 5, 6, 26 | Chapter 30 preservation and Loss declarations |
| [§29.10 Typed Claim Consolidation](../01_blocks/04_part_iii_retype.md#29-10-functional-projection-as-a-typed-claim) | §§29.1–29.8 | Chapter 30 result and mapping separation |
| [§29.11 RETYPE versus Recontextualization](../01_blocks/04_part_iii_retype.md#29-11-retype-versus-recontextualization) | PMS Φ; Chapter 4 operation grammar | Chapter 30 boundary procedure; Chapters 37–38 confusion tests |
| [§29.12 RETYPE versus COMPOSE](../01_blocks/04_part_iii_retype.md#29-12-retype-versus-compose) | PATH and Chapter 15 | operation-chain records and Chapter 30 |
| [§29.13 RETYPE versus DECOMPOSE](../01_blocks/04_part_iii_retype.md#29-13-retype-versus-decompose) | SUB and Chapter 26 | Chapter 30 complete `PROJECT_AS` specification |

WP3 closes conceptual drafting but leaves the integrated Chapter-29 lock audit to WP4.

## Chapter 29 Lock and Chapter 30 Preparation Cross-References

| From | To | Relation |
|---|---|---|
| Chapter 29 completion boundary | Chapter 30 Preparation Record | conceptual lock to operation-preparation handoff |
| Chapter 30 Preparation Record | Chapter 30 Contract | work-package and completion-control binding |
| Chapter 30 Preparation Record | Operation Registry | existing `PROJECT_AS` identity and applicability owner |
| Chapter 30 Preparation Record | Shared Record schema | field-syntax and conditional-payload owner |
| Chapter 30 Preparation Record | Output Classes / Decision Tree | class identity and route-selection owners |
| Chapter 30 Preparation Record | Chapter 31 | later family-specific operational handoff |

Primary links: [Chapter 29 completion](../01_blocks/04_part_iii_retype.md#chapter-29-completion-boundary), [Chapter 29 execution record](Chapter_29_Preparation_Record.md#19-wp4-execution-and-provisional-lock-record), and [Chapter 30 Preparation Record](Chapter_30_Preparation_Record.md).

## Chapter 30 WP1 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| PROJECT_AS definition | [§30.1](../01_blocks/04_part_iii_retype.md#30-1-definition) | Chapters 4, 5, and 29 | §§30.5–30.13 |
| minimal signature | [§30.2](../01_blocks/04_part_iii_retype.md#30-2-minimal-signature) | Structure §30.2; Operation Registry | Chapter 30 complete procedure |
| conjunctive preconditions | [§30.3](../01_blocks/04_part_iii_retype.md#30-3-preconditions) | Chapters 6–7 | WP2 tests and WP3 routing |
| source declaration | [§30.4](../01_blocks/04_part_iii_retype.md#30-4-source-declaration) | Chapters 1–3, 7, 29 | §30.5 target declaration |
| execution control | [WP1 Record](Chapter_30_Preparation_Record.md#16-wp1-execution-record) | Chapter-30 Contract | WP2 §§30.5–30.8 |

Chapter 30 remains open. `PROJECT_AS` has not been executed and Chapters 31–40 retain family, competition, limit, case, audit, and RETYPE-lock ownership.

## Chapter 30 WP2 Cross-Reference

```text
§30.5 Target Declaration
→ Chapter 2 target coordinates
→ Chapter 5 target function and transformation context

§30.6 Projection Justification
→ Chapter 6 PraxisPurchase and rival pressure
→ Chapter 29 typed X/T/C/F claim

§30.7 Constitutive Source Trace
→ Chapter 5 Functional Continuity
→ Chapter 6 TraceableLoad and Source Ceiling
→ Chapter 7 source and Loss retention

§30.8 Counterfactual Sensitivity
→ Chapter 6 mandatory sensitivity check
→ Chapter 29 bounded source/context variation
→ Chapter 30 WP3 result and scope completion
```

Primary route: [Chapter 30 WP2](../01_blocks/04_part_iii_retype.md#30-5-target-declaration).

## Chapter 30 WP3 Cross-References

- [Validity Scope](../01_blocks/04_part_iii_retype.md#30-9-validity-scope) → Chapter 2 coordinates; Chapter 5 Contextual Boundedness; Chapter 6 Claim Ceiling; Chapter 29 re-entry.
- [Projection Visibility and Loss](../01_blocks/04_part_iii_retype.md#30-10-projection-visibility-and-loss) → Chapter 7 Shared Record; canonical five-part Loss; prior source Loss.
- [Alternatives and No-Projection](../01_blocks/04_part_iii_retype.md#30-11-alternative-projections-and-no-projection) → Chapter 4 operation identity; Chapter 26 SUB/RETYPE boundary; Boundary Decision Tree.
- [Projection Results](../01_blocks/04_part_iii_retype.md#30-12-projection-results) → Output Class Index; Claim Type Table; result-axis separation.
- [PROJECT_AS Record](../01_blocks/04_part_iii_retype.md#30-13-project-as-record) → Chapter 7 Shared Transformation Record; Transformation Record schema; Appendix F future template.

Chapter 31 receives procedure only; its trajectory-as-frame-function claim remains unexecuted and independently testable.

\n## Chapter 30 Lock → Chapter 31 Preparation Route\n\n```text\nChapter 29 conceptual RETYPE lock\n→ Chapter 30 generic PROJECT_AS procedural lock\n→ Chapter 31 trajectory-to-frame-function family test\n→ later Chapter 36 competition, Chapter 39 limits, and Chapter 40 cases/audit\n```\n\nChapter 31 references Chapters 11–12 for Trajectory and historical load, Chapter 2 for Frame, Chapter 29 for projection without replacement, and Chapter 30 for the generic operation procedure.\n\nPrimary sites: [Chapter 30 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-30-completion-boundary) and [Chapter 31 Preparation Record](Chapter_31_Preparation_Record.md).\n


## Chapter 31 WP1 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| bounded family claim | [§31.1](../01_blocks/04_part_iii_retype.md#31-1-basic-claim) | Chapters 29–30 | §31.5 Historical Load |
| prior PATH source object | [§31.2](../01_blocks/04_part_iii_retype.md#31-2-source-object) | Chapters 11–12 and PATH source record | WP2 source carriers |
| later target context and evidence boundary | [§31.3](../01_blocks/04_part_iii_retype.md#31-3-target-context) | Chapters 2, 5, and 30 | §§31.5–31.7 |
| bounded frame-function candidate | [§31.4](../01_blocks/04_part_iii_retype.md#31-4-frame-function) | Origin-Type Preservation and PROJECT_AS | WP2–WP3 adjudication |
| execution control | [WP1 Record](Chapter_31_Preparation_Record.md#14-wp1-execution-record) | Preparation Record v0.2 | Chapter 31 WP2 |

Chapter 31 WP1 instantiates the generic procedure but does not inherit a successful family result.


## Chapter 31 WP2 Cross-References

| Chapter-31 site | Receives from | Hands to |
|---|---|---|
| [§31.5 Historical Load](../01_blocks/04_part_iii_retype.md#31-5-historical-load) | Chapters 11–12 source Trajectory; Chapter 30 Constitutive Source Trace | §31.9 Counterfactual Frame Test |
| [§31.6 Non-Deterministic Frame-Function](../01_blocks/04_part_iii_retype.md#31-6-frame-function-without-historical-determinism) | Chapter 31 WP1 bounded target function; PMS alternatives and Recontextualization | Chapter 39 limits and Chapter 40 cases |
| [§31.7 Multiple Frame Sources](../01_blocks/04_part_iii_retype.md#31-7-multiple-frame-sources) | present conditions from §31.3; alternative discipline from Chapter 30 | §§31.8–31.11 and Chapter 36 competing projections |
| [WP2 Execution Record](Chapter_31_Preparation_Record.md#15-wp2-execution-record) | Chapter-31 Contract and Prep v0.3 | WP3 §§31.8–31.11 |

The route preserves separate source-object and target-function warrants and does not preselect a family result or canonical class.


## Chapter 31 WP3 Cross-References

| Function | Canonical site | Supporting control |
|---|---|---|
| rhetorical history and trace failure | [§31.8](../01_blocks/04_part_iii_retype.md#31-8-rhetorical-history-versus-frame-function) | source selection and temporal evidence boundary from WP1 |
| Counterfactual Frame Test | [§31.9](../01_blocks/04_part_iii_retype.md#31-9-counterfactual-frame-test) | Chapter 30 Counterfactual Sensitivity procedure |
| same-end/different-history pressure | [§31.9](../01_blocks/04_part_iii_retype.md#31-9-counterfactual-frame-test) | PATH similar-end/different-path distinction |
| competing projections and no-projection | [§31.10](../01_blocks/04_part_iii_retype.md#31-10-competing-frame-projections) | Chapter 30 alternatives and no-projection |
| failed frame projection | [§31.11](../01_blocks/04_part_iii_retype.md#31-11-failed-frame-projection) | Failure/Stop/Non-Capture and Claim Ceiling |
| execution control | [WP3 Record](Chapter_31_Preparation_Record.md#16-wp3-execution-record) | Chapter 31 WP4 next |

## Chapter 31 Lock → Chapter 32 Preparation Cross-Reference

```text
Chapter 11 Trajectory
+ Chapter 15 COMPOSE
+ Chapter 29 functional projection
+ Chapter 30 PROJECT_AS procedure
+ Chapter 31 family non-automaticity
→ Chapter 32 Trajectory as Macro-Event
```

Chapter 32 routes back to Chapters 1 and 3 for Event/Transition distinctions, Chapters 9–17 for source formation, Chapter 23 for Event/Non-Event decomposition boundaries, Chapter 26 for SUB/RETYPE separation, and Chapter 30 for the generic operation Record. Later use occurs in Chapters 36, 39, and 40.

Primary sites: [Chapter 31 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-31-completion-boundary), [Chapter 31 WP4 Record](Chapter_31_Preparation_Record.md#17-wp4-execution-and-provisional-lock-record), and [Chapter 32 Preparation Record](Chapter_32_Preparation_Record.md).


## Chapter 32 WP1 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| bounded family claim and source entry | [§32.1](../01_blocks/04_part_iii_retype.md#32-1-basic-claim) | PATH and Chapters 29–30 | §32.5 Internal Duration |
| Macro-Event target-function grammar | [§32.2](../01_blocks/04_part_iii_retype.md#32-2-macro-event-as-target-function) | Chapter 29 type/function boundary | §32.7 Event Function |
| wider target Path or temporal Frame | [§32.3](../01_blocks/04_part_iii_retype.md#32-3-target-frame) | Chapter 2 coordinates and Chapter 30 target declaration | WP2 role/time/function scope |
| source-supported boundary selection | [§32.4](../01_blocks/04_part_iii_retype.md#32-4-boundary-selection) | PATH source record and Chapter 30 source trace | §32.10 Counterfactual Macro-Event Test |
| WP1 execution state | [Preparation Record §14](Chapter_32_Preparation_Record.md#14-wp1-execution-record) | ZIP 215 | WP2 §§32.5–32.7 |

## Chapter 32 WP2 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| internal duration preservation | [§32.5](../01_blocks/04_part_iii_retype.md#32-5-internal-duration) | PATH source record and WP1 boundaries | §32.8 Punctualization Error |
| internal heterogeneity and phase load | [§32.6](../01_blocks/04_part_iii_retype.md#32-6-internal-heterogeneity) | source trace and Admissibility Band | §32.10 Counterfactual Macro-Event Test |
| Macro-Event transition function | [§32.7](../01_blocks/04_part_iii_retype.md#32-7-event-function) | Chapter 30 target function and scope | §§32.9–32.11 |
| WP2 execution state | [Preparation Record §15](Chapter_32_Preparation_Record.md#15-wp2-execution-record) | ZIP 216 | WP3 §§32.8–32.11 |


## Chapter 32 WP3 Cross-References

| Function | Canonical site | Supporting control |
|---|---|---|
| punctualization error | [§32.8](../01_blocks/04_part_iii_retype.md#32-8-punctualization-error) | Chapters 1, 3, 8 and WP2 duration/heterogeneity preservation |
| `COMPOSE`/`PROJECT_AS` separation | [§32.9](../01_blocks/04_part_iii_retype.md#32-9-macro-event-versus-compose) | Chapters 15, 29, 30 and `new transformation = new testable claim` |
| Counterfactual Macro-Event Test | [§32.10](../01_blocks/04_part_iii_retype.md#32-10-counterfactual-macro-event-test) | Chapter 30 Counterfactual Sensitivity and Chapter 32 boundary warrant |
| rival periodization and alternative source | [§32.10](../01_blocks/04_part_iii_retype.md#32-10-counterfactual-macro-event-test) | PATH source revision and separate occurrence discipline |
| no-projection and failed projection | [§32.11](../01_blocks/04_part_iii_retype.md#32-11-failed-macro-event-projection) | Output mapping, Stop, Failure, Non-Capture, source non-invalidation |
| execution control | [WP3 Record](Chapter_32_Preparation_Record.md#16-wp3-execution-record) | Chapter 32 WP4 next |

## Chapter 32 Lock → Chapter 33 Entry

```text
Chapter 32 completion boundary
→ Chapter 32 WP4 Record
→ Chapter 33 Preparation Record
→ Chapter 33 WP1 §§33.1–33.4
```

Cross-reference obligations:

- Chapter 32 remains the owner of trajectory-to-Macro-Event family conditions.
- Chapter 33 receives no Macro-Event occurrence result or authority.
- Chapter 33 must reference Chapters 9–17 for source Trajectories, Chapter 21 for Attractor-typed occurrences, and Chapters 29–30 for `PROJECT_AS`.
- Chapter 35 remains the owner of operator-weighting profiles where conditionally invoked.

Primary sites: [Chapter 32 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-32-completion-boundary) and [Chapter 33 Preparation Record](Chapter_33_Preparation_Record.md).


## Chapter 33 WP1 Cross-Reference Return

| Chapter-33 WP1 element | Upstream owner | Current role |
|---|---|---|
| source Trajectories | Chapters 9–17 | independently warranted PATH objects |
| recurrent-form source | Chapter 33 | derived comparison object; candidate only |
| Α | PMS Base / Chapters 1 and 8 | operator type preserved |
| PROJECT_AS | Chapters 29–30 | existing operation instantiated, not executed |
| comparison coordinates | Chapters 2, 6, 7 | Frame/granularity/role/time/evidence relations declared |
| Pattern Threshold | Chapter 33 | non-numerical family entry discipline |
| exact five-part Loss | Chapters 6–7 | inherited and retained |
| target `D/E` contrast | Chapter 33 Preparation | same-source function/no-function pressure |

Primary site: [Chapter 33 WP1](../01_blocks/04_part_iii_retype.md#chapter-33-recurrent-trajectory-form-as-attractor-function).

## Chapter 33 WP2 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| constitutive repetition and break conditions | [§33.5](../01_blocks/04_part_iii_retype.md#33-5-constitutive-repetition) | PATH source records and WP1 Pattern Threshold | §§33.8–33.10 adversarial testing |
| reproduction/path-influence mechanism | [§33.5](../01_blocks/04_part_iii_retype.md#33-5-constitutive-repetition) | Chapter 30 Source Trace and temporal continuity | Counterfactual Attractor Test |
| Attractor Load and later-path difference | [§33.6](../01_blocks/04_part_iii_retype.md#33-6-attractor-load) | Chapter 30 target function/scope | WP3 rival/no-projection/failure routes |
| dynamic/static separation | [§33.7](../01_blocks/04_part_iii_retype.md#33-7-dynamic-versus-static-attractor-function) | Chapter 33 WP1 family grammar | Chapter 36 competing projections |
| WP2 execution state | [Preparation Record §15](Chapter_33_Preparation_Record.md#15-wp2-execution-record) | ZIP 220 | WP3 §§33.8–33.10 |

## Chapter 33 WP3 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| retrospective-similarity and source-selection discipline | [§33.8](../01_blocks/04_part_iii_retype.md#33-8-recurrent-form-versus-retrospective-similarity) | WP1 comparability and WP2 constitutive repetition | Chapter 33 WP4 lock audit |
| Counterfactual Attractor Test | [§33.9](../01_blocks/04_part_iii_retype.md#33-9-counterfactual-attractor-test) | Chapter 30 Counterfactual Sensitivity | Chapter 36 competing projections and Chapter 39 limits |
| rival and no-projection space | [§33.9](../01_blocks/04_part_iii_retype.md#33-9-counterfactual-attractor-test) | Chapter 29 typed projection and Chapter 30 alternatives | Chapter 40 cases/audit |
| failed attractor projection and source preservation | [§33.10](../01_blocks/04_part_iii_retype.md#33-10-failed-attractor-projection) | PATH source dispositions and RETYPE anti-immunization | Chapter 33 WP4 lock decision |
| WP3 execution state | [Preparation Record §16](Chapter_33_Preparation_Record.md#16-wp3-execution-record) | ZIP 221 | WP4 integrated audit and Chapter-34 preparation |

## Chapter 33 Lock and Chapter 34 Preparation Map

| Function | Canonical site |
|---|---|
| Chapter-33 family lock | [Chapter 33 completion](../01_blocks/04_part_iii_retype.md#chapter-33-completion-boundary) |
| Chapter-33 WP4 record | [Execution record](Chapter_33_Preparation_Record.md#17-wp4-execution-and-provisional-lock-record) |
| Chapter-34 preparation | [Preparation Record](Chapter_34_Preparation_Record.md) |
| Chapter-34 Contract | [Chapter Contracts](../05_minified/Chapter_Contracts.md#chapter-34-composite-structures-as-higher-level-functions) |
| Chapter-34 Structure | [Structure](../00_source/PMS-STRATA_Structure.md) |

## Chapter 34 WP1 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| family claim and relational source packet | [§34.1](../01_blocks/04_part_iii_retype.md#34-1-basic-claim) | Chapters 1, 20–22, 29–30 | §34.8 formation tests |
| higher-level boundary-function candidate | [§34.2](../01_blocks/04_part_iii_retype.md#34-2-local-differences-as-higher-level-boundary-function) | type/function non-equivalence | WP3 aggregation and counterfactual pressure |
| repeated-Non-Event attractor candidate | [§34.3](../01_blocks/04_part_iii_retype.md#34-3-repeated-non-events-as-higher-level-attractor-function) | PATH/SUB Λ and Chapter 33 safeguards | WP3 threshold and failure |
| distributed asymmetry/access candidate | [§34.4](../01_blocks/04_part_iii_retype.md#34-4-distributed-asymmetries-as-higher-level-omega-function) | Ω boundary and relation maps | WP3 substitution/subset/rival tests |
| WP1 execution state | [Preparation Record §13](Chapter_34_Preparation_Record.md#13-wp1-execution-record) | ZIP 223 | WP2 §§34.5–34.7 |

## Chapter 34 WP2 Cross-References

| WP2 object | Primary site | Required return | Deferred pressure |
|---|---|---|---|
| repeated commitments / binding-function | [§34.5](../01_blocks/04_part_iii_retype.md#34-5-repeated-commitments-as-higher-level-psi-function) | Chapter 21 binding occurrence; Chapters 22/30 | WP3 formation, threshold, failure |
| multiple integrations / integration-function | [§34.6](../01_blocks/04_part_iii_retype.md#34-6-multiple-integrations-as-higher-level-sigma-function) | Chapter 22 relation/conflict; Chapter 30 | WP3 aggregation and rivals |
| source-traceable emergence | [§34.7](../01_blocks/04_part_iii_retype.md#34-7-emergent-function) | Chapters 6, 22, 30 | WP3 threshold and Counterfactual Sensitivity |
| component roles and substitution | [§34.7](../01_blocks/04_part_iii_retype.md#34-7-emergent-function) | Chapter 22 | WP3 subset and frame pressure |
| WP2 execution state | [Preparation Record §14](Chapter_34_Preparation_Record.md#14-wp2-execution-record) | Formal-model mirror | WP3 §§34.8–34.11 |

## Chapter 34 WP3 Cross-Reference Return

- [§34.8](../01_blocks/04_part_iii_retype.md#34-8-aggregation-versus-functional-formation) applies Chapters 20–22 and 29–30 to aggregation versus formation.
- [§34.9](../01_blocks/04_part_iii_retype.md#34-9-thresholds) routes to Relevance Floor, Traceability Ceiling, subset, alternative-composite, and rival-Frame checks.
- [§34.10](../01_blocks/04_part_iii_retype.md#34-10-higher-level-function-without-authority-increase) routes to Counterfactual Sensitivity and the global authority prohibition.
- [§34.11](../01_blocks/04_part_iii_retype.md#34-11-failed-higher-level-projection) routes to canonical Reduction, Stop, Failure, Non-Capture, and exact Loss.
- [WP3 Execution Record](Chapter_34_Preparation_Record.md#15-wp3-execution-record) hands the complete family method to WP4.

## Chapter 34 Lock to Chapter 35 Preparation Links

| From | To | Relation |
|---|---|---|
| Chapter 34 completion boundary | Chapter 35 Preparation Record | higher-level-function traceability constrains profile formation |
| Chapter 35 Preparation Record | Chapter 35 WP1 | weighting, dependency, modulator, source/target, and non-type packet |
| PMS.yaml | Chapter 35 | unchanged operator order and dependencies |
| Chapter 22 | Chapter 35 | source-side occurrence load, relation, redundancy, and conflict |
| Chapter 30 | Chapter 35 | optional profile projection uses generic `PROJECT_AS` procedure |

## Chapter 35 WP1 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| family purpose and source packet | [§35.1](../01_blocks/04_part_iii_retype.md#35-1-purpose) | Chapters 1–8, 20–22, 29–30, 34 | WP2 profile formation |
| qualitative weighting dimensions | [§35.2](../01_blocks/04_part_iii_retype.md#35-2-operator-weighting) | PMS.yaml dependencies and occurrence/source evidence | WP2 role/phase stability |
| no-reordering and operation boundary | [§35.3](../01_blocks/04_part_iii_retype.md#35-3-weighting-is-not-reordering) | PMS Base and Chapter 4 | WP3 profile/type and inflation audit |
| contextual modulator and `K/L` packet | [§35.4](../01_blocks/04_part_iii_retype.md#35-4-modulator) | Chapters 5–7 and 30 | WP2 modulator variation; WP3 projection |
| WP1 execution state | [Preparation Record §13](Chapter_35_Preparation_Record.md#13-wp1-execution-record) | ZIP 227 | WP2 §§35.5–35.7 |

## Chapter 35 WP2 Cross-References

| Canonical element | Primary site | Upstream control | Next owner |
|---|---|---|---|
| modulating-profile relation | [§35.5](../01_blocks/04_part_iii_retype.md#35-5-modulating-profile) | WP1 source packet; Chapters 22 and 34 | WP3 profile/type boundary |
| bounded stability and prominence | [§35.5](../01_blocks/04_part_iii_retype.md#35-5-modulating-profile) | role/phase evidence; PMS dependencies | WP3 threshold and inflation audit |
| trajectory-form influence | [§35.6](../01_blocks/04_part_iii_retype.md#35-6-from-weighting-to-trajectory-form) | PATH Lock; Chapters 11–15 | WP3 projection and Counterfactual Test |
| modulator variation and rivals | [§35.6](../01_blocks/04_part_iii_retype.md#35-6-from-weighting-to-trajectory-form) | Chapters 6, 22, 30 | WP3 failure routes |
| source-traceable emergent profile | [§35.7](../01_blocks/04_part_iii_retype.md#35-7-emergent-functional-profile) | Chapter 34 emergence boundary | WP3 target-level projection |
| WP2 execution state | [Preparation Record §14](Chapter_35_Preparation_Record.md#14-wp2-execution-record) | ZIP 228 | WP3 §§35.8–35.12 |

## Chapter 35 WP3 Cross-References

- [Profile versus Type](../01_blocks/04_part_iii_retype.md#35-8-profile-versus-type) → Chapters 1, 5, 8, 29, 38.
- [Profile Projection](../01_blocks/04_part_iii_retype.md#35-9-profile-projection) → Chapters 29–30 and Chapter 36.
- [Profile Inflation](../01_blocks/04_part_iii_retype.md#35-10-risks-of-profile-inflation) → Admissibility Band and Chapter 39.
- [Add-On Stress Cases](../01_blocks/04_part_iii_retype.md#35-11-use-of-add-on-stress-cases) → Appendix J, without upstream authority.
- [Failed Modulation Claim](../01_blocks/04_part_iii_retype.md#35-12-failed-modulation-claim) → Stop, Failure, Non-Capture, and Chapter 40 cases.

## Chapter 35 Lock and Chapter 36 Cross-References

- [Chapter 35 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-35-completion-boundary)
- [Chapter 35 WP4 Record](Chapter_35_Preparation_Record.md#16-wp4-execution-and-provisional-lock-record)
- [Chapter 36 Preparation Gate](Chapter_36_Preparation_Record.md)
- [Chapter 36 Contract](../05_minified/Chapter_Contracts.md#chapter-36-competing-projections)
- [Chapter 36 Structure](../00_source/PMS-STRATA_Structure.md)

## Chapter 36 WP1 Cross-References

```text
Chapter 29 origin type / target function
→ Chapter 30 candidate-specific PROJECT_AS procedure
→ Chapters 31–35 family-specific burdens
→ Chapter 36 §§36.1–36.4 shared-source lock and target coordinates
→ Chapter 36 WP2 comparative criteria and indeterminacy
→ Chapter 36 WP3 non-translation, output discipline, and failure
→ Chapters 39–40 integrated alternatives and cases
```

Canonical prose: [Chapter 36 WP1](../01_blocks/04_part_iii_retype.md#chapter-36-competing-projections).  
Execution record: [Chapter 36 WP1 Execution Record](Chapter_36_Preparation_Record.md#chapter-36-wp1-execution-record).

## Chapter 36 WP2 Cross-References

```text
Chapter 36 WP1 comparison-entry grammar
→ §36.5 qualitative criteria and exact Loss comparison
→ §36.6 discriminative performance and no-projection pressure
→ §36.7 co-validity, context-dependence, partial preference,
  underdetermination, and non-comparability
→ Chapter 36 WP3 non-translation, tribunal boundary,
  comparison record, integrated counterfactual and failure discipline
```

Canonical prose: [Chapter 36 WP2](../01_blocks/04_part_iii_retype.md#36-5-comparative-criteria).  
Execution record: [Chapter 36 WP2 Execution Record](Chapter_36_Preparation_Record.md#chapter-36-wp2-execution-record).

## Chapter 36 WP3 Cross-References

```text
Chapter 36 WP1 comparison-entry grammar
→ Chapter 36 WP2 qualitative comparison and indeterminacy
→ §36.8 non-translation / non-contradiction / non-comparability
→ §36.9 non-tribunal integrated counterfactual and failure localization
→ §36.10 Projection Comparison Record
→ Chapter 36 WP4 integrated lock audit
→ Chapter 37 projection / analogy / label-substitution boundary
```

Canonical prose: [Chapter 36 WP3](../01_blocks/04_part_iii_retype.md#36-8-non-translation).  
Execution record: [Chapter 36 WP3 Execution Record](Chapter_36_Preparation_Record.md#chapter-36-wp3-execution-record).

## Chapter 36 Lock and Chapter 37 Cross-References

- [Chapter 36 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-36-completion-boundary)
- [Chapter 36 WP4 execution record](Chapter_36_Preparation_Record.md#chapter-36-wp4-execution-record)
- [Chapter 37 Preparation Gate](Chapter_37_Preparation_Record.md)
- Chapter 37 WP1 will begin at §§37.1–37.4.

## Chapter 37 WP1 Cross-Reference Route

```text
Chapter 29 origin type / target function
→ Chapter 30 complete PROJECT_AS burden
→ Chapters 31–35 family-specific projection burdens
→ Chapter 36 candidate comparison
→ Chapter 37 WP1 triad and cross-domain mapping entry
→ Chapter 37 WP2 mapping-status and substitution tests
```

Primary links:

- [§37.1 Why the Distinction Matters](../01_blocks/04_part_iii_retype.md#37-1-why-the-distinction-matters)
- [§37.2 Valid Functional Projection](../01_blocks/04_part_iii_retype.md#37-2-valid-functional-projection)
- [§37.3 Structural Analogy](../01_blocks/04_part_iii_retype.md#37-3-structural-analogy)
- [§37.4 Cross-Domain Projection](../01_blocks/04_part_iii_retype.md#37-4-cross-domain-projection)
- [WP1 Execution Record](Chapter_37_Preparation_Record.md#chapter-37-wp1-execution-record)

Chapter 38 later receives invalid type-jump and level-mixing cases; Chapter 40 later receives executed cases and confusion cases.

## Chapter 37 WP2 Cross-Reference Route

```text
§37.1 triad
→ §37.2 complete PROJECT_AS burden
→ §37.3 bounded analogy
→ §37.4 cross-domain coordinates and residuals
→ §37.5 symbolic/formal/executable separation
→ §37.6 terminal analogy
→ §37.7 partial analogy
→ §37.8 substitution markers and counterfactual mapping test
→ WP3 drift, translation, integrated stress, output, and failure
```

Primary links:

- [§37.5 Symbolic, Formal, and Executable Mapping](../01_blocks/04_part_iii_retype.md#37-5-symbolic-formal-and-executable-mapping)
- [§37.6 Analogy as a Legitimate Terminal Status](../01_blocks/04_part_iii_retype.md#37-6-analogy-as-a-legitimate-terminal-status)
- [§37.7 Partial Analogy](../01_blocks/04_part_iii_retype.md#37-7-partial-analogy)
- [§37.8 Label Substitution and Counterfactual Mapping Test](../01_blocks/04_part_iii_retype.md#37-8-label-substitution-and-counterfactual-mapping-test)
- [WP2 Execution Record](Chapter_37_Preparation_Record.md#chapter-37-wp2-execution-record)

## Chapter 37 WP3 Cross-Reference Route

```text
Chapter 37 WP1 triad and source/residual lock
→ Chapter 37 WP2 mapping statuses, terminal analogy, substitution markers and counterfactual test
→ §37.9 analogy drift
→ §37.10 translation breadth
→ §37.11 integrated Analogy Stress Test
→ §37.12 output, failure, Non-Capture and authority boundaries
→ Chapter 37 WP4 lock audit
```

Key links:

- [§37.9 Analogy Drift](../01_blocks/04_part_iii_retype.md#37-9-analogy-drift)
- [§37.10 Translation Breadth](../01_blocks/04_part_iii_retype.md#37-10-translation-breadth)
- [§37.11 Integrated Analogy Stress Test](../01_blocks/04_part_iii_retype.md#37-11-integrated-analogy-stress-test)
- [§37.12 Output, Failure, Non-Capture, and Authority Boundaries](../01_blocks/04_part_iii_retype.md#37-12-output-failure-non-capture-and-authority-boundaries)
- [WP3 Execution Record](Chapter_37_Preparation_Record.md#chapter-37-wp3-execution-record)

## Chapter 37 Lock → Chapter 38 Preparation Route

```text
Chapter 37 triad and semantic-preservation discipline
→ Chapter 37 provisional family-method lock
→ Chapter 38 invalid type/context/level/granularity taxonomy
→ Chapter 39 RETYPE Boundary Conditions
→ Chapter 40 cases and integrated local audit
```

Key links:

- [Chapter 37 integrated lock audit](../01_blocks/04_part_iii_retype.md#chapter-37-integrated-family-method-lock-audit)
- [Chapter 37 WP4 Execution Record](Chapter_37_Preparation_Record.md#chapter-37-wp4-execution-record)
- [Chapter 38 Preparation Record](Chapter_38_Preparation_Record.md)

## Chapter 38 WP1 Cross-References

```text
Chapter 29 origin type / target function
→ Chapter 30 complete PROJECT_AS procedure
→ Chapter 37 projection / analogy / substitution triad
→ Chapter 38 WP1 invalid type jump, missing context, and bounded metaphor
→ Chapter 38 WP2 level, granularity, rescue, person, and primitive errors
```

Canonical site: [Chapter 38 WP1](../01_blocks/04_part_iii_retype.md#38-1-invalid-type-jump).  
Execution site: [Chapter 38 WP1 Execution Record](Chapter_38_Preparation_Record.md#chapter-38-wp1-execution-record).

## Chapter 38 WP2 Cross-Reference Route

```text
§38.1 origin-type replacement
→ §38.2 source type / target function continuity
→ §38.3 target-coordinate completeness
→ §38.4 bounded metaphor and ambiguity
→ §38.5 cross-level relation versus mixing
→ §38.6 multi-granular relation versus direct transfer
→ §38.7 failure preservation and new-claim burden
→ §38.8 person/group boundary
→ §38.9 primitive and dual-record boundary
→ WP3 scope, time, Loss, invalid-record, and output discipline
```

Primary links:

- [§38.5 Unmarked Level Mixing](../01_blocks/04_part_iii_retype.md#38-5-unmarked-level-mixing)
- [§38.6 Granularity Mixing](../01_blocks/04_part_iii_retype.md#38-6-granularity-mixing)
- [§38.7 Projection as Rescue Operation](../01_blocks/04_part_iii_retype.md#38-7-projection-as-rescue-operation)
- [§38.8 Macrofunction Attributed to a Person](../01_blocks/04_part_iii_retype.md#38-8-macrofunction-attributed-to-a-person)
- [§38.9 New Primitive by Projection](../01_blocks/04_part_iii_retype.md#38-9-new-primitive-by-projection)
- [WP2 Execution Record](Chapter_38_Preparation_Record.md#chapter-38-wp2-execution-record)

## Chapter 38 WP3 Cross-References

- [§38.10 Scope Inflation](../01_blocks/04_part_iii_retype.md#38-10-scope-inflation)
- [§38.11 Temporal Flattening](../01_blocks/04_part_iii_retype.md#38-11-temporal-flattening)
- [§38.12 Projection without Loss](../01_blocks/04_part_iii_retype.md#38-12-projection-without-loss)
- [§38.13 Invalid Projection Record](../01_blocks/04_part_iii_retype.md#38-13-invalid-projection-record)
- [WP3 Completion Boundary](../01_blocks/04_part_iii_retype.md#chapter-38-wp3-completion-boundary)
- [WP3 Execution Record](Chapter_38_Preparation_Record.md#chapter-38-wp3-execution-record)
- [Chapter 39 Contract](../05_minified/Chapter_Contracts.md#chapter-39-retype-boundary-conditions)



<a id="chapter-38-lock-and-chapter-39-preparation-cross-reference-sync"></a>

## Chapter 38 Lock → Chapter 39 Preparation Route

```text
Chapter 30 complete PROJECT_AS procedure
→ Chapters 31–37 family and analogy boundaries
→ Chapter 38 invalidity taxonomy provisionally locked
→ Chapter 39 local RETYPE boundary gate
→ Chapter 40 executed cases and RETYPE lock
```

Primary sites:

- [Chapter 38 completion boundary](../01_blocks/04_part_iii_retype.md#chapter-38-completion-boundary)
- [Chapter 38 Preparation Record](Chapter_38_Preparation_Record.md#chapter-38-wp4-execution-record)
- [Chapter 39 Preparation Record](Chapter_39_Preparation_Record.md)
- [Chapter 39 Contract](../05_minified/Chapter_Contracts.md#chapter-39-retype-boundary-conditions)

Chapter 39 references Chapter 6 for the Band, Chapter 30 for the operation record, Chapter 37 for analogy-only, and Chapter 38 for invalidity and failure continuity. It does not redefine those sites.

<a id="chapter-39-wp1-cross-reference-sync"></a>

## Chapter 39 WP1 Cross-References

```text
Chapter 6 general Admissibility Band
→ Chapter 30 complete PROJECT_AS occurrence
→ Chapter 37 analogy/substitution boundary
→ Chapter 38 invalidity localization
→ Chapter 39 §§39.1–39.4 lower/upper RETYPE boundary entry
→ Chapter 39 WP2 Source Trace, Type, Context, and Counterfactual gates
```

Execution record: [Chapter 39 Preparation Record §14](Chapter_39_Preparation_Record.md#chapter-39-wp1-execution-record).

<a id="chapter-39-wp2-cross-reference-sync"></a>

## Chapter 39 WP2 Cross-References

```text
Chapter 6 non-compensatory Admissibility Band
→ Chapter 30 PROJECT_AS occurrence requirements
→ Chapter 38 Type, Context, Level, Loss, and failure localization
→ Chapter 39 WP1 lower/upper RETYPE boundaries
→ Chapter 39 WP2 Source Trace, Type, Context, and Counterfactual gates
→ Chapter 39 WP3 alternatives, analogy, elasticity, Stop, Non-Capture, and terminal gate
```

Execution record: [Chapter 39 Preparation Record §15](Chapter_39_Preparation_Record.md#chapter-39-wp2-execution-record).

<a id="chapter-39-wp3-cross-reference-sync"></a>

## Chapter 39 WP3 Cross-References

```text
Chapter 39 WP1 floor/ceiling
→ WP2 trace/type/context/counterfactual gates
→ WP3 alternatives/analogy/elasticity/Stop/Non-Capture
→ complete RETYPE Admissibility Test
→ WP4 lock audit and Chapter 40 Preparation Gate
```

<a id="chapter-39-lock-and-chapter-40-preparation-cross-reference-sync"></a>

## Chapter 39 Lock to Chapter 40 Case-Audit Route

```text
Chapter 29 → functional projection
Chapter 30 → PROJECT_AS record
Chapters 31–35 → projection families
Chapter 36 → projection comparison
Chapter 37 → projection / analogy / substitution
Chapter 38 → invalidity taxonomy
Chapter 39 → local RETYPE boundary gate, provisionally locked
Chapter 40 → cases, countercases, confusion cases, local audit, output mapping, lock decision
Chapter 53 → later integrated STRATA audit
```

Primary preparation record: [Chapter 40 Preparation Record](Chapter_40_Preparation_Record.md).

## Chapter 40 WP1 Positive-Case Route

| Chapter-40 section | Family source | Primary locked method | Open burden |
| --- | --- | --- | --- |
| [§40.1](../01_blocks/04_part_iii_retype.md#40-1-case-architecture) | all RETYPE cases | Chapters 29–30 and 39 | artifact, audit, mapping |
| [§40.2](../01_blocks/04_part_iii_retype.md#40-2-case-1-trajectory-as-frame-function) | Trajectory | Chapter 31 | non-deterministic frame-function |
| [§40.3](../01_blocks/04_part_iii_retype.md#40-3-case-2-trajectory-as-macro-event) | extended Trajectory | Chapter 32 | anti-punctualization |
| [§40.4](../01_blocks/04_part_iii_retype.md#40-4-case-3-recurrent-trajectory-form-as-attractor-function) | recurrent form | Chapter 33 | stabilizing load beyond similarity |
| [§40.5](../01_blocks/04_part_iii_retype.md#40-5-case-4-distributed-local-asymmetries-as-higher-level-function) | relational composite | Chapter 34 | formation beyond aggregation |
| [§40.6](../01_blocks/04_part_iii_retype.md#40-6-case-5-operator-weighting-profile-as-modulating-function) | weighting profile | Chapter 35 | dependency and person boundary |
| [§40.7](../01_blocks/04_part_iii_retype.md#40-7-case-6-two-compatible-projections) | stable shared source | Chapter 36 | separate coordinates and no merger |
| [§40.8](../01_blocks/04_part_iii_retype.md#40-8-case-7-two-competing-projections) | stable shared source | Chapter 36 | discrimination, Loss, provisionality, Non-Capture |

<a id="chapter-40-wp2-cross-reference-sync"></a>

## Chapter 40 WP2 Cross-References

```text
§40.9 Origin-Type Replacement
→ Chapters 29, 30, 38.1–38.2, 39.6

§40.10 Projection without Context
→ Chapters 30, 38.3, 39.7

§40.11 Label Substitution
→ Chapters 37.8, 38, 39.1–39.5

§40.12 Analogy Presented as Projection
→ Chapter 37 and Appendix K

§40.13 Macrofunction from Mere Aggregation
→ Chapters 34.8–34.9 and 38

§40.14 Projection as Claim Rescue
→ Chapters 38.7 and 39.11–39.12

§40.15 Person-Level Type Jump
→ Chapters 35.8, 38.8, and governance non-authority boundary
```

<a id="chapter-40-wp3-cross-reference-sync"></a>

## Chapter 40 WP3 Cross-References

```text
§40.16 RETYPE or SUB?
→ Chapters 18–26, 29–30, and Chapter 26 boundary

§40.17 RETYPE or COMPOSE?
→ Chapters 22, 29–30, and 34

§40.18 Projection or Recontextualization?
→ PMS Φ and Chapters 29, 30, and 38

§40.19 Attractor-Function or Repeated Similarity?
→ Chapters 33, 37, and 39

§40.20 Modulator or New Operator?
→ Chapters 35 and 38

§40.21 Projection or Structural Analogy?
→ Chapters 37 and 39 and Appendix K
```


## Chapter 40 Completion → Part IV LIMITS Route

```text
Chapters 29–39
→ provisionally locked RETYPE methods

Chapter 40
→ complete Layer-1 case architecture
→ thirty-two-question audit specification
→ canonical mapping boundary
→ bounded provisional Part-III lock
→ artifact-complete lock mandatory_stop

Chapter 41
→ constitutive LIMITS rationale
→ recursive risk and authority-drift architecture
```

Primary sites:

- [Chapter 40 Local Audit](../01_blocks/04_part_iii_retype.md#40-22-retype-local-audit)
- [Chapter 40 Output Classes](../01_blocks/04_part_iii_retype.md#40-23-retype-output-classes)
- [Chapter 40 Closing Statement](../01_blocks/04_part_iii_retype.md#40-24-retype-closing-statement)
- [Chapter 41 Preparation Record](Chapter_41_Preparation_Record.md)

The LIMITS handoff preserves the Chapter-40 artifact Stop and does not convert it into a completed RETYPE lock.

## PMS operator re-anchoring — Chapters 29–35

| Control point | Canonical location |
|---|---|
| conceptual source integrity and Functional Continuity | Chapters 29.1, 29.6–29.7 |
| generic `PROJECT_AS` occurrence route | Chapters 30.4, 30.7–30.8, 30.10, 30.13 |
| bounded Frame work and historical carriers | Chapter 31 |
| operator-structured phases and Macro-Event compression | Chapter 32 |
| recurrent occurrence relations and bounded Attractor work | Chapter 33 |
| component occurrence topology and emergence | Chapter 34 |
| invoked-occurrence scope and label-removal test | Chapter 35 |

Canonical block: [`01_blocks/04_part_iii_retype.md`](../01_blocks/04_part_iii_retype.md).
