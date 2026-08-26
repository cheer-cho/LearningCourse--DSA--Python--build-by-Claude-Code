from ex05_word_split import can_segment


def test_simple_two_word_split():
    assert can_segment("dogcat", ["dog", "cat"]) is True


def test_extra_dictionary_words_are_fine():
    assert can_segment("dogcatapp", ["dog", "cat", "app", "cats"]) is True


def test_no_valid_split_exists():
    assert can_segment("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_empty_string_is_trivially_splittable():
    assert can_segment("", ["a"]) is True


def test_single_word_matches_whole_string():
    assert can_segment("leetcode", ["leet", "code"]) is True


def test_word_reused_multiple_times():
    assert can_segment("aaaaaaa", ["a", "aa"]) is True


def test_close_but_leftover_character_fails():
    assert can_segment("aaaaaaab", ["a", "aa", "aaa"]) is False


def test_empty_word_list_only_matches_empty_string():
    assert can_segment("hi", []) is False
    assert can_segment("", []) is True


def test_efficiency_adversarial_all_a_then_b():
    # Classic worst case for a naive (unmemoized) backtracking split:
    # exponentially many ways to partition the "a" run before hitting
    # the trailing "b" and failing. DP examines each prefix once.
    n = 300
    s = "a" * n + "b"
    words = [("a" * k) for k in range(1, 21)]
    assert can_segment(s, words) is False


def test_efficiency_large_true_case():
    n = 1_000
    s = "a" * n
    assert can_segment(s, ["a", "aa", "aaa"]) is True
