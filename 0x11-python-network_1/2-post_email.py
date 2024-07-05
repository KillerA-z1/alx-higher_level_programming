#!/usr/bin/python3
"""
    Sends a POST request to the specified URL with the given email data.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email data to send in the request.

    Returns:
        str: The response body of the request.

    Raises:
        urllib.error.URLError: If there is an error with the request.
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    email_data = {'email': sys.argv[2]}
    encoded_data = parse.urlencode(email_data).encode('ascii')
    post_request = request.Request(sys.argv[1], encoded_data)
    with request.urlopen(post_request) as response:
        response_body = response.read()
        print(response_body.decode('utf-8'))
