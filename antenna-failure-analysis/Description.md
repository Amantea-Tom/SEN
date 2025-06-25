# Antenna Failure Analysis

This project simulates a diagnostic case focused on degraded performance in a satellite's  antenna system.

##  Context

A ground station detected persistent issues with the satellite’s backup antenna during scheduled passes. Key telemetry metrics—RSSI, SNR, and lock status—showed degraded values, suggesting potential hardware, alignment, or RF problems.

The goal was to analyze telemetry logs, visualize signal behavior across passes, and determine the root cause of performance degradation.

---

##  Objectives

- Parse and visualize antenna performance logs across multiple satellite passes.
- Detect anomalies or trends in RSSI, SNR, and lock status.
- Correlate lock failures with signal degradation.
- Suggest actionable next steps for satellite operations or maintenance.

---

## Dataset

- `antenna_backup_logs.csv`: Simulated telemetry logs with the following fields:
  - `timestamp`
  - `rssi` (Received Signal Strength Indicator in dBm)
  - `snr` (Signal-to-Noise Ratio in dB)
  - `lock_status` (LOCKED / LOST)

---

## Tools & Methods

- **Python**: For data parsing, processing, and visualization.
- **Matplotlib & Pandas**: To generate detailed per-pass and aggregate plots.
- **Markdown reporting**: For concise technical documentation.

---

##  Outputs

Plots are generated and saved in `/plots_per_pass/`:

- `performance_YYYY-MM-DD.png`: Daily RSSI & SNR plots with lock annotations.
- `lock_status_YYYY-MM-DD.png`: Binary lock state over time.
- `rssi_daily_avg.png`: Average RSSI across all passes.
- `snr_daily_avg.png`: Average SNR across all passes.

---

## Final Report

See `Antenna Performance Review` for a detailed analysis of the problem, conclusions, and recommended actions.

---

## Author

Tomás Amantea – Electronics/RF/Field Application Engineering  
**Status**: Self-driven practice project  
**Goal**: Reinforce applied systems thinking and signal diagnostics in aerospace contexts