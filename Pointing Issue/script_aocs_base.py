
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Data
df = pd.read_csv("aocs_logs.csv", parse_dates=["timestamp"])

# create output file if didnt exist
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Plot actitud (roll, pitch, yaw)
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["roll"], label="Roll (°)")
plt.plot(df["timestamp"], df["pitch"], label="Pitch (°)")
plt.plot(df["timestamp"], df["yaw"], label="Yaw (°)")
plt.title("Attitude Angles Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Angle (°)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "attitude_angles.png"))
plt.close()

# Plot antenna angle error + lock status
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["antenna_angle_error"], label="Antenna Angle Error (°)", color='orange')
plt.axvline(df["timestamp"][df["lock_status"] == "LOST"].iloc[0], color='red', alpha=0.1, label="Lock LOST")
for i in range(len(df)):
    if df["lock_status"].iloc[i] == "LOST":
        plt.axvline(df["timestamp"].iloc[i], color='red', alpha=0.05)
plt.title("Antenna Pointing Error & Lock Status")
plt.xlabel("Timestamp")
plt.ylabel("Error (°)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "antenna_error_lock.png"))
plt.close()

# Plot eclipse status
plt.figure(figsize=(12, 3))
plt.plot(df["timestamp"], df["sun_vector_angle"], label="Sun Vector Angle (°)", color='green')
plt.fill_between(df["timestamp"], 80, 100, where=df["eclipse"], color='gray', alpha=0.3, label="Eclipse")
plt.title("Sun Vector Angle & Eclipse Periods")
plt.xlabel("Timestamp")
plt.ylabel("Angle (°)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "sun_vector_eclipse.png"))
plt.close()

print("Plots saved in ../plots/")
