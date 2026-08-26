from functools import reduce


def find_single(nums: list[int]) -> int:
    # Pattern: XOR fold. a^a=0 cancels every pair, a^0=a leaves the
    # unpaired value -- order-independent since XOR is commutative and
    # associative. Time: O(n). Space: O(1).
    result = 0
    for x in nums:
        result ^= x
    return result


def find_missing(nums: list[int]) -> int:
    # Pattern: XOR fold over BOTH the full index range and the values.
    # Every present value cancels its matching index; only the missing
    # index's contribution survives. Time: O(n). Space: O(1).
    n = len(nums)
    result = reduce(lambda acc, i: acc ^ i, range(n + 1), 0)
    for x in nums:
        result ^= x
    return result


def swap_count_bits(a: int, b: int) -> int:
    # Pattern: Hamming distance = popcount of the XOR diff. Kernighan's
    # n & (n-1) loop runs once per differing bit. Time: O(k) differing
    # bits. Space: O(1).
    diff = a ^ b
    count = 0
    while diff:
        diff &= diff - 1
        count += 1
    return count
