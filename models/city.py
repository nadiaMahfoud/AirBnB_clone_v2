#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """Representation of city """
    """ If the storage type is a database ('db'), define the table name"""
    if models.storage_t == "db":
        __tablename__ = 'cities'
        """Define columns for the City table in the database """
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        """ Define a relationship between City and Place (backref)"""
        places = relationship("Place", backref="cities")
    else:
        """If the storage type is not a database, set default values"""
        state_id = ""
        name = ""


    def __init__(self, *args, **kwargs):
    """initializes city"""
    """Call the constructor of the BaseModel class to initialize common attributes"""
    super().__init__(*args, **kwargs)

