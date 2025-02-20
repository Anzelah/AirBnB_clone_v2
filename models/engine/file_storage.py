#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
import models


class FileStorage():
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models of specific class in storage"""

        if cls is None:
            return FileStorage.__objects
        else:
            class_objects = {}
            for key, value in FileStorage.__objects.items():
                if cls == type(value):
                    class_objects[key] = value
            return class_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete objects from class attribute __objects if inside"""
        if obj is None:
            pass
        else:
            for key, value in FileStorage.__objects.items():
                if value == type(obj):
                    del(obj)
                    del FileStorage.__objects[key]
                    self.save()

    def close(self):
        """deserealize the json file to objects"""
        self.reload()
