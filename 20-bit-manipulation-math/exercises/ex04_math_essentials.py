# Scenario: a scheduling tool needs to line up repeating events (gcd/
# lcm) and a security tool needs to test and enumerate primes. Pattern:
# Euclid's gcd, lcm via gcd, trial-division primality, sieve of
# Eratosthenes.
# Run: uv run pytest 20-bit-manipulation-math -k ex04


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of `a` and `b` (Euclid's
    algorithm, iterative).

    Repeatedly replace `(a, b)` with `(b, a % b)` until `b` is 0; `a`
    is then the answer. Every common divisor of `a` and `b` is also a
    common divisor of `b` and `a % b` (and vice versa), so the pair
    can shrink without ever losing the true gcd.

    gcd(48, 18) -> 6
    gcd(0, 5) -> 5
    gcd(7, 0) -> 7
    gcd(0, 0) -> 0

    `a, b >= 0`. Target complexity: O(log(min(a, b))) time, O(1) space.
    """
    raise NotImplementedError


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of `a` and `b`.

    `lcm(a, b) == a // gcd(a, b) * b` -- divide by the shared factor
    BEFORE multiplying, so the intermediate value stays small.

    lcm(4, 6) -> 12
    lcm(5, 7) -> 35

    `a, b >= 1`. Target complexity: O(log(min(a, b))) time, O(1) space.
    """
    raise NotImplementedError


def primes_upto(n: int) -> list[int]:
    """Return every prime `p` with `2 <= p <= n`, in ascending order.

    Sieve of Eratosthenes: start by assuming every number `2..n` is
    prime. For each number `p` still marked prime, cross out every
    multiple of `p` starting at `p*p` (smaller multiples of `p` were
    already crossed out by a smaller prime factor). Whatever survives
    is prime.

    primes_upto(30) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    primes_upto(1) -> []
    primes_upto(0) -> []

    `n >= 0`. Target complexity: O(n log log n) time, O(n) space.
    """
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """Return True if `n` is prime (no divisors other than 1 and
    itself, and `n >= 2`).

    Trial division only needs to check candidate divisors up to
    `floor(sqrt(n))`: if `n == a * b` with both `a` and `b` greater
    than `sqrt(n)`, their product would exceed `n` -- a contradiction
    -- so any factor pair has one member `<= sqrt(n)`.

    is_prime(97) -> True
    is_prime(91) -> False   (7 * 13)
    is_prime(1) -> False
    is_prime(2) -> True

    Target complexity: O(sqrt(n)) time, O(1) space.
    """
    raise NotImplementedError
