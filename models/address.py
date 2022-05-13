#!/usr/bin/python3
"""Defines the  Address model"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


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
    customer_id = Column(String(60),
                       ForeignKey('customers.id'),
                       nullable=False)
    region_id = Column(String(60),
                       ForeignKey('regions.id'),
                       nullable=False)
    city_id = Column(String(60),
                       ForeignKey('regions.id'),
                       nullable=False)
    town = Column(String(60), nullable=False)
    phone_number = Column(String(60), unique=True, nullable=False)
