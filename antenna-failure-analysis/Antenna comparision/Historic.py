
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rcParams["figure.figsize"] = (14, 5)
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.linestyle"] = ":"
plt.rcParams["grid.alpha"] = 0.7

def main():
    # Cargar archivos CSV
    df_afectada = pd.read_csv("metrics_antena_afectada.csv", parse_dates=["timestamp"])
    df_comparativa = pd.read_csv("metrics_antena_comparativa.csv", parse_dates=["timestamp"])
    df_events = pd.read_csv("event_log.csv", parse_dates=["date"])

    # Crear carpeta de salida si no existe
    output_dir = "figuras"
    os.makedirs(output_dir, exist_ok=True)

    # Preparar datos diarios
    df_afectada['day'] = df_afectada['timestamp'].dt.date
    df_comparativa['day'] = df_comparativa['timestamp'].dt.date

    daily_afectada = df_afectada.groupby('day').agg({'RSSI_dBm':'mean','SNR_dB':'mean','Lock':'mean'}).reset_index()
    daily_comparativa = df_comparativa.groupby('day').agg({'RSSI_dBm':'mean','SNR_dB':'mean','Lock':'mean'}).reset_index()

    # Baseline y detección de degradación
    rssi_baseline = daily_afectada['RSSI_dBm'].iloc[:5].mean()
    degradacion = daily_afectada[daily_afectada['RSSI_dBm'] < rssi_baseline - 10]
    degradation_day = degradacion['day'].min() if not degradacion.empty else None

    # --- Gráfico RSSI ---
    plt.figure()
    plt.plot(daily_afectada['day'], daily_afectada['RSSI_dBm'], marker='o', label='Antena Afectada')
    plt.plot(daily_comparativa['day'], daily_comparativa['RSSI_dBm'], marker='o', label='Antena Comparativa')
    plt.axhline(rssi_baseline, linestyle='--', color='gray', label='RSSI Nominal Ref.')
    if degradation_day:
        plt.axvline(degradation_day, linestyle='--', color='red', label=f'Inicio degradación: {degradation_day}')
    plt.title('RSSI diario promedio')
    plt.xlabel('Fecha')
    plt.ylabel('RSSI [dBm]')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "rssi_promedio.png"))
    plt.close()

    # --- Gráfico SNR ---
    plt.figure()
    plt.plot(daily_afectada['day'], daily_afectada['SNR_dB'], marker='o', label='Antena Afectada')
    plt.plot(daily_comparativa['day'], daily_comparativa['SNR_dB'], marker='o', label='Antena Comparativa')
    plt.axhline(daily_afectada['SNR_dB'].iloc[:5].mean(), linestyle='--', color='gray', label='SNR Nominal Ref.')
    if degradation_day:
        plt.axvline(degradation_day, linestyle='--', color='red', label=f'Inicio degradación: {degradation_day}')
    plt.title('SNR diario promedio')
    plt.xlabel('Fecha')
    plt.ylabel('SNR [dB]')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "snr_promedio.png"))
    plt.close()

    # --- Gráfico RSSI con eventos ---
    plt.figure()
    plt.plot(daily_afectada['day'], daily_afectada['RSSI_dBm'], marker='o', label='Antena Afectada')
    for _, row in df_events.iterrows():
        plt.axvline(row['date'], linestyle=':', color='lightgray', alpha=0.5)
        plt.text(row['date'], rssi_baseline - 12, row['event'], rotation=90, fontsize=8, alpha=0.7)
    plt.axhline(rssi_baseline, linestyle='--', color='gray', label='RSSI Nominal Ref.')
    if degradation_day:
        plt.axvline(degradation_day, linestyle='--', color='red', label='Inicio degradación')
    plt.title('RSSI con eventos del sistema')
    plt.xlabel('Fecha')
    plt.ylabel('RSSI [dBm]')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "rssi_eventos.png"))
    plt.close()

if __name__ == "__main__":
    main()
