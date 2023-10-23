#!/usr/bin/python3
""" Review module for the HBNB project"""


# Import necessary modules and classes
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Review class to store review information"""
    # Define the name of the SQL table
    __tablename__ = 'reviews'

    # Define columns in the SQL table for review attributes
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
