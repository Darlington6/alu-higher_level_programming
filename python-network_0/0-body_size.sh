#!/bin/bash
# Display Content-Length
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
