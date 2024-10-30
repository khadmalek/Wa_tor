import random

class Poisson:
    
    def __init__(self, x, y, temps_reproduction_poisson):

        self.emplacement_x = x  # Position x du poisson dans la grille
        self.emplacement_y = y  # Position y du poisson dans la grille
        self.temps_reproduction_poisson = temps_reproduction_poisson 
        self.temps_reproduction = 0  
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]  # Dernière position avant déplacement

    def cases_voisines(self, longueur, largeur) -> list[tuple]:
       
        return [
            (mouvement_thoroidal(self.emplacement_x + 1, longueur), self.emplacement_y), 
            (mouvement_thoroidal(self.emplacement_x - 1, longueur), self.emplacement_y),
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y + 1, largeur)), 
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y - 1, largeur))
        ]

    def deplacement(self, liste_animaux : list["Poisson", "Requin"], longueur, largeur):
        
        # Stocke la position actuelle comme ancien emplacement pour l'utiliser dans la reproduction
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]
        cases_voisines = self.cases_voisines(longueur, largeur)
        coordonnes_animaux = []
        for animal in liste_animaux:
            coordonnes_animaux.append[(animal.emplacement_x, animal.emplacement_y)]

        for _ in range(len(cases_voisines)):
            case_choisie = random.choice(cases_voisines)
            if case_choisie not in coordonnes_animaux : 
                self.emplacement_x = case_choisie[0]
                self.emplacement_y = case_choisie[1]
                break
            else : 
                cases_voisines.remove(case_choisie)
                
        self.temps_reproduction += 1

    def reproduction(self, liste_animaux):
        
        # Vérifie si le cycle de reproduction est atteint et si l'ancien emplacement est différent
        if self.temps_reproduction >= self.temps_reproduction_poisson and \
           [self.emplacement_x, self.emplacement_y] != self.ancien_emplacement:
            
            # Coordonnées de l'ancien emplacement pour le nouveau poisson
            nouveau_x, nouveau_y = self.ancien_emplacement
            
            # Crée un nouveau poisson avec les mêmes paramètres de reproduction
            nouveau_poisson = Poisson(nouveau_x, nouveau_y, self.temps_reproduction_poisson)
            
            liste_animaux.append(nouveau_poisson)
            
            self.temps_reproduction = 0

    def __str__(self):
       
        return " 🐟"


# autes Fonction
def mouvement_thoroidal(coord, longueur):
   
    if coord == longueur:  
        return 0
    elif coord == -1:  
        return longueur - 1
    return coord 
