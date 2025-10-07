def display_student(name, age):
    print(name, age)


display_student("Emma", 26)

# a new pointer to the function
show_student = display_student
show_student("dana", 25)
