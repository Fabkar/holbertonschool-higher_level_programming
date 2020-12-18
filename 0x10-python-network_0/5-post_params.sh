#!/bin/bash
#takes in a URL, sends a POST request to the passed URL.
curl -sX POST -d "hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
