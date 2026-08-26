# Scenario: a point-of-sale system wants to know if any two DIFFERENT
# items in a cart sum exactly to a promotional target price. Walk the
# 5-step framework end to end: brute force first, then the pattern
# that removes the bottleneck.
# Concepts: complement lookup with a hash set.
# Run: uv run pytest 01-big-o-foundations -k ex05


def has_pair_brute(nums: list[int], target: int) -> bool:
    """Return True if two DIFFERENT positions i != j exist with
    nums[i] + nums[j] == target. A single element can't pair with
    itself, but equal VALUES at different positions count.

    has_pair_brute([2, 7, 11, 15], 9) -> True   (2 + 7)
    has_pair_brute([3, 3], 6) -> True            (two different 3's)
    has_pair_brute([5], 10) -> False             (only one position)

    --- The 5-step framework, walked for this exercise ---
    1. Understand: input is a list and a target sum; output is a bool;
       edge cases are an empty list and a list with one element.
    2. Brute force (THIS function): check every pair of positions.
    3. Bottleneck: for each element, we re-scan the rest of the list
       looking for its complement -- repeated work.
    4. Pattern (see has_pair_fast): remember every value seen so far in
       a set; for each new element, check if its complement is already
       in the set. One pass, no re-scanning.
    5. Verify: empty list, one element, duplicate values, negative
       numbers, target of 0.

    Target complexity: O(n^2) time, O(1) extra space. This is step 2,
    not the answer -- has_pair_fast is where the pattern lands.
    """
    raise NotImplementedError


def has_pair_fast(nums: list[int], target: int) -> bool:
    """Same contract as has_pair_brute, using the complement-lookup
    pattern from step 4 above.

    has_pair_fast([2, 7, 11, 15], 9) -> True
    has_pair_fast([3, 3], 6) -> True
    has_pair_fast([5], 10) -> False

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError
