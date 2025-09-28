word = input("Enter word: ")
num = int(input("Enter number: "))

right_align = f"{word + str(num):>20}"
# alternative
print(f"{word:>20}{num}")
