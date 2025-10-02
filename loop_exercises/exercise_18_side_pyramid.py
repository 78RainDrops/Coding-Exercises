num = 5
for i in range(num):
    print("* " * i)
for j in range(num, 0, -1):
    print("* " * j)

# alternative
row = 5
for i in range(0, row):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\r")
for i in range(row, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print("\r")
