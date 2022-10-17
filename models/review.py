#!/usr/bin/python3
""" class Review that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class review """
    # will be the Place.id
    place_id = ""
    # will be the User.id
    user_id = ""
    text = ""
