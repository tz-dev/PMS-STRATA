# PMS-STRATA Case Record Companion Template

> **Status:** human-readable companion for one Shared Transformation Record. This file does not create a second operation occurrence, second adjudication, or independent theory source.

## Record Identity

```text
Case / Record label: <LABEL>
Record ID:           <record_id>
Claim ID:            <claim_id>
Record scope:        operation_occurrence | integrated_chain
Routing state:       routed | formal_diagnostic
Operation:           COMPOSE | DECOMPOSE | PROJECT_AS | n/a for chain/diagnostic
Selected class:      <canonical Output Class or none for formal diagnostic>
YAML record:         ../yaml/<same-basename>.yaml
Package narrative:   <optional relative link>
```

## Tested Claim

<Write the exact bounded claim tested by this record. Preserve the reference object, operation-occurrence boundary, context, temporal scope, and excluded reach.>

## Source Field

### Reference object

<Identify the source reference object or source set and its origin typing.>

### Source coordinates

```text
Frame:          <source frame>
Granularity:    <source granularity>
Relative level:<source-relative level>
Temporal scope:<source temporal scope>
Source scope:   <bounded source scope>
```

### Source basis and Constitutive Source Trace

<Summarize which source items carry which claim components and how material source change would alter the result. Do not replace the detailed YAML trace with generic language.>

### Known gaps and Source Ceiling

<Declare known gaps and the strongest relation, reach, precision, generality, functional scope, dependence strength, and inferential distance supported by the source basis.>

## Operation Occurrence

```text
Occurrence ID: <occurrence_id>
Kind:          <COMPOSE | DECOMPOSE | PROJECT_AS>
Context:       <transformation context>
```

### Operation justification

<Explain why this operation rather than another operation or no transformation is claimed.>

### Expected praxeological difference

<State the analytical purchase without converting it into a score or automatic warrant.>

### Selection rule and operation-specific burden

<Summarize the controlling selection rule and the load-bearing operation-specific details.>

## Target Field

### Target object or contextual function

<Identify the target object. For PROJECT_AS, state the bounded target function and preserve the origin type. For COMPOSE or DECOMPOSE, do not invent a contextual target function.>

### Target coordinates and validity scope

```text
Frame:          <target frame>
Granularity:    <target granularity>
Relative level:<target-relative level>
Temporal scope:<target temporal scope>
Validity scope:<bounded validity scope>
```

## Admissibility Findings

Summarize the result of the twelve-stage audit, including:

- PraxisPurchase;
- TraceableLoad;
- Type Integrity;
- Reference, Functional, and Temporal Continuity where applicable;
- Contextual Boundedness;
- Counterfactual Sensitivity;
- Source and Calibration Ceilings;
- Selection and Loss;
- Alternatives;
- Claim and Authority Ceilings;
- Stop and Non-Capture.

```text
non-compensation confirmed: true
```

## Loss

### Preserved

- <preserved item>

### Compressed

- <compressed item or explicit none>

### Excluded

- <excluded item or explicit none>

### Uncertain

- <uncertain item or explicit none>

### Irrecoverable

- <irrecoverable item or explicit none>

## Alternatives

<Summarize serious rival COMPOSE, DECOMPOSE, or PROJECT_AS routes; no-transformation; non-translation; and unresolved alternatives. Do not claim exhaustive search without a bounded rationale.>

## Stop, Capture, and Re-entry

```text
Stop reached:              <true | false>
Stop mode:                 <mandatory | optional | n/a>
Capture limit present:     <true | false>
Genuine non_capture route: <true | false>
Re-entry contemplated:     <true | false>
```

<Explain the preserved result, capture boundary, distortion if forced, and re-entry condition where applicable.>

## Result

### Local operation result

<Summarize the operation-specific result without replacing the canonical route.>

### Status axes

```text
Support status:          <status>
Resolution-test result:  <result>
Claim disposition:       <disposition>
Capture statement:       <claim-relative statement>
```

### Canonical route

```text
Selected Output Class: <class or none for formal diagnostic>
Route ID:              <route or none>
```

<Give the class-selection rationale and preserve all non-selected findings.>

## Claim and Authority Boundary

<State the Claim Ceiling, excluded reach, prohibited inferences, external-warrant requirements, and the prohibition on authority inheritance.>

```yaml
governance:
  authority_inheritance: prohibited
  formal_validation_not_substantive_validation_acknowledged: true
  application_authority_not_granted: true
```

## Relations and Preservation

<List predecessor, successor, reduced, revised, split, sibling, rival, chain, or countercase relations. Explicitly preserve prior failures, Stops, reductions, and Non-Capture findings.>

## Artifact Boundary

```text
Markdown companion
≠ YAML record
≠ second operation occurrence
≠ second adjudication
≠ theory authority
```
