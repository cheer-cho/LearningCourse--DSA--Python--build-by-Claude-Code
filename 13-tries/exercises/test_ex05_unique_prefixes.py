from ex05_unique_prefixes import longest_common_prefix_all, shortest_unique_prefix


def test_shortest_unique_prefix_classic_set():
    words = ["dog", "dove", "duck", "dodge"]
    assert shortest_unique_prefix(words) == ["dog", "dov", "du", "dod"]


def test_shortest_unique_prefix_single_word():
    assert shortest_unique_prefix(["cat"]) == ["c"]


def test_shortest_unique_prefix_completely_distinct_words():
    words = ["cat", "dog", "elephant"]
    assert shortest_unique_prefix(words) == ["c", "d", "e"]


def test_shortest_unique_prefix_word_is_prefix_of_another():
    assert shortest_unique_prefix(["do", "dog"]) == ["do", "dog"]


def test_shortest_unique_prefix_preserves_input_order():
    words = ["duck", "dog", "dove"]
    assert shortest_unique_prefix(words) == ["du", "dog", "dov"]


def test_longest_common_prefix_typical():
    assert longest_common_prefix_all(["flower", "flow", "flight"]) == "fl"


def test_longest_common_prefix_no_common_prefix():
    assert longest_common_prefix_all(["dog", "cat"]) == ""


def test_longest_common_prefix_identical_words():
    assert longest_common_prefix_all(["same", "same"]) == "same"


def test_longest_common_prefix_empty_list():
    assert longest_common_prefix_all([]) == ""


def test_longest_common_prefix_single_word():
    assert longest_common_prefix_all(["solo"]) == "solo"


def test_longest_common_prefix_one_word_is_prefix_of_others():
    assert longest_common_prefix_all(["do", "dog", "dodge"]) == "do"


def test_longest_common_prefix_with_empty_string_in_list():
    assert longest_common_prefix_all(["", "abc"]) == ""
