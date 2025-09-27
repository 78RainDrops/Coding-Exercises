
num = -12
org_num = num
rev_num = 0

while num > 0:
    reminder = num % 10
    rev_num = (rev_num * 10) + reminder
    num //= 10

print(f'Original Number: {org_num}')
if org_num == rev_num:
    print(f'{org_num} is Palindrome')
else:
    print(f'{org_num} is not Palidrome')