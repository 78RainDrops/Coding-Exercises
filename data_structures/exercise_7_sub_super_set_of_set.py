first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print(f"First set is a subset of second set - {first_set.issubset(second_set)}")

print(f"Second set is a subset of first set - {second_set.issubset(first_set)}")

print(f"First set is a superset of second set - {first_set.issuperset(second_set)}")

print(f"Second set is a superset of first set - {second_set.issuperset(first_set)}")

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print(f"First set {first_set}")
print(f"Second set {second_set}")
