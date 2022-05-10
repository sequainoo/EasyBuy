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
        self.id = str(uuid.uuid4())
        self.date_created = datetime.now()
        self.date_modified = self.date_created
