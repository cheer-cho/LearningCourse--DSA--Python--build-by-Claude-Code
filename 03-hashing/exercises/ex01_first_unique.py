# Scenario: a log-scrubbing tool needs the first character in a token
# that never repeats, and a voting tally needs the option most people
# picked. Pattern: counting with a hash map (two-pass).
# Run: uv run pytest 03-hashing -k ex01


def first_unique_index(s: str) -> int:
    """Return the index of the first character in `s` that appears
    exactly once, scanning left to right. Return -1 if every character
    repeats (or `s` is empty).

    Two passes: build a count map, then scan again for the first index
    whose character has count 1. One pass alone can't answer this — you
    don't know a character is "unique" until you've seen the whole
    string.

    first_unique_index("swiss") -> 1   ('s' repeats; 'w' at index 1 is unique)
    first_unique_index("aabb") -> -1
    first_unique_index("") -> -1

    Target: O(n) time, O(k) space (k = distinct characters).
    """
    raise NotImplementedError


def majority_item(nums: list[int]) -> int:
    """Return the element that appears more than len(nums) // 2 times.

    `nums` is guaranteed to contain a majority element (this is the
    classic "Majority Element" setup — the caller has already checked
    one exists). Count occurrences with a hash map and return the key
    whose count clears the threshold.

    majority_item([2, 2, 1, 2, 3]) -> 2
    majority_item([7]) -> 7

    Target: O(n) time, O(n) space.

    Bonus (not required here): the Boyer-Moore Voting Algorithm solves
    this in O(1) space by keeping a single running "candidate" and a
    counter that increments on a match and decrements otherwise —
    worth knowing for the follow-up "can you do it in O(1) space?".
    """
    raise NotImplementedError
