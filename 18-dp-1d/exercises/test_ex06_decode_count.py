from ex06_decode_count import decode_ways


def test_empty_string_has_one_way():
    assert decode_ways("") == 1


def test_single_valid_digit():
    assert decode_ways("7") == 1


def test_single_zero_is_undecodable():
    assert decode_ways("0") == 0


def test_two_letters_or_one_combined():
    assert decode_ways("12") == 2


def test_ambiguous_middle_run():
    assert decode_ways("226") == 3


def test_leading_zero_kills_whole_string():
    assert decode_ways("06") == 0


def test_ten_only_decodes_as_pair():
    assert decode_ways("10") == 1


def test_hundred_has_no_valid_decoding():
    assert decode_ways("100") == 0


def test_twenty_seven_is_two_singles_only():
    # "27" as a pair is invalid (> 26); only "2", "7" works.
    assert decode_ways("27") == 1


def test_double_zero_is_always_dead():
    assert decode_ways("1200") == 0


def test_run_of_ones_grows_like_fibonacci():
    # Every adjacent pair of '1's can combine, mirroring the
    # climbing-stairs recurrence exactly.
    assert decode_ways("11") == 2
    assert decode_ways("111") == 3
    assert decode_ways("1111") == 5


def test_efficiency_long_ambiguous_digit_string():
    n = 5_000
    digits = "1" * n
    result = decode_ways(digits)
    assert result > 0
