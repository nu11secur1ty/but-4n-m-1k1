#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from unittest import TestCase
from socket import getaddrinfo

from lib.connection.dns import cache_dns, cached_getaddrinfo
from lib.core.settings import DUMMY_DOMAIN


class TestDNS(TestCase):
    def test_cache_dns(self):
        cache_dns(DUMMY_DOMAIN, 80, "127.0.0.1")
        self.assertEqual(
            cached_getaddrinfo(DUMMY_DOMAIN, 80),
            getaddrinfo("127.0.0.1", 80),
            "Adding DNS cache doesn't work",
        )
