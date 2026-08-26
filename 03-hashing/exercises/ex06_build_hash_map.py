# Scenario: build the machinery that ex01-ex05 took for granted. A
# HashMap from scratch: an array of buckets, each holding a small list
# of (key, value) pairs, that resizes itself as it fills up.
# Run: uv run pytest 03-hashing -k ex06
#
# FROM SCRATCH RULE: no dict/Map/object may be used as the bucket
# storage itself. `self._buckets` must be a plain list of lists (each
# inner list holds (key, value) tuples). You may use a dict/list
# anywhere else you like (e.g. temporarily, in tests) — just not as the
# thing that maps key -> bucket contents.

LOAD_FACTOR = 0.75


class HashMap:
    """A hash map built from an array of buckets (separate chaining).

    Layout: `self._buckets` is a `list` of length `self._capacity`;
    `self._buckets[i]` is a `list[tuple[key, value]]` holding every
    entry whose key hashes to bucket `i`. Collisions just mean more
    than one tuple lands in the same bucket's list.

    Supported key types: `int` and `str`.
      - int keys: bucket index = `key % capacity` (Python's `%` is
        already non-negative for a positive divisor, so negative keys
        work with no extra handling).
      - str keys: a polynomial rolling hash, computed with Horner's
        method, THEN reduced mod capacity:
            h = 0
            for ch in key:
                h = (h * 31 + ord(ch)) % 1_000_000_007
            bucket_index = h % capacity
        (31 is a small odd prime base; 1_000_000_007 is a large prime
        modulus — both are the classic choices for string hashing.)

    Resizing: whenever inserting a NEW key would push
    `size / capacity` above `LOAD_FACTOR` (0.75), the capacity doubles
    and every existing entry is rehashed into the new, larger bucket
    array (its bucket index changes because capacity changed).
    """

    def __init__(self, initial_capacity: int = 8) -> None:
        """Create an empty HashMap with `initial_capacity` buckets, all
        starting empty."""
        raise NotImplementedError

    def set(self, key: int | str, value: object) -> None:
        """Insert `key` -> `value`, or overwrite `value` if `key` is
        already present. Triggers a resize first if adding a NEW key
        would push the load factor over 0.75 (updating an existing
        key's value never triggers a resize).

        m = HashMap()
        m.set("a", 1)
        m.set("a", 2)   # overwrites; size() stays 1

        Target: O(1) average time (amortized, across resizes).
        """
        raise NotImplementedError

    def get(self, key: int | str, default: object = None) -> object:
        """Return the value stored for `key`, or `default` if `key` is
        not present.

        Target: O(1) average time.
        """
        raise NotImplementedError

    def delete(self, key: int | str) -> bool:
        """Remove `key` if present. Return True if something was
        removed, False if `key` wasn't in the map. Does not resize
        down.

        Target: O(1) average time.
        """
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of key/value pairs currently stored."""
        raise NotImplementedError

    def keys(self) -> list[int | str]:
        """Return a list of every key currently stored, in no
        particular order."""
        raise NotImplementedError

    def bucket_count(self) -> int:
        """Return the current number of buckets (the array length),
        so callers/tests can observe that a resize happened."""
        raise NotImplementedError
