name1, name2, name3 = input("Enter name: ").split()

print(f"Name1: {name1}")
print(f"Name2: {name2}")
print(f"Name3: {name3}")

data = []
print("Enter Name: ")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break

for i in range(len(data)):
    print(f"Name{i + 1}: {data[i]}")
