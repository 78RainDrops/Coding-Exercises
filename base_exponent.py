
def exponent(base, exp):
    ans = base ** exp
    return ans

base = 5
exp = 4
ans = exponent(base, exp)
print(f"{base} raises to the power of {exp}: {ans}")

for i in range(exp):
    print(f"{base}", end=" ")
    if i < exp-1:
        print("*", end=' ')
    else:
        print(f"= {ans}")