def remove_chars(word, n):
    remaining = []
    for i in word[n:]:
        remaining.append(i)
    
    remaining = ''.join(remaining)
    return remaining

def alternative_solution(word,n):
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars('PYnative', 4))

print(alternative_solution("pynative", 2))