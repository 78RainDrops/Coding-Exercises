t1: tuple[int, int, int] = (1, 2, 3)
t2: tuple[int, int, int] = (1, 2, 4)

if t1 > t2:
    print(f"{t1} is greater than {t2}")
elif t1 < t2:
    print(f"{t2} is greater than {t1}")
else:
    print(f"{t1} is equal to {t2}")

# for i, j in zip(t1, t2):
#     if i > j:
#         print(f"{t1} is greater than {t2}")
#         break
#     elif j > i:
#         print(f"{t2} is greater than {t1}")
#         break
# else:
#     print(f"{t1} is equal to {t2}")
