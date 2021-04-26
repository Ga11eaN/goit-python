from abc import abstractmethod, ABC
import json
import pickle

class SerializationInterface(ABC):
    
    @abstractmethod
    def save_to_json(self):
        pass
        
    @abstractmethod
    def save_to_byte(self):
        pass

class SomeData(SerializationInterface):
    
    def __init__(self, data):
        self.data = data
        
    def save_to_json(self):
        with open('some_data.json', 'w') as fh:
            json.dump(self.data, fh)
        
    def save_to_byte(self):
        with open('some_data.bin', 'wb') as fh:
            pickle.dump(self.data, fh)

class Meta(type):
    class_list = []
    
    def __new__(*args):
        if not args[1] in Meta.class_list:
           Meta.class_list.append(args[1])
        args[3]['class_number'] = Meta.class_list.index(args[1])    
        instance = type.__new__(*args)
        return instance

Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)