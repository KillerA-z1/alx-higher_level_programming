#!/bin/bash
# This script sends a GET request to a specified URL and prints the HTTP status code.
curl -so /dev/null -w "%{http_code}" "$1"
