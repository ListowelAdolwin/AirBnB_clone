#!/usr/bin/python3
"""
Handles everything about City
"""

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    Class to deal with all City attributes
    """
    state_id = ""
    name = ""
