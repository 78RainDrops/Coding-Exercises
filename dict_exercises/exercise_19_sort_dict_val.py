my_dict = {"Jessa": 3, "Kelly": 1, "Jon": 2, "Kerry": 4, "Joy": 1}

new_dict = sorted(my_dict.items(), key=lambda x: x[1])
print(new_dict)
