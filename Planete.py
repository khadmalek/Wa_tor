
class Planete : 
    def __init__(self, largeur : int, hauteur : int, liste_entites : list):
        self.__largeur = largeur
        self.__longueur = hauteur
        self.liste_entites = liste_entites
        self.grille = {}    # dictionnaire contenant toutes les cases possibles de la grille, avec poisson, requins et cases vides

    def affichage_entites(self) : 
        print("Affichage de la grille des requins, poisson et cases eau")
        for objets in self.liste_entites : 
            print(objets)
            
    def afficher_statistiques (self) : 
        print("Affiche le nombre de requins et de poisson à chaque chronon")
        
