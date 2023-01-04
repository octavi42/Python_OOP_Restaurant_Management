from controller import Controller

class UI:
    def __init__(self):
        self.controller = Controller()

    def start(self):
        print("1 - Bestellung registriren") # muss in lage sein costumer entweder zu suchen oder hinzufugen
        print("2 - Manage")

        imp = int(input("Option = "))

        if imp == 1:
            self.register()
        elif imp == 2:
            self.manage()
        else:
            print("falsches Option, versuch noch mal")
            self.select_op(self)

    def manage(self):
        print()
        print(">------------")
        print()
        print("Manage: \n")
        print("1 - Kunden")
        print("2 - Gericht")
        print("3 - Getrank")

        imp1 = int(input("Option = "))

        print()
        print(">------------")
        print()
        print("1 - Hinzufugen")
        print("2 - Anzeigen")
        print("3 - Aktualisieren")
        print("4 - Loschen")

        imp2 = int(input("Option = "))

        self.crud(imp1, imp2)

        print("\n")

    def crud(self, edit, type):
        if edit == 1:
            if type == 1:
                self.create_kunde()
            elif type == 2:
                self.read_kunde()
            elif type == 3:
                self.update_kunde()
            elif type == 4:
                self.delete_kunde()
            else:
                print("falsches Option, versuch noch mal")
        elif edit == 2:
            if type == 1:
                self.create_gericht()
            elif type == 2:
                self.read_gericht()
            elif type == 3:
                self.update_gericht()
            elif type == 4:
                self.delete_gericht()
            else:
                print("falsches Option, versuch noch mal")
        elif edit == 3:
            if type == 1:
                self.create_getrank()
            elif type == 2:
                self.read_getrank()
            elif type == 3:
                self.update_getrank()
            elif type == 4:
                self.delete_getrank()
            else:
                print("falsches Option, versuch noch mal")
        else:
            print("falsches Option, versuch noch mal")

    def register(self):
        print()
        print()
        print("Bestellung: \n")
        print("1 - Registrieren")
        print("2 - Lesen")

        imp = int(input("Option = "))

        if imp == 1:
            self.create_bestellung()
        elif imp == 2:
            self.read_bestellung()
        else:
            print("falsches Option, versuch noch mal")
            self.register()


    def create_kunde(self):
        name = str(input("Name = "))
        adresse = str(input("Adresse = "))
        return self.controller.create_kunde(name, adresse)

    def read_kunde(self):
        id = input("ID = ")
        print()
        objects = self.controller.read_kunde(id)
        for object in objects:
            print("id = ", object.id)
            print("name = ", object.name)
            print("adresse = ", object.adresse)
            print()

    def update_kunde(self):
        id = int(input("ID = "))
        name = str(input("Name = "))
        adresse = str(input("Adresse = "))
        self.controller.update_kunde(id, name, adresse)

    def delete_kunde(self):
        id = int(input("ID = "))
        print()
        if self.check_for_bestellung(id):
            self.controller.delete_kunde(id)
        else:
            print("Ok, nicht geloscht")

    def create_gericht(self):
        portion = int(input("Portion = "))
        preis = float(input("Preis = "))
        zeit = str(input("Zeit = "))
        self.controller.create_gekochterGericht(portion, preis, zeit)

    def read_gericht(self):
        id = input("ID = ")
        print()
        objects = self.controller.read_gekochter_gericht(id)
        for object in objects:
            print("id = ", object.id)
            print("portion = ", object.portion)
            print("preis = ", object.preis)
            print("zeit = ", object.zeit)
            print()

    def update_gericht(self):
        id = int(input("ID = "))
        portion = int(input("Portion = "))
        preis = float(input("Preis = "))
        zeit = str(input("Zeit = "))
        self.controller.update_gekochter_gericht(id, portion, preis, zeit)

    def delete_gericht(self):
        id = int(input("ID = "))
        print()
        if self.check_for_bestellung(id):
            self.controller.delete_gekochter_gericht(id)
        else:
            print("Ok, nicht geloscht")


    def create_getrank(self):
        portion = int(input("Portion = "))
        preis = float(input("Preis = "))
        alkohol = str(input("Alkohol = "))
        self.controller.create_getrank(portion, preis, alkohol)

    def read_getrank(self):
        id = input("ID = ")
        print()
        objects = self.controller.read_getrank(id)
        for object in objects:
            print("id = ", object.id)
            print("portion = ", object.portion)
            print("preis = ", object.preis)
            print("alkohol = ", object.alkohol)
            print()

    def update_getrank(self):
        id = int(input("ID = "))
        portion = int(input("Portion = "))
        preis = float(input("Preis = "))
        zeit = str(input("Zeit = "))
        self.controller.update_getrank(id, portion, preis, zeit)

    def delete_getrank(self):
        id = int(input("ID = "))
        print()
        if self.check_for_bestellung(id):
            self.controller.delete_getrank(id)
        else:
            print("Ok, nicht geloscht")
        

    
    def create_bestellung(self):

        kunden = []
        while True:
            print()
            print()
            print("Wie soll man die Kunden hineinfugen? (done wenn du fertig bist)")
            print()
            print("1 - Suchen")
            print("2 - Fugen")
            print("3 - id")
            inp = input("Option = ")
            if inp == "done":
                break
            elif int(inp) == 1:
                kunden.append(self.such_bestellung().id)
            elif int(inp) == 2:
                kunde = self.create_kunde()
                print()
                print("Mochtest du den neuen Kunde in Bestellung speichern? (Ja/Nein)")
                inp = input()
                if inp.lower() == 'ja':
                    kunden.append(kunde.id)
                elif inp.lower() == 'nein':
                    print("Ok, kunde nicht gespeichert")
            elif int(inp) == 3:
                id = input("Kunde id = ")
                kunden.append(int(id))

        gerichts = []
        while True:
            print("Gericht id ( -1 wenn fertig ):")
            id = input()
            if id == "-1":
                break
            gerichts.append(int(id))

        getranke = []
        while True:
            print("Getrank id ( -1 wenn fertig ):")
            id = input()
            if id == "-1":
                break
            getranke.append(int(id))
        self.controller.create_bestellung(kunden, gerichts, getranke)

        # print()
        # print(">------------")
        # print()
        # print("Create Bestellung durch: \n")
        # print("1 - Suchen")
        # print("2 - Lesen")
        # print("3 - Id")

        # imp = int(input("Option = "))

        # if imp == 1:
        #     self.create_bestellung_suchen()
        # elif imp == 2:
        #     self.create_bestellung_lesen()
        # elif imp == 3:
        #     self.create_bestellung_id()
        # else:
        #     print("falsches Option, versuch noch mal")
        #     self.create_bestellung()


    def such_bestellung(self):
        kunden = self.controller.read_kunde('')
        print()
        print()
        string = input("Name oder Adresse des Kundes = ")
        print()
        print("such resultat:")
        results = self.controller.suche(string, kunden)
        for i, result in enumerate(results):
            print("number = ", i)
            print("name = ", result.name)
            print("adresse = ", result.adresse)
            print()
        item_to_add = int(input("number of the item to add = "))
        return results[item_to_add]

    def read_bestellung(self):
        print("screib 'all' wenn alle bestellungen zuruckgegeben werden soll")

        id = input("ID = ")
        objects = self.controller.read_bestellung(id)
        for object in objects:
            print()
            print()
            print("id: ", object.id)
            print("kunden_ids: [")
            for obj in object.kunden_ids:
                print("     {")
                print("         id: ", self.controller.read_kunde(obj)[0].id)
                print("         name: ", self.controller.read_kunde(obj)[0].name)
                print("         adresse: ", self.controller.read_kunde(obj)[0].adresse)
                print("     }")
            print("]")

            print("gerichte_ids: [")
            for obj in object.gerichte_ids:
                print("     {")
                print("         id: ", self.controller.read_gekochter_gericht(obj)[0].id)
                print("         portion: ", self.controller.read_gekochter_gericht(obj)[0].portion)
                print("         preis: ", self.controller.read_gekochter_gericht(obj)[0].preis)
                print("     }")
            print("]")

            print("getranke_ids: [")
            for obj in object.getranke_ids:
                print("     {")
                print("         id: ", self.controller.read_getrank(obj)[0].id)
                print("         portion: ", self.controller.read_getrank(obj)[0].portion)
                print("         preis: ", self.controller.read_getrank(obj)[0].preis)
                print("         alkohol: ", self.controller.read_getrank(obj)[0].alkohol)
                print("     }")
            print("]")

            print("total_cost: ", object.total_cost)
            print()


    def check_for_bestellung(self, id):
        objects = self.controller.read_bestellung('')
        for object in objects:
            if id in object.kunden_ids:
                print("Es gibt eine bestellung mit dieses id, mochtest du es doch loschen?")
                print("1 - Ja")
                print("2 - Nein")
                inp = int(input("Option = "))
                if inp == 1: 
                    self.controller.delete_bestellung(object.id)
                    return True
                elif inp == 2: return False
            else: return True