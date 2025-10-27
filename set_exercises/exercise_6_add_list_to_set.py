sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

# sample_set.update(sample_list)
# print(sample_set)

for item in sample_list:
    sample_set.add(item)

print(sample_set)
