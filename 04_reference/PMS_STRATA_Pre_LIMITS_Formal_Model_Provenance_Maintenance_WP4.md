# PMS-STRATA Pre-LIMITS Formal Model Provenance Maintenance — WP4

**Status:** completed  
**Input Source of Truth:** PMS-STRATA Source-of-Truth ZIP 259  
**Output release:** PMS-STRATA Source-of-Truth ZIP 260  
**Scope:** M41-PRE-13 and M41-PRE-14  
**Authority:** maintenance and provenance record only; no independent theory, Rule, operation, Output Class, case-result, or application authority

## 1. Purpose

WP4 removes ambiguity between active Formal Model assembly provenance and older build history, and makes the current operative rule core visibly distinguishable from accumulated chapter, WP, review, and maintenance handoffs.

The governing separations are:

```text
build-input snapshot
≠ current semantic authority

current operative rule core
≠ historical production trace

historical trace retention
≠ current-status inheritance
```

## 2. M41-PRE-13 — Assembly Provenance

The active Root assembly basis now records:

```yaml
built_from_snapshot: PMS-STRATA_Source_of_Truth_ZIP_259.zip
built_from_snapshot_sha256: 5d252aa46e85e6fc6d08c20f9a39bbf0e7ab1f03c96c7f5e0e94efecf5917fc4
```

The former active ZIP-147 reference was removed. The snapshot records the verified input used for this maintenance assembly. It does not override the repository authority order, confer Source-of-Truth status on the Root model, or establish semantic validity.

## 3. M41-PRE-14 — Model Layering

`Admissibility_Rules.yaml` now declares three layers:

1. **Current operative rule core** — the existing sixteen-Rule formalization, controlled local vocabularies, twelve-stage audit, non-compensation, Claim Reduction, Stop, Non-Capture, anti-immunization, ceilings, operation overlays, and formal boundary.
2. **Integration metadata** — current cross-artifact routing and ownership metadata without independent rule semantics.
3. **Historical production trace** — chapter, WP, review, re-anchoring, and maintenance handoffs retained as non-normative provenance.

Historical traces may not:

- define a new Rule, operation, Output Class, or audit stage;
- override current core semantics or controlled vocabularies;
- convert stale `pending` or `next step` language into current status;
- create case results, truth, authority, legitimacy, or application warrant.

No large refactor or second rule registry was introduced. Existing trace records remain in place and are classified rather than migrated.

## 4. Synchronized Formal Artifacts

```text
Admissibility_Rules.yaml
0.1.148 → 0.1.149

PMS-STRATA.yaml
0.1.206 → 0.1.207
```

The Root component descriptor for `admissibility_rules` is synchronized to the current component version and content fingerprint.

## 5. Preserved Boundaries

```text
operations
→ exactly 3

Output Classes
→ exactly 10

Rules
→ exactly 16

audit stages
→ exactly 12

canonical Loss fields
→ exactly 5

artifact-complete RETYPE lock
→ mandatory_stop

Chapter 41 canonical prose
→ not started
```

WP4 creates no new schema field, case, smoke fixture, Transformation Record, substantive result, or authority inheritance.

## 6. Handoff

Next controlled step:

```text
Maintenance WP5
→ integrated parse, schema, record, inventory, fingerprint, link, status, and boundary verification
→ next Source-of-Truth release
→ Chapter 41 WP1 only after the completion gate passes
```
