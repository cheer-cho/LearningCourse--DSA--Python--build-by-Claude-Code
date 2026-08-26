def pair_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    # Pattern: complement lookup. For each value, first check whether
    # target - value was already seen (its index is in the map); only
    # then record the current value. One pass, no revisiting.
    # Time: O(n). Space: O(n).
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return (seen[complement], i)
        seen[value] = i
    return None
