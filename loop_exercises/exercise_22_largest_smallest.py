def large_small(num) -> tuple:
    if num == 0:
        return 0, 0

    str_num = str(abs(num))
    largest_num = int(str_num[0])
    smallest_num = int(str_num[0])

    for digit in str_num[1:]:
        int_digit = int(digit)
        if largest_num < int_digit:
            largest_num = int_digit
        if smallest_num > int_digit:
            smallest_num = int_digit

    return smallest_num, largest_num


num1 = 9876543210
num2 = -5082
smallest_num, largest_num = large_small(num1)
if smallest_num is not None:
    print(f"Largest Number: {largest_num}")
    print(f"Smallest Number: {smallest_num}")

smallest_num, largest_num = large_small(num2)
if smallest_num is not None:
    print(f"Largest Number: {largest_num}")
    print(f"Smallest Number: {smallest_num}")
