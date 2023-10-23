#!/usr/bin/python3
""" This module is the 'Amenity' Module for HBNB project """
from sqlalchemy import Column, String, Table, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models
from os import getenv


class Amenity(BaseModel, Base):
    """
    This is the definition of the class for Amenity

    Attributes:
        name: name of the amenity
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # Relationship with Place for database storage (Many-to-Many)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       viewonly=False,
                                       back_populates="amenities")
    else:
        # Defining the name attribute for non-database storage
        name = ""

    def __init__(self, *args, **kwargs):
        """ This method Initializes Amenity """
        super().__init__(*args, **kwargs)
