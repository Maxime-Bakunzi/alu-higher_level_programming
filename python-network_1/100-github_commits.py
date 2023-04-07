#!/usr/bin/python3
"""Lists 10 commits from recent to oldest of the repository "rails"

Usage:
    ./100-github_commits.py <repository name> <owner name>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <ownwer name>")
    else:
        REPO_NAME = sys.argv[1]
        OWNER_NAME = sys.argv[2]

        url = "https://api.github.com/repos/{}/{}/commits".format(
                REPO_NAME, OWNER_NAME)

        r = requests.get(url)
        commits = r.json()
        try:
            for count in range(10):
                print("{}: {}".format(
                    commits[count].get("sha"),
                    commits[count].get("commit").get("author").get("name")))
        except IndexError:
            pass
