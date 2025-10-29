nums = [1, 1, 1, 2, 2, 3]
k = 2


def topKFrequent(nums, k):
    count = dict()
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        # if num in count:
        #     count[num] += 1
        # else:
        #     count[num] = 1
        count[num] = count.get(num, 0) + 1

    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
    # return freq


print(topKFrequent(nums, k))
