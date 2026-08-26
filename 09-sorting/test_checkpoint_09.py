import random

from checkpoint_09 import bucket_by_grade, rank_players, top_k_scores

# --- rank_players ------------------------------------------------------------


def test_rank_players_multi_key_order():
    records = [
        ("Ada", 80, 3, "2024-02-01"),
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 80, 5, "2024-01-15"),
    ]
    assert rank_players(records) == [
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 80, 5, "2024-01-15"),
        ("Ada", 80, 3, "2024-02-01"),
    ]


def test_rank_players_empty():
    assert rank_players([]) == []


def test_rank_players_single_record():
    records = [("Solo", 50, 0, "2024-01-01")]
    assert rank_players(records) == records


def test_rank_players_full_tie_is_stable():
    records = [
        ("First", 10, 1, "2024-01-01"),
        ("Second", 10, 1, "2024-01-01"),
    ]
    # Every key ties — a stable sort must preserve input order.
    assert rank_players(records) == records


def test_rank_players_does_not_mutate_input():
    records = [("Ada", 80, 3, "2024-02-01"), ("Bo", 90, 1, "2024-01-01")]
    original = list(records)
    rank_players(records)
    assert records == original


# --- top_k_scores --------------------------------------------------------------


def test_top_k_scores_matches_rank_players_prefix():
    records = [
        ("Ada", 80, 3, "2024-02-01"),
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 80, 5, "2024-01-15"),
        ("Di", 40, 0, "2024-03-01"),
    ]
    assert top_k_scores(records, 2) == rank_players(records)[:2]


def test_top_k_scores_k_equals_n():
    records = [("Ada", 80, 3, "2024-02-01"), ("Bo", 90, 1, "2024-01-01")]
    assert top_k_scores(records, 2) == rank_players(records)


def test_top_k_scores_k_equals_one():
    records = [
        ("Ada", 80, 3, "2024-02-01"),
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 60, 0, "2024-01-15"),
    ]
    assert top_k_scores(records, 1) == [("Bo", 90, 1, "2024-01-01")]


def test_top_k_scores_does_not_mutate_input():
    records = [("Ada", 80, 3, "2024-02-01"), ("Bo", 90, 1, "2024-01-01")]
    original = list(records)
    top_k_scores(records, 1)
    assert records == original


def test_top_k_scores_efficiency_partitions_instead_of_full_sort(monkeypatch):
    # n = 200_000, k tiny: enforce "no full sort of all n" behaviorally
    # by spying on every sorted() call's input size — none should ever
    # see the full n records (only the small partitioned-out group).
    import checkpoint_09 as mod

    real_sorted = sorted
    call_sizes: list[int] = []

    def spy(iterable, *args, **kwargs):
        items = list(iterable)
        call_sizes.append(len(items))
        return real_sorted(items, *args, **kwargs)

    random.seed(13)
    n = 200_000
    records = [
        (f"p{i}", random.randint(0, 1_000_000), random.randint(0, 50), "2024-01-01")
        for i in range(n)
    ]
    k = 10

    monkeypatch.setattr(mod, "sorted", spy, raising=False)
    result = top_k_scores(records, k)
    monkeypatch.undo()  # restore the real sorted() before computing the expected value

    assert len(result) == k
    assert result == rank_players(records)[:k]
    assert all(size < n for size in call_sizes), (
        f"top_k_scores called sorted() on up to {max(call_sizes, default=0)} "
        f"items — it must never sort all {n}"
    )


# --- bucket_by_grade -----------------------------------------------------------


def test_bucket_by_grade_basic():
    result = bucket_by_grade([95, 72, 81, 60, 40, 91])
    assert result == {
        "A": [91, 95],
        "B": [81],
        "C": [72],
        "D": [60],
        "F": [40],
    }


def test_bucket_by_grade_empty():
    assert bucket_by_grade([]) == {"A": [], "B": [], "C": [], "D": [], "F": []}


def test_bucket_by_grade_boundaries():
    result = bucket_by_grade([100, 90, 89, 80, 79, 70, 69, 60, 59, 0])
    assert result == {
        "A": [90, 100],
        "B": [80, 89],
        "C": [70, 79],
        "D": [60, 69],
        "F": [0, 59],
    }


def test_bucket_by_grade_sorted_within_bucket():
    result = bucket_by_grade([95, 92, 90, 99])
    assert result["A"] == [90, 92, 95, 99]


def test_bucket_by_grade_all_same_grade():
    result = bucket_by_grade([61, 65, 60, 69])
    assert result == {"A": [], "B": [], "C": [], "D": [60, 61, 65, 69], "F": []}
