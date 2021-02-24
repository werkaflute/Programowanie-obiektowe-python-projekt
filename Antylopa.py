from Polozenie import Polozenie
from Zwierze import Zwierze
import random


class Antylopa(Zwierze):

    def __init__(self, swiat, polozenie):
        super(Antylopa, self).__init__(4, 4, swiat, polozenie)

    def sklonuj(self):
        return Antylopa(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "A"

    def akcja(self):
        nowe = self.swiat.zwroc_polozenie(self.polozenie, 2)
        sasiad = self.swiat.zwroc_org_o_pol(nowe)

        if sasiad is not None:
            sasiad.kolizja(self)

        else:
            self.polozenie = nowe

    def kolizja(self, atakujacy):
        if self is not atakujacy:
            if random.randint(0, 2) == 1:
                tmp = Polozenie(self.polozenie.x, self.polozenie.y)
                self.polozenie.set(atakujacy)
                atakujacy.polozenie.set(tmp)

            else:
                super(Antylopa, self).kolizja(atakujacy)
