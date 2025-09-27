str_x = "Emma is good developer. Emma is a writer"

s = [word for word in str_x.split() if word == "Emma"]

# alternative
st = str_x.count("Emma")

print(st)