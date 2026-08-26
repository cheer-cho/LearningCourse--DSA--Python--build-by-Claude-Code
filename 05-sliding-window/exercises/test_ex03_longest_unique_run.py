from ex03_longest_unique_run import longest_unique


def test_longest_unique_typical():
    assert longest_unique("abcabcbb") == 3


def test_longest_unique_all_same_char():
    assert longest_unique("bbbbb") == 1


def test_longest_unique_empty_string():
    assert longest_unique("") == 0


def test_longest_unique_single_char():
    assert longest_unique("z") == 1


def test_longest_unique_no_repeats_at_all():
    assert longest_unique("abcdef") == 6


def test_longest_unique_repeat_jumps_left_past_stale_index():
    assert longest_unique("dvdf") == 3


def test_longest_unique_repeat_at_very_end():
    assert longest_unique("abba") == 2


def test_longest_unique_efficiency_long_repeating_string():
    s = "ab" * 100_000
    assert longest_unique(s) == 2
