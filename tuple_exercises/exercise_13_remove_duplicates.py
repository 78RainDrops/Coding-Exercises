my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple: {my_tuple}")

new_tuple = tuple(set(my_tuple))

print(f"Unique element tuple: {new_tuple}")
