import random

from ex06_build_hash_map import HashMap


def test_set_and_get_roundtrip():
    m = HashMap()
    m.set("a", 1)
    assert m.get("a") == 1


def test_get_missing_key_returns_none_by_default():
    m = HashMap()
    assert m.get("missing") is None


def test_get_missing_key_returns_custom_default():
    m = HashMap()
    assert m.get("missing", "fallback") == "fallback"


def test_set_overwrites_existing_key():
    m = HashMap()
    m.set("a", 1)
    m.set("a", 2)
    assert m.get("a") == 2
    assert m.size() == 1


def test_size_starts_at_zero():
    assert HashMap().size() == 0


def test_size_tracks_distinct_keys():
    m = HashMap()
    m.set("a", 1)
    m.set("b", 2)
    m.set("a", 99)  # overwrite, not a new key
    assert m.size() == 2


def test_integer_keys_including_negative():
    m = HashMap()
    m.set(5, "five")
    m.set(-5, "neg five")
    m.set(0, "zero")
    assert m.get(5) == "five"
    assert m.get(-5) == "neg five"
    assert m.get(0) == "zero"


def test_mixed_int_and_string_keys_coexist():
    m = HashMap()
    m.set(1, "int one")
    m.set("1", "string one")
    assert m.get(1) == "int one"
    assert m.get("1") == "string one"
    assert m.size() == 2


def test_delete_removes_key_and_reports_true():
    m = HashMap()
    m.set("a", 1)
    assert m.delete("a") is True
    assert m.get("a") is None
    assert m.size() == 0


def test_delete_missing_key_returns_false():
    m = HashMap()
    assert m.delete("missing") is False


def test_delete_then_reinsert():
    m = HashMap()
    m.set("a", 1)
    m.delete("a")
    m.set("a", 2)
    assert m.get("a") == 2
    assert m.size() == 1


def test_keys_returns_every_key_no_particular_order():
    m = HashMap()
    for k in ("a", "b", "c"):
        m.set(k, k.upper())
    assert sorted(m.keys()) == ["a", "b", "c"]


def test_keys_empty_map():
    assert HashMap().keys() == []


def test_bucket_count_starts_at_initial_capacity():
    m = HashMap(initial_capacity=4)
    assert m.bucket_count() == 4


def test_resize_grows_bucket_count_and_preserves_entries():
    m = HashMap(initial_capacity=4)
    initial_buckets = m.bucket_count()

    for i in range(20):
        m.set(f"key{i}", i)

    assert m.bucket_count() > initial_buckets
    for i in range(20):
        assert m.get(f"key{i}") == i
    assert m.size() == 20


def test_resize_never_triggered_by_pure_overwrites():
    m = HashMap(initial_capacity=8)
    m.set("a", 1)
    buckets_before = m.bucket_count()
    for _ in range(50):
        m.set("a", "overwritten")
    assert m.bucket_count() == buckets_before


def test_many_mixed_operations_stay_consistent():
    # 10_000 mixed set/get/delete operations against a plain-dict oracle.
    m = HashMap()
    oracle: dict[int, int] = {}
    rng = random.Random(7)

    for _ in range(10_000):
        key = rng.randint(0, 999)
        op = rng.choice(["set", "delete"])
        if op == "set":
            value = rng.randint(0, 1_000_000)
            m.set(key, value)
            oracle[key] = value
        else:
            deleted = m.delete(key)
            assert deleted == (key in oracle)
            oracle.pop(key, None)

    assert m.size() == len(oracle)
    for key, value in oracle.items():
        assert m.get(key) == value
    assert sorted(m.keys()) == sorted(oracle.keys())
