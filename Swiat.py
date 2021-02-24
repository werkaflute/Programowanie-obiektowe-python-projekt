import Organizm
import random

from BrakWolnegoMiejsca import BrakWolnegoMiejsca
from Polozenie import Polozenie


class Swiat:

    def __init__(self, w, h):
        self._h = h
        self._w = w
        self._organizmy = []
        self.key_pressed = ''

    def dodaj_organizm(self, organizm: Organizm):
        self._organizmy.append(organizm)

    def dodaj_organizm_z_losowaniem(self, organizm: Organizm):
        self.losuj_polozenie(organizm)
        self._organizmy.append(organizm)

    def usun_organizm(self, organizm: Organizm):
        self._organizmy.remove(organizm)

    def sprawdz_czy_w_swiecie(self, p):
        return p.y >= 0 and p.y < self._h and p.x >= 0 and p.x < self._w

    def zwroc_org_o_pol(self, p) -> Organizm:
        for i in range(0, len(self._organizmy)):
            if self._organizmy[i].polozenie.equals(p):
                return self._organizmy[i]

        return None

    def get_organizmy(self):
        return self._organizmy

    def zwroc_polozenie(self, polozenie, zasieg):
        while True:
            kierunek = random.randint(0, 7)
            nowe = Polozenie()
            nowe.set(polozenie)
            if kierunek == 0:
                nowe.y = nowe.y - zasieg
            elif kierunek == 1:
                nowe.y = nowe.y - zasieg
                nowe.x = nowe.x + zasieg
            elif kierunek == 2:
                nowe.x = nowe.x + zasieg
            elif kierunek == 3:
                nowe.y = nowe.y + zasieg
                nowe.x = nowe.x - zasieg
            elif kierunek == 4:
                nowe.y = nowe.y + zasieg
            elif kierunek == 5:
                nowe.y = nowe.y + zasieg
                nowe.x = nowe.x - zasieg
            elif kierunek == 6:
                nowe.x = nowe.x - zasieg
            elif kierunek == 7:
                nowe.y = nowe.y - zasieg
                nowe.x = nowe.x - zasieg
            if self.sprawdz_czy_w_swiecie(nowe):
                return nowe

    def zwroc_wolne_polozenie(self, polozenie, zasieg):
        i = 0
        while True:
            nowe = self.zwroc_polozenie(polozenie, zasieg)
            if self.zwroc_org_o_pol(nowe) is None:
                return nowe
            i += 1
            if i >= 100:
                raise BrakWolnegoMiejsca()

    def wykonaj_ture(self):
        for i in range(len(self._organizmy)):
            if i >= len(self._organizmy):
                break
            if self._organizmy[i] is not None:
                self._organizmy[i].akcja()

    def losuj_polozenie(self, org):
        spr = True
        while spr is True:
            x = random.randint(0, self._h-1)
            y = random.randint(0, self._w-1)
            temp = Polozenie()
            temp.set(Polozenie(x, y))
            for i in range(0, len(self._organizmy)):
                if self._organizmy[i].polozenie.equals(temp):
                    spr = False
            if spr is False:
                spr = True
            else:
                spr = False
                org.polozenie.set_x(y)
                org.polozenie.set_y(x)

    def get_swiat(self, _swiat):
        return _swiat

    def set_swiat(self, _swiat):
        self = _swiat