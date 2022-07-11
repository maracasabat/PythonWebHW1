from abc import ABCMeta, abstractmethod, ABC
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):
    def __init__(self, data, filename):
        self.data = data
        self.__filename = None
        self.filename = filename

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass


class PickleSerialization(SerializationInterface):
    def serialize(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)

    def deserialize(self):
        with open(self.filename, 'rb') as f:
            self.data = pickle.load(f)


class JsonSerialization(SerializationInterface):
    def serialize(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def deserialize(self):
        with open(self.filename, 'r') as f:
            self.data = json.load(f)


if __name__ == '__main__':
    data = {'name': 'Bob', 'age': 25, 'sex': 'male', 'city': 'London'}

    json_file = JsonSerialization(data, 'data.json')
    json_file.serialize()
    json_file.deserialize()

    pickle_file = PickleSerialization(data, 'data.bin')
    pickle_file.serialize()
    pickle_file.deserialize()