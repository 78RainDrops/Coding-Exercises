def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res


# result = []
#
# for i in range(len(temperatures)):
#     num_days = 0
#     for j in range(i, len(temperatures)):
#         if temperatures[i] < temperatures[j]:
#             num_days = j - i
#             result.append(num_days)
#             break
#     if num_days == 0:
#         result.append(0)
#
# print(result)


# temperatures = [30, 38, 30, 36, 35, 40, 28]
temperatures = [22, 21, 20]

print(dailyTemperatures(temperatures))

# dailyTemperatures(temperatures)
