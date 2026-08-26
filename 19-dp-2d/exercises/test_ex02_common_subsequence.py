from ex02_common_subsequence import lcs_length, lcs_string


def test_lcs_length_classic_example():
    assert lcs_length("ace", "abcde") == 3


def test_lcs_length_identical_strings():
    assert lcs_length("abc", "abc") == 3


def test_lcs_length_no_overlap():
    assert lcs_length("abc", "def") == 0


def test_lcs_length_empty_first_string():
    assert lcs_length("", "abc") == 0


def test_lcs_length_both_empty():
    assert lcs_length("", "") == 0


def test_lcs_length_efficiency_large_inputs():
    a = "ab" * 500
    b = "ba" * 500
    assert lcs_length(a, b) == len(a) - 1


def test_lcs_string_classic_example():
    assert lcs_string("ace", "abcde") == "ace"


def test_lcs_string_matches_lcs_length():
    a, b = "abcba", "abcbcba"
    result = lcs_string(a, b)
    assert len(result) == lcs_length(a, b)
    assert result == "abcba"


def test_lcs_string_empty_input():
    assert lcs_string("", "abc") == ""


def test_lcs_string_no_common_characters():
    assert lcs_string("abc", "xyz") == ""


def test_lcs_string_is_a_true_subsequence_of_both():
    a, b = "human", "chimpanzee"
    result = lcs_string(a, b)

    def is_subsequence(sub: str, full: str) -> bool:
        it = iter(full)
        return all(ch in it for ch in sub)

    assert len(result) == lcs_length(a, b)
    assert is_subsequence(result, a)
    assert is_subsequence(result, b)
