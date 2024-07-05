#!/usr/bin/python3
"""
Sends a POST request to the specified URL with the given email data
and request to the passed URL with the email then displays the body
of the response.
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
