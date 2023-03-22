#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
import os
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey=('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey=('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if os.environ.get('HBNB_TYPE_STORAGE') = 'db':
        reviews = relationship('Place', cascade='delete,
                               delete-orphan', backref='place')
    else:
        @property
        def reviews(self):
            all_reviews = models.storage.all(Review).values()
            review_list = []
            for review in all_reviews:
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
