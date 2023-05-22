#!/usr/bin/python3
"""
This is a simple module and it only has
one class called Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class defines a Amenity that inherits from BaseModel

    Attrs:
        name(str)
    """
    name = ''
