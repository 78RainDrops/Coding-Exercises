s1 = "Abc"
s2 = "Xyz"

fs1 = s1[0]

s3 = s1[0] + s2[-1] + s1[1] + s2[1] + s1[-1] + s2[0]
print(s3)

# alternative

l1 = len(s1)
l2 = len(s2)

result = ""

length = l1 if l1 > l2 else l2

s2 = s2[::-1]

for i in range(length):
    if i < l1:
        result += s1[i]
    if i < l2:
        result += s2[i]

print(result)
