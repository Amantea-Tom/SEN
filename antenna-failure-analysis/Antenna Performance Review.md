# Antenna Performance Review

**Author:** Tomas Amantea  
**Date:** 2025-06-24  
**System:** Communications  
**Document Type:** Performance Review  

---

## Summary:

During a scheduled pass to test the secondary antenna(S-band backup), a command was sent to switch from the primary antenna.
A detailed analysis of the antenna's performance was performed to verify proper operation.

---

## Data Analysis Summary

- Number of passes analyzed: 10  
- Performance requirements:
  - RSSI > -110 dBm
  - SNR > 6 dB
  - Lock status > 95% of time

## Problem Summary

A persistent degradation has been detected in the reception system associated on satellite [Satellite Name or ID], as evidenced by anomalous telemetry metrics. Current measurements indicate significantly degraded performance, below nominal operational thresholds.

## Observed Metrics
Analysis of satellite passes over the last day reveals the following anomalies:

Metric	Observed Value	Expected Threshold	Comments
RSSI	~ -110 dBm	> -95 dBm	Persistently weak signal
SNR	~ 6 dB or less	> 10 dB	Low useful signal margin
Lock Status	Intermittent or absent	Sustained lock	Difficulty maintaining stable link

Note: Metrics have remained consistent across multiple passes, indicating a structural issue rather than a transient one.

![RSSI Avg](<Antenna Failure/plots_per_pass/rssi_daily_avg.png>)

![SNR Avg](<Antenna Failure/plots_per_pass/snr_daily_avg.png>)

---

## Evaluated Hypotheses

Several potential root causes have been evaluated based on telemetry, historical behavior, and cross-comparison with equivalent systems:

Hypothesis	Preliminary Assessment
Antenna misalignment	Pending analysis of AOCS logs to confirm possible angular deviation from expected pointing profile.
Hardware or cabling failure	Internal RF subsystem telemetry (e.g., temperature, current) not yet available to confirm or dismiss component failure.
Increased RF path loss	RF link model simulation is proposed to evaluate whether observed degradation aligns with increased path loss (e.g., due to damage or decoupling).
Environmental or external interference	No recorded atmospheric events or recent configuration changes to explain widespread signal degradation. Issue appears isolated to this antenna.


## Conclusions
The reception system exhibits persistent degradation inconsistent with nominal operational behavior.

RSSI and SNR values fall well below acceptable thresholds, rendering the receiver unreliable for stable signal acquisition.

The intermittent lock status confirms direct impact on reception quality.

The issue appears structural and localized to this specific antenna, with no evidence of global environmental impact.

## Recommended Actions.

Preliminary System Diagnosis
1. What should typical RSSI/SNR values ​​for this antenna look like under normal conditions?

    * Evaluate Nominal system specifications 

2. Is the degradation structural or does it begin at a specific point in time?
This requires analyzing:

    * Time trend: Check if the RSSI and SNR show a sharp drop on a specific date.

    * Associated events: Check if the following occurred on that date:

    * System reconfiguration

    * Orbital maneuver

    * Thermal changes

    * Activation/deactivation of other subsystems

## Analysis Result

Degradation Detection:

The system shows a significant drop in RSSI starting on June 15, 2025, with more than 10 dB below the nominal value (approximately -90 dBm → -110 dBm).
![Degradation Detection RSSI](<Antenna comparision/figuras/rssi_promedio.png>)

The SNR also drops starting on the same day, reinforcing the hypothesis of persistent degradation.

![Degradation Detection SNR](<Antenna comparision/figuras/snr_promedio.png>)

The other antenna maintains its nominal performance (RSSI and SNR stable).

This indicates that the satellite's general environment and orbital conditions are not the cause of the problem.

An RF chain reconfiguration was applied on June 14.

This coincides temporally with the onset of the degradation.

This could be a relevant clue for investigating internal causes (switching failure, misapplied parameters, etc.)