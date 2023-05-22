#!/usr/bin/python3
"""
This is a simple module and it only has
one function called fun_name
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class defines a State that inherits from BaseModel

    Attrs:
        name(str)
    """
    name = ''
