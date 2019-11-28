#!/usr/local/bin/python3

import subprocess

#if the return code is 0, the command executed successfully!
proc = subprocess.run(["ls","-l"])
#print(f"{proc}")
