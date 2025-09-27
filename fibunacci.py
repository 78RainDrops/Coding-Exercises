def sum_of_curr_prev_num(n):
    previous_num = 0
    for i in range(n):
        sum = i + previous_num
        print(f"Current Number: {i}, Previous Number: {previous_num} Sum: {sum} ")
        previous_num = i

sum_of_curr_prev_num(10)