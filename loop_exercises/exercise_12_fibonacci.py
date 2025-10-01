fib = [0, 1]

curr = fib[0]
next = fib[1]

for i in range(2, 10, 1):
    res = curr + next
    fib.append(res)
    curr = next
    next = res

print(fib)

# alternative
num1, num2 = 0, 1
for i in range(10):
    print(num1, end=" ")
    res = num1 + num2
    num1 = num2
    num2 = res
