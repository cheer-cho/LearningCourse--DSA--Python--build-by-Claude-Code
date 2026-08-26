from ex01_recursion_warmups import countdown, factorial, reverse_string_rec, sum_digits


def test_factorial_base_case():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_typical():
    assert factorial(5) == 120


def test_factorial_larger():
    assert factorial(10) == 3628800


def test_sum_digits_single_digit():
    assert sum_digits(0) == 0
    assert sum_digits(9) == 9


def test_sum_digits_multiple_digits():
    assert sum_digits(12345) == 15


def test_sum_digits_with_zeros_inside():
    assert sum_digits(1002) == 3


def test_countdown_single():
    assert countdown(1) == [1]


def test_countdown_typical():
    assert countdown(4) == [4, 3, 2, 1]


def test_countdown_zero_is_empty():
    assert countdown(0) == []


def test_countdown_negative_is_empty():
    assert countdown(-3) == []


def test_reverse_string_rec_empty():
    assert reverse_string_rec("") == ""


def test_reverse_string_rec_single_char():
    assert reverse_string_rec("a") == "a"


def test_reverse_string_rec_typical():
    assert reverse_string_rec("claude") == "edualc"


def test_reverse_string_rec_palindrome():
    assert reverse_string_rec("level") == "level"


def test_reverse_string_rec_with_spaces():
    assert reverse_string_rec("ab cd") == "dc ba"
