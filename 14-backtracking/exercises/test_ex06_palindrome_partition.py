from ex06_palindrome_partition import palindrome_partitions


def as_set(list_of_lists: list[list[str]]) -> set[tuple[str, ...]]:
    return {tuple(item) for item in list_of_lists}


def test_palindrome_partitions_basic():
    result = palindrome_partitions("aab")
    expected = {("a", "a", "b"), ("aa", "b")}
    assert as_set(result) == expected


def test_palindrome_partitions_single_char():
    assert palindrome_partitions("a") == [["a"]]


def test_palindrome_partitions_empty_string():
    assert palindrome_partitions("") == [[]]


def test_palindrome_partitions_all_same_char():
    result = palindrome_partitions("aaa")
    expected = {
        ("a", "a", "a"),
        ("a", "aa"),
        ("aa", "a"),
        ("aaa",),
    }
    assert as_set(result) == expected


def test_palindrome_partitions_no_palindromic_substring_longer_than_one():
    result = palindrome_partitions("abc")
    assert as_set(result) == {("a", "b", "c")}


def test_palindrome_partitions_every_piece_is_a_palindrome():
    for partition in palindrome_partitions("racecarxyz"):
        for piece in partition:
            assert piece == piece[::-1]


def test_palindrome_partitions_pieces_reconstruct_input():
    s = "abba"
    for partition in palindrome_partitions(s):
        assert "".join(partition) == s
