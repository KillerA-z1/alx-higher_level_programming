#!/usr/bin/python3

"""
This script sends a GET request to https://alx-intranet.hbtn.io/status
and prints the response body along with its type and utf-8 content.
"""

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        utf8_content = body.decode('utf-8')
        print("\t- utf8 content: {}".format(utf8_content))
