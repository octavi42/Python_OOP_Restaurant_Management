from gericht import Gericht

class Getrank(Gericht):
    def __init__(self, portion, preis, alkohol, id=None):
        super().__init__(portion, preis, id)
        self.alkohol = alkohol