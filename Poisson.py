import random

class Poisson:
    
    def __init__(self, x, y, temps_reproduction_poisson):

        self.emplacement_x = x  # Position x du poisson dans la grille
        self.emplacement_y = y  # Position y du poisson dans la grille
        self.temps_reproduction_poisson = temps_reproduction_poisson  # Temps requis pour la reproduction
        self.temps_reproduction = 0  # Compteur de reproduction initialisé à 0

    def voisins_libres(self, grille, largeur, hauteur):
        """
        Trouve les cases adjacentes libres autour du poisson dans la grille.

        :param grille: Liste de listes représentant la grille.
        :param largeur: Largeur de la grille.
        :param hauteur: Hauteur de la grille.
        :return: Liste de tuples (x, y) des positions libres adjacentes.
        """
        voisins_libres = []
        x, y = self.emplacement_x, self.emplacement_y

        # Vérifie chaque direction autour de la position (x, y) sans sortir de la grille
        if x > 0 and grille[y][x - 1] is None:  # Gauche
            voisins_libres.append((x - 1, y))
        if x < largeur - 1 and grille[y][x + 1] is None:  # Droite
            voisins_libres.append((x + 1, y))
        if y > 0 and grille[y - 1][x] is None:  # Haut
            voisins_libres.append((x, y - 1))
        if y < hauteur - 1 and grille[y + 1][x] is None:  # Bas
            voisins_libres.append((x, y + 1))

        return voisins_libres

    def deplacement(self, grille, largeur, hauteur):
        """
        Déplace le poisson vers une case libre adjacente si disponible.

        :param grille: Instance de la grille pour accéder aux cases libres.
        :param largeur: Largeur de la grille.
        :param hauteur: Hauteur de la grille.
        :return: Tuple (nouveau_x, nouveau_y) si le poisson a bougé, sinon None.
        """
        # Obtenir les cases libres autour du poisson
        voisins_libres = self.voisins_libres(grille, largeur, hauteur)

        if voisins_libres:
            # Choisit une case libre au hasard parmi les voisins libres
            nouvelle_position = random.choice(voisins_libres)
            
            # Met à jour les coordonnées du poisson dans la grille
            grille[self.emplacement_y][self.emplacement_x] = None  # Efface l'ancienne position
            self.emplacement_x, self.emplacement_y = nouvelle_position
            grille[self.emplacement_y][self.emplacement_x] = self  # Place le poisson dans la nouvelle position
            
            # Incrémente le compteur de reproduction après le déplacement
            self.temps_reproduction += 1
            
            return nouvelle_position
        return None

    def reproduction(self, grille, largeur, hauteur):
        """
        Tente de créer un nouveau poisson dans une case adjacente si le cycle de reproduction est atteint.

        :param grille: Liste de listes représentant la grille.
        :param largeur: Largeur de la grille.
        :param hauteur: Hauteur de la grille.
        :return: Un nouvel objet Poisson si la reproduction a lieu, sinon None.
        """
        # Vérifie si le compteur de reproduction a atteint le cycle requis
        if self.temps_reproduction >= self.temps_reproduction_poisson:
            voisins_libres = self.voisins_libres(grille, largeur, hauteur)

            if voisins_libres:
                # Choisit une case libre pour le nouveau poisson
                nouvelle_position = random.choice(voisins_libres)
                
                # Réinitialise le compteur de reproduction
                self.temps_reproduction = 0
                
                # Crée un nouveau poisson et le place dans la grille
                nouveau_poisson = Poisson(nouvelle_position[0], nouvelle_position[1], self.temps_reproduction_poisson)
                grille[nouvelle_position[1]][nouvelle_position[0]] = nouveau_poisson
                
                return nouveau_poisson
        return None
    
    def __str__(self):

        return " 🐟"

















