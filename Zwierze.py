from Organizm import Organizm


class Zwierze(Organizm):

    def __init__(self, sila, inicjatywa, swiat, polozenie):
        super(Zwierze, self).__init__(sila, inicjatywa, swiat, polozenie)

    def akcja(self):
        nowe = self.swiat.zwroc_polozenie(self.polozenie, 1)
        sasiad = self.swiat.zwroc_org_o_pol(nowe)
        if sasiad is not None and sasiad is not self:
            sasiad.kolizja(self)
        else:
            self.polozenie = nowe

    def kolizja(self, atakujacy):
        if type(self) == type(atakujacy):
            super(Zwierze, self).rozmnoz()

        else:
            super(Zwierze, self).kolizja(atakujacy)

