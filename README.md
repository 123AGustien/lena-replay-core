
## 🧊 System Freeze (v1.0)

LENA Replay Core operates under a **frozen deterministic baseline (v1.0)**.

This ensures:

- Deterministic event replay is locked
- Failure reconstruction is fully reproducible
- Timeline reconstruction is stable and consistent
- Identical input logs always produce identical system state outputs

---

## 🔒 Frozen Components

The following subsystems are frozen in v1.0:

- Event log parser
- Deterministic replay engine
- State tracking system
- Failure propagation reconstruction logic
- Timeline reconstruction pipeline

---

## 🌿 Evolution Rule

- `v1.0` → immutable deterministic replay baseline
- `develop` → experimental replay enhancements
- `v1.1+` → validated system improvements

---

## 🧠 System Boundary

This system is strictly defined as a:

**deterministic failure reconstruction and analysis engine**

It is used for:
- Debugging system failures
- Reconstructing event causality
- Replaying distributed system states

It is **not a live control system**.


# LENA Replay Core – Automotive Deterministic Failure Reconstruction Engine


## 🚀 Live Demo

[![Run Demo](https://img.shields.io/badge/Run%20Demo-GitHub%20Actions-blue?style=for-the-badge)](https://github.com/123AGustien/lena-replay-core/actions/workflows/poc-run.yml)

## Overview

LENA Replay Core is a deterministic event replay system designed for automotive diagnostics and ECU failure reconstruction.

It enables reproducible system-state reconstruction from event logs, allowing engineers to trace failure causality across distributed vehicle systems.

---

## Primary Use Case

- Automotive diagnostics
- EV system failure reconstruction
- ECU-level fault tracing
- Distributed system behavior analysis

---

## Core Pipeline

Event Log (JSON)  
→ Parser  
→ Deterministic Replay Engine  
→ State Tracker  
→ Failure Detection Module  
→ Timeline Reconstruction  

---

## Key Feature

**Deterministic Replay Guarantee**

Same input event log → identical system state reconstruction every execution

---

## Expected Output

- Step-by-step failure propagation log  
- Replay validation result (`True` if deterministic consistency is achieved)  

---

## Engineering Note

This project is intended for evaluation of deterministic failure reconstruction in automotive system diagnostics and is focused on:

- Reproducibility  
- Traceability  
- System-level fault analysis
