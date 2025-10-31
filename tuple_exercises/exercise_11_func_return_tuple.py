def get_min_max(numbers):
    max_num = max(numbers)
    min_num = min(numbers)

    return min_num, max_num


my_numbers = [10, 5, 20, 2, 15]
min_max_value = get_min_max(my_numbers)
print(my_numbers)
print(min_max_value)
