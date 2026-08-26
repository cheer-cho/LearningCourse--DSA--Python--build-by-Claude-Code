from functools import cmp_to_key


def largest_concat_number(nums: list[int]) -> str:
    # Pattern: custom comparator — order candidates by which
    # concatenation (a+b vs b+a) is bigger. Applies here because "biggest
    # concatenation" isn't a natural ascending/descending order on the
    # numbers themselves. Complexity: O(n log n) time (sort with an
    # O(len) comparator), O(n) space.
    strs = [str(n) for n in nums]

    def compare(a: str, b: str) -> int:
        if a + b > b + a:
            return -1  # a should come first
        if a + b < b + a:
            return 1
        return 0

    strs.sort(key=cmp_to_key(compare))
    result = "".join(strs)
    # All-zero input (e.g. ["0", "0"]) would otherwise concatenate to
    # "00" — strip the leading zeros down to a single "0". An empty
    # input has no digits to collapse, so it stays "".
    if result and result.lstrip("0") == "":
        return "0"
    return result


def sort_by_frequency(nums: list[int]) -> list[int]:
    # Pattern: multi-key sort via a tuple key — primary key frequency
    # ascending, secondary key value descending. Applies here because
    # "least frequent first, ties broken by value" is exactly two
    # ordered comparisons. Complexity: O(n log n) time, O(n) space.
    counts: dict[int, int] = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    return sorted(nums, key=lambda n: (counts[n], -n))


def relative_order(nums: list[int], order: list[int]) -> list[int]:
    # Pattern: sort by an external rank via a key function — unknown
    # values get a rank past every known one, so they naturally sort
    # last (then break ties among themselves by value). Complexity:
    # O(n log n + m) time (m = len(order), for building the rank map),
    # O(n + m) space.
    rank = {value: i for i, value in enumerate(order)}
    unknown_rank = len(order)
    return sorted(nums, key=lambda n: (rank.get(n, unknown_rank), n))
