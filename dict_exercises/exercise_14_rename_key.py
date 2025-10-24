sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york",
}

# loc = sample_dict.pop("city")
# sample_dict["location"] = loc
# or
sample_dict["locations"] = sample_dict.pop("city")
print(sample_dict)
