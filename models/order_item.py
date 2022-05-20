#!/usr/bin/python3
"""Defines the OrderItem model"""

from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


class OrderItem(AbstractBaseModel, Base):
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

    __tablename__ = 'order_items'
    order_id = Column(String(60),
                      ForeignKey('orders.id'),
                      nullable=False)
    phone_id = Column(String(60),
                      ForeignKey('phones.id'),
                      nullable=False)
    quantity_ordered = Column(Integer, nullable=False)
    unit_cost = Column(Float, nullable=False)
    total_cost = Column(Float, nullable=False)
    phone = relationship('Phone', backref='orders')
