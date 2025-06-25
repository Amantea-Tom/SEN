# Gyroscope Thermal Drift Case

This project investigates a subtle attitude estimation error potentially caused by thermal drift in the gyroscope sensor.

## Context

The satellite has not shown critical failures but operators have observed small, systematic pointing offsets accumulating over time. There is a hypothesis that these are correlated with thermal variations in the gyroscope.

## Dataset

`gyro_logs.csv` contains 900 rows (10 orbital passes). Each row includes:

- `timestamp`
- `gyro_x`, `gyro_y`, `gyro_z`: angular velocities
- `est_att_*` and `true_att_*`: estimated vs actual attitude angles
- `gyro_temp`: internal temperature of the gyroscope
- `bias_flag`: system flag set when bias is detected (late in timeline)

## Objectives

1. Detect if attitude estimation errors are accumulating.
2. Determine correlation between thermal variations and drift.
3. Assess whether the system's estimator adapts or fails to compensate.

All results will be visualized using custom scripts.

## Outputs


The script `script_gyro.py` generates:

- `attitude_angles.png`: Time series of roll, pitch, yaw
- `antenna_error_lock.png`: Pointing error with lock loss events marked
- `sun_vector_eclipse.png`: Sun angle with eclipse periods shaded

All plots are saved to the `plots/` directory.

---

## Suggestion


---

## Final Report

See `` for a detailed analysis of the problem, conclusions, and recommended actions.

---

## Author

Tomás Amantea – Electronics/RF/Field Application Engineering  
**Status**: Self-driven practice project  
**Goal**: Reinforce applied systems thinking and signal diagnostics in aerospace contexts