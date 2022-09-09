#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from lib.core.settings import NEW_LINE
from lib.reports.base import FileBaseReport


class SimpleReport(FileBaseReport):
    def generate(self, entries):
        return NEW_LINE.join(entry.url for entry in entries)
