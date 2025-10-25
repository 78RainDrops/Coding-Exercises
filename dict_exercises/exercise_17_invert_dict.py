original_dict1 = {"a": 1, "b": 2, "c": 3}

new_dict = dict()

for k, v in original_dict1.items():
    new_dict[v] = k

print(new_dict)
