import sys
import subprocess

# Get arguments into a list called "args"
args = sys.argv

# Command to run
# cmd = ["ping", "-c", "4", args[1]]
cmd = ["curl", args[1]]

if len(args) == 2:
    stdout, stderr = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print(stdout)
else:
    print("usage (only 2 arguments): python3 curl.py [url/IP address to ping]")