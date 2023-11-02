#!/bin/bash
# takes in a URL and displays all HTTP methods the server
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cur -c 2- | rev | cut -c 2 - | rev
