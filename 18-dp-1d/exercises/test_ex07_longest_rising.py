from ex07_longest_rising import lis_length, lis_length_fast


def sawtooth(block_size: int, num_blocks: int) -> list[int]:
    """[1..block_size] repeated `num_blocks` times. The best strictly
    increasing run is exactly one full ascending block (length
    block_size) -- crossing into the next block always drops back down
    to 1, which can never extend a run past its own block's top."""
    return list(range(1, block_size + 1)) * num_blocks


# --- lis_length: O(n^2) reference ---


def test_lis_length_empty():
    assert lis_length([]) == 0


def test_lis_length_single_element():
    assert lis_length([5]) == 1


def test_lis_length_classic_example():
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_lis_length_all_equal_values_stay_length_one():
    assert lis_length([7, 7, 7, 7]) == 1


def test_lis_length_already_strictly_increasing():
    assert lis_length([1, 2, 3, 4, 5]) == 5


def test_lis_length_strictly_decreasing():
    assert lis_length([5, 4, 3, 2, 1]) == 1


def test_lis_length_sawtooth():
    assert lis_length(sawtooth(6, 5)) == 6


# --- lis_length_fast: must match the O(n^2) reference everywhere ---


def test_fast_matches_slow_on_classic_example():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert lis_length_fast(nums) == lis_length(nums) == 4


def test_fast_matches_slow_on_mixed_duplicates():
    nums = [0, 1, 0, 3, 2, 3]
    assert lis_length_fast(nums) == lis_length(nums) == 4


def test_fast_matches_slow_across_small_sawtooth_scale():
    nums = sawtooth(20, 10)
    assert lis_length_fast(nums) == lis_length(nums) == 20


def test_fast_handles_empty_and_single():
    assert lis_length_fast([]) == 0
    assert lis_length_fast([9]) == 1


def test_efficiency_large_input_distinguishes_fast_from_naive():
    # n = 100_000: the O(n^2) reference (10^10 comparisons) is
    # infeasible here -- only lis_length_fast is exercised at this
    # scale. The sawtooth pattern keeps the answer non-trivial (not
    # just "fully sorted" or "fully reversed") while staying exactly
    # computable: one full ascending block, length 200.
    nums = sawtooth(block_size=200, num_blocks=500)
    assert len(nums) == 100_000
    assert lis_length_fast(nums) == 200
