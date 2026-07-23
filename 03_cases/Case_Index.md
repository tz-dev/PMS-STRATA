# PMS-STRATA Case Index

**Version:** 0.1.6  
**Status:** provisional Part-I-locked case-corpus index  
**Authority:** navigation and artifact registry only; no independent theory authority  
**Current production stage:** Part I — PATH provisionally locked after Chapter 17 WP4 integrated audit; Chapter 18 Preparation is next

```text
case index entry
≠ theory definition
≠ empirical proof
≠ automatic Output-Class decision
```

## Instantiated Cases

| Case ID | Title | Class | Operation | Local result | Canonical mapping | Lock-critical | Artifacts |
|---|---|---|---|---|---|---|---|
| `C17-ATTR-01` | Trajectory or Attractor? | `confusion_case` | `COMPOSE` | admissible single Trajectory with Attractor-function claim withheld | `admissible_with_bounded_claim` | no | [MD](markdown/C17-ATTR-01_Trajectory_or_Attractor.md) · [YAML](yaml/C17-ATTR-01_Trajectory_or_Attractor.yaml) |
| `C17-BRANCH-01` | Branching Path | `positive_case` | `COMPOSE` | admissible branching Path | `admissible` | no | [MD](markdown/C17-BRANCH-01_Branching_Path.md) · [YAML](yaml/C17-BRANCH-01_Branching_Path.yaml) |
| `C17-CHRON-01` | Chronology Presented as Path | `countercase` | `COMPOSE` | failed Path claim with retained chronology | `claim_reduction_required` | no | [MD](markdown/C17-CHRON-01_Chronology_Presented_as_Path.md) · [YAML](yaml/C17-CHRON-01_Chronology_Presented_as_Path.yaml) |
| `C17-FALSEL-01` | False Central Non-Event | `countercase` | `COMPOSE` | central Λ claim withdrawn with retained event field | `claim_reduction_required` | no | [MD](markdown/C17-FALSEL-01_False_Central_Non_Event.md) · [YAML](yaml/C17-FALSEL-01_False_Central_Non_Event.yaml) |
| `C17-HISTORY-01` | Similar End States, Different Histories | `positive_case` | `COMPOSE` | admissible dimension-specific Path-Dependence claim across similar endpoints | `admissible_with_bounded_claim` | no | [MD](markdown/C17-HISTORY-01_Similar_End_States_Different_Histories.md) · [YAML](yaml/C17-HISTORY-01_Similar_End_States_Different_Histories.yaml) |
| `C17-LAMBDA-01` | Trajectory with a Central Non-Event | `positive_case` | `COMPOSE` | admissible source-sensitive Trajectory with central Λ | `admissible` | yes | [MD](markdown/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.md) · [YAML](yaml/C17-LAMBDA-01_Trajectory_with_Central_Non_Event.yaml) |
| `C17-LINEAR-01` | Simple Linear Path | `positive_case` | `COMPOSE` | admissible bounded Path | `admissible` | no | [MD](markdown/C17-LINEAR-01_Simple_Linear_Path.md) · [YAML](yaml/C17-LINEAR-01_Simple_Linear_Path.yaml) |
| `C17-MACRO-01` | Macro-Label without Traceable Path | `countercase` | `COMPOSE` | failed source-indifferent macro-Trajectory composition | `failed_transformation` | yes | [MD](markdown/C17-MACRO-01_Macro_Label_without_Traceable_Path.md) · [YAML](yaml/C17-MACRO-01_Macro_Label_without_Traceable_Path.yaml) |
| `C17-OMEGA-01` | Composition through Omitted Asymmetry | `countercase` | `COMPOSE` | failed Trajectory composition through omitted asymmetry | `failed_transformation` | no | [MD](markdown/C17-OMEGA-01_Composition_through_Omitted_Asymmetry.md) · [YAML](yaml/C17-OMEGA-01_Composition_through_Omitted_Asymmetry.yaml) |
| `C17-PROJ-01` | Path or Projection? | `confusion_case` | `COMPOSE` | admissible source-sensitive Trajectory with projection claim separated | `admissible_with_bounded_claim` | yes | [MD](markdown/C17-PROJ-01_Path_or_Projection.md) · [YAML](yaml/C17-PROJ-01_Path_or_Projection.yaml) |
| `C17-RES-01` | Path or Resolution Drift? | `confusion_case` | `DECOMPOSE` | resolution-neutral finer reconstruction; no new Path or stronger historical claim | `resolution_neutral` | no | [MD](markdown/C17-RES-01_Path_or_Resolution_Drift.md) · [YAML](yaml/C17-RES-01_Path_or_Resolution_Drift.yaml) |
| `C17-TEL-01` | Teleological Composition | `countercase` | `COMPOSE` | failed teleological Trajectory composition | `failed_transformation` | no | [MD](markdown/C17-TEL-01_Teleological_Composition.md) · [YAML](yaml/C17-TEL-01_Teleological_Composition.yaml) |
| `C17-WEAKPD-01` | Repeated Pattern with Weak Path Dependence | `positive_case` | `COMPOSE` | admissible repeated-pattern Path with weak order dependence | `admissible_with_bounded_claim` | no | [MD](markdown/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.md) · [YAML](yaml/C17-WEAKPD-01_Repeated_Pattern_with_Weak_Path_Dependence.yaml) |

## WP4 Provisional PATH-Lock Status

- five positive cases, five countercases, and three confusion cases instantiated;
- thirteen Markdown reconstructions and thirteen schema-valid Shared Transformation Records present;
- twelve-stage record audit complete in every case;
- the twenty-question integrated PATH Local Audit passes;
- complete five-part Loss, alternatives, Output mapping, Stop, Non-Capture, Claim Scope, and governance boundaries are present across the corpus;
- all three lock-critical artifacts are present: `C17-LAMBDA-01`, `C17-MACRO-01`, `C17-PROJ-01`;
- all six remaining Chapter-17 integrated duties are complete;
- Part-I lock readiness passes;
- the integrated Chapters 9–17 audit passes;
- Part I — PATH is provisionally locked;
- Chapter 18 Preparation is the next controlled step.

```text
Chapter 17 complete
+ integrated WP4 audit passed
= Part I provisionally locked

Part I provisional lock
≠ final STRATA lock
```

## Index Boundary

This index records artifact identity, class, operation, local result, canonical mapping, status, and ownership. It does not determine substantive case truth, select a class automatically, revise canonical prose, or grant application authority.

```yaml
governance:
  authority_inheritance: prohibited
```

Machine-readable companion: [`Case_Index.yaml`](Case_Index.yaml)
