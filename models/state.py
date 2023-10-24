#!/usr/bin/python3
""" This is the State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


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
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete,  delete-orphan")

    # For FileStorage:
    # Getter attribute to return a list of City instances
    # with state_id equals to the current State.id
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            # Creating an empty list to store the City instances
            # associated with this State
            cities_list = []

            # Getting all the City instances from the storage
            all_cities = models.storage.all("City")

            # Iterating through all the City instances
            for city in all_cities.values():

                # Checking if the state_id of the City matches id of this State
                if city.state_id == self.id:

                    # If there's a match, add the City instance to the list
                    cities_list.append(city)

            # Returning the list of City instances associated with this State
            return cities_list
