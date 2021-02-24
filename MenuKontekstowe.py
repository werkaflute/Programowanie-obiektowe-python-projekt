from PyQt5.QtWidgets import QMenu, QAction

from Swiat import Swiat


class MenuKontekstowe(QMenu):

    def __init__(self, swiat: Swiat, orgButton, *__args):
        super().__init__(*__args)
        self.swiat = swiat
        self.orgButton = orgButton
        self.dodaj_pola()

    def dodaj_pola(self):
        self.addAction(QAction('opcja', self))

