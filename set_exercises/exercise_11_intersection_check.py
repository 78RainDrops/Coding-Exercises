set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# if set1.isdisjoint(set2):
#     print("No common elements")
# else:
#     print(set1.intersection(set2))
intersect = set()
for i in set1:
    if i in set2:
        intersect.add(i)

print(intersect)
