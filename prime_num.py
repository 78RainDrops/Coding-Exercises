import math
num = 20
is_prime = True
def is_prime(num):
    if num <= 1:
        return False

    return all([num % i != 0 for i in range( 2, int(num ** 0.5)+1)])

prime = []
for num in range(2, num+1):
    if is_prime(num):
        prime.append(num)

print(f"All prime numbers from 1 to {num}: {[n for n in prime]}" )


for num in range(0, len(prime), 2):
    print(prime[num], end=" ")