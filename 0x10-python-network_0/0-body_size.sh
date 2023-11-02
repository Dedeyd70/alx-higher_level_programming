#!/bin/bash
#Getting the byte size
curl -s "$1" | wc -c
