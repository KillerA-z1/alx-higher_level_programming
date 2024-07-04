#!/bin/bash
# Script that sends a POST request to a URL and displays the body of the response
curl -s -X POST "$1" -d email=test@gmail.com -d subject="I will always be here for PLD" 
