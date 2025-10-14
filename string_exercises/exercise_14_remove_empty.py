str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]


filtered_list = list(filter(lambda s: s is not None and s != "", str_list))
print(filtered_list)

list2 = list(filter(None, str_list))
print(f"List 2: {list2}")
