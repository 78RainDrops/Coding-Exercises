num = 5
j = 1
for i in range(num, 0, -1):
    print(f"{j} " * i)
    j += 1

# betterz
for i in range(1, num+1):
    for j in range(num - i + 1):
        print(f"{i}", end=" ")
    print()