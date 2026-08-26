# Scenario: you're reviewing 8 short functions in a teammate's PR and
# need to label each one with its time complexity before approving it.
# Concepts: reading complexity from code (sequential = add, nested =
# multiply, halving = log), recursion that branches = exponential.
# Run: uv run pytest 01-big-o-foundations -k ex01

# The 8 snippets under review. `arr` always has length n. Read each one
# and decide its time complexity — don't run them, just reason about
# the shape of the work.
#
# constant_lookup:
#     def f(arr):
#         return arr[0] + arr[-1]
#
# print_all:
#     def f(arr):
#         for x in arr:
#             print(x)
#
# binary_search_style:
#     def f(arr, target):
#         lo, hi = 0, len(arr) - 1
#         while lo <= hi:
#             mid = (lo + hi) // 2
#             if arr[mid] == target:
#                 return mid
#             elif arr[mid] < target:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#         return -1
#
# two_separate_loops:
#     def f(arr):
#         total = 0
#         for x in arr:
#             total += x
#         for x in arr:
#             print(x)
#         return total
#
# sort_then_scan:
#     def f(arr):
#         arr2 = sorted(arr)
#         for x in arr2:
#             print(x)
#         return arr2
#
# nested_loop_all_pairs:
#     def f(arr):
#         count = 0
#         for i in arr:
#             for j in arr:
#                 count += 1
#         return count
#
# triangular_nested_loop:
#     def f(arr):
#         count = 0
#         for i in range(len(arr)):
#             for j in range(i + 1, len(arr)):
#                 count += 1
#         return count
#
# recursive_subsets:
#     def f(arr):
#         if not arr:
#             return [[]]
#         first, rest = arr[0], arr[1:]
#         without_first = f(rest)
#         with_first = [[first] + s for s in without_first]
#         return without_first + with_first

# Pick every answer from this fixed set — use the strings exactly as written.
ANSWER_SET = {"O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(2^n)"}


def classify_snippets() -> dict[str, str]:
    """Return a dict mapping each snippet name above to its time
    complexity, chosen from ANSWER_SET.

    Keys (exactly these 8): "constant_lookup", "print_all",
    "binary_search_style", "two_separate_loops", "sort_then_scan",
    "nested_loop_all_pairs", "triangular_nested_loop",
    "recursive_subsets".

    classify_snippets()["constant_lookup"] -> "O(1)"
    classify_snippets()["nested_loop_all_pairs"] -> "O(n^2)"
    """
    raise NotImplementedError
