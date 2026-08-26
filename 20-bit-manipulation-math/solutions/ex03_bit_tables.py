def count_bits_upto(n: int) -> list[int]:
    # Pattern: DP over bits. popcount(i) = popcount(i >> 1) + (i & 1) --
    # i>>1 is a strictly smaller, already-computed index. One O(1) step
    # per entry, bottom-up. Time: O(n). Space: O(n) for the output.
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result


def reverse_bits32(n: int) -> int:
    # Pattern: fixed-width bit reversal. Peel the lowest bit off n,
    # shift it into the top of result, 32 times. Time: O(1) (32 fixed
    # iterations). Space: O(1).
    n &= 0xFFFFFFFF
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
