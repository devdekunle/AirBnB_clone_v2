#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os

class Amenity(BaseModel, Base):
    """ represent amenities table """
    __tablename__ = 'amenities'

    name = Column(
        String(128), nullable=False

    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''
