import numpy as np

# 🌦️ Maximmeteo Model V1.0
# Modèle régional expérimental
# 🌡️ Champ de température initial
temperature = 15.0 - 0.006 * (Y / 1000.0)
# 🧭 Champ de pression initial
pressure = 1013.25 - 0.01 * (X / 1000.0)
# 💨 Champ de vent initial
wind_u = np.full((ny, nx), 5.0)
wind_v = np.full((ny, nx), 0.0)
