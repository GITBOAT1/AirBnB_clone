#!/usr/bin/python3
from models.base_model import BaseModel

"""
   recreate a BaseModel from another one by using a 
   dictionary representation
"""

class FileStorage(BaseModel):
    """
    A class FileStorage that serializes instances to a JSON file and deserializes JSON file to 
    instances

    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a
    BaseModel object with id=12121212, the key will be BaseModel.12121212)

    """
    __file_path = "file.json"
    __objects   = {}
    

    """
       def __init__(self):
        "" initialize the class attribute ""
        self.file_path = __file_path
        self.objects = __objects
    """

    def all(self):
        """   string - path to the JSON file """
        return BaseModle.to_Dict()

    @property
    def new(self, obj):
        """ sets in __objects the obj with key """
        return self.obj

    @new.setter
    def new(self, obj):
        self.obj = __objects
        
    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "a")as f:
            json.dump(all(), f)
        
    def reload(self):
        """  deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__object = json.load(f)
        except FileNotFoundError:
            pass   
