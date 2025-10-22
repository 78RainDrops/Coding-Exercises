keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
new_dict = dict()
for k, v in zip(keys, values):
    new_dict[k] = v

print(new_dict)

# alternative
new_dict2 = dict(zip(keys, values))
print(new_dict2)
