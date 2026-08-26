# Scenario: a ship's crew loads passengers onto lifeboats (2 per boat,
# weight-limited) and a camp assigns gift kits to kids by size.
# Pattern: greedy sort + two pointers (pair extremes / satisfy-most).
# Run: uv run pytest 17-greedy-intervals -k ex04


def min_boats(weights: list[int], limit: int) -> int:
    """Each lifeboat holds AT MOST 2 people and a total weight of AT
    MOST `limit`. Every person in `weights` individually fits alone in
    a boat (`weights[i] <= limit`). Return the minimum number of boats
    needed to carry everyone.

    Sort weights, then two pointers from both ends: always try to pair
    the heaviest remaining person with the lightest remaining person.
    If they fit together, both board one boat; if not, the heaviest
    goes alone (the lightest can only pair even worse with anyone
    heavier, so pairing them was never going to work). Greedy proof
    sketch: pairing the heaviest with the LIGHTEST available person
    gives the heaviest its best possible chance at a companion — if
    even the lightest doesn't fit with it, no one does.

    min_boats([1, 2], 3) -> 1
    min_boats([3, 2, 2, 1], 3) -> 3
    min_boats([5, 1, 4, 2], 6) -> 2

    Target: O(n log n) time (the sort), O(1) extra space beyond it.
    """
    raise NotImplementedError


def assign_kits(kits: list[int], needs: list[int]) -> int:
    """`kits[i]` is the size of gift kit `i`; `needs[j]` is the
    smallest kit size that satisfies kid `j` (a kit satisfies a kid if
    `kit_size >= need`). Each kit can be given to at most one kid.
    Return the maximum number of kids that can be satisfied.

    Assign-cookies shape: sort both lists ascending, then walk two
    pointers. If the smallest remaining kit satisfies the smallest
    remaining unsatisfied need, use it (advance both pointers);
    otherwise that kit is too small for anyone still waiting, so skip
    it (advance only the kit pointer). Greedy proof sketch: giving the
    smallest sufficient kit to the smallest need saves every larger
    kit for a kid who might actually need that size.

    assign_kits([1, 2, 3], [1, 2]) -> 2
    assign_kits([1, 2], [1, 2, 3]) -> 2
    assign_kits([], [1, 2]) -> 0

    Target: O(n log n + m log m) time, O(1) extra space beyond sorting.
    """
    raise NotImplementedError
