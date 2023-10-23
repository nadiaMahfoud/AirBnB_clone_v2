#!/usr/bin/python3
"""This module defines a class User"""

"""Import necessary modules and classes"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    """Define the name of the SQL table"""
    __tablename__ = "users"


    """ Define user attributes as columns in the SQL table"""
    email = Column(String(128), nullable=False)  """ User's email, which is required"""
    password = Column(String(128), nullable=False)  """ User's password, which is required"""
    first_name = Column(String(128)  """ User's first name"""
    last_name = Column(String(128)  """ User's last name"""


    """ Define relationships with other classes"""
    places = relationship('Place', backref='user', cascade='delete')  # A user can have multiple places
    reviews = relationship('Review', backref='user', cascade='delete')  # A user can have multiple reviews

