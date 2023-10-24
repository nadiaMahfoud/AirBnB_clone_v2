#!/usr/bin/python3
""" This module is the 'Amenity' Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    This is the definition of the class for Amenity

    Attributes:
        name: name of the amenity
    """
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ' '
