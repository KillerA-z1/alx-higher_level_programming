#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response decoded in utf-8, handling HTTP errors appropriately.
"""
from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            response_content = response.read()
            print(response_content.decode('utf-8'))
    except error.HTTPError as http_error:
        print('Error code:', http_error.code)
