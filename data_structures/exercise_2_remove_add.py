list1 = [54, 44, 27, 79, 91, 41]

rem_item = list1.pop(4)

print(f"List after removing index 4: {list1}")

list1.insert(2, rem_item)

print(f"List after adding element at index 2: {list1}")

list1.append(rem_item)

print(f"List affter adding element at last: {list1}")
