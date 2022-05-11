#!/usr/bin/python3
"""Defines the  Address model"""

from models.base import AbstractBaseModel


class Address(AbstractBaseModel):
    """Address model definition.

    Attributes:
        user_id (str): user with that address
        Region_id (str): Region located such as Ashanti, Greater Accra.
        city_id (str): city with the region
        Town (str): Town of the address
        phone_number (str): ten or 13(with code prefix and + sign) digit phone number
    """
    user_id = ''
    region_id = ''
    city_id = ''
    town = ''
    phone_number = ''
