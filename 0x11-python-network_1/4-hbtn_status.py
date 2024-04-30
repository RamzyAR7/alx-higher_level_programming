#!/usr/bin/python3
import requests

with requests.get("https://alx-intranet.hbtn.io/status") as req:
    site = req.text

print("Body response:")
print("\t- type:", type(site))
print("\t- content:", site)
