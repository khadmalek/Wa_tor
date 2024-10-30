from Poisson import Poisson
import random

class Requin(Poisson):
    """
    Classe représentant un requin, héritant de la classe Poisson.

    Cette classe modélise le comportement d'un requin dans un environnement aquatique, y compris ses déplacements, sa reproduction, sa capacité à manger des poissons, et sa gestion de l'énergie. Elle inclut des méthodes pour gérer ces comportements ainsi que des attributs pour suivre l'état du requin.

    Attributes:
        temps_reproduction_requin (int): Le temps nécessaire pour que le requin se reproduise.
        energie (int): Le niveau d'énergie actuel du requin.
        chronons_reproduction (int): Compteur de temps de reproduction.
        ancien_emplacement (list): Enregistrement de l'ancien emplacement du requin.
    """

    
    def __init__(self, x: int, y: int, temps_reproduction_requin: int, energie: int):
        """
        Initialise une instance de Requin avec sa position, son temps de reproduction et son niveau d'énergie.

        Ce constructeur définit l'état initial du Requin, y compris ses coordonnées, le temps de reproduction, l'énergie actuelle et un compteur pour le temps de reproduction. Il enregistre également l'emplacement précédent du Requin.

        Args:
        x (int): La coordonnée x de la position du Requin.
        y (int): La coordonnée y de la position du Requin.
        temps_reproduction_requin (int): Le temps nécessaire pour que le Requin se reproduise.
        energie (int): Le niveau d'énergie actuel du Requin.
        """
        # Appel du constructeur de la classe parente
        super().__init__(x, y, temps_reproduction_requin) 
        self.temps_reproduction_requin = temps_reproduction_requin  # Temps nécessaire pour se reproduire
        self.energie = energie  # Énergie actuelle du requin
        self.chronons_reproduction = 0  # Compteur de temps de reproduction
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]  # Enregistrement de l'ancien emplacement

    
    def deplacement(self, liste_animaux: list, largeur: int, hauteur: int):
        """
        Déplace le requin dans l'environnement en fonction de la présence de poissons et d'autres requins.

        Cette méthode réduit l'énergie du requin à chaque déplacement et met à jour sa position en fonction de la présence de poissons adjacents. Si des poissons sont présents, le requin se déplace vers l'un d'eux et le mange ; sinon, il se déplace vers une case vide. Le compteur de reproduction est également incrémenté à chaque déplacement.

        Args:
        liste_animaux (list): La liste des animaux présents dans l'environnement.
        largeur (int): La largeur de l'environnement.
        hauteur (int): La hauteur de l'environnement.
        """
        # Réduit l'énergie à chaque déplacement
        self.energie -= 1
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]
        
        # Recherche des poissons adjacents
        voisins = self.cases_voisines(largeur, hauteur)
        poissons_adjacents = []
        requins_adjacents = []

        # Identification des poissons et requins adjacents
        for animal in liste_animaux: 
            if (animal.emplacement_x, animal.emplacement_y) in voisins:
                if isinstance(animal, Poisson) and not isinstance(animal, Requin): 
                    poissons_adjacents.append(animal)
                elif isinstance(animal, Requin): 
                    requins_adjacents.append(animal)

        # Déplacement vers un poisson si présent
        if poissons_adjacents:
            poisson_a_miam = random.choice(poissons_adjacents)
            # Met à jour les coordonnées du requin dans la grille
            self.emplacement_x, self.emplacement_y = poisson_a_miam.emplacement_x, poisson_a_miam.emplacement_y
            # Manger le poisson
            self.manger_poisson(poisson_a_miam, liste_animaux)

        # Déplacement vers une case vide sinon
        else: 
            cases_vides = []
            for voisin in voisins: 
                if voisin not in requins_adjacents: 
                    cases_vides.append(voisin)
            case_vide = random.choice(cases_vides)
            self.emplacement_x, self.emplacement_y = case_vide
        
        # Incrémenter le nombre de chronons de reproduction à chaque déplacement
        self.chronons_reproduction += 1



    def manger_poisson(self, poisson: "Poisson", liste_animaux: list):
        """
        Permet au requin de manger un poisson, augmentant ainsi son niveau d'énergie.

        Cette méthode augmente l'énergie du requin de 1 point lorsqu'il mange un poisson et le retire de la liste des animaux présents dans l'environnement. Cela simule l'action de chasse et de consommation de proies par le requin.

        Args:
        poisson (Poisson): L'objet poisson que le requin va manger.
        liste_animaux (list): La liste des animaux présents dans l'environnement.
        """
        # Augmente l'énergie en mangeant un poisson
        self.energie += 1
        liste_animaux.remove(poisson)  # Retire le poisson de la liste des animaux


    def mourir(self, liste_animaux: list):
        """
        Supprime le requin de la liste des animaux s'il n'a plus d'énergie.

        Cette méthode vérifie si l'énergie du requin est inférieure ou égale à zéro et, si c'est le cas, le retire de la liste des animaux présents dans l'environnement. Cela simule la mort du requin en raison de l'épuisement de son énergie.

        Args:
        liste_animaux (list): La liste des animaux présents dans l'environnement.
        """
        # Supprime le requin de la liste s'il n'a plus d'énergie
        if self.energie <= 0:
            liste_animaux.remove(self)


        
    def reproduction_requin(self, liste_animaux: list):
        """
        Gère la reproduction du requin en fonction des conditions établies.

        Cette méthode vérifie si le requin a atteint le nombre requis de chronons de reproduction et s'il a changé d'emplacement. Si ces conditions sont remplies, un nouveau requin est créé à l'ancienne position et ajouté à la liste des animaux, et le compteur de reproduction est réinitialisé.

        Args:
        liste_animaux (list): La liste des animaux présents dans l'environnement.
        """
        # Vérifie les conditions de reproduction
        if self.chronons_reproduction >= self.temps_reproduction_requin and [self.emplacement_x, self.emplacement_y] != self.ancien_emplacement:
            x_nouveau = self.ancien_emplacement[0]
            y_nouveau = self.ancien_emplacement[1]
            # Crée un nouveau requin et l'ajoute à la population
            nouveau_requin = Requin(x_nouveau, y_nouveau, self.temps_reproduction_requin, self.energie)
            liste_animaux.append(nouveau_requin)
            # Réinitialise le compteur de reproduction
            self.chronons_reproduction = 0



    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du requin.

        Cette méthode retourne un emoji représentant le requin, permettant ainsi d'afficher une version visuelle de l'objet dans les interfaces utilisateur ou les journaux.

        Returns:
        str: Une chaîne de caractères contenant l'emoji du requin.
        """
        return " 🦈"  # Représentation textuelle du requin


if __name__ == "__main__": 
    requin1 = Requin(3, 3, 5, 6)
    print(requin1) 

