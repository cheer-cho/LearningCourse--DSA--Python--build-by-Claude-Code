from checkpoint_19 import best_feature_set, bundle_ways, is_fair_split, slogan_similarity


def test_best_feature_set_classic_knapsack():
    result = best_feature_set([1, 3, 4, 5], [1, 4, 5, 7], 7)
    assert sorted(result) == [1, 2]


def test_best_feature_set_zero_budget():
    assert best_feature_set([1, 2], [10, 20], 0) == []


def test_best_feature_set_no_features():
    assert best_feature_set([], [], 10) == []


def test_best_feature_set_single_feature_fits():
    assert best_feature_set([3], [10], 5) == [0]


def test_best_feature_set_single_feature_does_not_fit():
    assert best_feature_set([10], [42], 5) == []


def test_best_feature_set_all_features_fit():
    result = best_feature_set([1, 1, 1], [5, 5, 5], 10)
    assert sorted(result) == [0, 1, 2]


def test_best_feature_set_reconstruction_matches_optimal_value():
    costs = [2, 3, 4, 5]
    impacts = [3, 4, 5, 6]
    budget = 5
    chosen = best_feature_set(costs, impacts, budget)
    total_impact = sum(impacts[i] for i in chosen)
    total_cost = sum(costs[i] for i in chosen)
    assert total_cost <= budget
    assert total_impact == 7  # either items 0+1 (cost 5, impact 7) or item 2 (cost 4, impact 5)


def test_best_feature_set_efficiency_large_input():
    # 50 features, budget 10_000: brute-force over 2**50 subsets is
    # impossible, but the O(n * budget) table finishes instantly.
    n = 50
    costs = [(i % 10) + 1 for i in range(n)]
    impacts = [(i % 7) + 1 for i in range(n)]
    result = best_feature_set(costs, impacts, 10_000)
    assert all(0 <= i < n for i in result)
    assert len(set(result)) == len(result)
    assert sum(costs[i] for i in result) <= 10_000


def test_slogan_similarity_classic_example():
    assert slogan_similarity("kitten", "sitting") == 3


def test_slogan_similarity_identical():
    assert slogan_similarity("launch", "launch") == 0


def test_slogan_similarity_empty_a():
    assert slogan_similarity("", "abc") == 3


def test_slogan_similarity_empty_b():
    assert slogan_similarity("xyz", "") == 3


def test_bundle_ways_classic_example():
    assert bundle_ways([1, 2, 5], 5) == 4


def test_bundle_ways_impossible():
    assert bundle_ways([2], 3) == 0


def test_bundle_ways_zero_order_is_one_way():
    assert bundle_ways([1, 2], 0) == 1


def test_bundle_ways_no_pack_sizes_zero_order():
    assert bundle_ways([], 0) == 1


def test_bundle_ways_no_pack_sizes_positive_order():
    assert bundle_ways([], 3) == 0


def test_is_fair_split_classic_true():
    assert is_fair_split([1, 5, 11, 5]) is True


def test_is_fair_split_classic_false():
    assert is_fair_split([1, 2, 3, 5]) is False


def test_is_fair_split_two_equal_numbers():
    assert is_fair_split([2, 2]) is True


def test_is_fair_split_odd_total():
    assert is_fair_split([1, 2]) is False


def test_is_fair_split_single_element():
    assert is_fair_split([4]) is False


def test_is_fair_split_empty_is_vacuously_true():
    assert is_fair_split([]) is True
