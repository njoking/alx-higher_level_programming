#!/bin/bash
# Sends a GET request to a URL and displays the body of the response only for a 200 status code
curl -s -L "$1" -o /dev/null -w "%{http_code}" | grep -q "200" && curl -s -L "$1"
