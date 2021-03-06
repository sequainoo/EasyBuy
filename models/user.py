#!/usr/bin/python3
"""Defines the User model"""

from models.base import AbstractBaseModel


class User(AbstractBaseModel):
    """User model definition.

    Attributes:
        email (str): unique email.
        password (str): user password
        first_name: user first name
        last_name: user last name
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
