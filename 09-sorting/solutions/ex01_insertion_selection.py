def selection_sort(nums: list[int]) -> list[int]:
    # Pattern: elementary O(n^2) sort — repeatedly select the minimum
    # of the unsorted remainder and place it at the front. Applies here
    # as the simplest possible baseline (fewest writes, no adaptivity).
    # Complexity: O(n^2) time always, O(n) space for the copy.
    result = nums[:]
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    return result


def insertion_sort(nums: list[int], counter: list[int] | None = None) -> list[int]:
    # Pattern: elementary adaptive sort — grow a sorted prefix one
    # element at a time, shifting bigger already-placed elements right.
    # Applies here because it's O(n) on nearly-sorted input, unlike
    # selection sort. Complexity: O(n) best (nearly sorted), O(n^2)
    # worst (reverse sorted); O(n) space for the copy.
    result = nums[:]
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            if counter is not None:
                counter[0] += 1
            j -= 1
        result[j + 1] = current
    return result
