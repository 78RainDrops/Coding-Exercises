def calculation(a, b) -> tuple:
    sum = a + b
    diff = a - b

    return sum, diff


sum, dif = calculation(40, 10)
print(sum, dif)
print(sum, ", ", dif)
print(f"{sum}, {dif}")
print("{}, {}".format(sum, dif))
print("%s, %s" % (sum, dif))
