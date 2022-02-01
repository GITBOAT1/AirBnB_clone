#!/usr/bin/python3
""" User class """


from models.base_model import BaseModel
import json


class User(BaseModel):
    """ User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
