from ex07_min_cover_window import min_window_cover


def test_min_window_cover_typical():
    assert min_window_cover("ADOBECODEBANC", "ABC") == "BANC"


def test_min_window_cover_not_enough_of_a_character():
    assert min_window_cover("a", "aa") == ""


def test_min_window_cover_empty_t():
    assert min_window_cover("abc", "") == ""


def test_min_window_cover_empty_s():
    assert min_window_cover("", "a") == ""


def test_min_window_cover_whole_string_needed():
    assert min_window_cover("aa", "aa") == "aa"


def test_min_window_cover_shrinks_past_extra_duplicates():
    assert min_window_cover("aabbcc", "abc") == "abbc"


def test_min_window_cover_respects_multiplicity():
    assert min_window_cover("aaabbb", "ab") == "ab"


def test_min_window_cover_no_valid_window():
    assert min_window_cover("abcdef", "xyz") == ""


def test_min_window_cover_efficiency_large_input():
    s = "x" * 50_000 + "aabbcc" + "x" * 50_000
    assert min_window_cover(s, "abc") == "aabbcc"[1:5]  # "abbc"
