import math

from checkpoint_10 import find_version, first_bad_build, min_test_rigs


def test_first_bad_build_typical():
    assert first_bad_build(5, lambda v: v >= 3) == 3


def test_first_bad_build_first_build_is_bad():
    assert first_bad_build(1, lambda v: v >= 1) == 1


def test_first_bad_build_only_last_is_bad():
    assert first_bad_build(10, lambda v: v >= 10) == 10


def test_first_bad_build_calls_stay_logarithmic():
    n = 100_000
    threshold = 73_991
    calls = 0

    def is_bad(v: int) -> bool:
        nonlocal calls
        calls += 1
        return v >= threshold

    result = first_bad_build(n, is_bad)
    assert result == threshold
    assert calls <= math.floor(math.log2(n)) + 2


def test_min_test_rigs_typical():
    assert min_test_rigs([1, 2, 3, 4, 5], 6) == 3


def test_min_test_rigs_all_fit_one_rig():
    assert min_test_rigs([1, 1, 1, 1], 4) == 1


def test_min_test_rigs_one_rig_per_load():
    assert min_test_rigs([5, 5, 5], 5) == 3


def test_min_test_rigs_single_load():
    assert min_test_rigs([7], 7) == 1


def test_min_test_rigs_large_input_is_fast():
    loads = [3] * 50_000
    assert min_test_rigs(loads, 9) == math.ceil(50_000 * 3 / 9)


def test_find_version_repeated_tag():
    assert find_version(["v1", "v2", "v2", "v2", "v3"], "v2") == (1, 3)


def test_find_version_missing_tag():
    assert find_version(["v1", "v2", "v3"], "v9") == (-1, -1)


def test_find_version_empty_list():
    assert find_version([], "v1") == (-1, -1)


def test_find_version_single_occurrence():
    assert find_version(["v1", "v2", "v3"], "v2") == (1, 1)


def test_find_version_all_same_tag():
    tags = ["v1"] * 6
    assert find_version(tags, "v1") == (0, 5)


def test_find_version_first_and_last_elements():
    tags = ["v1", "v1", "v2", "v3", "v3"]
    assert find_version(tags, "v1") == (0, 1)
    assert find_version(tags, "v3") == (3, 4)


def test_find_version_large_list_is_fast():
    tags = sorted(f"v{i // 4:06d}" for i in range(400_000))
    first, last = find_version(tags, "v012345")
    assert last - first + 1 == 4
