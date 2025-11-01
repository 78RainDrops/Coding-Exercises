num = 76542
reverse = 0
while num > 0:
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num //= 10

print(f"Reverse: {reverse}")
print("answewr")
