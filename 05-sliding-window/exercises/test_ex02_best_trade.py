from ex02_best_trade import max_profit


def test_max_profit_typical():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_max_profit_falling_only_returns_zero():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_max_profit_empty_list():
    assert max_profit([]) == 0


def test_max_profit_single_price():
    assert max_profit([5]) == 0


def test_max_profit_all_equal_prices():
    assert max_profit([3, 3, 3, 3]) == 0


def test_max_profit_buy_low_at_the_end_no_time_to_sell():
    assert max_profit([5, 4, 3, 2, 1]) == 0


def test_max_profit_dip_then_rise():
    assert max_profit([9, 1, 2, 3, 10]) == 9


def test_max_profit_efficiency_large_input():
    n = 200_000
    prices = list(range(n, 0, -1))  # falling
    prices.append(n + 1)  # one huge spike at the very end
    assert max_profit(prices) == n
