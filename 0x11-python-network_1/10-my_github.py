#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
from sys import argv
import requests
# from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    req = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    try:
        dict_json = req.json()
        print(dict_json["id"])
    except Exception:
        print("None")
