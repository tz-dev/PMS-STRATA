# PMS-STRATA Formal Model v0 — Canonical Smoke Examples

**Artifact role:** controlled index and execution boundary for the canonical Formal Model v0 smoke-record suite  
**Current suite state:** eight canonical YAML records populated; seven `operation_occurrence` records and one `integrated_chain` record  
**Routing state of committed records:** `routed`  
**Current model versions:** Operation Registry `0.1.1`; Output Classes `0.1.1`; Admissibility Rules `0.1.2`; Boundary Decision Tree `0.1.1`; Transformation Record Schema `0.1.2`  
**Gate status:** record production, suite-level cross-record audit, Reference/status synchronization, Root fingerprint/provenance synchronization, and final Formal Model v0 internal smoke-gate rerun complete and passed

---

## 1. Purpose

This directory contains the smallest canonical set of synthetic records used to test whether the current PMS-STRATA Formal Model v0 can:

- represent each of the three operations without adding a fourth operation;
- distinguish positive transformation, failure, claim reduction, mandatory stop, and non-capture;
- preserve the separation between operation type, operation occurrence, and integrated chain;
- keep origin type distinct from contextual target function;
- enforce the Praxeological Relevance Floor and Praxeological Traceability Ceiling as different boundaries;
- preserve loss, claim ceilings, source ceilings, stop conditions, non-capture, and authority limits;
- reject structurally invalid records through the schema;
- expose schema-valid but materially inconsistent routings to a separate semantic and boundary audit;
- test that local component admissibility does not automatically transfer to a chain-level claim.

The records are synthetic formal fixtures. They are not empirical cases, domain findings, scientific confirmations, legal or normative determinations, person evaluations, implementation certifications, or application permissions.

```text
formal conformance
≠ empirical truth
≠ semantic validity
≠ normative validity
≠ application authority
```

---

## 2. Authority and Control Boundaries

The examples do not define STRATA theory, operations, rules, schemas, routes, or Output Classes. They instantiate current controlled owners:

| Control concern | Current owner |
| --- | --- |
| operation inventory and signatures | `../Operation_Registry.yaml` |
| canonical Output Classes and class payloads | `../Output_Classes.yaml` |
| admissibility and boundary rules | `../Admissibility_Rules.yaml` |
| formal route ordering and boundary collisions | `../Boundary_Decision_Tree.yaml` |
| individual record structure | `../Transformation_Record.schema.json` |
| integrated model assembly and inventories | `../PMS-STRATA.yaml` |
| integrated model shape | `../PMS-STRATA.schema.json` |
| semantic definitions and non-equivalences | governing prose, Minified Kernel, and `04_reference/*` |

The examples may reveal missing fields, invalid values, route collisions, insufficient distinctions, or cross-record inconsistencies. They do not replace their owners and do not increase their authority.

---

## 3. Canonical Suite Inventory

| No. | File | Record scope | Operation or chain | Expected class | Expected route | Primary boundary tested |
| ---: | --- | --- | --- | --- | --- | --- |
| 01 | [`01_COMPOSE_Admissible.yaml`](01_COMPOSE_Admissible.yaml) | `operation_occurrence` | `COMPOSE` | `admissible` | `route_admissible` | positive traceable composition |
| 02 | [`02_DECOMPOSE_Relevance_Floor_Stop.yaml`](02_DECOMPOSE_Relevance_Floor_Stop.yaml) | `operation_occurrence` | `DECOMPOSE` | `mandatory_stop` | `route_mandatory_stop` | further resolution below the Relevance Floor |
| 03 | [`03_PROJECT_AS_Admissible.yaml`](03_PROJECT_AS_Admissible.yaml) | `operation_occurrence` | `PROJECT_AS` | `admissible` | `route_admissible` | bounded contextual function with origin type preserved |
| 04 | [`04_PROJECT_AS_Label_Substitution.yaml`](04_PROJECT_AS_Label_Substitution.yaml) | `operation_occurrence` | `PROJECT_AS` | `failed_transformation` | `route_failed_transformation` | label substitution without source-sensitive function |
| 05 | [`05_Traceability_Ceiling_Failure.yaml`](05_Traceability_Ceiling_Failure.yaml) | `operation_occurrence` | `COMPOSE` | `failed_transformation` | `route_failed_transformation` | abstraction above the Traceability Ceiling |
| 06 | [`06_Claim_Reduction.yaml`](06_Claim_Reduction.yaml) | `operation_occurrence` | `DECOMPOSE` | `claim_reduction_required` | `route_claim_reduction_required` | genuine resolution gain with an overstrong current claim |
| 07 | [`07_Mandatory_Stop.yaml`](07_Mandatory_Stop.yaml) | `operation_occurrence` | `DECOMPOSE` | `mandatory_stop` | `route_mandatory_stop` | stop before reference- and function-detaching fragmentation |
| 08 | [`08_Non_Capture.yaml`](08_Non_Capture.yaml) | `integrated_chain` | `COMPOSE → PROJECT_AS` | `non_capture` | `route_non_capture` | local admissibility does not aggregate into an adequate whole claim |

All committed records use:

```yaml
routing_state: routed
```

Formal-diagnostic behavior is tested through temporary mutation fixtures during audits. Such mutations are not additional canonical records and must not be committed as a ninth example.

---

## 4. Suite Topology

```text
8 canonical records
├── 7 operation_occurrence records
│   ├── COMPOSE: 2
│   ├── DECOMPOSE: 3
│   └── PROJECT_AS: 2
└── 1 integrated_chain record
    └── COMPOSE → PROJECT_AS
```

The integrated chain is not a fourth operation. It is a record scope for testing a sequence of separately typed operation occurrences and the new claim produced by their integration.

```text
operation type
≠ operation occurrence
≠ integrated chain
```

---

## 5. Cross-Record Relations

### 5.1 Source and rival relations

```text
01_COMPOSE_Admissible
├── source for 03_PROJECT_AS_Admissible
├── source for 04_PROJECT_AS_Label_Substitution
└── positive rival for 05_Traceability_Ceiling_Failure

03_PROJECT_AS_Admissible
├── positive rival for 04_PROJECT_AS_Label_Substitution
└── component of 08_Non_Capture

01_COMPOSE_Admissible
+ 03_PROJECT_AS_Admissible
→ components of 08_Non_Capture
```

Records 02, 06, and 07 contain prior source claims internal to their synthetic fixtures. Those prior claims are not additional canonical STRATA smoke records.

### 5.2 Required handoff for Record 03

Record 03 must preserve from Record 01:

- record ID `smoke.compose.admissible.01`;
- claim ID `claim.compose.admissible.01`;
- reference object `composite.authorization-sequence.alpha`;
- origin type `sequence`;
- the local COMPOSE result and its loss record.

PROJECT_AS creates a new contextual-function claim. It does not retroactively validate, strengthen, replace, or retype the COMPOSE claim.

### 5.3 Required handoff for Record 08

Record 08 must resolve and preserve:

- `smoke.compose.admissible.01`;
- `smoke.project-as.admissible.03`;
- declared sequence `COMPOSE → PROJECT_AS`;
- both component claims;
- both component Output Classes;
- both component loss records;
- the sequence-to-function reference and type handoff.

The chain-level claim is separately testable:

```text
local admissibility
≠ inherited chain admissibility

new transformation
= new testable claim
```

---

## 6. Boundary Matrix

| Boundary | Positive or retained side | Rejected or stopped side | Primary record |
| --- | --- | --- | --- |
| composition vs ordered list | constitutive selection, order, relation, and loss | chronology or aggregation without formation | 01 |
| resolution gain vs resolution neutrality | finer distinctions alter a warranted reconstruction | more detail without praxeological purchase | 02, 06 |
| projection vs label substitution | target function is bounded and source-sensitive | target label remains indifferent to source structure | 03, 04 |
| Relevance Floor vs Traceability Ceiling | useful distinction within source support | below-floor detail or above-ceiling abstraction | 02, 05, 07 |
| failure vs mandatory stop | attempted operation fails a necessary condition | prohibited continuation is stopped before assertion | 04–05, 07 |
| claim reduction vs bounded admissibility | weaker formulation still requires a new test | reduced claim treated as already passed | 06 |
| component result vs integrated whole | local results remain valid in their scopes | global whole inherits local admissibility or authority | 08 |
| missing information vs non-event | absence of source support remains uncertainty | missing trace is converted into a positive non-event | 06–07 |
| non-capture vs weak-claim protection | no adequate retained whole remains after alternatives | non-capture used to shield an overstrong but reducible claim | 08 |

---

## 7. Output-Class Coverage

The formal model controls ten canonical Output Classes. The initial committed smoke suite directly instantiates five:

| Canonical class | Direct committed instance |
| --- | --- |
| `admissible` | 01, 03 |
| `admissible_with_bounded_claim` | not directly instantiated |
| `admissible_but_provisional` | not directly instantiated |
| `resolution_neutral` | not selected as a final class; retained as a local resolution result in 02 |
| `analogy_only` | not directly instantiated |
| `partially_admissible` | not directly instantiated |
| `claim_reduction_required` | 06 |
| `mandatory_stop` | 02, 07 |
| `failed_transformation` | 04, 05 |
| `non_capture` | 08 |

The absence of a direct committed instance does not remove a class from the controlled inventory. All ten classes remain represented in each routed record's candidate-assessment structure and remain controlled by the Output Class Registry and Boundary Decision Tree.

The initial suite must therefore not be described as a complete empirical or exhaustive class census.

---

## 8. Record-Level Validation Requirements

Each committed record must pass all applicable checks below.

### 8.1 Structural checks

- UTF-8 YAML parsing with duplicate-key rejection;
- validation against `../Transformation_Record.schema.json`;
- exact `record_scope` branch;
- exact operation inventory membership or declared chain sequence;
- exact routing-state vocabulary;
- complete five-field loss declaration;
- complete governance declaration;
- exactly one selected Output-Class candidate;
- selected class, route ID, and class payload agreement;
- valid controlled-value or declared-extension provenance.

### 8.2 Controlled-inventory checks

- exactly three available operation kinds: `COMPOSE`, `DECOMPOSE`, `PROJECT_AS`;
- exactly ten canonical Output Classes;
- all sixteen current admissibility rules assessed;
- all twelve current audit stages represented;
- final route IDs owned by the Boundary Decision Tree;
- no local record creates a new operation, primitive, rule, or Output Class.

### 8.3 Material boundary checks

The schema validates declared structure and controlled vocabularies. A separate semantic and boundary audit must assess whether the declarations justify the selected route.

Examples of schema-valid but materially rejectable combinations include:

- `mandatory_stop` while `PraxisPurchase` is declared as gain without an independent stop boundary;
- positive PROJECT_AS routing while origin type or source reference is not preserved;
- positive routing while the target function is source-insensitive;
- failed routing while support, continuity, and sensitivity are simultaneously declared as satisfied;
- claim reduction while the proposed weaker formulation is identical to the original claim;
- chain-level admissibility inherited only from locally admissible components.

```text
schema validity
≠ material admissibility
```

---

## 9. Negative Mutation Policy

Negative mutations are temporary audit fixtures derived from a canonical record. They test whether an invalid or inconsistent change is:

1. rejected structurally by the schema; or
2. accepted structurally but rejected by semantic, boundary, or cross-record checks.

Typical mutation families include:

- missing required fields;
- invalid enum values;
- a fabricated fourth operation;
- route/class/payload mismatch;
- broken source or claim pointer;
- erased loss field;
- unpreserved earlier result under `mandatory_stop`;
- source-insensitive function under positive PROJECT_AS routing;
- changed component order in an integrated chain;
- inherited local admissibility at chain level;
- unauthorized claim, scope, or authority expansion.

Mutation fixtures must not be committed into this directory as canonical examples. Audit reports may record the mutation description and expected rejection layer.

---

## 10. Loss, Stop, and Non-Capture Invariants

Every record must retain the canonical loss structure:

```yaml
loss:
  preserved:
  compressed:
  excluded:
  uncertain:
  irrecoverable:
```

The suite tests three distinct limit outcomes:

```text
Record 02
→ mandatory stop below the Relevance Floor

Record 07
→ mandatory stop before Reference and Functional Continuity are destroyed

Record 08
→ non-capture because no adequate retained whole claim remains
```

These outcomes are not interchangeable:

```text
mandatory stop
≠ failed transformation
≠ claim reduction
≠ non-capture
```

A stop preserves the earlier result and a future changed-ground re-entry route. Non-capture preserves captured portions, rival routes, limits, and the fact that the declared whole is not adequately retained.

---

## 11. Governance Invariants

Every canonical record must preserve the following boundaries:

- `authority_inheritance: prohibited`;
- formal validation is not substantive validation;
- application authority is not granted;
- empirical truth and causality are not machine-decided;
- semantic and normative validity are not machine-decided;
- persons are not typed, ranked, diagnosed, sanctioned, or evaluated;
- no result grants legal, political, institutional, clinical, or moral legitimacy;
- derived objects and contextual functions are not new PMS primitives;
- a new frame, granularity, level, composition, or target function creates a new testable claim rather than erasing an earlier failed claim.

---

## 12. What the Suite Can and Cannot Establish

### 12.1 The suite can establish

- that the eight committed records are structurally representable by the current schema;
- that expected operation, rule, route, class, loss, and governance fields can be populated together;
- that selected positive, failure, reduction, stop, and non-capture boundaries are formally testable;
- that cross-record IDs, claims, objects, types, functions, losses, and operation order can be audited;
- that some invalid mutations are schema-rejectable while others require material review;
- that local admissibility need not imply integrated admissibility.

### 12.2 The suite cannot establish

- empirical truth or causal correctness;
- completeness or scientific superiority of STRATA;
- inter-rater agreement on real cases;
- exhaustive coverage of all ten Output Classes;
- correctness of future canonical prose or cases;
- validation of PMS Base;
- implementation security, legal validity, governance legitimacy, or application authority;
- permanent impossibility where a record currently returns stop or non-capture.

---

## 13. Recommended Inspection Order

```text
README.md
→ ../Transformation_Record.schema.json
→ ../Operation_Registry.yaml
→ ../Output_Classes.yaml
→ ../Admissibility_Rules.yaml
→ ../Boundary_Decision_Tree.yaml
→ 01 through 07 operation-occurrence records
→ 08 integrated-chain record
→ suite-level cross-record audit
→ governing prose and Reference owners
```

For the positive-to-negative PROJECT_AS boundary, inspect:

```text
01 → 03 → 04
```

For the COMPOSE traceability boundary, inspect:

```text
01 ↔ 05
```

For the two distinct mandatory-stop grounds, inspect:

```text
02 ↔ 07
```

For anti-immunization and chain-level non-inheritance, inspect:

```text
01 → 03 → 08
```

---

## 14. Suite Gate

Record production is complete when all eight YAML files and this README are populated.

The full Formal Model v0 smoke-test gate is closed only after all of the following are verified together:

- all eight records parse with duplicate-key protection;
- all eight records validate against the current Transformation Record Schema;
- every selected class, route, class payload, rule assessment, audit stage, and loss field is coherent;
- all record IDs and claim IDs are unique;
- all cross-record pointers and handoffs resolve;
- the integrated-chain graph is acyclic and preserves component results;
- expected negative mutations fail at the correct structural or material layer;
- the README inventory matches the actual records;
- Reference and repository status statements are synchronized;
- affected fingerprints and Root provenance are synchronized;
- the final package and adversarial audits pass.

Current controlled status:

```text
record production: complete
examples README: complete
full suite-level cross-record audit: passed
Reference/status sync: complete
Root fingerprint/provenance sync: complete
Formal Model v0 internal smoke-test gate: passed
```

---

## 15. Change Discipline

Changes to a canonical example require:

1. a declared reason for the change;
2. revalidation against the current schema;
3. route, class, loss, governance, and boundary re-audit;
4. cross-record re-audit for every dependent record;
5. README inventory review;
6. Reference/status synchronization where affected;
7. Root fingerprint and provenance synchronization where registered;
8. updated package integrity checks.

A change to source object, frame, granularity, relative level, operation, target function, claim, or validity scope may create a new transformation claim and must not silently inherit an earlier result.

---

## 16. Status Boundary

This README is a navigation and control artifact for the smoke suite. It is not a theory source, not an additional schema, not a route owner, and not evidence of empirical truth, scientific confirmation, semantic or normative validity, application authority, external validity, or a completed canonical corpus. It records passage of the internal Formal Model v0 smoke-test gate only.

```text
suite legibility
≠ suite authority

record completeness
≠ substantive validation

successful smoke gate
≠ scientific confirmation
```
