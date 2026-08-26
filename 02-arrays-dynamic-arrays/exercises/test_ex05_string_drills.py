from ex05_string_drills import reverse_words, run_length_decode, run_length_encode


def test_reverse_words_typical():
    assert reverse_words("one two") == "two one"


def test_reverse_words_collapses_extra_spaces():
    assert reverse_words("  hello   world  ") == "world hello"


def test_reverse_words_single_word():
    assert reverse_words("solo") == "solo"


def test_reverse_words_empty_string():
    assert reverse_words("") == ""


def test_reverse_words_only_whitespace():
    assert reverse_words("   ") == ""


def test_reverse_words_many_words():
    assert reverse_words("the quick brown fox") == "fox brown quick the"


def test_run_length_encode_typical():
    assert run_length_encode("aaabb") == "a3b2"


def test_run_length_encode_no_repeats():
    assert run_length_encode("abc") == "a1b1c1"


def test_run_length_encode_empty_string():
    assert run_length_encode("") == ""


def test_run_length_encode_single_character():
    assert run_length_encode("z") == "z1"


def test_run_length_encode_long_run():
    assert run_length_encode("a" * 12) == "a12"


def test_run_length_decode_typical():
    assert run_length_decode("a3b2") == "aaabb"


def test_run_length_decode_no_repeats():
    assert run_length_decode("a1b1c1") == "abc"


def test_run_length_decode_empty_string():
    assert run_length_decode("") == ""


def test_run_length_decode_multi_digit_count():
    assert run_length_decode("a12") == "a" * 12


def test_encode_decode_round_trip():
    original = "aaabbbbccccccd"
    assert run_length_decode(run_length_encode(original)) == original


def test_run_length_encode_efficiency_on_large_input():
    n = 100_000
    original = "x" * n
    encoded = run_length_encode(original)
    assert encoded == f"x{n}"
