subset_set = {10, 20}
main_set = {10, 20, 30, 40}
count = 0
# print(subset_set.issubset(main_set))
for i in main_set:
    if count == len(subset_set):
        print(True)
    if i in subset_set:
        count += 1
