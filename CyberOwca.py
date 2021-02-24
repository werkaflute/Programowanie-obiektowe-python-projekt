from BarszczSosnowskiego import BarszczSosnowskiego
from Polozenie import Polozenie
from Zwierze import Zwierze


class CyberOwca(Zwierze):

    def __init__(self, swiat, polozenie):
        super(CyberOwca, self).__init__(11, 4, swiat, polozenie)

    def sklonuj(self):
        return CyberOwca(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "#"

    def akcja(self):
        najblizszy_barszcz = None
        najmniejsza_odleglosc = 1000
        for org in self.swiat.get_organizmy():
            if isinstance(org, BarszczSosnowskiego):
                dist = org.polozenie.get_distance(self.polozenie)
                if dist < najmniejsza_odleglosc:
                    najblizszy_barszcz = org
                    najmniejsza_odleglosc = dist
        if najblizszy_barszcz is not None:
            direction = najblizszy_barszcz.polozenie.subtract(self.polozenie)
            if direction.x > 0:
                direction.x = 1
            elif direction.x < 0:
                direction.x = -1
            if direction.y > 0:
                direction.y = 1
            elif direction.y < 0:
                direction.y = -1

            nowe = self.polozenie.add(direction)
            sasiad = self.swiat.zwroc_org_o_pol(nowe)
            if sasiad is not None and sasiad is not self:
                sasiad.kolizja(self)
            else:
                self.polozenie = nowe

        else:
            super().akcja()

    def kolizja(self, atakujacy):
        super().kolizja(atakujacy)
