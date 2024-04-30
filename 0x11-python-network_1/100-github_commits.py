#!/usr/bin/python3
"""Python script that takes 2 arguments in order and print first 10 commits"""
from sys import argv
import requests


if __name__ == "__main__":
    with requests.get("https://api.github.com/repos/{}/{}/commits?per_page=10"
                      .format(argv[2], argv[1])) as res:
        for commit in res.json():
            print("{}: {}"
                  .format(commit.get("sha"),
                          commit.get("commit").get("author").get("name")))
