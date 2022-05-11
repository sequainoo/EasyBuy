#!/usr/bin/python3
"""Defines the Phone Model"""

from models.base import AbstractBaseModel


class Phone(AbstractBaseModel):
    """Model of Phone

    Attributes:
        id (str): unique identity
        date_created (datetime): date and time created
        date_modified (datetime): date and time phone is updated
        name (str): name of phone
        description (str): a description of phone
        brand_id (str): the id of the phone's brand
        quantity (int): the number of instances of the phone in stock
        price (float): the price of the phone

    Relationship:
        images: a list of images related to the phone
    """

    name = ''
    description = ''
    brand_id = ''
    quantity = 0
    price = 0.00
    images = []
