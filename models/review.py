#!/usr/bin/python3
"""
This is a simple module and it only has
one class called Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines a Review and inherits from BaseModel

    Attrs:
        place_id(str)
        user_id(str)
        text(str)
    """
    place_id = ''
    user_id = ''
    text = ''
