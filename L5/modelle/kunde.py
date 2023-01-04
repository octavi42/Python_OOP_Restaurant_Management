from identifizierbar import Identifizierbar

class Kunde(Identifizierbar):
    def __init__(self, name, adresse, id=None):
        super().__init__(id)
        self.name = name
        self.adresse = adresse