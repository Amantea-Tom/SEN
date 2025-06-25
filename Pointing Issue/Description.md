# AOCS Pointing Diagnostic Case Study

This project simulates a diagnostic case focused on a Pointing issue in a satellite's  antenna system.


## Context

A satellite has experienced **intermittent signal losses** during downlink sessions, even though the attitude control system (AOCS) reports seemingly nominal values. The operations team suspects a **pointing misalignment** between the antenna's line-of-sight and the ground station target.


The main idea is to analyze telemetry logs and determine if the loss of lock correlates with poor pointing performance or other anomalies.

---

## Dataset

The file `aocs_logs.csv` contains one day of telemetry sampled every minute. Each row includes:

- `timestamp`: Timestamp of the observation
- `roll`, `pitch`, `yaw`: Attitude angles in degrees
- `antenna_angle_error`: Angular misalignment between antenna direction and target (in degrees)
- `lock_status`: Whether communication was `LOCKED` or `LOST`
- `sun_vector_angle`: Angle between Sun and satellite
- `eclipse`: Boolean indicating if the satellite is in eclipse

---

## Objectives


1. **Visualize attitude evolution**: Plot roll, pitch, and yaw across the day.
2. **Inspect antenna pointing error**:
   - Identify when the angle exceeds acceptable bounds.
   - Correlate these events with `lock_status = LOST`.
3. **Investigate potential causes**:
   - Does the error increase during eclipse?
   - Is there a drift in one specific attitude axis?
4. **Propose a hypothesis**:
   - Offset in frame transformation?
   - Drift in sensors?
   - Eclipse-induced degradation?

---

## Outputs


The script `script_aocs_base.py` generates:

- `attitude_angles.png`: Time series of roll, pitch, yaw
- `antenna_error_lock.png`: Pointing error with lock loss events marked
- `sun_vector_eclipse.png`: Sun angle with eclipse periods shaded

All plots are saved to the `plots/` directory.

---

## Suggestion

A pointing error > 7° is considered problematic. Analize patterns in angular drift, especially around the times when lock is lost.

---

## Final Report

See `Pointing Issue` for a detailed analysis of the problem, conclusions, and recommended actions.

---

## Author

Tomás Amantea – Electronics/RF/Field Application Engineering  
**Status**: Self-driven practice project  
**Goal**: Reinforce applied systems thinking and signal diagnostics in aerospace contexts