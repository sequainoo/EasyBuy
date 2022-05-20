#!/usr/bin/python3
"""small helper funtions"""

import uuid


def uuid4():
    """Returns a string representation of uuid4"""
    return str(uuid.uuid4())


def valid_image_name(filename):
    """checks if a filename has an image kind extension"""
    return '.' in filename\
        and filename.rsplit('.', 1)[1].lower()\
        in ['png', 'gif', 'jpeg', 'jpg', 'webp']