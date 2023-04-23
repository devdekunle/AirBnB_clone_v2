#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True, default=str(uuid4()))
    created_at = Column(String(100), default=datetime.utcnow(), nullable=False)
    updated_at = Column(String(100), default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a string representation of the instance"""
        dictionary = self.__dict__.copy()
        keys = dictionary.keys()
        if '_sa_instance_state' in keys:
            del dictionary['_sa_instance_state']
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        if hasattr(self, '_sa_instance_state'):
            del self._sa_instance_state
        dictionary = {}
        dictionary.update(self.__dict__.copy())
        obj_keys = dictionary.keys()
        if '_sa_instance_state' in obj_keys:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """to delete the current instance from the models.storage"""
        self.models.storage.delete(self)
