#!/usr/bin/python3
"""This script displays the value of X-Request-Id variable"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as reqs:
    print(reqs.info()['X-Request-Id'])
