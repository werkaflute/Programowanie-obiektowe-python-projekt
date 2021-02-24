from Polozenie import Polozenie
from Zwierze import Zwierze
import random


class Zolw(Zwierze):

    def __init__(self, swiat, polozenie):
        super(Zolw, self).__init__(2, 1, swiat, polozenie)

    def sklonuj(self):
        return Zolw(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "Z"

    def akcja(self):
        if random.randint(0, 100) <= 25:
            super(Zolw, self).akcja()

    def kolizja(self, atakujacy):
        if atakujacy.get_sila() >= 5:
            super(Zolw, self).kolizja(atakujacy)
