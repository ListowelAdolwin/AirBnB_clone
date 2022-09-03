#!/usr/bin/python3
"""
A user class to manage the user object
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class to manage the User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
