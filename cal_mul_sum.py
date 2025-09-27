# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))

# multiply = num_1 * num_2

# if multiply <= 1000:
#     print(multiply)
# else:
#     print(num_1 + num_2)
# more clean solution

def multiply_or_sum(num_1, num_2):
    product = num_1 * num_2

    if product <= 1000:
        return product
    else:
        return num_1 + num_2

result = multiply_or_sum(20, 30)

print(result)
