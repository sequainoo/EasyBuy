#!/usr/bin/python3
"""Unit tests for BaseModel"""

import uuid
from unittest import TestCase
from datetime import datetime

from models.base import BaseModel


class TestInitMethod(TestCase):
    """Tests for the BaseModel"""

    def setUp(self):
        """Setup each test case with an instance of BaseModel"""
        self.instance = BaseModel()

    def test_initialization(self):
        """Test that initialization does not fail"""
        self.assertTrue(type(self.instance) is BaseModel)

    def test_initialized_with_id(self):
        """Test BaseModel instance if initialized with id"""
        self.assertTrue(type(self.instance.id) == str)
        self.assertTrue(type(uuid.UUID(self.instance.id)) == uuid.UUID)

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


class TestUpdateMethod(TestCase):
    """Tests the BaseModel update method"""

    def setUp(self):
        """Setup test cases with instance of BaseModel"""
        self.instance = BaseModel()

    def test_invoked_with_no_arg(self):
        """Test that when no argument is passed ValueError is raised"""
        self.assertRaises(TypeError, self.instance.update)

    def test_invoked_with_positional_arg(self):
        """Test BaseModel.update raises TypeError if passed positional arg"""
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
