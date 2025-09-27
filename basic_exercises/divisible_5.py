def divisible_by_five(list_num):
    divisible = [n for n in list_num if n % 5 == 0 ]
    return divisible

list_num = [10, 20, 33, 46, 55]
print(divisible_by_five(list_num))