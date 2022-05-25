#!/usr/bin/python3
"""Defines the Payment model"""

from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


class Payment(AbstractBaseModel, Base):
    """Payment model definition.

    Attributes:
        order_id (str): id of order that payment is for.
        user_id (str): if of the user from which payment was made
        amount_paid (float): Amount paid
        order (obj): order object related to a payment
        customer (obj): customer object related to payment
    """

    __tablename__ = 'payments'
    order_id = Column(String(60),
                      ForeignKey('orders.id'),
                      unique=True)
    customer_id = Column(String(60),
                         ForeignKey('customers.id'))
    amount_paid = Column(Float, nullable=False)
    refund_amount = Column(Float, default=0.00)