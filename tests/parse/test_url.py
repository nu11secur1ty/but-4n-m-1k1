#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from unittest import TestCase

from lib.core.settings import DUMMY_URL
from lib.parse.url import clean_path, parse_path


class TestURLParsers(TestCase):
    def test_clean_path(self):
        self.assertEqual(clean_path("/foo?a=1#a=1"), "/foo")
        self.assertEqual(clean_path("/foo?a=1#a=1", keep_queries=True), "/foo?a=1")

    def test_parse_path(self):
        self.assertEqual(
            parse_path("foo/bar"),
            "foo/bar",
            "Path parser gives unexpected result")
        self.assertEqual(
            parse_path("/foo/bar"),
            "foo/bar",
            "Path parser gives unexpected result")
        self.assertEqual(
            parse_path(f"{DUMMY_URL}foo/bar"),
            "foo/bar",
            "Path parser gives unexpected result",
        )
