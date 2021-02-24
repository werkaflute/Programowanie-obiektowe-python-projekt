from PyQt5.QtWidgets import QTextEdit


class Komentator:
    text_edit: QTextEdit

    @staticmethod
    def set_text_edit(text):
        Komentator.text_edit = text

    def dodaj_wiadomosc(self, wiadomosc):
        self.set_text_edit(self.text_edit + wiadomosc + "\n")