#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
# from models.amenity import Amenity
import os  # Import the 'os' module to access environment variables
import models
# from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table

# Check the value of the environment variable 'HBNB_TYPE_STORAGE'
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == "db":
    relationship_table = Table('place_amenity', Base.metadata,
                               Column('place_id', String(60),
                                      ForeignKey('places.id'),
                                      nullable=False),
                               Column('amenity_id', String(60),
                                      ForeignKey('amenities.id'),
                                      nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    if storage_type == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity', secondary=relationship_table,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Place reviews """
            rv = models.storage.all(Review).values()
            return {re for re in rv if re.place_id == self.id}

        @property
        def amenities(self):
            """ Place amenities """
            ob = models.storage.all(Amenity).values()
            return [obj for obj in ob if obj.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """ Amenities setter """
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
