from collections import OrderedDict

my_dict = {"apple": 3, "zebra": 1, "banana": 2, "cat": 4}

sorted_keys = OrderedDict(sorted(my_dict.items()))
print(sorted_keys)

new_sorted = sorted(my_dict.items())
print(new_sorted)
