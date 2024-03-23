#!/usr/bin/python3
"""This module is documented."""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    """"This is documented"""
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Data should be in bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))
