#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
   recreate a BaseModel from another one by using a
   dictionary representation
"""


class FileStorage:
    """
    A class FileStorage that serializes instances to a JSON
    file and deserializes JSON file to
    instances

    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by
    <class name>.id (ex: to store a
    BaseModel object with id=12121212, the key will be
    BaseModel.12121212)

    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    """
       def __init__(self):
        "" initialize the class attribute ""
        self.file_path = __file_path
        self.objects = __objects
    """

    def all(self):
        """   string - path to the JSON file """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            data = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[data] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        jdata = {}
        print("hollo"*3)
        for i, j in self.__objects.item():
            jdata[i] = j.to_dict()
            print("{} _> fom i".format(i))
        with open(self.__file_path, 'w') as f:
            json.dump(jdata, f)

    def reload(self):
        """  deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
