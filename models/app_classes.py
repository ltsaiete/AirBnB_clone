#!/usr/bin/python3
"""This module defines a variable that will return
dict mapping all models of the application
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

appClasses = {
    'BaseModel': BaseModel,
    'Amenity':  Amenity,
    'User': User,
    'City':  City,
    'Place':  Place,
    'Review':  Review,
    'State':  State
}
