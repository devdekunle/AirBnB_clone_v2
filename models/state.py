#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='delete')

    @property
    def cities(self):
        """ getter attribute cities that returns the list of City
        instances with state_id equals to the current State.id"""
        all_cities = storage.all(City).values()
        city_list = []
        for city in all_cities:
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
