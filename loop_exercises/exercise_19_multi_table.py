def multi_table(num):
    for i in range(1, 11):
        print(num * i, end=" ")


for i in range(1, 11):
    num = i
    print("multiplication table of: {}".format(num))
    multi_table(num)
    print()
