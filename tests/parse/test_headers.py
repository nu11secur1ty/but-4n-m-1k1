#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

from unittest import TestCase

from lib.parse.headers import HeadersParser


class TestHeadersParser(TestCase):
    def test_str_to_dict(self):
        test_str = """
Header1: foo
Header2:bar
Header3:
        """
        expected_dict = {"Header1": "foo", "Header2": "bar", "Header3": ""}
        self.assertEqual(HeadersParser.str_to_dict(test_str.strip()), expected_dict, "Raw headers to dictionary converter gives unexpected result")

    def test_dict_to_str(self):
        test_dict = {"foo": "bar"}
        expected_str = "foo: bar"
        self.assertEqual(HeadersParser.dict_to_str(test_dict), expected_str, "Headers dictionary to raw converter gives unexpected result")
