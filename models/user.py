#!/usr/bin/python3
"""
This is a simple module and it only has
one function called fun_name
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines a user and inherits from BaseModel

    Attrs:
        email(str)
        password(str)
        first_name(str)
        last_name(str)
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
