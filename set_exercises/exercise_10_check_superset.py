set1 = {10, 20}
set2 = {10, 20, 30, 40}
is_superset = True
# print(set2.issuperset(set1))
for i in set1:
    if i not in set2:
        is_superset = False
        break
print(is_superset)
