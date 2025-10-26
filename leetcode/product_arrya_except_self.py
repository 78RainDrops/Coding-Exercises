def productExceptSelf(nums):
    l_n = len(nums)
    # res = [0] * l_n
    # prefix = [0] * l_n
    # suffix = [0] * l_n
    #
    # prefix[0] = suffix[l_n - 1] = 1
    #
    # for i in range(1, l_n):
    #     prefix[i] = prefix[i - 1] * nums[i - 1]
    # for i in range(l_n - 2, -1, -1):
    #     suffix[i] = suffix[i + 1] * nums[i + 1]
    # for i in range(l_n):
    #     res[i] = prefix[i] * suffix[i]
    #
    # return res
    # Alternative
    res = [1] * l_n
    prefix = 1
    for i in range(l_n):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(l_n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
