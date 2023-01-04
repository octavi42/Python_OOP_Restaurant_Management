from gericht import Gericht

class GekochterGericht(Gericht):
    def __init__(self, portion, preis, zeit, id=None):
        super().__init__(portion, preis, id)
        self.zeit = zeit