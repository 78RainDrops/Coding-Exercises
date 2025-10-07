x = [4, 6, 8, 24, 12, 2]

print(max(x))
m_n = 0
for i in x:
    if m_n < i:
        m_n = i

print(m_n)
