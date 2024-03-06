#!/usr/bin/python3
"""the state Module for the airbnb project"""
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """the State class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            gets the list of city objects
            """
            my_cityobj = []
            list_of_cities = list(models.storage.all(City).values())
            for city in list_of_cities:
                if city.state_id == self.id:
                    my_cityobj.append(city)
            return my_cityobj
