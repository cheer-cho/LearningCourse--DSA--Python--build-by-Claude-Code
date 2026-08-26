# Scenario: checking whether scraped forum post titles read the same
# forwards and backwards once punctuation/spacing/case are ignored,
# plus a "typo tolerance" check that allows deleting one character.
# Pattern: two pointers, opposite ends, with a skip/branch rule.
# Run: uv run pytest 04-two-pointers-prefix-sums -k ex02


def is_clean_palindrome(s: str) -> bool:
    """Return True if `s` reads the same forwards and backwards once
    non-alphanumeric characters are ignored and case is folded.

    Walk `left` from the start and `right` from the end. Skip past any
    character that isn't a letter or digit. Compare the rest
    case-insensitively; a mismatch means it's not a palindrome.

    is_clean_palindrome("A man, a plan, a canal: Panama") -> True
    is_clean_palindrome("race a car") -> False
    is_clean_palindrome("") -> True

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError


def valid_after_one_delete(s: str) -> bool:
    """Return True if `s` (lowercase letters only) is a palindrome, or
    can become one by deleting AT MOST one character.

    Two pointers close in from both ends. On the first mismatch, try
    both branches once: skip the left character, or skip the right
    character, and check whether what's left reads as a palindrome.
    Branching only once (never recursing into a second mismatch) is
    what keeps this O(n) instead of exponential.

    valid_after_one_delete("abca") -> True   (remove 'c' or 'b')
    valid_after_one_delete("abc") -> False
    valid_after_one_delete("a") -> True

    Target complexity: O(n) time, O(1) extra space.
    """
    raise NotImplementedError
