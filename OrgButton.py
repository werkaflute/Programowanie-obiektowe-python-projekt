from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic.properties import QtGui

from MenuKontekstowe import MenuKontekstowe
from Polozenie import Polozenie
from Swiat import Swiat


class OrgButton(QPushButton):


    def __init__(self, parent, swiat: Swiat, x: int, y: int):
        super(OrgButton, self).__init__(' ', parent)
        self.swiat = swiat
        self._x = x
        self._y = y
        self.menu = MenuKontekstowe(swiat, self, self)
        #self.clicked.connect(self.action)
        #self.setContextMenuPolicy(Qt.CustomContextMenu)

    def paintEvent(self, q_paint_event):

        o = self.swiat.zwroc_org_o_pol(Polozenie(self._x, self._y))
        if o is not None:
            self.setText(o.pobierz_znak())
        else:
            self.setText('')

        super().paintEvent(q_paint_event)

    def action(self):
        self.menu.popup(QPoint())
