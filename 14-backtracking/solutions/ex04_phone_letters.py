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
    # Pattern: backtracking, combinations-by-position (one choice per
    # digit position, chosen from that digit's letters).
    # Why: each digit independently contributes one letter to the
    # current path; a for-loop per digit's letters covers every
    # combination without hand-writing nested loops per digit count.
    # Complexity: O(4^n * n) time worst case (n = len(digits)).
    if not digits:
        return []

    results: list[str] = []
    path: list[str] = []

    def backtrack(index: int) -> None:
        if index == len(digits):
            results.append("".join(path))
            return
        for letter in KEYPAD[digits[index]]:
            path.append(letter)
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return results
