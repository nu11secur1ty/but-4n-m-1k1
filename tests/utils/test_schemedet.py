#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from unittest import TestCase

from lib.core.settings import DUMMY_DOMAIN
from lib.utils.schemedet import detect_scheme


class TestSchemedet(TestCase):
    def test_detect_scheme(self):
        self.assertEqual(detect_scheme(DUMMY_DOMAIN, 443), "https", "Incorrect scheme detected")
        self.assertEqual(detect_scheme(DUMMY_DOMAIN, 80), "http", "Incorrect scheme detected")
        self.assertEqual(detect_scheme(DUMMY_DOMAIN, 1234), "http", "Incorrect scheme detected")
