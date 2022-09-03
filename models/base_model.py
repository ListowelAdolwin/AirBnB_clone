#!/usr/bin/python3
"""
Base class for all the classes in the AirBnB clone
project

"""

import uuid
from datetime import datetime
import models


tformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    This is the base class from which all other
    classes of the project will inherrit.

    """

    def __init__(self, *args, **kwargs):
        """
        It takes a variable number of arguments. If no
        argument is provided, it
        initializes the following public instance attributes:
            id: a unique id for all instances of the class
            created_at: the date an instance was created

        Otherwise if there are arguments(It takes an instance of the
        BaseModel class), it uses those values to initilize the
        attributes of the instance to be created
        """
        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Prints a formatted class. Display;
            Class name
            self.id
            self.__dict__

        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the public instance attribute, updated_at

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all the key-values of the
        the __dict__ of the instance
               """

        create_dict = self.__dict__.copy()
        create_dict["created_at"] = create_dict["created_at"].strftime(tformat)
        create_dict["updated_at"] = create_dict["updated_at"].strftime(tformat)
        create_dict["__class__"] = __class__.__name__

        return create_dict
