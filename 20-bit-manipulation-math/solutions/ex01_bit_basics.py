def get_bit(n: int, i: int) -> int:
    # Pattern: shift-and-mask. Shift bit i to position 0, mask off the rest.
    # Time: O(1). Space: O(1).
    return (n >> i) & 1


def set_bit(n: int, i: int) -> int:
    # Pattern: OR in a single 1 at position i; every other bit passes
    # through OR'd with 0, i.e. unchanged. Time/space: O(1).
    return n | (1 << i)


def clear_bit(n: int, i: int) -> int:
    # Pattern: AND with a mask that's 0 only at position i (~(1<<i)).
    # Time/space: O(1).
    return n & ~(1 << i)


def toggle_bit(n: int, i: int) -> int:
    # Pattern: XOR with a single 1 at position i flips exactly that bit
    # (a^1 = ~a, a^0 = a for every other position). Time/space: O(1).
    return n ^ (1 << i)


def is_power_of_two(n: int) -> bool:
    # Pattern: a power of two has exactly one set bit, so dropping the
    # lowest set bit (n & (n-1)) leaves 0. Time/space: O(1).
    return n > 0 and (n & (n - 1)) == 0


def count_set_bits(n: int) -> int:
    # Pattern: Kernighan's trick. n & (n-1) clears the LOWEST set bit,
    # so the loop runs exactly once per set bit -- never once per bit
    # position. Time: O(k) for k set bits (independent of bit width).
    # Space: O(1).
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count
