def factorial(n):
    if n < 0:
        print("from if")
        raise ValueError("No no no")
    elif n == 0:
        print("from elif")
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


num = 5
fact = factorial(num)
print(fact)
