import time
num = 5

while num > 0:
    print(f"Time remaining: {num} seconds ")
    time.sleep(1)
    num -= 1
print("Time's up!")

msg = "Hello, World"

for c in msg:
    print(c, end="", flush=True)
    time.sleep(2)
