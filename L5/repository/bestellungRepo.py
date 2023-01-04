from dataRepo import DataRepo
import json
import sys
sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')
from modelle.bestellung import Bestellung

class BestellungRepo(DataRepo):
    def convert_to_string(self, objects):
        bestellungen = list(map(lambda bestellung:{
            "id": bestellung.id,
            "kunden_ids": bestellung.kunden_ids,
            "gerichte_ids": bestellung.gerichte_ids,
            "getranke_ids": bestellung.getranke_ids,
            "total_cost": bestellung.total_cost
        }, objects))
        bestellungen.sort(key=lambda x: x['id'])
        return json.dumps(bestellungen, indent=4)

    def convert_from_string(self, data):
        bestellungen = list(map(lambda bestellung_data: Bestellung(
            id = bestellung_data['id'],
            kunden_ids = bestellung_data['kunden_ids'],
            gerichte_ids = bestellung_data['gerichte_ids'],
            getranke_ids = bestellung_data['getranke_ids']
        ), json.loads(data)))
        return bestellungen