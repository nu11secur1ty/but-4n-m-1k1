#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

from email.parser import BytesParser

from lib.core.settings import NEW_LINE
from lib.core.structures import CaseInsensitiveDict


class HeadersParser:
    def __init__(self, headers):
        self.str = self.dict = headers

        if isinstance(headers, str):
            self.dict = self.str_to_dict(headers)
        elif isinstance(headers, dict):
            self.str = self.dict_to_str(headers)
            self.dict = self.str_to_dict(self.str)

        self.headers = CaseInsensitiveDict(self.dict)

    def get(self, key):
        return self.headers[key]

    @staticmethod
    def str_to_dict(headers):
        if not headers:
            return {}

        return dict(BytesParser().parsebytes(headers.encode()))

    @staticmethod
    def dict_to_str(headers):
        if not headers:
            return

        return NEW_LINE.join(f"{key}: {value}" for key, value in headers.items())

    def __iter__(self):
        return iter(self.headers.items())

    def __str__(self):
        return self.str
