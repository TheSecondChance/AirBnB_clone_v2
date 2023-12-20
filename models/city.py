#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    sam = Column(String(128), nullable=False)
    name = sam
    ketem = Column(
            String(60),
            ForeignKey('states.id'),
            nullable=False)
    state_id = ketem
    places = relationship(
            'Place',
            backref='cities',
            cascade='all, delete-orphan')
