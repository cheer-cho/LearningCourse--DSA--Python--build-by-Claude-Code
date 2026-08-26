from checkpoint_01 import ANSWER_SET, complexity_report, first_repeated, most_common


def test_most_common_typical():
    assert most_common(["a", "b", "a", "c", "b", "a"]) == "a"


def test_most_common_tie_broken_by_first_occurrence():
    assert most_common(["b", "a", "a", "b"]) == "b"


def test_most_common_single_word():
    assert most_common(["x"]) == "x"


def test_most_common_all_unique_returns_first():
    assert most_common(["z", "y", "x"]) == "z"


def test_most_common_large_input_is_fast():
    words = [f"w{i % 5}" for i in range(200_000)]
    assert most_common(words) == "w0"


def test_first_repeated_typical():
    assert first_repeated([2, 5, 3, 5, 2]) == 5


def test_first_repeated_no_repeats_returns_none():
    assert first_repeated([1, 2, 3]) is None


def test_first_repeated_immediate_repeat():
    assert first_repeated([7, 7, 1]) == 7


def test_first_repeated_empty_and_single_return_none():
    assert first_repeated([]) is None
    assert first_repeated([9]) is None


def test_first_repeated_large_input_is_fast():
    nums = list(range(200_000))
    nums.append(0)  # repeat only at the very end, forces a full scan
    assert first_repeated(nums) == 0


def test_complexity_report_matches_answer_key():
    assert complexity_report() == {
        "most_common_time": "O(n)",
        "first_repeated_time": "O(n)",
        "reverse_and_scan": "O(n)",
        "binary_search_twice": "O(log n)",
        "matrix_double_loop": "O(n^2)",
    }


def test_complexity_report_only_uses_allowed_answers():
    for answer in complexity_report().values():
        assert answer in ANSWER_SET
