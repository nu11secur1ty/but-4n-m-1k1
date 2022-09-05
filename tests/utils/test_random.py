#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

from unittest import TestCase

from lib.utils.random import rand_string


class TestRandom(TestCase):
    def test_rand_string(self):
        test_omit = "abcde"
        self.assertEqual(len(rand_string(9)), 9, "Incorrect random string length")
        for x, y in zip(rand_string(5, omit=test_omit), test_omit):
            self.assertNotEqual(x, y, "Random string's characters are not distinct from omit")
