def longest_consecutive(nums):
    res = 0
    numSet = set(nums)
    longest = 0

    # for num in nums:
    #     count, curr = 0, num
    #     while curr in numSet:
    #         count += 1
    #         curr += 1
    #     res = max(res, count)
    # return res

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            print(f"Outer length: {length}, outer number: {num}")
            while (num + length) in numSet:
                length += 1
                print(f"inner length: {length}, inner number: {num}")

            longest = max(length, longest)
    return longest


nums = [2, 20, 4, 10, 3, 4, 5]
print(longest_consecutive(nums))
