# s = ")"
s = "()[]{}"


def valid_parentheses(s: str) -> bool:
    stk = []
    pair = {")": "(", "]": "[", "}": "{"}
    print(s)
    print("Keys: ", pair.keys())
    print("values: ", pair.values())
    for i in s:
        print(i)
        if i in pair.keys():
            print("True for Key", i)
            if len(stk) == 0 or stk.pop() != pair[i]:
                return False
        elif i in pair.values():
            print("true for value", i)
            stk.append(i)

    return True if len(stk) == 0 else False

    # for i in s:
    #     if i in pair:
    #         if s_stk or s_stk[-1] == pair[i]:
    #             s_stk.pop()
    #         else:
    #             return False
    #     else:
    #         s_stk.append(i)
    #
    # return not s_stk

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
