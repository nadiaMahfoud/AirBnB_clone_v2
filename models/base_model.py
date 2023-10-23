#!/usr/bin/python3
"""ThIs module defines a base class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

# Creating a declarative base for SQLAlchemy
Base = declarative_base()


class BaseModel:
    """This class is a base class for all the hbnb models"""

    # Unique ID for the model, 60 characters, primary key, cannot be null
    id = Column(String(60), primary_key=True, nullable=False)

    # Timestamp for when the instance was created, cannot be null
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    # Timestamp for when the instance was last updated, cannot be null
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ This method instantiates a new model"""
        if not kwargs:
            # Generating a unique ID
            self.id = str(uuid.uuid4())
            # Setting the 'created_at','updated_at' timestamps to current time
            self.created_at = self.updated_at = datetime.now()
        else:
            if 'created_at' in kwargs:
                # Converting the 'created_at' timestamp to a datetime object
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                # Converting the 'updated_at' timestamp to a datetime object
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                # Setting the attributes based on key-value pairs in kwargs
                setattr(self, key, value)

    def __str__(self):
        """This method returns a string representation of the instance"""
        # Getting the class name as a string
        class_str = (str(type(self)).split('.')[-1]).split('\'')[0]
        d = self.__dict__.copy()
        # Remove SQLAlchemys internal state attribute
        d.pop('_sa_instance_state', None)
        # Returning the formatted string representation of the instance
        return '[{}] ({}) {}'.format(class_str, self.id, d)

    def save(self):
        """This method updates 'updated_at' with the current time
        and saves the instance
        """
        # Updating the 'updated_at' timestamp to the current time
        self.updated_at = datetime.now()
        # Adding the new instance to the storage
        models.storage.new(self)
        # Saving the instance using the storage
        models.storage.save()

    def to_dict(self):
        """This method converts the instance into a dictionary format"""
        d = self.__dict__.copy()
        # Formatting the 'created_at''updated_at' timestamps as ISO strings
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        # Removing SQLAlchemy internal state attribute
        d.pop('_sa_instance_state', None)
        # Returning a dictionary representation of the instance
        return d

    def delete(self):
        """This method deletes the current instance from storage"""
        # Deleting the instance from the storage
        models.storage.delete(self)
