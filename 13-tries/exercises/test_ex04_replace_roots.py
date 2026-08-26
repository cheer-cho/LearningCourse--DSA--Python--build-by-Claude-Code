from ex04_replace_roots import replace_with_roots


def test_replaces_each_word_with_its_shortest_root():
    roots = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    assert replace_with_roots(roots, sentence) == "the cat was rat by the bat"


def test_shortest_of_multiple_matching_roots_wins():
    assert replace_with_roots(["a", "aa"], "aaa") == "a"


def test_word_with_no_matching_root_is_unchanged():
    assert replace_with_roots(["catt"], "cat") == "cat"


def test_word_equal_to_a_root_is_replaced_by_itself():
    assert replace_with_roots(["cat"], "cat") == "cat"


def test_no_roots_leaves_sentence_unchanged():
    assert replace_with_roots([], "the cattle was rattled") == "the cattle was rattled"


def test_single_word_sentence():
    assert replace_with_roots(["run"], "running") == "run"


def test_mixed_matched_and_unmatched_words():
    roots = ["cat"]
    sentence = "cattle dog cats"
    assert replace_with_roots(roots, sentence) == "cat dog cat"


def test_root_longer_than_word_never_matches():
    assert replace_with_roots(["cattle"], "cat") == "cat"


def test_duplicate_roots_do_not_change_result():
    assert replace_with_roots(["cat", "cat"], "cattle") == "cat"
