#!/usr/bin/python3
""" a Python script that fetches https://intranet.hbtn.io/status
    using urllib """


import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    utf8 = html.decode('utf-8')
print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(utf8))
