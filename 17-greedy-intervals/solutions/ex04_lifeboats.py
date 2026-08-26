def min_boats(weights: list[int], limit: int) -> int:
    # Pattern: greedy sort + two pointers, pairing extremes. Pairing
    # the heaviest remaining person with the lightest remaining person
    # gives the heaviest its best possible shot at a companion.
    # Complexity: O(n log n) time (the sort), O(1) extra space.
    weights_sorted = sorted(weights)
    lo, hi = 0, len(weights_sorted) - 1
    boats = 0

    while lo <= hi:
        boats += 1
        if lo != hi and weights_sorted[lo] + weights_sorted[hi] <= limit:
            lo += 1
        hi -= 1

    return boats


def assign_kits(kits: list[int], needs: list[int]) -> int:
    # Pattern: assign-cookies greedy — sort both, two pointers. Give
    # the smallest sufficient kit to the smallest unmet need, saving
    # every larger kit for a kid who might actually require that size.
    # Complexity: O(n log n + m log m) time, O(1) extra space.
    kits_sorted = sorted(kits)
    needs_sorted = sorted(needs)
    kit_i = 0
    satisfied = 0

    for need in needs_sorted:
        while kit_i < len(kits_sorted) and kits_sorted[kit_i] < need:
            kit_i += 1
        if kit_i == len(kits_sorted):
            break
        satisfied += 1
        kit_i += 1

    return satisfied
