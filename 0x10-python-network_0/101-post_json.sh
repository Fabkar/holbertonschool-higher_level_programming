#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl "$1" -sH "Content-Type: application/json" -d "@$2" 
