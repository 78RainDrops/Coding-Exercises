
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

odd_list = list(filter(lambda l: l % 2 != 0, list1 + list2))


def longshot(list1, list2):
    merged = []

    for num in list1:
        if num % 2 != 0:
            merged.append(num)
    
    for num in list2:
        if num % 2 != 0:
            merged.append(num)
    
    return merged

print(longshot(list1, list2))
    