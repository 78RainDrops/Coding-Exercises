numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

get_first = numbers_y[0]
get_last = numbers_y[-1]

if get_first == get_last:
    print(True)
else:
    print(False)

# alternative

def first_last_num(list_num):
    get_first = list_num[0]
    get_last = list_num[-1]

    if get_first == get_last:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print(first_last_num(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print(first_last_num(numbers_y))
