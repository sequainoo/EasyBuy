#!/usr/bin/python3
"""Defines the  Address model"""

from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base
from utilities import small_helpers

class Address(AbstractBaseModel, Base):
    """Address model definition.

    Attributes:
        user_id (str): user with that address
        Region_id (str): Region located such as Ashanti, Greater Accra.
        city_id (str): city with the region
        Town (str): Town of the address
        phone_number (str): ten or 13(with code prefix and + sign) digit phone number
    """

    __tablename__ = 'addresses'
    id = Column(String(40), unique=True, default=small_helpers.uuid4)
    customer_id = Column(String(60),
                       ForeignKey('customers.id'),
                       primary_key=True,
                       nullable=False)
    region_id = Column(String(60),
                       ForeignKey('regions.id'),
                       primary_key=True,
                       nullable=False)
    city_id = Column(String(60),
                       ForeignKey('cities.id'),
                       primary_key=True,
                       nullable=False)
    town = Column(String(60), nullable=False, primary_key=True,)
    phone_number = Column(String(60), nullable=False)
    default = Column(Boolean, nullable=False, default=True)
    region = relationship('Region')
    city = relationship('City')
