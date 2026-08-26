def factorial(n: int) -> int:
    # Pattern: linear recursion (peel off one unit of work per call).
    # Base case n == 0 stops the shrink; each level multiplies by n.
    # Time: O(n), Space: O(n) call-stack depth.
    if n == 0:
        return 1
    return n * factorial(n - 1)


def sum_digits(n: int) -> int:
    # Pattern: linear recursion shrinking via integer division.
    # Base case n < 10 (single digit); each level peels off n % 10.
    # Time: O(d), Space: O(d), d = digit count.
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def countdown(n: int) -> list[int]:
    # Pattern: linear recursion building a list top-down.
    # Base case n <= 0 -> []; each level prepends n and recurses on n - 1.
    # Time: O(n), Space: O(n).
    if n <= 0:
        return []
    return [n] + countdown(n - 1)


def reverse_string_rec(s: str) -> str:
    # Pattern: linear recursion reversing via "reverse the tail, then
    # move the head to the end". Base case len(s) <= 1 -> s.
    # Time: O(n^2) (concatenation copies each level), Space: O(n).
    if len(s) <= 1:
        return s
    return reverse_string_rec(s[1:]) + s[0]
