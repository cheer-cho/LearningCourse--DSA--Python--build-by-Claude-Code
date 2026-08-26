LOAD_FACTOR = 0.75

_POLY_BASE = 31
_POLY_MOD = 1_000_000_007


class HashMap:
    # Pattern: separate chaining. `_buckets` is a plain list of lists so
    # the mapping itself never delegates to a dict/Map; each bucket is
    # a short list of (key, value) tuples, scanned linearly on collision.
    # Time: O(1) average for set/get/delete (O(1) amortized including
    # resizes); O(n) worst case if everything collides into one bucket.
    # Space: O(n).

    def __init__(self, initial_capacity: int = 8) -> None:
        self._capacity = initial_capacity
        self._buckets: list[list[tuple[int | str, object]]] = [[] for _ in range(initial_capacity)]
        self._size = 0

    def _hash_key(self, key: int | str) -> int:
        if isinstance(key, str):
            h = 0
            for ch in key:
                h = (h * _POLY_BASE + ord(ch)) % _POLY_MOD
            return h % self._capacity
        if isinstance(key, int):
            return key % self._capacity
        raise TypeError(f"unsupported key type: {type(key)!r}")

    def _bucket_for(self, key: int | str) -> list[tuple[int | str, object]]:
        return self._buckets[self._hash_key(key)]

    def set(self, key: int | str, value: object) -> None:
        bucket = self._bucket_for(key)
        for i, (existing_key, _existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        if (self._size + 1) / self._capacity > LOAD_FACTOR:
            self._resize()
            bucket = self._bucket_for(key)  # capacity changed; re-locate

        bucket.append((key, value))
        self._size += 1

    def get(self, key: int | str, default: object = None) -> object:
        bucket = self._bucket_for(key)
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return default

    def delete(self, key: int | str) -> bool:
        bucket = self._bucket_for(key)
        for i, (existing_key, _value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def size(self) -> int:
        return self._size

    def keys(self) -> list[int | str]:
        return [key for bucket in self._buckets for key, _value in bucket]

    def bucket_count(self) -> int:
        return self._capacity

    def _resize(self) -> None:
        old_entries = [entry for bucket in self._buckets for entry in bucket]
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        for key, value in old_entries:
            self._buckets[self._hash_key(key)].append((key, value))
