#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv



storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    '''
        Implementation for the State class.
    '''
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    if storage_type != 'db':
        @property
        def cities(self):
            """
            list of City instances with state_id
            """
            cityList = []
            allCity = models.storage.all(City)
            for key, objCity in allCity.items():
                if objCity.state_id == self.id:
                    cityList.append(objCity)
            return cityList
