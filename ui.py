import pygame
import configparser
from Poisson import Poisson
from Requin import Requin
from Planete import Planete
from Chronometre import Chronometre
from main import creer_animaux

# Paramètres de la simulation

config = configparser.ConfigParser()
config.read('parametre.ini')


# Lecture des paramètres de configuration
largeur = int(config["main"]['largeur'])
hauteur = int(config["main"]['hauteur'])
taille_cellule = 20

pygame.init()

largeur_fenetre = largeur * taille_cellule
hauteur_fenetre = hauteur * taille_cellule

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Wa-tor")

aqualand = Planete(largeur,hauteur)

liste_animaux = creer_animaux(largeur,hauteur)
chrono = Chronometre()
chrono.demarrer()

running = True
clock = pygame.time.Clock()
chronon = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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