counter = 0

number = 75869

while True:
    if number == 0:
        break
    number //= 10
    counter += 1

print(counter)
