from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = []
    for i, h in enumerate(heights):
        start = i
        while start and stack[-1][1] > h:
            idx, height = stack.pop()
            maxArea = max(maxArea, height * (i - idx))
            start = idx
        stack.append([start, h])

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
