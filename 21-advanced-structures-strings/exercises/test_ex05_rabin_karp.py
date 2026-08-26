from ex05_rabin_karp import count_repeated_windows, find_all


def test_find_all_typical():
    assert find_all("abracadabra", "abra") == [0, 7]


def test_find_all_overlapping_matches():
    assert find_all("aaaa", "aa") == [0, 1, 2]


def test_find_all_empty_pattern():
    assert find_all("hello", "") == []


def test_find_all_pattern_longer_than_text():
    assert find_all("hi", "hello") == []


def test_find_all_no_match():
    assert find_all("abcdef", "xyz") == []


def test_find_all_pattern_equals_text():
    assert find_all("abc", "abc") == [0]


def test_find_all_single_char_pattern():
    assert find_all("banana", "a") == [1, 3, 5]


def test_find_all_similar_but_not_matching_substrings():
    # regression guard against "hash match without verification"
    assert find_all("aabaabaaa", "aaba") == [0, 3]


def test_count_repeated_windows_typical():
    assert count_repeated_windows("AAAAA", 2) == 1


def test_count_repeated_windows_dna_example():
    assert count_repeated_windows("ACGTACGT", 4) == 1


def test_count_repeated_windows_no_repeats():
    assert count_repeated_windows("ABCDEFG", 3) == 0


def test_count_repeated_windows_k_longer_than_string():
    assert count_repeated_windows("ACGT", 10) == 0


def test_count_repeated_windows_k_zero_or_negative():
    assert count_repeated_windows("ACGT", 0) == 0


def test_find_all_efficiency_large_input():
    # n = 200,000 text with the pattern hidden near the end. A naive
    # O(n*m) character-by-character scan would compare up to m
    # characters at every one of ~n start positions; the rolling
    # hash slides in O(1) per position.
    n = 200_000
    pattern = "NEEDLE"
    text = "a" * n + pattern + "a" * n
    result = find_all(text, pattern)
    assert result == [n]


def test_count_repeated_windows_efficiency_large_input():
    # A 200,000-character string built from a period-4 repeat has
    # exactly 4 distinct 4-length windows total (one per starting
    # residue mod 4), and with ~50,000 characters worth of extra
    # repeats each one repeats many times over -- a well-defined
    # expected answer without an O(n^2) reference computation.
    n = 200_000
    dna = "ACGT" * (n // 4)
    assert count_repeated_windows(dna, 4) == 4
