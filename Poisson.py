import random
from Requin import Requin

class Poisson:
    
    def __init__(self, x, y, temps_reproduction_poisson):

        self.emplacement_x = x  # Position x du poisson dans la grille
        self.emplacement_y = y  # Position y du poisson dans la grille
        self.temps_reproduction_poisson = temps_reproduction_poisson  # Temps requis pour la reproduction
        self.temps_reproduction = 0  # Compteur de reproduction initialisé à 0
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]


    def cases_voisines(self) -> list[tuple]:

        return [
            (mouvement_thoroidal(self.emplacement_x+1), self.emplacement_y), 
            (mouvement_thoroidal(self.emplacement_x-1), self.emplacement_y),
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y+1)), 
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y-1))
        ]

    def deplacement(self):

        # stocker l'ancien emplacement du poisson
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]
        # Obtenir les cases libres autour du poisson
        cases_voisines = self.cases_voisines()

        for _ in range(len(cases_voisines)) :
            # Choisit une case libre au hasard parmi les voisins libres
            case_choisie = random.choice(cases_voisines)
            if not isinstance(case_choisie, Requin) and not isinstance(case_choisie, Poisson):
                self.emplacement_x, self.emplacement_y = case_choisie
                break
            else : 
                cases_voisines.remove(case_choisie)
        # Incrémente le compteur de reproduction après le déplacement
        self.temps_reproduction += 1
        

    def reproduction(self, liste_animaux : list["Poisson", "Requin"]):

        # Vérifie si le compteur de reproduction a atteint le cycle requis
        if self.temps_reproduction >= self.temps_reproduction_poisson and [self.emplacement_x, self.emplacement_y] != self.ancien_emplacement:
            nouveau_x, nouveau_y = self.ancien_emplacement
            
            # Crée un nouveau poisson et le place dans la grille
            nouveau_poisson = Poisson(nouveau_x, nouveau_y, self.temps_reproduction_poisson)
            
            # on ajoute le nouveau poisson à la liste d'animaux
            liste_animaux.append(nouveau_poisson)
            
            # Réinitialise le compteur de reproduction
            self.temps_reproduction = 0
                
    
    def __str__(self):

        return " 🐟"


# Autres fonctions

def mouvement_thoroidal(coord, longueur) : 
    if coord == longueur : 
        return 0
    elif coord == -1 : 
        return longueur-1
    # return coord % longueur


def mouvement_thoroidal(coord, longueur) : 
    if coord == longueur : 
        return 0
    elif coord == -1 : 
        return longueur-1
    # return coord % longueur











