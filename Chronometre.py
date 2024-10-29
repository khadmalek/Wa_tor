import time

class Chronometre:
    def __init__(self):
        self.temps_debut = 0
        self.temps_fin = 0
        self.en_marche = False

    def demarrer(self):
        if not self.en_marche:
            self.temps_debut = time.time()
            self.en_marche = True

    def arreter(self):
        if self.en_marche:
            self.temps_fin = time.time()
            self.en_marche = False

    def obtenir_temps(self):
        if self.en_marche:
            return time.time() - self.temps_debut
        return self.temps_fin - self.temps_debut

    def afficher_temps(self):
        temps = self.obtenir_temps()
        heures = int(temps // 3600)
        minutes = int((temps % 3600) // 60)
        secondes = int(temps % 60)
        return f"{heures:02d}:{minutes:02d}:{secondes:02d}"