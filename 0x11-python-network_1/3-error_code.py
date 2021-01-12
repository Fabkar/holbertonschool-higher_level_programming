#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""
from sys import argv
import urllib.request as request
import urllib.response as response
import urllib.error as error


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as request:
            print(request.read().decode("utf-8"))
        except error.HTTPError as error:
            print("Error code : {}".format(error.code))
