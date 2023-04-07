#!/usr/bin/python3
""" Sends a request to a given URL and displays the response body.

Usage:
    ./3-error_code.py <URL>
    - Handles HTTP errors.
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <url>")
    else:
        URL = sys.argv[1]

        req = urllib.request.Request(URL)
        try:
            with urllib.request.urlopen(req) as res:
                print(res.read().decode("ascii"))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
