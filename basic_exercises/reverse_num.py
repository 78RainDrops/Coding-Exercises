def reverse_int(n, rev=0):
    negative_num = n < 0
    num = abs(n)

    while num != 0:
        rev = rev * 10 + num % 10
        num //= 10
    if negative_num:
        rev = -rev
    
    rev = str(rev)
    rev = " ".join(rev)

    return rev

# short anwer

def rev_int (n):
    rev = 0
    while n > 0:
        digit = n % 10

        n //= 10 

        print(digit, end=" ")

rev_int(123456)
