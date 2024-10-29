import random

class Poisson:
    
    def __init__(self, x, y, temps_reproduction_poisson):

        self.emplacement_x = x  # Position x du poisson dans la grille
        self.emplacement_y = y  # Position y du poisson dans la grille
        self.temps_reproduction_poisson = temps_reproduction_poisson 
        self.temps_reproduction = 0  
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]  # Dernière position avant déplacement

    def cases_voisines(self, longueur):
       
        return [
            (mouvement_thoroidal(self.emplacement_x + 1, longueur), self.emplacement_y), 
            (mouvement_thoroidal(self.emplacement_x - 1, longueur), self.emplacement_y),
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y + 1, longueur)), 
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y - 1, longueur))
        ]

    def deplacement(self, longueur):
        
        # Stocke la position actuelle comme ancien emplacement
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]

        cases_voisines = self.cases_voisines(longueur)

        for _ in range(len(cases_voisines)):
            case_choisie = random.choice(cases_voisines)

            # Vérifie si la case est libre (ni requin ni poisson)
            x, y = case_choisie
            if not isinstance(case_choisie, "Requin") and not isinstance(case_choisie, Poisson):
                # Déplace le poisson à la nouvelle position
                self.emplacement_x, self.emplacement_y = case_choisie
                break
            else:
                # Retire la case de la liste si elle n'est pas libre
                cases_voisines.remove(case_choisie)

        # Incrémente le compteur de reproduction après le déplacement
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











