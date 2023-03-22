#!/usr/bin/python3
""" Database Storage Engine """
import mysqldb
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

env = os.environ.get('HBNB_ENV')
user = os.environ.get('HBNB_MYSQL_USER')
password = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class DBStorage:
    """ Represnts our database """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize new db engine"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(user, password, host, db),
            pool_pre_ping=True)

        #drop all tables if the environment variable
        #HBNB_ENV is equal to test
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            query on the current database session (self.__session)
            all objects depending of the class name (argument cls)
        """
        from models import classes
        objects = {}

        if cls is None:
            for cls in classes.values():
                for obj in self.__session.query(cls).all():
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objects[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = f'{obj.__class__.__name__}.{obj.id}'
                objects[key] = obj

        return objects

    def new(self, obj):
        """add the object to the current
           database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
