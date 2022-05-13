#!/usr/bin/python3
"""Defines the Customer model"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


class Customer(AbstractBaseModel, Base):
    """Customer model definition.

    Attributes:
        email (str): unique email.
        password (str): Customer password
        first_name: Customer first name
        last_name: Customer last name
    """

    __tablename__ = 'customers'
    email = Column(String(60), unique=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    payments = relationship('Payment',
                            cascade='all, delete-orphan',
                            backref='cutomer')
    addresses = relationship("Address",
                             cascade='all, delete-orphan')
