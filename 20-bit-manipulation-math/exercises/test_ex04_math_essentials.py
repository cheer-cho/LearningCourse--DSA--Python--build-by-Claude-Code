from ex04_math_essentials import gcd, is_prime, lcm, primes_upto

# -- gcd --------------------------------------------------------------------


def test_gcd_typical():
    assert gcd(48, 18) == 6


def test_gcd_coprime_pair():
    assert gcd(17, 5) == 1


def test_gcd_one_operand_zero():
    assert gcd(0, 5) == 5
    assert gcd(7, 0) == 7


def test_gcd_both_zero():
    assert gcd(0, 0) == 0


def test_gcd_equal_values():
    assert gcd(9, 9) == 9


def test_gcd_matches_brute_force():
    for a in range(1, 60):
        for b in range(1, 60):
            expected = max(d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0)
            assert gcd(a, b) == expected


# -- lcm ----------------------------------------------------------------


def test_lcm_typical():
    assert lcm(4, 6) == 12


def test_lcm_coprime_pair():
    assert lcm(5, 7) == 35


def test_lcm_equal_values():
    assert lcm(6, 6) == 6


def test_lcm_one_divides_the_other():
    assert lcm(3, 9) == 9


# -- primes_upto --------------------------------------------------------


def test_primes_upto_typical():
    assert primes_upto(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_primes_upto_below_two_is_empty():
    assert primes_upto(1) == []
    assert primes_upto(0) == []


def test_primes_upto_two_is_just_two():
    assert primes_upto(2) == [2]


def test_primes_upto_matches_brute_force():
    def is_prime_brute(k: int) -> bool:
        if k < 2:
            return False
        return all(k % d != 0 for d in range(2, k))

    expected = [k for k in range(2, 201) if is_prime_brute(k)]
    assert primes_upto(200) == expected


def test_primes_upto_large_n_is_efficient():
    n = 1_000_000
    primes = primes_upto(n)
    assert len(primes) == 78_498
    assert primes[0] == 2
    assert primes[-1] == 999_983


# -- is_prime -------------------------------------------------------------


def test_is_prime_true_cases():
    for n in (2, 3, 5, 7, 11, 97):
        assert is_prime(n) is True


def test_is_prime_false_cases():
    for n in (0, 1, 4, 6, 91, 100):
        assert is_prime(n) is False


def test_is_prime_negative_is_false():
    assert is_prime(-7) is False


def test_is_prime_matches_sieve_over_a_range():
    n = 500
    sieve_primes = set(primes_upto(n))
    for k in range(n + 1):
        assert is_prime(k) == (k in sieve_primes)


def test_is_prime_large_prime_and_large_composite():
    assert is_prime(999_983) is True
    assert is_prime(999_984) is False
