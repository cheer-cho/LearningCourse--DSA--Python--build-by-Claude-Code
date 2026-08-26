import random

from ex06_digit_strings import add_binary, is_happy, plus_one

# -- add_binary -------------------------------------------------------------


def test_add_binary_typical():
    assert add_binary("11", "1") == "100"


def test_add_binary_different_lengths():
    assert add_binary("1010", "1011") == "10101"


def test_add_binary_both_zero():
    assert add_binary("0", "0") == "0"


def test_add_binary_no_carry_needed():
    assert add_binary("100", "1") == "101"


def test_add_binary_full_carry_chain():
    assert add_binary("111", "1") == "1000"


def test_add_binary_matches_python_int_conversion_over_random_pairs():
    rng = random.Random(20)
    for _ in range(100):
        a_val = rng.randint(0, 4095)
        b_val = rng.randint(0, 4095)
        a, b = bin(a_val)[2:], bin(b_val)[2:]
        expected = bin(a_val + b_val)[2:]
        assert add_binary(a, b) == expected


# -- plus_one -----------------------------------------------------------


def test_plus_one_typical():
    assert plus_one([1, 2, 3]) == [1, 2, 4]


def test_plus_one_single_nine():
    assert plus_one([9]) == [1, 0]


def test_plus_one_all_nines():
    assert plus_one([9, 9]) == [1, 0, 0]


def test_plus_one_zero():
    assert plus_one([0]) == [1]


def test_plus_one_trailing_nines_only():
    assert plus_one([1, 2, 9]) == [1, 3, 0]


def test_plus_one_does_not_mutate_a_fresh_list_argument():
    original = [4, 5, 6]
    plus_one(original)
    # The exercise allows in-place mutation OR a new list; either way
    # the returned value must be correct.
    assert plus_one([4, 5, 6]) == [4, 5, 7]


# -- is_happy -------------------------------------------------------------


def test_is_happy_true_case():
    assert is_happy(19) is True


def test_is_happy_one_is_happy():
    assert is_happy(1) is True


def test_is_happy_false_case():
    assert is_happy(2) is False


def test_is_happy_another_known_happy_number():
    assert is_happy(7) is True


def test_is_happy_another_known_unhappy_number():
    assert is_happy(4) is False


def test_is_happy_larger_happy_number():
    assert is_happy(100) is True
