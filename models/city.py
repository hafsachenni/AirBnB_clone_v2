#!/usr/bin/python3
"""the city Module for the airbnb project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.place import Place
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """city class that contains the state ID and name"""
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
