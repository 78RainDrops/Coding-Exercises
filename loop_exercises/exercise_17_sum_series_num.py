num = 2
terms = 5
current_term = num
sum = num

for i in range(terms - 1):
    current_term = (current_term * 10) + num
    print(current_term)
    sum += current_term

print(sum)
# alternative
terms = 5
num = 2
sum = 0
for i in range(0, terms):
    print(num, end="+")
    sum += num
    num = num * 10 + 2
print(f"Sum: {sum}")
