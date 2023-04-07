#!/usr/bin/python3
""" Sends a POST request to a given URL with a given email.

Usage:
    ./2-post_email.py <url> <email>
    - Display the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <url> <email>")
    else:
        URL = sys.argv[1]
        value = {
                    "email": sys.argv[2]
                }
        data = urllib.parse.urlencode(value).encode("ascii")

        req = urllib.request.Request(URL, data)
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
