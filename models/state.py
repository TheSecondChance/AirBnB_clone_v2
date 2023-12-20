#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    sam = Column(String(128), nullable=False)
    name = sam
    ketm = relationship('City', backref='state', cascade='all, delete-orphan')
    cities = ketm
