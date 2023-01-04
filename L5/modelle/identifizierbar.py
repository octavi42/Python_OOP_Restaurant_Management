class Identifizierbar:
    id = 0

    def __init__(self, id=None):
        self.get_id_count()
        if id is None:
            type(self).id += 1
            self.id = type(self).id
        else:
            self.id = id
        self.save_id_count()

    @classmethod
    def get_id_count(cls):
        with open("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/id_count.txt", "r") as f:
            cls.id = int(f.read())
        

    @classmethod
    def save_id_count(cls):
        with open("/Users/cristeaoctavian/Documents/ubb/fp/teme/L5/datei/id_count.txt", "w") as f:
            f.write(str(cls.id))