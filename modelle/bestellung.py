from functools import reduce
from identifizierbar import Identifizierbar

import sys
sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')

from repository.gekochterGerichtRepo import GekochterGerichtRepo
from repository.getrankRepo import GetrankRepo

# import sys
# sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')

# from controller import Controller

class Bestellung(Identifizierbar):
    def __init__(self, kunden_ids, gerichte_ids, getranke_ids, id = None):
        super().__init__(id)

        self.gekoch_r = GekochterGerichtRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_gerichte.json")
        self.getrank_r = GetrankRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_getranke.json")

        self.kunden_ids = kunden_ids
        self.gerichte_ids = gerichte_ids
        self.getranke_ids = getranke_ids
        self.total_cost = self.calculate_cost()

        
    def calculate_cost(self):
        gericht_costs = [self.get_gericht_cost(gericht_id) for gericht_id in self.gerichte_ids]
        getrank_costs = [self.get_getrank_cost(getrank_id) for getrank_id in self.getranke_ids]
        all_costs = gericht_costs + getrank_costs
        return reduce(lambda x, y: x + y, all_costs)

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



# gericht1 = Gericht(0, 2, 10.0)
# gericht2 = Gericht(1, 3, 14.4)
# getrank1 = Getrank(0, 40, 11.9, 70)
# getrank2 = Getrank(1, 50, 99.9, 0)

# bestellung1 = Bestellung(0, 1, [gericht1, gericht2], [getrank1, getrank2], 0)

# kost = bestellung1.calculate_cost()
# print(kost)