set1 = {10, 20, 30, 40, 50}
to_remove = [10, 20, 30]
# set1.difference_update({10, 20, 30})
set1 = {i for i in set1 if i not in to_remove}
print(set1)
