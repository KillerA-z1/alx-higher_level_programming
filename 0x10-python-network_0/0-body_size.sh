#!/bin/bash
# Displays the size of the body of the response in bytes
# Usage: ./0-body_size.sh <url>

body_size=$(curl -s "$1" | wc -c)
echo "$body_size"