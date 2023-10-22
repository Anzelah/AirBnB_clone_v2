#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import os
from datetime import datetime
from models.base_model import BaseModel, Base
import models
#from models.city import City

class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__= 'states'

        name = Column(String(128), nullable=False)
#        created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
#        updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ""

        @property
        def cities(self):
            """Return list of City objects from storage"""
            list_city = []
#            import models
            the_cities = models.storage.all(City)
            for k, v in the_cities.values():
                if v.state_id == self.id:
                    list_city.append(c)

            return (list_city)
