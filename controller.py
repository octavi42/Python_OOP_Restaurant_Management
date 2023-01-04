from modelle.gericht import Gericht
from modelle.gekochterGericht import GekochterGericht
from modelle.getrank import Getrank
from modelle.kunde import Kunde
from modelle.bestellung import Bestellung

from repository.bestellungRepo import BestellungRepo
from repository.gekochterGerichtRepo import GekochterGerichtRepo
from repository.getrankRepo import GetrankRepo
from repository.kundeRepo import KundeRepo

class Controller:
    def __init__(self):
        self.bestellung_repo = BestellungRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_bestellungen.json")
        self.getrank_repo = GetrankRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_getranke.json")
        self.kunde_repo = KundeRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_kunden.json")
        self.gekochter_gericht_repo = GekochterGerichtRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_gerichte.json")


    # Create objects
    def create_gekochterGericht(self, portion, preis, zeit):
        gekochterGericht = GekochterGericht(portion, preis, zeit)
        load = self.gekochter_gericht_repo.load()
        load.append(gekochterGericht)
        self.gekochter_gericht_repo.save(load)

    def create_getrank(self, portion, preis, alkohol):
        getrank = Getrank(portion, preis, alkohol)
        load = self.getrank_repo.load()
        load.append(getrank)
        self.getrank_repo.save(load)

    def create_kunde(self, name, adresse):
        kunde = Kunde(name, adresse)
        load = self.kunde_repo.load()
        load.append(kunde)
        self.kunde_repo.save(load)
        return kunde

    def create_bestellung(self, kunden_id, gerichte_ids, getranke_ids):
        bestellung = Bestellung(kunden_id, gerichte_ids, getranke_ids)
        load = self.bestellung_repo.load()
        load.append(bestellung)
        self.bestellung_repo.save(load)


    # Read objects
    def read_gekochter_gericht(self, id):
        objects = self.gekochter_gericht_repo.load()
        if id == '': return objects
        id=int(id)
        for i, obj in enumerate(objects):
            if obj.id == id:
                return [objects[i]]

        raise ValueError("Object with ID {} not found".format(id))

    def read_getrank(self, id):
        objects = self.getrank_repo.load()
        if id == '': return objects
        id=int(id)
        for i, obj in enumerate(objects):
            if obj.id == id:
                return [objects[i]]

        raise ValueError("Object with ID {} not found".format(id))

    def read_kunde(self, id):
        objects = self.kunde_repo.load()
        if id == '': return objects
        id=int(id)
        for i, obj in enumerate(objects):
            if obj.id == id:
                return [objects[i]]

        raise ValueError("Object with ID {} not found".format(id))

    def read_bestellung(self, id):
        objects = self.bestellung_repo.load()
        if id == '': return objects
        id=int(id)
        for i, obj in enumerate(objects):
            if obj.id == id:
                return [objects[i]]

        raise ValueError("Object with ID {} not found".format(id))


    # Update objects
    def update_gekochter_gericht(self, id, portion, preis, zeit):
        gericht = self.read_gekochter_gericht(id)
        if gericht:
            gericht = GekochterGericht(portion, preis, zeit, id)
            self.gekochter_gericht_repo.update(gericht)
            return True
        return False

    def update_getrank(self, id, portion, preis, alkohol):
        getrank = self.read_getrank(id)
        if getrank:
            getrank = Getrank(portion, preis, alkohol, id)
            self.getrank_repo.update(getrank)
            return True
        return False

    def update_kunde(self, id, name, adresse):
        kunde = self.read_kunde(id)
        if kunde:
            kunde = Kunde(name, adresse, id)
            self.kunde_repo.update(kunde)
            return True
        return False


    # Delete objects
    def delete_gekochter_gericht(self, id):
        self.gekochter_gericht_repo.delete(id)

    def delete_getrank(self, id):
        self.getrank_repo.delete(id)

    def delete_kunde(self, id):
        self.kunde_repo.delete(id)

    def delete_bestellung(self, id):
        self.bestellung_repo.delete(id)


    # Such objects
    def suche(self, string, objects):
        string = string.lower()
        search_results = [object for object in objects if string in object.name.lower() or string in object.adresse.lower()]
        return search_results