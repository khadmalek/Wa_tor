import random
from Poisson import Poisson
from Requin import Requin
from Planete import Planete
from Planete import afficher_chiffres
import os
import time
import configparser
from Chronometre import Chronometre


# Paramètres de la simulation

config = configparser.ConfigParser()
config.read('parametre.ini')


largeur = int(config["main"]['largeur'])
hauteur = int(config["main"]['hauteur'])
nombre_poisson_initial = int(config["main"]['nombre_poisson_initial'])
nombre_requin_initial = int(config["main"]['nombre_requin_initial'])
energie_initiale = int(config["main"]['energie_initiale'])
temps_de_reproduction_poisson = int(config["main"]['temps_de_reproduction_poisson'])
temps_de_reproduction_requin = int(config["main"]['temps_de_reproduction_requin'])
gain_energie_par_poisson = int(config["main"]['gain_energie_par_poisson'])


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
chrono = Chronometre()
chrono.demarrer()


chronon = 0
while True:
    if chronon % 10 == 0 :
        
        poissons_nes = 0
        for animal in liste_animaux :
            if isinstance(animal, Poisson) and not isinstance(animal, Requin):
                animal.deplacement(liste_animaux,largeur, hauteur)
                if animal.reproduction(liste_animaux) : 
                    poissons_nes += 1
        
        requin_nes = 0
        requins_morts = 0
        poissons_miam = 0
        for animal in liste_animaux:
            if isinstance(animal, Requin):
                if animal.deplacement(liste_animaux, largeur, hauteur) :        # et manger poisson en meme temps
                    poissons_miam += 1
                if animal.reproduction_requin(liste_animaux) == True : 
                    requin_nes += 1
                if animal.mourir(liste_animaux) : 
                    requins_morts += 1
        
        # Afficher la grille et les statistiques
        os.system("clear")
        aqualand.affichage_grille(liste_animaux)
        print(chrono.afficher_temps())
        afficher_chiffres(liste_animaux)
        print("-"*65)
        print(f"nombre de requins nés : {requin_nes:<6} nombre de requins morts : {requins_morts}")
        print(f"nombre de poissons nés : {poissons_nes:<5} nombre de poissons miamiamés : {poissons_miam}")
        time.sleep(0.3)
    
    chronon += 1
