from Roslina import Roslina
from Polozenie import Polozenie


class WilczeJagody(Roslina):

    def __init__(self, swiat, polozenie):
        super(WilczeJagody, self).__init__(99, 0, swiat, polozenie)

    def sklonuj(self):
        return WilczeJagody(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "J"

    def kolizja(self, atakujacy):
        self.swiat.usun_organizm(atakujacy)
        self.swiat.usun_organizm(self)
