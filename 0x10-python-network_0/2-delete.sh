#!/bin/bash
# Script that sends a DELETE request to URL passed as a first argument and displays the body of the response
curl -sX DELETE "$1"
