import random

from ex02_xor_tricks import find_missing, find_single, swap_count_bits

# -- find_single ----------------------------------------------------------


def test_find_single_typical():
    assert find_single([4, 1, 2, 1, 2]) == 4


def test_find_single_single_element():
    assert find_single([7]) == 7


def test_find_single_value_at_start_of_list():
    assert find_single([9, 3, 3, 5, 5]) == 9


def test_find_single_with_negative_numbers():
    assert find_single([-3, 2, 2, -3, -7]) == -7


def test_find_single_large_input_is_efficient():
    rng = random.Random(20)
    pairs = [rng.randint(-10_000, 10_000) for _ in range(200_000)]
    nums = pairs + pairs  # every value now appears twice
    nums.append(999_999)  # the odd one out
    rng.shuffle(nums)
    assert find_single(nums) == 999_999


# -- find_missing -----------------------------------------------------------


def test_find_missing_typical():
    assert find_missing([3, 0, 1]) == 2


def test_find_missing_missing_is_the_max():
    assert find_missing([0, 1]) == 2


def test_find_missing_missing_is_zero():
    assert find_missing([1]) == 0


def test_find_missing_only_element_is_zero_missing_is_one():
    assert find_missing([0]) == 1


def test_find_missing_matches_brute_force_over_many_shuffles():
    rng = random.Random(3)
    for n in range(1, 30):
        full = list(range(n + 1))
        missing = rng.choice(full)
        nums = [x for x in full if x != missing]
        rng.shuffle(nums)
        assert find_missing(nums) == missing


def test_find_missing_large_input_is_efficient():
    n = 200_000
    missing = 123_456
    nums = [x for x in range(n + 1) if x != missing]
    assert find_missing(nums) == missing


# -- swap_count_bits ----------------------------------------------------


def test_swap_count_bits_typical():
    assert swap_count_bits(0b1010, 0b1001) == 2


def test_swap_count_bits_identical_values():
    assert swap_count_bits(5, 5) == 0


def test_swap_count_bits_completely_different():
    assert swap_count_bits(0b0000, 0b1111) == 4


def test_swap_count_bits_matches_brute_force():
    rng = random.Random(11)
    for _ in range(200):
        a, b = rng.randint(0, 4096), rng.randint(0, 4096)
        expected = sum(1 for x, y in zip(bin(a)[2:].zfill(13), bin(b)[2:].zfill(13)) if x != y)
        assert swap_count_bits(a, b) == expected
