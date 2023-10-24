#!/usr/bin/python3
"""This module is a database storage definition"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """This is the DBStorage class

    Attributes:
        __engine
        __session
    """
    # Private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """
        This method creates the engine with configuration
        from environment variables
        """
        # Setting the connection details for the database
        # from environment variables
        db_user = getenv("HBNB_MYSQL_USER")
        db_password = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")

        # Creating the engine with the specified dialect, driver,
        # and connection details
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(db_user, db_password, db_host,
                                             db_name), pool_pre_ping=True)

        # Dropping all tables if HBNB_ENV is 'test'
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        This method is to query all the objects in the database session"""
        session = self.__session
        results_dict = {}
        classes = [State, City, User, Place, Review, Amenity]

        if cls is not None:
            query = session.query(cls)
        else:
            query = session.query(*classes)

        for item in query.all():
            key = "{}.{}".format(item.__class__.__name__, item.id)
            results_dict[key] = item

        return results_dict

    def new(self, obj):
        """
        This method adds the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        This method commits all the changes in the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """
        This method deletes the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        This method creates tables and a new database session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
        self.__session = Session()

    def get(self, cls, id):
        """
        This method is retrieving an object based on class name and id
        """
        if cls and id:
            objects = self.all(cls)
            key = "{}.{}".format(cls.__name__, id)
            return objects.get(key)
        return None

    def count(self, cls=None):
        """
        This method counts the number of objects in
        the database for a given class

        If cls is None, count all objects.
        """
        return len(self.all(cls))

    def close(self):
        """
        This method closes the current session
        """
        self.__session.close()
