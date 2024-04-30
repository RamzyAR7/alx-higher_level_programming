#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv


url = argv[1]

with urlopen(url) as respone:
    if "X-Request-Id" in respone.headers:
        print(respone.headers["X-Request-Id"])
