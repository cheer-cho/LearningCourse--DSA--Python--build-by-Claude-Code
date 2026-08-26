def max_container(heights: list[int]) -> int:
    # Pattern: two pointers, opposite ends, exchange argument. The
    # shorter wall is always the bottleneck, so only moving it can ever
    # improve the answer -- see the docstring for the full argument.
    # O(n) time (each pointer moves at most n times total), O(1) space.
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        if heights[left] < heights[right]:
            best = max(best, heights[left] * width)
            left += 1
        else:
            best = max(best, heights[right] * width)
            right -= 1
    return best
