#!/usr/bin/python3
""" Database Storage Engine """
import MySQLdb
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base


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
    classes = {'User': User,
               'Place': Place, 'State': State, 'City': City,
               'Review': Review, 'Amenity': Amenity}

    def __init__(self):
        """ Initialize new db engine"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(user, password, host, db),
            pool_pre_ping=True)

        """drop all tables if the environment variable
           HBNB_ENV is equal to test
        """
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            query on the current database session (self.__session)
            all objects depending of the class name (argument cls)
        """
        objects = {}
        if cls is None:
            for class_ in DBStorage.classes.values():
                modl = "{}".format(class_.__name__)
                for obj in self.__session.query(DBStorage.classes[modl]).all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[key] = obj

        else:
            model = "{}".format(cls.__name__)
            for obj in self.__session.query(DBStorage.classes[model]).all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
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

    def reload(self):

        """restarts database engine"""

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
