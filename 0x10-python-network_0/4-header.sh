#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL
[ -n "$1" ] && curl -sH "X-School-User-Id: 98" "$1"
