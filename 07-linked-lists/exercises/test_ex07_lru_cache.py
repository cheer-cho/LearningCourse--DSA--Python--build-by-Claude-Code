import random
import time
from collections import OrderedDict

from ex07_lru_cache import LRUCache


def test_get_missing_key_returns_minus_one():
    cache = LRUCache(2)
    assert cache.get(1) == -1


def test_put_then_get_round_trips():
    cache = LRUCache(2)
    cache.put(1, 100)
    assert cache.get(1) == 100


def test_put_overwrites_existing_key():
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(1, 200)
    assert cache.get(1) == 200


def test_eviction_drops_least_recently_used():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    cache.put(3, "c")  # capacity 2 -> evicts key 1 (never touched since)
    assert cache.get(1) == -1
    assert cache.get(2) == "b"
    assert cache.get(3) == "c"


def test_get_refreshes_recency_and_saves_from_eviction():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    cache.get(1)  # 1 is now most-recently-used, 2 is now least
    cache.put(3, "c")  # evicts 2, not 1
    assert cache.get(2) == -1
    assert cache.get(1) == "a"
    assert cache.get(3) == "c"


def test_capacity_one_always_evicts_the_only_entry():
    cache = LRUCache(1)
    cache.put(1, "a")
    cache.put(2, "b")
    assert cache.get(1) == -1
    assert cache.get(2) == "b"


def test_put_on_existing_key_does_not_trigger_eviction():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    cache.put(1, "a-updated")  # key 1 already existed, no eviction
    assert cache.get(1) == "a-updated"
    assert cache.get(2) == "b"


def test_matches_ordereddict_oracle_under_a_mixed_workload():
    # Correctness cross-check: replay the same random ops against a
    # hand-rolled OrderedDict-based LRU and assert every get() agrees.
    capacity = 20
    cache = LRUCache(capacity)
    oracle: OrderedDict[int, int] = OrderedDict()
    rng = random.Random(1234)

    for _ in range(3000):
        key = rng.randrange(0, 50)
        if rng.random() < 0.5:
            value = rng.randrange(0, 1000)
            cache.put(key, value)
            if key in oracle:
                oracle.move_to_end(key)
            oracle[key] = value
            if len(oracle) > capacity:
                oracle.popitem(last=False)
        else:
            expected = oracle.get(key, -1)
            if key in oracle:
                oracle.move_to_end(key)
            assert cache.get(key) == expected


def test_100_000_mixed_ops_at_capacity_500_is_fast_and_correct():
    # Efficiency test: O(1) get/put means 100_000 ops over a capacity-
    # 500 cache finishes almost instantly; a naive O(capacity) scan for
    # "least recently used" would be dramatically slower at this scale.
    capacity = 500
    cache = LRUCache(capacity)

    start = time.perf_counter()
    for i in range(100_000):
        cache.put(i, i * 2)
        if i >= 10:
            cache.get(i - 10)
    elapsed = time.perf_counter() - start

    # only the most recent `capacity` keys can possibly still be present
    assert cache.get(99_999) == 99_999 * 2
    assert cache.get(0) == -1  # long since evicted
    assert elapsed < 8.0  # generous: O(1) ops finish well under a second
