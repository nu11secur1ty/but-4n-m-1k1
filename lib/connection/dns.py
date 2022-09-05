#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

from socket import getaddrinfo

_dns_cache = {}


def cache_dns(domain, port, addr):
    _dns_cache[domain, port] = getaddrinfo(addr, port)


def cached_getaddrinfo(*args, **kwargs):
    """
    Replacement for socket.getaddrinfo, they are the same but this function
    does cache the answer to improve the performance
    """

    host, port = args[:2]
    if (host, port) not in _dns_cache:
        _dns_cache[host, port] = getaddrinfo(*args, **kwargs)

    return _dns_cache[host, port]
