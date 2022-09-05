#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

import difflib
import re

from lib.core.settings import MAX_MATCH_RATIO


class DynamicContentParser:
    def __init__(self, content1, content2):
        self._static_patterns = None
        self._differ = difflib.Differ()
        self._is_static = content1 == content2
        self._base_content = content1

        if not self._is_static:
            self._static_patterns = self.get_static_patterns(
                self._differ.compare(content1.split(), content2.split())
            )

    def compare_to(self, content):
        """
        DynamicContentParser.compare_to() workflow

          1. Check if the wildcard response is static or not, if yes, compare 2 responses
          2. If it's not static, get static patterns (splitting by space) in both responses
            and check if they match
          3. In some rare cases, checking static patterns fails, so make a final confirmation
            if the similarity ratio of 2 responses is not high enough to prove they are the same
        """

        if self._is_static:
            return content == self._base_content

        diff = self._differ.compare(self._base_content.split(), content.split())
        static_patterns_are_matched = self._static_patterns == self.get_static_patterns(diff)
        match_ratio = difflib.SequenceMatcher(None, self._base_content, content).ratio()
        return static_patterns_are_matched or match_ratio > MAX_MATCH_RATIO

    @staticmethod
    def get_static_patterns(patterns):
        # difflib.Differ.compare returns something like below:
        # ["  str1", "- str2", "+ str3", "  str4"]
        #
        # Get only stable patterns in the contents
        return [pattern for pattern in patterns if pattern.startswith("  ")]


def generate_matching_regex(string1, string2):
    start = "^"
    end = "$"

    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            start += ".*"
            break

        start += re.escape(char1)

    if start.endswith(".*"):
        for char1, char2 in zip(string1[::-1], string2[::-1]):
            if char1 != char2:
                break

            end = re.escape(char1) + end

    return start + end
