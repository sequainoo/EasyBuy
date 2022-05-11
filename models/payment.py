#!/usr/bin/python3
"""Defines the Payment model"""

from models.base import BaseModel


class Payment(BaseModel):
    """Payment model definition.

    Attributes:
        order_id (str): id of order that payment is for.
        user_id (str): if of the user from which payment was made
        amount_paid (float): Amount paid
    """

    user_id = ''
    order_id = ''
    amount_paid = 0.00
