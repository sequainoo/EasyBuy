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
