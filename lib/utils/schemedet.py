#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

import ssl
import socket

from lib.core.settings import SOCKET_TIMEOUT


def detect_scheme(host, port):
    if not port:
        raise ValueError

    s = socket.socket()
    s.settimeout(SOCKET_TIMEOUT)
    conn = ssl.SSLContext().wrap_socket(s)

    try:
        conn.connect((host, port))
        conn.close()
        return "https"
    except Exception:
        return "http"
