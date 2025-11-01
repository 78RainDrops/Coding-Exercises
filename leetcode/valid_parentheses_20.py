s = ")"


def valid_parentheses(s: str) -> bool:
    s_stk = []
    pair = {")": "(", "]": "[", "}": "{"}

    for i in s:
        if i in pair:
            if s_stk or s_stk[-1] == pair[i]:
                s_stk.pop()
            else:
                return False
        else:
            s_stk.append(i)

    return not s_stk

    # for i in s:
    #     if i in ("{", "[", "("):
    #         s_stk.append(i)
    #     else:
    #         if not s_stk:
    #             return False
    #         top = s_stk[-1]
    #
    #         if top == "{" and i == "}":
    #             s_stk.pop()
    #         elif top == "[" and i == "]":
    #             s_stk.pop()
    #         elif top == "(" and i == ")":
    #             s_stk.pop()
    #         else:
    #             return False
    # return True if not s_stk else False


print(valid_parentheses(s))
