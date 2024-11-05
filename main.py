import random
from Poisson import Poisson
from Requin import Requin
from Planete import Planete
from Planete import afficher_chiffres
import os
import time
import configparser
from Chronometre import Chronometre

"""Module principal de la simulation.

Ce module importe les classes et fonctions nécessaires pour exécuter la simulation 
des interactions entre poissons et requins dans un environnement planétaire. 
Il utilise également des bibliothèques pour gérer le hasard, la configuration, 
le temps et les entrées/sorties du système.

Imports:
    random: Pour générer des éléments aléatoires dans la simulation.
    Poisson: Classe représentant les poissons dans la simulation.
    Requin: Classe représentant les requins dans la simulation.
    Planete: Classe représentant l'environnement de la simulation.
    afficher_chiffres: Fonction pour afficher les statistiques des entités.
    os: Pour interagir avec le système d'exploitation.
    time: Pour gérer le temps dans la simulation.
    configparser: Pour lire et gérer les fichiers de configuration.
    Chronometre: Classe pour mesurer le temps écoulé dans la simulation.
"""



# Paramètres de la simulation

config = configparser.ConfigParser()
config.read('parametre.ini')


# Lecture des paramètres de configuration
largeur = int(config["main"]['largeur'])
hauteur = int(config["main"]['hauteur'])
nombre_poisson_initial = int(config["main"]['nombre_poisson_initial'])
nombre_requin_initial = int(config["main"]['nombre_requin_initial'])
energie_initiale = int(config["main"]['energie_initiale'])
temps_de_reproduction_poisson = int(config["main"]['temps_de_reproduction_poisson'])
temps_de_reproduction_requin = int(config["main"]['temps_de_reproduction_requin'])
gain_energie_par_poisson = int(config["main"]['gain_energie_par_poisson'])


# création d'une fonction qui créée la liste d'animaux

def creer_animaux(largeur : int, hauteur : int) -> list :

    """Crée une liste d'animaux dans une grille donnée.

    Cette fonction génère des poissons et des requins à des positions aléatoires 
    dans une grille définie par sa largeur et sa hauteur. Elle s'assure que chaque 
    animal est placé dans une case vide et retourne une liste contenant tous les 
    animaux créés.

    Args:
        largeur (int): La largeur de la grille où les animaux seront placés.
        hauteur (int): La hauteur de la grille où les animaux seront placés.

    Returns:
        list: Une liste d'objets de type Poisson et Requin.
    """
    
    # Crée une liste de toutes les positions vides dans la grille
    cases_vides = [(x, y) for x in range(largeur) for y in range(hauteur)]
    liste_animaux = []

    # Ajout de poissons dans la liste
    for _ in range(nombre_poisson_initial):
        x, y = random.choice(cases_vides) # Choisir une position vide aléatoire
        liste_animaux.append(Poisson(x, y, temps_de_reproduction_poisson))
        cases_vides.remove((x, y)) # Retirer la case occupée

    # Ajout de requins dans la liste
    for _ in range(nombre_requin_initial):
        x, y = random.choice(cases_vides) # Choisir une position vide aléatoire
        liste_animaux.append(Requin(x, y, temps_de_reproduction_requin, energie_initiale))
        cases_vides.remove((x, y)) # Retirer la case occupée
    return liste_animaux


# Création de la planète
aqualand = Planete(largeur, hauteur) # Initialisation de l'environnement
liste_animaux = creer_animaux(largeur, hauteur) # Création des animaux
chrono = Chronometre() # Initialisation du chronomètre
chrono.demarrer() # Démarrage du chronomètre


chronon = 0 # Compteur de temps
while True:
    if chronon % 10 == 0 :  # Exécuter chaque 10 chronons
        
        poissons_nes = 0 # Compteur pour les poissons nés
        for animal in liste_animaux :
            if isinstance(animal, Poisson) and not isinstance(animal, Requin): # Vérifie si l'animal est un poisson
                animal.deplacement(liste_animaux,largeur, hauteur) # Déplace le poisson
                if animal.reproduction(liste_animaux) : # Vérifie la reproduction
                    poissons_nes += 1 # Incrémente le compteur de poissons nés
        
        requin_nes = 0  # Compteur pour les requins nés
        requins_morts = 0 # Compteur pour les requins morts
        poissons_miam = 0 # Compteur pour les poissons mangés
        for animal in liste_animaux:
            if isinstance(animal, Requin): # Vérifie si l'animal est un requin
                if animal.deplacement(liste_animaux, largeur, hauteur) : # Déplace le requin
                    poissons_miam += 1 # Incrémente le compteur de poissons mangés
                if animal.reproduction_requin(liste_animaux) == True : # Vérifie la reproduction des requins
                    requin_nes += 1 # Incrémente le compteur de requins nés
                if animal.mourir(liste_animaux) : # Vérifie si le requin meurt
                    requins_morts += 1  # Incrémente le compteur de requins morts
        
        # Afficher la grille et les statistiques
        os.system("clear") # Efface l'écran
        aqualand.affichage_grille(liste_animaux) # Affiche la grille des animaux
        print(chrono.afficher_temps()) # Affiche le temps écoulé
        afficher_chiffres(liste_animaux) # Affiche les statistiques des animaux
        print("-"*65) # Ligne de séparation
        print(f"nombre de requins nés : {requin_nes:<6} nombre de requins morts : {requins_morts}")
        print(f"nombre de poissons nés : {poissons_nes:<5} nombre de poissons miamiamés : {poissons_miam}")
        time.sleep(0.3) # Pause pour ralentir la simulation
    
    chronon += 1 # Incrémente le chronomètre
