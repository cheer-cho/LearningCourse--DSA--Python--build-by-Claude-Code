# Scenario: two "whole-range" bit tricks -- a popcount table built
# with a DP recurrence, and a 32-bit reversal. Pattern: DP-over-bits,
# fixed-width masking.
# Run: uv run pytest 20-bit-manipulation-math -k ex03


def count_bits_upto(n: int) -> list[int]:
    """Return a list `result` of length `n + 1` where `result[i]` is
    the number of set bits in `i`, for every `i` from 0 to `n`.

    This is secretly dynamic programming: `i >> 1` is `i` with its
    lowest bit dropped, and `i & 1` is exactly that dropped bit. So
    `popcount(i) == popcount(i >> 1) + (i & 1)` -- the popcount of a
    smaller, already-computed number, plus 0 or 1. State: `result[i]`.
    Recurrence: `result[i] = result[i >> 1] + (i & 1)`. Base case:
    `result[0] = 0`. Order: bottom-up, `i` ascending (so `i >> 1` is
    always already filled in by the time you need it).

    count_bits_upto(5) -> [0, 1, 1, 2, 1, 2]
    count_bits_upto(0) -> [0]

    `n >= 0`. Target complexity: O(n) time, O(n) space (one O(1) step
    per entry -- no per-entry Kernighan loop).
    """
    raise NotImplementedError


def reverse_bits32(n: int) -> int:
    """Reverse the bits of `n`, treated as a 32-bit UNSIGNED integer,
    and return the resulting 32-bit unsigned integer.

    Bit 0 of the input becomes bit 31 of the output and vice versa.
    Build the result one bit at a time: shift the result left, pull
    the lowest bit off `n`, OR it in, shift `n` right; repeat 32
    times. Mask the input to 32 bits first so a Python int larger than
    32 bits (or conceptually "negative" in two's complement) doesn't
    leak extra high bits into the result.

    reverse_bits32(0b00000000000000000000000000001011) -> 0b11010000000000000000000000000000
    reverse_bits32(0) -> 0

    `0 <= n < 2**32`. Target complexity: O(1) time (fixed 32 iterations),
    O(1) space.
    """
    raise NotImplementedError
