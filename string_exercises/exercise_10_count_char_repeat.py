str1 = "Apple"

occur = {}

for i in str1:
    if i in occur:
        occur[i] += 1
    else:
        occur[i] = 1

print(occur)

# alternative
occur2 = {}
for i in str1:
    count = str1.count(i)
    occur2[i] = count

print(f"occurence: {occur2}")
