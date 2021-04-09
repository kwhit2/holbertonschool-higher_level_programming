#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and...
    ...displays the body of the response (decoded in utf-8). """


import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]

    request = urllib.request.Request(url)

    try:
        urllib.request.urlopen(request)
        with urllib.request.urlopen(request) as response:
            content = response.read()
            utf8 = content.decode('utf-8')
        print(utf8)
    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.status))
