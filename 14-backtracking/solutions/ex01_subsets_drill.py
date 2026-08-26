def subsets(nums: list[int]) -> list[list[int]]:
    # Pattern: backtracking, subsets shape (for-loop with a start index;
    # every node visited, not just leaves, is a valid subset).
    # Why: each element is independently in/out, so a for-loop over
    # "which element comes next" naturally enumerates every combination.
    # Complexity: O(2^n) time/output, O(n) extra space (path + recursion).
    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        results.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return results


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # Pattern: backtracking, subsets shape + duplicate skip.
    # Why: sorting groups equal values together; skipping a repeated
    # value at the same tree level (i > start) avoids generating the
    # same subset twice while still allowing [2, 2] one level deeper.
    # Complexity: O(2^n) time, O(n) extra space excluding output.
    nums_sorted = sorted(nums)
    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        results.append(path.copy())
        for i in range(start, len(nums_sorted)):
            if i > start and nums_sorted[i] == nums_sorted[i - 1]:
                continue
            path.append(nums_sorted[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return results
