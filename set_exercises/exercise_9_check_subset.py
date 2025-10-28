subset_set = {10, 20}
main_set = {10, 20, 30, 40}
is_subset = True
# print(subset_set.issubset(main_set))
for i in subset_set:
    if i not in main_set:
        is_subset = False
        break
print(is_subset)
