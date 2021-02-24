from Polozenie import Polozenie
from Roslina import Roslina
from Zwierze import Zwierze


class BarszczSosnowskiego(Roslina):


    def __init__(self, swiat, polozenie):
        super(BarszczSosnowskiego, self).__init__(10, 0, swiat, polozenie)

    def sklonuj(self):
        return BarszczSosnowskiego(self.swiat, Polozenie())

    def pobierz_znak(self):
        return "B"

    def akcja(self):
        for i in range(0, 100):
            nowe = self.swiat.zwroc_polozenie(self.polozenie, 1)
            sasiad = self.swiat.zwroc_org_o_pol(nowe)
            from CyberOwca import CyberOwca
            if sasiad is not None and isinstance(sasiad, Zwierze) and not isinstance(sasiad, CyberOwca):
                sasiad.swiat.usun_organizm(sasiad)

        super(BarszczSosnowskiego, self).akcja()

    def kolizja(self, atakujacy):
        from CyberOwca import CyberOwca
        if not isinstance(atakujacy, CyberOwca):
            self.swiat.usun_organizm(atakujacy)
        self.swiat.usun_organizm(self)

