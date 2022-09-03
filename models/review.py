#!/usr/bin/python3
"""
Handles the review section
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class that deals with all instances of the Review
    """
    place_id = ""
    user_id = ""
    text = ""
    