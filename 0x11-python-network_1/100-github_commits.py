#!/usr/bin/python3
""" script that takes 2 arguments in order to solve this challenge."""
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    URL = "https://api.github.com/repos/{}/{}commits".format(owner, repo_name)
    response = requests.get(url)
    commits = response.json()
    try:
        for d in range(10)
        print("{}: {}".format(
            commits[d].get("sha"),
            commits[d].get("commit").get("author").get("name")))
    except IndexError:
        pass
