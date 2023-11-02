#!/bin/bash
#that sends a request to a URL passed as an argument
[ -n "$1" ] && { curl -sI "$1" | grep -i "HTTP" | cut -d " " -f 2; }
