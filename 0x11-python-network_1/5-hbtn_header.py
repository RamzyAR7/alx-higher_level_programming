#!/usr/bin/python3
"""
python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import sys
import requests


def main():
    url = sys.argv[1]

    with requests.get(url) as req:
        if "X-Request-Id" in req.headers:
            print(req.headers["X-Request-Id"])


if __name__ == "__main__":
    main()
