#!/usr/bin/python3
"""
This script takes a URL as a command-line argument and sends a GET request to
that URL using the requests library then prints the value of the X-Request-Id
header from the response.
"""

import sys
import requests

if __name__ == "__main__":
    request_url = sys.argv[1]

    response = requests.get(request_url)
    print(response.headers.get("X-Request-Id"))
