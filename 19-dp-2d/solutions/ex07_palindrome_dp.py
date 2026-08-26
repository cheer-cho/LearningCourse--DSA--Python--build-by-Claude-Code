from __future__ import annotations


def count_palindromic_substrings(s: str) -> int:
    # Pattern: expand-around-center.
    # STATE: for each of the 2n-1 centers (n single-char, n-1 gaps), the
    # palindrome radius reachable from it.
    # CHOICE: keep expanding outward while both ends still match.
    # RECURRENCE: count one palindrome per successful (left, right) pair.
    # BASE CASE: every single character is a palindrome of length 1.
    # Time: O(n^2), Space: O(1).
    n = len(s)
    count = 0
    for center in range(2 * n - 1):
        left = center // 2
        right = left + (center % 2)
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count


def longest_palindromic_substring(s: str) -> str:
    # Pattern: expand-around-center, tracking the best window seen.
    # STATE/CHOICE/RECURRENCE/BASE CASE: same as count_palindromic_substrings.
    # ORDER: centers left to right; ties keep the EARLIEST (smallest start)
    # because only a strictly longer match overwrites the best.
    # Time: O(n^2), Space: O(1).
    best_start, best_len = 0, 1 if s else 0
    n = len(s)
    for center in range(2 * n - 1):
        left = center // 2
        right = left + (center % 2)
        while left >= 0 and right < n and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > best_len:
                best_start, best_len = left, current_len
            left -= 1
            right += 1
    return s[best_start : best_start + best_len]
