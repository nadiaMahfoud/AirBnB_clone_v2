#!/usr/bin/python3
""" This is the State Module for HBNB project """

import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from models.city import City
from sqlalchemy import String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ This is the definition of a State class """
    # The following is the Table name for the State class
    __tablename__ = "states"

    # Setting the name of the state, up to 128 characters, cannot be null
    name = Column(String(128), nullable=False)

    # Defining a relationship with the City class
    # For DBStorage:
    # Linked City obj are automatically deleted if the State obj is deleted
    # And, set the reference from City to State as 'state'
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related Cities."""
            city_l = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
