#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances:
"""
import json
from os.path import isfile


class FileStorage():
    """ Class serializes and deserializes """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dict """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            # we pass the name of the dict and the name of the file(f)
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                # update __objects with the load file 
                self.__objects.update(json.loads(f.read()))
