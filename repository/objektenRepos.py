# from dataRepo import DataRepo
# import json
# import sys
# sys.path.insert(0, '/Users/cristeaoctavian/Documents/ubb/fp/teme/L5')
# from modelle.gericht import Gericht
# from modelle.getrank import Getrank
# from modelle.bestellung import Bestellung
# from modelle.kunde import Kunde

# class BestellungRepo(DataRepo):
#     def convert_to_string(self, objects):
#         bestellungen = []
#         for bestellung in objects:
#             bestellung_dict = {
#                 "kunden_id": bestellung.kunden_id,
#                 "gerichte_ids": bestellung.gerichte_ids,
#                 "getranke_ids": bestellung.getranke_ids,
#                 "total_kost": bestellung.total_kost
#             }
#             bestellungen.append(bestellung_dict)
#         return json.dumps(bestellungen, indent=4)

#     def convert_from_string(self, sting):
#         bestellungen = []
#         data = json.loads(sting)
#         for bestellung_data in data:
#             kunden_id = bestellung_data['kunden_id']
#             gerichte_ids = bestellung_data['gerichte_ids']
#             getranke_ids = bestellung_data['getranke_ids']
#             total_kost = bestellung_data['total_kost']
#             bestellung = Bestellung(kunden_id, gerichte_ids, getranke_ids, total_kost)
#             bestellungen.append(bestellung)
#         return bestellungen


# class GekochterGerichtRepo(DataRepo):
#     def convert_to_string(self, objects):
#         gerichten = []
#         for gericht in objects:
#             gericht_dict = {
#                 "id": gericht.id,
#                 "portion": gericht.portion,
#                 "preis": gericht.preis,
#                 "zeit": gericht.zeit
#             }
#             gerichten.append(gericht_dict)
#         return json.dumps(gerichten, indent=4)

#     def convert_from_string(self, sting):
#         gerichten = []
#         data = json.loads(sting)
#         for gericht_data in data:
#             id = gericht_data['id']
#             portion = gericht_data['portion']
#             preis = gericht_data['preis']
#             zeit = gericht_data['zeit']
#             gericht = Gericht(id, portion, preis, zeit)
#             gerichten.append(gericht)
#         return gerichten


# class GetrankRepo(DataRepo):
#     def convert_to_string(self, objects):
#         getranke = []
#         for getrank in objects:
#             getrank_dict = {
#                 "id": getrank.id,
#                 "portion": getrank.portion,
#                 "preis": getrank.preis,
#                 "alkohol": getrank.alkohol
#             }
#             getranke.append(getrank_dict)
#         return json.dumps(getranke, indent=4)

#     def convert_from_string(self, sting):
#         getranke = []
#         data = json.loads(sting)
#         for getrank_data in data:
#             id = getrank_data['id']
#             portion = getrank_data['portion']
#             preis = getrank_data['preis']
#             alkohol = getrank_data['alkohol']
#             getrank = Getrank(id, portion, preis, alkohol)
#             getranke.append(getrank)
#         return getranke


# class KundeRepo(DataRepo):
#     def convert_to_string(self, objects):
#         kunden = []
#         for kunde in objects:
#             kunde_dict = {
#                 "id": kunde.id,
#                 "name": kunde.name,
#                 "adresse": kunde.adresse
#             }
#             kunden.append(kunde_dict)
#         return json.dumps(kunden, indent=4)

#     def convert_from_string(self, data):
#         kunden = []
#         data = json.loads(data)
#         for kunde_data in data:
#             id = kunde_data['id']
#             name = kunde_data['name']
#             adresse = kunde_data['adresse']
#             kunde = Kunde(name, adresse, id)
#             kunden.append(kunde)
#         return kunden