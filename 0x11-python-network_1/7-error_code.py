#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
from sys import argv
import requests


if __name__ == "__main__":

    with requests.get(argv[1]) as req:
        if req.ok:
            print(req.text)
        else:
            print(f"Error code: {req.status_code}")
