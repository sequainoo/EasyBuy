#!/usr/bin/python3
"""Base Model"""

import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from utilities import small_helpers


Base = declarative_base()


class AbstractBaseModel:
    """This class implements all common behavior for the other models.

         Attributes:
             id (str): a unique id for the object
             date_created (datetime): date and time created
             date_modified (datetime): data and time modified
    """

    id = Column(String(40), primary_key=True, default=small_helpers.uuid4)
    date_created = Column(DateTime(), default=datetime.now)
    date_modified = Column(DateTime(),
                           default=datetime.now,
                           onupdate=datetime.now)

    def update(self, *args, **kwargs):
        "Updates an instance with key/value pairs provided"
        if args:
            raise TypeError('Invoked with positional argument(s)')
        if not kwargs:
            raise TypeError('Invoked with no keyword argument(s)')

        if 'id' in kwargs:
            kwargs.pop('id')
        if 'date_created' in kwargs:
            kwargs.pop('date_created')
        if 'date_modified' in kwargs:
            kwargs.pop('date_modified')
        self.date_modified = datetime.now()
        self.__dict__.update(kwargs)

    def to_dict(self):
        """Produces a dictionary representation of the instance"""
        temp = self.__dict__.copy()
        dict_ = {}

        for key, value in temp.items():
            if key == 'date_created' or key == 'date_modified':
                value = value.isoformat()
            if not key.startswith('_'):
                dict_[key] = value
        return dict_
    
    def __str__(self):
        """Return string representation of the instance"""
        str_ = '[{}] - ({})'.format(self.__class__.__name__, self.id)
        return str_
