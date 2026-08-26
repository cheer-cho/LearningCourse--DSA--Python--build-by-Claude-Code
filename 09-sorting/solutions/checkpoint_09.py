import random

PlayerRecord = tuple[str, int, int, str]  # (name, score, wins, joined)


def _rank_key(record: PlayerRecord) -> tuple[int, int, str]:
    _name, score, wins, joined = record
    return (-score, -wins, joined)  # negate for "descending" on a tuple sort


def rank_players(records: list[PlayerRecord]) -> list[PlayerRecord]:
    # Pattern: multi-key stable sort via a single tuple key (score desc,
    # wins desc, joined asc) — Python's sort is stable, so any remaining
    # full ties keep their original order for free. Complexity:
    # O(n log n) time, O(n) space.
    return sorted(records, key=_rank_key)


def top_k_scores(records: list[PlayerRecord], k: int) -> list[PlayerRecord]:
    # Pattern: quickselect — partition on the same rank key to isolate
    # the top-k group in O(n) average time, then sort only that small
    # group (O(k log k)) instead of the full n. Complexity: O(n) average
    # + O(k log k), never O(n log n) overall.
    records = records[:]  # partition in a scratch copy; never mutate the caller's list
    n = len(records)
    lo, hi = 0, n - 1
    target_idx = k - 1  # after partitioning, indices [0, k) are the top k

    while lo < hi:
        p = _partition(records, lo, hi)
        if p == target_idx:
            break
        if p < target_idx:
            lo = p + 1
        else:
            hi = p - 1

    top_group = records[:k]
    return sorted(top_group, key=_rank_key)


def _partition(records: list[PlayerRecord], lo: int, hi: int) -> int:
    pivot_idx = random.randint(lo, hi)
    records[pivot_idx], records[hi] = records[hi], records[pivot_idx]
    pivot_key = _rank_key(records[hi])

    i = lo - 1
    for j in range(lo, hi):
        if _rank_key(records[j]) < pivot_key:
            i += 1
            records[i], records[j] = records[j], records[i]
    records[i + 1], records[hi] = records[hi], records[i + 1]
    return i + 1


def bucket_by_grade(scores: list[int]) -> dict[str, list[int]]:
    # Pattern: counting sort restricted to a fixed 0..100 range, grouped
    # into 5 letter-grade buckets by a single pass over the count array.
    # Applies here because scores are bounded ints. Complexity:
    # O(n + 101) time, O(n) space.
    counts = [0] * 101
    for score in scores:
        counts[score] += 1

    buckets: dict[str, list[int]] = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for score in range(101):
        if counts[score] == 0:
            continue
        grade = _grade_for(score)
        buckets[grade].extend([score] * counts[score])
    return buckets


def _grade_for(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
