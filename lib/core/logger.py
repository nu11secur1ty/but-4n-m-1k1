#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

import logging
from logging.handlers import RotatingFileHandler

from lib.core.data import options


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.disabled = True


def enable_logging():
    logger.disabled = False
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    handler = RotatingFileHandler(options["log_file"], maxBytes=options["log_file_size"])
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
