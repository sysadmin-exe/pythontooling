#!/usr/local/bin/python3

# WHAT DOES THIS SCRIPT DO? 
# This script will check if the provided filename or dirname is present

import os.path
import sys
import subprocess

# Get arguments into a list called "args"
args = sys.argv

if len(args) == 2:
    if os.path.isfile(args[1]):
        print("The File ", args[1], " does exist on this system", sep=" ")
    elif os.path.isdir(args[1]):
        print("The Directory ", args[1], " does exist on this system", sep=" ")
    else:
        print("the requested file or directory does not exist on this system")
else:
    print("usage (only 2 arguments): EXAMPLE => python3 ispresent.py [directory or file absolute path]")