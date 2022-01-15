#!/usr/bin/python3
"""This script displays the value of X-Request-Id variable"""
import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as reqs:
        print(reqs.info()['X-Request-Id'])
