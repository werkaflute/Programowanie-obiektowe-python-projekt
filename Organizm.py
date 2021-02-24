from Komentator import Komentator
from Swiat import Swiat
from BrakWolnegoMiejsca import BrakWolnegoMiejsca
from Polozenie import Polozenie


class Organizm:

    def __init__(self, sila, inicjatywa, swiat: Swiat, polozenie: Polozenie):
        self._sila = sila
        self._inicjatywa = inicjatywa
        self.swiat = swiat
        self.polozenie = polozenie

    def kolizja(self, atakujacy):
        if atakujacy.get_sila() > self._sila:
            atakujacy.polozenie = self.polozenie
            self.swiat.usun_organizm(self)
            #Komentator.dodaj_wiadomosc(atakujacy.pobierz_znak() + "zjadl")
            print(atakujacy.pobierz_znak() + " zjadl " + self.pobierz_znak())


        else:
            self.swiat.usun_organizm(atakujacy)
            print(self.pobierz_znak() + " zjadl " + atakujacy.pobierz_znak())

    def rozmnoz(self):
        try:
            nowe = self.swiat.zwroc_wolne_polozenie(self.polozenie, 1)
            nowy = self.sklonuj()
            nowy.polozenie.set(nowe)
            self.swiat.dodaj_organizm(nowy)

        except BrakWolnegoMiejsca:
            pass

    def get_sila(self):
        return self._sila

    def set_sila(self, sila):
        self.sila = sila
