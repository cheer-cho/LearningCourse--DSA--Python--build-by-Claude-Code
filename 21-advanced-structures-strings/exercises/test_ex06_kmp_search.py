from ex06_kmp_search import failure_table, kmp_find_all


def test_failure_table_ababaca():
    assert failure_table("ababaca") == [0, 0, 1, 2, 3, 0, 1]


def test_failure_table_all_same_char():
    assert failure_table("aaaa") == [0, 1, 2, 3]


def test_failure_table_no_repeats():
    assert failure_table("abcd") == [0, 0, 0, 0]


def test_failure_table_empty_pattern():
    assert failure_table("") == []


def test_failure_table_single_char():
    assert failure_table("z") == [0]


def test_failure_table_partial_border():
    # "abab" -> "a"(1), "ab"(2) are the growing borders
    assert failure_table("abab") == [0, 0, 1, 2]


def test_kmp_find_all_typical():
    assert kmp_find_all("ababcababcababc", "ababc") == [0, 5, 10]


def test_kmp_find_all_overlapping_matches():
    assert kmp_find_all("aaaa", "aa") == [0, 1, 2]


def test_kmp_find_all_empty_pattern():
    assert kmp_find_all("hello", "") == []


def test_kmp_find_all_pattern_longer_than_text():
    assert kmp_find_all("hi", "hello") == []


def test_kmp_find_all_no_match():
    assert kmp_find_all("abcdef", "xyz") == []


def test_kmp_find_all_pattern_equals_text():
    assert kmp_find_all("abc", "abc") == [0]


def test_kmp_find_all_matches_naive_reference():
    text = "abababababab"
    pattern = "ababab"
    expected = [
        i for i in range(len(text) - len(pattern) + 1) if text[i : i + len(pattern)] == pattern
    ]
    assert kmp_find_all(text, pattern) == expected


def test_kmp_find_all_worst_case_efficiency():
    # Text is all 'a's; pattern is a long run of 'a's ending in 'b'.
    # A naive scan re-checks nearly the whole pattern at almost every
    # start position (O(n*m)); KMP's failure table lets the text
    # pointer move forward only, guaranteeing O(n + m).
    n = 200_000
    text = "a" * n
    pattern = "a" * 1_000 + "b"
    assert kmp_find_all(text, pattern) == []
