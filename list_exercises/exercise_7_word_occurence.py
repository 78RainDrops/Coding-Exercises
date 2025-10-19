sports = ["Cricket", "Football", "Hockey", "Football", "Tennis"]

word = "Football"
cnt = 0
for i in sports:
    if i == word:
        cnt += 1

print(f"Football appears {cnt} times")

occur = sports.count(word)

print(f"Football appears {occur} times")
