#!/usr/bin/python3
"""
This is a simple module and it only has
one class called FileStorage
"""
import json
from models.app_classes import appClasses
from models.base_model import BaseModel


class FileStorage:
    """
    This serializes instances to a JSON file
    and deserializes JSON file to instances

    Attrs:
        __file_path(str): path to the JSON file (ex: file.json)
        __objects(dict): will store all objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        # returns the dictionary __objects
        return FileStorage.__objects

    def new(self, obj):
        # sets in __objects the obj with key <obj class name>.id
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        # serializes __objects to the JSON file (path: __file_path)
        dicts = {}
        for k, v in FileStorage.__objects.items():
            dicts[k] = v.to_dict()
        json_str = json.dumps(dicts)

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(json_str)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as file:
                json_dict = file.read()
        except FileNotFoundError:
            return

        dicts = json.loads(json_dict)

        for k, v in dicts.items():
            # print(BaseModel)
            dicts[k] = appClasses[k.split('.')[0]](**v)

        FileStorage.__objects = dicts
