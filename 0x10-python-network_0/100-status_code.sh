#!/bin/bash
#sending  a request to a URL passed as an argument
[ -n "$1" ] && { curl -sI "$1" -o /dev/null | awk 'NR=={printf "%s", $2}'; }
