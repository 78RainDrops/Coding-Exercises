rows = 5
num = 1
for i in range(1, rows + 1):
    if i % 2 != 0:  # Odd row: increasing order
        for x in range(num, num + i):
            print(x, end=" ")
        print()  # to diaply next row of number on new line
    else:  # Even row: decreasing order
        for y in range(num + i - 1, num - 1, -1):
            print(y, end=" ")
        print()  # to diaply next row of number on new line
    num += i

num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
