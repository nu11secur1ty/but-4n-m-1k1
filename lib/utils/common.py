#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

from ipaddress import IPv4Network, IPv6Network
from urllib.parse import quote, urljoin

from lib.core.settings import (
    INVALID_CHARS_FOR_WINDOWS_FILENAME, INSECURE_CSV_CHARS,
    INVALID_FILENAME_CHAR_REPLACEMENT, URL_SAFE_CHARS, TEXT_CHARS,
)


def safequote(string_):
    return quote(string_, safe=URL_SAFE_CHARS)


def uniq(array, type_=list):
    return type_(filter(None, dict.fromkeys(array)))


def lstrip_once(string, pattern):
    if string.startswith(pattern):
        return string[len(pattern):]

    return string


def rstrip_once(string, pattern):
    if string.endswith(pattern):
        return string[:-len(pattern)]

    return string


# Some characters are denied in file name by Windows
def get_valid_filename(string):
    for char in INVALID_CHARS_FOR_WINDOWS_FILENAME:
        string = string.replace(char, INVALID_FILENAME_CHAR_REPLACEMENT)

    return string


def human_size(num):
    base = 1024
    for unit in ["B ", "KB", "MB", "GB"]:
        if -base < num < base:
            return f"{num}{unit}"
        num = round(num / base)

    return f"{num}TB"


def is_binary(bytes):
    return bool(bytes.translate(None, TEXT_CHARS))


def is_ipv6(ip):
    return ip.count(":") >= 2


def iprange(subnet):
    network = IPv4Network(subnet)
    if is_ipv6(subnet):
        network = IPv6Network(subnet)

    return [str(ip) for ip in network]


# Prevent CSV injection. Reference: https://www.exploit-db.com/exploits/49370
def escape_csv(text):
    if text.startswith(INSECURE_CSV_CHARS):
        text = "'" + text

    return text.replace('"', '""')


# The browser direction behavior when you click on <a href="bar">link</a>
# (https://website.com/folder/foo -> https://website.com/folder/bar)
def merge_path(url, path):
    parts = url.split("/")
    # Normalize path like the browser does (dealing with ../ and ./)
    path = urljoin("/", path).lstrip("/")
    parts[-1] = path

    return "/".join(parts)
