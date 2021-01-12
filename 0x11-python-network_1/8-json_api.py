#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2 or len(argv) > 2:
        q = ""
    else:
        q = argv[1]
    req = requests.post("http://52bc8ae81d52.87bf5168.hbtn-cod.io:5000/search_user", data={"q": q})
    try:
        req_dict_json = req.json()
        id = req_dict_json.get("id")
        name = req_dict_json.get("name")
        if len(req_dict_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(req_dict_json.get("id"),
                                   req_dict_json.get("name")))
    except Exception:
        print("Not a valid JSON")
