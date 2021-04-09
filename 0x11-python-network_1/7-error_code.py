#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and...
    ...displays the body of the response. """


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    r = requests.get(url)
    rs = r.status_code

    if rs >= 400:
        print("Error code: {}".format(rs))
    else:
        print(r.content.decode('utf-8'))
