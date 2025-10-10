s1 = "America"
s2 = "Japan"


l1 = len(s1)
l2 = len(s2)

m1 = int(l1 / 2)
m2 = int(l2 / 2)

s3 = s1[0] + s2[0]
s3 += s1[m1] + s2[m2]
s3 += s1[-1] + s2[-1]

print(s3)

# alternative


def mix_string(s1, s2):
    f_char = s1[0] + s2[0]
    s_char = s1[int(len(s1) / 2)] + s2[int(len(s2) / 2)]
    l_char = s1[-1] + s2[-1]

    return f_char + s_char + l_char


print(mix_string(s1, s2))
