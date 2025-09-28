import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "text.txt")
x = 0
with open(path, "r") as f:
    lines = f.readlines()[3].strip()
    print(lines)
