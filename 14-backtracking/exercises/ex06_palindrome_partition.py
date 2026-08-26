# Scenario: a DNA-sequence tool needs every way to split a strand into
# pieces that each read the same forwards and backwards. Pattern:
# backtracking over "where does the next piece end", combinations-by-
# position shape.
# Run: uv run pytest 14-backtracking -k ex06


def palindrome_partitions(s: str) -> list[list[str]]:
    """Return every way to split `s` into a list of substrings where
    EVERY substring is a palindrome (reads the same forwards and
    backwards; single characters and the empty string both count).
    The substrings, concatenated in order, must reconstruct `s`
    exactly.

    At each position, try every possible next piece (from length 1 up
    to the rest of the string); only recurse into pieces that are
    themselves palindromes — that's the pruning.

    palindrome_partitions("aab") -> [["a","a","b"], ["aa","b"]]
        (any order of the outer list)
    palindrome_partitions("a") -> [["a"]]
    palindrome_partitions("") -> [[]]

    Target: O(n * 2^n) time worst case (checking each candidate piece
    plus the exponential number of splits), O(n) recursion depth.
    """
    raise NotImplementedError
