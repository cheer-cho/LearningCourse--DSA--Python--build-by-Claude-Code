# Checkpoint 09 — Tournament board
#
# A player record is (name, score, wins, joined) — joined is an ISO date
# string ("2024-03-01") so plain string comparison already sorts it
# chronologically. Build the three board operations below: a full
# ranking (multi-key stable sort), a fast top-k lookup (quickselect,
# not a full sort), and a grade bucketing (counting sort). This pulls
# together every idea from the module.
# Run: uv run pytest 09-sorting -k checkpoint

PlayerRecord = tuple[str, int, int, str]  # (name, score, wins, joined)


def rank_players(records: list[PlayerRecord]) -> list[PlayerRecord]:
    """Return a NEW list of `records` ranked for the leaderboard:
    score DESCENDING, ties broken by wins DESCENDING, remaining ties
    broken by `joined` ASCENDING (earlier join date ranks higher).
    Must be STABLE for any records that tie on all three keys. Does
    not modify `records`.

    rank_players([
        ("Ada", 80, 3, "2024-02-01"),
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 80, 5, "2024-01-15"),
    ]) -> [
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 80, 5, "2024-01-15"),
        ("Ada", 80, 3, "2024-02-01"),
    ]

    Target complexity: O(n log n) time, O(n) space.
    """
    raise NotImplementedError


def top_k_scores(records: list[PlayerRecord], k: int) -> list[PlayerRecord]:
    """Return the top `k` records ranked the same way as `rank_players`
    (score desc, wins desc, joined asc), WITHOUT fully sorting all n
    records first — partition out the top-k group (quickselect idea),
    then only sort that small group. `records` has at least `k`
    elements. Does not modify `records`.

    top_k_scores([
        ("Ada", 80, 3, "2024-02-01"),
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 80, 5, "2024-01-15"),
    ], 2) -> [
        ("Bo", 90, 1, "2024-01-01"),
        ("Cy", 80, 5, "2024-01-15"),
    ]

    Target complexity: O(n) average time to select the top-k group,
    plus O(k log k) to order that group — never O(n log n) overall.
    """
    raise NotImplementedError


def bucket_by_grade(scores: list[int]) -> dict[str, list[int]]:
    """Group `scores` (each an int in [0, 100]) into letter-grade
    buckets using a counting-sort-style single pass (no comparisons):
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59. Each bucket's
    scores are sorted ascending. Always returns all five keys, in the
    order "A", "B", "C", "D", "F", even if a bucket is empty.

    bucket_by_grade([95, 72, 81, 60, 40, 91]) -> {
        "A": [91, 95], "B": [81], "C": [72], "D": [60], "F": [40],
    }

    Target complexity: O(n + 101) time, O(n) space.
    """
    raise NotImplementedError
