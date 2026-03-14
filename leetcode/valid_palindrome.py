def isPalindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

    # return alphaNum


s = "Was it a car or a cat I saw?"
print(isPalindrome(s))
