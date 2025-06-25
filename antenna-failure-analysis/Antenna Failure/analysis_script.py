import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar datos
df = pd.read_csv("antenna_backup_logs.csv", parse_dates=["timestamp"])
df["date"] = df["timestamp"].dt.date
df["lock_binary"] = df["lock_status"].apply(lambda x: 1 if x == "LOCKED" else 0)

# Crear carpeta de salida
output_dir = "plots_per_pass"
os.makedirs(output_dir, exist_ok=True)

# Loop por cada pasada/día
unique_days = df["date"].unique()

for day in unique_days:
    df_day = df[df["date"] == day]

    fig, axs = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

    # === RSSI ===
    axs[0].plot(df_day["timestamp"], df_day["rssi"], marker='o', color='blue', label="RSSI (dBm)")
    axs[0].axhline(-110, linestyle='--', color='red', label="Threshold (-110 dBm)")
    axs[0].set_ylabel("RSSI (dBm)")
    axs[0].set_title(f"Antenna Performance – {day}")
    axs[0].legend()
    axs[0].grid(True)

    # Etiquetas de lock sobre puntos RSSI
    for i in range(len(df_day)):
        ts = df_day["timestamp"].iloc[i]
        rssi_val = df_day["rssi"].iloc[i]
        lock_txt = "LOCKED" if df_day["lock_binary"].iloc[i] == 1 else "LOST"
        axs[0].text(ts, rssi_val + 1, lock_txt, fontsize=8, ha='center', color='black', rotation=45)

    # === SNR ===
    axs[1].plot(df_day["timestamp"], df_day["snr"], marker='x', color='green', label="SNR (dB)")
    axs[1].axhline(6, linestyle='--', color='orange', label="Threshold (6 dB)")
    axs[1].set_ylabel("SNR (dB)")
    axs[1].legend()
    axs[1].grid(True)

    # Etiquetas de lock sobre puntos SNR
    for i in range(len(df_day)):
        ts = df_day["timestamp"].iloc[i]
        snr_val = df_day["snr"].iloc[i]
        lock_txt = "LOCKED" if df_day["lock_binary"].iloc[i] == 1 else "LOST"
        axs[1].text(ts, snr_val + 0.2, lock_txt, fontsize=8, ha='center', color='black', rotation=45)

    axs[1].set_xlabel("Timestamp")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"performance_{day}.png"))
    plt.close()


# ========== PARTE 2: Promedios diarios ==========

# Calcular medias diarias
daily_means = df.groupby("date")[["rssi", "snr"]].mean().reset_index()

# --- Gráfico promedio RSSI ---
plt.figure(figsize=(12, 5))
plt.plot(daily_means["date"], daily_means["rssi"], marker='o', color='blue', label="Avg RSSI (dBm)")
plt.axhline(-110, linestyle='--', color='red', label="Threshold (-110 dBm)")
plt.title("Daily Average RSSI")
plt.xlabel("Date")
plt.ylabel("Avg RSSI (dBm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "rssi_daily_avg.png"))
plt.close()

# --- Gráfico promedio SNR ---
plt.figure(figsize=(12, 5))
plt.plot(daily_means["date"], daily_means["snr"], marker='x', color='green', label="Avg SNR (dB)")
plt.axhline(6, linestyle='--', color='orange', label="Threshold (6 dB)")
plt.title("Daily Average SNR")
plt.xlabel("Date")
plt.ylabel("Avg SNR (dB)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "snr_daily_avg.png"))
plt.close()

 # === LOCK STATUS ===
plt.figure(figsize=(12, 2.5))
plt.step(df_day["timestamp"], df_day["lock_binary"], where='post', color='red')
plt.yticks([0, 1], labels=["LOST", "LOCKED"])
plt.ylim(-0.1, 1.1)
plt.title(f"Lock Status – {day}")
plt.xlabel("Timestamp")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f"lock_status_{day}.png"))
plt.close()