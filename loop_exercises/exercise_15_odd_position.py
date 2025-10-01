my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(my_list), 2):
    print(my_list[i])

for i in my_list[1::2]:
    print(i, end=" ")
