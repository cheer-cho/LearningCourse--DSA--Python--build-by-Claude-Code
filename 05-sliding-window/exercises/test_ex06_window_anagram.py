from ex06_window_anagram import contains_permutation


def test_contains_permutation_found_mid_string():
    assert contains_permutation("abc", "eidbacoo") is True


def test_contains_permutation_not_found():
    assert contains_permutation("ab", "eidboaoo") is False


def test_contains_permutation_empty_needle():
    assert contains_permutation("", "anything") is True


def test_contains_permutation_needle_longer_than_haystack():
    assert contains_permutation("abc", "ab") is False


def test_contains_permutation_exact_match():
    assert contains_permutation("abc", "cab") is True


def test_contains_permutation_repeated_chars_in_needle():
    assert contains_permutation("aab", "eidboaoo") is False
    assert contains_permutation("aab", "eidaabo") is True


def test_contains_permutation_efficiency_large_input():
    needle = "z" * 500 + "y" * 500
    haystack = "x" * 100_000 + needle[::-1] + "x" * 100_000
    assert contains_permutation(needle, haystack) is True


def test_contains_permutation_efficiency_no_match_large_input():
    needle = "q" * 1000
    haystack = "p" * 200_000
    assert contains_permutation(needle, haystack) is False
