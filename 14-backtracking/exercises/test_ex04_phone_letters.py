from ex04_phone_letters import letter_combos


def test_letter_combos_two_digits():
    result = letter_combos("23")
    expected = {"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"}
    assert set(result) == expected
    assert len(result) == 9


def test_letter_combos_empty_input_is_empty_output():
    assert letter_combos("") == []


def test_letter_combos_single_digit():
    result = letter_combos("7")
    assert set(result) == {"p", "q", "r", "s"}


def test_letter_combos_count_multiplies_letters_per_digit():
    # "9" has 4 letters, "7" has 4 letters -> 16 combos
    assert len(letter_combos("97")) == 16


def test_letter_combos_no_duplicate_combos():
    result = letter_combos("234")
    assert len(result) == len(set(result))


def test_letter_combos_each_combo_has_length_of_digits():
    for combo in letter_combos("2345"):
        assert len(combo) == 4
