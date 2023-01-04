from dataRepo import DataRepo
import json
import sys
sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')
from modelle.getrank import Getrank

class GetrankRepo(DataRepo):
    def convert_to_string(self, objects):
        getranke = list(map(lambda getrank:{
            "id": getrank.id,
            "portion": getrank.portion,
            "preis": getrank.preis,
            "alkohol": getrank.alkohol
        }, objects))
        getranke.sort(key=lambda x: x['id'])
        return json.dumps(getranke, indent=4)

    def convert_from_string(self, data):
        getranke = list(map(lambda getrank_data: Getrank(
            id = getrank_data['id'],
            portion = getrank_data['portion'],
            preis = getrank_data['preis'],
            alkohol = getrank_data['alkohol'],
        ), json.loads(data)))
        return getranke