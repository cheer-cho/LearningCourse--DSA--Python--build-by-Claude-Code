from ex02_balanced_brackets import is_balanced, min_removals_to_balance

# ---- is_balanced -------------------------------------------------------


def test_is_balanced_empty_string():
    assert is_balanced("") is True


def test_is_balanced_simple_pairs():
    assert is_balanced("()") is True
    assert is_balanced("[]") is True
    assert is_balanced("{}") is True


def test_is_balanced_nested():
    assert is_balanced("([{}])") is True


def test_is_balanced_sequential():
    assert is_balanced("()[]{}") is True


def test_is_balanced_ignores_other_characters():
    assert is_balanced("f([a, b])") is True


def test_is_balanced_rejects_interleaving():
    assert is_balanced("([)]") is False


def test_is_balanced_rejects_mismatched_type():
    assert is_balanced("(]") is False


def test_is_balanced_rejects_closer_before_opener():
    assert is_balanced(")(") is False


def test_is_balanced_rejects_unclosed_opener():
    assert is_balanced("(()") is False


def test_is_balanced_rejects_extra_closer():
    assert is_balanced("())") is False


# ---- min_removals_to_balance -------------------------------------------


def test_min_removals_already_balanced():
    assert min_removals_to_balance("()") == 0
    assert min_removals_to_balance("(())") == 0


def test_min_removals_empty_string():
    assert min_removals_to_balance("") == 0


def test_min_removals_unclosed_opener():
    assert min_removals_to_balance("(()") == 1


def test_min_removals_mixed_unmatched():
    assert min_removals_to_balance("())(") == 2


def test_min_removals_closer_before_opener():
    assert min_removals_to_balance(")(") == 2


def test_min_removals_all_openers():
    assert min_removals_to_balance("(((") == 3


def test_min_removals_all_closers():
    assert min_removals_to_balance(")))") == 3


def test_min_removals_ignores_non_paren_characters():
    assert min_removals_to_balance("a(b(c)d") == 1
