#!/usr/bin/python3
"""script that takes in a letter and sends a POST request"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    response = requests.post(url, payload)
    try:
        user = response.json()
        if user == {}:
            print("No result")
        else:
            print("[{}] {}".format(user["id"], user["name"]))
    except ValueError:
        print("Not a valid JSON")
