#!/usr/bin/python3
"""
Creates an object,
from a json file
"""

import json


def load_from_json_file(filename):
    """
    Creates an object,
    from a json file
    """
    with open(filename, "r") as f:
        return json.loads(f.read())
