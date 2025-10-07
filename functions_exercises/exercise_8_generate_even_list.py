even_list = []

for num in range(4, 30):
    if num % 2 == 0:
        even_list.append(num)

print(even_list)

even = [num for num in range(4, 30) if num % 2 == 0]
print(even)


even = [num for num in range(4, 30, 2)]
print(even)
