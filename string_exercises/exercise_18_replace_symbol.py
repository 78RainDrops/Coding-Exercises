import string

str1 = "/*Jon is @developer & musician!!"

for i in string.punctuation:
    str1 = str1.replace(i, "#")

print(str1)
