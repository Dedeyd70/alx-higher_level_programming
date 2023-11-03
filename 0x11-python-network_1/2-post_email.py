#!/usr/bin/python3
"""A script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response
"""
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urlencode(val)
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as request:
        response = request.read()
        print(response.decode("utf-8"))
