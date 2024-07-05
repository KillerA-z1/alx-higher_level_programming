#!/usr/bin/python3
"""
Retrieves the user ID from GitHub API using the provided username and token.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=(username, token))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print("Failed to retrieve user information")
