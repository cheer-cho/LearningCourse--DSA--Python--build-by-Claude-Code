import pytest
from ex05_postfix_eval import eval_postfix


def test_single_operand():
    assert eval_postfix(["5"]) == 5


def test_add_and_multiply():
    assert eval_postfix(["3", "4", "+", "2", "*"]) == 14


def test_subtraction_order_matters():
    assert eval_postfix(["10", "3", "-"]) == 7
    assert eval_postfix(["3", "10", "-"]) == -7


def test_division_truncates_toward_zero_positive():
    assert eval_postfix(["10", "3", "/"]) == 3


def test_division_truncates_toward_zero_negative():
    assert eval_postfix(["-7", "2", "/"]) == -3
    assert eval_postfix(["7", "-2", "/"]) == -3


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        eval_postfix(["1", "0", "/"])


def test_negative_literals_and_mixed_ops():
    assert eval_postfix(["4", "-2", "*", "3", "+"]) == -5


def test_longer_expression():
    # (2 + 1) * (7 - 4) / 3 = 3 * 3 / 3 = 3
    assert eval_postfix(["2", "1", "+", "7", "4", "-", "*", "3", "/"]) == 3
