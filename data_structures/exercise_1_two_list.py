l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_inx = l1[1::2]
even_inx = l2[::2]

l3 = odd_inx + even_inx

print(l3)
