from Polozenie import Polozenie
from Roslina import Roslina


class Trawa(Roslina):

    def __init__(self, swiat, polozenie):
        super(Trawa, self).__init__(0, 0, swiat, polozenie)

    def sklonuj(self):
        return Trawa(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "T"

