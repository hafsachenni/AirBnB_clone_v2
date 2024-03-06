#!/usr/bin/python3
"""module that defines the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """defining a user by his attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places= relationship("Place", backref="user", cascade="delete")
    reviews= relationship("Review", backref="user", cascade="delete")
