a = (1,)
b = (2, [1, 2, 3])
d = {}

try:
    d[a] = "f"
    print(d[a], end="")
except Excpetion:
    print("b", end="")
try:
    d[b] = "g"
    print(d[b], end="")
except Exception:
    print("a", end="")
