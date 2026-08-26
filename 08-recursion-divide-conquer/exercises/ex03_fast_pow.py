# Scenario: exponentiation by squaring — a divide & conquer trick that
# turns O(n) repeated multiplication into O(log n). `tick`, if given, is
# called once per recursive call so tests can verify the log-n call count.
# Run: uv run pytest 08-recursion-divide-conquer -k ex03

from collections.abc import Callable


def power(x: float, n: int, tick: Callable[[], None] = lambda: None) -> float:
    """Compute x ** n using fast exponentiation (divide & conquer), not
    n repeated multiplications.

    Split: n -> n // 2. Solve: recursively compute x ** (n // 2). Combine:
    square that result, and multiply by x once more if n was odd.
    Negative n: x ** n == 1 / (x ** -n) (x must be nonzero).

    Base case: n == 0 -> 1.
    Calls tick() once per recursive call (default: a no-op, for tests
    that don't care about the count).

    power(2, 10) -> 1024
    power(2, -2) -> 0.25
    power(5, 0) -> 1

    Target: O(log |n|) time, O(log |n|) space.
    """
    raise NotImplementedError


def power_mod(base: int, exp: int, mod: int, tick: Callable[[], None] = lambda: None) -> int:
    """Compute (base ** exp) % mod using fast exponentiation, taking the
    modulo at every step so the intermediate numbers never blow up. This
    is the building block Rabin-Karp string matching (module 21) uses to
    keep rolling-hash values bounded.

    Split: exp -> exp // 2. Solve: recursively compute (base ** (exp //
    2)) % mod. Combine: square mod `mod`, and multiply by `base` mod
    `mod` once more if exp was odd.

    Base case: exp == 0 -> 1 % mod.
    Assumes exp >= 0 and mod >= 1. Calls tick() once per recursive call.

    power_mod(2, 10, 1000) -> 24        (2**10 = 1024, 1024 % 1000 = 24)
    power_mod(7, 0, 5) -> 1
    power_mod(3, 5, 7) -> 5             (3**5 = 243, 243 % 7 = 5)

    Target: O(log exp) time, O(log exp) space.
    """
    raise NotImplementedError
