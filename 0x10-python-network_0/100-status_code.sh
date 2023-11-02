#!/bin/bash
#that sends a request to a URL passed as an argument
[ -n "$1" ] && { curl -s -o /dev/null -w "%{http_code}" "$1"; }
