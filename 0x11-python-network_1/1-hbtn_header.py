#!/usr/bin/python3
"""
    Sends a request to a URL and prints the value of the 'X-Request-Id' header.

    Args:
        sys.argv[1] (str): The URL to send the request to.

    Returns:
        None
"""

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        response_headers = response.info()
        print(response_headers.get('X-Request-Id'))
