tuple1 = (("a", 23), ("b", 37), ("c", 11), ("d", 29))

tuple1 = list(tuple1)

tuple1 = tuple(sorted(tuple1, key=lambda i: i[1]))
print(tuple1)
