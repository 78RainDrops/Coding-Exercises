names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Names':<10} Scores")
print("-" * 17)
for i in range(len(names)):
    print(f"{names[i]:<10} {scores[i]}")

# alternative
print(f"{'Names':<10} {'Scores':<10}")
print("-" * 15)
for name, score in zip(names, scores):
    print(f"{name:<10} {score:<5}")
