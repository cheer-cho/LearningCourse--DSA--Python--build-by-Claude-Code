def days_until_warmer(temps: list[int]) -> list[int]:
    # Pattern: monotonic (decreasing) stack of indexes still waiting for
    # a warmer day. Each index is pushed once and popped once, so the
    # total work across the whole left-to-right pass is O(n).
    # Complexity: O(n) time, O(n) space.
    result = [0] * len(temps)
    stack: list[int] = []
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result


def next_greater(nums: list[int]) -> list[int]:
    # Pattern: the same monotonic-decreasing stack of indexes, but the
    # value written back is the winning VALUE, not a distance.
    # Complexity: O(n) time, O(n) space.
    result = [-1] * len(nums)
    stack: list[int] = []
    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            result[stack.pop()] = value
        stack.append(i)
    return result
