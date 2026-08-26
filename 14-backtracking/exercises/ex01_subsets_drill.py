# Scenario: a survey tool needs every possible combination of optional
# add-ons a customer could select. Pattern: backtracking, subsets shape
# (include/skip each element, or a for-loop with a start index).
# Run: uv run pytest 14-backtracking -k ex01


def subsets(nums: list[int]) -> list[list[int]]:
    """Return every subset (the power set) of `nums`, including the
    empty subset and `nums` itself. `nums` has no duplicate values.

    Order of subsets, and order of elements within a subset, does not
    matter — tests compare as sets of frozensets.

    subsets([1, 2]) -> [[], [1], [2], [1, 2]]   (any order)
    subsets([]) -> [[]]

    Target: O(2^n) time (that's the point — there are 2^n subsets),
    O(n) space per subset excluding the output.
    """
    raise NotImplementedError


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    """Return every distinct subset of `nums`, which MAY contain
    duplicate values (e.g. [1, 2, 2]). No duplicate subset appears
    twice in the result.

    Sort first, then skip a repeated value at the same tree level
    (see LESSON.md) so you don't generate the same subset twice.

    subsets_with_dup([1, 2, 2]) -> [[], [1], [2], [1,2], [2,2], [1,2,2]]
        (any order; each subset appears exactly once)

    Target: O(2^n) time, O(n) space per subset excluding the output.
    """
    raise NotImplementedError
