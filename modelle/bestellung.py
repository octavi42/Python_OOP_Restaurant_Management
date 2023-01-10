from functools import reduce
from identifizierbar import Identifizierbar

import sys
sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')

from repository.gekochterGerichtRepo import GekochterGerichtRepo
from repository.getrankRepo import GetrankRepo
from repository.kundeRepo import KundeRepo

# import sys
# sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')

# from controller import Controller

class Bestellung(Identifizierbar):
    def __init__(self, kunden_ids, gerichte_ids, getranke_ids, id = None):
        super().__init__(id)

        self.gekoch_r = GekochterGerichtRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_gerichte.json")
        self.getrank_r = GetrankRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_getranke.json")
        self.kunden_r = KundeRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_kunden.json")

        self.kunden_ids = kunden_ids
        self.gerichte_ids = gerichte_ids
        self.getranke_ids = getranke_ids
        self.total_cost = self._calculate_cost()

        
    def _calculate_cost(self):
        gericht_costs = [self.get_gericht_cost(gericht_id) for gericht_id in self.gerichte_ids]
        getrank_costs = [self.get_getrank_cost(getrank_id) for getrank_id in self.getranke_ids]
        all_costs = gericht_costs + getrank_costs
        return reduce(lambda x, y: x + y, all_costs)

    def _generate_receipt_string(self):
        gerichte = self.gekoch_r.load()
        gerichte_on_receipt = list(filter(lambda gericht: gericht.id in self.gerichte_ids, gerichte))
        gerichte_string = "\n".join(map(lambda gericht: str(gericht.portion) + ": " + str(gericht.preis) + " €", gerichte_on_receipt))
        getranke = self.getrank_r.load()
        getranke_on_receipt = list(filter(lambda getrank: getrank.id in self.getranke_ids, getranke))
        getranke_string = "\n".join(map(lambda getrank: str(getrank.portion) + ": " + str(getrank.preis) + " €", getranke_on_receipt))
        kunden = self.kunden_r.load()
        kunden_on_receipt = list(filter(lambda kunde: kunde.id in self.kunden_ids, kunden))
        kunden_string = "\n".join(map(lambda kunde: kunde.name + " - " + kunde.adresse, kunden_on_receipt))
        return f"Gerichte:\n{gerichte_string}\nGetränke:\n{getranke_string}\nKunde:\n{kunden_string}\nTotal: {self.total_cost} €"


    def get_gericht_cost(self, id):
        
        objects = self.gekoch_r.load()

        for obj in objects:
            if obj.id == id:
                return obj.preis

        raise ValueError("Object with ID {} in gericht datei war entfarnt".format(id))

    def get_getrank_cost(self, id):
        objects = self.getrank_r.load()

        for obj in objects:
            if obj.id == id:
                return obj.preis

        raise ValueError("Object with ID {} in getrank datei war entfarnt".format(id))

    