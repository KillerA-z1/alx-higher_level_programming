#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the body of the response or the error code.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.text if response.ok
          else f"Error code: {response.status_code}")
