import random
from Poisson import Poisson
from Requin import Requin
from Planete import Planete
from Planete import afficher_chiffres
import os
import time
import configparser


# Paramètres de la simulation

config = configparser.ConfigParser()
config.read('parametre.ini')

largeur = config['largeur']
hauteur = config['hauteur']
nombre_poisson_initial = config['nombre_poisson_initial']
nombre_requin_initial = config['nombre_requin_initial']
energie_initiale = config['energie_initiale']
temps_de_reproduction_poisson = config['temps_de_reproduction_poisson']
temps_de_reproduction_requin = ['temps_de_reproduction_requin']
gain_energie_par_poisson = config['gain_energie_par_poisson']


####################################################################################


# création d'une fonction qui créée la liste d'animaux

def creer_animaux(largeur : int, hauteur : int) -> list :
    
    cases_vides = [(x, y) for x in range(largeur) for y in range(hauteur)]
    liste_animaux = []
    for _ in range(nombre_poisson_initial):
        x, y = random.choice(cases_vides)
        liste_animaux.append(Poisson(x, y, temps_de_reproduction_poisson))
        cases_vides.remove((x, y))

    for _ in range(nombre_requin_initial):
        x, y = random.choice(cases_vides)
        liste_animaux.append(Requin(x, y, temps_de_reproduction_requin, energie_initiale))
        cases_vides.remove((x, y))
    return liste_animaux


####################################################################################

# Création de la planète
aqualand = Planete(largeur, hauteur)
liste_animaux = creer_animaux(largeur, hauteur)


chronon = 0
while True:
    if chronon % 10 == 0 :
        for animal in liste_animaux :
            if isinstance(animal, Poisson) and not isinstance(animal, Requin):
                animal.deplacement(liste_animaux,largeur, hauteur)
                animal.reproduction(liste_animaux)
        
        for animal in liste_animaux:
            if isinstance(animal, Requin):
                animal.deplacement(liste_animaux, largeur, hauteur)       # et manger poisson en meme temps
                animal.reproduction_requin(liste_animaux)
                animal.mourir(liste_animaux)
        
        # Afficher la grille et les statistiques
        os.system("clear")
        aqualand.affichage_grille(liste_animaux)
        afficher_chiffres(liste_animaux)
        time.sleep(0.3)
    
    chronon += 1
