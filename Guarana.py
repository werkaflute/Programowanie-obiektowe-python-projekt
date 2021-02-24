from Polozenie import Polozenie
from Roslina import Roslina


class Guarana(Roslina):

    def __init__(self, swiat, polozenie):
        super(Guarana, self).__init__(0, 0, swiat, polozenie)

    def sklonuj(self):
        return Guarana(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "G"

    def kolizja(self, atakujacy):
        atakujacy._sila = atakujacy._sila + 3
        super(Guarana, self).kolizja(atakujacy)
