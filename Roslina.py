from Organizm import Organizm
import random


class Roslina(Organizm):

    def __init__(self, sila, inicjatywa, swiat, polozenie):
        super(Roslina, self).__init__(sila, inicjatywa, swiat, polozenie)

    def akcja(self):
        if random.randint(0, 100) < 5:
            self.rozmnoz()
            #print("Powstał " + self.pobierz_znak())

    def kolizja(self, atakujacy):
        super(Roslina, self).kolizja(atakujacy)
