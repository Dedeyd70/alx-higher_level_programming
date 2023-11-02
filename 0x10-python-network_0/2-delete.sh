#!/bin/bash
#sends a DELETE request to the URL passed as the first argument 
[ -n "$1" ] && curl -sX DELETE "$1"
