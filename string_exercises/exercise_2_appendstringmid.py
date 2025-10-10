def append_middle(s1, s2):
    l = len(s1)
    m = int(l / 2)
    s3 = s1[:m] + s2 + s1[m:]
    return s3


s1 = "Ault"
s2 = "Kelly"


s3 = append_middle(s1, s2)
print(s3)
