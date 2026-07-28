# PMS-STRATA Appendix Production Map

**Status:** Appendices A–L substantive bounded provisional completion; Appendices M–N preflight-ready  
**Authority:** production-routing and ownership map only; no independent theory authority  
**Source basis:** `00_source/PMS-STRATA_Structure.md`, `05_minified/Block_Contracts.md`, `05_minified/Chapter_Contracts.md`, current Formal Model, Reference Kernel, and paired Case corpus  

```text
14 Appendices: A–N
14 Appendix files: present
Appendices A–L substantive content: complete
Appendices M–N substantive content: pending
contract objects parsed: 62
appendix-directed migration clauses: 154
non-appendix/reference-directed clauses: 24
new theory introduced: 0
```

## 1. Governing production rule

```text
Appendix
→ consolidates, operationalizes, indexes, or templates existing content

Appendix
≠ competing definition site
≠ new operation
≠ new output class
≠ new PMS primitive
≠ higher authority
```

All Appendix claims must trace upward to PMS Base, Structure, canonical Blocks, Minified Controls, or the Formal Model owner of the relevant syntax. Cases may illustrate and test; they do not originate theory.

## 2. Production order

```text
A → B → C → D → E → F → G → H → I → J → K → L → M → N
```

The order is functional rather than hierarchical: definitions and notation precede schemas; shared schema precedes operation templates; admissibility tests precede pattern and confusion catalogues; the case index precedes the integrated audit template.

## 3. Appendix ownership matrix

| Appendix | Title | Contract migrations | Canonical owners / inputs | Required output | Prohibited drift |
|---|---|---:|---|---|---|
| A | Core Definitions — substantive complete | 4 | `01_blocks/01_foundations.md`<br>`04_reference/Glossary.md`<br>`04_reference/Non_Equivalence_Index.md`<br>`07_model/Operation_Registry.yaml`<br>`07_model/Output_Classes.yaml` | definition table<br>primary definition location<br>non-equivalences<br>authority boundary | new definitions<br>new PMS primitives<br>person typing |
| B | Formal Notation — substantive complete | 15 | `01_blocks/01_foundations.md`<br>`05_minified/PMS_STRATA_Operation_Signatures_Minified.md`<br>`04_reference/Transformation_Operation_Index.md`<br>`07_model/Operation_Registry.yaml`<br>`07_model/Transformation_Record.schema.json` | typed object notation<br>frame/granularity/level notation<br>operation-occurrence notation<br>chain notation | proof of completeness<br>numerical scoring<br>new semantics |
| C | Shared Transformation Record Schema — substantive complete | 6 | `01_blocks/01_foundations.md`<br>`05_minified/Chapter_Contracts.md`<br>`07_model/Transformation_Record.schema.json`<br>`07_model/PMS-STRATA.yaml` | field groups<br>required declarations<br>loss fields<br>route/output separation | substantive truth automation<br>new fields not in schema<br>merged chain records |
| D | COMPOSE Record Template — substantive complete | 5 | `01_blocks/02_part_i_path.md`<br>`05_minified/PMS_STRATA_Operation_Signatures_Minified.md`<br>`07_model/Operation_Registry.yaml`<br>`07_model/Transformation_Record.schema.json` | source multiplicity/order<br>constitutive relations<br>selection<br>composite identity | lossless inversion<br>automatic trajectory status<br>automatic higher authority |
| E | DECOMPOSE Record Template — substantive complete | 5 | `01_blocks/03_part_ii_sub.md`<br>`05_minified/PMS_STRATA_Operation_Signatures_Minified.md`<br>`07_model/Operation_Registry.yaml`<br>`07_model/Transformation_Record.schema.json` | same reference object<br>resolution change<br>reconstructed relations<br>residual binding | operator-type decomposition<br>finer-is-truer rule<br>hidden RETYPE |
| F | PROJECT_AS Record Template — substantive complete | 7 | `01_blocks/04_part_iii_retype.md`<br>`05_minified/PMS_STRATA_Operation_Signatures_Minified.md`<br>`07_model/Operation_Registry.yaml`<br>`07_model/Transformation_Record.schema.json` | origin type<br>target function<br>target context<br>counterfactual sensitivity | origin-type replacement<br>label substitution<br>analogy as projection |
| G | Admissibility Band Tests — substantive complete | 16 | `01_blocks/01_foundations.md`<br>`01_blocks/05_part_iv_limits.md`<br>`05_minified/PMS_STRATA_Admissibility_Band_Minified.md`<br>`07_model/Admissibility_Rules.yaml`<br>`07_model/Output_Classes.yaml` | PraxisPurchase<br>TraceableLoad<br>TypeIntegrity<br>continuity | numeric scoring<br>compensatory weighting<br>automatic class ranking |
| H | Valid and Invalid Transformation Patterns — substantive complete | 26 | `01_blocks/01_foundations.md`<br>`04_reference/Non_Equivalence_Index.md`<br>`07_model/Operation_Registry.yaml`<br>`07_model/Output_Classes.yaml` | positive patterns<br>failure patterns<br>claim reduction patterns<br>stop patterns | case ranking<br>universal inference from examples<br>new theory |
| I | Boundary and Confusion Cases — substantive complete | 30 | `01_blocks/01_foundations.md`<br>`01_blocks/05_part_iv_limits.md`<br>`04_reference/Output_Class_Index.md`<br>`07_model/Boundary_Decision_Tree.yaml`<br>`07_model/Output_Classes.yaml` | operation collisions<br>output-class boundaries<br>same-source contrasts where available<br>stop versus failure versus non-capture | class hierarchy<br>first-match-wins<br>score-based routing |
| J | Optional Operator-Weighting and Trajectory Stress Tests — substantive complete | 10 | `01_blocks/02_part_i_path.md`<br>`01_blocks/04_part_iii_retype.md`<br>`04_reference/Operator_Index.md`<br>`07_model/Operation_Registry.yaml` | weighting as configuration profile<br>trajectory/path distinctions<br>historical alternative status<br>false-trajectory contrasts | new operators<br>renamed Δ–Ψ dependencies<br>formal weight scoring |
| K | Cross-Domain Projection and Analogy Stress Tests — substantive complete | 3 | `01_blocks/04_part_iii_retype.md`<br>`04_reference/Non_Equivalence_Index.md`<br>`07_model/Operation_Registry.yaml`<br>`07_model/Boundary_Decision_Tree.yaml` | source-sensitive projection<br>analogy-only route<br>label-substitution failure<br>contextual boundedness | analogy as proof<br>domain authority transfer<br>origin-type replacement |
| L | Non-Operator Remainders and Limits of Decomposition — substantive complete | 5 | `01_blocks/03_part_ii_sub.md`<br>`01_blocks/05_part_iv_limits.md`<br>`04_reference/Non_Equivalence_Index.md`<br>`07_model/Admissibility_Rules.yaml`<br>`07_model/Output_Classes.yaml` | non-operator remainder<br>residual relation<br>source-function return<br>granularity stop | operator-type decomposition<br>unbounded microdetail<br>non-capture as weak-claim shield |
| M | Case and Countercase Index — substantive complete | 13 | `03_cases/Case_Index.md`<br>`03_cases/Case_Index.yaml`<br>`03_cases/Case_Artifact_Pairing.csv`<br>`07_model/Output_Classes.yaml` | case class<br>operation<br>output class<br>source/target summary | new adjudication<br>case ranking<br>duplicate full case narratives |
| N | Integrated STRATA Audit Template — substantive complete | 9 | `01_blocks/05_part_iv_limits.md`<br>`04_reference/Audit_Checklist.md`<br>`07_model/Admissibility_Rules.yaml`<br>`07_model/Boundary_Decision_Tree.yaml` | twelve audit stages<br>candidate generation<br>collision adjudication<br>output mapping | audit stage 13<br>automatic substantive finding<br>merged local results |

## 4. Detailed appendix contracts

### Appendix A — Core Definitions

**Current production status:** substantive bounded provisional completion; primary chapter ownership and authority limits preserved.


**Target file:** `02_appendices/Appendix_A_Core_Definitions.md`  
**Purpose:** Consolidate canonical definitions and protected distinctions without becoming a competing definition site.  
**Contributing contract migrations:** 4 from `1, 10, 18, 29`

**Canonical owners / source inputs**

- `01_blocks/01_foundations.md`
- `04_reference/Glossary.md`
- `04_reference/Non_Equivalence_Index.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`
- `07_model/Output_Classes.yaml`

**Must include**

- definition table
- primary definition location
- non-equivalences
- authority boundary

**Must not introduce**

- new definitions
- new PMS primitives
- person typing
- new operation

### Appendix B — Formal Notation

**Current production status:** substantive bounded provisional completion; prose precedence, non-scoring, non-ontological, and non-completeness boundaries preserved.

**Target file:** `02_appendices/Appendix_B_Formal_Notation.md`  
**Purpose:** Provide notation for objects, coordinates, occurrences, chains, loss, and admissibility while preserving prose precedence.  
**Contributing contract migrations:** 15 from `1, 2, 3, 5, 9, 11, 19, 23, 29, 30, 32, 42, 49, 54, FM-TERMINOLOGY-NOTATION`

**Canonical owners / source inputs**

- `01_blocks/01_foundations.md`
- `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`
- `04_reference/Transformation_Operation_Index.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`
- `07_model/Transformation_Record.schema.json`

**Must include**

- typed object notation
- frame/granularity/level notation
- operation-occurrence notation
- chain notation
- loss notation
- status of formulas

**Must not introduce**

- proof of completeness
- numerical scoring
- new semantics
- category-theoretic claims not already defined

### Appendix C — Shared Transformation Record Schema

**Current production status:** substantive bounded provisional completion; Chapter-7 semantic ownership, schema syntax ownership, route/status separation, and non-authority boundary preserved.

**Target file:** `02_appendices/Appendix_C_Shared_Transformation_Record_Schema.md`  
**Purpose:** Explain the shared record contract and its relation to the formal schema without duplicating or overriding the schema owner.  
**Contributing contract migrations:** 6 from `7, 47, 48, 49, 51, 52`

**Canonical owners / source inputs**

- `01_blocks/01_foundations.md`
- `05_minified/Chapter_Contracts.md`

**Formal-model inputs**

- `07_model/Transformation_Record.schema.json`
- `07_model/PMS-STRATA.yaml`

**Case inputs**

- `03_cases/Case_Artifact_Pairing.csv`

**Must include**

- field groups
- required declarations
- loss fields
- route/output separation
- schema-authority boundary

**Must not introduce**

- substantive truth automation
- new fields not in schema
- merged chain records

**Assigned downstream template outputs**

- `03_cases/templates/case_template.md`

### Appendix D — COMPOSE Record Template

**Production status:** substantive bounded provisional completion  

**Target file:** `02_appendices/Appendix_D_COMPOSE_Record_Template.md`  
**Purpose:** Provide a usable COMPOSE occurrence template derived from the shared schema and operation registry.  
**Contributing contract migrations:** 5 from `7, 9, 10, 14, 15`

**Canonical owners / source inputs**

- `01_blocks/02_part_i_path.md`
- `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`
- `07_model/Transformation_Record.schema.json`

**Case inputs**

- `03_cases/yaml/C17-LINEAR-01_Simple_Linear_Path.yaml`
- `03_cases/packages/C54-CD1_COMPOSE_to_DECOMPOSE_Non_Invertibility_Chain.md`

**Must include**

- source multiplicity/order
- constitutive relations
- selection
- composite identity
- loss
- no automatic target function

**Must not introduce**

- lossless inversion
- automatic trajectory status
- automatic higher authority

**Assigned downstream template outputs**

- `03_cases/templates/compose_case_template.yaml`

### Appendix E — DECOMPOSE Record Template

**Production status:** substantive bounded provisional completion  

**Target file:** `02_appendices/Appendix_E_DECOMPOSE_Record_Template.md`  
**Purpose:** Provide a usable DECOMPOSE occurrence template derived from the shared schema and operation registry.  
**Contributing contract migrations:** 5 from `7, 18, 20, 22, 23`

**Canonical owners / source inputs**

- `01_blocks/03_part_ii_sub.md`
- `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`
- `07_model/Transformation_Record.schema.json`

**Case inputs**

- `03_cases/yaml/C28-TRAJECTORY-01_Admissible_Trajectory_Decomposition.yaml`
- `03_cases/yaml/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.yaml`

**Must include**

- same reference object
- resolution change
- reconstructed relations
- residual binding
- loss
- stop/non-capture

**Must not introduce**

- operator-type decomposition
- finer-is-truer rule
- hidden RETYPE
- lossless inverse

**Assigned downstream template outputs**

- `03_cases/templates/decompose_case_template.yaml`

### Appendix F — PROJECT_AS Record Template

**Production status:** substantive bounded provisional completion  

**Target file:** `02_appendices/Appendix_F_PROJECT_AS_Record_Template.md`  
**Purpose:** Provide a usable PROJECT_AS occurrence template derived from the shared schema and operation registry.  
**Contributing contract migrations:** 7 from `5, 7, 30, 31, 32, 34, 36`

**Canonical owners / source inputs**

- `01_blocks/04_part_iii_retype.md`
- `05_minified/PMS_STRATA_Operation_Signatures_Minified.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`
- `07_model/Transformation_Record.schema.json`

**Case inputs**

- `03_cases/yaml/C40-P1_Trajectory_as_Bounded_Frame_Function.yaml`
- `03_cases/yaml/C38-N1_PROJECT_AS_Origin_Type_Replacement_Failure.yaml`

**Must include**

- origin type
- target function
- target context
- counterfactual sensitivity
- contextual boundedness
- type integrity

**Must not introduce**

- origin-type replacement
- label substitution
- analogy as projection
- authority inheritance

**Assigned downstream template outputs**

- `03_cases/templates/project_as_case_template.yaml`

### Appendix G — Admissibility Band Tests

**Production status:** substantive bounded provisional completion; non-compensation, non-scoring, local-judgment, and routing-separation boundaries preserved.  

**Target file:** `02_appendices/Appendix_G_Admissibility_Band_Tests.md`  
**Purpose:** Operationalize lower/upper band tests and their non-compensatory relation without replacing local judgment.  
**Contributing contract migrations:** 16 from `6, 12, 13, 16, 19, 25, 27, 30, 33, 39, 43, 44, 45, 46, 51, 53`

**Canonical owners / source inputs**

- `01_blocks/01_foundations.md`
- `01_blocks/05_part_iv_limits.md`
- `05_minified/PMS_STRATA_Admissibility_Band_Minified.md`

**Formal-model inputs**

- `07_model/Admissibility_Rules.yaml`
- `07_model/Output_Classes.yaml`
- `07_model/Boundary_Decision_Tree.yaml`

**Case inputs**

- `03_cases/yaml/C28-OVERFINE-01_Overfine_Analysis_below_the_Relevance_Floor.yaml`
- `03_cases/yaml/C17-MACRO-01_Macro_Label_without_Traceable_Path.yaml`

**Must include**

- PraxisPurchase
- TraceableLoad
- TypeIntegrity
- continuity
- counterfactual sensitivity
- source/claim ceilings
- stop/non-capture

**Must not introduce**

- numeric scoring
- compensatory weighting
- automatic class ranking
- truth proof

### Appendix H — Valid and Invalid Transformation Patterns

**Production status:** substantive bounded provisional completion; pattern-as-aid, no-case-ranking, and no-automatic-routing boundaries preserved.  

**Target file:** `02_appendices/Appendix_H_Valid_and_Invalid_Transformation_Patterns.md`  
**Purpose:** Collect recurring admissible and invalid patterns without creating new operations or classes.  
**Contributing contract migrations:** 26 from `0, 1, 4, 6, 8, 15, 16, 20, 25, 26, 27, 29, 30, 34, 37, 38, 39, 41, 42, 44, 45, 46, 47, 48, 50, 56`

**Canonical owners / source inputs**

- `01_blocks/01_foundations.md`
- `04_reference/Non_Equivalence_Index.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`
- `07_model/Output_Classes.yaml`

**Case inputs**

- `03_cases/Case_Index.md`
- `03_cases/packages/*`

**Must include**

- positive patterns
- failure patterns
- claim reduction patterns
- stop patterns
- non-capture contrast

**Must not introduce**

- case ranking
- universal inference from examples
- new theory

**Assigned downstream template outputs**

- `03_cases/templates/countercase_template.md`

### Appendix I — Boundary and Confusion Cases

**Current production status:** substantive bounded provisional completion; all fourteen registered collision families, operation/object confusions, and Stop/Failure/Non-Capture boundaries covered.

**Target file:** `02_appendices/Appendix_I_Boundary_and_Confusion_Cases.md`  
**Purpose:** Consolidate load-bearing collision boundaries and confusion routes across operations and output classes.  
**Contributing contract migrations:** 30 from `0, 2, 4, 6, 8, 9, 13, 14, 16, 19, 23, 24, 26, 29, 31, 32, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52`

**Canonical owners / source inputs**

- `01_blocks/01_foundations.md`
- `01_blocks/05_part_iv_limits.md`
- `04_reference/Output_Class_Index.md`

**Formal-model inputs**

- `07_model/Boundary_Decision_Tree.yaml`
- `07_model/Output_Classes.yaml`

**Case inputs**

- `03_cases/Case_Index.md`
- `03_cases/markdown/*`

**Must include**

- operation collisions
- output-class boundaries
- same-source contrasts where available
- stop versus failure versus non-capture

**Must not introduce**

- class hierarchy
- first-match-wins
- score-based routing

**Assigned downstream template outputs**

- `03_cases/templates/confusion_case_template.md`

### Appendix J — Optional Operator-Weighting and Trajectory Stress Tests

**Current production status:** substantive bounded provisional completion; operator-occurrence profile, Trajectory, historical-alternative, false-Trajectory, and Reader-rendering boundaries preserved.

**Target file:** `02_appendices/Appendix_J_Operator_Weighting_and_Trajectory_Stress_Tests.md`  
**Purpose:** Provide optional stress vectors for weighting profiles, trajectories, branches, alternatives, and path dependence.  
**Contributing contract migrations:** 10 from `3, 11, 12, 14, 21, 22, 24, 33, 34, 35`

**Canonical owners / source inputs**

- `01_blocks/02_part_i_path.md`
- `01_blocks/04_part_iii_retype.md`
- `04_reference/Operator_Index.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`

**Case inputs**

- `03_cases/markdown/C17-*.md`
- `03_cases/packages/C35-A1_Operator_Weighting_Profile_and_RETYPE_Type_Boundary.md`

**Must include**

- weighting as configuration profile
- trajectory/path distinctions
- historical alternative status
- false-trajectory contrasts

**Must not introduce**

- new operators
- renamed Δ–Ψ dependencies
- formal weight scoring
- historical branch invention

### Appendix K — Cross-Domain Projection and Analogy Stress Tests

**Current production status:** substantive bounded provisional completion; projection/analogy/substitution and cross-domain non-capture boundaries preserved.

**Target file:** `02_appendices/Appendix_K_Cross_Domain_Projection_and_Analogy_Stress_Tests.md`  
**Purpose:** Stress-test PROJECT_AS against analogy, recontextualization, and cross-domain label transfer.  
**Contributing contract migrations:** 3 from `8, 37, 38`

**Canonical owners / source inputs**

- `01_blocks/04_part_iii_retype.md`
- `04_reference/Non_Equivalence_Index.md`

**Formal-model inputs**

- `07_model/Operation_Registry.yaml`
- `07_model/Boundary_Decision_Tree.yaml`

**Case inputs**

- `03_cases/yaml/C40-X6_Projection_versus_Structural_Analogy.yaml`
- `03_cases/yaml/C38-X3_PROJECT_AS_or_Recontextualization_Failure.yaml`

**Must include**

- source-sensitive projection
- analogy-only route
- label-substitution failure
- contextual boundedness

**Must not introduce**

- analogy as proof
- domain authority transfer
- origin-type replacement

### Appendix L — Non-Operator Remainders and Limits of Decomposition

**Current production status:** substantive bounded provisional completion; remainder, decomposition-limit, Stop, and genuine Non-Capture boundaries preserved.

**Target file:** `02_appendices/Appendix_L_Non_Operator_Remainders_and_Decomposition_Limits.md`  
**Purpose:** Consolidate remainders, residual binding, source-function limits, stop, and genuine non-capture under DECOMPOSE.  
**Contributing contract migrations:** 5 from `18, 22, 25, 27, 52`

**Canonical owners / source inputs**

- `01_blocks/03_part_ii_sub.md`
- `01_blocks/05_part_iv_limits.md`
- `04_reference/Non_Equivalence_Index.md`

**Formal-model inputs**

- `07_model/Admissibility_Rules.yaml`
- `07_model/Output_Classes.yaml`

**Case inputs**

- `03_cases/yaml/C28-FRAGMENT-01_Fragmentation_without_Source_Function.yaml`
- `03_cases/yaml/C52-NC1_Competing_Decompositions_of_a_Compressed_Handoff_Occurrence.yaml`

**Must include**

- non-operator remainder
- residual relation
- source-function return
- granularity stop
- genuine non-capture

**Must not introduce**

- operator-type decomposition
- unbounded microdetail
- non-capture as weak-claim shield

**Assigned downstream template outputs**

- `03_cases/templates/non_capture_case_template.yaml`

### Appendix M — Case and Countercase Index

**Production status:** substantive bounded provisional completion  

**Target file:** `02_appendices/Appendix_M_Case_and_Countercase_Index.md`  
**Purpose:** Provide a publishable, human-readable index into paired Records and package narratives.  
**Contributing contract migrations:** 13 from `10, 11, 12, 13, 15, 17, 20, 21, 24, 28, 36, 40, 53`

**Canonical owners / source inputs**

- `03_cases/Case_Index.md`
- `03_cases/Case_Index.yaml`
- `03_cases/Case_Artifact_Pairing.csv`

**Formal-model inputs**

- `07_model/Output_Classes.yaml`

**Case inputs**

- `03_cases/markdown/*`
- `03_cases/yaml/*`
- `03_cases/packages/*`

**Must include**

- case class
- operation
- output class
- source/target summary
- record/package links
- coverage role

**Must not introduce**

- new adjudication
- case ranking
- duplicate full case narratives

### Appendix N — Integrated STRATA Audit Template

**Production status:** substantive bounded provisional completion  

**Target file:** `02_appendices/Appendix_N_Integrated_STRATA_Audit_Template.md`  
**Purpose:** Provide the full twelve-stage audit and chain handoff template without making machine validity substantive truth.  
**Contributing contract migrations:** 9 from `7, 17, 28, 39, 40, 41, 50, 53, 54`

**Canonical owners / source inputs**

- `01_blocks/05_part_iv_limits.md`
- `04_reference/Audit_Checklist.md`

**Formal-model inputs**

- `07_model/Admissibility_Rules.yaml`
- `07_model/Boundary_Decision_Tree.yaml`
- `07_model/Transformation_Record.schema.json`

**Case inputs**

- `03_cases/packages/C53-CPD1_COMPOSE_PROJECT_AS_DECOMPOSE_Integrated_Audit_Chain.md`

**Must include**

- twelve audit stages
- candidate generation
- collision adjudication
- output mapping
- loss/stop/failure preservation
- chain handoff

**Must not introduce**

- audit stage 13
- automatic substantive finding
- merged local results
- authority inheritance

**Assigned downstream template outputs**

- `03_cases/templates/integrated_audit_case_template.yaml`

## 5. Template strategy

The eight currently empty files in `03_cases/templates/` are assigned rather than deleted:

| Template | Owning Appendix | Intended role |
|---|---|---|
| `case_template.md` | C | generic human-readable Record companion |
| `compose_case_template.yaml` | D | usable COMPOSE occurrence template |
| `decompose_case_template.yaml` | E | usable DECOMPOSE occurrence template |
| `project_as_case_template.yaml` | F | usable PROJECT_AS occurrence template |
| `countercase_template.md` | H | countercase narrative template |
| `confusion_case_template.md` | I | confusion-case narrative template |
| `non_capture_case_template.yaml` | L | genuine non-capture test template |
| `integrated_audit_case_template.yaml` | N | full integrated audit / chain template |

Each template must be executable or directly reusable after its owning Appendix is produced. No empty template may remain at Appendix completion.

## 6. Case-artifact boundary

```text
59 operation-record YAML files
↔ 59 same-basename Markdown companions
+ 10 multi-record package narratives
+ 1 Markdown Case Index
+ 1 YAML Case Index
```

The package narratives exist only where several distinct operation occurrences require shared source context, comparison, or chain handoff. They are not chapter-by-chapter appendices and do not replace local Records.

## 7. Minified and contract status

The four compact kernels are current and unchanged in substance. `Block_Contracts.md` and `Chapter_Contracts.md` retain their original contract semantics; a final downstream-status note now marks their historical next-step language as completed and identifies Appendices A–N as the current production phase.

## 8. Deferred work

The complete rule-guided iteration of `01_blocks/*` remains scheduled for the later Integrated Corpus Audit. Appendix production may cite current Blocks, but must not treat working-package residue in the Blocks as Appendix-owned content or silently repair it there.

## 9. Preflight completion gate

Appendix production may begin only if:

- all 14 target stubs exist;
- the A–N titles match Structure;
- every Appendix has declared owners and prohibited drift;
- schema/template Appendices are bound to current Formal Model owners;
- Case inputs distinguish local Records from package narratives;
- `_workfiles/**` remains excluded;
- the root contains no active production workfile;
- no Appendix O or P is implied;
- no Appendix is used to reopen a final lock.

**Preflight result:** `pass`  
**Appendix production result:** `A–N substantive completion`  
**Next controlled step:** `Reference Freeze`

Machine-readable companions:

- [`Appendix_Production_Map.csv`](Appendix_Production_Map.csv)
- [`Appendix_Migration_Matrix.csv`](Appendix_Migration_Matrix.csv)
