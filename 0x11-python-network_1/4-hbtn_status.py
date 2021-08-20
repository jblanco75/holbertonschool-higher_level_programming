#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""


import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
