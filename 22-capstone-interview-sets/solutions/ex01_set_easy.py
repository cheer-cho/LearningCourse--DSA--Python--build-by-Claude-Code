from collections import deque


def top_grossing_movie(sales: list[str]) -> str:
    # Pattern: hash counting (module 03 - hashing). Count occurrences in
    # one pass; track the current best so ties resolve to first-seen
    # without a second pass or a sort.
    # O(n) time, O(n) space.
    if not sales:
        raise ValueError("sales log is empty")
    counts: dict[str, int] = {}
    best = sales[0]
    best_count = 0
    for title in sales:
        counts[title] = counts.get(title, 0) + 1
        if counts[title] > best_count:
            best = title
            best_count = counts[title]
    return best


def two_books_for_slot(thicknesses: list[int], target: int) -> tuple[int, int] | None:
    # Pattern: two pointers, opposite ends (module 04 - two pointers &
    # prefix sums). Sorted input lets us discard one end each step
    # instead of rescanning.
    # O(n) time, O(1) space.
    lo, hi = 0, len(thicknesses) - 1
    while lo < hi:
        total = thicknesses[lo] + thicknesses[hi]
        if total == target:
            return (thicknesses[lo], thicknesses[hi])
        if total < target:
            lo += 1
        else:
            hi -= 1
    return None


def busiest_call_window(calls_per_minute: list[int], k: int) -> int:
    # Pattern: fixed-size sliding window (module 05 - sliding window).
    # Maintain a running sum, add the entering element and drop the
    # leaving one each step instead of resumming the window.
    # O(n) time, O(1) space.
    n = len(calls_per_minute)
    if k < 1 or k > n:
        raise ValueError("k must be between 1 and len(calls_per_minute)")
    window_sum = sum(calls_per_minute[:k])
    best = window_sum
    for i in range(k, n):
        window_sum += calls_per_minute[i] - calls_per_minute[i - k]
        best = max(best, window_sum)
    return best


def is_balanced_formula(expr: str) -> bool:
    # Pattern: stack-based matching (module 06 - stacks & queues). Push
    # openers, pop-and-check on closers; a stack is exactly the right
    # tool for "most recently opened closes first."
    # O(n) time, O(n) space.
    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set(pairs.values())
    stack: list[str] = []
    for ch in expr:
        if ch in openers:
            stack.append(ch)
            continue
        if ch not in pairs:
            continue
        if not stack or stack.pop() != pairs[ch]:
            return False
    return not stack


def shortest_path_to_exit(floor_plan: list[list[int]]) -> int:
    # Pattern: BFS on an implicit grid graph (module 15 - graphs 1).
    # Unweighted grid + "minimum moves" -> BFS guarantees the first
    # time we reach a cell is via a shortest path.
    # O(rows * cols) time, O(rows * cols) space.
    if not floor_plan or not floor_plan[0]:
        return -1
    rows, cols = len(floor_plan), len(floor_plan[0])
    if floor_plan[0][0] == 1 or floor_plan[rows - 1][cols - 1] == 1:
        return -1
    if rows == 1 and cols == 1:
        return 0

    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True
    queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and floor_plan[nr][nc] == 0:
                if nr == rows - 1 and nc == cols - 1:
                    return dist + 1
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return -1


def first_ticket_with_priority(priorities: list[int], target: int) -> int:
    # Pattern: binary search for the leftmost occurrence (module 10 -
    # binary search). Standard lower-bound template, then verify the
    # landing index actually holds the target.
    # O(log n) time, O(1) space.
    lo, hi = 0, len(priorities)
    while lo < hi:
        mid = (lo + hi) // 2
        if priorities[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if lo < len(priorities) and priorities[lo] == target:
        return lo
    return -1
