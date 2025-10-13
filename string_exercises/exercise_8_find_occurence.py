str1 = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"
count = 0
for subs in str1.split(". "):
    if substring.lower() in subs.lower():
        count += 1

print(count)

# shorter alternative
#
temp_str = str1.lower()

count = temp_str.count(substring.lower())
print(count)
