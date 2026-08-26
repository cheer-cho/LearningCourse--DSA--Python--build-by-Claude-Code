from collections.abc import Callable


def power(x: float, n: int, tick: Callable[[], None] = lambda: None) -> float:
    # Pattern: divide & conquer (exponentiation by squaring). Split n in
    # half, solve the smaller power once, combine by squaring (and one
    # extra multiply for odd n) instead of multiplying x by itself n times.
    # Time: O(log |n|), Space: O(log |n|) call-stack depth.
    tick()
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n, tick)
    half = power(x, n // 2, tick)
    if n % 2 == 0:
        return half * half
    return half * half * x


def power_mod(base: int, exp: int, mod: int, tick: Callable[[], None] = lambda: None) -> int:
    # Pattern: same divide & conquer as power(), but takes `% mod` at
    # every combine step so intermediate values stay bounded — the trick
    # Rabin-Karp's rolling hash (module 21) relies on.
    # Time: O(log exp), Space: O(log exp).
    tick()
    if exp == 0:
        return 1 % mod
    half = power_mod(base, exp // 2, mod, tick)
    result = (half * half) % mod
    if exp % 2 == 1:
        result = (result * base) % mod
    return result
