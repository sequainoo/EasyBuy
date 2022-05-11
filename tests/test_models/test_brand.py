#!/usr/bin/python3
"""Test for phone_brand"""

import unittest

from models.phone_brand import PhoneBrand


class TestPhoneBrand(unittest.TestCase):
    """Tests for PhoneBrand Model"""

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(PhoneBrand.name == '')
