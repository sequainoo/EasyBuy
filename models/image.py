#!/usr/bin/python3
"""Defines the Image model"""

from sqlalchemy import (Column, String, Boolean, Float,
                        Integer, ForeignKey, Text)
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


class Image(AbstractBaseModel, Base):
    """image model definition.

    Attributes:
        phone_id (str): id of the phone with that image.
        alt_text (str): alternate text for the image
        url (str): image url
    """

    __tablename__ = 'images'
    phone_id = Column(String(60),
                      ForeignKey('phones.id'),
                      nullable=False)
    alt_text = Column(String(100), nullable=False)
    url = Column(String(100), nullable=False, unique=True)
