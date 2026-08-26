from ex04_pattern_quiz import PATTERNS, pattern_quiz

EXPECTED = {
    "q1": "hash-map/set",
    "q2": "two-pointers",
    "q3": "fixed-window",
    "q4": "variable-window",
    "q5": "prefix-sums",
    "q6": "monotonic-stack",
    "q7": "stack/queue",
    "q8": "binary-search",
    "q9": "BFS",
    "q10": "DFS/backtracking",
    "q11": "heap/priority-queue",
    "q12": "topological-sort",
    "q13": "union-find",
    "q14": "greedy",
    "q15": "DP-1D",
    "q16": "DP-2D",
    "q17": "Dijkstra",
    "q18": "segment-tree",
    "q19": "trie",
    "q20": "two-heaps",
}


def test_pattern_quiz_has_all_twenty_keys():
    answers = pattern_quiz()
    assert set(answers.keys()) == set(EXPECTED.keys())


def test_pattern_quiz_uses_only_labels_from_patterns():
    answers = pattern_quiz()
    for label in answers.values():
        assert label in PATTERNS


def test_pattern_quiz_every_pattern_covered_at_least_once():
    answers = pattern_quiz()
    assert set(answers.values()) == set(PATTERNS)


def test_pattern_quiz_matches_expected_answers():
    answers = pattern_quiz()
    assert answers == EXPECTED
