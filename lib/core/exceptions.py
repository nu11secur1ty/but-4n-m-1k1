#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022


class FailedDependenciesInstallation(Exception):
    pass


class InvalidRawRequest(Exception):
    pass


class InvalidURLException(Exception):
    pass


class RequestException(Exception):
    pass


class SkipTargetInterrupt(Exception):
    pass


class QuitInterrupt(Exception):
    pass


class UnpicklingError(Exception):
    pass
