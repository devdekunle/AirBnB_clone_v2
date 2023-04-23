#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


""" create a new table place_amenity that represents a relationship between
    Amenity and Place
"""
if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
        ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False

        )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(
        String(60), ForeignKey('cities.id'), nullable=False

    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False

    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
        String(128), nullable=False

    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(
        String(1024), nullable=True

    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(
        Integer, nullable=False, default=0

    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(
        Integer, nullable=False, default=0

    ) if os.environ.get('HBNB_TYOE_STORAGE') == 'db' else 0
    max_guest = Column(
        Integer, nullable=False, default=0

    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(
        Integer, nullable=False, default=0
    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(
        Float, nullable=True
    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(
        Float, nullable=True
    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = []

    reviews = relationship(
        'Review',
        cascade='all, delete, delete-orphan',
        backref='place'
    ) if os.environ.get('HBNB_TYPE_STORAGE') == 'db' else None
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            backref='place_amenities'
        )
    else:
        @property
        def reviews(self):
            from models.review import Review

            all_reviews = models.storage.all(Review).values()
            review_list = []
            for review in all_reviews:
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            returns the list of Amenity instances based
            on the attribute amenity_ids that contains
            all Amenity.id linked to the Place
            """
            from models.amenity import Amenity
            import models
            place_amenity_list = []
            all_amenity = models.storage.all(Amenity).values()
            for obj in all_amenity:
                if obj.id in self.amenity_ids:
                    place_amenity_list.append(obj)
            return place_amenity_list

        @amenities.setter
        def amenities(self, obj):
            """
            that handles append method for adding an
            Amenity.id to the attribute amenity_ids
            """
            if obj.__class__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
