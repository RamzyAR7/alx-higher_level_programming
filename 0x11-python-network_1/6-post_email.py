#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
,and finally displays the body of the response.
"""
import sys
import requests


def main():
    # Extracting URL and email from command-line arguments
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    # Sending the request and retrieving the response
    with requests.post(url, data=value) as req:
        # Reading and printing the response
        print(req.text)


if __name__ == "__main__":
    main()
