"""This is the core module : mostly data classes to manage Friends."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['parsed_date', 'Friend', 'Repository']

# %% ../nbs/00_core.ipynb 2
from datetime import datetime,date
from dateutil import parser as dtparse     
from dataclasses import dataclass
from uuid import uuid4

# %% ../nbs/00_core.ipynb 4
def parsed_date(s:str):
    "Convert `s` to a datetime"
    return dtparse.parse(s)

# %% ../nbs/00_core.ipynb 8
@dataclass
class Friend:
    """Class for keeping track of a friend item."""
    id: str
    family_name: str
    first_name: str
    email: str
    phone: str
    linkedin: str
    twitter: str

# %% ../nbs/00_core.ipynb 10
from fastsql import *
import sqlalchemy as sa

# %% ../nbs/00_core.ipynb 19
class Repository:
    """Repository Service for the Friend dataclass. 
    The repository implementation is based on SQLLite with a file storage"""
    
    def __init__(self, _db_file_path:str):
        """
        Constructor

        Parameters:
          _db_file_path: relative path of the file (to the script) 
        """
        self.db_file_path = _db_file_path
        self.create()

    def create(self):
        """
        Creates the database
        """
        uri = 'sqlite:///'+self.db_file_path
        self.db = Database(uri)
        self.store = self.db.create(Friend, pk='id')

    def add_obj(self, f:Friend):
        random_uuid = uuid4()
        """
        Adds a Friend object to the repository
        """
        self.store.insert(f)

    def add(self, family_name: str, 
            first_name: str,
            email: str,
            phone: str,
            linkedin: str,
            twitter: str):
        """
        Creates and Adds a Friend to the repository
        """
        random_uuid = uuid4() # str(random_uuid)
        friend = Friend(str(random_uuid), family_name, first_name, email, phone, linkedin, twitter)
        self.add_obj(friend)

    def friends(self):
        return self.store() 
    
    def __repr__(self):
        return "Repository SQLLite at " + self.db_file_path
