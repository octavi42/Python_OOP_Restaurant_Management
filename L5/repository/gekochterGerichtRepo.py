from dataRepo import DataRepo

import sys
sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')

import json
from modelle.gekochterGericht import GekochterGericht

class GekochterGerichtRepo(DataRepo):
    def convert_to_string(self, objects):
        gerichten = list(map(lambda gericht:{
            "id": gericht.id,
            "portion": gericht.portion,
            "preis": gericht.preis,
            "zeit": gericht.zeit
        }, objects))
        gerichten.sort(key=lambda x: x['id'])
        return json.dumps(gerichten, indent=4)

    def convert_from_string(self, data):
        gerichten = list(map(lambda gericht_data: GekochterGericht(
            id = gericht_data['id'],
            portion = gericht_data['portion'],
            preis = gericht_data['preis'],
            zeit = gericht_data['zeit']
        ), json.loads(data)))
        return gerichten