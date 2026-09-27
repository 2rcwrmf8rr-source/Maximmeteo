# 🌡️ Advection de température
dT_dx = np.gradient(temperature, dx, axis=1)
dT_dy = np.gradient(temperature, dy, axis=0)

advection_temperature = (
    wind_u * dT_dx +
    wind_v * dT_dy
)

temperature -= dt * advection_temperature
import numpy as np

# 🌦️ Maximmeteo Model V0.8
# Modèle régional expérimental

# 📏 Résolution de la grille
dx = 5000.0
dy = 5000.0

# 🌍 Domaine : 1000 × 1000 km
domain_x = 1_000_000.0
domain_y = 1_000_000.0

# 🧮 Nombre de points
nx = int(domain_x / dx) + 1
ny = int(domain_y / dy) + 1

# 📍 Coordonnées
x = np.arange(nx) * dx
y = np.arange(ny) * dy
X, Y = np.meshgrid(x, y)

# 🌡️ État initial
temperature = np.full((ny, nx), 15.0)
pressure = np.full((ny, nx), 1013.25)
humidity = np.full((ny, nx), 70.0)

# 💨 Vent
wind_u = np.zeros((ny, nx))
wind_v = np.zeros((ny, nx))

print("🌦️ Maximmeteo Model V0.8")
print(f"Grille : {nx} × {ny} points")
print(f"Résolution : {dx / 1000:.1f} km")
# ⏱️ Pas de temps
dt = 300.0  # 5 minutes en secondes

# ⏳ Durée de la simulation
forecast_hours = 48
forecast_seconds = forecast_hours * 3600

# 🔢 Nombre de pas de temps
n_steps = int(forecast_seconds / dt)
# 🔄 Boucle temporelle
for step in range(n_steps):

    # ⏱️ Temps écoulé
    current_time = step * dt
      # 🌡️ Advection de température
    dT_dx = np.gradient(temperature, dx, axis=1)
    dT_dy = np.gradient(temperature, dy, axis=0)

    advection_temperature = (
        wind_u * dT_dx +
        wind_v * dT_dy
    )

    temperature -= dt * advection_temperature
