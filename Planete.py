from Requin import Requin
from Poisson import Poisson
import itertools



################################################################################################

class Planete : 

    def __init__(self, largeur : int, hauteur : int):
        self.__largeur = largeur
        self.__hauteur = hauteur        


    def affichage_grille(self, liste_entites: list["Poisson", "Requin"]) -> None:
        
        # stocker les coordonnées et le __str__ des entités dans un dictionnaire
        grille_entites = {(entite.emplacement_x, entite.emplacement_y): str(entite) for entite in liste_entites}
        
        # toutes les coordonnées de la planète (selon la hauteur et la largeur)
        coordonnees = list(itertools.product(range(self.__largeur), range(self.__hauteur)))
        
        # création d'une grille vide
        grille_vide = {coord : "    " for coord in coordonnees}
        
        # ajout de cases vides aux coordonnées non occupées de la grille des entités
        for coord in grille_vide.keys():
            if coord not in grille_entites:
                grille_entites[coord] = grille_vide[coord]
        
        # ordonner la grille avant de l'afficher
        grille_ordonnee = dict(sorted(grille_entites.items(), key=lambda x: (x[0][0], x[0][1])))
        
        # splitter la grille en plusieurs sous-listes pour simplifier l'affichage
        grille_items = list(grille_ordonnee.values())
        grille_a_afficher = [[item for item in grille_items[i:i+self.__largeur]] for i in range(0, len(grille_ordonnee), self.__largeur)]
        
        
        # affichage de la grille
        separateur = "-" + "-" * (self.__largeur * 4 + (self.__largeur - 1))
        print(separateur)
        for ligne in grille_a_afficher :
            for e in ligne : 
                print(e, end="|")
            print()
            print(separateur)

            
################################################################################################

# affichage du nombre de poissons et de requins
def afficher_chiffres(list_entites : list["Poisson", "Requin"]) : 
    
    nombre_poissons = len([e for e in list_entites if isinstance(e, Poisson) and not isinstance(e, Requin)])
    nombre_requins = len([e for e in list_entites if isinstance(e, Requin)])
    print(f"Nombre de poissons : {nombre_poissons} \nNombre de requins : {nombre_requins} ")




def statistiques() : 
    pass


if __name__ == "__main__" : 
    
    l1 = [Poisson(0,0,5), Poisson(0,1,5), Poisson(1,0,5), Requin(1,1,5,5)]
    planete1 = Planete(5,5)
    planete1.affichage_grille(l1)
    afficher_chiffres(l1)






