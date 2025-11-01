tuple1 = (50, 10, 60, 70, 50)

cnt = tuple1.count(50)
print(cnt)

cnt = 0

for i in tuple1:
    if i == 50:
        cnt += 1
print(cnt)
