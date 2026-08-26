# Scenario: a low-level math library operates on numeric strings and
# digit arrays where parsing the whole thing into one big int is
# banned -- practice the carry-loop and digit-array idioms behind
# arbitrary-precision arithmetic. Pattern: carry loop, cycle detection
# with a set.
# Run: uv run pytest 20-bit-manipulation-math -k ex06


def add_binary(a: str, b: str) -> str:
    """Add two binary strings and return their sum as a binary string.

    Do NOT convert either whole string to an int (no `int(a, 2)` on
    the full input, no built-in bigint parse) -- add them the way you
    would by hand: a carry loop from the rightmost digit leftward.

    add_binary("11", "1") -> "100"
    add_binary("1010", "1011") -> "10101"
    add_binary("0", "0") -> "0"

    `a` and `b` are non-empty strings of '0'/'1', no leading zeros
    except the single-character "0". Target complexity:
    O(max(len(a), len(b))) time and space.
    """
    raise NotImplementedError


def plus_one(digits: list[int]) -> list[int]:
    """`digits` is a non-negative integer written as a list of decimal
    digits, most significant first. Return the digits of `digits + 1`.

    Walk from the last digit leftward, propagating the carry: a 9
    becomes 0 and carries into the next digit left; anything else just
    increments and the carry stops. If the carry survives past the
    front (e.g. 999 -> 1000), prepend a 1.

    plus_one([1, 2, 3]) -> [1, 2, 4]
    plus_one([9, 9]) -> [1, 0, 0]
    plus_one([0]) -> [1]

    `digits` has no leading zeros except the single-element `[0]`.
    Target complexity: O(n) time, O(1) extra space beyond the output
    (the carry rarely ripples past a handful of digits).
    """
    raise NotImplementedError


def is_happy(n: int) -> bool:
    """Is `n` a "happy number"?

    Repeatedly replace `n` with the sum of the squares of its decimal
    digits. `n` is happy if this sequence eventually reaches 1 (and
    stays there forever after). If it isn't happy, the sequence falls
    into a cycle that never includes 1.

    Track every value seen so far in a set: if you reach 1, return
    True; if you reach a value already in the set, you're in a cycle
    that will never hit 1 -- return False. (Floyd's cycle detection
    from module 07 -- slow/fast pointers -- also solves this in O(1)
    space instead of O(cycle length); the set version is the more
    common interview-clear answer since the unhappy cycle is short.)

    is_happy(19) -> True    (19 -> 82 -> 68 -> 100 -> 1)
    is_happy(2) -> False    (2 cycles without ever reaching 1)
    is_happy(1) -> True

    `n >= 1`. Target complexity: O(log n) per step; terminates quickly
    in practice (the unhappy cycle has only a handful of distinct
    values).
    """
    raise NotImplementedError
