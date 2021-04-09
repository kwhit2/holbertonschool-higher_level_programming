#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST request to..
    ..the passed URL with the email as a parameter, and displays the body of...
    ...the response (decoded in utf-8) """


import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    params = urllib.parse.urlencode({'email': email})
    params = params.encode('ascii')
    request = urllib.request.Request(url, params)

    with urllib.request.urlopen(request) as response:
        content = response.read()
        utf8 = content.decode('utf-8')
    print(utf8)
