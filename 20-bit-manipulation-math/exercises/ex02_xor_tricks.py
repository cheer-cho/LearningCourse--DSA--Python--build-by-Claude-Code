# Scenario: XOR's three laws (a^a=0, a^0=a, order doesn't matter) let
# you cancel pairs, spot an odd one out, and diff two values -- all in
# O(1) extra space. Pattern: XOR fold.
# Run: uv run pytest 20-bit-manipulation-math -k ex02


def find_single(nums: list[int]) -> int:
    """Every value in `nums` appears exactly TWICE except one, which
    appears exactly ONCE. Return that one value.

    XOR-fold the whole list: every pair of equal values cancels to 0
    (a^a=0), leaving only the value with no partner (x^0=x). Order of
    folding never matters -- XOR is commutative and associative.

    find_single([4, 1, 2, 1, 2]) -> 4
    find_single([7]) -> 7

    `nums` has at least one element. Target complexity: O(n) time,
    O(1) space.
    """
    raise NotImplementedError


def find_missing(nums: list[int]) -> int:
    """`nums` holds `n` distinct values drawn from the range `0..n`
    inclusive, with exactly ONE value missing. Return the missing one.

    XOR version (required here): XOR every index `0..n` together with
    every value in `nums`. Every value present cancels with its own
    index-XOR contribution, leaving only the missing one. (A tempting
    alternative is `sum(0..n) - sum(nums)`, which also works, but
    risks integer overflow in fixed-width languages -- XOR never
    does, since it never carries.)

    find_missing([3, 0, 1]) -> 2      (range is 0..3, 2 is absent)
    find_missing([0, 1]) -> 2         (range is 0..2, 2 is absent)
    find_missing([1]) -> 0            (range is 0..1, 0 is absent)

    Target complexity: O(n) time, O(1) space.
    """
    raise NotImplementedError


def swap_count_bits(a: int, b: int) -> int:
    """Return the Hamming distance between `a` and `b`: the number of
    bit positions where they differ.

    `a ^ b` has a 1 in exactly the positions where `a` and `b`
    disagree -- so the Hamming distance is just the popcount of
    `a ^ b`.

    swap_count_bits(0b1010, 0b1001) -> 2
    swap_count_bits(5, 5) -> 0

    Target complexity: O(k) time where k = number of differing bits,
    O(1) space.
    """
    raise NotImplementedError
