#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
 displays the body of the response (decoded in utf-8)"""


from sys import argv
import urllib.request
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
