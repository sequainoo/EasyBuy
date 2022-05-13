#!/usr/bin/python3
"""User Account Model Definition"""

from sqlalchemy import Column, String

from modAccountels.base import AbstractBaseModel, Base


class (AbstractBaseModel, Base):
    """User Account Definition for registered users"""

    __tablename__ = 'accounts'
    id = Column(String(60),
                ForeignKey('customers.id'),
                primary_key=True)
    username = Column(String(60))
    password = Column(String(60), nullable=False)
    customer = relationship('Customer', uselist=False, backref='account')
