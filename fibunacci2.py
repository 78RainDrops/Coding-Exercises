def fibunacci(n):
    if n <= 0:
        return "No negative number"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fib_series = [0,1]
  
    for i in range(2, n):
        next_num = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_num)
    
    return fib_series

fibs = fibunacci(15)
print("Fibunacci Sequence")
for fib in fibs:
    print(fib , end=" ")