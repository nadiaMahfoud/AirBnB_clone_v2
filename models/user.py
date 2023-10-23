#!/usr/bin/python3
"""This module defines a class User"""

# Import necessary modules and classes
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    # Define the name of the SQL table
    __tablename__ = "users"

    # Define user attributes as columns in the SQL table
    # User's email, which is required
    email = Column(String(128), nullable=False)

    # User's password, which is required
    password = Column(String(128), nullable=False)

    # User's first name
    first_name = Column(String(128))

    # User's last name
    last_name = Column(String(128))

    # Define relationships with other classes
    # A user can have multiple places
    places = relationship('Place', backref='user', cascade='delete')

    # A user can have multiple reviews
    reviews = relationship('Review', backref='user', cascade='delete')
