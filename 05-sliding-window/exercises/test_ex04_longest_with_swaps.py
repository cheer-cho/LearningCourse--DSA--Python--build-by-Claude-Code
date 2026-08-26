import pytest
from ex04_longest_with_swaps import longest_uniform_with_k_edits


def test_longest_uniform_with_k_edits_negative_k_raises():
    with pytest.raises(ValueError):
        longest_uniform_with_k_edits("aabccbb", -1)


def test_longest_uniform_with_k_edits_typical():
    assert longest_uniform_with_k_edits("aabccbb", 2) == 5


def test_longest_uniform_with_k_edits_zero_edits_all_same():
    assert longest_uniform_with_k_edits("aaaa", 0) == 4


def test_longest_uniform_with_k_edits_zero_edits_all_distinct():
    assert longest_uniform_with_k_edits("abcde", 0) == 1


def test_longest_uniform_with_k_edits_empty_string():
    assert longest_uniform_with_k_edits("", 2) == 0


def test_longest_uniform_with_k_edits_single_char():
    assert longest_uniform_with_k_edits("x", 0) == 1


def test_longest_uniform_with_k_edits_k_covers_whole_string():
    assert longest_uniform_with_k_edits("abcd", 3) == 4


def test_longest_uniform_with_k_edits_stale_max_freq_still_correct():
    # A classic case where max_freq goes stale after a shrink but the
    # answer is still correct.
    assert longest_uniform_with_k_edits("ababbbaaba", 1) == 5


def test_longest_uniform_with_k_edits_efficiency_large_input():
    s = "a" * 100_000 + "b" * 100_000
    assert longest_uniform_with_k_edits(s, 100_000) == 200_000
