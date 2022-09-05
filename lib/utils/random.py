#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

import random
import string


def rand_string(n, omit=None):
    seq = string.ascii_lowercase + string.ascii_uppercase + string.digits

    if omit:
        seq = list(set(seq) - set(omit))

    return "".join(random.choice(seq) for _ in range(n))
