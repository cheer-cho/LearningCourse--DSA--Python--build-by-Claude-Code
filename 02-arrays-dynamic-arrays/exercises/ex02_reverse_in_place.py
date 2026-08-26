# Scenario: a playlist needs to be flipped and a photo carousel needs to
# cycle its slides without ever allocating a second array. Concepts:
# opposite-ends two-pointer swap, the triple-reversal rotation trick.
# Run: uv run pytest 02-arrays-dynamic-arrays -k ex02


def reverse(nums: list[int]) -> None:
    """Reverse `nums` in place. Returns nothing — mutate the list itself.

    nums = [1, 2, 3, 4]; reverse(nums) -> nums is now [4, 3, 2, 1]
    nums = []; reverse(nums) -> nums is still []
    nums = [7]; reverse(nums) -> nums is still [7]

    Target complexity: O(n) time, O(1) extra space (no second list).
    """
    raise NotImplementedError


def rotate_right(nums: list[int], k: int) -> None:
    """Rotate `nums` right by `k` positions, in place. `k` may be 0,
    equal to len(nums), or larger than len(nums) (treat it mod len(nums)).

    Use the triple-reversal trick: reverse the whole array, then reverse
    each of the two resulting segments. That's three calls to a
    `reverse`-style sweep and zero extra arrays.

    nums = [1, 2, 3, 4, 5]; rotate_right(nums, 2)
        -> nums is now [4, 5, 1, 2, 3]
    nums = [1, 2, 3]; rotate_right(nums, 0) -> nums is still [1, 2, 3]
    nums = [1, 2, 3]; rotate_right(nums, 3) -> nums is still [1, 2, 3]
    nums = [1, 2, 3]; rotate_right(nums, 5) -> same as rotate_right(nums, 2)

    Target complexity: O(n) time, O(1) extra space (no second list).
    """
    raise NotImplementedError
