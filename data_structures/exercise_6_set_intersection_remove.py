first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

new_set = first_set.intersection(second_set)
print(f"Intersection is: {new_set}")

for i in new_set:
    first_set.remove(i)

print(f"First set after removing the common element: {first_set}")
