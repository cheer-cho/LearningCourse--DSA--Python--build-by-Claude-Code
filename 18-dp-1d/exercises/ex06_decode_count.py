# Scenario: an old radio cipher maps 'A'..'Z' to '1'..'26'. Given a
# digit string, count how many distinct letter-messages it could
# decode to. Digits '0' can never stand alone as a letter.
# Pattern: "count the ways" DP with a two-choice recurrence (take one
# digit as a letter, or two digits as a letter) -- an edge-case gauntlet.
# Run: uv run pytest 18-dp-1d -k ex06

from __future__ import annotations


def decode_ways(digits: str) -> int:
    """Return the number of distinct ways `digits` can be decoded,
    where '1'->'A', '2'->'B', ..., '26'->'Z'. A '0' is never valid as
    a standalone letter (there's no letter 0), only as the second
    digit of "10" or "20".

    STATE: dp[i] = number of ways to decode the prefix digits[:i].
    CHOICE: the LAST decoded letter used either 1 digit (digits[i-1])
    or 2 digits (digits[i-2:i]).
    RECURRENCE: dp[i] = dp[i-1] if digits[i-1] != '0' (single digit is
    a valid letter '1'-'9'), PLUS dp[i-2] if digits[i-2:i] is between
    "10" and "26" (two digits form a valid letter). Both parts can
    apply to the same i (e.g. "11" -> "AA" or "K").
    BASE CASE: dp[0] = 1 (the empty prefix decodes one way: nothing).

    decode_ways("12") -> 2      ("AB" or "L")
    decode_ways("226") -> 3     ("2,2,6"="BBF", "22,6"="VF", "2,26"="BZ")
    decode_ways("06") -> 0      (leading zero can't stand alone)
    decode_ways("10") -> 1      (only "1,0" -> invalid single '0';
        "10" as a pair -> "J")
    decode_ways("100") -> 0     ("1,00" and "10,0" both dead ends)
    decode_ways("") -> 1        (nothing to decode, one empty way)

    Target: O(n) time, O(1) space.
    """
    raise NotImplementedError
