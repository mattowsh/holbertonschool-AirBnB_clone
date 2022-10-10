#!/usr/bin/python3
"""
Module that defines the base class for 'AirBnB Clone' project
"""
import uuid
from datetime import datetime


class BaseModel():
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Init constructor to generate new instances:
        ATTRIBUTES
            @id: uniq universal ID in str format
            @created_at: current datetime when an instance is created
            @update_at: current datetime when an instance is updated
        """
        if len(kwargs) > 0:
            dt_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, dt_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, dt_format)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Overrides the __str__ method so that it returns a personalizated
        message in string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute updated_at with the current
        datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
        instance """
        new_dict = self.__dict__.copy()
        to_add = {'__class__': self.__class__.__name__}
        new_dict.update(to_add)

        for key, value in new_dict.items():
            if key == "created_at":
                new_dict.update([(key, value.isoformat())])
            elif key == "updated_at":
                new_dict.update([(key, value.isoformat())])
            else:
                new_dict.update([(key, value)])

        return new_dict
