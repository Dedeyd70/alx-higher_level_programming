#!/bin/bash
# takes in a URL and displays all HTTP methods the server
[ -n "$1" ] && curl -sI "$1" | grep -i "Allow:" | awk '{print $2}'
