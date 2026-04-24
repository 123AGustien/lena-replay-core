# LENA Replay Core

## Deterministic Failure Reconstruction Engine for EV Systems

LENA Replay Core is a deterministic event replay engine designed to reconstruct system failures in complex, distributed automotive architectures.

It transforms raw event logs into reproducible system state timelines, enabling engineers to trace failure causality across ECUs, sensors, and subsystems.

---

## Problem

Modern EV systems generate fragmented telemetry across multiple ECUs and subsystems. When failures occur:

- Logs are asynchronous
- Root cause chains are unclear
- Failures are non-reproducible

---

## Solution

LENA introduces deterministic replay:

> Same event log → identical system state reconstruction every time

This allows engineers to:

- Reconstruct failure sequences
- Identify trigger points
- Trace propagation across components
- Validate system behavior post-failure

---

## Core Capability

- JSON event ingestion
- Deterministic state transition engine
- Failure trigger detection
- Timeline-based visualization

---
## Example Input

```json
{ "t": 5, "component": "ECU", "state": "FAIL_SAFE_TRIGGERED" }
```

## Output

- Step-by-step system state evolution  
- Highlighted failure timestamp  
- Full system state snapshot at each step

## System Architecture

```
Event Log (JSON)
      ↓
Parser Layer
      ↓
Deterministic Replay Engine
      ↓
State Tracker
      ↓
Failure Detection Module
      ↓
Timeline Visualization (Flask UI)
```
