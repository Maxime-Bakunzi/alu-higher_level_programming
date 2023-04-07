#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage:
    ./6-post_email.py <url> <email>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <url> <email>")
    else:
        URL = sys.argv[1]

        value = {
                    "email": sys.argv[2]
                }
        r = requests.post(URL, data=value)
        print(r.text)
