string1 = "Jessa"
count = dict()

for i in string1:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

print(count)

# alternative

fre_dict = dict()

for i in string1:
    fre_dict[i] = fre_dict.get(i, 0) + 1

print(fre_dict)
