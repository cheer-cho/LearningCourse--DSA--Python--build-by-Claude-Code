from ex01_growth_rates import ANSWER_SET, classify_snippets

EXPECTED = {
    "constant_lookup": "O(1)",
    "print_all": "O(n)",
    "binary_search_style": "O(log n)",
    "two_separate_loops": "O(n)",
    "sort_then_scan": "O(n log n)",
    "nested_loop_all_pairs": "O(n^2)",
    "triangular_nested_loop": "O(n^2)",
    "recursive_subsets": "O(2^n)",
}


def test_classify_snippets_matches_answer_key():
    assert classify_snippets() == EXPECTED


def test_classify_snippets_has_exactly_the_expected_keys():
    assert set(classify_snippets().keys()) == set(EXPECTED.keys())


def test_classify_snippets_only_uses_allowed_answers():
    for answer in classify_snippets().values():
        assert answer in ANSWER_SET
