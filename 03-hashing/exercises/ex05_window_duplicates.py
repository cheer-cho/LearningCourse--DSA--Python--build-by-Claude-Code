# Scenario: a fraud-detection feed wants to know if the same
# transaction ID shows up twice close together in a stream. Pattern:
# a hash map remembering the LAST index a value was seen — a preview of
# module 05's sliding window.
# Run: uv run pytest 03-hashing -k ex05


def has_nearby_duplicate(nums: list[int], k: int) -> bool:
    """Return True if some value appears at least twice in `nums` with
    the two indices at most `k` apart (i.e. |i - j| <= k).

    Keep a map of value -> its most recently seen index. For each new
    index, check whether that value's last-seen index is within k
    before updating it. Recency matters: only the CLOSEST prior
    occurrence can satisfy the distance check, so overwriting the map
    with the newest index each time is exactly right.

    has_nearby_duplicate([1, 2, 3, 1], 3) -> True    # both 1's, distance 3
    has_nearby_duplicate([1, 2, 3, 1], 2) -> False   # distance 3 > k
    has_nearby_duplicate([1, 2, 3], 1) -> False

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError


def first_repeated_within(stream: list[int], k: int) -> int | None:
    """Scan `stream` left to right and return the VALUE of the first
    element that turns out to be a repeat of something seen within the
    last `k` positions. Return None if no such repeat occurs.

    "First" means: the earliest index at which the repeat is detected
    while scanning forward (not the earliest value numerically).

    first_repeated_within([5, 6, 5, 7], 2) -> 5   # second 5 at index 2,
                                                    # distance 2 <= k
    first_repeated_within([5, 6, 7, 5], 2) -> None  # distance 3 > k
    first_repeated_within([], 3) -> None

    Target: O(n) time, O(n) space.
    """
    raise NotImplementedError
