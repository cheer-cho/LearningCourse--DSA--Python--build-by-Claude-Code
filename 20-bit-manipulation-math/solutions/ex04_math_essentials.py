def gcd(a: int, b: int) -> int:
    # Pattern: Euclid's algorithm. (a, b) -> (b, a % b) preserves the
    # set of common divisors while shrinking b roughly by half every
    # two steps. Time: O(log(min(a, b))). Space: O(1).
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    # Pattern: lcm via gcd, dividing before multiplying to avoid an
    # unnecessarily large intermediate. Time: O(log(min(a, b))).
    # Space: O(1).
    return a // gcd(a, b) * b


def primes_upto(n: int) -> list[int]:
    # Pattern: Sieve of Eratosthenes. Cross out multiples of each
    # surviving prime starting at p*p (smaller multiples were already
    # crossed out by a smaller prime factor). Time: O(n log log n).
    # Space: O(n).
    if n < 2:
        return []
    is_composite = [False] * (n + 1)
    primes = []
    for p in range(2, n + 1):
        if not is_composite[p]:
            primes.append(p)
            for multiple in range(p * p, n + 1, p):
                is_composite[multiple] = True
    return primes


def is_prime(n: int) -> bool:
    # Pattern: trial division up to sqrt(n) -- any factor pair has one
    # member at or below sqrt(n). Time: O(sqrt(n)). Space: O(1).
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
