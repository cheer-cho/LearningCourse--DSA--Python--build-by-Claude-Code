# Scenario: a race organizer needs every possible finishing order for a
# small field of runners. Pattern: backtracking, permutations shape
# (a "used" tracker since every element is a candidate at every
# position).
# Run: uv run pytest 14-backtracking -k ex03


def permutations(nums: list[int]) -> list[list[int]]:
    """Return every permutation (ordering) of `nums`. `nums` has no
    duplicate values.

    Order of the outer list doesn't matter; each permutation's element
    order matters and must be preserved exactly as generated.

    permutations([1, 2]) -> [[1, 2], [2, 1]]   (any order of the two)
    permutations([]) -> [[]]

    Target: O(n! * n) time (that's the output size), O(n) space for
    the used-tracker and recursion depth.
    """
    raise NotImplementedError


def permutations_unique(nums: list[int]) -> list[list[int]]:
    """Return every DISTINCT permutation of `nums`, which MAY contain
    duplicate values (e.g. [1, 1, 2]). No duplicate permutation
    appears twice in the result.

    A `used: list[bool]` array alone isn't enough here — it prevents
    reusing the same INDEX twice within one permutation, but two
    equal VALUES at different indices would still both get tried at
    the same position, producing duplicate permutations. Instead,
    track how many of EACH VALUE are still available (e.g. a
    dict[value, count]): at each position, try each distinct value at
    most once, decrement its count while it's placed, restore it when
    you backtrack.

    permutations_unique([1, 1, 2]) -> [[1,1,2],[1,2,1],[2,1,1]]
        (any order; each permutation appears exactly once)

    Target: O(n! * n) time in the worst case, O(n) space for the
    count map and recursion depth.
    """
    raise NotImplementedError
