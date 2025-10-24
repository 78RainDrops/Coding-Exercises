from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        print(count)
        res[tuple(count)].append(s)

    return res.values()


print(list(group_anagrams(strs)))
