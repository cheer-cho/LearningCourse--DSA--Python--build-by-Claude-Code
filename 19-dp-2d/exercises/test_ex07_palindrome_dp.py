from ex07_palindrome_dp import count_palindromic_substrings, longest_palindromic_substring


def test_count_palindromic_substrings_no_repeats():
    assert count_palindromic_substrings("abc") == 3


def test_count_palindromic_substrings_all_same_character():
    assert count_palindromic_substrings("aaa") == 6


def test_count_palindromic_substrings_mixed():
    assert count_palindromic_substrings("aba") == 4


def test_count_palindromic_substrings_single_character():
    assert count_palindromic_substrings("z") == 1


def test_count_palindromic_substrings_even_length_pair():
    assert count_palindromic_substrings("aa") == 3


def test_count_palindromic_substrings_efficiency_large_input():
    s = "a" * 2_000
    # n*(n+1)/2 palindromic substrings for an all-same-character string.
    assert count_palindromic_substrings(s) == 2_000 * 2_001 // 2


def test_longest_palindromic_substring_odd_length_answer():
    assert longest_palindromic_substring("babad") in ("bab", "aba")


def test_longest_palindromic_substring_even_length_answer():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_longest_palindromic_substring_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_longest_palindromic_substring_no_repeats_returns_first_char():
    assert longest_palindromic_substring("ac") == "a"


def test_longest_palindromic_substring_whole_string_is_a_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_longest_palindromic_substring_efficiency_large_input():
    # A single large palindrome (equal "a" runs on both sides of the
    # center "b") so the whole 1999-character string is the answer.
    s = "a" * 999 + "b" + "a" * 999
    result = longest_palindromic_substring(s)
    assert result == s
    assert len(result) == 1_999
