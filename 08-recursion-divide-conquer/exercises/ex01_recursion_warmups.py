# Scenario: warm up the recursive muscle on four classic self-similar
# problems. Pattern: base case + shrinking step (LESSON.md's three rules).
# Run: uv run pytest 08-recursion-divide-conquer -k ex01


def factorial(n: int) -> int:
    """Return n! = n * (n-1) * ... * 1, computed recursively.

    Base case: n == 0 -> 1 (0! is defined as 1).
    Shrinking step: n * factorial(n - 1).

    Params: n (int, n >= 0). Returns: n factorial.

    factorial(0) -> 1
    factorial(1) -> 1
    factorial(5) -> 120

    Target: O(n) time, O(n) space (call-stack depth n).
    """
    raise NotImplementedError


def sum_digits(n: int) -> int:
    """Return the sum of the decimal digits of a non-negative integer.

    Base case: n < 10 -> n itself (already a single digit).
    Shrinking step: last digit (n % 10) plus sum_digits of what's left
    (n // 10).

    Params: n (int, n >= 0). Returns: sum of n's digits.

    sum_digits(0) -> 0
    sum_digits(9) -> 9
    sum_digits(12345) -> 15

    Target: O(d) time, O(d) space, where d is the number of digits.
    """
    raise NotImplementedError


def countdown(n: int) -> list[int]:
    """Build [n, n-1, ..., 1] recursively (n <= 0 gives an empty list).

    Base case: n <= 0 -> [].
    Shrinking step: [n] + countdown(n - 1).

    Params: n (int). Returns: list counting down from n to 1.

    countdown(1) -> [1]
    countdown(4) -> [4, 3, 2, 1]
    countdown(0) -> []

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError


def reverse_string_rec(s: str) -> str:
    """Return s reversed, built recursively. Don't reach for the slice
    shortcut `s[::-1]` here — the point is to practice the shrinking step.

    Base case: len(s) <= 1 -> s.
    Shrinking step: reverse_string_rec(s[1:]) + s[0] (reverse the tail,
    then move the first character to the end).

    Params: s (str). Returns: s reversed.

    reverse_string_rec("") -> ""
    reverse_string_rec("a") -> "a"
    reverse_string_rec("claude") -> "edualc"

    Target: O(n^2) time (string concatenation copies), O(n) space is fine
    here — this exercise is about the recursive shape, not optimality.
    """
    raise NotImplementedError
