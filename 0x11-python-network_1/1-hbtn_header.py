#!/usr/bin/python3
"""
python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib.request import urlopen


url = sys.argv[1]

with urlopen(url) as respone:
    head = respone.headers.get('X-Request-Id')
    print(head)
