sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to remove
keys = ["name", "salary"]

for k in keys:
    del sample_dict[k]

print(sample_dict)
# or
for k in keys:
    sample_dict.pop(k)
print(sample_dict)

new_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(new_dict)
