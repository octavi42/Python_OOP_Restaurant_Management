from identifizierbar import Identifizierbar

class Gericht(Identifizierbar):
    def __init__(self, portion, preis, id=None):
        super().__init__(id)
        self.portion = portion
        self.preis = preis