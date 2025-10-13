def present(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True


s1 = "Yn"
s2 = "PYnative"


# s1 = "Ynf"
# s2 = "PYnative"

print(present(s1, s2))
