import json
import matplotlib.pyplot as plt

# Charger les données depuis le fichier JSON
with open("reproduction_statistiques.json", "r") as f:
    data = json.load(f)

# Extraire les données des chronons
chronons = [entry["chronon"] for entry in data["chronons"]][:100]
poissons_nes = [entry["poissons_nes"] for entry in data["chronons"]][:100]
requin_nes = [entry["requin_nes"] for entry in data["chronons"]][:100]

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(chronons, poissons_nes, label="Reproduction des Poissons")
plt.plot(chronons, requin_nes, label="Reproduction des Requins")

# Ajouter des labels et un titre
plt.xlabel("Chronons")
plt.ylabel("Nombre de Naissances")
plt.title("Évolution de la Reproduction des Poissons et des Requins")
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()
