import re

str1 = "PYnative29@#8496"
total = 0
count = 0
for i in str1:
    if i.isdigit():
        total += int(i)
        count += 1

average = total / count

print(f"Average is: {average}")

# alternative
digit_list = [int(num) for num in re.findall(r"\d", str1)]

total = sum(digit_list)
avr = total / len(digit_list)
print(avr)
