#!/usr/bin/python3
"""Defines the Order model"""

from models.base import BaseModel


class Order(BaseModel):
    """Order model definition.

    Attributes:
        order_number (int): an auto incrementing number
        user_id (str): id of use who made the order
        items (list): relationship with order items, list of order items
        paid (bool): indicates an order has been paid
        processed (bool): indicates an order is ready and being shipped
        shipped (bool): indicates an order has been shipped
        number_of_items (int): total number of items ordered
        total_cost (float): total cost of order
    """

    order_number = 0
    user_id = ''
    items = []
    paid = False
    processed = False
    shipped = False
    number_of_items = 0
    total_cost = 0.00
