def merge(a: list[int], b: list[int]) -> list[int]:
    # Pattern: linear merge (the merge step of merge sort). Two pointers
    # walk `a` and `b` in lockstep; the smaller head is always the next
    # smallest element overall, so a single pass produces sorted output.
    # Time: O(m + n) — each element read once. Space: O(m + n) for result.
    result: list[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def merge_into(a: list[int], m: int, b: list[int]) -> None:
    # Pattern: back-to-front merge. Writing from the highest index down
    # means every write lands on a slot that's either already-consumed
    # `a` data or an unused placeholder — never data still waiting to be
    # read. That's what makes O(1) extra space possible.
    # Time: O(m + n) — each element read/written once. Space: O(1) extra.
    n = len(b)
    write = m + n - 1
    i = m - 1  # last valid element of a
    j = n - 1  # last element of b
    while i >= 0 and j >= 0:
        if a[i] >= b[j]:
            a[write] = a[i]
            i -= 1
        else:
            a[write] = b[j]
            j -= 1
        write -= 1
    while j >= 0:
        a[write] = b[j]
        j -= 1
        write -= 1
    # any remaining a[:i+1] is already in place — nothing left to do
