import pickle
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.uic.properties import QtCore

from Antylopa import Antylopa
from BarszczSosnowskiego import BarszczSosnowskiego
from Czlowiek import Czlowiek
from Guarana import Guarana
from Lis import Lis
from Mlecz import Mlecz
from OrgButton import OrgButton
from Owca import Owca
from Polozenie import Polozenie
from Swiat import Swiat
from Trawa import Trawa
from WilczeJagody import WilczeJagody
from Wilk import Wilk
from Zolw import Zolw
from CyberOwca import CyberOwca
from Komentator import Komentator


class Plansza(QWidget):

    def __init__(self, swiat: Swiat):
        super(Plansza, self).__init__()
        self.title = 'Weronika Piotrowska 175771'
        self.left = 200
        self.top = 200
        self.width = 1500
        self.height = 800
        self._swiat = swiat
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        for i in range(0, 20):
            for j in range(0, 20):
                button = OrgButton(self, self._swiat, i, j)
                button.resize(30, 30)
                button.move(i * 30, j * 30)

        # text = QTextEdit(self)
        # text.move(800, 100)
        # text.resize(300, 400)
        # Komentator.set_text_edit(text)
        self.show()

    def keyPressEvent(self, q_key_event):
        self._swiat.key_pressed = q_key_event.key()
        super().keyPressEvent(q_key_event)
        self._swiat.wykonaj_ture()
        input = self._swiat.key_pressed
        if input == 90:
            mylist = self._swiat
            with open('mylist.txt', 'wb') as f:
                pickle.dump(mylist, f)
        if input == 79:
            with open('mylist.txt', 'rb') as f:
                obiekt = pickle.load(f)
            self.close()
            self.Open = Plansza(obiekt)
            self.Open.show()

        self.repaint()

    def cos(self, plansza1, plansza2):
        plansza1 = plansza2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Swiat(20, 20)
    ex = Plansza(s)

    s.dodaj_organizm_z_losowaniem(CyberOwca(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Antylopa(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(BarszczSosnowskiego(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Czlowiek(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Guarana(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Lis(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Mlecz(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Owca(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Trawa(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(WilczeJagody(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Wilk(s, Polozenie()))
    s.dodaj_organizm_z_losowaniem(Zolw(s, Polozenie()))


    ex.repaint()
    sys.exit(app.exec_())
