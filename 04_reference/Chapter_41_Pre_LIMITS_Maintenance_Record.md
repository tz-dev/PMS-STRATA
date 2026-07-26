# Chapter 41 Pre-LIMITS Maintenance Record

**Record version:** v0.7  
**Status:** Four-pass intake audit consolidated; Maintenance WP0–WP5 complete; completion gate passed; Chapter 41 WP1 next  
**Audit source:** PMS-STRATA Source-of-Truth ZIP 254 and PMS Base files supplied with Handover Bundle v0.6  
**Current maintenance execution release:** PMS-STRATA Source-of-Truth ZIP 261  
**Repository role:** Pre-production maintenance control record; supporting reference only  
**Authority:** No independent theory, operation, Rule, Output Class, case-result, or application authority  
**Current production state:** Chapter 41 Preparation Gate complete; canonical Chapter 41 prose not started  
**Next controlled route:** Chapter 41 WP1 — §§41.1–41.4; canonical Chapter 41 prose remains unstarted until that production step begins  

## 1. Purpose

This record consolidates the complete four-pass intake review and the executed Pre-LIMITS maintenance performed before Part IV — LIMITS production. It provides one controlled location from which completed dispositions, preserved Stops, future lock dependencies, and the Chapter 41 handoff can be inspected without reopening the entire repository audit.

The record now preserves both the original inventory and the executed dispositions. `M41-PRE-01` through `M41-PRE-14` are completed, `M41-PRE-15` remains protected under the existing artifact-complete RETYPE `mandatory_stop`, `M41-PRE-16` remains an explicit future dependency for Chapter 53/Part-IV lock, and `M41-PRE-17` remains a confirmed non-action item. No Chapter 41 prose was created during maintenance.

The governing separation is:

```text
maintenance inventory complete
+ maintenance execution complete
+ completion gate passed
≠ Chapter 41 WP1 complete
≠ artifact-complete RETYPE lock available
≠ Part IV final lock available
```

## 2. Authority and Non-Authority Boundary

This record remains subordinate to:

```text
PMS.yaml
→ 00_source/PMS-STRATA_Structure.md
→ 01_blocks/*
→ 05_minified/*
→ 07_model/*
→ 04_reference/*
```

It may:

- identify inconsistencies, drift, unresolved maintenance, and execution order;
- preserve verified audit findings;
- route later patches and validation;
- distinguish blockers, non-blockers, and deferred lock dependencies.

It may not:

- redefine PMS Base or Δ–Ψ dependencies;
- add a fourth STRATA operation;
- add or rename an Output Class;
- adjudicate unproduced RETYPE cases;
- convert mechanical validation into substantive admissibility;
- override Contracts, Minified controls, or canonical Block prose;
- erase the existing artifact-complete RETYPE `mandatory_stop`.

## 3. Four-Pass Audit Coverage

### Pass 1 — PMS Base and Main Paper

Verified:

- bundle and standalone PMS Base files are byte-identical;
- `PMS.yaml` parses without duplicate keys;
- all eleven operators and their dependencies are internally consistent;
- PMS Base and the main paper share the same bounded, non-self-authorizing claim posture.

Binding non-equivalences confirmed:

```text
PMS operator composition ≠ STRATA COMPOSE
Σ ≠ COMPOSE
Φ ≠ PROJECT_AS
PMS operator layers ≠ STRATA relative levels
Α stabilization ≠ automatically established path dependence
derived construct ≠ new PMS primitive
machine-readable consistency ≠ truth proof
```

### Pass 2 — Handover and Control Layer

Verified:

- all outer and work-package checksums pass;
- the embedded Source-of-Truth state is ZIP 254;
- current RETYPE prose, Chapter 41 Preparation Record, and re-anchoring reviews are byte-identical to their canonical repository counterparts;
- Chapter 41 WP1 is the intended production successor after maintenance;
- artifact-complete RETYPE lock remains under `mandatory_stop` because the three required packages are absent.

Detected:

- README tail contains historical next-step language that no longer matches the current route;
- historical preparation/review records use older ZIP numbers as provenance and should not be read as current Source of Truth.

### Pass 3 — Canonical Corpus, Reference Kernel, and Formal Model

Verified:

- Foundations 0–8, PATH 9–17, SUB 18–28, and RETYPE 29–40 are present in their declared bounded states;
- `01_blocks/05_part_iv_limits.md` is empty and Chapter 41 prose has not begun;
- exactly three operations, ten canonical Output Classes, and five Loss fields remain intact;
- 48 YAML files and both JSON Schemas parse successfully;
- Formal Model Root, eight Smoke Fixtures, and all 29 PATH/SUB records validate against their schemas;
- all 29 case-index pairs, paths, hashes, and selected-class constraints pass.

Detected:

- stale Reference status headers and early inventory snapshots;
- incorrect `placeholder` labels for already populated Blocks and Case artefacts;
- unresolved fragment anchors concentrated in Foundations Chapters 2 and 8 and PATH Chapters 11–17;
- RETYPE heading-level drift for Chapters 35–40;
- historical Formal Model assembly provenance still names ZIP 147.

### Pass 4 — Remaining Architecture and LIMITS Readiness

Verified:

- Chapters 41–53 possess a coherent non-overlapping architecture;
- LIMITS is a Part and cross-cutting admissibility discipline, not a fourth operation or meta-PMS;
- the available RETYPE method corpus is sufficient for Chapter 41 production after maintenance;
- final LIMITS lock is not available until the required integrated and RETYPE artefact dependencies are satisfied.

Detected:

- controlled-vocabulary drift in Counterfactual Sensitivity;
- possible collision between Structure-level illustrative YAML snippets and the canonical Shared Transformation Record;
- natural-language Output-Class spellings in the Blueprint that must not replace canonical identifiers;
- an ownership error in the Chapter 41 Preparation Record;
- an internally tense Q0 failed-projection status;
- Chapters 36–40 still need the equivalent conservative PMS occurrence-level re-anchoring audit/patch applied to Chapters 29–35.

## 4. Stable Baseline and Protected Non-Changes

The following are not maintenance targets unless a later patch independently demonstrates a defect:

```text
operations:
  - COMPOSE
  - DECOMPOSE
  - PROJECT_AS

parts:
  - PATH
  - SUB
  - RETYPE
  - LIMITS

loss:
  - preserved
  - compressed
  - excluded
  - uncertain
  - irrecoverable
```

The ten canonical Output Classes remain exactly:

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

No maintenance work may silently alter these inventories, Δ–Ψ, PMS dependencies, the twelve audit stages, or the Shared Record ownership architecture.

## 5. Pre-LIMITS Maintenance Register

### M41-PRE-01 — Correct Chapter 41 Definition Ownership

**Priority:** required before Chapter 41 WP1  
**Status:** completed in Maintenance WP0

The Chapter 41 Preparation Record currently assigns both the Admissibility Band and the twelve-stage integrated audit architecture to Chapter 6.

Required correction:

```text
Chapter 6
→ owns the Admissibility Band

Chapter 53
→ owns the integrated twelve-stage STRATA audit
```

Chapter 41 may establish why integrated limits are necessary, but must not pre-empt Chapter 53 by owning or fully specifying the integrated audit.

**WP0 execution:** Corrected in `Chapter_41_Preparation_Record.md`; Chapter 6 now owns the Admissibility Band and Chapter 53 owns the integrated twelve-stage STRATA audit.

### M41-PRE-02 — Normalize Counterfactual Sensitivity Vocabulary

**Priority:** required before Chapters 41 and 46  
**Status:** completed in Maintenance WP1

Current formal-model vocabulary:

```text
strongly_sensitive
partially_sensitive
weakly_sensitive
insensitive
underdetermined
untestable
```

Earlier Foundations prose uses:

```text
sensitive
partially sensitive
insensitive
underdetermined
not testable with available sources
```

Required work:

- declare one canonical controlled vocabulary;
- map older prose labels explicitly rather than adding a third vocabulary;
- synchronize Foundations, Reference files, LIMITS Blueprint language, and formal-model descriptions;
- preserve Counterfactual Sensitivity as non-causal and claim-relative.

**WP1 execution:** The six-value formal vocabulary is now canonical across Foundations, Structure, Reference, Contracts, Minified control, and `Admissibility_Rules.yaml`; older prose labels are explicitly mapped and do not remain controlled alternatives.

### M41-PRE-03 — Bind LIMITS Blueprint Views to the Shared Transformation Record

**Priority:** required before LIMITS prose uses record examples  
**Status:** completed in Maintenance WP1

The Structure Blueprint contains illustrative views such as:

```text
relevance_floor
traceability_ceiling
counterfactual_test
continuity
source_and_calibration
stop
capture_status
non_capture
strata_audit
```

These are not the canonical top-level structure of `Transformation_Record.schema.json`.

Required work:

- classify each Blueprint snippet as a conceptual view or projection of existing Shared Record fields;
- map every illustrative field to the canonical record path or mark it as explanatory prose only;
- prohibit a second LIMITS-specific record grammar;
- preserve Chapter 48's single-record-system boundary.

**WP1 execution:** A binding LIMITS Record-View Control now maps all Chapter 44–53 Blueprint snippets to canonical Shared Record paths. Every illustrative snippet is marked conceptual; no field or schema was added.

### M41-PRE-04 — Enforce Exact Canonical Output-Class Identifiers

**Priority:** required before Chapters 51–53  
**Status:** completed in Maintenance WP1

Natural-language spellings in the Blueprint, including `admissible with bounded claim`, `resolution-neutral`, `analogy only`, and `non-capture`, must not be mistaken for additional or alternative canonical classes.

Required rule:

```text
explanatory prose may be natural language
canonical mapping, tables, records, and audit outputs
→ exact underscore identifiers only
```

**WP1 execution:** Chapter 53's audit-result inventory now uses the exact ten identifiers. Natural-language prose remains explanatory only and is not a parallel class vocabulary.

### M41-PRE-05 — Repair Q0 Prior-Failure Status Logic

**Priority:** required before Chapter 41 WP1 example production  
**Status:** completed in Maintenance WP0

The Chapter 41 pressure chain currently combines:

```text
claim_id: Q0_failed_projection
prior_disposition: failed_transformation_candidate_only
substantive_result: unadjudicated
```

This weakens the Contract requirement that a failed projection remain failed when later transformations are attempted.

Required resolution:

- treat Q0 as a methodically stipulated prior `failed_transformation` disposition already warranted in a separate record; or
- use an existing formal fixture only as a formal pressure source while explicitly preserving `fixture ≠ case evidence`.

Q1–Q3 must remain separate new testable claims with separate Records, Loss, and outputs. Later success may not erase Q0.

**WP0 execution:** Q0 is now explicitly a stipulated prior `failed_transformation` disposition from a separately warranted Record premise that is not created or readjudicated in the Preparation Record. Q1–Q3 remain separate unadjudicated claims.

### M41-PRE-06 — Separate LIMITS Production Permission from LIMITS Lock Permission

**Priority:** required before Chapter 41 WP1  
**Status:** completed in Maintenance WP0

The current state must be stated consistently as:

```text
RETYPE method corpus
→ bounded provisional lock
→ sufficient dependency for Chapter 41 method production

artifact-complete RETYPE lock
→ mandatory_stop
→ not available

Part IV final lock
→ not available until RETYPE and integrated case dependencies are satisfied
```

Chapter 41 production must not be read as inheritance of the absent RETYPE artefact lock.

**WP0 execution:** The Preparation Record now separates method-production permission, the continuing artifact-complete RETYPE `mandatory_stop`, and the unavailable Part IV final lock.

### M41-PRE-07 — Complete Conservative PMS Re-Anchoring Review/Patch for Chapters 36–40

**Priority:** recommended before Chapter 41 WP1; required before RETYPE artefact lock or Reference Freeze  
**Status:** completed in Maintenance WP2

The intervention must remain occurrence-level, claim-relevant, and non-decorative.

#### Chapter 36 — Competing Projections

Add a light source-carrier comparison rule where PMS-derived source structures materially carry rival projections. Rival projections must differ through declared source weighting, relation selection, or target context, not merely through competing labels.

#### Chapter 37 — Analogy and Label Substitution

Add a bounded positive occurrence-level test using existing Source Reference, Constitutive Source Trace, sensitivity, and Loss positions. Include a label-removal pressure test where useful.

#### Chapter 38 — Invalid Type Jumps

Add one concise occurrence-grounded example that exposes the prohibited jump from operator-typed occurrence or derived function to operator identity, primitive, or person type.

#### Chapter 39 — RETYPE Boundary Conditions

Preserve the already strong generic anchoring. Add at most one narrowly useful operator-grounded Ceiling example; avoid redundant symbol insertion.

#### Chapter 40 — Cases and Local Audit

Do not substitute prose for the three missing case packages. Ensure future artefacts use concrete occurrence/relation traces, exact Loss, and canonical class mapping.

Protected boundary:

```text
re-anchoring patch
≠ new operator_trace field
≠ full Δ–Ψ inventory requirement
≠ inferred source typing from target fit
≠ RETYPE artefact completion
```

**WP2 execution:** Chapters 36–40 now contain bounded occurrence-level anchors for rival-source comparison, analogy/projection Source Trace, invalid type-jump pressure, the Traceability Ceiling, and future case-artifact requirements. The exact execution record is [`PMS_Operator_Reanchoring_Todo_Chapters_36_40.md`](PMS_Operator_Reanchoring_Todo_Chapters_36_40.md). No case family was adjudicated and the artifact-complete RETYPE lock remains `mandatory_stop`.

### M41-PRE-08 — Synchronize README Current Route and Historical Tail

**Priority:** required before release of the maintenance-complete ZIP  
**Status:** completed in Maintenance WP0

Required work:

- make the current Pre-LIMITS maintenance route visible at the top and final current-status section;
- mark older review-next-step paragraphs as historical or remove their stale routing language;
- ensure the next controlled production step becomes Chapter 41 WP1 only after the maintenance gate passes.

**WP0 execution:** README routing was corrected and the two stale tail next-step lines were marked historical. Later maintenance handoffs superseded the stage-local WP1 route; WP5 now synchronizes the final Chapter 41 WP1 route.

### M41-PRE-09 — Refresh Reference Status Headers and Historical Layering

**Priority:** required before Chapter 41 reference synchronization; mandatory before Reference Freeze  
**Status:** completed in Maintenance WP3

Several Reference files still identify themselves as Chapter-20-era synchronized although later content reaches Chapter 40 and Chapter 41 Preparation.

Required work:

- add a current-status summary to each affected Reference file;
- distinguish current canonical navigation from historical WP-stage records;
- avoid deleting useful provenance where a clear historical label suffices;
- remove or supersede statements such as `Chapters 21–57 remain pending` where objectively false.

Affected core files include:

```text
Glossary.md
Operator_Index.md
Transformation_Operation_Index.md
Non_Equivalence_Index.md
Output_Class_Index.md
Claim_Type_Table.md
Admissibility_Band_Reference.md
Cross_Reference_Map.md
Evidence_Map.md
Audit_Checklist.md
Reader_Pathways.md
```


**WP3 execution:** All eleven core Reference controls now carry a current Pre-LIMITS synchronization header and an explicit historical-layering rule. Stage-local `pending` and `next controlled step` statements remain available as provenance but no longer override the current header.

### M41-PRE-10 — Correct Cross-Reference Placeholder States

**Priority:** required before Reference Freeze; recommended during maintenance  
**Status:** completed in Maintenance WP3

The early Cross-Reference inventory still labels populated Blocks and Case artefacts as placeholders.

Required work:

- update the inventory status of Foundations, PATH, SUB, RETYPE, Case Index, and PATH/SUB case directories;
- preserve intentional placeholders for Front Matter, LIMITS, Conclusion, Appendices, Derivatives, and Reader content that are correctly deferred.


**WP3 execution:** The Cross-Reference artifact registry now marks Foundations, PATH, SUB, RETYPE, both Case Index files, and the PATH/SUB case directories according to their actual populated or bounded-lock states. Intentional future placeholders remain unchanged.

### M41-PRE-11 — Repair Fragment Anchor Coverage

**Priority:** recommended before Chapter 41 production; mandatory before Reader/Reference Freeze  
**Status:** completed in Maintenance WP3

Verified file targets exist, but many fragment routes do not resolve. The main gaps are:

```text
Foundations Chapters 2 and 8
PATH Chapters 11–17
```

Preferred conservative repair:

- add the explicit anchors already expected by the current Reference links;
- avoid mass rewriting all Reference links unless an anchor cannot be restored safely;
- rerun a GitHub-compatible fragment audit after patching.


**WP3 execution:** Explicit compatibility anchors were added for Foundations Chapters 2 and 8, PATH Chapters and referenced sections 11–17, SUB §§23.10–23.11, Structure Chapters 17–20, and five referenced Chapter Contracts. The one obsolete Chapter-5 fragment was routed to the actual canonical anchor. The repository-wide local fragment audit now resolves all declared internal fragments.

### M41-PRE-12 — Normalize RETYPE Heading Levels for Chapters 35–40

**Priority:** low-risk maintenance before Chapter 41  
**Status:** completed in Maintenance WP2

Pre-patch structure:

```text
Part III — RETYPE → H1
Chapters 29–34 → H2
Chapters 35–40 → H1
```

Required correction:

```text
Chapters 35–40
# → ##
```

The change is navigational only and must preserve explicit anchors and prose.

**WP2 execution:** Chapter headings 35–40 were normalized from H1 to H2. The Part III title remains H1; explicit anchors and prose are unchanged.

### M41-PRE-13 — Clarify Formal Model Assembly Provenance

**Priority:** required during maintenance if the Formal Model Root is touched; mandatory before Model Finalization  
**Status:** completed in Maintenance WP4

Before WP4, `07_model/PMS-STRATA.yaml` stated:

```text
built_from_snapshot: ...ZIP_147.zip
```

while current component hashes are valid and the active repository source is ZIP 254/its successor.

Required work:

- either update the active assembly snapshot to the current release source; or
- rename/qualify the field as historical initial-assembly provenance;
- do not imply that a historical snapshot is the current Source of Truth.

**WP4 execution:** The active assembly input is now `PMS-STRATA_Source_of_Truth_ZIP_259.zip` with its verified SHA-256 fingerprint. ZIP 147 no longer appears in the active assembly basis. The field records the build-input snapshot for Root assembly and does not confer Source-of-Truth or semantic authority.

### M41-PRE-14 — Distinguish Current Formal Rules from Historical Handoff Accumulation

**Priority:** maintenance/documentation; mandatory before Model Finalization  
**Status:** completed in Maintenance WP4

`Admissibility_Rules.yaml` is syntactically valid but contains extensive historical chapter/WP/handoff metadata beside the current normative core.

Required work:

- identify the current operative rule core visibly;
- mark historical production traces as historical/non-normative;
- prevent stale `pending` statements from being read as current status;
- avoid a large model refactor unless necessary for semantic clarity.

**WP4 execution:** `Admissibility_Rules.yaml` now contains an explicit `model_layering` declaration. It enumerates the current operative rule-core keys, separates current integration metadata, classifies chapter/WP/review/maintenance handoffs as non-normative provenance, and prohibits historical traces from overriding rules, vocabularies, operations, Output Classes, audit stages, current status, or authority boundaries. No large refactor or second registry was introduced.

### M41-PRE-15 — Preserve the RETYPE Artefact-Complete Stop

**Priority:** protected deferred dependency  
**Status:** deferred under `mandatory_stop`

The three absent lock-critical packages remain:

1. trajectory as bounded frame-function;
2. `PROJECT_AS` label-substitution failure;
3. projection versus structural analogy confusion case.

Each later package requires:

```text
Markdown case
YAML PROJECT_AS record
local audit
exact five-part Loss
alternatives
canonical Output-Class mapping
```

This maintenance sequence must not fabricate or silently infer these results.

### M41-PRE-16 — Preserve Integrated-Case Dependencies for LIMITS Lock

**Priority:** deferred; required before Chapter 53/Part IV lock  
**Status:** open future dependency

Formal Smoke support is available, including one integrated-chain fixture, but:

```text
Smoke fixture
≠ substantive case
≠ empirical support
≠ RETYPE lock package
```

Before final LIMITS lock, the required operation chains and boundary cases must be represented through separate operation Records and a chain-level audit Record.

### M41-PRE-17 — Preserve Intentional Empty Layers

**Priority:** non-action item  
**Status:** confirmed intentional

The following empty or scaffold layers are not current defects:

- Front Matter;
- LIMITS prose before Chapter 41;
- Conclusion;
- Appendices A–N;
- Derivative Publications;
- Reader implementation/content;
- empty case templates before integrated case production.

They must not be filled early merely to remove empty files.

## 6. Proposed Maintenance Work Packages

The following sequence is recommended for later prompts.

### Maintenance WP0 — Control and Routing Corrections

Scope:

- M41-PRE-01;
- M41-PRE-05;
- M41-PRE-06;
- final routing language in README and Chapter 41 Preparation Record.

Gate:

- Chapter ownership correct;
- Q0 pressure logic usable;
- production permission and lock permission separated;
- current route unambiguous.

### Maintenance WP0 — Execution Result

**Disposition:** completed

Completed items:

- `M41-PRE-01` — definition ownership corrected;
- `M41-PRE-05` — Q0 prior-failure premise repaired without creating a case result;
- `M41-PRE-06` — method-production permission separated from artifact and Part-lock permission;
- `M41-PRE-08` — current README route and historical tail synchronized.

Preserved boundaries:

```text
Chapter 41 prose
→ not started

artifact-complete RETYPE lock
→ mandatory_stop

Part IV final lock
→ unavailable
```

**Historical WP0 handoff:** Maintenance WP1 — Vocabulary and Record-Semantics Alignment.

### Maintenance WP1 — Execution Result

**Disposition:** completed

Completed items:

- `M41-PRE-02` — one six-value Counterfactual Sensitivity vocabulary established, with explicit legacy mapping;
- `M41-PRE-03` — all LIMITS Blueprint record views bound to the existing Shared Transformation Record;
- `M41-PRE-04` — exact ten Output-Class identifiers enforced in canonical audit mapping;
- Chapter 47 — `type continuity` fixed as a continuity view under canonical `TypeIntegrity`, not a new Rule.

Preserved boundaries:

```text
operations
→ exactly 3

Output Classes
→ exactly 10

Shared Record grammar
→ unchanged

new Rule or schema field
→ none
```

Verification completed for WP1:

```text
48 YAML files parsed with duplicate-key rejection
2 JSON schemas parsed
Formal Model Root schema validation passed
8 Smoke Records + 29 PATH/SUB Records = 37/37 record validations passed
formal-root component hashes passed
29 case-index path and SHA-256 bindings passed
operations = 3
Output Classes = 10
Counterfactual Sensitivity values = 6
Chapter 41 canonical prose = not started
```

**Historical WP1/WP2 handoff:** Maintenance WP2 completed in ZIP 258, after which WP3 was the next controlled maintenance step. This stage-local route is superseded by the passed WP5 completion gate.

### Maintenance WP2 — RETYPE Chapters 36–40 Re-Anchoring

Scope:

- M41-PRE-07;
- M41-PRE-12 where convenient in the same Block patch.

Gate result — **passed in ZIP 258**:

- conservative occurrence-level anchoring complete;
- no decorative operator inventory;
- no case-result fabrication;
- Chapter 40 artefact Stop preserved;
- RETYPE headings 35–40 normalized without anchor or prose loss.

### Maintenance WP3 — Reference and Navigation Synchronization

**Disposition:** completed in ZIP 259

**Execution record:** [`PMS_STRATA_Pre_LIMITS_Reference_Navigation_Maintenance_WP3.md`](PMS_STRATA_Pre_LIMITS_Reference_Navigation_Maintenance_WP3.md)

Completed scope:

- completed `M41-PRE-08` routing remains synchronized;
- `M41-PRE-09` current Reference status and historical layering;
- `M41-PRE-10` populated-artifact registry correction;
- `M41-PRE-11` explicit fragment-anchor repair.

Gate result:

- current status summaries are consistent;
- stage-local production statements are visibly historical under the header rule;
- populated Blocks and PATH/SUB Case artefacts are not marked placeholders;
- all declared internal Markdown file targets and fragments resolve under the repository audit;
- no canonical theory, case result, operation, Output Class, or lock status changed.

Historical WP3 handoff: **Maintenance WP4 — Formal Model Provenance and Historical-State Clarity**.

### Maintenance WP4 — Formal Model Provenance and Historical-State Clarity

Scope:

- M41-PRE-13;
- M41-PRE-14;
- any component fingerprint updates caused by modified registered Reference controls.

Gate result — **passed in ZIP 260**:

- active assembly input provenance now names ZIP 259 with a verified fingerprint;
- historical ZIP 147 no longer appears as the active assembly basis;
- current operative rule-core keys, integration metadata, and historical production traces are explicitly separated;
- historical traces are non-normative and cannot override current semantics or status;
- no large model refactor, new Rule, operation, Output Class, audit stage, schema field, or route was introduced;
- Formal Model Root descriptor versions and component fingerprints are synchronized.

**Execution record:** [`PMS_STRATA_Pre_LIMITS_Formal_Model_Provenance_Maintenance_WP4.md`](PMS_STRATA_Pre_LIMITS_Formal_Model_Provenance_Maintenance_WP4.md)

**Historical WP4 handoff:** Maintenance WP5 — Integrated Verification and Release.

### Maintenance WP5 — Integrated Verification and Release

**Disposition:** completed; gate passed in ZIP 261  
**Execution record:** [`PMS_STRATA_Pre_LIMITS_Integrated_Verification_Maintenance_WP5.md`](PMS_STRATA_Pre_LIMITS_Integrated_Verification_Maintenance_WP5.md)

Executed checks:

1. all YAML parsed with duplicate-key rejection;
2. both JSON Schemas parsed;
3. Formal Model Root validated;
4. all eight Smoke Fixtures validated;
5. all 29 existing PATH/SUB records validated;
6. operation, Output-Class, Rule, audit-stage, Counterfactual-Sensitivity, and Loss inventories verified;
7. Case Index paths, hashes, and selected-class constraints verified;
8. registered component, governing-control, Reference, and schema fingerprints verified;
9. all local file links and fragment anchors resolved;
10. current-status surfaces synchronized and historical stage records kept non-normative;
11. all discovered `authority_inheritance` fields remain `prohibited`;
12. Chapter 40 artifact-complete RETYPE status remains `mandatory_stop`;
13. the repository was packaged as Source-of-Truth ZIP 261.

The exact machine counts and boundary checks are preserved in the WP5 execution record.

## 7. Maintenance Completion Gate

**Disposition:** passed in Source-of-Truth ZIP 261  

Chapter 41 WP1 is now the next controlled production step because all of the following hold:

```text
M41-PRE-01 through M41-PRE-14
→ completed, explicitly deferred, or documented as non-blocking

Counterfactual Sensitivity
→ one controlled vocabulary

LIMITS record examples
→ mapped to the Shared Transformation Record

Chapter 41 pressure object
→ preserves a genuine prior failed disposition

RETYPE method dependency
→ available with bounded claim

RETYPE artifact-complete lock
→ still mandatory_stop

README / Preparation / Reference navigation
→ same current route

YAML / JSON / Schema / Case / Hash / Anchor checks
→ passed within declared scope
```

The resulting route is then:

```text
Pre-LIMITS maintenance gate passed
→ Chapter 41 WP1
→ §§41.1–41.4
```

## 8. Final Audit Disposition

The four-pass review found no fundamental STRATA architecture failure and no blocker requiring redesign of PMS Base, the three operations, the four Parts, the Admissibility Band, the ten Output Classes, or the Shared Record.

The exact current disposition is:

```text
canonical theory and method
→ robust

formal syntax and existing schema validation
→ robust

handover and Source-of-Truth integrity
→ robust

pre-LIMITS maintenance inventory
→ complete

pre-LIMITS maintenance execution
→ WP0–WP5 complete; completion gate passed

Chapter 41 Preparation Gate
→ complete

Chapter 41 canonical prose
→ not started

artifact-complete RETYPE lock
→ mandatory_stop

Part IV final lock
→ unavailable
```

This record is the closed Pre-LIMITS maintenance control record. The next controlled production step is Chapter 41 WP1; the deferred RETYPE and integrated-case dependencies remain visible and unchanged.
