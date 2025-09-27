import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "text.txt")

if os.path.getsize(path) == 0:
    print("File is Empty")
else:
    print("File is not Empty")

with open(path) as f:
    first = f.read(1)
    if not first:
        print(True)
    else:
        print(False)
    file = os.stat(path).st_size
    if file == 0:
        print(True)
    else:
        print(False)
