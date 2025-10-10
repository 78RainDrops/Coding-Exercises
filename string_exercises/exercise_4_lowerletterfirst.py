str1 = "PyNaTive"
front = ""
last = ""
for char in str1:
    if char.islower():
        front += char
    else:
        last += char

str2 = front + last
print(str2)

# alternative

lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

str2 = "".join(lower + upper)
print(str2)
