str1 = "James"

str2 = str1[::2]

print(str2)

# alternative

result = str1[0]
length = len(str1)
mid = int(length / 2)
result += str1[mid]
result += str1[1]
print(f"Result: {result}")
