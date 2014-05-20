#!/bin/bash

cat - | grep '\.\.\. [12] \.\.\.' | sed 's/^.*[[:space:]]\([[:digit:]]* \*.*\)$/\1/' | sort -k 10 -d -f -b
