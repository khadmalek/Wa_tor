from Poisson import Poisson
import random

class Requin(Poisson):
    def __init__(self,energie,x,y,temps_reproduction_requin):
        super().__init__(x,y,temps_reproduction_requin):
        self.energie = energie 
        self.temps_reproduction_requin= temps_reproduction_requin
        self.chronons_reproduction =  0
    
    
    def deplacement(self,planete):
        self.energie -=1
        # recherche des poissons adjacents
        voisins = self.voisins_libres(planete)
        poissons_adjacents = [(x,y) for (x,y) in voisins 
                              if isinstance(planete.grille[x][y], Poisson) and not isinstance(planete.grille[x][y], Requin)]
        #deplacer un requin vers un poisson
        if poissons_adjacents:
            poisson_a_miam = random.choice(poissons_adjacents)
        
    
    
    
    def manger_poisson(self):
        self.energie += 1


    
    
    
    def mourir(self):
        if self.energie <= 0:
            del self 
        
        