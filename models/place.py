#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os
from sqlalchemy.orm import relationship, Table
from models import review, amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade='delete, delete-orphan', backref='place')
        amenities = relationship('Amenity', cascade='delete, delete-orphan', backref='place')
    else:
        @property
        def reviews(self):
            all_reviews = models.storage.all(Review).values()
            review_list = []
            for review in all_reviews:
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
