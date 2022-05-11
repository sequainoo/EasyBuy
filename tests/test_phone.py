#!/usr/bin/python3
"""Tests for the Phone Model"""

import unittest
from datetime import datetime

from models.phone import Phone


class TestClassAttributes(unittest.TestCase):
    """Tests For the Phone Model class attributes.
    """

    def test_name(self):
        """Test the name attribute"""
        self.assertTrue(hasattr(Phone, 'name'))
        self.assertTrue(type(getattr(Phone, 'name', None)) is str)
        self.assertTrue(Phone.name == '')

    def test_description(self):
        """Test for description attribute"""
        self.assertTrue(hasattr(Phone, 'description'))
        self.assertTrue(type(getattr(Phone, 'description', None)) is str)
        self.assertTrue(Phone.description == '')

    def test_images(self):
        """Test for images attribute"""
        self.assertTrue(hasattr(Phone, 'images'))
        self.assertTrue(type(getattr(Phone, 'images', None)) is list)
        self.assertTrue(Phone.images == [])

    def test_brand(self):
        """Test for brand attrs"""
        self.assertTrue(hasattr(Phone, 'brand_id'))
        self.assertTrue(type(getattr(Phone, 'brand_id', None)) is str)
        self.assertTrue(Phone.brand_id == '')

    def test_quantity(self):
        """Test for quantity attrs"""
        self.assertTrue(hasattr(Phone, 'quantity'))
        self.assertTrue(type(getattr(Phone, 'quantity', None)) is int)
        self.assertTrue(Phone.quantity == 0)

    def test_price(self):
        """Test for price attrs"""
        self.assertTrue(hasattr(Phone, 'price'))
        self.assertTrue(type(getattr(Phone, 'price', None)) is float)
        self.assertTrue(Phone.price == 0.00)


class TestPhoneInstances(unittest.TestCase):
    """Test instances of Phone."""

    def test_inherited_instance_attr(self):
        """Test that Phone instance has all of base attrs"""
        phone = Phone()
        self.assertTrue(hasattr(phone, 'id')
                        and hasattr(phone, 'date_created')
                        and hasattr(phone, 'date_modified'))

    def test_phone_has_all_initialised_attr(self):
        """Test Phone instance has all initialised attrs"""
        name = 'Itel123'
        description = 'Blue Itel 2013, comes with bluetooth headset'
        phone = Phone(name=name,
                      description=description)
        self.assertTrue(hasattr(phone, 'id')
                        and hasattr(phone, 'date_created')
                        and hasattr(phone, 'date_modified')
                        and getattr(phone, 'name', None) == name
                        and getattr(phone, 'description', None) == description)

    def test_phone_update(self):
        """Test Phone update method"""
        # create instance of phone and capture attributes
        name = 'Iphone 6s plus'
        description = 'Space gray'
        phone = Phone(name=name, description=description)
        id_ = phone.id
        date_created = phone.date_created
        date_modified = phone.date_modified
        
        # update the phone attribute, and compare to confirm they're not same
        phone.update(id='341',
                     date_created=datetime.now(),
                     name="Iphone 7plus",
                     description='Nothing to describe')
        self.assertNotEqual(phone.name, name)
        self.assertNotEqual(phone.description, description)
        self.assertEqual(phone.id, id_)
        self.assertIs(phone.date_created, date_created)
        delta = phone.date_modified - date_modified
        self.assertTrue(delta.microseconds > 0)

        # also confirm the updated attributes have the expected values
        self.assertEqual(phone.name, 'Iphone 7plus')
        self.assertEqual(phone.description, 'Nothing to describe')
