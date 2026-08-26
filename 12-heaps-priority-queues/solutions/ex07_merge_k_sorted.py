import heapq


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    # Pattern: k-way merge. Heap holds one "frontier" candidate per
    # list, keyed (value, list_index, element_index) -- the indices
    # break ties so equal values never fall back to comparing lists.
    # Time: O(n log k), n = total elements, k = number of lists.
    # Space: O(k) for the heap, O(n) for the result.
    heap: list[tuple[int, int, int]] = []
    for list_idx, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], list_idx, 0))

    result: list[int] = []
    while heap:
        value, list_idx, elem_idx = heapq.heappop(heap)
        result.append(value)
        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result
