list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

set1 = set(list1)
set2 = set(list2)
common = set1 & set2
common2 = set1.intersection(set2)
print(common)
print(common2)
