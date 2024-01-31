#!/usr/bin/python3
""""state a for many to many relationship table
between Place and Amenity record
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """"state a for many to many relationship table
    between Place and Amenity record
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            """"state a for many to many relationship table
            between Place and Amenity record
            """
            cityList = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList
