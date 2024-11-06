import random

"""Module Poisson.

Ce module utilise la bibliothèque `random` pour introduire des éléments de hasard dans 
la simulation des poissons. Cela inclut des fonctionnalités telles que le déplacement 
aléatoire des poissons et la sélection aléatoire de cases voisines.
"""

class Poisson:

    """Représente un poisson dans la simulation.

    Cette classe gère les propriétés et comportements d'un poisson, y compris sa position 
    dans la grille, son temps de reproduction, et ses interactions avec d'autres poissons.

    Attributs:
        emplacement_x (int): La position x du poisson dans la grille.
        emplacement_y (int): La position y du poisson dans la grille.
        temps_reproduction_poisson (int): Le temps nécessaire pour que le poisson se reproduise.
        temps_reproduction (int): Le temps écoulé depuis la dernière reproduction.
        ancien_emplacement (list): La dernière position du poisson avant son déplacement.
    """

    def __init__(self, x : int, y : int, temps_reproduction_poisson : int) -> None:

        """Initialise une instance de la classe Poisson.

        Cette méthode définit la position initiale du poisson dans la grille ainsi que 
        son temps de reproduction. Elle initialise également le temps de reproduction écoulé 
        à zéro et enregistre l'ancien emplacement du poisson.

        Args:
            x (int): La position x initiale du poisson dans la grille.
            y (int): La position y initiale du poisson dans la grille.
            temps_reproduction_poisson (int): Le temps nécessaire pour que le poisson se reproduise.
        """

        self.emplacement_x = x  # Position x du poisson dans la grille
        self.emplacement_y = y  # Position y du poisson dans la grille
        self.temps_reproduction_poisson = temps_reproduction_poisson # Temps nécessaire pour la reproduction
        self.temps_reproduction = 0  # Temps écoulé depuis la dernière reproduction
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]  # Dernière position avant déplacement

    def cases_voisines(self, largeur : int, hauteur : int) -> list[tuple]:

        """Renvoie les coordonnées des cases voisines du poisson.

        Cette méthode calcule les positions adjacentes du poisson en tenant compte des 
        limites de la grille, en utilisant un mouvement toroidal pour gérer les bords.

        Args:
            largeur (int): La largeur de la grille.
            hauteur (int): La hauteur de la grille.

        Returns:
            list[tuple]: Une liste de tuples représentant les coordonnées des cases voisines.
        """
       
        return [
            (mouvement_thoroidal(self.emplacement_x + 1, largeur), self.emplacement_y), # Case à droite
            (mouvement_thoroidal(self.emplacement_x - 1, largeur), self.emplacement_y), # Case à gauche
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y + 1, hauteur)), # Case en bas
            (self.emplacement_x, mouvement_thoroidal(self.emplacement_y - 1, hauteur))  # Case en haut
        ]


    def deplacement(self, liste_animaux : list["Poisson"], largeur : int, hauteur : int) -> None :

        """Déplace le poisson vers une case voisine.

        Cette méthode choisit aléatoirement une case voisine non occupée par un autre poisson 
        et déplace le poisson à cette position. Elle met également à jour l'ancien emplacement 
        du poisson et incrémente le temps de reproduction.

        Args:
            liste_animaux (list): Une liste d'objets de type "Poisson" pour vérifier les 
            positions occupées.
            largeur (int): La largeur de la grille.
            hauteur (int): La hauteur de la grille.

        Returns:
            None
        """
        
        # Stocke la position actuelle comme ancien emplacement pour l'utiliser dans la reproduction
        self.ancien_emplacement = [self.emplacement_x, self.emplacement_y]
        cases_voisines = self.cases_voisines(largeur, hauteur) # Récupère les cases voisines
        coordonnes_animaux = [] # Initialise une liste pour les coordonnées des autres poissons
        for animal in liste_animaux: # Parcourt la liste des animaux
            coordonnes_animaux.append((animal.emplacement_x, animal.emplacement_y)) # Ajoute leurs coordonnées

        for _ in range(len(cases_voisines)): # Essaye de trouver une case voisine libre
            case_choisie = random.choice(cases_voisines) # Choisit une case voisine aléatoire
            if case_choisie not in coordonnes_animaux : # Vérifie si la case est libre
                self.emplacement_x = case_choisie[0] # Déplace le poisson
                self.emplacement_y = case_choisie[1]
                break  # Sort de la boucle après le déplacement
            else : 
                cases_voisines.remove(case_choisie) # Retire la case choisie si occupée
                
        self.temps_reproduction += 1  # Incrémente le temps de reproduction

    def reproduction(self, liste_animaux : list["Poisson"]) -> bool :

        """Gère le processus de reproduction du poisson.

        Cette méthode vérifie si le poisson a atteint le cycle de reproduction et si son 
        emplacement a changé. Si les conditions sont remplies, elle crée un nouveau poisson 
        à l'ancien emplacement et l'ajoute à la liste des animaux.

        Args:
            liste_animaux (list): Une liste d'objets de type "Poisson" pour ajouter le 
            nouveau poisson.

        Returns:
            bool: True si la reproduction a eu lieu, sinon False.
        """
        
        # Vérifie si le cycle de reproduction est atteint et si l'ancien emplacement est différent
        if self.temps_reproduction >= self.temps_reproduction_poisson and \
           [self.emplacement_x, self.emplacement_y] != self.ancien_emplacement:
            
            # Coordonnées de l'ancien emplacement pour le nouveau poisson
            nouveau_x, nouveau_y = self.ancien_emplacement
            
            # Crée un nouveau poisson avec les mêmes paramètres de reproduction
            nouveau_poisson = Poisson(nouveau_x, nouveau_y, self.temps_reproduction_poisson)
            
            liste_animaux.append(nouveau_poisson) # Ajoute le nouveau poisson à la liste
            
            self.temps_reproduction = 0 # Réinitialise le temps de reproduction
            return True # Indique que la reproduction a eu lieu
        return False # Indique que la reproduction n'a pas eu lieu


    def __str__(self):

        """Renvoie une représentation sous forme de chaîne du poisson.

        Cette méthode retourne un symbole représentant le poisson pour l'affichage, 
        facilitant ainsi la visualisation de l'entité dans la grille.

        Returns:
            str: Une chaîne représentant le poisson.
        """
       
        return " 🐟 " # Représentation visuelle du poisson


# autres Fonction
def mouvement_thoroidal(coord : int, longueur : int) -> int:

    """Applique un mouvement toroidal à une coordonnée.

    Cette fonction ajuste une coordonnée pour qu'elle reste dans les limites d'une grille 
    en utilisant un mouvement toroidal. Si la coordonnée dépasse la longueur, elle est 
    ramenée à zéro, et si elle est inférieure à zéro, elle est ajustée à la dernière 
    position valide.

    Args:
        coord (int): La coordonnée à ajuster.
        longueur (int): La longueur de la grille.

    Returns:
        int: La coordonnée ajustée dans les limites de la grille.
    """
   
    if coord == longueur:  
        return 0 # Retourne à la première position si dépasse la longueur
    elif coord == -1:  
        return longueur - 1 # Ajuste à la dernière position valide si en dessous de zéro
    return coord # Retourne la coordonnée inchangée si elle est dans les limites
