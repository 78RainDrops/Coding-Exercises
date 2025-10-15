str1 = "Emma25 is Data scientist50 and AI Expert"
str1 = str1.split()

res_list = []

for i in str1:
    if any(c.isalpha() for c in i) and any(c.isdigit() for c in i):
        res_list.append(i)
print(res_list)
