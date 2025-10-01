list1 = [10, 20, 30, 40, 50]

for i in list1[::-1]:
    print(i)

print()
# alternative

new_list = reversed(list1)

for item in new_list:
    print(item)

print()
# solution 2
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])
