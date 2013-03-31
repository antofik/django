from __future__ import unicode_literals

from django.db.backends.util import format_number
from django.test import TestCase
from decimal import Decimal


class BackendUtilTests(TestCase):

    def test_format_number(self):
        """
        Tests that ensures in correct number formatting
        """
        equal = lambda value, string, d, p: self.assertEqual(format_number(Decimal(value), d, p),string)
        
        equal('0', '0.000', 12, 3)
        equal('0', '0.00000000', 12, 8)
        equal('1', '1.000000000', 12, 9)
        equal('0.00000000', '0.00000000', 12, 8)
        equal('0.000000004', '0.00000000', 12, 8)
        equal('0.000000008', '0.00000001', 12, 8)
        equal('0.000000000000000000999', '0.00000000', 10, 8)
        equal('0.1234567890', '0.1234567890', 12, 10)
        equal('0.1234567890', '0.123456789', 12, 9)
        equal('0.1234567890', '0.12345679', 12, 8)
        equal('0.1234567890', '0.1234568', 12, 7)
        equal('0.1234567890', '0.12346', 12, 5)
        equal('0.1234567890', '0.123', 12, 3)
        equal('0.1234567890', '0.1', 12, 1)
        equal('0.1234567890', '0', 12, 0)
