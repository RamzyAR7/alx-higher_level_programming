#!/usr/bin/python3
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def main():
    # Extracting URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encoding the email parameter
    data = urlencode({'email': email}).encode('utf-8')

    # Creating a POST request
    req = Request(url, data=data, method='POST')

    # Sending the request and retrieving the response
    with urlopen(req) as response:
        # Reading and printing the response
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main()
