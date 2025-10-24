sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = dict()

for k in keys:
    if k in sample_dict:
        new_dict[k] = sample_dict[k]
# using list comprehension
newDict = {k: sample_dict[k] for k in keys}

# using .update()
new_dict_3 = dict()
for k in keys:
    new_dict_3.update({k: sample_dict[k]})


print(new_dict_3)
