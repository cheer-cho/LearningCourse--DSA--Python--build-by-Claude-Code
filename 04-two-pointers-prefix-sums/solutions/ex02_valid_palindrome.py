def is_clean_palindrome(s: str) -> bool:
    # Pattern: two pointers, opposite ends, skipping non-alphanumeric
    # characters as they close in. O(n) time, O(1) extra space (no
    # cleaned copy of the string is built).
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def _is_palindrome_range(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def valid_after_one_delete(s: str) -> bool:
    # Pattern: two pointers, opposite ends, with a one-time branch on
    # the first mismatch (try skipping either side). O(n) time overall
    # since each branch is itself an O(n) palindrome check and we only
    # ever take one branch, O(1) extra space.
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return _is_palindrome_range(s, left + 1, right) or _is_palindrome_range(
                s, left, right - 1
            )
        left += 1
        right -= 1
    return True
