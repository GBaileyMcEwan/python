#!/usr/bin/python3

import time

theTime = time.localtime()
print(theTime)
print(f"{theTime.tm_hour}:{theTime.tm_min}:{theTime.tm_hour}")
