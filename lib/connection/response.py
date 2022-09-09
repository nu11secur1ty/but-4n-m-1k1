#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from lib.core.settings import (
    DEFAULT_ENCODING, ITER_CHUNK_SIZE,
    MAX_RESPONSE_SIZE, UNKNOWN,
)
from lib.parse.url import clean_path, parse_path
from lib.utils.common import is_binary


class Response:
    def __init__(self, response):
        self.url = response.url
        self.full_path = parse_path(response.url)
        self.path = clean_path(self.full_path)
        self.status = response.status_code
        self.headers = response.headers
        self.redirect = self.headers.get("location") or ""
        self.history = [res.url for res in response.history]
        self.content = ""
        self.body = b""

        for chunk in response.iter_content(chunk_size=ITER_CHUNK_SIZE):
            self.body += chunk

            if len(self.body) >= MAX_RESPONSE_SIZE or (
                "content-length" in self.headers and is_binary(self.body)
            ):
                break

        if not is_binary(self.body):
            self.content = self.body.decode(
                response.encoding or DEFAULT_ENCODING, errors="ignore"
            )

    @property
    def type(self):
        if "content-type" in self.headers:
            return self.headers.get("content-type").split(";")[0]

        return UNKNOWN

    @property
    def length(self):
        try:
            return int(self.headers.get("content-length"))
        except TypeError:
            return len(self.body)

    def __hash__(self):
        return hash(self.body)

    def __eq__(self, other):
        return (self.status, self.body, self.redirect) == (
            other.status,
            other.body,
            other.redirect,
        )
