#!/usr/bin/python3
"""the Place Module for the airbnb project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from os import getenv
from models.review import Review
from models.amenity import Amenity
import models
from sqlalchemy.orm import relationship

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """info about place to stay at"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """returns a list of amenities instances"""
            all_amenities = []
            amenities_instances = list(models.storage.all(Amenity).values())
            for amenity in amenities_instances:
                if amenity.id in self.amenity_ids:
                    all_amenities.append(amenity)
            return all_amenities

        @amenities.setter
        def amenities(self, value):
            """setter attribute that handles append method"""
            if isinstance(value, "Amenity"):
                self.amenity_ids.append(value.id)
