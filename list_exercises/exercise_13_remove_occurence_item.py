list1 = [5, 20, 15, 20, 25, 50, 20]


def use_lambda(num_list, val):
    return list(filter(lambda x: x != val, num_list))


def use_for_loop(num_list, val):
    return [i for i in num_list if i != val]


def use_remove(num_list, val):
    while val in num_list:
        num_list.remove(val)
    return num_list


list2 = use_remove(list1, 20)
print(list2)
