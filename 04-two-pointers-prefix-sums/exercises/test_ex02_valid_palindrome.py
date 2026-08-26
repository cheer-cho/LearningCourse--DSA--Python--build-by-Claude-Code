from ex02_valid_palindrome import is_clean_palindrome, valid_after_one_delete


def test_is_clean_palindrome_ignores_punctuation_case_and_spaces():
    assert is_clean_palindrome("A man, a plan, a canal: Panama") is True


def test_is_clean_palindrome_false_for_non_palindrome():
    assert is_clean_palindrome("race a car") is False


def test_is_clean_palindrome_empty_string():
    assert is_clean_palindrome("") is True


def test_is_clean_palindrome_all_non_alphanumeric():
    assert is_clean_palindrome(".,!?") is True


def test_is_clean_palindrome_single_character():
    assert is_clean_palindrome("z") is True


def test_is_clean_palindrome_digits_count_as_alphanumeric():
    assert is_clean_palindrome("0P") is False


def test_is_clean_palindrome_mixed_alnum_true():
    assert is_clean_palindrome("Was it a car or a cat I saw?") is True


def test_valid_after_one_delete_already_palindrome():
    assert valid_after_one_delete("aba") is True


def test_valid_after_one_delete_remove_from_left_branch():
    assert valid_after_one_delete("abca") is True


def test_valid_after_one_delete_unfixable():
    assert valid_after_one_delete("abc") is False


def test_valid_after_one_delete_single_character():
    assert valid_after_one_delete("a") is True


def test_valid_after_one_delete_empty_string():
    assert valid_after_one_delete("") is True


def test_valid_after_one_delete_remove_from_right_branch():
    assert valid_after_one_delete("cbbcc") is True
