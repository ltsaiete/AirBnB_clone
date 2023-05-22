#!/usr/bin/python3
"""
This is a simple module and it only has
one class called BaseModel
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This class defines all common attributes/methods for other classes

    Attrs:
        id(str): assigned with uuid when an instance is created
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>'

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict = {**self.__dict__}
        dict['id'] = self.id
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = f'{self.created_at.isoformat()}'
        dict['updated_at'] = f'{self.updated_at.isoformat()}'
        return dict
