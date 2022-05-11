#!/usr/bin/python3
"""Unit tests for AbstractBaseModel"""

import uuid
import unittest
from datetime import datetime

from models.base import AbstractBaseModel


class TestInitMethod(unittest.TestCase):
    """Tests for the AbstractBaseModel"""

    def setUp(self):
        """Setup each test case with an instance of AbstractBaseModel"""
        self.instance = AbstractBaseModel()

    def test_initialization(self):
        """Test that initialization does not fail"""
        self.assertTrue(type(self.instance) is AbstractBaseModel)

    def test_initialized_with_id(self):
        """Test AbstractBaseModel instance is initialized with id"""
        self.assertTrue(type(self.instance.id) == str)
        self.assertTrue(type(uuid.UUID(self.instance.id)) == uuid.UUID)

    def test_initialised_with_existing_data(self):
        """Test that instance can be created from existing record"""
        # existing record info
        id_ = str(uuid.uuid4())
        date_created = datetime.now()
        instance = AbstractBaseModel(id=id_,
                                     date_created=date_created,
                                     date_modified=date_created)
        self.assertEqual(instance.id, id_)
        self.assertIs(instance.date_created, date_created)
        self.assertIs(instance.date_modified, date_created)

    def test_date_created(self):
        """Test date_created to be equivalent to now"""
        now = datetime.now()
        # get time difference between created_date and now
        # should be less than 3 seconds: is some gap though
        delta = now - self.instance.date_created
        self.assertTrue(delta.seconds <= 3)

    def test_date_modified(self):
        """Test date modified to be equivalent to date_created"""
        self.assertIs(self.instance.date_modified, self.instance.date_created)


class TestUpdateMethod(unittest.TestCase):
    """Tests the AbstractBaseModel update method"""

    def setUp(self):
        """Setup test cases with instance of AbstractBaseModel"""
        self.instance = AbstractBaseModel()

    def test_invoked_with_no_arg(self):
        """Test that when no argument is passed ValueError is raised"""
        self.assertRaises(TypeError, self.instance.update)

    def test_invoked_with_positional_arg(self):
        """Test AbstractBaseModel.update raises TypeError if passed positional arg"""
        self.assertRaises(TypeError, self.instance.update, 'Apple')

    def test_date_created_unchanged(self):
        """test date_created remains the same after an update is made"""
        date = self.instance.date_created
        self.instance.update(name='iphone')
        self.assertIs(date, self.instance.date_created)

    def test_date_modified_changed(self):
        """Test that date_modified is changed after an update"""
        date = self.instance.date_modified
        self.instance.update(name='Apple')
        self.assertIsNot(self.instance.date_modified, date)

    def test_update_with_one_value(self):
        """Test that value is available on instance after update"""
        self.instance.update(name='Apple')
        self.assertEqual(self.instance.name, 'Apple')

    def test_update_with_two_values(self):
        """Test that values is available on instance after update"""
        self.instance.update(name='Apple', phone='iphone 5s')
        self.assertEqual(self.instance.name, 'Apple')
        self.assertEqual(self.instance.phone, 'iphone 5s')


class TestToDict(unittest.TestCase):
    """Tests for AbstractBaseModel to_dict method."""
    
    def setUp(self):
        """Setup tests"""
        self.instance = AbstractBaseModel(name='Apple')

    def test_output_is_dict(self):
        """Test that output is a dictionary object"""
        self.assertIs(type(self.instance.to_dict()), dict)

    def test_has_all_keys_and_values(self):
        """Test to_dict produce the expected key/value pairs
        Makes sure length is as expected along with key/values
        """
        expect = {
                'id': self.instance.id,
                'date_created': self.instance.date_created.isoformat(),
                'date_modified': self.instance.date_modified.isoformat(),
                'name': self.instance.name}
        self.assertDictEqual(self.instance.to_dict(), expect)


class TestStr(unittest.TestCase):
    """Tests for __str__"""

    def test___str__(self):
        """Test return of __str__
        
        format:
            [type] - (id)
        """
        instance = AbstractBaseModel()
        expected = "[{:s}] - ({:s})".format(instance.__class__.__name__,
                                            instance.id)
        
        self.assertEqual(str(instance), expected)
