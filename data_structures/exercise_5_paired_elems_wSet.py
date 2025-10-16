first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

third_set = set()

for i in range(len(first_list)):
    temp = first_list[i], second_list[i]
    third_set.add(temp)
print(third_set)

# or

t_set = set(zip(first_list, second_list))

print(t_set)
