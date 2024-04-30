#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
