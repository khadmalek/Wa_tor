from Poisson import Poisson
from Requin import Requin
import itertools

"""Module Planete.

Ce module importe les classes `Poisson` et `Requin` pour représenter des entités dans 
la simulation de la planète. Il utilise également le module `itertools` pour faciliter 
la manipulation des coordonnées et des itérations dans la grille de la planète.
"""

class Planete : 

    """Représente une planète avec une grille pour afficher des entités.

    Cette classe permet de créer une planète de dimensions spécifiées et d'afficher une grille 
    contenant des entités telles que des poissons et des requins à leurs emplacements respectifs.

    Attributs:
        __largeur (int): La largeur de la grille de la planète.
        __hauteur (int): La hauteur de la grille de la planète.
    """

    def __init__(self, largeur : int, hauteur : int) -> None:

        """Initialise une instance de la classe Planete.

        Cette méthode définit la largeur et la hauteur de la planète, 
        permettant de créer une grille de dimensions spécifiées.

        Args:
        largeur (int): La largeur de la grille de la planète.
        hauteur (int): La hauteur de la grille de la planète.
        """

        # Initialisation des attributs de largeur et de hauteur
        self.__largeur = largeur
        self.__hauteur = hauteur        


    def affichage_grille(self, liste_entites: list["Poisson", "Requin"]) -> None:

        """Affiche la grille de la planète avec les entités présentes.

        Cette méthode crée une représentation visuelle de la grille en plaçant les entités 
        à leurs coordonnées respectives et en remplissant les cases vides. Elle organise 
        les entités dans une grille et les affiche de manière structurée.

        Args:
        liste_entites (list): Une liste d'entités à afficher sur la grille, 
        comprenant des objets de type "Poisson" et "Requin".

        Returns:
            None
        """
        
        # stocker les coordonnées et le __str__ des entités dans un dictionnaire
        grille_entites = {(entite.emplacement_x, entite.emplacement_y): str(entite) for entite in liste_entites}
        
        # Générer toutes les coordonnées possibles de la grille (selon la hauteur et la largeur)
        coordonnees = list(itertools.product(range(self.__largeur), range(self.__hauteur)))
        
        # Créer une grille vide avec des cases initialisées
        grille_vide = {coord : "    " for coord in coordonnees}
        
        # Ajouter des cases vides aux coordonnées non occupées de la grille des entités
        for coord in grille_vide.keys():
            if coord not in grille_entites:
                grille_entites[coord] = grille_vide[coord]
        
        # Ordonner la grille avant de l'afficher
        grille_ordonnee = dict(sorted(grille_entites.items(), key=lambda x: (x[0][0], x[0][1])))
        
        # Splitter la grille en plusieurs sous-listes pour simplifier l'affichage
        grille_items = list(grille_ordonnee.values())
        grille_a_afficher = [[item for item in grille_items[i:i+self.__largeur]] for i in range(0, len(grille_ordonnee), self.__largeur)]
        
        
        # Affichage de la grille
        separateur = "-" + "-" * (self.__largeur * 5)
        # separateur = "--" + "-" * (self.__largeur * 4 + (self.__largeur - 1))
        print(" "+separateur)
        for ligne in grille_a_afficher :
            print(" |", end="")
            for e in ligne : 
                print(e, end="|")
            print()
            print(" "+separateur)


def afficher_chiffres(list_entites : list["Poisson", "Requin"]) -> None : 

    """Affiche le nombre d'entités présentes dans la liste.

    Cette méthode compte et affiche le nombre de poissons et de requins dans la liste 
    fournie. Elle distingue les poissons des requins et affiche les résultats de manière 
    lisible.

    Args:
        list_entites (list): Une liste d'entités comprenant des objets de type "Poisson" 
        et "Requin".

    Returns:
        None
    """

    # Compte le nombre de poissons dans la liste   
    nombre_poissons = len([e for e in list_entites if isinstance(e, Poisson) and not isinstance(e, Requin)])
    # Compte le nombre de requins dans la liste
    nombre_requins = len([e for e in list_entites if isinstance(e, Requin)])
    # Affiche le nombre de poissons et de requins
    print(f"Nombre de poissons : {nombre_poissons} \nNombre de requins : {nombre_requins} ")


if __name__ == "__main__" :

    # Création d'une liste de poissons
    l1 = [Poisson(0,0,5), Poisson(0,1,5), Poisson(1,0,5), Poisson(1,1,5)]
    # Création d'une planète de dimensions 5x5
    planete1 = Planete(5,5)
    # Affichage de la grille avec les poissons
    planete1.affichage_grille(l1)
    # Affichage du nombre de poissons et de requins
    afficher_chiffres(l1)
