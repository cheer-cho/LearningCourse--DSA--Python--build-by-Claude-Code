# Scenario: merge k already-sorted server logs into one sorted
# timeline. Pattern: k-way merge with a heap holding "the next
# candidate from each list."
# Run: uv run pytest 12-heaps-priority-queues -k ex07


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Merge `lists` (each individually sorted ascending, may be
    empty, `lists` itself may be empty) into one sorted ascending list.

    merge_k_sorted([[1, 4, 7], [2, 5], [3, 6, 8, 9]])
        -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_k_sorted([[], [1], []]) -> [1]
    merge_k_sorted([]) -> []

    Seed a heap with the FIRST element of every non-empty list, keyed
    as `(value, list_index, element_index)` -- the index fields exist
    purely to break ties (heaps compare tuples element by element, and
    two equal values would otherwise fall through to comparing lists,
    which crashes). Repeatedly pop the smallest, append it to the
    result, and if that list has a next element, push it.

    Compare this to merging lists two-at-a-time, pairwise
    (`merge(merge(a, b), c)`, ...): that revisits early elements once
    per merge round, `O(n * k)` total for `n` total elements across
    `k` lists. The heap does each of the `n` elements' work once,
    paying only `O(log k)` per pop for the heap upkeep.

    Target complexity: O(n log k) time, where n is the total element
    count across all lists; O(k) extra space for the heap.
    """
    raise NotImplementedError
