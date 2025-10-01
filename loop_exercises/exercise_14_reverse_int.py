num = 76542
reverse = 0
while num > 0:
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num //= 10
    print(f"reminder num:{num}")
    print(f"Reverse num:{reverse}")
    print(f"Current num:{reminder}")
    print()

print(f"Reverse: {reverse}")
print("answewr")
