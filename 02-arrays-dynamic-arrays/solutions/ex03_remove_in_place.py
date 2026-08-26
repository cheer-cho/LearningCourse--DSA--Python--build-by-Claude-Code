def remove_value(nums: list[int], val: int) -> int:
    # Pattern: reader/writer two-index sweep. `read` scans every element
    # once; `write` only advances when a survivor is found, so survivors
    # get compacted to the front without a second array.
    # Time: O(n) — one pass. Space: O(1) extra.
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write


def dedupe_sorted(nums: list[int]) -> int:
    # Pattern: reader/writer two-index sweep, specialized for sorted
    # input — a value is a duplicate exactly when it equals the last
    # value the writer kept, so no extra lookup structure is needed.
    # Time: O(n) — one pass. Space: O(1) extra.
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
