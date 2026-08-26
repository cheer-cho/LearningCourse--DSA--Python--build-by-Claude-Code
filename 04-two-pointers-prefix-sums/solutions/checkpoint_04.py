GAP_SENTINEL = -1


def flat_pairs(sorted_readings: list[int], target: int) -> list[tuple[int, int]]:
    # Pattern: opposite-ends two pointers. Values are distinct, so a
    # match followed by moving both pointers can never re-find the
    # same pair. O(n) time, O(1) extra space (excluding output).
    pairs: list[tuple[int, int]] = []
    left, right = 0, len(sorted_readings) - 1
    while left < right:
        total = sorted_readings[left] + sorted_readings[right]
        if total == target:
            pairs.append((left, right))
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    return pairs


def compact_gaps(readings: list[int]) -> int:
    # Pattern: same-direction reader/writer, same shape as move_zeroes.
    # O(n) time, O(1) extra space.
    write = 0
    for read in range(len(readings)):
        if readings[read] != GAP_SENTINEL:
            readings[write], readings[read] = readings[read], readings[write]
            write += 1
    return write


class RangeGain:
    # Pattern: prefix sums over the segment-delta array. Build O(n)
    # time/space; query O(1) time.
    def __init__(self, readings: list[int]) -> None:
        prefix = [0] * (len(readings) + 1)
        for i, value in enumerate(readings):
            prefix[i + 1] = prefix[i] + value
        self._prefix = prefix

    def query(self, i: int, j: int) -> int:
        return self._prefix[j + 1] - self._prefix[i]


def balanced_checkpoint(readings: list[int]) -> int:
    # Pattern: prefix sums via a running total (same idea as
    # pivot_index). O(n) time, O(1) extra space.
    total = sum(readings)
    left_sum = 0
    for i, value in enumerate(readings):
        right_sum = total - left_sum - value
        if left_sum == right_sum:
            return i
        left_sum += value
    return -1
