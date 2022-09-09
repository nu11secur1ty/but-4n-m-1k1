#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from unittest import TestCase

from lib.utils.common import merge_path, uniq, get_valid_filename


class TestCommonUtils(TestCase):
    def test_uniq(self):
        self.assertEqual(uniq(["foo", "bar", "foo"]), ["foo", "bar"], "The result is not unique or in wrong order")

    def test_get_valid_filename(self):
        self.assertEqual(get_valid_filename("http://example.com:80/foobar"), "http___example.com_80_foobar", "Invalid filename for Windows")

    def test_merge_path(self):
        self.assertEqual(merge_path("http://example.com/foo", "bar"), "http://example.com/bar")
        self.assertEqual(merge_path("http://example.com/folder/", "foo/../bar/./"), "http://example.com/folder/bar/")
