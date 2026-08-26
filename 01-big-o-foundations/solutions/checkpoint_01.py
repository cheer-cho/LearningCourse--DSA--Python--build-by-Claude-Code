ANSWER_SET = {"O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(2^n)"}


def most_common(words: list[str]) -> str:
    # Pattern: counting with a dict. O(n) time, O(n) space.
    # Dict iteration order is insertion order, i.e. first-occurrence
    # order, so max() by count naturally returns the first word to
    # reach the highest count on a tie.
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return max(counts, key=lambda w: counts[w])


def first_repeated(nums: list[int]) -> int | None:
    # Pattern: "have I seen this before?" via a hash set, one pass.
    # O(n) time, O(n) space. The first repeat found while scanning left
    # to right is, by construction, the earliest second-occurrence.
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return None


def complexity_report() -> dict[str, str]:
    return {
        "most_common_time": "O(n)",
        "first_repeated_time": "O(n)",
        "reverse_and_scan": "O(n)",
        "binary_search_twice": "O(log n)",
        "matrix_double_loop": "O(n^2)",
    }
