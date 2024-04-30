#!/usr/bin/python3
"""
python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
from urllib.request import urlopen
from sys import argv


url = argv[1]

with urlopen(url) as respone:
    if "X-Request-Id" in respone.headers:
        print(respone.headers["X-Request-Id"])
