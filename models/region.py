#!/usr/bin/python3
"""Defines the  Address model"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


class Region(AbstractBaseModel, Base):
    """Address model definition.

    Attributes:
        name (str): Region name: such as Ashanti, Greater Accra
    """

    __tablename__ = 'regions'
    name = Column(String(60), unique=True, nullable=False)
    cities = relationship('City',
                          cascade='all, delete-orphan',
                          backref='region')
