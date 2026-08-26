# Scenario: the bit-flag toolkit every later exercise in this module
# builds on. Pattern: shift-and-mask (get/set/clear/toggle), plus the
# two identities n & -n (lowest set bit) and n & (n-1) (drop lowest
# set bit / Kernighan's popcount loop).
# Run: uv run pytest 20-bit-manipulation-math -k ex01


def get_bit(n: int, i: int) -> int:
    """Return bit `i` of `n` (0 = least significant), as 0 or 1.

    Shift the target bit down to position 0, then mask off the rest.

    get_bit(0b1010, 1) -> 1
    get_bit(0b1010, 0) -> 0

    Target complexity: O(1) time, O(1) space.
    """
    raise NotImplementedError


def set_bit(n: int, i: int) -> int:
    """Return `n` with bit `i` forced to 1 (all other bits unchanged).

    OR in a single 1 at position `i`.

    set_bit(0b0000, 2) -> 0b0100
    set_bit(0b0100, 2) -> 0b0100   (already set: no change)

    Target complexity: O(1) time, O(1) space.
    """
    raise NotImplementedError


def clear_bit(n: int, i: int) -> int:
    """Return `n` with bit `i` forced to 0 (all other bits unchanged).

    AND with a mask that is 0 only at position `i`.

    clear_bit(0b0100, 2) -> 0b0000
    clear_bit(0b0000, 2) -> 0b0000  (already clear: no change)

    Target complexity: O(1) time, O(1) space.
    """
    raise NotImplementedError


def toggle_bit(n: int, i: int) -> int:
    """Return `n` with bit `i` flipped (0 -> 1 or 1 -> 0).

    XOR with a single 1 at position `i`.

    toggle_bit(0b0100, 2) -> 0b0000
    toggle_bit(0b0000, 2) -> 0b0100

    Target complexity: O(1) time, O(1) space.
    """
    raise NotImplementedError


def is_power_of_two(n: int) -> bool:
    """Return True if `n` is a positive power of two (1, 2, 4, 8, ...).

    A power of two has exactly one set bit, so `n & (n - 1)` (drop the
    lowest set bit) leaves 0. `n <= 0` is never a power of two here.

    is_power_of_two(16) -> True
    is_power_of_two(18) -> False
    is_power_of_two(0) -> False
    is_power_of_two(-4) -> False

    Target complexity: O(1) time, O(1) space.
    """
    raise NotImplementedError


def count_set_bits(n: int) -> int:
    """Return how many 1-bits are in the non-negative integer `n`
    (its "popcount" / Hamming weight).

    Use Kernighan's trick: `n & (n - 1)` clears the LOWEST set bit
    each time, so the loop runs exactly once per set bit, no matter
    how many total bits `n` occupies. Do NOT loop over a fixed bit
    width (e.g. `for i in range(32)`) -- that does wasted work on
    every bit that's already 0.

    count_set_bits(0b1011) -> 3
    count_set_bits(0) -> 0
    count_set_bits(1 << 40) -> 1   (huge bit width, one set bit)

    Target complexity: O(k) time where k = number of set bits, O(1)
    space.
    """
    raise NotImplementedError
