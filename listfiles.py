#!/usr/local/bin/python3

# WHAT DOES THIS SCRIPT DO?
# list files of a directory

# use subprocess module to interact with the linux CLI
import subprocess

# Represent the list  command in a dictionary
ls_cmd = ["ls", "-a", "/var"]

# Get stdout and stderr as variables
stdout, stderr = subprocess.Popen(ls_cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# view output of each variable above
print("stdout: %s" % stdout)
print("stderr: %s" % stderr)