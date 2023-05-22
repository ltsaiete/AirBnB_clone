#!/usr/bin/python3
"""
This is a simple module and it only has
one class called City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class defines a City that inherits from BaseModel

    Attrs:
        state_id(str)
        name(str)
    """
    state_id = ''
    name = ''
