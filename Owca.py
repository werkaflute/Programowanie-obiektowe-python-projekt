from Polozenie import Polozenie
from Zwierze import Zwierze


class Owca(Zwierze):

    def __init__(self, swiat, polozenie):
        super(Owca, self).__init__(4, 4, swiat, polozenie)

    def sklonuj(self):
        return Owca(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "O"
