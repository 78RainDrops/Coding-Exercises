def twoSum(nums, target):
    seen = dict()

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            print(seen[diff], i)
        seen[num] = i


nums = [2, 7, 11, 15]
target = 9

twoSum(nums, target)
