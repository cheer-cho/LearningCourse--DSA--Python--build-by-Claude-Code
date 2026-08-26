import random
import time

from ex05_merge_count_inversions import count_inversions


def brute_force_inversions(nums: list[int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
    return count


def test_sorted_list_has_zero_inversions():
    assert count_inversions([1, 2, 3]) == 0


def test_empty_and_single_element():
    assert count_inversions([]) == 0
    assert count_inversions([5]) == 0


def test_reverse_sorted_is_maximal():
    assert count_inversions([3, 2, 1]) == 3


def test_typical_small_case():
    assert count_inversions([2, 4, 1, 3, 5]) == 3


def test_all_equal_elements_have_no_inversions():
    assert count_inversions([4, 4, 4, 4]) == 0


def test_does_not_mutate_input():
    nums = [3, 1, 2]
    count_inversions(nums)
    assert nums == [3, 1, 2]


def test_matches_brute_force_on_random_lists():
    rng = random.Random(42)
    for _ in range(20):
        nums = [rng.randint(-50, 50) for _ in range(rng.randint(0, 60))]
        assert count_inversions(nums) == brute_force_inversions(nums)


def test_efficiency_on_reverse_sorted_hundred_thousand():
    # A reverse-sorted list of size n has the maximum possible n*(n-1)/2
    # inversions. An O(n^2) pairwise scan would need ~5*10^9 comparisons
    # here and never finish in a reasonable time; O(n log n) breezes
    # through it.
    n = 100_000
    nums = list(range(n, 0, -1))

    start = time.perf_counter()
    result = count_inversions(nums)
    elapsed = time.perf_counter() - start

    assert result == n * (n - 1) // 2
    assert elapsed < 5.0  # generous ceiling, never a tight wall-clock check
