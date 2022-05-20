#!/usr/bin/python3
"""Defines the PhoneBrand model"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import AbstractBaseModel, Base


class PhoneBrand(AbstractBaseModel, Base):
    """Phone Brand Model"""
    
    __tablename__ = 'phone_brands'
    name = Column(String(60), nullable=False, unique=True)
    phones = relationship('Phone', backref='brand')
