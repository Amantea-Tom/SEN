import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression

df = pd.read_csv('gyro_thermal_drift_case.csv', parse_dates=['timestamp'])

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Calcular error entre actitud estimada y real
df['error_x'] = df['est_att_x'] - df['true_att_x']
df['error_y'] = df['est_att_y'] - df['true_att_y']
df['error_z'] = df['est_att_z'] - df['true_att_z']
# Agregar columna de fecha (sin hora)
df['hour'] = df['timestamp'].dt.floor('15min')

# Agrupar por hora
interval_mean = df.groupby('hour')[['error_x', 'error_y', 'error_z']].mean()
# Graficar errores
fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True)
axs[0].plot(df['timestamp'], df['error_x'], label='Error X', color='tab:red')
axs[1].plot(df['timestamp'], df['error_y'], label='Error Y', color='tab:blue')
axs[2].plot(df['timestamp'], df['error_z'], label='Error Z', color='tab:green')

axs[0].set_ylabel("Error X (deg)")
axs[1].set_ylabel("Error Y (deg)")
axs[2].set_ylabel("Error Z (deg)")
axs[2].set_xlabel("Timestamp")

for ax in axs:
    ax.legend()
    ax.grid(True)

# Inicializar gráfico
plt.figure(figsize=(12, 7))

colors = {'error_x': 'red', 'error_y': 'blue', 'error_z': 'green'}
labels = {'error_x': 'Error X', 'error_y': 'Error Y', 'error_z': 'Error Z'}

# Plot de puntos + regresión
for i, err in enumerate(['error_x', 'error_y', 'error_z']):
    X = df['gyro_temp'].values.reshape(-1, 1)
    y = df[err].values

    # Scatter plot
    plt.scatter(X, y, color=colors[err], alpha=0.3, label=labels[err])

    # Ajuste lineal
    model = LinearRegression()
    model.fit(X, y)              # Ajusta la recta a los datos
    y_pred = model.predict(X)    # Predice los valores de error según la recta
    r2 = model.score(X, y)       # R²: qué tan bien se ajusta la recta a los datos

    # Línea de regresión
    plt.plot(X, y_pred, color=colors[err], linewidth=2, label=f"{labels[err]} Fit (R² = {r2:.2f})")

# Estética
plt.title("Attitude Estimation Error vs Gyro Temperature", fontsize=14)
plt.xlabel("Gyro Temperature (°C)", fontsize=12)
plt.ylabel("Attitude Estimation Error (deg)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()

# Guardar
plt.savefig(os.path.join(output_dir, "error_vs_gyro_temp.png"))
plt.close()

# Histogramas
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

for i, axis in enumerate(['error_x', 'error_y', 'error_z']):
    data = df[axis]
    mean = data.mean()
    std = data.std()
    
    axs[i].hist(data, bins=30, color='skyblue', edgecolor='black')
    axs[i].axvline(mean, color='red', linestyle='--', label=f'Mean = {mean:.3f}°')
    axs[i].set_title(f'{axis.upper()} (std = {std:.3f}°)')
    axs[i].set_xlabel("Error (deg)")
    axs[i].set_ylabel("Count")
    axs[i].legend()

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "attitude_error_distribution.png"))
plt.close()


# Graficar
plt.figure(figsize=(14, 6))
plt.plot(interval_mean.index, interval_mean['error_x'], label='Error X', color='tab:red', marker='o')
plt.plot(interval_mean.index, interval_mean['error_y'], label='Error Y', color='tab:blue', marker='o')
plt.plot(interval_mean.index, interval_mean['error_z'], label='Error Z', color='tab:green', marker='o')

plt.title("Mean Attitude Error Every 15 Minutes")
plt.xlabel("Time")
plt.ylabel("Mean Error (deg)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Guardar
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, "quarter_hour_error_mean.png"))
plt.close()