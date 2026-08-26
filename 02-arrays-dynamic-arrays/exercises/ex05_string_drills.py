# Scenario: cleaning up user-typed search queries and compressing repeated
# sensor characters for cheap storage. Concepts: strings are immutable in
# Python, so build a list of pieces then `str.join` once at the end instead
# of repeatedly concatenating (which is an O(n^2) trap).
# Run: uv run pytest 02-arrays-dynamic-arrays -k ex05


def reverse_words(s: str) -> str:
    """Reverse the order of the words in `s`, collapsing any run of extra
    whitespace (leading, trailing, or between words) down to a single
    space between words in the result.

    reverse_words("one two") -> "two one"
    reverse_words("  hello   world  ") -> "world hello"
    reverse_words("solo") -> "solo"
    reverse_words("") -> ""
    reverse_words("   ") -> ""

    Target complexity: O(n) time, O(n) space (the output is a new string).
    """
    raise NotImplementedError


def run_length_encode(s: str) -> str:
    """Run-length encode `s`: each maximal run of the same character
    becomes that character followed by its run length, even when the
    run length is 1 (this keeps decoding unambiguous).

    run_length_encode("aaabb") -> "a3b2"
    run_length_encode("abc") -> "a1b1c1"
    run_length_encode("") -> ""

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


def run_length_decode(s: str) -> str:
    """Invert `run_length_encode`: expand a string of (character, count)
    pairs back into the original repeated characters. Counts may be more
    than one digit long.

    run_length_decode("a3b2") -> "aaabb"
    run_length_decode("a1b1c1") -> "abc"
    run_length_decode("a12") -> "aaaaaaaaaaaa"
    run_length_decode("") -> ""

    Target complexity: O(n) time, O(n) space, where n is the length of
    the DECODED output.
    """
    raise NotImplementedError
