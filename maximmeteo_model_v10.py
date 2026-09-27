import numpy as np

# 🌦️ Maximmeteo Model V1.0
# Modèle régional expérimental
# 🌡️ Champ de température initial
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
temperature = 15.0 - 0.006 * (Y / 1000.0)
# 🧭 Champ de pression initial
pressure = 1013.25 - 0.01 * (X / 1000.0)
# 💨 Champ de vent initial
wind_u = np.full((ny, nx), 5.0)
wind_v = np.full((ny, nx), 0.0)
