#!/usr/bin/python3
"""
This is a simple module and it only has
one class called Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class defines a Place and inherits from BaseModel

    Attrs:
        city_id(str)
        user_id(str)
        name(str)
        description(str)
        number_rooms(int)
        number_bathrooms(int)
        max_guests(int)
        price_by_night(int)
        latitude(float)
        longitude(float)
        amenity_ids(list)
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
