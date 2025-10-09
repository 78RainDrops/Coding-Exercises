def apply_operation(func, x, y):
    add = func(x, y)
    return add


def func(x, y):
    return x + y


sum = apply_operation(func, 2, 5)
print(sum)


def sub(x, y):
    return x - y


ans = apply_operation(sub, 5, 21)
print(ans)

