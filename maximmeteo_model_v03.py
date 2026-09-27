import numpy as np

# 🌦️ Maximmeteo Model V0.3
# Grille régionale métrique

# 📏 Résolution
dx = 5000.0  # 5 km
dy = 5000.0  # 5 km

# 🌍 Domaine : 1000 × 1000 km
domain_x = 1_000_000.0
domain_y = 1_000_000.0

# 🧮 Nombre de points
nx = int(domain_x / dx) + 1
ny = int(domain_y / dy) + 1

# 📍 Coordonnées en mètres
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

print("🌦️ Maximmeteo Model V0.3")
print("🗺️ Grille régionale métrique")
print(f"📏 Résolution : {dx / 1000:.1f} km")
print(f"📐 Domaine : {domain_x / 1000:.0f} × {domain_y / 1000:.0f} km")
print(f"🧮 Grille : {nx} × {ny}")
print(f"📊 Nombre de points : {nx * ny:,}")

print(f"🌡️ Température : {temperature.mean():.1f} °C")
print(f"🔵 Pression : {pressure.mean():.2f} hPa")
print(f"💧 Humidité : {humidity.mean():.1f} %")
# 🌍 Référence géographique du domaine
center_lat = 46.5
center_lon = 2.5

print("\n🌍 Référence géographique")
print(f"Latitude centrale : {center_lat}°N")
print(f"Longitude centrale : {center_lon}°E")
# 🇫🇷 Projection Lambert conforme conique
lat0 = np.radians(46.5)
lon0 = np.radians(2.5)

lat1 = np.radians(44.0)
lat2 = np.radians(49.0)

# Constantes de la projection
n = (
    np.log(np.cos(lat1) / np.cos(lat2))
    /
    np.log(
        np.tan(np.pi / 4 + lat2 / 2)
        /
        np.tan(np.pi / 4 + lat1 / 2)
        omega = 7.2921159e-5  # vitesse angulaire de rotation terrestre (rad/s)

latitude_rad = np.deg2rad(LAT)
f = 2.0 * omega * np.sin(latitude_rad)
    )
)

F = (
    np.cos(lat1)
    *
    np.tan(np.pi / 4 + lat1 / 2) ** n
    / n
)

rho0 = F / np.tan(np.pi / 4 + lat0 / 2) ** n

# Coordonnées projetées relatives au centre
x_proj = X - domain_x / 2
y_proj = Y - domain_y / 2

# Rayon depuis l'origine
rho = np.sqrt(
    x_proj**2 +
    (rho0 - y_proj)**2
)

theta = np.arctan2(
    x_proj,
    rho0 - y_proj
)

# Conversion inverse vers latitude / longitude
latitude = (
    2 * np.arctan(
        (F / rho) ** (1 / n)
    )
    - np.pi / 2
)

longitude = lon0 + theta / n

# Conversion radians → degrés
latitude = np.degrees(latitude)
longitude = np.degrees(longitude)

print("\n🗺️ Projection Lambert")
print(
    f"Latitude : {latitude.min():.2f}° → "
    f"{latitude.max():.2f}°"
)
print(
    f"Longitude : {longitude.min():.2f}° → "
    f"{longitude.max():.2f}°"
)
import json

# 📡 Sortie du modèle
forecast_data = {
    "model": "Maximmeteo Model",
    "version": "V0.3",
    "resolution_km": dx / 1000,
    "grid": {
        "nx": nx,
        "ny": ny
    },
    "domain": {
        "center_lat": center_lat,
        "center_lon": center_lon
    },
    "initial_state": {
        "temperature_mean": float(temperature.mean()),
        "pressure_mean": float(pressure.mean()),
        "humidity_mean": float(humidity.mean())
    }
}

# 💾 Création du fichier JSON
with open("forecast.json", "w", encoding="utf-8") as file:
    json.dump(forecast_data, file, indent=2, ensure_ascii=False)

print("\n📡 Sortie créée : forecast.json")
print("✅ Données Maximmeteo prêtes à être utilisées par le site")
cor_u = f * wind_v
cor_v = -f * wind_u

wind_u += dt * cor_u
wind_v += dt * cor_v
print("\n=== TEST DE STABILITÉ V0.7 — 48 H ===")

wind_speed = np.sqrt(wind_u**2 + wind_v**2)

print(f"Vent min : {wind_speed.min():.2f} m/s")
print(f"Vent max : {wind_speed.max():.2f} m/s")

print(f"Pression min : {pressure.min():.2f} hPa")
print(f"Pression max : {pressure.max():.2f} hPa")

print(f"Température min : {temperature.min():.2f} °C")
print(f"Température max : {temperature.max():.2f} °C")

print(f"Humidité min : {humidity.min():.2f} %")
print(f"Humidité max : {humidity.max():.2f} %")

# Vérification des valeurs non finies
if not np.isfinite(wind_u).all():
    print("⚠️ Instabilité détectée dans wind_u")

if not np.isfinite(wind_v).all():
    print("⚠️ Instabilité détectée dans wind_v")

if not np.isfinite(pressure).all():
    print("⚠️ Instabilité détectée dans pressure")

if not np.isfinite(temperature).all():
    print("⚠️ Instabilité détectée dans temperature")

if not np.isfinite(humidity).all():
    print("⚠️ Instabilité détectée dans humidity")

print("=== FIN DU TEST ===")
