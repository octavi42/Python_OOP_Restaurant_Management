from modelle.gekochterGericht import GekochterGericht
from modelle.getrank import Getrank
from modelle.kunde import Kunde
from modelle.bestellung import Bestellung
from repository.bestellungRepo import BestellungRepo
from controller import Controller
from ui import UI

class Tests:
    def __init__(self):
        self.controller = Controller()
        self.ui = UI()

    def add_gericht(self):
        gericht = GekochterGericht(200, 27.5, "20")
        self.controller.create_gekochterGericht(portion=gericht.portion, preis=gericht.preis, zeit=gericht.zeit)
        objects = self.controller.read_gekochter_gericht('')
        assert gericht.portion == objects[-1].portion
        assert gericht.preis == objects[-1].preis
        assert gericht.zeit == objects[-1].zeit

    def suchen_nach_teilname(self):
        kunde = self.controller.read_kunde('')
        name = "And"
        results = self.controller.suche(name, kunde)
        assert results[0].id == 8

    def suchen_nach_teiladresse(self):
        kunde = self.controller.read_kunde('')
        name = "Luna"
        results = self.controller.suche(name, kunde)
        assert results[0].id == 6

    def update_name_kunde(self):
        id = 9
        name = "Felix"
        adresse = "Bucales"
        self.controller.update_kunde(id, name, adresse)
        kunde = self.controller.read_kunde(9)
        assert kunde[0].name == "Felix"

    def print_string(self):
        bestellung = Bestellung(kunden_ids=[6, 7, 8], gerichte_ids=[20, 88], getranke_ids=[29])

        receipt_string = bestellung._generate_receipt_string()
        result = "Gerichte:\n100: 50.0 €\n300: 50.0 €\nGetränke:\n300: 11.1 €\nKunde:\nCosmin - Luna\nLoti - Sighisoara\nAndrew - Brasov\nTotal: 111.1 €"

        assert receipt_string == result

    def save_bestellung(self):
        bestellung = Bestellung(kunden_ids=[2, 6, 7], gerichte_ids=[20], getranke_ids=[89])
        self.controller.create_bestellung(kunden_ids=bestellung.kunden_ids, gerichte_ids=bestellung.gerichte_ids, getranke_ids=bestellung.getranke_ids)
        objects = self.controller.read_bestellung('')

        assert bestellung.kunden_ids == objects[-1].kunden_ids
        assert bestellung.gerichte_ids == objects[-1].gerichte_ids
        assert bestellung.getranke_ids == objects[-1].getranke_ids
        assert bestellung.total_cost == objects[-1].total_cost

    def load_bestellung(self):
        bestellung = Bestellung(kunden_ids=[2, 6, 7], gerichte_ids=[20], getranke_ids=[89])
        bestellung_repo = BestellungRepo("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/datei_bestellungen.json")
        load = bestellung_repo.load()
        load.append(bestellung)
        bestellung_repo.save(load)
        objects = self.controller.read_bestellung('')

        assert bestellung.id == objects[-1].id
        assert bestellung.kunden_ids == objects[-1].kunden_ids
        assert bestellung.gerichte_ids == objects[-1].gerichte_ids
        assert bestellung.getranke_ids == objects[-1].getranke_ids
        assert bestellung.total_cost == objects[-1].total_cost