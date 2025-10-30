tuple1 = (11, 22)
tuple2 = (99, 88)
print(f"tuple 1: {tuple1}")
print(f"tuple 2: {tuple2}")

# temp = tuple1
# tuple1 = tuple2
# tuple2 = temp
tuple1, tuple2 = tuple2, tuple1

print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")
