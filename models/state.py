#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey  # Import Integer for primary key
from sqlalchemy.orm import relationship
import os
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)

        # Unconditional relationship definition
        from models.city import City
        cities = relationship('City', cascade='delete', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Return list of City objects from storage"""
            list_city = []
            import models
            the_cities = models.storage.all(City)
            for k, v in the_cities.values():
                if v.state_id == self.id:
                    list_city.append(c)

            return (list_city)
