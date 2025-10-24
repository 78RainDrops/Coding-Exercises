s = "aacc"
t = "ccac"


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    print(f"S: {countS}")
    print(f"T: {countT}")
    return countS == countT


print(isAnagram(s, t))
