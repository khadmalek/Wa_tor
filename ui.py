import pygame
from Poisson import Poisson
from Requin import Requin
from Planete import Planete
from Chronometre import Chronometre
from main import creer_animaux

# Paramètres de la simulation
pygame.init()
largeur = 30
hauteur = 30
taille_cellule = 20

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

            # Affichage de la simulation
            fenetre.fill((255, 255, 255))  # Remplir la fenêtre avec un fond blanc
            aqualand.affichage_grille(liste_animaux, fenetre, taille_cellule)  # Afficher la grille avec les animaux

            # Afficher les statistiques
            font = pygame.font.Font(None, 36)
            temps = chrono.afficher_temps()
            stats_text = font.render(f"{temps} - Poissons: {len([x for x in liste_animaux if isinstance(x, Poisson)])}, Requins: {len([x for x in liste_animaux if isinstance(x, Requin)])}", True, (0, 0, 0))
            fenetre.blit(stats_text, (10, 10))

            pygame.display.flip()  # Mettre à jour l'affichage


            # Pause pour ralentir la simulation
            pygame.time.wait(300)

            chronon += 1  # Incrémenter le chronomètre

            
            clock.tick(30)  # Limiter la vitesse du jeu à 30 FPS

    pygame.display.update()

pygame.quit()  # Quitter Pygame