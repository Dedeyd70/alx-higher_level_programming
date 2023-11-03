#!/usr/bin/python3
"""Fetches the content of given URL using urllib"""


import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(f"-Body Response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- ut8 content: {html.decode('utf-8')}")
