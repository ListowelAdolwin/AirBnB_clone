#!/usr/bin/python3
"""
Deals with all states in the database
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Class to handle all attributes of the state object
    """

    name = ""
