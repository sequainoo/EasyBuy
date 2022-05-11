#!/usr/bin/python3
"""Defines the OrderItem model"""

from models.base import BaseModel


class OrderItem(BaseModel):
    """Model of Phone

    Attributes:
        id (str): unique identity
        date_created (datetime): date and time created
        date_modified (datetime): date and time updated
        order_id (str): the id of the order
        quantity_ordered (int): the number of units ordered for that item
        unit_price (float): the price of the each unit of the phone
        total_price (float): the total price for all units of the phone
    """

    order_id = ''
    phone_id = ''
    quantity_ordered = 0
    unit_price = 0.00
    total_price = 0.00
