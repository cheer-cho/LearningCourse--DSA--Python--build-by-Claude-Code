def add_binary(a: str, b: str) -> str:
    # Pattern: carry loop, right to left, exactly like adding by hand.
    # Time: O(max(len(a), len(b))). Space: same, for the output.
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result: list[str] = []

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result.append(str(total % 2))
        carry = total // 2

    result.reverse()
    return "".join(result)


def plus_one(digits: list[int]) -> list[int]:
    # Pattern: carry loop, right to left. A 9 becomes 0 and carries;
    # anything else stops the carry immediately. Time: O(n). Space:
    # O(1) extra beyond the output.
    result = digits[:]
    for i in range(len(result) - 1, -1, -1):
        if result[i] < 9:
            result[i] += 1
            return result
        result[i] = 0
    return [1] + result


def is_happy(n: int) -> bool:
    # Pattern: cycle detection with a seen-set. A non-happy sequence
    # always revisits a value before it could reach 1. Time: O(log n)
    # per step, terminates quickly. Space: O(cycle length).
    seen: set[int] = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
