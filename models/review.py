#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(
        String(60), ForeignKey('places.id'), nullable=False
    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
