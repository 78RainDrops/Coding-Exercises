
def capitalize_words(text):    
    new_word = text.split()
    capitalize_words = [word.capitalize() for word in new_word]
    return " ".join(capitalize_words)

words = "pynative.com is for python lovers"
capitalize_string = capitalize_words(words)
print(capitalize_string)