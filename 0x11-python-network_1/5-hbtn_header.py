#!/usr/bin/python3
"""Response header value(sends a request to the URL and displays the value
of the variable X-Request-Id in the response heade"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    # Dictionary headers information
    print(req.headers.get("X-Request-Id"))
