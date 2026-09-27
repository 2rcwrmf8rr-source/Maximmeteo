import numpy as np

# Grille du modèle
nx = 50
ny = 50

# État initial
temperature = np.full((ny, nx), 15.0)   # °C
pressure = np.full((ny, nx), 1013.25)   # hPa
humidity = np.full((ny, nx), 70.0)      # %

wind_u = np.zeros((ny, nx))             # vent est-ouest
wind_v = np.zeros((ny, nx))             # vent nord-sud

print("🌦️ Maximmeteo Model V0.1")
print(f"Grille : {nx} × {ny}")
print(f"Température moyenne : {temperature.mean():.1f} °C")
print(f"Pression moyenne : {pressure.mean():.2f} hPa")
print(f"Humidité moyenne : {humidity.mean():.1f} %")
import numpy as np

# -----------------------------
# MAXIMMETEO MODEL V0.1
# -----------------------------

nx = 50
ny = 50

# Coordonnées de la grille
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)

X, Y = np.meshgrid(x, y)

# 🌡️ Température :
# plus chaude au sud (Y=0), plus fraîche au nord (Y=1)
temperature = 22 - 8 * Y

# 💧 Humidité :
# légèrement plus humide vers l'ouest
humidity = 75 - 20 * X

# 🧭 Pression :
# petite dépression vers le centre de la grille
pressure = 1015 - 8 * np.exp(
    -((X - 0.5)**2 + (Y - 0.5)**2) / 0.08
)

# 💨 Vent initial
wind_u = np.full((ny, nx), 5.0)
wind_v = np.full((ny, nx), 2.0)

# Affichage de l'état initial
print("🌦️ Maximmeteo Model V0.1")
print(f"Grille : {nx} × {ny}")
print(f"Température : {temperature.min():.1f} à {temperature.max():.1f} °C")
print(f"Humidité : {humidity.min():.1f} à {humidity.max():.1f} %")
print(f"Pression : {pressure.min():.1f} à {pressure.max():.1f} hPa")
print(f"Vent U : {wind_u.mean():.1f}")
print(f"Vent V : {wind_v.mean():.1f}")
# -----------------------------
# ÉVOLUTION DU MODÈLE : +1 H
# -----------------------------

dt = 3600          # 1 heure en secondes
dx = 1.0           # distance simplifiée entre deux points
dy = 1.0

# Gradients spatiaux
dT_dx = np.gradient(temperature, axis=1) / dx
dT_dy = np.gradient(temperature, axis=0) / dy

dH_dx = np.gradient(humidity, axis=1) / dx
dH_dy = np.gradient(humidity, axis=0) / dy

# Advection simplifiée
temperature_new = temperature - dt * (
    wind_u * dT_dx + wind_v * dT_dy
)

humidity_new = humidity - dt * (
    wind_u * dH_dx + wind_v * dH_dy
)

# État à +1 heure
temperature = temperature_new
humidity = humidity_new

print("\n⏱️ Prévision à +1 h")
print(f"Température : {temperature.min():.1f} à {temperature.max():.1f} °C")
print(f"Humidité : {humidity.min():.1f} à {humidity.max():.1f} %")
# -----------------------------
# PRÉVISION MAXIMMETEO : 48 H
# -----------------------------

forecast = []

for hour in range(49):
    forecast.append({
        "heure": hour,
        "temperature": temperature.copy(),
        "humidity": humidity.copy(),
        "pressure": pressure.copy(),
        "wind_u": wind_u.copy(),
        "wind_v": wind_v.copy()
    })

    if hour == 48:
        break

    # Évolution d'une heure
    dT_dx = np.gradient(temperature, axis=1)
    dT_dy = np.gradient(temperature, axis=0)

    dH_dx = np.gradient(humidity, axis=1)
    dH_dy = np.gradient(humidity, axis=0)

    temperature = temperature - (
        wind_u * dT_dx + wind_v * dT_dy
    )

    humidity = humidity - (
        wind_u * dH_dx + wind_v * dH_dy
    )

print("\n🌦️ Prévision Maximmeteo")
print("Échéance : 48 heures")
print(f"Nombre d'échéances : {len(forecast)}")

for data in forecast[::6]:
    print(
        f"T+{data['heure']:02d}h | "
        f"T moyenne : {data['temperature'].mean():.1f} °C | "
        f"Humidité moyenne : {data['humidity'].mean():.1f} %"
    )
