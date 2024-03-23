#!/usr/bin/python3
"""This module is documented."""

import urllib.request
import urllib.error
import sys

if __name__ = '__main__':
    """This is documented."""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print("{}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e .code))
    except urllib.error.URLError as e:
        print(e.reason)