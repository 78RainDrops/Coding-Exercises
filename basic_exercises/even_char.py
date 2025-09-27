char = "PYnative"

for c in char[::2]:
    print(c)

# alternative 

char = input("Enter a word: ")

size = len(char)

for i in range(0, size - 1, 2):
    print(f"{char[i]}")