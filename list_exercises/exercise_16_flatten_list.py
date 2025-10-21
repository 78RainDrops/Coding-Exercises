list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
flatten_list = list()
for i in list_of_lists:
    for j in i:
        flatten_list.append(j)
print(flatten_list)

# list comprehension alternative

flatten_list2 = [j for i in list_of_lists for j in i]
print(flatten_list2)
