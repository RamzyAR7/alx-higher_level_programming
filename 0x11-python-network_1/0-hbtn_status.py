#!/usr/bin/python3
from urllib import request


with request.urlopen("https://alx-intranet.hbtn.io/status") as respone:
    site = respone.read()

print("Body response:")
print("\t- type:", type(site))
print("\t- content:", site)
print("\t- utf8 content:", site.decode('utf-8'))
