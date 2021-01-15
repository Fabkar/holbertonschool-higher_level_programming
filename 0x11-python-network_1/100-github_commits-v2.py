#!/usr/bin/python3
"""script that takes 2 arguments in order to return
commit, owner and name"""
import requests
from sys import argv
if __name__ == "__main__":
    owner = argv[1]
    repo = argv[2]
    headers = {'Accept': 'application/vnd.github.v3+json'}
    params = {'state': 'open'}
    # "https://docs.github.com/en/free-pro-team@latest/rest/reference/users"
    URL = f"https://api.github.com/repos/{owner}/{repo}/commits"
    req = requests.get(URL, headers=headers, params=params)
    json = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(json[i].get('sha'),
                  json[i].get('commit').get('author').get('name')))
    except Exception:
        print("None")
