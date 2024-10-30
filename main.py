import random
from Poisson import Poisson
from Requin import Requin
from Planete import Planete
from Planete import afficher_chiffres

# Paramètres de la simulation
largeur = 15
hauteur = 15
nombre_poisson_initial = 80
nombre_requin_initial = 10
energie_initiale = 10
temps_de_reproduction_poisson = 3
temps_de_reproduction_requin = 8
gain_energie_par_poisson = 6


####################################################################################











####################################################################################

# Création de la planète
aqualand = Planete(largeur, hauteur)

# Initialisation des listes d'animaux et des cases vides
liste_animaux = []
liste_poissons = []
liste_requins = []
cases_vides = [(x, y) for x in range(largeur) for y in range(hauteur)]

# Création des requins
for _ in range(nombre_requin_initial):
    x, y = random.choice(cases_vides)
    liste_animaux.append(Requin(x, y, temps_de_reproduction_requin, energie_initiale))
    cases_vides.remove((x, y))

# Création des poissons
for _ in range(nombre_poisson_initial):
    x, y = random.choice(cases_vides)
    liste_animaux.append(Poisson(x, y, temps_de_reproduction_poisson))
    cases_vides.remove((x, y))

chronon = 0
while True:
    for animal in liste_animaux:
        if isinstance(animal, Poisson) and not isinstance(animal, Requin):
            animal.deplacement(largeur)
            animal.reproduction(liste_animaux)
    
    for animal in liste_animaux:
        if isinstance(animal, Requin):
            animal.deplacement(liste_animaux)       # et manger poisson en meme temps
            animal.reproduction_requin(liste_animaux)
            animal.manger_poisson(liste_animaux)        # a supprimer
            animal.mourir(liste_animaux)
    
    # Afficher la grille et les statistiques
    print(f"\nChronon : {chronon}")
    aqualand.affichage_grille(liste_animaux)
    afficher_chiffres(liste_animaux)
    
    chronon += 1
