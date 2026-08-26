from ex06_monotonic_warm_days import days_until_warmer, next_greater

# ---- days_until_warmer --------------------------------------------------


def test_days_until_warmer_classic_example():
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    assert days_until_warmer(temps) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_days_until_warmer_strictly_increasing():
    assert days_until_warmer([30, 40, 50]) == [1, 1, 0]


def test_days_until_warmer_strictly_decreasing():
    assert days_until_warmer([50, 40, 30]) == [0, 0, 0]


def test_days_until_warmer_empty():
    assert days_until_warmer([]) == []


def test_days_until_warmer_single_element():
    assert days_until_warmer([60]) == [0]


def test_days_until_warmer_plateau_then_rise():
    assert days_until_warmer([70, 70, 70, 80]) == [3, 2, 1, 0]


def test_days_until_warmer_large_decreasing_input_is_fast():
    # Efficiency test: worst case for a naive O(n^2) scan-right
    # approach — nothing is ever warmer, so every element would scan
    # all the way to the end. A monotonic stack still finishes in O(n).
    n = 200_000
    temps = list(range(n, 0, -1))
    assert days_until_warmer(temps) == [0] * n


# ---- next_greater ---------------------------------------------------


def test_next_greater_typical():
    assert next_greater([2, 1, 3, 4]) == [3, 3, 4, -1]


def test_next_greater_strictly_decreasing():
    assert next_greater([4, 3, 2, 1]) == [-1, -1, -1, -1]


def test_next_greater_strictly_increasing():
    assert next_greater([1, 2, 3]) == [2, 3, -1]


def test_next_greater_empty():
    assert next_greater([]) == []


def test_next_greater_duplicates():
    assert next_greater([2, 2, 3]) == [3, 3, -1]


def test_next_greater_large_decreasing_input_is_fast():
    n = 200_000
    nums = list(range(n, 0, -1))
    assert next_greater(nums) == [-1] * n
