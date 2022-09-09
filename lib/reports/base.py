#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from lib.core.decorators import locked
from lib.core.settings import IS_WINDOWS


class FileBaseReport:
    def __init__(self, output_file):
        if IS_WINDOWS:
            from os.path import normpath

            output_file = normpath(output_file)

        self.output_file = output_file

    @locked
    def save(self, entries):
        if not entries:
            return

        with open(self.output_file, "w") as fd:
            fd.writelines(self.generate(entries))
            fd.flush()

    def generate(self, entries):
        raise NotImplementedError
