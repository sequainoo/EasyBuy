#!/usr/bin/python3
"""Defines the Phone Model"""

from sqlalchemy import (Column, Integer, Float, String, Text,
                        ForeignKey, CheckConstraint)
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


class Phone(AbstractBaseModel, Base):
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
        images [list]: a list of images related to the phone
    """

    __tablename__ = 'phones'
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    brand_id = Column(String(60),
                      ForeignKey('phone_brands.id'),
                      nullable=False)
    quantity = Column(Integer, default=1)
    price = Column(Float, nullable=False)
    images = relationship('Image',
                          cascade="all, delete-orphan",
                          backref='phone')
    __table_args__ = (
        CheckConstraint('quantity >= 0', name='quantity_check'),
    )
