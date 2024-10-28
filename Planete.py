from Poisson import Poisson
# from Requin import Requin
import itertools

class Planete : 
    def __init__(self, largeur : int, hauteur : int, liste_entites : list):
        self.__largeur = largeur
        self.__longueur = hauteur
        # self.liste_entites = liste_entites
        

    def affichage_grille(self, liste_entites : list["Poisson", "Requin"]) : 
        
        print("Affichage de la grille des requins, poisson ")
        grille = {(entite.emplacement_x, entite.emplacement_y) : entite.__str__ for entite in liste_entites}
        grille_vide = {tuple(itertools.product(self.__largeur, self.__longueur)) : "vide"}
        for key, value in grille_vide.keys() : 
            if key not in grille : 
                grille[key] = value
        grille_ordonnee = sorted(grille, key=lambda x : (x[0], x[1]))
        
        
        
        # grille_a_afficher = [grille_ordonnee[i:i+self.__largeur] for i in range (0, len(grille_ordonnee), self.__largeur)]
        # for value in grille_a_afficher.values() : 
            

  
            
            
    def afficher_statistiques (self) : 
        
        print("Affiche le nombre de requins et de poisson à chaque chronon")
        

l1 = [Poisson(0,0,5), Poisson(0,1,5), Poisson(1,0,5), Poisson(1,1,5)]

planete1 = Planete(5,5,l1)

print(planete1)