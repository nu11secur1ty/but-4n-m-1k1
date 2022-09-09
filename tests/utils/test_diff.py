#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from unittest import TestCase

from lib.utils.diff import DynamicContentParser, generate_matching_regex


class TestDiff(TestCase):
    def test_generate_matching_regex(self):
        self.assertEqual(generate_matching_regex("add.php", "abc.php"), "^a.*\\.php$", "Matching regex isn't correct")

    def test_dynamic_content_parser(self):
        self.assertEqual(DynamicContentParser("a b c", "a b d")._static_patterns, ["  a", "  b"], "Static patterns are not right")
        self.assertTrue(DynamicContentParser("a b c", "a b d").compare_to("a b ef"))
