import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# using math library
def is_prime_optimize(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


start = 25
end = 50
prime = []
for i in range(start, end + 1):
    if is_prime_optimize(i):
        prime.append(i)

for item in prime:
    print(item)
