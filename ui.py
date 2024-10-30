import pygame
from pygame.locals import *
import sys

########################################################################################################

# couleurs : 
blanc = 255,255,255
bleu = 0, 200, 255      # eau

# initialiser pygame  :
pygame.init()

# créer la fenetre :
largeur = 800
hauteur = 600
largeur_ligne = 3           # largeur de la ligne qui separe les cases de la grille 

fenetre = pygame.display.set_mode((largeur, hauteur))       # créer la fenetre
fenetre.fill(bleu)
pygame.display.set_caption("WA_TOR")                        # afficher le titre "WA_TOR"

def dessiner_grille() :

    blockSize = 10
    for x in range(0, largeur, blockSize):
        for y in range(0, hauteur, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(fenetre, blanc, rect, 1)
            

while True :
    dessiner_grille()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()















