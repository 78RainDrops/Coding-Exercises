import re
import string

str1 = "/*Jon is @developer & musician"

res = re.sub(r"[^\w\s]", "", str1)
print(res)

res = str1.translate(str.maketrans("", "", string.punctuation))
print(res)
