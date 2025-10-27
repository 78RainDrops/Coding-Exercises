set1 = {10, 20, 30}
set2 = {20, 40, 50}

# set1.difference_update(set2)
# print(set1)
set1 = {i for i in set1 if i not in set2}
print(set1)
