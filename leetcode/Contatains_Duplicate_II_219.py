nums = [1, 2, 3, 1, 2, 3]
k = 2


def containsNearbyDuplicate(nums, k):
    seen = dict()
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False


print(containsNearbyDuplicate(nums, k))
