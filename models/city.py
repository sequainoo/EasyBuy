#!/usr/bin/python3
"""Defines the  Address model"""

from sqlalchemy import Column, String, ForeignKey

from models.base import AbstractBaseModel, Base


class City(AbstractBaseModel, Base):
    """Address model definition.

    Attributes:
        name (str): city name
        Region_id (str): Region located such as Ashanti, Greater Accra.
    """

    __tablename__ = 'cities'
    name = Column(String(60), unique=True, nullable=False)
    region_id = Column(String(60),
                       ForeignKey('regions.id'),
                       nullable=False)
