import random

class Poisson:
    """
    Classe représentant un poisson dans une simulation d'écosystème.

    Attributs :
    - emplacement_x (int) : Coordonnée x du poisson dans la grille.
    - emplacement_y (int) : Coordonnée y du poisson dans la grille.
    - temps_reproduction (int) : Compteur qui suit le temps écoulé depuis la dernière reproduction.
    - temps_reproduction_poisson (int) : Temps nécessaire pour que le poisson puisse se reproduire.
    """
    
    def __init__(self, x, y, temps_reproduction_poisson):
        """
        Initialise un objet Poisson avec sa position et le cycle de reproduction requis.

        :param x: Coordonnée x initiale du poisson.
        :param y: Coordonnée y initiale du poisson.
        :param temps_reproduction_poisson: Nombre de tours avant que le poisson puisse se reproduire.
        """
        self.emplacement_x = x  # Position x du poisson dans la grille
        self.emplacement_y = y  # Position y du poisson dans la grille
        self.temps_reproduction_poisson = temps_reproduction_poisson  # Temps requis pour la reproduction

        self.age_reproduction = 0

        voisins_libres = []

        # Vérifie chaque direction autour de la position (x, y) sans sortir de la grille
        if x > 0 and self.grille[y][x - 1] is None:  # Gauche
            voisins_libres.append((x - 1, y))
        if x < self.largeur - 1 and self.grille[y][x + 1] is None:  # Droite
            voisins_libres.append((x + 1, y))
        if y > 0 and self.grille[y - 1][x] is None:  # Haut
            voisins_libres.append((x, y - 1))
        if y < self.hauteur - 1 and self.grille[y + 1][x] is None:  # Bas
            voisins_libres.append((x, y + 1))

        # Retourne la liste des positions libres adjacentes
        return voisins_libres


    def deplacement(self):
        """
        Déplace le poisson vers une case libre adjacente si disponible.

        :param planete: Instance de la classe Planete pour accéder aux cases libres.
        :return: Tuple (nouveau_x, nouveau_y) si le poisson a bougé, sinon None.
        """
        # Obtenir les cases libres autour du poisson via la méthode voisins_libres de Planete
        voisins_libres = voisins_libres(self.emplacement_x, self.emplacement_y)

        # Si des cases libres sont disponibles autour du poisson
        if voisins_libres:
            # Choisit une case libre au hasard parmi les voisins libres
            nouvelle_position = random.choice(voisins_libres)
            
            # Met à jour les coordonnées du poisson
            self.emplacement_x, self.emplacement_y = nouvelle_position
            
            # Incrémente le compteur de reproduction après le déplacement
            self.temps_reproduction += 1
            
            # Retourne la nouvelle position pour d'éventuelles actions externes
            return nouvelle_position
        
        # Si aucune case libre, retourne None pour indiquer aucun déplacement
        return None


    def reproduction(self, voisins_libres):
        """
        Tente de créer un nouveau poisson dans une case adjacente si le cycle de reproduction est atteint.

        :param voisins_libres: Liste des positions adjacentes libres sous forme de tuples (x, y).
        :return: Un nouvel objet Poisson si la reproduction a lieu, sinon None.
        """
        # Vérifie si le compteur de reproduction a atteint le cycle requis
        if self.age_reproduction >= self.temps_reproduction_poisson:
            # Si des cases libres sont disponibles
            if voisins_libres:
                # Choisit une case libre pour le nouveau poisson
                nouvelle_position = random.choice(voisins_libres)
                
                # Réinitialise le compteur de reproduction après la reproduction
                self.temps_reproduction = 0
                
                # Retourne un nouvel objet Poisson dans la case libre choisie
                return Poisson(nouvelle_position[0], nouvelle_position[1], self.temps_reproduction_poisson)
        
        # Si le poisson n'est pas prêt à se reproduire, retourne None
        return None

















