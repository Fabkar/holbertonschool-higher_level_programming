#!/usr/bin/python3
"""script that takes 2 arguments in order to return
commit, owner and name"""
import requests
from sys import argv
if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    headers = {'Accept': 'application/vnd.github.v3+json'}
    # "https://docs.github.com/en/free-pro-team@latest/rest/reference/users"
    URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = requests.get(URL, headers=headers)
    json = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(json[i].get('sha'),
                  json[i].get('commit').get('author').get('name')))
    except Exception:
        pass
