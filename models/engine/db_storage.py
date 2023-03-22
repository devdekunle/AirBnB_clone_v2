#!/usr/bin/python3
""" Database Storage Engine """
import mysqldb
import os

environment = os.environ.get('HBNB_ENV')
user = os.environ.get('HBNB_MYSQL_USER')
password = os.environ.get('HBNB_MYSQL_PWD')
localhost = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class DBStorage:
    """ Represnts our database """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = DBStorage.__engine
        if __name__ == '__main__':
            conn = MySQLdb.connect(
                host=localhost
                port=3306, user=user,
                passwd=password,
                db=db,
                charset="utf8")
