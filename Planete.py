from Poisson import Poisson
from Requin import Requin
import itertools

class Planete : 
    def __init__(self, largeur : int, hauteur : int):
        self.__largeur = largeur
        self.__longueur = hauteur        


    def affichage_grille(self, liste_entites: list["Poisson", "Requin"]) -> None:
        
        # Stocker les coordonnées et le __str__ des entités dans un dictionnaire
        grille_entites = {(entite.emplacement_x, entite.emplacement_y): str(entite) for entite in liste_entites}
        
        # Toutes les coordonnées de la planète (selon la longueur et la largeur)
        coordonnees = list(itertools.product(range(self.__largeur), range(self.__longueur)))
        
        # Création d'une grille vide
        grille_vide = {coord: " o " for coord in coordonnees}
        
        # Ajout de cases vides aux coordonnées non occupées de la grille des entités
        for coord in grille_vide:
            if coord not in grille_entites:
                grille_entites[coord] = grille_vide[coord]
        
        # Ordonner la grille avant de l'afficher
        grille_ordonnee = sorted(grille_entites.items(), key=lambda x: (x[0][0], x[0][1]))
        
        # Splitter la grille en plusieurs sous-listes pour simplifier l'affichage
        grille_a_afficher = [grille_ordonnee[i:i+self.__largeur] for i in range(0, len(grille_ordonnee), self.__largeur)]
        
        # Affichage de la grille
        for ligne in grille_a_afficher:
            print(" | ".join(value for _, value in ligne))
  
  
            
        
        

# affichage du nombre de poissons et de requins
def afficher_chiffres(list_entites : list["Poisson", "Requin"]) : 
    
    nombre_poissons = len([e for e in list_entites if isinstance(e, Poisson) and not isinstance(e, Requin)])
    nombre_requins = len([e for e in list_entites if isinstance(e, Requin)])
    print(f"Nombre de poissons : {nombre_poissons} \nNombre de requins : {nombre_requins} ")



def statistiques() : 
    pass




def afficher_statistiques (list_entites : list["Poisson", "Requin"]) : 
  
    nombre_poissons = len([e for e in list_entites if isinstance(e, Poisson) and not isinstance(e, Requin)])
    nombre_requins = len([e for e in list_entites if isinstance(e, Requin)])
    print(f"Nombre de poissons : {nombre_poissons} \nNombre de requins : {nombre_requins} ")







