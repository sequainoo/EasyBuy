#!/usr/bin/python3
"""Base Model"""

import uuid
from datetime import datetime


class BaseModel:
    """This class implements all common behavior for the other models.
    """
    def __init__(self, *args, **kwargs):
        """Initializes the instance with kwargs.

        Args:
            args : (null)
            kwargs: (null).

        Attributes:
            id (str): a unique id for the object
            date_created (datetime): date and time created
            date_modified (datetime): data and time modified
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        
        if 'id' in kwargs:
            if type(self.date_created) is not datetime\
                or type(self.date_modified) is not datetime:
                raise ValueError('date must be a datetime instance')
        else:
            self.id = str(uuid.uuid4())
            self.date_created = datetime.now()
            self.date_modified = self.date_created

    def update(self, *args, **kwargs):
        "Updates an instance with key/value pairs provided"
        if args:
            raise TypeError('Invoked with positional argument(s)')
        if not kwargs:
            raise TypeError('Invoked with no keyword argument(s)')
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
            dict_[key] = value
        return dict_
    
    def __str__(self):
        """Return string representation of the instance"""
        str_ = '[{}] - ({})'.format(self.__class__.__name__, self.id)
        return str_
