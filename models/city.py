#!/usr/bin/python3
""" class City that inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ class city """
    # will be the state.id
    state_id = ""
    name = ""
