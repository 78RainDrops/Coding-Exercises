def dif_type_counter(string):
    digit = 0
    chars = 0
    symbol = 0

    for char in string:
        if char.isdigit():
            digit += 1
        elif char.isalpha():
            chars += 1
        elif not char.isalnum():
            symbol += 1

    print(f"Digit: {digit}")
    print(f"Chars: {chars}")
    print(f"Symbol: {symbol}")


str1 = "P@#yn26at^&i5ve"
dif_type_counter(str1)
