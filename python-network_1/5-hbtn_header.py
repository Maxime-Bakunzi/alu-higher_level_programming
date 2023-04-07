#!/usr/bin/python3
"""Displays the value of the variable X-Request-Id in the response header

Usage:
    ./5-hbtn_header.py <url>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <url>")
    else:
        URL = sys.argv[1]

        r = requests.get(URL)
        print(r.headers.get("X-Request-Id"))
