from Polozenie import Polozenie
from Roslina import Roslina


class Mlecz(Roslina):

    def __init__(self, swiat, polozenie):
        super(Mlecz, self).__init__(0, 0, swiat, polozenie)

    def sklonuj(self):
        return Mlecz(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "M"

    def akcja(self):
        for i in range(0,3):
            super(Mlecz, self).akcja()
