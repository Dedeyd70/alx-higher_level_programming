#!/bin/bash
# takes in a URL and displays all HTTP methods the server accept
[ -n "$1" ] && curl -sX DELETE "$1"
