def trap(height):
    res = 0

    # for i in range(len(height)):
    #     maxL = maxR = height[i]
    #
    #     for j in range(i):
    #         maxL = max(maxL, height[j])
    #
    #     for j in range(i + 1, len(height)):
    #         maxR = max(maxR, height[j])
    #
    #     res += min(maxR, maxL) - height[i]
    l, r = 0, len(height) - 1

    maxL, maxR = height[l], height[r]

    while l < r:
        if maxL < maxR:
            l += 1
            maxL = max(maxL, height[l])

            res += maxL - height[l]
        else:
            r -= 1
            maxR = max(maxR, height[r])
            res += maxR - height[r]

    return res


height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
print(trap(height))
# trap(height)
