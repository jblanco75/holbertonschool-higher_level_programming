#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
 to URL with the letter as a parameter"""


import requests
from sys import argv


if __name__ == '__main__':
    q = argv[1] if len(argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(url, data={'q': q}).json()
        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
