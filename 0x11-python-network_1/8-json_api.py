#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
from sys import argv
import requests


if __name__ == "__main__":
    val = "" if len(argv) == 1 else argv[1]
    values = {"q": val}
    with requests.post("http://0.0.0.0:5000/search_user", data=values) as res:
        try:
            output = res.json()
            if output:
                print("[{}] {}".format(output.get("id"), output.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
