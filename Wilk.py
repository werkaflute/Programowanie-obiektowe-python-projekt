from Polozenie import Polozenie
from Zwierze import Zwierze


class Wilk(Zwierze):

    def __init__(self, swiat, polozenie):
        super(Wilk, self).__init__(9, 5, swiat, polozenie)

    def sklonuj(self):
        return Wilk(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "W"
