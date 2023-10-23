#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

# Import the FileStorage class from the models.engine.file_storage module
from models.engine.file_storage import FileStorage
# Import the DBStorage class from the models.engine.db_storage module
from models.engine.db_storage import DBStorage
#  Import the getenv function from the os module
from os import getenv


"""  Check if the environment variable HBNB_TYPE_STORAGE is set to 'db'"""
if getenv("HBNB_TYPE_STORAGE") == 'db':
    # If it is, create an instance of DBStorage
    # and assign it to the 'storage' variable
    storage = DBStorage()
else:
    # If it's not set to 'db', create an instance of FileStorage
    # and assign it to the 'storage' variable
    storage = FileStorage()

    # Load data into the 'storage' object,
    # which could be either FileStorage
    # or DBStorage based on the condition above"""
    storage.reload()
