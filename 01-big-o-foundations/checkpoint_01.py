# Checkpoint 01 — Performance Review
#
# You're doing a "performance review" of some analytics code: find the
# most common word in a log, find the first value that repeats, and
# classify the time complexity of a few snippets -- including the two
# functions you just wrote.
# Run: uv run pytest 01-big-o-foundations -k checkpoint

# Three more snippets to classify, alongside your own two functions
# below. `arr` has length n; `matrix` is an n x n grid.
#
# reverse_and_scan:
#     def f(arr):
#         arr2 = arr[::-1]
#         for x in arr2:
#             print(x)
#
# binary_search_twice:
#     def f(arr, t1, t2):
#         binary_search(arr, t1)
#         binary_search(arr, t2)
#
# matrix_double_loop:
#     def f(matrix):
#         total = 0
#         for row in matrix:
#             for val in row:
#                 total += val
#         return total

ANSWER_SET = {"O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(2^n)"}


def most_common(words: list[str]) -> str:
    """Return the most frequent word in `words`. Ties are broken by
    first occurrence: among words tied for the highest count, return
    whichever one appears earliest in `words`.

    most_common(["a", "b", "a", "c", "b", "a"]) -> "a"
    most_common(["b", "a", "a", "b"]) -> "b"   # tied at 2, b appears first

    `words` has at least one element.

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


def first_repeated(nums: list[int]) -> int | None:
    """Scanning `nums` left to right, return the first value you
    encounter for a SECOND time. Return None if every value is unique.

    first_repeated([2, 5, 3, 5, 2]) -> 5
        # 5's second occurrence (index 3) comes before 2's (index 4)
    first_repeated([1, 2, 3]) -> None

    Target complexity: O(n) time, O(n) space.
    """
    raise NotImplementedError


def complexity_report() -> dict[str, str]:
    """Return a dict answering 5 classification questions with an
    answer from ANSWER_SET:

    - "most_common_time": time complexity of most_common above.
    - "first_repeated_time": time complexity of first_repeated above.
    - "reverse_and_scan": time complexity of that snippet.
    - "binary_search_twice": time complexity of that snippet.
    - "matrix_double_loop": time complexity of that snippet.
    """
    raise NotImplementedError
