set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# set1.symmetric_difference_update(set2)
# print(set1)
diff_set = set()
for i in set1:
    if i not in set2:
        diff_set.add(i)
for i in set2:
    if i not in set1:
        diff_set.add(i)
print(diff_set)

new_set = set1 ^ set2
print(new_set)
