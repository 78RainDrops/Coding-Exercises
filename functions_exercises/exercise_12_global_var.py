global_var = 20


def func():
    global global_var
    global_var = 10

    print(global_var)


func()

print(global_var)
