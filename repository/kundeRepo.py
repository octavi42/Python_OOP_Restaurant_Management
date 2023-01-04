from dataRepo import DataRepo
import json
import sys
sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')
from modelle.kunde import Kunde

class KundeRepo(DataRepo):
    def convert_to_string(self, objects):
        kunden = list(map(lambda kunde: {
            "id": kunde.id,
            "name": kunde.name,
            "adresse": kunde.adresse
        }, objects))
        kunden.sort(key=lambda x: x['id'])
        return json.dumps(kunden, indent=4)

    def convert_from_string(self, data):
        kunden = list(map(lambda kunde_data: Kunde(
            kunde_data['name'],
            kunde_data['adresse'],
            kunde_data['id']
        ), json.loads(data)))
        return kunden