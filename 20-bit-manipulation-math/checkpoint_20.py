# CHECKPOINT 20 -- Hardware diagnostics
#
# A hardware diagnostics subsystem leans on the whole module-20
# toolkit: popcount-based parity, XOR-based fault detection, in-place
# grid rotation, and prime enumeration via sieve.
#
# Passing `uv run pytest 20-bit-manipulation-math` completes this
# module.


def parity_report(packets: list[int]) -> dict[str, object]:
    """Given `packets` (each a non-negative int whose bits are the
    payload), produce a diagnostic report with two keys:

    - `"per_packet_bit_counts"`: a list, the popcount (number of
      1-bits) of each packet, in order.
    - `"overall_checksum"`: the XOR of every packet -- a cheap parity
      check, since any single-bit corruption flips this value.

    Use Kernighan's `n & (n - 1)` trick for each popcount -- one AND
    per set bit, not one per bit position.

    parity_report([5, 3, 6])
        -> {"per_packet_bit_counts": [2, 2, 2], "overall_checksum": 0}
        (5 = 0b101, 3 = 0b011, 6 = 0b110; 5^3^6 == 0)
    parity_report([]) -> {"per_packet_bit_counts": [], "overall_checksum": 0}

    Target complexity: O(sum of popcounts) time, O(n) space for the
    output list.
    """
    raise NotImplementedError


def find_faulty_sensor(readings: list[int]) -> int:
    """Every sensor reading in `readings` is duplicated (appears
    exactly twice) for redundancy, except one faulty sensor whose
    reading appears exactly once. Return that reading.

    Same shape as `find_single` from ex02: XOR-fold the whole list --
    every duplicated pair cancels to 0, leaving only the unpaired
    value.

    find_faulty_sensor([7, 3, 7, 5, 3]) -> 5

    `readings` is non-empty. Target complexity: O(n) time, O(1) space.
    """
    raise NotImplementedError


def firmware_grid_rotate(grid: list[list[int]]) -> None:
    """Rotate a firmware image (a square `n x n` grid) 90 degrees
    clockwise, IN PLACE (no second grid).

    Recipe: transpose, then reverse each row.

    grid = [[1, 2], [3, 4]]
    firmware_grid_rotate(grid) -> grid is now [[3, 1], [4, 2]]

    `grid` is `n x n`, `n >= 1`. Target complexity: O(n^2) time, O(1)
    extra space.
    """
    raise NotImplementedError


def prime_channel_ids(limit: int) -> list[int]:
    """Return every prime channel ID from 2 up to and including
    `limit`, via the Sieve of Eratosthenes.

    (Prime channel IDs never share a harmonic with each other's
    multiples -- that's why the diagnostics tool wants only the
    primes.)

    prime_channel_ids(20) -> [2, 3, 5, 7, 11, 13, 17, 19]
    prime_channel_ids(1) -> []

    `limit >= 0`. Target complexity: O(limit * log(log(limit))) time,
    O(limit) space.
    """
    raise NotImplementedError
