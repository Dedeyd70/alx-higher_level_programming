#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge."""
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)
    dcommits = response.json()

    try:
        for d in range(10):
            print("{}: {}".format(
                dcommits[d].get("sha"),
                dcommits[d].get("commit").get("author").get("name")))
    except IndexError:
        pass
