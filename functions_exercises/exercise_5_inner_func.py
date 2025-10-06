def outer(a, b):
    def inner(a, b):
        return a + b

    sum = 5 + inner(a, b)

    return sum


sum = outer(5, 8)
print(sum)
