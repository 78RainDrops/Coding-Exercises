from typing import List

# Using Stack


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = sorted([[p, s] for p, s in zip(position, speed)], reverse=True)
    stack = []
    for p, s in pair:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


def carFleet2(target: int, position: List[int], speed: List[int]) -> int:
    n = len(position)
    if n <= 1:
        return n

    idx = list(range(n))

    idx.sort(key=lambda i: position[i], reverse=True)

    last_fleet_time = -1.0
    result = 0

    for i in idx:
        curr_time = (target - position[i]) / speed[i]

        if curr_time > last_fleet_time:
            last_fleet_time = curr_time
            result += 1

    return result


target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]

print(carFleet2(target, position, speed))
