import math

while True:
    print("Option: ")
    print("1. Say Hello")
    print("2. Calculate Square")
    print("3. Exit")
    print("Enter your choice: ", end="")
    choice = int(input())

    if choice == 1:
        print("Hello Asshole")
    elif choice == 2:
        num = int(input("Enter num to get square: "))

        # result = math.sqrt(num)
        result = num**0.5

        print(f"Square root of {num}: {result}")
    elif choice == 3:
        break

    else:
        print("Unknown operation")
