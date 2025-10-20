nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]

for i in nested_list:
    for j in i:
        if j == 55:
            print(j)
        else:
            print("Not 55")
