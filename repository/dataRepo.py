from abc import ABC, abstractmethod

class DataRepo(ABC):
    def __init__(self, datei):
        self.datei = datei

    def save(self, objects):
        data = self.convert_to_string(objects)
        self.write_to_file(data)

    def load(self):
        data = self.read_file()
        return self.convert_from_string(data)

    def read_file(self):
        with open(self.datei, "r") as f:
            return f.read()

    def write_to_file(self, data):
        with open(self.datei, "w") as f:
            f.write(data)

    def update(self, object_to_update):
        objects = self.load()

        for i, obj in enumerate(objects):
            if obj.id == object_to_update.id:
                objects[i] = object_to_update

                self.save(objects)
                return

        raise ValueError("Object with ID {} not found".format(object_to_update.id))


    def delete(self, object_to_delete):
        objects = self.load()

        for i, obj in enumerate(objects):
            if obj.id == object_to_delete:
                del objects[i]

                self.save(objects)
                return

        raise ValueError("Object with ID {} not found".format(object_to_delete))


    @abstractmethod
    def convert_to_string(self, objects):
        pass

    @abstractmethod
    def convert_from_string(self, string):
        pass