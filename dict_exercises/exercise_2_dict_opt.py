my_dict = {"name": "Alice", "age": 35, "city": "New York", "profession": "Doctor"}

print(f"Original: {my_dict}")
del my_dict["profession"]
print(f"Remove Profession: {my_dict}")

for k, v in my_dict.items():
    print(f"{k}: {v}")

key = "age"
print(f"Does {key} exist?", end=" ")

if key in my_dict:
    print(True)
else:
    print(False)
