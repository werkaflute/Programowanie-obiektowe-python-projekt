from Polozenie import Polozenie
from Zwierze import Zwierze


class Lis(Zwierze):

    def __init__(self, swiat, polozenie):
        super(Lis, self).__init__(3, 7, swiat, polozenie)

    def sklonuj(self):
        return Lis(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "L"

    def akcja(self):
        sasiad = None
        nowe = None
        for i in range(0, 100):
            nowe = self.swiat.zwroc_polozenie(self.polozenie, 1)
            sasiad = self.swiat.zwroc_org_o_pol(nowe)

            if sasiad is None or sasiad.get_sila() <= self._sila:
                break
        if sasiad is not None:
            sasiad.kolizja(self)
        else:
            self.polozenie = nowe
