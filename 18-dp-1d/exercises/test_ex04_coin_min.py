from ex04_coin_min import min_coins


def test_zero_amount_needs_no_coins():
    assert min_coins([1, 5, 10], 0) == 0


def test_classic_us_change():
    assert min_coins([1, 5, 10, 25], 30) == 2


def test_impossible_amount_returns_minus_one():
    assert min_coins([2], 3) == -1


def test_greedy_biggest_coin_first_would_fail_here():
    # Greedy: 4 + 1 + 1 = 3 coins. Optimal: 3 + 3 = 2 coins.
    assert min_coins([1, 3, 4], 6) == 2


def test_single_denomination_exact_multiple():
    assert min_coins([5], 20) == 4


def test_single_denomination_no_exact_multiple():
    assert min_coins([5], 22) == -1


def test_amount_smaller_than_every_coin():
    assert min_coins([5, 10], 3) == -1


def test_no_coins_available():
    assert min_coins([], 7) == -1


def test_efficiency_large_amount_awkward_coins():
    # amount = 10_000 with a coin set that has no small "unit" coin
    # covering every remainder cleanly -- a naive uncached recursive
    # solution would be exponential (and a naive MEMOIZED recursion
    # would risk RecursionError past Python's default 1000-frame
    # limit); the bottom-up table handles it as a plain nested loop.
    coins = [7, 11, 13, 37]
    result = min_coins(coins, 10_000)
    assert result != -1
    assert result * min(coins) <= 10_000 + max(coins)
    assert sum_uses_valid_coins(coins, result, 10_000)


def sum_uses_valid_coins(coins: list[int], num_coins: int, amount: int) -> bool:
    """Sanity check: `num_coins` coins from `coins` COULD plausibly sum
    to `amount` (necessary, not sufficient, but catches wildly wrong
    answers without re-solving the problem)."""
    if num_coins == 0:
        return amount == 0
    return min(coins) * num_coins <= amount <= max(coins) * num_coins
