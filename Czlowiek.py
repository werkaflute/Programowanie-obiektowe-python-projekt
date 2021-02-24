import pickle

from Zwierze import Zwierze
from Polozenie import Polozenie


class Czlowiek(Zwierze):
    def __init__(self, swiat, polozenie):
        self.swiat = swiat
        super(Czlowiek, self).__init__(5, 4, swiat, polozenie)
        self.ile_tur = 0

    def sklonuj(self):
        return None

    def pobierz_znak(self):
        return "C"

    def akcja(self):
        czy_ruszyl = False
        kierunek = 0
        input = self.swiat.key_pressed
        if input is 87:
            kierunek = 1
        elif input is 83:
            kierunek = 3
        elif input is 65:
            kierunek = 4
        elif input is 68:
            kierunek = 2
        elif input is 85:
            if self.ile_tur <= 0:
                self.ile_tur = 10

        zasieg = 1

        nowe = Polozenie(self.polozenie.x, self.polozenie.y)
        if kierunek == 1:
            nowe.y = nowe.y - zasieg
            czy_ruszyl = True
        elif kierunek == 2:
            nowe.x = nowe.x + zasieg
            czy_ruszyl = True
        elif kierunek == 3:
            nowe.y = nowe.y + zasieg
            czy_ruszyl = True
        elif kierunek == 4:
            nowe.x = nowe.x - zasieg
            czy_ruszyl = True

        if czy_ruszyl is True:
            sasiad = self.swiat.zwroc_org_o_pol(nowe)
            if self.swiat.sprawdz_czy_w_swiecie(nowe):
                if sasiad is not None:
                    sasiad.kolizja(self)
                else:
                    self.polozenie.set(nowe)

        if self.ile_tur == 10:
            self._sila += 10

        if 0 < self.ile_tur < 5:
            self._sila -= 1

        if self.ile_tur > 0:
            self.ile_tur -= 1
            print("Umiejetnosc czlowieka aktywowana przez " + str(self.ile_tur) + " tur")
