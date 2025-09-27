str_x = 125
rev = str(str_x)[::-1]
# rev =  ''.join(rev)
print(rev)

print(f"original number {str_x}")
if str_x == int(rev):
    print(f"Yes, {str_x} is a palindrome")
else:
    print(f"{str_x} not a palindrome")

# calculation approach 

def palindrome(n):
    org = n
    reversed_num = 0
    while n > 0:
        reminder = n % 10
        reversed_num = (reversed_num * 10) + reminder
        n //= 10
    
    print(f"original number {org}")
    if org == reversed_num:
        print(f"Yes, {org} is a palindrome")
    else:
        print(f"{org} not a palindrome")

palindrome(121)
palindrome(125)