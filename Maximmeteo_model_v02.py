import numpy as np

# 🌍 Domaine France métropolitaine
lat_min = 42.0
lat_max = 51.5

lon_min = -5.0
lon_max = 9.5

# 📏 Résolution approximative : 5 km
resolution_km = 5

# Nombre de points
ny = 191
nx = 291

# Grille géographique
lat = np.linspace(lat_min, lat_max, ny)
lon = np.linspace(lon_min, lon_max, nx)

LON, LAT = np.meshgrid(lon, lat)

# 🌡️ État initial
temperature = np.full((ny, nx), 15.0)
pressure = np.full((ny, nx), 1013.25)
humidity = np.full((ny, nx), 70.0)

# 💨 Vent
wind_u = np.zeros((ny, nx))
wind_v = np.zeros((ny, nx))

print("🌦️ Maximmeteo Model V0.2")
print("🌍 Grille géographique France métropolitaine")
print(f"📏 Résolution : environ {resolution_km} km")
print(f"🧮 Grille : {nx} × {ny}")
print(f"📍 Latitude : {lat_min}°N → {lat_max}°N")
print(f"📍 Longitude : {lon_min}°W → {lon_max}°E")

print(f"🌡️ Température initiale : {temperature.mean():.1f} °C")
print(f"💧 Humidité initiale : {humidity.mean():.1f} %")
print(f"🔵 Pression initiale : {pressure.mean():.2f} hPa")
import matplotlib.pyplot as plt

# 🗺️ Visualisation de la grille
plt.figure(figsize=(10, 7))

plt.scatter(
    LON[::10, ::10],
    LAT[::10, ::10],
    c=temperature[::10, ::10],
    cmap="coolwarm",
    s=8
)

plt.xlabel("Longitude (°)")
plt.ylabel("Latitude (°)")
plt.title("🌦️ Maximmeteo Model V0.2 — Grille géographique")

plt.colorbar(label="Température (°C)")
plt.grid(True)

plt.show()
51.5°N ─────────────────────
       • • • • • • • • •
       • • • • • • • • •
       • • • • • • • • •
       • • • • • • • • •
42°N  ─────────────────────
       -5°W             9.5°E
# 🌡️ Champ de température spatial
temperature = 22.0 - 0.9 * (LAT - 42.0)

# Petite perturbation thermique
temperature += 2.0 * np.exp(
    -((LON - 2.0)**2 + (LAT - 46.5)**2) / 3.0
)

# 💧 Humidité variable
humidity = 80.0 - 2.0 * (LAT - 42.0)

# 🔵 Pression avec une dépression simplifiée
pressure = 1015.0 - 12.0 * np.exp(
    -((LON - 1.0)**2 + (LAT - 47.0)**2) / 4.0
)

print("\n🌦️ Champs météorologiques générés")
print(f"🌡️ Température : {temperature.min():.1f} à {temperature.max():.1f} °C")
print(f"💧 Humidité : {humidity.min():.1f} à {humidity.max():.1f} %")
print(f"🔵 Pression : {pressure.min():.1f} à {pressure.max():.1f} hPa")
