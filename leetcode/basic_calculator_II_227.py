s = "3+2*2"

"""
Stack Solution
"""


def calculate(s: str) -> int:
    formula = []
    curr_op = "+"
    curr_num = 0
    for i in s + "+":
        if i.isdigit():
            curr_num = (curr_num * 10) + int(i)
            # curr_num = int(i)
        if not i.isdigit() and not i.isspace():
            if curr_op == "+":
                formula.append(curr_num)

            elif curr_op == "-":
                formula.append(-curr_num)

            elif curr_op == "*":
                top = formula.pop()
                formula.append(top * curr_num)

            elif curr_op == "/":
                top = formula.pop()
                formula.append(int(top / curr_num))
            curr_op = i
            curr_num = 0

    res = 0
    while formula:
        res += formula.pop()

    return res


def calculate_const(s: str) -> int:
    i = 0
    curr = prev = res = 0
    curr_op = "+"
    while i < len(s):
        c = s[i]
        if c.isdigit():
            while i < len(s) and s[i].isdigit():
                curr = (curr * 10) + int(s[i])
                i += 1
            i -= 1
            if curr_op == "+":
                res += curr
                prev = curr
            elif curr_op == "-":
                res -= curr
                prev = -curr
            elif curr_op == "*":
                res -= prev
                res += prev * curr
                prev = curr * prev
            elif curr_op == "/":
                res -= prev
                res += int(prev / curr)
                prev = int(prev / curr)
            curr = 0
        elif not c.isspace():
            curr_op = c

        i += 1
    return res


print(f"The result: {calculate(s)}")


# def calculate(s: str) -> int:
#     i = 0
#     formula = []
#     curr_op = "+"
#     curr_num = 0
#     while i < len(s):
#         char = s[i]
#         if char.isdigit():
#             curr_num = (curr_num * 10) + int(char)
#             # curr_num = int(i)
#         if not char.isdigit() and not char.isspace():
#             if curr_op == "+":
#                 formula.append(curr_num)
#
#             elif curr_op == "-":
#                 formula.append(-curr_num)
#
#             elif curr_op == "*":
#                 top = formula.pop()
#                 formula.append(top * curr_num)
#
#             elif curr_op == "/":
#                 top = formula.pop()
#                 formula.append(int(top / curr_num))
#             curr_op = char
#             curr_num = 0
#         i += 1
#
#     res = 0
#     while formula:
#         res += formula.pop()
#
#     return res
