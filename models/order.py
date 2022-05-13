#!/usr/bin/python3
"""Defines the Order model"""

from sqlalchemy import Column, String, Boolean, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from models.base import AbstractBaseModel, Base


class Order(AbstractBaseModel, Base):
    """Order model definition.

    Attributes:
        order_number (int): an auto incrementing number
        customer_id (str): id of use who made the order
        items (list): relationship with order items, list of order items
        paid (bool): indicates an order has been paid
        processed (bool): indicates an order is ready and being shipped
        shipped (bool): indicates an order has been shipped
        number_of_items (int): total number of items ordered
        total_cost (float): total cost of order
    """

    __tablename__ = 'orders'
    order_number = Column(Integer, autoincrement=True)
    customer_id = Column(String(60), ForeignKey('customers.id'))
    paid = Column(Boolean, default=False)
    processed = Column(Boolean, default=False)
    shipped = Column(Boolean, default=False)
    shipping_date = Column(DateTime, nullable=True)
    number_of_items = Column(Integer, nullable=False)
    total_cost = Column(Float, nullable=False)
    customer = relationship('Customer',
                            backref=backref('orders', cascade='all, delete-orphan'),
                            uselist=False)
    items = relationship('OrderItem', backref='order')
    payment = relationship('Payment', backref='order', uselist=False)
