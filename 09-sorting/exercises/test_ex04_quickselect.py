import random

from ex04_quickselect import kth_largest


def test_kth_largest_first_is_max():
    assert kth_largest([3, 1, 4, 1, 5], 1) == 5


def test_kth_largest_last_is_min():
    assert kth_largest([3, 1, 4, 1, 5], 5) == 1


def test_kth_largest_middle():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_kth_largest_single_element():
    assert kth_largest([7], 1) == 7


def test_kth_largest_duplicates():
    assert kth_largest([2, 2, 2, 1], 1) == 2
    assert kth_largest([2, 2, 2, 1], 4) == 1


def test_kth_largest_negatives():
    assert kth_largest([-5, -1, -3], 1) == -1


def test_kth_largest_does_not_call_sorted(monkeypatch):
    # Guards against the shortcut that defeats the point of the
    # exercise: quickselect must partition, never fully sort.
    import ex04_quickselect as mod

    def _blocked(*_args, **_kwargs):
        raise AssertionError("kth_largest must not call sorted() — partition instead")

    monkeypatch.setattr(mod, "sorted", _blocked, raising=False)
    nums = list(range(50))
    random.seed(3)
    random.shuffle(nums)
    assert mod.kth_largest(nums, 1) == 49
    assert mod.kth_largest(nums, 50) == 0


def test_kth_largest_efficiency_large_input():
    # n = 200_000, generous op environment: correctness at scale, not a
    # tight timing assertion. A full sort would also pass this
    # correctness check — the sorted() guard above is what enforces the
    # partition-based approach.
    random.seed(5)
    nums = [random.randint(0, 5_000_000) for _ in range(200_000)]
    expected_max = max(nums)
    expected_min = min(nums)
    assert kth_largest(nums, 1) == expected_max
    assert kth_largest(nums, len(nums)) == expected_min
