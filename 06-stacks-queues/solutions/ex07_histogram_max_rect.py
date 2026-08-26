def largest_rectangle(heights: list[int]) -> int:
    # Pattern: monotonic non-decreasing stack of indexes. A sentinel bar
    # of height 0 appended past the end forces every bar still on the
    # stack to be popped and closed out, so no leftover-stack special
    # case is needed after the loop.
    # Complexity: O(n) time, O(n) space.
    stack: list[int] = []
    best = 0
    extended = [*heights, 0]
    for i, h in enumerate(extended):
        while stack and extended[stack[-1]] > h:
            height = extended[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, height * width)
        stack.append(i)
    return best
