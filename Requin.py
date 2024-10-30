from Poisson import Poisson
import random

class Requin(Poisson):
    def __init__(self, x : int, y : int, temps_reproduction_requin : int, energie : int):
        super().__init__(x, y, temps_reproduction_requin) 
        self.temps_reproduction_requin= temps_reproduction_requin
        self.energie = energie 
        self.chronons_reproduction =  0
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]
    
    
    def deplacement(self, liste_animaux : list ["Requin", "Poisson"], largeur: int, hauteur: int):
        
        self.energie -=1
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]
        
        # recherche des poissons adjacents
        voisins = self.cases_voisines(largeur,hauteur)
        poissons_adjacents = []
        requin_adjactents= []

        for animal in liste_animaux : 
            if (animal.emplacement_x, animal.emplacement_y) in voisins and isinstance(animal, Poisson) and not isinstance(animal, Requin): 
                poissons_adjacents.append(animal)
            if (animal.emplacement_x, animal.emplacement_y) in voisins and isinstance(animal, Requin) and not isinstance(animal, Poisson):
                requin_adjactents.append((animal.emplacement_x, animal.emplacement_y))

        # deplacer un requin vers un poisson
        if poissons_adjacents :
            poisson_a_miam = random.choice(poissons_adjacents)
            # Met à jour les coordonnées du requin dans la grille
            self.emplacement_x, self.emplacement_y = poisson_a_miam.emplacement_x, poisson_a_miam.emplacement_y
            # miam poisson
            self.manger_poisson(poisson_a_miam, liste_animaux)

        # deplacer un requin vers une case vide
        else : 
            cases_vides = []
            for voisin in voisins : 
                if voisin not in requin_adjactents : 
                    cases_vides.append(voisin)
            case_vide = random.choice(cases_vides)
            self.emplacement_x, self.emplacement_y = case_vide
        
        # incrémenter le nombre de chronons de reproduction à chaque deplacement
        self.chronons_reproduction += 1


    def manger_poisson(self, poisson : "Poisson", liste_animaux : list["Requin", "Poisson"]):
        self.energie += 1
        liste_animaux.remove(poisson)

    

    def mourir(self, liste_animaux : list["Requin", "Poisson"]):
        if self.energie <= 0:
            liste_animaux.remove(self)
        
    
    def reproduction_requin(self,liste_animaux : list ["Requin", "Poisson"]):
        if self.chronons_reproduction >= self.temps_reproduction_requin and [self.emplacement_x, self.emplacement_y] != self.ancien_emplacement :
            x_nouveau = self.ancien_emplacement[0]
            y_nouveau = self.ancien_emplacement[1]
            # Crée un nouveau requin et le place dans la population
            nouveau_requin = Requin(x_nouveau, y_nouveau, self.temps_reproduction_requin, self.energie)
            liste_animaux.append(nouveau_requin)
            # Réinitialise le compteur de reproduction
            self.chronons_reproduction = 0

    def __str__(self):
        return " 🦈"
    
if __name__ == "__main__" : 

    requin1 = Requin(3, 3, 5, 6)
    print(requin1)