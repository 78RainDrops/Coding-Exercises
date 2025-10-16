sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

sample_dict = {}

for i in sample_list:
    if i in sample_dict:
        sample_dict[i] += 1
    else:
        sample_dict[i] = 1

print(f"Printing count of each item: {sample_dict}")
