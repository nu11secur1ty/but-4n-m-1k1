#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

from lib.utils.common import lstrip_once


def clean_path(path, keep_queries=False, keep_fragment=False):
    if not keep_fragment:
        path = path.split("#")[0]
    if not keep_queries:
        path = path.split("?")[0]

    return path


def parse_path(value):
    try:
        scheme, url = value.split("//", 1)
        if (
            scheme and (not scheme.endswith(":") or "/" in scheme)
            or url.startswith("/")
        ):
            raise ValueError

        return "/".join(url.split("/")[1:])
    except Exception:
        return lstrip_once(value, "/")
