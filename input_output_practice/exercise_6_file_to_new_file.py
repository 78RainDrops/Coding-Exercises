import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "text.txt")
file = open(path, "r")
lines = file.read()


# new = open("new_file.txt", "w")

# for line in lines:
#     new.write(line)

# print(lines)
# print()

# alternative
with open(path, "r") as f:
    # for line in f:
    #     lines = f.readlines()
    lines = f.read()
    print(lines)

new_path = os.path.join(BASE_DIR, "new_file.txt")
with open(new_path, "w") as f:
    for line in lines:
        f.write(line)
