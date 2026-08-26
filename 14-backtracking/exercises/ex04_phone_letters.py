# Scenario: an old phone keypad text-predictor needs every letter
# combination a sequence of digit presses could spell. Pattern:
# backtracking, combinations-by-position (one choice per digit, chosen
# from that digit's letters).
# Run: uv run pytest 14-backtracking -k ex04

KEYPAD: dict[str, str] = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combos(digits: str) -> list[str]:
    """Return every letter combination `digits` (each character '2'-'9')
    could represent on a phone keypad, using the `KEYPAD` mapping
    above. One letter is chosen per digit, in the digits' original
    order.

    letter_combos("23") -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        (any order)
    letter_combos("") -> []   (pin this: empty input, empty output —
        NOT [""], even though an empty path is "technically" valid)

    Target: O(4^n * n) time in the worst case (n = len(digits), 4 is
    the max letters per digit), O(n) recursion depth.
    """
    raise NotImplementedError
