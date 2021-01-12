#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)"""
from sys import argv
import urllib.request as request
import urllib.parse as parse


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    email = parse.urlencode(value).encode("ascii")
    req = request.Request(url, email)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
