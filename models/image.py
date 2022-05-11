#!/usr/bin/python3
"""Defines the Image model"""

from models.base import BaseModel


class Image(BaseModel):
    """image model definition.

    Attributes:
        phone_id (str): id of the phone with that image.
        alt_text (str): alternate text for the image
        url (str): image url
    """

    phone_id = ''
    alt_text = ''
    url = ''
