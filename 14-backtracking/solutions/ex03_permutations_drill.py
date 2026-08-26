def permutations(nums: list[int]) -> list[list[int]]:
    # Pattern: backtracking, permutations shape (a `used` tracker since
    # every not-yet-placed element is a candidate at every position).
    # Why: order matters, so we can't use a start index — each position
    # scans the whole list, skipping only what's already placed.
    # Complexity: O(n! * n) time/output, O(n) extra space.
    results: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            results.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return results


def permutations_unique(nums: list[int]) -> list[list[int]]:
    # Pattern: backtracking, permutations shape + duplicate skip via a
    # value->count map (not a used-index array, which can't tell two
    # equal values apart at the same position).
    # Why: trying each DISTINCT value at most once per position, and
    # decrementing/restoring its count, skips duplicate permutations
    # without an index-based same-level check.
    # Complexity: O(n! * n) time worst case, O(n) extra space.
    counts: dict[int, int] = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1

    results: list[list[int]] = []
    path: list[int] = []

    def backtrack() -> None:
        if len(path) == len(nums):
            results.append(path.copy())
            return
        for value, count in counts.items():
            if count == 0:
                continue
            counts[value] -= 1
            path.append(value)
            backtrack()
            path.pop()
            counts[value] += 1

    backtrack()
    return results
