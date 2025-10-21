list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = list()
for i in list1:
    for j in list2:
        list3.append(i + j)

print(list3)

res = [i + j for i in list1 for j in list2]
print(f"result: {res}")
