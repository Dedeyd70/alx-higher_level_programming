#!/usr/bin/python3
"""Fetches the content of given URL using urllib"""


import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('-Body Response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- ut8 content:', html.decode('utf-8'))
