#!/usr/bin/python3
""" Displays the X-Request-Id header variable of a request to a given URL

Usage:
    ./1-hbtn_header.py <URL>
"""


import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) == 2:
        URL = sys.argv[1]

        req = urllib.request.Request(URL)
        with urllib.request.urlopen(req) as res:
            print(dict(res.headers).get("X-Request-Id"))
    else:
        print("Usage: ./1-hbtn_header.py <url>")
