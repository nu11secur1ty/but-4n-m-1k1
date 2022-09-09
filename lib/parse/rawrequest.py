#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from lib.core.exceptions import InvalidRawRequest
from lib.core.logger import logger
from lib.core.settings import NEW_LINE
from lib.parse.headers import HeadersParser
from lib.utils.file import File


def parse_raw(raw_file):
    with File(raw_file) as fd:
        raw_content = fd.read()

    try:
        head = raw_content.split(NEW_LINE * 2)[0].splitlines(0)
        method, path = head[0].split()[:2]
    except Exception as e:
        logger.exception(e)
        raise InvalidRawRequest("The raw request is formatively invalid")

    try:
        headers = HeadersParser(NEW_LINE.join(head[1:]))
        host = headers.get("host").strip()
    except KeyError:
        raise InvalidRawRequest("Can't find the Host header in the raw request")
    except Exception as e:
        logger.exception(e)
        raise InvalidRawRequest("Invalid headers in the raw request")

    try:
        body = raw_content.split(NEW_LINE * 2)[1]
    except IndexError:
        body = None

    return [host + path], method, dict(headers), body
