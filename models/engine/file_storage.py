#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances:
"""
import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ Class serializes and deserializes """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dict """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
          new_dict.update([(key, value.to_dict())])

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
              # we pass the name of the dict and the name of the file(f)
              json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                # deserializate data, we will obtain a dict
                fromjson = json.load(f)
                # update __objects with the load file
                for key, value in fromjson.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
