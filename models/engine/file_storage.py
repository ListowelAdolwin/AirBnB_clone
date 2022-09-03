#!/usr/bin/python3
"""
Handles the serialization and desserialization of all
objects in the project
Converts objects to JSON and vice versa
"""

import json
from models.base_model import BaseModel
import os
from models.user import User


class FileStorage:
    """
    This class contain methods that deals with the storage
    of data in the project

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the objects/instances in the class attribute
        __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new instance, obj to the dictionary, __object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the object, __object to a JSON file, __file_path
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(new_dict, f, indent=4)
        except FileNotFoundError:
            pass

    def reload(self):
        try:
            if (os.path.isfile(FileStorage.__file_path)):
                _dict = {}
                with open(FileStorage.__file_path, "r") as f:
                    _dict = json.load(f)

                new_dict = {}
                for key, value in _dict.items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**value)
                    new_dict[key] = obj

                FileStorage.__objects = new_dict

        except FileNotFoundError:
            pass
