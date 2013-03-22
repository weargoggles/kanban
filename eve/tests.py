"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from eve.models import Type


class TypeTest(TestCase):
    def test_type_name_fetch(self):
        t = Type(id=34, volume=0.01)
        t.fetch_name()
        self.assertEqual(t.name, 'Tritanium')