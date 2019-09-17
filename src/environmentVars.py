#!/usr/bin/python3

import os

test = os.environ

print(f"{test}")

print(os.environ["USER"])

#stage = os.getenv("STAGE", default="dev")
stage = os.getenv("STAGE")

print(f"{stage}")

