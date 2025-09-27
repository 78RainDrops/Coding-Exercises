
def is_string(s_name):
    for c in s_name:
        if c.isdigit():
            return True
    return False

def contains_digit(s_name):
    for c in s_name:
        if '0' <= c <= '9':
            return True
    return False

string_name = input("Enter a string: ")
if contains_digit(string_name):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")    
