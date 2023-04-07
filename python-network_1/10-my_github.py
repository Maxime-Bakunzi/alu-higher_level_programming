#!/usr/bin/python3
"""Script that takes your GitHub credentials (username and password) \
and uses the Github API to display your id

Usage:
    ./10-my_github.py <username> <password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <password>")
    else:
        USER_NAME = sys.argv[1]
        PASSWD = sys.argv[2]

        auth = HTTPBasicAuth(USER_NAME, PASSWD)
        r = requests.get("https://api.github.com/user", auth=auth)
        print(r.json().get("id"))
