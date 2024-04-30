#!/usr/bin/python3
"""
python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib import request


def main():
    url = sys.argv[1]

    with request.urlopen(url) as respone:
        if "X-Request-Id" in respone.headers:
            print(respone.headers["X-Request-Id"])


if __name__ == "__main__":
    main()
